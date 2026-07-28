import re
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
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from content import (
    SPECIALTIES,
    SPECIALTY_ORDER,
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

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

BTN_MCQ = "Short MCQ"
BTN_CASE = "Case-based Question"
BTN_PDF = "PDF files"
BTN_BOOKS = "Book source"
BTN_BACK = "Change specialty"

FEATURE_LABELS = {
    BTN_MCQ: "question",
    BTN_CASE: "case",
    BTN_PDF: "pdf",
    BTN_BOOKS: "books",
    BTN_BACK: "back",
}

INTENT_PATTERNS = {
    "question": [
        r"\bcreate\s+questions?\b",
        r"\bshort\s+mcq\b",
        r"\bmcq\b",
    ],
    "case": [
        r"\bcase[-\s]?based\b",
        r"\bcase\s+questions?\b",
    ],
    "pdf": [
        r"\bpdf\b",
        r"\bpdf\s+files?\b",
    ],
    "books": [
        r"\bbook\s+sources?\b",
        r"\btextbooks?\b",
    ],
    "back": [
        r"\bchange\s+specialty\b",
        r"\bback\b",
        r"\bmenu\b",
    ],
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
            [KeyboardButton(BTN_BACK)],
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


def question_keyboard(specialty_key: str, idx: int, item: dict) -> InlineKeyboardMarkup:
    rows = []
    row = []
    for option in item["options"]:
        letter = option_letter(option)
        row.append(
            InlineKeyboardButton(
                option,
                callback_data=f"q:{specialty_key}:{idx}:{letter}",
            )
        )
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(rows)


def case_keyboard(specialty_key: str, idx: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("Reveal answer", callback_data=f"c:{specialty_key}:{idx}")]]
    )


async def show_specialty_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str | None = None) -> None:
    context.user_data["specialty"] = None
    await update.message.reply_text(
        text or specialty_menu_text(),
        parse_mode="Markdown",
        reply_markup=specialty_keyboard(),
    )


async def show_feature_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, specialty_key: str) -> None:
    context.user_data["specialty"] = specialty_key
    await update.message.reply_text(
        feature_menu_text(specialty_key),
        parse_mode="Markdown",
        reply_markup=feature_keyboard(),
    )


async def require_specialty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str | None:
    key = current_specialty(context)
    if key:
        return key
    await show_specialty_menu(
        update,
        context,
        "Please choose a *specialty* first.",
    )
    return None


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    store = remaining_map(context, "remaining_questions")
    remaining = store.get(specialty_key)
    idx, item, remaining = pick_question(specialty_key, remaining)
    store[specialty_key] = remaining

    label = specialty_label(specialty_key)
    await update.message.reply_text(
        format_question_prompt(item, label),
        parse_mode="Markdown",
        reply_markup=question_keyboard(specialty_key, idx, item),
    )


async def send_case(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    store = remaining_map(context, "remaining_cases")
    remaining = store.get(specialty_key)
    idx, item, remaining = pick_case(specialty_key, remaining)
    store[specialty_key] = remaining

    label = specialty_label(specialty_key)
    await update.message.reply_text(
        format_case_prompt(item, label),
        parse_mode="Markdown",
        reply_markup=case_keyboard(specialty_key, idx),
    )


async def send_books(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return
    await update.message.reply_text(
        format_book_sources(specialty_key),
        parse_mode="Markdown",
        reply_markup=feature_keyboard(),
    )


async def send_pdfs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    specialty_key = await require_specialty(update, context)
    if not specialty_key:
        return

    path = pdf_for_specialty(specialty_key, PDF_DIR)
    label = specialty_label(specialty_key)
    await update.message.reply_text(
        f"📄 Sending *{label}* PDF study notes…",
        parse_mode="Markdown",
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
    if intent == "back":
        await show_specialty_menu(update, context)
    elif intent == "question":
        await send_question(update, context)
    elif intent == "case":
        await send_case(update, context)
    elif intent == "pdf":
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

    # Specialty selection (first menu)
    specialty_key = label_to_key(text)
    if specialty_key:
        await show_feature_menu(update, context, specialty_key)
        return

    # Feature selection (second menu)
    intent = detect_feature_intent(text)
    if intent:
        await dispatch_feature(update, context, intent)
        return

    if current_specialty(context):
        await update.message.reply_text(
            "Please choose a feature from the buttons below, or tap *Change specialty*.",
            parse_mode="Markdown",
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
            _, specialty_key, idx_s, choice = data.split(":", 3)
            idx = int(idx_s)
            item = SPECIALTIES[specialty_key]["questions"][idx]
        except (ValueError, IndexError, KeyError):
            await query.edit_message_text(
                "This question expired. Tap *Short MCQ* again.",
                parse_mode="Markdown",
            )
            return
        label = specialty_label(specialty_key)
        await query.edit_message_text(
            format_question_result(item, choice, label),
            parse_mode="Markdown",
        )
        return

    if data.startswith("c:"):
        try:
            _, specialty_key, idx_s = data.split(":", 2)
            idx = int(idx_s)
            item = SPECIALTIES[specialty_key]["cases"][idx]
        except (ValueError, IndexError, KeyError):
            await query.edit_message_text(
                "This case expired. Tap *Case-based Question* again.",
                parse_mode="Markdown",
            )
            return
        label = specialty_label(specialty_key)
        await query.edit_message_text(
            format_case_result(item, label),
            parse_mode="Markdown",
        )
        return


def main() -> None:
    ensure_pdfs(PDF_DIR)
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("question", send_question))
    app.add_handler(CommandHandler("case", send_case))
    app.add_handler(CommandHandler("pdf", send_pdfs))
    app.add_handler(CommandHandler("books", send_books))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    print("CharaNas Medicine bot running (UG Medicine specialties)…")
    app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
