"""CharaNas hub bot — routes users to Medicine, Dentistry, or Pharmacy bots."""

from __future__ import annotations

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(Path(__file__).resolve().parent / "bot.log"),
    ],
)
log = logging.getLogger("charanas-hub-bot")

load_dotenv(Path(__file__).resolve().parent / ".env")

# Department bots (Telegram usernames without @)
DEPARTMENTS = [
    {
        "key": "medicine",
        "label": "Medicine",
        "username": os.getenv("MEDICINE_BOT_USERNAME", "CharanasMedicine_bot"),
        "blurb": "Undergraduate medicine specialties, MCQs, cases, PDFs, and book sources.",
    },
    {
        "key": "dentistry",
        "label": "Dentistry",
        "username": os.getenv("DENTISTRY_BOT_USERNAME", "Charanasdentistry_bot"),
        "blurb": "Undergraduate dentistry specialties, MCQs, cases, PDFs, and book sources.",
    },
    {
        "key": "pharmacy",
        "label": "Pharmacy",
        "username": os.getenv("PHARMACY_BOT_USERNAME", "Charanaspharmacy_bot"),
        "blurb": "Undergraduate pharmacy specialties, MCQs, cases, PDFs, and book sources.",
    },
]


def bot_url(username: str) -> str:
    return f"https://t.me/{username}?start=from_hub"


def menu_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(f"Open {d['label']} bot", url=bot_url(d["username"]))]
        for d in DEPARTMENTS
    ]
    return InlineKeyboardMarkup(rows)


def welcome_text() -> str:
    lines = [
        "Welcome to *CharaNas*",
        "",
        "Choose your field below. You will be taken to that department's study bot:",
        "",
    ]
    for d in DEPARTMENTS:
        lines.append(f"• *{d['label']}* — @{d['username']}")
        lines.append(f"  _{d['blurb']}_")
        lines.append("")
    lines.append("Tap a button to open the bot for your field.")
    return "\n".join(lines)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        welcome_text(),
        parse_mode="Markdown",
        reply_markup=menu_keyboard(),
        disable_web_page_preview=True,
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("✅ CharaNas hub bot is online. Send /start to choose a field.")


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip().lower()
    for d in DEPARTMENTS:
        if d["label"].lower() in text or d["key"] in text:
            await update.message.reply_text(
                f"Open the *{d['label']}* bot:\n@{d['username']}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(f"Go to {d['label']}", url=bot_url(d["username"]))]]
                ),
                disable_web_page_preview=True,
            )
            return

    await update.message.reply_text(
        "Please choose a field from the buttons below, or send /start.",
        reply_markup=menu_keyboard(),
    )


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.error("Handler error: %s", context.error)


def main() -> None:
    token = os.getenv("HUB_BOT_TOKEN") or os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit(
            "HUB_BOT_TOKEN is missing. Copy .env.example to .env and set HUB_BOT_TOKEN."
        )

    app = (
        Application.builder()
        .token(token)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(on_error)

    log.info("CharaNas hub bot starting…")
    print("CharaNas hub bot running…")
    app.run_polling(drop_pending_updates=False, allowed_updates=Update.ALL_TYPES, bootstrap_retries=5)


if __name__ == "__main__":
    main()
