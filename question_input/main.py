"""CharaNas Question Input bot — add Short MCQ / cases / PDFs / books into department bots."""

from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

try:
    from catalog import (
        CASE_DIFFICULTIES,
        CONTENT_TYPES,
        DEPARTMENTS,
        DIFFICULTIES,
        department_stages,
        specialty_label,
        stage_curricula,
        stage_label,
        uses_stages,
    )
    from dedupe import DuplicateQuestionError, existing_stem_samples, filter_unique_batch, iter_bank_questions
    from perplexity_gen import (
        PerplexityError,
        allocate_mix,
        configured as perplexity_configured,
        generate_batch,
        mix_summary,
        single_distribution,
    )
    from storage import append_book, append_case, append_short_mcq, bank_counts, load_bank, save_pdf
except ImportError:  # pragma: no cover
    from question_input.catalog import (
        CASE_DIFFICULTIES,
        CONTENT_TYPES,
        DEPARTMENTS,
        DIFFICULTIES,
        department_stages,
        specialty_label,
        stage_curricula,
        stage_label,
        uses_stages,
    )
    from question_input.perplexity_gen import (
        PerplexityError,
        allocate_mix,
        configured as perplexity_configured,
        generate_batch,
        mix_summary,
        single_distribution,
    )
    from question_input.dedupe import (
        DuplicateQuestionError,
        existing_stem_samples,
        filter_unique_batch,
        iter_bank_questions,
    )
    from question_input.storage import (
        append_book,
        append_case,
        append_short_mcq,
        bank_counts,
        load_bank,
        save_pdf,
    )

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(Path(__file__).resolve().parent / "bot.log"),
    ],
)
log = logging.getLogger("charanas-input-bot")

load_dotenv(Path(__file__).resolve().parent / ".env")
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

TOKEN = (os.getenv("QUESTION_INPUT_BOT_TOKEN") or os.getenv("INPUT_BOT_TOKEN") or "").strip()
ADMIN_IDS = {
    int(x.strip())
    for x in (os.getenv("INPUT_ADMIN_IDS") or "").split(",")
    if x.strip().isdigit()
}


def _allowed(user_id: int | None) -> bool:
    if user_id is None:
        return False
    if not ADMIN_IDS:
        return True
    return user_id in ADMIN_IDS


def _kb(rows: list[list[tuple[str, str]]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text, callback_data=data) for text, data in row] for row in rows]
    )


