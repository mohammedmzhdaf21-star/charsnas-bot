import logging
import re
import traceback
from pathlib import Path

from dotenv import load_dotenv
import os

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(Path(__file__).resolve().parent / "bot.log"),
    ],
)
log = logging.getLogger("charanas-pharmacy-bot")

from content import (
    DIFFICULTIES,
    DIFFICULTY_LABELS,
    LABEL_TO_DIFFICULTY,
    SPECIALTIES,
    SPECIALTY_ORDER,
    correct_letter,
    difficulty_menu_text,
    feature_menu_text,
    format_book_sources,
    format_case_prompt,
    format_case_result,
    format_question_prompt,
    format_question_result,
    present_question,
    label_to_key,
    option_letter,
    pick_case,
    pick_question,
    specialty_label,
    specialty_menu_text,
    reload_department_content,
)
from generate_pdfs import PDF_DIR, ensure_pdfs, pdf_for_specialty
from bank_loader import custom_pdf_paths
from quiz_session import (
    COUNT_OPTIONS,
    DAILY_LIMIT,
    DailyUsageStore,
    SeenQuestionsStore,
    allowed_counts,
    bank_question_ids,
    build_difficulty_queue,
    count_menu_text,
    daily_limit_text,
    level_menu_text,
    parse_count,
    parse_level,
    session_complete_text,
    specialty_bank_total,
)

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_TOKEN = os.getenv("PHARMACY_BOT_TOKEN") or os.getenv("BOT_TOKEN")

ROOT = Path(__file__).resolve().parent
USAGE_STORE = DailyUsageStore(ROOT / "data" / "daily_mcq_usage.json")
SEEN_STORE = SeenQuestionsStore(ROOT / "data" / "seen_questions.json")
BANKS_DIR = ROOT / "question_banks"
CUSTOM_CONTENT_DIR = ROOT / "custom_content"

def refresh_content() -> None:
    """Pick up Short MCQs / cases / books saved by the input bot."""
    reload_department_content(SPECIALTIES, BANKS_DIR, CUSTOM_CONTENT_DIR)

BTN_MCQ = "Short MCQ"
BTN_CASE = "Case-based Question"
BTN_PDF = "PDF files"
BTN_BOOKS = "Book source"
BTN_BACK_SPECIALTY = "Change specialty"
BTN_BACK_FEATURES = "Back to features"

FEATURE_LABELS = {
    BTN_MCQ: "question",
    BTN_CASE: "case",
    BTN_PDF: "pdf",
    BTN_BOOKS: "books",
    BTN_BACK_SPECIALTY: "back_specialty",
    BTN_BACK_FEATURES: "back_features",
}

INTENT_PATTERNS = {
    "question": [r"\bshort\s+mcq\b", r"\bmcq\b"],
    "case": [r"\bcase[-\s]?based\b", r"\bcase\s+questions?\b"],
    "pdf": [r"\bpdf\b", r"\bpdf\s+files?\b"],
    "books": [r"\bbook\s+sources?\b", r"\btextbooks?\b"],
    "back_specialty": [r"\bchange\s+specialty\b"],
    "back_features": [r"\bback\s+to\s+features\b", r"^back$"],
}


def specialty_keyboard() -> ReplyKeyboardMarkup:
    labels = [SPECIALTIES[k]["label"] for k in SPECIALTY_ORDER]
    rows: list[list[KeyboardButton]] = []
    row: list[KeyboardButton] = []
    for label in labels:
        row.append(KeyboardButton(label))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return ReplyKeyboardMarkup(rows, resize_keyboard=True, is_persistent=True)


