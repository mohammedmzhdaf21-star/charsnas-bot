"""CharaNas hub bot — Kurdish Sorani UI; routes to department bots."""

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

# All student-facing copy is Central Kurdish (Sorani). Brand name CharaNas kept.
DEPARTMENTS = [
    {
        "key": "medicine",
        "label": "پزیشکی",
        "aliases": ("medicine", "پزیشکی", "پەزیشکی"),
        "username": os.getenv("MEDICINE_BOT_USERNAME", "CharanasMedicine_bot"),
        "blurb": "تایبەتمەندییەکانی پزیشکی قۆناغی بەکالۆریۆس، پرسیاری فرەهەڵبژاردە، کەیس، پەڕگەی PDF و سەرچاوەی کتێب.",
    },
    {
        "key": "dentistry",
        "label": "پزیشکی ددان",
        "aliases": ("dentistry", "پزیشکی ددان", "ددانسازی", "ددان‌سازی", "ددان سازی"),
        "username": os.getenv("DENTISTRY_BOT_USERNAME", "Charanasdentistry_bot"),
        "blurb": "تایبەتمەندییەکانی پزیشکی ددان قۆناغی بەکالۆریۆس، پرسیاری فرەهەڵبژاردە، کەیس، پەڕگەی PDF و سەرچاوەی کتێب.",
    },
    {
        "key": "pharmacy",
        "label": "دەرمانسازی",
        "aliases": ("pharmacy", "دەرمانسازی", "دەرمان سازی", "فارماسی"),
        "username": os.getenv("PHARMACY_BOT_USERNAME", "Charanaspharmacy_bot"),
        "blurb": "تایبەتمەندییەکانی دەرمانسازی قۆناغی بەکالۆریۆس، پرسیاری فرەهەڵبژاردە، کەیس، پەڕگەی PDF و سەرچاوەی کتێب.",
    },
    {
        "key": "mls",
        "label": "تاقیگەی پزیشکی",
        "aliases": (
            "mls",
            "laboratory",
            "lab science",
            "تاقیگە",
            "تاقیگەی پزیشکی",
            "زانستی تاقیگە",
            "زانستی تاقیگەی پزیشکی",
        ),
        "username": os.getenv("MLS_BOT_USERNAME", "CharanasMLS_bot"),
        "blurb": "تایبەتمەندییەکانی زانستی تاقیگەی پزیشکی قۆناغی بەکالۆریۆس، پرسیاری فرەهەڵبژاردە، کەیس، پەڕگەی PDF و سەرچاوەی کتێب.",
    },
    {
        "key": "nursing",
        "label": "پەرستاری",
        "aliases": ("nursing", "nurse", "پەرستاری", "نەرسینگ"),
        "username": os.getenv("NURSING_BOT_USERNAME", "Charanasnursing_bot"),
        "blurb": "تایبەتمەندییەکانی پەرستاری قۆناغی بەکالۆریۆس، پرسیاری فرەهەڵبژاردە، کەیس، پەڕگەی PDF و سەرچاوەی کتێب.",
    },
]

LABEL_TO_DEPT = {d["label"]: d for d in DEPARTMENTS}
KEY_TO_DEPT = {d["key"]: d for d in DEPARTMENTS}

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


CHANNEL_CHAT_ID = _load_channel_chat_id()
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

FOLDER_INVITE_LINK = (os.getenv("FOLDER_INVITE_LINK") or "").strip()
FOLDER_NAME = (os.getenv("FOLDER_NAME") or "CharaNas").strip() or "CharaNas"
CAMPUS_GROUP_INVITE = (os.getenv("CAMPUS_GROUP_INVITE") or "").strip()
CAMPUS_GROUP_CHAT_ID = (os.getenv("CAMPUS_GROUP_CHAT_ID") or "").strip()
HUB_BOT_USERNAME = (os.getenv("HUB_BOT_USERNAME") or "Charanaseducenter_bot").strip().lstrip("@")
BTN_FOLDER = f"فۆڵدەری {FOLDER_NAME}"


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
    if CHANNEL_CHAT_ID:
        try:
            return int(CHANNEL_CHAT_ID)
        except ValueError:
            return CHANNEL_CHAT_ID
    if CHANNEL_USERNAME:
        return f"@{CHANNEL_USERNAME}"
    return None


