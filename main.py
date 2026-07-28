import re
from pathlib import Path

from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from content import format_book_sources, format_case, format_question, help_text
from generate_pdfs import PDF_DIR, ensure_pdfs

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

# Intent patterns (natural language for UG medicine students)
INTENT_PATTERNS = {
    "question": [
        r"\bcreate\s+questions?\b",
        r"\bgenerate\s+questions?\b",
        r"\bmake\s+(me\s+)?(a\s+)?questions?\b",
        r"\bgive\s+(me\s+)?(a\s+)?questions?\b",
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


def detect_intent(text: str) -> str | None:
    normalized = " ".join(text.lower().strip().split())
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, normalized):
                return intent
    return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(help_text(), parse_mode="Markdown")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(help_text(), parse_mode="Markdown")


async def question_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(format_question(), parse_mode="Markdown")


async def case_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(format_case(), parse_mode="Markdown")


async def books_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(format_book_sources(), parse_mode="Markdown")


async def send_pdfs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    paths = ensure_pdfs(PDF_DIR)
    await update.message.reply_text(
        "📄 Sending undergraduate medicine PDF study files…"
    )
    for path in paths:
        with path.open("rb") as fh:
            await update.message.reply_document(
                document=fh,
                filename=path.name,
                caption=f"UG Medicine — {path.stem.replace('_', ' ')}",
            )


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text or ""
    intent = detect_intent(text)

    if intent == "question":
        await update.message.reply_text(format_question(), parse_mode="Markdown")
    elif intent == "case":
        await update.message.reply_text(format_case(), parse_mode="Markdown")
    elif intent == "pdf":
        await send_pdfs(update, context)
    elif intent == "books":
        await update.message.reply_text(format_book_sources(), parse_mode="Markdown")
    else:
        await update.message.reply_text(
            "I only help with *undergraduate medicine*.\n\n"
            "Try:\n"
            "• create question\n"
            "• case based question\n"
            "• give me pdf files\n"
            "• book source\n\n"
            "Or /help",
            parse_mode="Markdown",
        )


def main() -> None:
    ensure_pdfs(PDF_DIR)
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("question", question_cmd))
    app.add_handler(CommandHandler("case", case_cmd))
    app.add_handler(CommandHandler("pdf", send_pdfs))
    app.add_handler(CommandHandler("books", books_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    print("CharaNas Medicine bot running (UG Medicine)…")
    app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
