"""CharaNas hub bot — routes users to department bots after optional channel join."""

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
from telegram.error import BadRequest, Forbidden, TelegramError
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    ChatMemberHandler,
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
        "username": os.getenv("NURSING_BOT_USERNAME", "Charanasnursing_bot"),
        "blurb": "Undergraduate nursing specialties, MCQs, cases, PDFs, and book sources.",
    },
]

LABEL_TO_DEPT = {d["label"]: d for d in DEPARTMENTS}
KEY_TO_DEPT = {d["key"]: d for d in DEPARTMENTS}

# Channel join gate (Telegram cannot force-join; we require join then verify)
CHANNEL_USERNAME = (os.getenv("CHANNEL_USERNAME") or "").strip().lstrip("@")
CHANNEL_INVITE_LINK = (os.getenv("CHANNEL_INVITE_LINK") or "").strip()
_CHANNEL_ID_FILE = Path(__file__).resolve().parent / "channel_chat_id.txt"


def _load_channel_chat_id() -> str:
    env_id = (os.getenv("CHANNEL_CHAT_ID") or "").strip()
    if env_id:
        return env_id
    if _CHANNEL_ID_FILE.exists():
        return _CHANNEL_ID_FILE.read_text().strip()
    return ""


CHANNEL_CHAT_ID = _load_channel_chat_id()  # e.g. -100xxxxxxxxxx
REQUIRE_CHANNEL = (
    os.getenv(
        "REQUIRE_CHANNEL",
        "1" if (CHANNEL_USERNAME or CHANNEL_CHAT_ID or CHANNEL_INVITE_LINK) else "0",
    )
    .strip()
    .lower()
    in {"1", "true", "yes", "on"}
)

JOINED_STATUSES = {"creator", "administrator", "member", "restricted"}

# Optional Telegram shared-folder link (t.me/addlist/...).
# Shareable folders can include channels + groups (NOT bot DMs directly).
# Workaround: put a Campus group (with all bots as members) + channel in the folder.
FOLDER_INVITE_LINK = (os.getenv("FOLDER_INVITE_LINK") or "").strip()
FOLDER_NAME = (os.getenv("FOLDER_NAME") or "CharaNas").strip() or "CharaNas"
CAMPUS_GROUP_INVITE = (os.getenv("CAMPUS_GROUP_INVITE") or "").strip()
CAMPUS_GROUP_CHAT_ID = (os.getenv("CAMPUS_GROUP_CHAT_ID") or "").strip()
HUB_BOT_USERNAME = (os.getenv("HUB_BOT_USERNAME") or "Charanaseducenter_bot").strip().lstrip("@")
BTN_FOLDER = f"{FOLDER_NAME} folder"


def bot_url(username: str) -> str:
    return f"https://t.me/{username}?start=from_hub"


def channel_url() -> str | None:
    if CHANNEL_INVITE_LINK:
        return CHANNEL_INVITE_LINK
    if CHANNEL_USERNAME:
        return f"https://t.me/{CHANNEL_USERNAME}"
    return None


def folder_url() -> str | None:
    link = FOLDER_INVITE_LINK
    if link and ("t.me/addlist/" in link or link.startswith("tg://")):
        return link
    return None


def campus_url() -> str | None:
    return CAMPUS_GROUP_INVITE or None


def channel_ref() -> str | int | None:
    """Chat id/username passed to getChatMember."""
    if CHANNEL_CHAT_ID:
        try:
            return int(CHANNEL_CHAT_ID)
        except ValueError:
            return CHANNEL_CHAT_ID
    if CHANNEL_USERNAME:
        return f"@{CHANNEL_USERNAME}"
    return None


def field_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Medicine"), KeyboardButton("Dentistry")],
            [KeyboardButton("Pharmacy"), KeyboardButton("MLS")],
            [KeyboardButton("Nursing")],
            [KeyboardButton(BTN_FOLDER)],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def link_keyboard(dept: dict) -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(f"Open {dept['label']} bot", url=bot_url(dept["username"]))]]
    furl = folder_url()
    curl = channel_url()
    camp = campus_url()
    if furl:
        rows.append([InlineKeyboardButton(f"Add {FOLDER_NAME} folder", url=furl)])
    if camp:
        rows.append([InlineKeyboardButton("Open campus group (bots inside)", url=camp)])
    if curl and not furl:
        rows.append([InlineKeyboardButton("Join CharaNas channel", url=curl)])
    return InlineKeyboardMarkup(rows)