def resolve_department(text: str) -> dict | None:
    stripped = text.strip()
    if not stripped:
        return None
    if stripped in LABEL_TO_DEPT:
        return LABEL_TO_DEPT[stripped]
    lowered = stripped.lower()

    for d in DEPARTMENTS:
        if d["key"] == lowered:
            return d
        for alias in d["aliases"]:
            if alias == stripped or alias.lower() == lowered:
                return d

    # Prefer the longest alias contained in the text (پزیشکی ددان > پزیشکی)
    best: dict | None = None
    best_len = 0
    for d in DEPARTMENTS:
        for alias in d["aliases"]:
            if len(alias) < 3:
                continue
            if alias in stripped or alias.lower() in lowered:
                if len(alias) > best_len:
                    best = d
                    best_len = len(alias)
    return best


def field_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("پزیشکی"), KeyboardButton("پزیشکی ددان")],
            [KeyboardButton("دەرمانسازی"), KeyboardButton("تاقیگەی پزیشکی")],
            [KeyboardButton("پەرستاری")],
            [KeyboardButton(BTN_FOLDER)],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def link_keyboard(dept: dict) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(
                f"کردنەوەی بۆتی {dept['label']}",
                url=bot_url(dept["username"]),
            )
        ]
    ]
    furl = folder_url()
    curl = channel_url()
    camp = campus_url()
    if furl:
        rows.append([InlineKeyboardButton(f"زیادکردنی فۆڵدەری {FOLDER_NAME}", url=furl)])
    if camp:
        rows.append(
            [InlineKeyboardButton("کردنەوەی گرووپی کەمپەس (بۆتەکان تێیدان)", url=camp)]
        )
    if curl and not furl:
        rows.append([InlineKeyboardButton("بەشداری لە کەناڵی چاراناس", url=curl)])
    return InlineKeyboardMarkup(rows)


def pick_field_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(d["label"], callback_data=f"dept:{d['key']}")] for d in DEPARTMENTS]
    )


def start_extra_keyboard() -> InlineKeyboardMarkup | None:
    rows: list[list[InlineKeyboardButton]] = []
    furl = folder_url()
    camp = campus_url()
    curl = channel_url()
    if furl:
        rows.append([InlineKeyboardButton(f"زیادکردنی فۆڵدەری {FOLDER_NAME}", url=furl)])
    if camp:
        rows.append([InlineKeyboardButton("گرووپی کەمپەس (بۆتەکان لێرەن)", url=camp)])
    if curl:
        label = "بەشداری لە کەناڵ" if furl or camp else "بەشداری لە کەناڵی چاراناس"
        rows.append([InlineKeyboardButton(label, url=curl)])
    return InlineKeyboardMarkup(rows) if rows else None


def join_gate_keyboard(dept_key: str) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    furl = folder_url()
    curl = channel_url()
    camp = campus_url()
    step = 1
    if furl:
        rows.append(
            [InlineKeyboardButton(f"{step}) زیادکردنی فۆڵدەری {FOLDER_NAME}", url=furl)]
        )
        step += 1
    elif curl:
        rows.append([InlineKeyboardButton(f"{step}) بەشداری لە کەناڵ", url=curl)])
        step += 1
    if camp:
        rows.append([InlineKeyboardButton(f"{step}) کردنەوەی گرووپی کەمپەس", url=camp)])
        step += 1
    if curl and furl:
        rows.append([InlineKeyboardButton("یان تەنها بەشداری کەناڵ بکە", url=curl)])
    rows.append(
        [
            InlineKeyboardButton(
                f"{step}) بەشداریم کرد — بەردەوامبە",
                callback_data=f"joined:{dept_key}",
            )
        ]
    )
    return InlineKeyboardMarkup(rows)