def feature_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(BTN_MCQ), KeyboardButton(BTN_CASE)],
            [KeyboardButton(BTN_PDF), KeyboardButton(BTN_BOOKS)],
            [KeyboardButton(BTN_BACK_SPECIALTY)],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def difficulty_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Easy"), KeyboardButton("Medium")],
            [KeyboardButton("Hard"), KeyboardButton("Extreme")],
            [KeyboardButton(BTN_BACK_FEATURES), KeyboardButton(BTN_BACK_SPECIALTY)],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def count_keyboard(remaining: int) -> ReplyKeyboardMarkup:
    opts = allowed_counts(remaining)
    rows: list[list[KeyboardButton]] = []
    row: list[KeyboardButton] = []
    for n in opts:
        label = f"{n} questions" if n in COUNT_OPTIONS else f"{n} questions"
        row.append(KeyboardButton(label))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([KeyboardButton(BTN_BACK_FEATURES), KeyboardButton(BTN_BACK_SPECIALTY)])
    return ReplyKeyboardMarkup(rows, resize_keyboard=True, is_persistent=True)


def level_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Level 1"), KeyboardButton("Level 2")],
            [KeyboardButton("Level 3"), KeyboardButton("Level 4")],
            [KeyboardButton("Level 5")],
            [KeyboardButton(BTN_BACK_FEATURES), KeyboardButton(BTN_BACK_SPECIALTY)],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def clear_mcq_session(context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("mcq_session", None)
    context.user_data.pop("mcq_await", None)
    context.user_data.pop("mcq_count", None)


def current_specialty(context: ContextTypes.DEFAULT_TYPE) -> str | None:
    key = context.user_data.get("specialty")
    return key if key in SPECIALTIES else None


def remaining_map(context: ContextTypes.DEFAULT_TYPE, field: str) -> dict:
    store = context.user_data.get(field)
    if not isinstance(store, dict):
        store = {}
        context.user_data[field] = store
    return store


def pool_key(specialty_key: str, difficulty: str) -> str:
    return f"{specialty_key}:{difficulty}"


def detect_feature_intent(text: str) -> str | None:
    stripped = text.strip()
    if stripped in FEATURE_LABELS:
        return FEATURE_LABELS[stripped]
    normalized = " ".join(stripped.lower().split())
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, normalized):
                return intent
    return None


def question_keyboard(specialty_key: str, difficulty: str, idx: int, item: dict) -> InlineKeyboardMarkup:
    """Short A–D buttons; full option text is in the message body."""
    rows = []
    row = []
    diff_code = {"easy": "e", "medium": "m", "hard": "h", "extreme": "x"}[difficulty]
    spec_code = specialty_key[:8]
    for option in item["options"]:
        letter = option_letter(option)
        row.append(
            InlineKeyboardButton(
                letter,  # full answer text is shown in the message, not truncated on the button
                callback_data=f"q:{spec_code}:{diff_code}:{idx}:{letter}",
            )
        )
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(rows)


def case_keyboard(specialty_key: str, difficulty: str, idx: int) -> InlineKeyboardMarkup:
    diff_code = {"easy": "e", "medium": "m", "hard": "h", "extreme": "x"}[difficulty]
    spec_code = specialty_key[:8]
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("Reveal answer", callback_data=f"c:{spec_code}:{diff_code}:{idx}")]]
    )


def resolve_specialty_code(code: str) -> str | None:
    matches = [k for k in SPECIALTIES if k.startswith(code) or k[:8] == code]
    return matches[0] if len(matches) == 1 else (matches[0] if matches else None)


DIFF_CODE = {"e": "easy", "m": "medium", "h": "hard", "x": "extreme"}


async def safe_reply(update: Update, text: str, reply_markup=None, parse_mode: str | None = "Markdown") -> None:
    """Send a reply; if Markdown fails, retry as plain text."""
    message = update.effective_message
    if not message:
        return
    try:
        await message.reply_text(text, parse_mode=parse_mode, reply_markup=reply_markup)
    except BadRequest as exc:
        log.warning("Markdown send failed: %s — retrying plain text", exc)
        await message.reply_text(text, reply_markup=reply_markup)