def pick_field_keyboard() -> InlineKeyboardMarkup:
    """Inline field picks use callbacks so the channel gate can run."""
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(d["label"], callback_data=f"dept:{d['key']}")] for d in DEPARTMENTS]
    )


def start_extra_keyboard() -> InlineKeyboardMarkup | None:
    """Folder / channel / campus buttons shown on /start."""
    rows: list[list[InlineKeyboardButton]] = []
    furl = folder_url()
    camp = campus_url()
    curl = channel_url()
    if furl:
        rows.append([InlineKeyboardButton(f"Add {FOLDER_NAME} folder", url=furl)])
    if camp:
        rows.append([InlineKeyboardButton("Campus group (bots live here)", url=camp)])
    if curl:
        label = "Join channel" if furl or camp else "Join CharaNas channel"
        rows.append([InlineKeyboardButton(label, url=curl)])
    return InlineKeyboardMarkup(rows) if rows else None


def join_gate_keyboard(dept_key: str) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    furl = folder_url()
    curl = channel_url()
    camp = campus_url()
    step = 1
    if furl:
        rows.append([InlineKeyboardButton(f"{step}) Add {FOLDER_NAME} folder", url=furl)])
        step += 1
    elif curl:
        rows.append([InlineKeyboardButton(f"{step}) Join the channel", url=curl)])
        step += 1
    if camp:
        rows.append([InlineKeyboardButton(f"{step}) Open campus group", url=camp)])
        step += 1
    if curl and furl:
        rows.append([InlineKeyboardButton("Or join channel only", url=curl)])
    rows.append(
        [InlineKeyboardButton(f"{step}) I joined — Continue", callback_data=f"joined:{dept_key}")]
    )
    return InlineKeyboardMarkup(rows)


def welcome_text() -> str:
    lines = [
        f"Welcome to {FOLDER_NAME} Education Center",
        "",
        "Choose your field:",
        "",
    ]
    for d in DEPARTMENTS:
        lines.append(f"- {d['label']}")
        lines.append(f"  {d['blurb']}")
        lines.append("")
    if folder_url() or campus_url():
        lines.append(f"Folder setup: channel + campus group (bots are members of the group).")
        lines.append(f"Tap {BTN_FOLDER} for the one-tap add link and how to keep bots in the tab.")
        lines.append("")
    elif REQUIRE_CHANNEL and channel_url():
        lines.append("Join our Telegram channel first, then Continue.")
        lines.append("")
    lines.append("Tap a field button below.")
    return "\n".join(lines)


def folder_howto_text() -> str:
    """How bots end up in the folder despite Telegram's share-folder limits."""
    lines = [
        f"How {FOLDER_NAME} folder works",
        "",
        "Telegram will not put bot chats inside a *shared* folder invite.",
        "So we use this working setup:",
        "",
        "1) Shared folder = Channel + Campus group",
        "2) All study bots are *members/admins of the campus group*",
        "   → opening the folder shows the group → bots are inside it",
        "3) After you Open a department bot once, add that bot chat to the",
        f"   {FOLDER_NAME} folder on your phone (Edit folder → Included chats)",
        "   → the bot then appears as its own chat in your folder tab too",
        "",
    ]
    if folder_url():
        lines.append(f"Folder link: {folder_url()}")
    else:
        lines.append("Folder link: not set yet (admin: create folder + paste FOLDER_INVITE_LINK).")
    if campus_url():
        lines.append(f"Campus group: {campus_url()}")
    else:
        lines.append("Campus group: not set yet (admin: create group, add all bots, paste CAMPUS_GROUP_INVITE).")
    if channel_url():
        lines.append(f"Channel: {channel_url()}")
    lines.extend(
        [
            "",
            "Admin setup checklist:",
            "1. Create group: CharaNas Campus",
            "2. Add as admin: hub + Medicine + Dentistry + Pharmacy + MLS + Nursing bots",
            "3. Settings → Chat Folders → New folder → add Channel + Campus group",
            "4. Share folder → copy https://t.me/addlist/... link",
            "5. Put FOLDER_INVITE_LINK and CAMPUS_GROUP_INVITE in hub/.env and restart",
        ]
    )
    return "\n".join(lines)


def bot_in_folder_tip(dept: dict) -> str:
    return (
        f"Keep @{dept['username']} in your {FOLDER_NAME} folder:\n"
        f"1) Open the bot (button above)\n"
        f"2) Telegram → Settings → Chat Folders → {FOLDER_NAME}\n"
        f"3) Included chats → add @{dept['username']}\n\n"
        "That is how bot chats appear in the folder tab "
        "(shared folder invites cannot include bots directly)."
    )