def welcome_text() -> str:
    lines = [
        f"بەخێربێیت بۆ ناوەندی پەروەردەی {FOLDER_NAME}",
        "",
        "بوارەکەت هەڵبژێرە:",
        "",
    ]
    for d in DEPARTMENTS:
        lines.append(f"- {d['label']}")
        lines.append(f"  {d['blurb']}")
        lines.append("")
    if folder_url() or campus_url():
        lines.append("ڕێکخستنی فۆڵدەر: کەناڵ + گرووپی کەمپەس (بۆتەکان ئەندامی گرووپەکەن).")
        lines.append(
            f"دوگمەی «{BTN_FOLDER}» لێدە بۆ بەستەری زیادکردن و شێوازی هێشتنی بۆتەکان لە فۆڵدەر."
        )
        lines.append("")
    elif REQUIRE_CHANNEL and channel_url():
        lines.append("سەرەتا بەشداری کەناڵەکەمان لە تێلێگرام بکە، پاشان بەردەوامبە.")
        lines.append("")
    lines.append("دوگمەی بوارێک لە خوارەوە لێدە.")
    return "\n".join(lines)


def folder_howto_text() -> str:
    lines = [
        f"فۆڵدەری {FOLDER_NAME} چۆن کاردەکات",
        "",
        "تێلێگرام ڕێگە نادات گفتوگۆی بۆت لەناو بانگەوازی فۆڵدەری هاوبەش دابنرێت.",
        "بۆیە ئەم ڕێگەکارە بەکاردەهێنین:",
        "",
        "١) فۆڵدەری هاوبەش = کەناڵ + گرووپی کەمپەس",
        "٢) هەموو بۆتەکانی خوێندن ئەندام/بەڕێوەبەری گرووپی کەمپەسن",
        "   ← کردنەوەی فۆڵدەر گرووپەکە پیشان دەدات ← بۆتەکان تێیدان",
        "٣) دوای کردنەوەی بۆتی بەشێک جارێک، ئەو بۆتە زیاد بکە بۆ",
        f"   فۆڵدەری {FOLDER_NAME} لە مۆبایلەکەت (دەستکاری فۆڵدەر ← چاتەکان)",
        "   ← ئەوکات بۆتەکە وەک گفتوگۆیەکی سەربەخۆش لە تابەکە دەردەکەوێت",
        "",
    ]
    if folder_url():
        lines.append(f"بەستەری فۆڵدەر: {folder_url()}")
    else:
        lines.append("بەستەری فۆڵدەر: هێشتا دانەنراوە (بەڕێوەبەر: فۆڵدەر دروست بکە و FOLDER_INVITE_LINK دابنێ).")
    if campus_url():
        lines.append(f"گرووپی کەمپەس: {campus_url()}")
    else:
        lines.append(
            "گرووپی کەمپەس: هێشتا دانەنراوە (بەڕێوەبەر: گرووپ دروست بکە، بۆتەکان زیاد بکە، CAMPUS_GROUP_INVITE دابنێ)."
        )
    if channel_url():
        lines.append(f"کەناڵ: {channel_url()}")
    lines.extend(
        [
            "",
            "پێڕستی ڕێکخستن بۆ بەڕێوەبەر:",
            "١. گرووپ دروست بکە: کەمپەسی چاراناس",
            "٢. وەک بەڕێوەبەر زیاد بکە: بۆتی ناوەند + پزیشکی + پزیشکی ددان + دەرمانسازی + تاقیگە + پەرستاری",
            "٣. ڕێکخستنەکان ← فۆڵدەری چات ← فۆڵدەری نوێ ← کەناڵ + گرووپی کەمپەس زیاد بکە",
            "٤. فۆڵدەر هاوبەش بکە ← بەستەری https://t.me/addlist/... کۆپی بکە",
            "٥. FOLDER_INVITE_LINK و CAMPUS_GROUP_INVITE لە hub/.env دابنێ و بۆتەکە دەستپێبکەرەوە",
        ]
    )
    return "\n".join(lines)


