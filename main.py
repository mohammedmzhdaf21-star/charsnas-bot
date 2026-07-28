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
    CASES,
    QUESTIONS,
    format_book_sources,
    format_case_prompt,
    format_case_result,
    format_question_prompt,
    format_question_result,
    help_text,
    option_letter,
    pick_case,
    pick_question,
)
from generate_pdfs import PDF_DIR, ensure_pdfs

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

# Main feature buttons shown to the user
BTN_MCQ = "Short MCQ"
BTN_CASE = "Case-based Question"
BTN_PDF = "PDF files"
BTN_BOOKS = "Book source"

MENU_LABELS = {
    BTN_MCQ: "question",
    BTN_CASE: "case",
    BTN_PDF: "pdf",
    BTN_BOOKS: "books",
}

INTENT_PATTERNS = {
    "question": [
        r"\bcreate\s+questions?\b",
        r"\bgenerate\s+questions?\b",
        r"\bmake\s+(me\s+)?(a\s+)?questions?\b",
        r"\bgive\s+(me\s+)?(a\s+)?questions?\b",
        r"\bshort\s+mcq\b",
        r"\bmcq\b",
    ],
    "case": [
        r"\bcase[-\s]?based\b",
        r"\bcase\s+questions?\b",
        r"\bclinical\s+case\b",
    ],
    "pdf": [
        r"\bpdf\b",
        r"\bgive\s+me\s+pdf",
        r"\bpdf\s+files?\b",
        r"\bsend\s+(me\s+)?(the\s+)?pdf",
        r"\bstudy\s+notes?\b",
    ],
    "books": [
        r"\bbook\s+sources?\b",
        r"\bbooks?\s+sources?\b",
        r"\btextbooks?\b",
        r"\breferences?\b",
    ],
}


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(BTN_MCQ), KeyboardButton(BTN_CASE)],
            [KeyboardButton(BTN_PDF), KeyboardButton(BTN_BOOKS)],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def detect_intent(text: str) -> str | None:
    stripped = text.strip()
    if stripped in MENU_LABELS:
        return MENU_LABELS[stripped]

    normalized = " ".join(stripped.lower().split())
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, normalized):
                return intent
    return None


def question_keyboard(idx: int, item: dict) -> InlineKeyboardMarkup:
    rows = []
    row = []
    for option in item["options"]:
        letter = option_letter(option)
        row.append(
            InlineKeyboardButton(
                option,
                callback_data=f"q:{idx}:{letter}",
            )
        )
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(rows)


def case_keyboard(idx: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("Reveal answer", callback_data=f"c:{idx}")]]
    )


async def send_menu(update: Update, text: str | None = None) -> None:
    await update.message.reply_text(
        text or help_text(),
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )


async def send_question(update: Update) -> None:
    idx, item = pick_question()
    await update.message.reply_text(
        format_question_prompt(item),
        parse_mode="Markdown",
        reply_markup=question_keyboard(idx, item),
    )


async def send_case(update: Update) -> None:
    idx, item = pick_case()
    await update.message.reply_text(
        format_case_prompt(item),
        parse_mode="Markdown",
        reply_markup=case_keyboard(idx),
    )


async def send_books(update: Update) -> None:
    await update.message.reply_text(
        format_book_sources(),
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )


async def send_pdfs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    paths = ensure_pdfs(PDF_DIR)
    await update.message.reply_text(
        "📄 Sending undergraduate medicine PDF study files…",
        reply_markup=main_menu_keyboard(),
    )
    for path in paths:
        with path.open("rb") as fh:
            await update.message.reply_document(
                document=fh,
                filename=path.name,
                caption=f"UG Medicine — {path.stem.replace('_', ' ')}",
            )


async def dispatch_intent(
    update: Update, context: ContextTypes.DEFAULT_TYPE, intent: str
) -> None:
    if intent == "question":
        await send_question(update)
    elif intent == "case":
        await send_case(update)
    elif intent == "pdf":
        await send_pdfs(update, context)
    elif intent == "books":
        await send_books(update)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_menu(update)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_menu(update)


async def question_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_question(update)


async def case_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_case(update)


async def books_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_books(update)


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text or ""
    intent = detect_intent(text)

    if intent:
        await dispatch_intent(update, context, intent)
        return

    await send_menu(
        update,
        "I only help with *undergraduate medicine*.\n\n"
        "Please choose a feature from the buttons below.",
    )


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data or ""

    if data.startswith("q:"):
        try:
            _, idx_s, choice = data.split(":", 2)
            idx = int(idx_s)
            item = QUESTIONS[idx]
        except (ValueError, IndexError, KeyError):
            await query.edit_message_text(
                "This question expired. Tap *Short MCQ* again.",
                parse_mode="Markdown",
            )
            return

        text = format_question_result(item, choice)
        await query.edit_message_text(text, parse_mode="Markdown")
        return

    if data.startswith("c:"):
        try:
            idx = int(data.split(":", 1)[1])
            item = CASES[idx]
        except (ValueError, IndexError):
            await query.edit_message_text(
                "This case expired. Tap *Case-based Question* again.",
                parse_mode="Markdown",
            )
            return
        await query.edit_message_text(format_case_result(item), parse_mode="Markdown")
        return


def main() -> None:
    ensure_pdfs(PDF_DIR)
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("question", question_cmd))
    app.add_handler(CommandHandler("case", case_cmd))
    app.add_handler(CommandHandler("pdf", send_pdfs))
    app.add_handler(CommandHandler("books", books_cmd))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    print("CharaNas Medicine bot running (UG Medicine)…")
    app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
