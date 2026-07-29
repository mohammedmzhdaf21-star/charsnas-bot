"""CharaNas hub bot — routes users to Medicine, Dentistry, Pharmacy, MLS, or Nursing bots."""

from __future__ import annotations

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.error import BadRequest
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
    {
        "key": "mls",
        "label": "MLS",
        "username": os.getenv("MLS_BOT_USERNAME", "CharanasMLS_bot"),
        "blurb": "Undergraduate medical laboratory science specialties, MCQs, cases, PDFs, and book sources.",
    },
    {
        "key": "nursing",
        "label": "Nursing",
        "username": os.getenv("NURSING_BOT_USERNAME", "CharanasNursing_bot"),
        "blurb": "Undergraduate nursing specialties, MCQs, cases, PDFs, and book sources.",
    },
]

LABEL_TO_DEPT = {d["label"]: d for d in DEPARTMENTS}


def bot_url(username: str) -> str:
    return f"https://t.me/{username}?start=from_hub"


def field_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Medicine"), KeyboardButton("Dentistry")],
            [KeyboardButton("Pharmacy"), KeyboardButton("MLS")],
            [KeyboardButton("Nursing")],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def link_keyboard(dept: dict) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(f"Open {dept['label']} bot", url=bot_url(dept["username"]))]]
    )


def all_links_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(d["label"], url=bot_url(d["username"]))]
            for d in DEPARTMENTS
        ]
    )


def welcome_text() -> str:
    lines = [
        "Welcome to CharaNas Education Center",
        "",
        "Choose your field:",
        "",
    ]
    for d in DEPARTMENTS:
        lines.append(f"- {d['label']}")
        lines.append(f"  {d['blurb']}")
        lines.append("")
    lines.append("Tap a field button below, then Open to go to that bot.")
    return "\n".join(lines)


async def safe_reply(update: Update, text: str, reply_markup=None) -> None:
    message = update.effective_message
    if not message:
        return
    try:
        await message.reply_text(text, reply_markup=reply_markup, disable_web_page_preview=True)
    except BadRequest as exc:
        log.warning("Send failed: %s", exc)
        await message.reply_text(text)


async def send_department_link(update: Update, dept: dict) -> None:
    await safe_reply(
        update,
        f"{dept['label']} bot\n@{dept['username']}\n\n{dept['blurb']}\n\nTap the button below to open it:",
        reply_markup=link_keyboard(dept),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Persistent field buttons + inline deep links
    await safe_reply(update, welcome_text(), reply_markup=field_reply_keyboard())
    await safe_reply(
        update,
        "Or tap a field here to open that bot directly:",
        reply_markup=all_links_keyboard(),
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(update, "CharaNas hub bot is online. Send /start to choose a field.")


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    dept = LABEL_TO_DEPT.get(text)
    if dept:
        await send_department_link(update, dept)
        return

    lowered = text.lower()
    for d in DEPARTMENTS:
        if d["label"].lower() in lowered or d["key"] in lowered:
            await send_department_link(update, d)
            return
    if "laboratory" in lowered or "lab science" in lowered:
        await send_department_link(update, LABEL_TO_DEPT["MLS"])
        return

    if "nurse" in lowered:
        await send_department_link(update, LABEL_TO_DEPT["Nursing"])
        return

    await safe_reply(
        update,
        "Please choose Medicine, Dentistry, Pharmacy, MLS, or Nursing.",
        reply_markup=field_reply_keyboard(),
    )
    await safe_reply(
        update,
        "Direct links:",
        reply_markup=all_links_keyboard(),
    )


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.error("Handler error: %s", context.error)
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "Something went wrong. Please send /start again."
            )
        except Exception:
            pass


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
    app.run_polling(
        drop_pending_updates=False,
        allowed_updates=Update.ALL_TYPES,
        bootstrap_retries=5,
    )


if __name__ == "__main__":
    main()