def bot_in_folder_tip(dept: dict) -> str:
    return (
        f"بۆتی @{dept['username']} لە فۆڵدەری {FOLDER_NAME} بهێڵەرەوە:\n"
        f"١) بۆتەکە بکەرەوە (دوگمەی سەرەوە)\n"
        f"٢) تێلێگرام ← ڕێکخستنەکان ← فۆڵدەری چات ← {FOLDER_NAME}\n"
        f"٣) چاتەکان ← @{dept['username']} زیاد بکە\n\n"
        "ئەمە شێوازی دەرکەوتنی گفتوگۆی بۆتە لە تابەکەی فۆڵدەر "
        "(بانگەوازی فۆڵدەری هاوبەش ڕاستەوخۆ بۆت وەرناگرێت)."
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
    if not REQUIRE_CHANNEL:
        return True
    chat = channel_ref()
    if chat is None:
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
        f"بۆتی {dept['label']}\n@{dept['username']}\n\n{dept['blurb']}\n\n"
        "بۆ کردنەوەی، دوگمەی خوارەوە لێدە:",
        reply_markup=link_keyboard(dept),
    )
    await safe_reply(update, bot_in_folder_tip(dept), reply_markup=start_extra_keyboard())


async def send_folder_help(update: Update) -> None:
    await safe_reply(
        update,
        folder_howto_text(),
        reply_markup=start_extra_keyboard() or field_reply_keyboard(),
    )
    await safe_reply(
        update,
        "هەر کاتێک بوارێک هەڵبژێرە:",
        reply_markup=field_reply_keyboard(),
    )