def clear_flow(context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("flow", None)


def flow(context: ContextTypes.DEFAULT_TYPE) -> dict:
    return context.user_data.setdefault("flow", {})


async def safe_edit_or_reply(update: Update, text: str, reply_markup=None) -> None:
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text(
                text, reply_markup=reply_markup, parse_mode="Markdown"
            )
            return
        except Exception:
            pass
        await update.callback_query.message.reply_text(
            text, reply_markup=reply_markup, parse_mode="Markdown"
        )
        return
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not _allowed(user.id if user else None):
        await update.message.reply_text(
            "This input bot is restricted. Ask the admin to add your Telegram user id to `INPUT_ADMIN_IDS`."
        )
        return
    clear_flow(context)
    rows = [[(label, f"type:{key}")] for key, label in CONTENT_TYPES]
    rows.append([("Cancel", "cancel")])
    await update.message.reply_text(
        "CharaNas *Question Input*\n\n"
        "What do you want to add into a department bot?\n\n"
        "• *Generate Short MCQs (auto-save)* — Perplexity writes questions into the bank\n"
        "• *Type Short MCQs myself* — you enter stem/options one by one",
        reply_markup=_kb(rows),
        parse_mode="Markdown",
    )


async def cmd_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    clear_flow(context)
    await update.message.reply_text("Cancelled. Send /start to begin again.")


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pplx = "ready" if perplexity_configured() else "missing PERPLEXITY_API_KEY"
    await update.message.reply_text(
        "Use /start to add content.\n\n"
        "Manual flow: Short MCQ / Case / PDF / Book → department → specialty → enter items.\n\n"
        "Perplexity flow:\n"
        "1) Generate Short MCQs (Perplexity)\n"
        "2) Form: department → stage/curriculum → count → topic → difficulty mix\n"
        "3) API generates strict JSON → validated → saved into the bank automatically\n\n"
        f"Perplexity status: {pplx}\n"
        "Use /cancel to stop."
    )


async def show_departments(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    rows = [[(dep["label"], f"dept:{key}")] for key, dep in DEPARTMENTS.items()]
    rows.append([("⟵ Back", "back:type"), ("Cancel", "cancel")])
    f = flow(context)
    ctype = dict(CONTENT_TYPES).get(f.get("content_type", ""), "content")
    await safe_edit_or_reply(
        update,
        f"*{ctype}*\n\nWhich department should receive this?",
        reply_markup=_kb(rows),
    )


async def show_stages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    dep = DEPARTMENTS[f["department"]]
    rows = [[(label, f"stage:{key}")] for key, label, _curricula in department_stages(f["department"])]
    rows.append([("⟵ Back", "back:dept"), ("Cancel", "cancel")])
    await safe_edit_or_reply(
        update,
        f"*{dep['label']}* — {dict(CONTENT_TYPES).get(f.get('content_type'), '')}\n\n"
        "Choose the *stage level*:",
        reply_markup=_kb(rows),
    )


async def show_curricula(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    dep = DEPARTMENTS[f["department"]]
    stage_key = f.get("stage") or ""
    curricula = stage_curricula(f["department"], stage_key)
    rows = []
    row = []
    for key, label in curricula:
        # Telegram button text max ~64 chars; keep labels readable
        btn = label if len(label) <= 60 else label[:57] + "…"
        row.append((btn, f"spec:{key}"))
        if len(row) == 1:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([("⟵ Back", "back:stage"), ("Cancel", "cancel")])
    s_label = stage_label(f["department"], stage_key)
    await safe_edit_or_reply(
        update,
        f"*{dep['label']} → {s_label}*\n"
        f"{dict(CONTENT_TYPES).get(f.get('content_type'), '')}\n\n"
        "Choose the *curriculum*:",
        reply_markup=_kb(rows),
    )


async def show_specialties(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    if uses_stages(f["department"]):
        await show_stages(update, context)
        return
    dep = DEPARTMENTS[f["department"]]
    specs = dep["specialties"]
    rows = []
    row = []
    for key, label in specs:
        row.append((label, f"spec:{key}"))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([("⟵ Back", "back:dept"), ("Cancel", "cancel")])
    await safe_edit_or_reply(
        update,
        f"*{dep['label']}* — {dict(CONTENT_TYPES).get(f.get('content_type'), '')}\n\n"
        "Choose the specialty:",
        reply_markup=_kb(rows),
    )


def _back_to_target_after_specialty(department: str) -> str:
    return "back:curr" if uses_stages(department) else "back:spec"


async def show_difficulty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    diffs = CASE_DIFFICULTIES if f.get("content_type") == "case_based" else DIFFICULTIES
    rows = [[(label, f"diff:{key}")] for key, label in diffs]
    rows.append([("⟵ Back", _back_to_target_after_specialty(f["department"])), ("Cancel", "cancel")])
    await safe_edit_or_reply(
        update,
        "Choose difficulty for these items:",
        reply_markup=_kb(rows),
    )


def _path_label(f: dict) -> str:
    dep = DEPARTMENTS[f["department"]]
    spec = specialty_label(f["department"], f.get("specialty", ""))
    if uses_stages(f["department"]) and f.get("stage"):
        return f"{dep['label']} → {stage_label(f['department'], f['stage'])} → {spec}"
    return f"{dep['label']} → {spec}"


def _is_mcq_type(ctype: str | None) -> bool:
    return ctype in {"short_mcq", "perplexity_mcq"}


async def ask_count(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    f["step"] = "count"
    if f.get("content_type") == "perplexity_mcq":
        tip = (
            "How many Short MCQs should Perplexity generate?\n"
            "Send a number from *1* to *20*.\n"
            "They are written into the live bank automatically after generation."
        )
        difficulty_line = ""
    else:
        tip = (
            "How many items will you input now?\n"
            "Send a number from *1* to *50*."
        )
        difficulty_line = f"Difficulty: *{f.get('difficulty', 'n/a')}*\n\n"
    await safe_edit_or_reply(
        update,
        f"*{_path_label(f)}*\n"
        f"{difficulty_line}"
        f"{tip}",
    )


async def ask_perplexity_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    f["step"] = "pplx_topic"
    spec = specialty_label(f["department"], f["specialty"])
    await safe_edit_or_reply(
        update,
        f"*{_path_label(f)}*\n"
        f"Count: *{f['count']}*\n\n"
        f"Send a *topic focus* (e.g. pulpitis diagnosis), or type `skip` to use *{spec}*.",
    )


async def show_distribution_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    f["step"] = "pplx_distribution"
    rows = [[(f"Level {n}", f"pplxlevel:{n}")] for n in range(1, 6)]
    rows.append([("Single difficulty…", "pplxdist:single")])
    rows.append([("⟵ Back", "back:pplx_topic"), ("Cancel", "cancel")])
    topic = f.get("topic") or specialty_label(f["department"], f["specialty"])
    await safe_edit_or_reply(
        update,
        f"*{_path_label(f)}*\n"
        f"Topic: *{topic}*\n"
        f"Count: *{f['count']}*\n\n"
        "Choose the *difficulty distribution*:\n"
        "Levels 1–5 use the same mixes as the study bots, or pick one single difficulty.",
        reply_markup=_kb(rows),
    )


async def show_single_difficulty_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    rows = [[(label, f"pplxdiff:{key}")] for key, label in DIFFICULTIES]
    rows.append([("⟵ Back", "back:pplx_dist"), ("Cancel", "cancel")])
    await safe_edit_or_reply(
        update,
        "Choose one difficulty for all generated questions:",
        reply_markup=_kb(rows),
    )


async def begin_item_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    f["index"] = 0
    f["saved"] = 0
    if f.get("content_type") == "perplexity_mcq":
        await ask_perplexity_topic(update, context)
        return
    await prompt_next_item(update, context)


def _escape_md(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace("*", "\\*")
        .replace("_", "\\_")
        .replace("`", "\\`")
        .replace("[", "\\[")
    )


def _preview_keyboard() -> InlineKeyboardMarkup:
    return _kb(
        [
            [("Publish all", "pplx:publish"), ("Drop this", "pplx:drop")],
            [("Next", "pplx:next"), ("Edit stem", "pplx:edit")],
            [("Discard draft", "pplx:discard")],
        ]
    )


async def show_draft_preview(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    draft = f.get("pplx_draft") or {}
    items = draft.get("questions") or []
    if not items:
        clear_flow(context)
        await safe_edit_or_reply(update, "Draft is empty. Send /start to generate again.")
        return
    idx = min(int(f.get("pplx_index", 0)), len(items) - 1)
    f["pplx_index"] = idx
    f["step"] = "pplx_preview"
    item = items[idx]
    opts = "\n".join(f"{L}) {_escape_md(o)}" for L, o in zip("ABCD", item["options"]))
    dist = mix_summary(draft.get("difficulty_distribution") or {})
    text = (
        f"*Preview {idx + 1}/{len(items)}* — not saved yet\n"
        f"*{_path_label(f)}*\n"
        f"Topic: {_escape_md(draft.get('topic') or '')}\n"
        f"Mix: {dist}\n\n"
        f"*[{item['difficulty']}]* {_escape_md(item['question'])}\n\n"
        f"{opts}\n\n"
        f"Answer: *{item['answer_letter']}*\n"
        f"Explanation: {_escape_md(item.get('explanation') or '')}\n"
    )
    cex = item.get("choice_explanations") or {}
    if isinstance(cex, dict) and any(cex.get(L) for L in "ABCD"):
        text += "\n*Why each choice:*\n"
        for L in "ABCD":
            if cex.get(L):
                text += f"{L}: {_escape_md(cex[L])}\n"
    text += (
        "\nPublish inserts into the live bank. Drop removes this item. Edit stem lets you rewrite it."
    )
    await safe_edit_or_reply(update, text, reply_markup=_preview_keyboard())


async def publish_draft(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    draft = f.get("pplx_draft") or {}
    items = list(draft.get("questions") or [])
    if not items:
        await safe_edit_or_reply(update, "Nothing to publish. Send /start.")
        clear_flow(context)
        return
    saved = 0
    skipped = 0
    for item in items:
        try:
            append_short_mcq(
                f["department"],
                f["specialty"],
                item["difficulty"],
                question=item["question"],
                options=item["options"],
                answer_letter=item["answer_letter"],
                explanation=item.get("explanation") or "",
                choice_explanations=item.get("choice_explanations") or {},
                source="perplexity",
                reject_similar=True,
            )
            saved += 1
        except DuplicateQuestionError:
            skipped += 1
    f["saved"] = saved
    f["content_type"] = "perplexity_mcq"
    if skipped:
        await _reply_plain(
            update,
            f"Skipped *{skipped}* duplicate/similar question(s) during publish.",
            markdown=True,
        )
    await finish_flow(update, context)


async def _reply_plain(update: Update, text: str, *, markdown: bool = False) -> None:
    kwargs = {"parse_mode": "Markdown"} if markdown else {}
    if update.callback_query and update.callback_query.message:
        await update.callback_query.message.reply_text(text, **kwargs)
        return
    if update.message:
        await update.message.reply_text(text, **kwargs)


async def run_perplexity_generation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    if not perplexity_configured():
        await _reply_plain(
            update,
            "Perplexity is not configured.\n"
            "Add `PERPLEXITY_API_KEY` to `question_input/.env`, restart the input bot, then try again.",
        )
        clear_flow(context)
        return

    dep = DEPARTMENTS[f["department"]]
    spec_lab = specialty_label(f["department"], f["specialty"])
    dist = f.get("distribution") or single_distribution(int(f["count"]), "medium")
    stage_key = f.get("stage") or ""
    s_label = stage_label(f["department"], stage_key) if stage_key else ""
    await _reply_plain(
        update,
        f"Calling Perplexity for\n*{_path_label(f)}*\n"
        f"Mix: {mix_summary(dist)}\n\n"
        "Validating strict JSON when it returns…",
        markdown=True,
    )
    f["step"] = "pplx_generating"
    existing_bank = load_bank(f["department"], f["specialty"])
    avoid_stems = existing_stem_samples(existing_bank, limit=50)
    try:
        batch = await asyncio.to_thread(
            generate_batch,
            department_key=f["department"],
            department_label=dep["label"],
            specialty_key=f["specialty"],
            specialty_label=spec_lab,
            distribution=dist,
            topic=f.get("topic") or "",
            stage_key=stage_key,
            stage_label=s_label,
            avoid_stems=avoid_stems,
        )
    except PerplexityError as exc:
        log.exception("Perplexity generation failed")
        await _reply_plain(update, f"Perplexity generation failed:\n{exc}\n\nSend /start to try again.")
        clear_flow(context)
        return
    except Exception as exc:  # pragma: no cover
        log.exception("Unexpected Perplexity error")
        await _reply_plain(update, f"Unexpected error: {exc}\n\nSend /start to try again.")
        clear_flow(context)
        return

    f["pplx_draft"] = batch
    f["pplx_index"] = 0
    # Drop near-duplicates vs bank and within the batch, then save
    raw_items = list(batch.get("questions") or [])
    unique_items, dropped = filter_unique_batch(raw_items, iter_bank_questions(existing_bank))
    saved = 0
    skipped = len(dropped)
    previews: list[str] = []
    for item in unique_items:
        try:
            saved_item = append_short_mcq(
                f["department"],
                f["specialty"],
                item["difficulty"],
                question=item["question"],
                options=item["options"],
                answer_letter=item["answer_letter"],
                explanation=item.get("explanation") or "",
                choice_explanations=item.get("choice_explanations") or {},
                source="perplexity",
                reject_similar=True,
            )
        except DuplicateQuestionError:
            skipped += 1
            continue
        saved += 1
        if len(previews) < 3:
            q = saved_item["question"]
            if len(q) > 120:
                q = q[:117] + "…"
            previews.append(f"• [{item['difficulty']}] {q}")
    f["saved"] = saved
    more = "" if saved <= 3 else f"\n…and {saved - 3} more."
    skip_line = f"\nSkipped *{skipped}* duplicate/similar question(s)." if skipped else ""
    if saved == 0:
        await _reply_plain(
            update,
            f"No new questions saved — all *{len(raw_items)}* were duplicate or too similar "
            f"to items already in this bank.{skip_line}\n\nSend /start to try a different topic.",
            markdown=True,
        )
        clear_flow(context)
        return
    await _reply_plain(
        update,
        f"✅ Generated and saved *{saved}* new Short MCQs into the bank."
        f"{skip_line}\n"
        f"Mix requested: {mix_summary(dist)}\n\n"
        + "\n".join(previews)
        + more,
        markdown=True,
    )
    await finish_flow(update, context)


async def prompt_next_item(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    n = f["index"] + 1
    total = f["count"]
    ctype = f["content_type"]

    if ctype == "short_mcq":
        f["step"] = "mcq_stem"
        f["draft"] = {}
        text = (
            f"Short MCQ *{n}/{total}*\n\n"
            "Send the *question stem* (the question text only)."
        )
    elif ctype == "case_based":
        f["step"] = "case_title"
        f["draft"] = {}
        text = (
            f"Case *{n}/{total}*\n\n"
            "Send the *case title*."
        )
    elif ctype == "book_source":
        f["step"] = "book_title"
        f["draft"] = {}
        text = (
            f"Book source *{n}/{total}*\n\n"
            "Send the *book title* (and edition/author if you want)."
        )
    elif ctype == "pdf_files":
        f["step"] = "pdf_wait"
        text = (
            f"PDF upload *{n}/{total}* (or more)\n\n"
            "Send a *PDF document* now.\n"
            "When finished, send /done"
        )
    else:
        text = "Unknown content type. /start again."
    await safe_edit_or_reply(update, text)


async def finish_flow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    if not f.get("department") or not f.get("specialty"):
        clear_flow(context)
        msg = "Nothing to finish. Send /start to begin."
        if update.message:
            await update.message.reply_text(msg)
        else:
            await safe_edit_or_reply(update, msg)
        return
    path = _path_label(f)
    target_word = "curriculum" if uses_stages(f["department"]) else "specialty"
    saved = f.get("saved", 0)
    ctype_key = f.get("content_type", "")
    if ctype_key == "perplexity_mcq":
        ctype_words = "Perplexity Short MCQs"
    else:
        ctype_words = dict(CONTENT_TYPES).get(ctype_key, "items").lower()
    counts = ""
    if _is_mcq_type(ctype_key):
        c = bank_counts(f["department"], f["specialty"])
        counts = (
            "\n\nBank totals now:\n"
            + "\n".join(f"• {k}: {v}" for k, v in c.items())
        )
    clear_flow(context)
    linked = (
        f"They were generated by Perplexity and saved into that department bot’s {target_word} bank."
        if ctype_key == "perplexity_mcq"
        else f"They are linked to that department bot’s {target_word} content."
    )
    msg = (
        f"✅ Saved *{saved}* {ctype_words} into\n"
        f"*{path}*.\n\n"
        f"{linked}"
        f"{counts}\n\n"
        "Send /start to add more."
    )
    if update.message:
        await update.message.reply_text(msg, parse_mode="Markdown")
    else:
        await safe_edit_or_reply(update, msg)


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user = update.effective_user
    if not _allowed(user.id if user else None):
        await query.edit_message_text("Not authorized.")
        return

    data = query.data or ""
    f = flow(context)

    if data == "cancel":
        clear_flow(context)
        await query.edit_message_text("Cancelled. Send /start to begin again.")
        return

    if data == "back:type":
        clear_flow(context)
        rows = [[(label, f"type:{key}")] for key, label in CONTENT_TYPES]
        rows.append([("Cancel", "cancel")])
        await query.edit_message_text(
            "What do you want to add into a department bot?\n\n"
            "• Generate Short MCQs (auto-save) — Perplexity writes into the bank\n"
            "• Type Short MCQs myself — enter stem/options manually",
            reply_markup=_kb(rows),
        )
        return

    if data == "back:dept":
        f.pop("stage", None)
        f.pop("specialty", None)
        await show_departments(update, context)
        return

    if data == "back:stage":
        f.pop("stage", None)
        f.pop("specialty", None)
        await show_stages(update, context)
        return

    if data in {"back:spec", "back:curr"}:
        f.pop("specialty", None)
        if uses_stages(f.get("department", "")) and f.get("stage"):
            await show_curricula(update, context)
        else:
            await show_specialties(update, context)
        return

    if data.startswith("type:"):
        ctype = data.split(":", 1)[1]
        if ctype == "perplexity_mcq" and not perplexity_configured():
            await query.edit_message_text(
                "Perplexity is not configured yet.\n\n"
                "1) Get an API key from Perplexity\n"
                "2) Put `PERPLEXITY_API_KEY=...` in `question_input/.env`\n"
                "3) Restart the Question Input bot\n"
                "4) Send /start again"
            )
            clear_flow(context)
            return
        if ctype == "short_mcq":
            # Offer generate vs manual so users don't land on stem entry by mistake
            f["step"] = "mcq_mode"
            rows = [
                [("Generate with Perplexity (auto-save)", "type:perplexity_mcq")],
                [("Type myself (stem / A–D)", "mcqmode:manual")],
                [("⟵ Back", "back:type"), ("Cancel", "cancel")],
            ]
            await query.edit_message_text(
                "Short MCQ — how do you want to add them?\n\n"
                "*Generate* writes questions into the bank automatically.\n"
                "*Type myself* asks you for each stem and options.",
                reply_markup=_kb(rows),
                parse_mode="Markdown",
            )
            return
        f["content_type"] = ctype
        f["step"] = "department"
        await show_departments(update, context)
        return

    if data == "mcqmode:manual":
        f["content_type"] = "short_mcq"
        f["step"] = "department"
        await show_departments(update, context)
        return

    if data.startswith("dept:"):
        f["department"] = data.split(":", 1)[1]
        f.pop("stage", None)
        f.pop("specialty", None)
        if uses_stages(f["department"]):
            f["step"] = "stage"
            await show_stages(update, context)
        else:
            f["step"] = "specialty"
            await show_specialties(update, context)
        return

    if data.startswith("stage:"):
        f["stage"] = data.split(":", 1)[1]
        f.pop("specialty", None)
        f["step"] = "curriculum"
        await show_curricula(update, context)
        return

    if data.startswith("spec:"):
        f["specialty"] = data.split(":", 1)[1]
        ctype = f.get("content_type")
        if ctype == "perplexity_mcq":
            # Form continues: count → topic → difficulty distribution
            await ask_count(update, context)
        elif ctype in {"short_mcq", "case_based"}:
            f["step"] = "difficulty"
            await show_difficulty(update, context)
        elif ctype == "pdf_files":
            f["difficulty"] = "n/a"
            f["count"] = 1
            f["step"] = "pdf_wait"
            f["index"] = 0
            f["saved"] = 0
            await prompt_next_item(update, context)
        else:
            f["difficulty"] = "n/a"
            await ask_count(update, context)
        return

    if data.startswith("diff:"):
        f["difficulty"] = data.split(":", 1)[1]
        await ask_count(update, context)
        return

    if data == "back:pplx_topic":
        await ask_perplexity_topic(update, context)
        return

    if data == "back:pplx_dist":
        await show_distribution_menu(update, context)
        return

    if data == "pplxdist:single":
        await show_single_difficulty_menu(update, context)
        return

    if data.startswith("pplxlevel:"):
        level = int(data.split(":", 1)[1])
        f["distribution"] = allocate_mix(int(f["count"]), level)
        f["difficulty"] = f"level_{level}"
        await run_perplexity_generation(update, context)
        return

    if data.startswith("pplxdiff:"):
        difficulty = data.split(":", 1)[1]
        f["distribution"] = single_distribution(int(f["count"]), difficulty)
        f["difficulty"] = difficulty
        await run_perplexity_generation(update, context)
        return

    if data == "pplx:publish":
        await publish_draft(update, context)
        return

    if data == "pplx:discard":
        clear_flow(context)
        await query.edit_message_text("Draft discarded. Nothing was saved. Send /start to begin again.")
        return

    if data == "pplx:drop":
        draft = f.get("pplx_draft") or {}
        items = draft.get("questions") or []
        idx = int(f.get("pplx_index", 0))
        if items and 0 <= idx < len(items):
            items.pop(idx)
            draft["questions"] = items
            dist = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
            for item in items:
                dist[item["difficulty"]] = dist.get(item["difficulty"], 0) + 1
            draft["difficulty_distribution"] = dist
            f["pplx_draft"] = draft
            if not items:
                clear_flow(context)
                await query.edit_message_text("All items dropped. Nothing saved. Send /start.")
                return
            f["pplx_index"] = min(idx, len(items) - 1)
        await show_draft_preview(update, context)
        return

    if data == "pplx:next":
        draft = f.get("pplx_draft") or {}
        items = draft.get("questions") or []
        if items:
            f["pplx_index"] = (int(f.get("pplx_index", 0)) + 1) % len(items)
        await show_draft_preview(update, context)
        return

    if data == "pplx:edit":
        f["step"] = "pplx_edit_stem"
        await query.edit_message_text(
            "Send the *new question stem* for this item.\n"
            "Options, answer, and explanation stay the same unless you discard and regenerate.\n"
            "Send /cancel to abort editing.",
            parse_mode="Markdown",
        )
        return


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not _allowed(user.id if user else None):
        return
    f = flow(context)
    if not f:
        await update.message.reply_text("Send /start to begin.")
        return

    text = (update.message.text or "").strip()
    step = f.get("step")

    if text.lower() in {"/done", "done"} and f.get("content_type") == "pdf_files":
        await finish_flow(update, context)
        return

    if step == "count":
        max_n = 20 if f.get("content_type") == "perplexity_mcq" else 50
        if not text.isdigit() or not (1 <= int(text) <= max_n):
            await update.message.reply_text(f"Please send a number from 1 to {max_n}.")
            return
        f["count"] = int(text)
        await begin_item_entry(update, context)
        return

    if step == "pplx_topic":
        f["topic"] = "" if text.lower() in {"skip", "/skip"} else text
        await show_distribution_menu(update, context)
        return

    if step == "pplx_edit_stem":
        draft = f.get("pplx_draft") or {}
        items = draft.get("questions") or []
        idx = int(f.get("pplx_index", 0))
        if not items or not (0 <= idx < len(items)):
            await update.message.reply_text("No draft item to edit. Send /start.")
            clear_flow(context)
            return
        items[idx]["question"] = text
        draft["questions"] = items
        f["pplx_draft"] = draft
        await update.message.reply_text("Stem updated.")
        await show_draft_preview(update, context)
        return

    if step == "pplx_generating":
        await update.message.reply_text("Still generating with Perplexity… please wait.")
        return

    if step == "pplx_preview":
        await update.message.reply_text(
            "Use the preview buttons: Publish all / Drop this / Next / Edit stem / Discard draft."
        )
        return

    ctype = f.get("content_type")
    draft = f.setdefault("draft", {})

    if ctype == "short_mcq":
        await handle_mcq_text(update, context, text, draft)
        return
    if ctype == "case_based":
        await handle_case_text(update, context, text, draft)
        return
    if ctype == "book_source":
        await handle_book_text(update, context, text)
        return
    if ctype == "pdf_files":
        await update.message.reply_text("Please send a PDF document, or /done when finished.")
        return
    if ctype == "perplexity_mcq":
        await update.message.reply_text("Send /start to generate more with Perplexity.")
        return

    await update.message.reply_text("Unexpected step. Send /start.")


async def handle_mcq_text(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, draft: dict) -> None:
    f = flow(context)
    step = f.get("step")
    n = f["index"] + 1
    total = f["count"]

    if step == "mcq_stem":
        draft["question"] = text
        f["step"] = "mcq_a"
        await update.message.reply_text(f"Q{n}/{total}: send option *A*", parse_mode="Markdown")
        return
    if step == "mcq_a":
        draft["a"] = text
        f["step"] = "mcq_b"
        await update.message.reply_text(f"Q{n}/{total}: send option *B*", parse_mode="Markdown")
        return
    if step == "mcq_b":
        draft["b"] = text
        f["step"] = "mcq_c"
        await update.message.reply_text(f"Q{n}/{total}: send option *C*", parse_mode="Markdown")
        return
    if step == "mcq_c":
        draft["c"] = text
        f["step"] = "mcq_d"
        await update.message.reply_text(f"Q{n}/{total}: send option *D*", parse_mode="Markdown")
        return
    if step == "mcq_d":
        draft["d"] = text
        f["step"] = "mcq_answer"
        await update.message.reply_text(
            f"Q{n}/{total}: which option is correct? Send *A*, *B*, *C*, or *D*.",
            parse_mode="Markdown",
        )
        return
    if step == "mcq_answer":
        letter = text.strip().upper()[:1]
        if letter not in "ABCD":
            await update.message.reply_text("Send A, B, C, or D.")
            return
        draft["answer"] = letter
        f["step"] = "mcq_explanation"
        await update.message.reply_text(
            f"Q{n}/{total}: send a short *explanation* (or type `skip`).",
            parse_mode="Markdown",
        )
        return
    if step == "mcq_explanation":
        explanation = "" if text.lower() == "skip" else text
        try:
            item = append_short_mcq(
                f["department"],
                f["specialty"],
                f["difficulty"],
                question=draft["question"],
                options=[draft["a"], draft["b"], draft["c"], draft["d"]],
                answer_letter=draft["answer"],
                explanation=explanation,
                reject_similar=True,
            )
        except DuplicateQuestionError as exc:
            await update.message.reply_text(
                "This question is too similar to one already in the bank, so it was *not* saved.\n"
                f"{exc}\n\nSend a different stem, or /cancel.",
                parse_mode="Markdown",
            )
            f["step"] = "mcq_stem"
            f["draft"] = {}
            return
        f["saved"] = f.get("saved", 0) + 1
        f["index"] += 1
        await update.message.reply_text(
            f"Saved Short MCQ `{item['id']}` "
            f"({f['saved']}/{f['count']}).",
            parse_mode="Markdown",
        )
        if f["index"] >= f["count"]:
            await finish_flow(update, context)
        else:
            await prompt_next_item(update, context)
        return


async def handle_case_text(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, draft: dict) -> None:
    f = flow(context)
    step = f.get("step")
    n = f["index"] + 1
    total = f["count"]

    prompts = {
        "case_title": ("title", "case_stem", "Send the *case stem* (scenario paragraph)."),
        "case_stem": ("stem", "case_question", "Send the *question* asked about this case."),
        "case_question": ("question", "case_answer", "Send the *correct answer* text."),
        "case_answer": ("answer", "case_discussion", "Send a short *discussion* (or `skip`)."),
    }
    if step in prompts:
        field, nxt, ask = prompts[step]
        draft[field] = text
        f["step"] = nxt
        await update.message.reply_text(f"Case {n}/{total}: {ask}", parse_mode="Markdown")
        return
    if step == "case_discussion":
        discussion = "" if text.lower() == "skip" else text
        item = append_case(
            f["department"],
            f["specialty"],
            f["difficulty"],
            title=draft["title"],
            stem=draft["stem"],
            question=draft["question"],
            answer=draft["answer"],
            discussion=discussion,
        )
        f["saved"] = f.get("saved", 0) + 1
        f["index"] += 1
        await update.message.reply_text(
            f"Saved case *{item['title']}* ({f['saved']}/{f['count']}).",
            parse_mode="Markdown",
        )
        if f["index"] >= f["count"]:
            await finish_flow(update, context)
        else:
            await prompt_next_item(update, context)


async def handle_book_text(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    f = flow(context)
    title = append_book(f["department"], f["specialty"], text)
    f["saved"] = f.get("saved", 0) + 1
    f["index"] += 1
    await update.message.reply_text(
        f"Saved book source: *{title}* ({f['saved']}/{f['count']}).",
        parse_mode="Markdown",
    )
    if f["index"] >= f["count"]:
        await finish_flow(update, context)
    else:
        await prompt_next_item(update, context)


async def on_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not _allowed(user.id if user else None):
        return
    f = flow(context)
    if not f or f.get("content_type") != "pdf_files" or f.get("step") != "pdf_wait":
        await update.message.reply_text("Send /start and choose *PDF files* first.", parse_mode="Markdown")
        return
    doc = update.message.document
    if not doc:
        return
    name = doc.file_name or "upload.pdf"
    if not name.lower().endswith(".pdf"):
        await update.message.reply_text("Please send a PDF file.")
        return
    tg_file = await doc.get_file()
    tmp = Path(__file__).resolve().parent / "data" / "tmp"
    tmp.mkdir(parents=True, exist_ok=True)
    local = tmp / name
    await tg_file.download_to_drive(custom_path=str(local))
    dest = save_pdf(f["department"], f["specialty"], local, name)
    try:
        local.unlink(missing_ok=True)
    except Exception:
        pass
    f["saved"] = f.get("saved", 0) + 1
    await update.message.reply_text(
        f"Saved PDF: `{dest.name}`\n"
        f"Total saved this session: *{f['saved']}*\n\n"
        "Send another PDF, or /done to finish.",
        parse_mode="Markdown",
    )


def main() -> None:
    if not TOKEN:
        raise SystemExit(
            "Missing QUESTION_INPUT_BOT_TOKEN. Create a bot with @BotFather, "
            "then put the token in question_input/.env"
        )
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("cancel", cmd_cancel))
    app.add_handler(CommandHandler("done", lambda u, c: finish_flow(u, c)))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.Document.ALL, on_document))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    log.info("Question input bot starting")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
