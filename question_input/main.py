"""CharaNas Question Input bot — add Short MCQ / cases / PDFs / books into department bots."""

from __future__ import annotations

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
    from catalog import CASE_DIFFICULTIES, CONTENT_TYPES, DEPARTMENTS, DIFFICULTIES
    from storage import append_book, append_case, append_short_mcq, bank_counts, save_pdf
except ImportError:  # pragma: no cover
    from question_input.catalog import CASE_DIFFICULTIES, CONTENT_TYPES, DEPARTMENTS, DIFFICULTIES
    from question_input.storage import append_book, append_case, append_short_mcq, bank_counts, save_pdf

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
        "What do you want to add into a department bot?",
        reply_markup=_kb(rows),
        parse_mode="Markdown",
    )


async def cmd_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    clear_flow(context)
    await update.message.reply_text("Cancelled. Send /start to begin again.")


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Use /start to add content.\n\n"
        "Flow:\n"
        "1) Choose Short MCQ / Case-based / PDF / Book source\n"
        "2) Choose department (Medicine, Dentistry, Pharmacy, MLS, Nursing)\n"
        "3) Choose specialty\n"
        "4) Enter how many items\n"
        "5) Submit each item with its details\n\n"
        "Short MCQs are saved into that specialty’s live question bank and appear in that department bot after reload.\n"
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


async def show_specialties(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
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


async def show_difficulty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    diffs = CASE_DIFFICULTIES if f.get("content_type") == "case_based" else DIFFICULTIES
    rows = [[(label, f"diff:{key}")] for key, label in diffs]
    rows.append([("⟵ Back", "back:spec"), ("Cancel", "cancel")])
    await safe_edit_or_reply(
        update,
        "Choose difficulty for these items:",
        reply_markup=_kb(rows),
    )


async def ask_count(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    f["step"] = "count"
    dep = DEPARTMENTS[f["department"]]
    spec_label = dict(dep["specialties"]).get(f["specialty"], f["specialty"])
    await safe_edit_or_reply(
        update,
        f"*{dep['label']} → {spec_label}*\n"
        f"Difficulty: *{f.get('difficulty', 'n/a')}*\n\n"
        "How many items will you input now?\n"
        "Send a number from *1* to *50*.",
    )


async def begin_item_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = flow(context)
    f["index"] = 0
    f["saved"] = 0
    await prompt_next_item(update, context)


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
    dep = DEPARTMENTS[f["department"]]
    spec_label = dict(dep["specialties"]).get(f["specialty"], f["specialty"])
    saved = f.get("saved", 0)
    ctype = dict(CONTENT_TYPES).get(f.get("content_type", ""), "items")
    counts = ""
    if f.get("content_type") == "short_mcq":
        c = bank_counts(f["department"], f["specialty"])
        counts = (
            "\n\nBank totals now:\n"
            + "\n".join(f"• {k}: {v}" for k, v in c.items())
        )
    clear_flow(context)
    msg = (
        f"✅ Saved *{saved}* {ctype.lower()} into\n"
        f"*{dep['label']} → {spec_label}*.\n\n"
        "They are linked to that department bot’s specialty content."
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
            "What do you want to add into a department bot?",
            reply_markup=_kb(rows),
        )
        return

    if data == "back:dept":
        await show_departments(update, context)
        return

    if data == "back:spec":
        await show_specialties(update, context)
        return

    if data.startswith("type:"):
        f["content_type"] = data.split(":", 1)[1]
        f["step"] = "department"
        await show_departments(update, context)
        return

    if data.startswith("dept:"):
        f["department"] = data.split(":", 1)[1]
        f["step"] = "specialty"
        await show_specialties(update, context)
        return

    if data.startswith("spec:"):
        f["specialty"] = data.split(":", 1)[1]
        ctype = f.get("content_type")
        if ctype in {"short_mcq", "case_based"}:
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
        if not text.isdigit() or not (1 <= int(text) <= 50):
            await update.message.reply_text("Please send a number from 1 to 50.")
            return
        f["count"] = int(text)
        await begin_item_entry(update, context)
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
        item = append_short_mcq(
            f["department"],
            f["specialty"],
            f["difficulty"],
            question=draft["question"],
            options=[draft["a"], draft["b"], draft["c"], draft["d"]],
            answer_letter=draft["answer"],
            explanation=explanation,
        )
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