async def safe_edit(query, text: str, parse_mode: str | None = "Markdown") -> None:
    """Show the full answer even when long; split across messages if needed."""
    import sys
    from pathlib import Path as _Path
    root = _Path(__file__).resolve().parent
    if (root / "telegram_text.py").exists():
        sys.path.insert(0, str(root))
    elif (root.parent / "telegram_text.py").exists():
        sys.path.insert(0, str(root.parent))
    from telegram_text import edit_or_send_full

    await edit_or_send_full(query, text)


async def show_specialty_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str | None = None) -> None:
    context.user_data["specialty"] = None
    context.user_data["quiz_mode"] = None
    context.user_data["difficulty"] = None
    clear_mcq_session(context)
    await safe_reply(update, text or specialty_menu_text(), reply_markup=specialty_keyboard())


async def show_feature_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str) -> None:
    context.user_data["specialty"] = specialty_key
    context.user_data["quiz_mode"] = None
    context.user_data["difficulty"] = None
    clear_mcq_session(context)
    await safe_reply(update, feature_menu_text(specialty_key), reply_markup=feature_keyboard())


async def show_difficulty_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str, mode: str
) -> None:
    context.user_data["specialty"] = specialty_key
    context.user_data["quiz_mode"] = mode
    await safe_reply(
        update,
        difficulty_menu_text(specialty_key, mode),
        reply_markup=difficulty_keyboard(),
    )


def question_id_for(specialty_key: str, difficulty: str, idx: int, item: dict | None = None) -> str:
    if item and item.get("id"):
        return str(item["id"])
    return f"{specialty_key}:{difficulty}:{idx}"


def bank_stats(user_id: int, specialty_key: str) -> tuple[int, int]:
    ids = bank_question_ids(SPECIALTIES, specialty_key)
    total = len(ids)
    unseen = SEEN_STORE.unseen_count(user_id, specialty_key, ids)
    return total, unseen


def pick_unseen_question(user_id: int, specialty_key: str, preferred_difficulty: str) -> tuple[str, int, dict]:
    """Return (difficulty, idx, item) never seen by this user; reset specialty when exhausted."""
    ids = bank_question_ids(SPECIALTIES, specialty_key)
    if ids and SEEN_STORE.unseen_count(user_id, specialty_key, ids) == 0:
        SEEN_STORE.reset_specialty(user_id, specialty_key)

    seen = SEEN_STORE.seen_set(user_id, specialty_key)

    def candidates(diff: str) -> list[tuple[str, int, dict]]:
        items = SPECIALTIES[specialty_key]["questions"][diff]
        out = []
        for i, item in enumerate(items):
            qid = question_id_for(specialty_key, diff, i, item)
            if qid not in seen:
                out.append((diff, i, item))
        return out

    pool = candidates(preferred_difficulty)
    if not pool:
        for diff in DIFFICULTIES:
            if diff == preferred_difficulty:
                continue
            pool = candidates(diff)
            if pool:
                break
    if not pool:
        # absolute fallback
        items = SPECIALTIES[specialty_key]["questions"][preferred_difficulty]
        return preferred_difficulty, 0, items[0]
    import random as _random

    return _random.choice(pool)


async def show_count_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str) -> None:
    user = update.effective_user
    if not user:
        return
    remaining = USAGE_STORE.remaining(user.id, specialty_key)
    bank_total, unseen = bank_stats(user.id, specialty_key)
    label = specialty_label(specialty_key)
    context.user_data["specialty"] = specialty_key
    context.user_data["quiz_mode"] = "question"
    context.user_data["mcq_await"] = "count"
    context.user_data.pop("mcq_count", None)
    context.user_data.pop("mcq_session", None)

    if remaining <= 0:
        await safe_reply(
            update,
            daily_limit_text(label, bank_total=bank_total),
            reply_markup=feature_keyboard(),
        )
        clear_mcq_session(context)
        context.user_data["quiz_mode"] = None
        return

    # Cap available counts by unseen as well
    available = min(remaining, unseen if unseen > 0 else remaining)
    await safe_reply(
        update,
        count_menu_text(label, remaining, bank_total=bank_total, unseen_total=unseen),
        reply_markup=count_keyboard(available),
    )