async def offer_department(
    update: Update, context: ContextTypes.DEFAULT_TYPE, dept: dict
) -> None:
    user = update.effective_user
    if not user:
        return

    context.user_data["pending_dept"] = dept["key"]

    status = await user_in_channel(context, user.id)
    if status is True or (status is None and context.user_data.get("channel_soft_ok")):
        await send_department_link(update, dept)
        return

    extra = " / فۆڵدەر" if folder_url() else ""
    await safe_reply(
        update,
        f"پێش کردنەوەی {dept['label']}، بەشداری کەناڵی {FOLDER_NAME}{extra} بکە.\n\n"
        "بۆتەکان لە ڕێگەی گرووپی کەمپەس و زیادکردنی هەر بۆتێک جارێک لە فۆڵدەر دەردەکەون.\n"
        "بەشداری / زیادکردنی فۆڵدەر لێدە، پاشان «بەشداریم کرد — بەردەوامبە».",
        reply_markup=join_gate_keyboard(dept["key"]),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(update, welcome_text(), reply_markup=field_reply_keyboard())
    extra = start_extra_keyboard()
    if extra:
        await safe_reply(
            update,
            "کەناڵ / فۆڵدەر:",
            reply_markup=extra,
        )
    await safe_reply(
        update,
        "یان لێرە بوارێک هەڵبژێرە:",
        reply_markup=pick_field_keyboard(),
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def folder_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_folder_help(update)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_reply(
        update,
        "بۆتی ناوەندی پەروەردەی چاراناس کاراە. /start بنێرە بۆ هەڵبژاردنی بوار.",
    )


async def post_campus_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not CAMPUS_GROUP_CHAT_ID:
        await safe_reply(
            update,
            "سەرەتا CAMPUS_GROUP_CHAT_ID لە hub/.env دابنێ (ژمارەی وەک -100...).",
        )
        return
    try:
        chat_id = int(CAMPUS_GROUP_CHAT_ID)
    except ValueError:
        chat_id = CAMPUS_GROUP_CHAT_ID

    rows = [[InlineKeyboardButton(d["label"], url=bot_url(d["username"]))] for d in DEPARTMENTS]
    if channel_url():
        rows.append([InlineKeyboardButton("کەناڵ", url=channel_url())])
    if folder_url():
        rows.append([InlineKeyboardButton(f"زیادکردنی فۆڵدەری {FOLDER_NAME}", url=folder_url())])
    text = (
        f"مێنیوی کەمپەسی {FOLDER_NAME}\n\n"
        "بۆتەکانی ئەم گرووپە بەشی فۆڵدەری هاوبەشن.\n"
        "بوارێک لێدە بۆ کردنەوەی بۆتی خوێندن لە چاتی تایبەت:"
    )
    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=InlineKeyboardMarkup(rows),
            disable_web_page_preview=True,
        )
        await safe_reply(update, "مێنیوی کەمپەس بۆ گرووپەکە نێردرا.")
    except TelegramError as exc:
        log.error("post_campus_menu failed: %s", exc)
        await safe_reply(
            update,
            f"نەتوانرا بۆ گرووپی کەمپەس بنێردرێت: {exc}\n"
            "دڵنیابە بۆتی ناوەند بەڕێوەبەری گرووپەکەیە.",
        )


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    if (
        text == BTN_FOLDER
        or text in {"فۆڵدەر", "فۆڵدەرەکان", f"فۆڵدەری {FOLDER_NAME}"}
        or text.lower() in {"folder", "folders", f"{FOLDER_NAME.lower()} folder"}
    ):
        await send_folder_help(update)
        return

    dept = resolve_department(text)
    if dept:
        await offer_department(update, context, dept)
        return

    await safe_reply(
        update,
        "تکایە پزیشکی، پزیشکی ددان، دەرمانسازی، تاقیگەی پزیشکی یان پەرستاری هەڵبژێرە.",
        reply_markup=field_reply_keyboard(),
    )
    await safe_reply(
        update,
        "یان لێرە بوارێک هەڵبژێرە:",
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
        prefix = "سوپاس بۆ بەشداریکردن!\n\n" if thanks else ""
        await query.edit_message_text(
            f"{prefix}بۆتی {dept['label']}\n@{dept['username']}\n\n{dept['blurb']}\n\n"
            "بۆ کردنەوەی، دوگمەی خوارەوە لێدە:"
        )
        await query.message.reply_text(
            f"کردنەوەی {dept['label']}:",
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
            await query.edit_message_text("بوار نەناسراو. /start بنێرە و دووبارە هەوڵ بدە.")
            return
        context.user_data["pending_dept"] = key
        status = await user_in_channel(context, user.id)
        if status is True or (status is None and context.user_data.get("channel_soft_ok")):
            await open_dept(dept)
            return
        extra = " / فۆڵدەر" if folder_url() else ""
        await query.edit_message_text(
            f"پێش کردنەوەی {dept['label']}، بەشداری کەناڵی {FOLDER_NAME}{extra} بکە.\n\n"
            "بۆتەکان لە ڕێگەی گرووپی کەمپەس و زیادکردنی هەر بۆتێک جارێک لە فۆڵدەر دەردەکەون.\n"
            "بەشداری / زیادکردنی فۆڵدەر لێدە، پاشان «بەشداریم کرد — بەردەوامبە».",
            reply_markup=join_gate_keyboard(key),
        )
        return

    if data.startswith("joined:"):
        key = data.split(":", 1)[1]
        dept = KEY_TO_DEPT.get(key) or KEY_TO_DEPT.get(context.user_data.get("pending_dept", ""))
        if not dept:
            await query.edit_message_text(
                "دانیشتنەکە بەسەرچوو. /start بنێرە و دووبارە بوار هەڵبژێرە."
            )
            return
        status = await user_in_channel(context, user.id)
        if status is False:
            await query.answer(
                "هێشتا لە کەناڵدا نادۆزرێیتەوە. سەرەتا بەشداری بکە، پاشان بەردەوامبە.",
                show_alert=True,
            )
            return
        if status is None:
            context.user_data["channel_soft_ok"] = True
        await open_dept(dept, thanks=True)
        return


async def on_my_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
                "هەڵەیەک ڕوویدا. تکایە دووبارە /start بنێرە."
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

    log.info("CharaNas hub bot starting (Sorani UI)…")
    print("CharaNas hub bot running (Kurdish Sorani)…")
    app.run_polling(
        drop_pending_updates=False,
        allowed_updates=Update.ALL_TYPES,
        bootstrap_retries=5,
    )


if __name__ == "__main__":
    main()
