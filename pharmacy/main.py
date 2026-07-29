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
    difficulty_menu_text,
    feature_menu_text,
    format_book_sources,
    format_case_prompt,
    format_case_result,
    format_question_prompt,
    format_question_result,
    label_to_key,
    option_letter,
    pick_case,
    pick_question,
    specialty_label,
    specialty_menu_text,
)
from generate_pdfs import PDF_DIR, ensure_pdfs, pdf_for_specialty

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_TOKEN = os.getenv("PHARMACY_BOT_TOKEN") or os.getenv("BOT_TOKEN")

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
    rows = []
    row = []
    # callback must stay under 64 bytes: q:card:e:0:A style short codes
    diff_code = {"easy": "e", "medium": "m", "hard": "h", "extreme": "x"}[difficulty]
    spec_code = specialty_key[:8]
    for option in item["options"]:
        letter = option_letter(option)
        row.append(
            InlineKeyboardButton(
                option,
                callback_data=f"q:{spec_code}:{diff_code}:{idx}:{letter}",
            )
        )
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    # store full keys for callback resolution
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
    try:
        await query.edit_message_text(text, parse_mode=parse_mode)
    except BadRequest as exc:
        log.warning("Markdown edit failed: %s — retrying plain text", exc)
        await query.edit_message_text(text)


async def show_specialty_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str | None = None) -> None:
    context.user_data["specialty"] = None
    context.user_data["quiz_mode"] = None
    context.user_data["difficulty"] = None
    await safe_reply(update, text or specialty_menu_text(), reply_markup=specialty_keyboard())


async def show_feature_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str) -> None:
    context.user_data["specialty"] = specialty_key
    context.user_data["quiz_mode"] = None
    context.user_data["difficulty"] = None
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


async def require_specialty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str | None:
    key = current_specialty(context)
    if key:
        return key
    await show_specialty_menu(update, context, "Please choose a *specialty* first.")
    return None


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, difficulty: str) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    store = remaining_map(context, "remaining_questions")
    key = pool_key(specialty_key, difficulty)
    remaining = store.get(key)
    idx, item, remaining = pick_question(specialty_key, difficulty, remaining)
    store[key] = remaining

    # remember for callback resolution of short codes
    context.user_data["difficulty"] = difficulty
    context.user_data.setdefault("cb_spec", {})[specialty_key[:8]] = specialty_key

    label = specialty_label(specialty_key)
    await safe_reply(
        update,
        format_question_prompt(item, label, difficulty),
        reply_markup=question_keyboard(specialty_key, difficulty, idx, item),
    )


async def send_case(update: Update, context: ContextTypes.DEFAULT_TYPE, difficulty: str) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

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
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return
    await safe_reply(
        update,
        format_book_sources(specialty_key),
        reply_markup=feature_keyboard(),
    )


async def send_pdfs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    path = pdf_for_specialty(specialty_key, PDF_DIR)
    label = specialty_label(specialty_key)
    await safe_reply(
        update,
        f"📄 Sending *{label}* PDF study notes…",
        reply_markup=feature_keyboard(),
    )
    with path.open("rb") as fh:
        await update.message.reply_document(
            document=fh,
            filename=path.name,
            caption=f"UG Medicine — {label}",
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

    if intent in ("question", "case"):
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

    # Difficulty selection (only when waiting for MCQ/case difficulty)
    if text in LABEL_TO_DIFFICULTY:
        difficulty = LABEL_TO_DIFFICULTY[text]
        mode = context.user_data.get("quiz_mode")
        if mode == "question":
            await send_question(update, context, difficulty)
            return
        if mode == "case":
            await send_case(update, context, difficulty)
            return
        # If difficulty pressed without mode, ask them to pick feature first
        if current_specialty(context):
            await safe_reply(
                update,
                "First choose *Short MCQ* or *Case-based Question*, then a difficulty.",
                reply_markup=feature_keyboard(),
            )
        else:
            await show_specialty_menu(update, context)
        return

    intent = detect_feature_intent(text)
    if intent:
        await dispatch_feature(update, context, intent)
        return

    if current_specialty(context):
        mode = context.user_data.get("quiz_mode")
        if mode in ("question", "case"):
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
            item = SPECIALTIES[specialty_key]["questions"][difficulty][idx]
        except (ValueError, IndexError, KeyError, TypeError):
            await safe_edit(
                query,
                "This question expired. Open *Short MCQ* and pick a difficulty again.",
            )
            return
        label = specialty_label(specialty_key)
        await safe_edit(query, format_question_result(item, choice, label, difficulty))
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
        await safe_edit(query, format_case_result(item, label, difficulty))
        return


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(update, "✅ Pharmacy bot is online. Send /start to open the specialty menu.")


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
    token = os.getenv("PHARMACY_BOT_TOKEN") or os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit(
            "PHARMACY_BOT_TOKEN (or BOT_TOKEN) is missing. Copy .env.example to .env and set it."
        )
    log.info("Preparing PDFs…")
    ensure_pdfs(PDF_DIR)
    app = (
        Application.builder()
        .token(token)
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