async def show_level_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str, count: int
) -> None:
    user = update.effective_user
    if not user:
        return
    remaining = USAGE_STORE.remaining(user.id, specialty_key)
    bank_total, unseen = bank_stats(user.id, specialty_key)
    label = specialty_label(specialty_key)
    context.user_data["specialty"] = specialty_key
    context.user_data["quiz_mode"] = "question"
    context.user_data["mcq_await"] = "level"
    context.user_data["mcq_count"] = count
    await safe_reply(
        update,
        level_menu_text(
            label, count, remaining, bank_total=bank_total, unseen_total=unseen
        ),
        reply_markup=level_keyboard(),
    )


async def require_specialty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str | None:
    key = current_specialty(context)
    if key:
        return key
    await show_specialty_menu(update, context, "Please choose a *specialty* first.")
    return None


def _prompt_with_progress(item: dict, label: str, difficulty: str, session: dict) -> str:
    text = format_question_prompt(item, label, difficulty)
    i = int(session.get("index", 0)) + 1
    n = int(session.get("count", 0))
    level = int(session.get("level", 0))
    header = f"📘 *Short MCQ — {label}*\n"
    if text.startswith(header):
        return text.replace(
            header,
            f"{header}Question *{i}/{n}* · Level *{level}*\n",
            1,
        )
    return f"Question *{i}/{n}* · Level *{level}*\n\n{text}"


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, difficulty: str) -> None:
    """Legacy single-difficulty send (kept for compatibility; Short MCQ uses sessions)."""
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    store = remaining_map(context, "remaining_questions")
    key = pool_key(specialty_key, difficulty)
    remaining = store.get(key)
    idx, item, remaining = pick_question(specialty_key, difficulty, remaining)
    store[key] = remaining

    context.user_data["difficulty"] = difficulty
    context.user_data.setdefault("cb_spec", {})[specialty_key[:8]] = specialty_key

    item = present_question(item)
    presented = context.user_data.setdefault("presented_questions", {})
    presented[f"{specialty_key}:{difficulty}:{idx}"] = item

    label = specialty_label(specialty_key)
    await safe_reply(
        update,
        format_question_prompt(item, label, difficulty),
        reply_markup=question_keyboard(specialty_key, difficulty, idx, item),
    )


async def start_mcq_session(
    update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str, count: int, level: int
) -> None:
    user = update.effective_user
    if not user:
        return
    # Pick up newly saved / Perplexity-generated bank items without restarting
    refresh_content()
    remaining = USAGE_STORE.remaining(user.id, specialty_key)
    bank_total, unseen = bank_stats(user.id, specialty_key)
    label = specialty_label(specialty_key)
    if remaining <= 0:
        await safe_reply(
            update, daily_limit_text(label, bank_total=bank_total), reply_markup=feature_keyboard()
        )
        clear_mcq_session(context)
        context.user_data["quiz_mode"] = None
        return
    # Never exceed daily remaining or unseen bank
    count = min(count, remaining, unseen if unseen > 0 else count)
    if count <= 0:
        await safe_reply(
            update,
            f"No unseen questions left right now for *{label}*. Bank total: *{bank_total}*.",
            reply_markup=feature_keyboard(),
        )
        return

    queue = build_difficulty_queue(count, level)
    context.user_data["mcq_session"] = {
        "specialty": specialty_key,
        "count": count,
        "level": level,
        "queue": queue,
        "index": 0,
        "correct": 0,
        "active": True,
    }
    context.user_data["mcq_await"] = None
    context.user_data["quiz_mode"] = "question"
    await send_session_question(update, context)