async def safe_reply(update: Update, text: str, reply_markup=None) -> None:
    message = update.effective_message
    if not message:
        return
    try:
        await message.reply_text(text, reply_markup=reply_markup, disable_web_page_preview=True)
    except BadRequest as exc:
        log.warning("Send failed: %s", exc)
        await message.reply_text(text)


def can_verify_membership() -> bool:
    return channel_ref() is not None


async def user_in_channel(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> bool | None:
    """Return True/False when verifiable; None when only invite-link soft gate is available."""
    if not REQUIRE_CHANNEL:
        return True
    chat = channel_ref()
    if chat is None:
        # Private invite configured but chat id unknown yet — soft gate
        return None
    try:
        member = await context.bot.get_chat_member(chat_id=chat, user_id=user_id)
        status = getattr(member, "status", None)
        ok = status in JOINED_STATUSES
        log.info("Channel check user=%s status=%s ok=%s", user_id, status, ok)
        return ok
    except Forbidden as exc:
        log.error(
            "Cannot check channel membership (is hub bot an admin of the channel?): %s",
            exc,
        )
        # Soft-fail: still show join link, but allow continue so students are not locked out
        return None
    except TelegramError as exc:
        log.warning("getChatMember failed: %s", exc)
        return False


def persist_channel_chat_id(chat_id: int) -> None:
    global CHANNEL_CHAT_ID
    CHANNEL_CHAT_ID = str(chat_id)
    _CHANNEL_ID_FILE.write_text(str(chat_id) + "\n")
    log.info("Saved channel chat id %s to %s", chat_id, _CHANNEL_ID_FILE.name)


async def send_department_link(update: Update, dept: dict) -> None:
    await safe_reply(
        update,
        f"{dept['label']} bot\n@{dept['username']}\n\n{dept['blurb']}\n\nTap the button below to open it:",
        reply_markup=link_keyboard(dept),
    )
    await safe_reply(update, bot_in_folder_tip(dept), reply_markup=start_extra_keyboard())


async def send_folder_help(update: Update) -> None:
    await safe_reply(update, folder_howto_text(), reply_markup=start_extra_keyboard() or field_reply_keyboard())
    await safe_reply(update, "Choose a field anytime:", reply_markup=field_reply_keyboard())


async def offer_department(
    update: Update, context: ContextTypes.DEFAULT_TYPE, dept: dict
) -> None:
    """Gate on channel membership, then open the department bot."""
    user = update.effective_user
    if not user:
        return

    context.user_data["pending_dept"] = dept["key"]

    status = await user_in_channel(context, user.id)
    if status is True or (status is None and context.user_data.get("channel_soft_ok")):
        await send_department_link(update, dept)
        return

    await safe_reply(
        update,
        f"Before opening {dept['label']}, join the {FOLDER_NAME} channel"
        + (" / folder" if folder_url() else "")
        + ".\n\n"
        "Bots appear in the folder through the campus group + adding each bot chat once.\n"
        "Tap Join / Add folder, then I joined — Continue.",
        reply_markup=join_gate_keyboard(dept["key"]),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(update, welcome_text(), reply_markup=field_reply_keyboard())
    extra = start_extra_keyboard()
    if extra:
        await safe_reply(
            update,
            "Channel / folder:",
            reply_markup=extra,
        )
    await safe_reply(
        update,
        "Or tap a field here:",
        reply_markup=pick_field_keyboard(),
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def folder_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_folder_help(update)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(update, "CharaNas hub bot is online. Send /start to choose a field.")


async def post_campus_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Admin helper: post Open-bot buttons into the campus group."""
    if not CAMPUS_GROUP_CHAT_ID:
        await safe_reply(
            update,
            "Set CAMPUS_GROUP_CHAT_ID in hub/.env first (numeric id like -100...).",
        )
        return
    try:
        chat_id = int(CAMPUS_GROUP_CHAT_ID)
    except ValueError:
        chat_id = CAMPUS_GROUP_CHAT_ID

    rows = [[InlineKeyboardButton(d["label"], url=bot_url(d["username"]))] for d in DEPARTMENTS]
    if channel_url():
        rows.append([InlineKeyboardButton("Channel", url=channel_url())])
    if folder_url():
        rows.append([InlineKeyboardButton(f"Add {FOLDER_NAME} folder", url=folder_url())])
    text = (
        f"{FOLDER_NAME} campus menu\n\n"
        "Bots in this group are part of the shared folder.\n"
        "Tap a department to open its study bot in private chat:"
    )
    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=InlineKeyboardMarkup(rows),
            disable_web_page_preview=True,
        )
        await safe_reply(update, "Posted campus menu to the group.")
    except TelegramError as exc:
        log.error("post_campus_menu failed: %s", exc)
        await safe_reply(
            update,
            f"Could not post to campus group: {exc}\n"
            "Make sure the hub bot is an admin there.",
        )


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    if text == BTN_FOLDER or text.lower() in {"folder", "folders", f"{FOLDER_NAME.lower()} folder"}:
        await send_folder_help(update)
        return

    dept = LABEL_TO_DEPT.get(text)
    if dept:
        await offer_department(update, context, dept)
        return

    lowered = text.lower()
    for d in DEPARTMENTS:
        if d["label"].lower() in lowered or d["key"] in lowered:
            await offer_department(update, context, d)
            return
    if "laboratory" in lowered or "lab science" in lowered:
        await offer_department(update, context, LABEL_TO_DEPT["MLS"])
        return

    if "nurse" in lowered:
        await offer_department(update, context, LABEL_TO_DEPT["Nursing"])
        return

    await safe_reply(
        update,
        "Please choose Medicine, Dentistry, Pharmacy, MLS, or Nursing.",
        reply_markup=field_reply_keyboard(),
    )
    await safe_reply(
        update,
        "Or tap a field here:",
        reply_markup=pick_field_keyboard(),
    )


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if not query:
        return
    await query.answer()
    data = query.data or ""
    user = update.effective_user
    if not user:
        return

    async def open_dept(dept: dict, thanks: bool = False) -> None:
        prefix = "Thanks for joining!\n\n" if thanks else ""
        await query.edit_message_text(
            f"{prefix}{dept['label']} bot\n@{dept['username']}\n\n{dept['blurb']}\n\nTap below to open it:"
        )
        await query.message.reply_text(
            f"Open {dept['label']}:",
            reply_markup=link_keyboard(dept),
            disable_web_page_preview=True,
        )
        await query.message.reply_text(
            bot_in_folder_tip(dept),
            reply_markup=start_extra_keyboard(),
            disable_web_page_preview=True,
        )

    if data.startswith("dept:"):
        key = data.split(":", 1)[1]
        dept = KEY_TO_DEPT.get(key)
        if not dept:
            await query.edit_message_text("Unknown field. Send /start and try again.")
            return
        context.user_data["pending_dept"] = key
        status = await user_in_channel(context, user.id)
        if status is True or (status is None and context.user_data.get("channel_soft_ok")):
            await open_dept(dept)
            return
        await query.edit_message_text(
            f"Before opening {dept['label']}, join the {FOLDER_NAME} channel"
            + (" / folder" if folder_url() else "")
            + ".\n\n"
            "Bots appear in the folder through the campus group + adding each bot chat once.\n"
            "Tap Join / Add folder, then I joined — Continue.",
            reply_markup=join_gate_keyboard(key),
        )
        return

    if data.startswith("joined:"):
        key = data.split(":", 1)[1]
        dept = KEY_TO_DEPT.get(key) or KEY_TO_DEPT.get(context.user_data.get("pending_dept", ""))
        if not dept:
            await query.edit_message_text("Session expired. Send /start and choose a field again.")
            return
        status = await user_in_channel(context, user.id)
        if status is False:
            await query.answer(
                "Still not seeing you in the channel. Join first, then tap Continue.",
                show_alert=True,
            )
            return
        if status is None:
            # Soft gate (private invite; chat id not known yet, or bot not admin)
            context.user_data["channel_soft_ok"] = True
        await open_dept(dept, thanks=True)
        return


async def on_my_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """When hub bot is added to the channel, remember chat id for hard membership checks."""
    mcm = update.my_chat_member
    if not mcm:
        return
    chat = mcm.chat
    if chat.type != "channel":
        return
    new_status = mcm.new_chat_member.status
    if new_status in {"administrator", "member"}:
        persist_channel_chat_id(chat.id)
        log.info(
            "Hub bot is now %s in channel %r (id=%s) — hard membership checks enabled",
            new_status,
            chat.title,
            chat.id,
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

    if REQUIRE_CHANNEL:
        log.info(
            "Channel gate ON (verify=%s invite=%s ref=%s)",
            "hard" if can_verify_membership() else "soft",
            "yes" if channel_url() else "no",
            channel_ref(),
        )
    else:
        log.info("Channel gate OFF")

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
    app.add_handler(CommandHandler("folder", folder_cmd))
    app.add_handler(CommandHandler("post_campus_menu", post_campus_menu))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(ChatMemberHandler(on_my_chat_member, ChatMemberHandler.MY_CHAT_MEMBER))
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
