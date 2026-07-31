"""Helpers so long Telegram quiz/case answers are shown in full."""

from __future__ import annotations

import logging

from telegram.error import BadRequest

log = logging.getLogger("charanas-text")

# Stay under Telegram's 4096 limit with a safety margin
TG_TEXT_LIMIT = 3900


def chunk_text(text: str, limit: int = TG_TEXT_LIMIT) -> list[str]:
    """Split text into Telegram-safe chunks on newlines when possible."""
    text = text or ""
    if len(text) <= limit:
        return [text]
    chunks: list[str] = []
    while text:
        if len(text) <= limit:
            chunks.append(text)
            break
        cut = text.rfind("\n", 0, limit)
        if cut < limit // 3:
            cut = limit
        chunks.append(text[:cut].rstrip())
        text = text[cut:].lstrip("\n")
    return chunks or [""]


def strip_markdown_markers(text: str) -> str:
    """Light cleanup so plain-text sends stay readable."""
    return (
        text.replace("*", "")
        .replace("_", "")
        .replace("`", "")
    )


async def send_full_text(message, text: str, reply_markup=None) -> None:
    """Send the entire text, splitting into multiple messages if needed (plain text)."""
    parts = chunk_text(text)
    for i, part in enumerate(parts):
        markup = reply_markup if i == 0 else None
        await message.reply_text(part, reply_markup=markup, disable_web_page_preview=True)


async def edit_or_send_full(query, text: str) -> None:
    """
    Show the full answer: edit the original message with part 1,
    then send any remaining parts as follow-up messages.
    Uses plain text so Markdown cannot hide or break long answers.
    """
    plain = strip_markdown_markers(text)
    parts = chunk_text(plain)
    first, rest = parts[0], parts[1:]
    try:
        await query.edit_message_text(first)
    except BadRequest as exc:
        log.warning("edit_message_text failed (%s) — sending as new message(s)", exc)
        await query.message.reply_text(first, disable_web_page_preview=True)
    for part in rest:
        await query.message.reply_text(part, disable_web_page_preview=True)