async def send_session_question(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    *,
    reply_to_message=None,
) -> None:
    session = context.user_data.get("mcq_session")
    if not session or not session.get("active"):
        return
    specialty_key = session["specialty"]
    user = update.effective_user
    if not user:
        return

    remaining = USAGE_STORE.remaining(user.id, specialty_key)
    bank_total, unseen = bank_stats(user.id, specialty_key)
    label = specialty_label(specialty_key)
    if remaining <= 0 or session["index"] >= session["count"]:
        session["active"] = False
        left = USAGE_STORE.remaining(user.id, specialty_key)
        bank_total, unseen = bank_stats(user.id, specialty_key)
        text = session_complete_text(
            label, session, left, bank_total=bank_total, unseen_total=unseen
        )
        clear_mcq_session(context)
        context.user_data["quiz_mode"] = None
        if reply_to_message is not None:
            await reply_to_message.reply_text(text, parse_mode="Markdown", reply_markup=feature_keyboard())
        else:
            await safe_reply(update, text, reply_markup=feature_keyboard())
        return

    preferred = session["queue"][session["index"]]
    difficulty, idx, item = pick_unseen_question(user.id, specialty_key, preferred)
    qid = question_id_for(specialty_key, difficulty, idx, item)

    context.user_data["difficulty"] = difficulty
    context.user_data.setdefault("cb_spec", {})[specialty_key[:8]] = specialty_key

    item = present_question(item)
    presented = context.user_data.setdefault("presented_questions", {})
    presented[f"{specialty_key}:{difficulty}:{idx}"] = item

    SEEN_STORE.mark_seen(user.id, specialty_key, qid)
    USAGE_STORE.increment(user.id, specialty_key, 1)
    prompt = _prompt_with_progress(item, label, difficulty, session)
    markup = question_keyboard(specialty_key, difficulty, idx, item)

    if reply_to_message is not None:
        try:
            await reply_to_message.reply_text(prompt, parse_mode="Markdown", reply_markup=markup)
        except BadRequest:
            await reply_to_message.reply_text(prompt, reply_markup=markup)
    else:
        await safe_reply(update, prompt, reply_markup=markup)


async def send_case(update: Update, context: ContextTypes.DEFAULT_TYPE, difficulty: str) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    refresh_content()
    store = remaining_map(context, "remaining_cases")
    key = pool_key(specialty_key, difficulty)
    remaining = store.get(key)
    idx, item, remaining = pick_case(specialty_key, difficulty, remaining)
    store[key] = remaining

    context.user_data["difficulty"] = difficulty
    context.user_data.setdefault("cb_spec", {})[specialty_key[:8]] = specialty_key

    label = specialty_label(specialty_key)
    await safe_reply(
        update,
        format_case_prompt(item, label, difficulty),
        reply_markup=case_keyboard(specialty_key, difficulty, idx),
    )


async def send_books(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    refresh_content()
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return
    await safe_reply(
        update,
        format_book_sources(specialty_key),
        reply_markup=feature_keyboard(),
    )


async def send_pdfs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    refresh_content()
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    path = pdf_for_specialty(specialty_key, PDF_DIR)
    label = specialty_label(specialty_key)
    extras = custom_pdf_paths(PDF_DIR, specialty_key)
    await safe_reply(
        update,
        f"📄 Sending *{label}* PDF study notes…"
        + (f" (+{len(extras)} custom)" if extras else ""),
        reply_markup=feature_keyboard(),
    )
    with path.open("rb") as fh:
        await update.message.reply_document(
            document=fh,
            filename=path.name,
            caption=f"UG Medicine — {label}",
        )
    for extra in extras:
        with extra.open("rb") as fh:
            await update.message.reply_document(
                document=fh,
                filename=extra.name,
                caption=f"Custom PDF — {label}",
            )


async def dispatch_feature(
    update: Update, context: ContextTypes.DEFAULT_TYPE, intent: str
) -> None:
    specialty_key = current_specialty(context)

    if intent == "back_specialty":
        await show_specialty_menu(update, context)
        return
    if intent == "back_features":
        if specialty_key:
            await show_feature_menu(update, context, specialty_key)
        else:
            await show_specialty_menu(update, context)
        return

    if intent == "question":
        if not specialty_key:
            await show_specialty_menu(update, context, "Please choose a *specialty* first.")
            return
        await show_count_menu(update, context, specialty_key)
        return

    if intent == "case":
        if not specialty_key:
            await show_specialty_menu(update, context, "Please choose a *specialty* first.")
            return
        await show_difficulty_menu(update, context, specialty_key, intent)
        return

    if intent == "pdf":
        await send_pdfs(update, context)
    elif intent == "books":
        await send_books(update, context)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await show_specialty_menu(update, context)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if current_specialty(context):
        await show_feature_menu(update, context, current_specialty(context))
    else:
        await show_specialty_menu(update, context)


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()

    # Specialty selection
    specialty_key = label_to_key(text)
    if specialty_key:
        await show_feature_menu(update, context, specialty_key)
        return

    intent = detect_feature_intent(text)
    if intent:
        await dispatch_feature(update, context, intent)
        return

    # Short MCQ: count selection
    if context.user_data.get("quiz_mode") == "question" and context.user_data.get("mcq_await") == "count":
        count = parse_count(text)
        spec = current_specialty(context)
        if not spec:
            await show_specialty_menu(update, context)
            return
        user = update.effective_user
        remaining = USAGE_STORE.remaining(user.id, spec) if user else 0
        bank_total, unseen = bank_stats(user.id, spec) if user else (0, 0)
        available = min(remaining, unseen if unseen > 0 else remaining)
        if count is None:
            await safe_reply(
                update,
                "Please choose *5*, *10*, *15*, or *20* questions.",
                reply_markup=count_keyboard(available),
            )
            return
        if remaining <= 0:
            await safe_reply(
                update,
                daily_limit_text(specialty_label(spec), bank_total=bank_total),
                reply_markup=feature_keyboard(),
            )
            clear_mcq_session(context)
            return
        if count > available:
            await safe_reply(
                update,
                (
                    f"Only *{available}* questions available now "
                    f"(today left *{remaining}*, unseen *{unseen}*, bank total *{bank_total}*). "
                    f"Choose an allowed count."
                ),
                reply_markup=count_keyboard(available),
            )
            return
        await show_level_menu(update, context, spec, count)
        return

    # Short MCQ: advancement level selection
    if context.user_data.get("quiz_mode") == "question" and context.user_data.get("mcq_await") == "level":
        level = parse_level(text)
        spec = current_specialty(context)
        count = context.user_data.get("mcq_count")
        if not spec or not isinstance(count, int):
            if spec:
                await show_count_menu(update, context, spec)
            else:
                await show_specialty_menu(update, context)
            return
        if level is None:
            await safe_reply(
                update,
                "Please choose *Level 1* through *Level 5*.",
                reply_markup=level_keyboard(),
            )
            return
        await start_mcq_session(update, context, spec, count, level)
        return

    # Case difficulty selection (Short MCQ no longer uses fixed difficulty alone)
    if text in LABEL_TO_DIFFICULTY:
        difficulty = LABEL_TO_DIFFICULTY[text]
        mode = context.user_data.get("quiz_mode")
        if mode == "case":
            await send_case(update, context, difficulty)
            return
        if mode == "question":
            # Redirect into new Short MCQ flow
            spec = current_specialty(context)
            if spec:
                await show_count_menu(update, context, spec)
            else:
                await show_specialty_menu(update, context)
            return
        if current_specialty(context):
            await safe_reply(
                update,
                "First choose *Short MCQ* (count + level) or *Case-based Question* (difficulty).",
                reply_markup=feature_keyboard(),
            )
        else:
            await show_specialty_menu(update, context)
        return

    if current_specialty(context):
        mode = context.user_data.get("quiz_mode")
        await_step = context.user_data.get("mcq_await")
        if mode == "question" and await_step == "count":
            user = update.effective_user
            rem = USAGE_STORE.remaining(user.id, current_specialty(context)) if user else 0
            await safe_reply(
                update,
                "Please choose how many questions to solve, or *Back to features*.",
                reply_markup=count_keyboard(rem),
            )
        elif mode == "question" and await_step == "level":
            await safe_reply(
                update,
                "Please choose an advancement level, or *Back to features*.",
                reply_markup=level_keyboard(),
            )
        elif mode == "question" and context.user_data.get("mcq_session", {}).get("active"):
            await safe_reply(
                update,
                "Answer the current question with the *A / B / C / D* buttons.",
                reply_markup=feature_keyboard(),
            )
        elif mode == "case":
            await safe_reply(
                update,
                "Please choose a difficulty button, or *Back to features*.",
                reply_markup=difficulty_keyboard(),
            )
        else:
            await safe_reply(
                update,
                "Please choose a feature from the buttons below, or tap *Change specialty*.",
                reply_markup=feature_keyboard(),
            )
    else:
        await show_specialty_menu(
            update,
            context,
            "Please choose a *specialty* from the buttons below.",
        )


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data or ""

    if data.startswith("q:"):
        try:
            _, spec_code, diff_code, idx_s, choice = data.split(":", 4)
            specialty_key = context.user_data.get("cb_spec", {}).get(spec_code) or resolve_specialty_code(spec_code)
            difficulty = DIFF_CODE[diff_code]
            idx = int(idx_s)
            bank_item = SPECIALTIES[specialty_key]["questions"][difficulty][idx]
        except (ValueError, IndexError, KeyError, TypeError):
            await safe_edit(
                query,
                "This question expired. Open *Short MCQ* again to start a new set.",
            )
            return
        presented = context.user_data.get("presented_questions", {})
        item = presented.get(f"{specialty_key}:{difficulty}:{idx}", bank_item)
        label = specialty_label(specialty_key)
        result = format_question_result(item, choice, label, difficulty)
        await safe_edit(query, result)

        session = context.user_data.get("mcq_session")
        if session and session.get("active") and session.get("specialty") == specialty_key:
            answered_ids = session.setdefault("answered_ids", [])
            qid = f"{specialty_key}:{difficulty}:{idx}"
            if qid in answered_ids:
                return
            answered_ids.append(qid)
            if choice.upper() == correct_letter(item):
                session["correct"] = int(session.get("correct") or 0) + 1
            session["index"] = int(session.get("index") or 0) + 1
            await send_session_question(update, context, reply_to_message=query.message)
        return

    if data.startswith("c:"):
        try:
            _, spec_code, diff_code, idx_s = data.split(":", 3)
            specialty_key = context.user_data.get("cb_spec", {}).get(spec_code) or resolve_specialty_code(spec_code)
            difficulty = DIFF_CODE[diff_code]
            idx = int(idx_s)
            item = SPECIALTIES[specialty_key]["cases"][difficulty][idx]
        except (ValueError, IndexError, KeyError, TypeError):
            await safe_edit(
                query,
                "This case expired. Open *Case-based Question* and pick a difficulty again.",
            )
            return
        label = specialty_label(specialty_key)
        result = format_case_result(item, label, difficulty)
        await safe_edit(query, result)
        return


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(update, "✅ CharaNas Pharmacy is online. Send /start to open the specialty menu.")


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.error("Handler error: %s\n%s", context.error, traceback.format_exc())
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "Something went wrong. Please send /start and try again."
            )
        except Exception:
            pass


def main() -> None:
    log.info("Preparing PDFs…")
    ensure_pdfs(PDF_DIR)
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("pdf", send_pdfs))
    app.add_handler(CommandHandler("books", send_books))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(on_error)
    log.info("CharaNas Pharmacy bot starting polling…")
    print("CharaNas Pharmacy bot running (specialties + difficulty)…")
    app.run_polling(
        drop_pending_updates=False,
        allowed_updates=Update.ALL_TYPES,
        bootstrap_retries=5,
    )


if __name__ == "__main__":
    main()