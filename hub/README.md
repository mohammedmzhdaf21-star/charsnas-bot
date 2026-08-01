# CharaNas Hub Bot

Entry bot that links users to the department study bots:

- Medicine → `@CharanasMedicine_bot`
- Dentistry → `@Charanasdentistry_bot`
- Pharmacy → `@Charanaspharmacy_bot`
- MLS → `@CharanasMLS_bot` (set `MLS_BOT_USERNAME` if different)
- Nursing → `@Charanasnursing_bot` (set `NURSING_BOT_USERNAME` if different)

## Flow

1. User sends `/start`
2. Hub shows **Medicine / Dentistry / Pharmacy / MLS / Nursing** buttons
3. If a channel is configured, the user must **join the channel** first (Join → Continue)
4. Then the hub opens that department bot

Telegram does **not** allow bots to add people to a channel automatically. The hub uses the standard join gate: open channel → verify membership → continue.

## Shared folder (channel + bots)

Telegram **blocks bots** in shareable folder invites. Working pattern:

1. **Campus group** with all bots as members/admins  
2. **Shared folder** = Channel + Campus group  
3. Students optionally add each bot chat to the folder after opening it once  

Full steps: [FOLDER_SETUP.md](FOLDER_SETUP.md). Hub commands: `/folder`, `/post_campus_menu`.

## Channel setup

1. Add the **hub bot** as an **admin** of your channel (needed for membership checks).
2. In `hub/.env`:

```bash
# Public channel
CHANNEL_USERNAME=YourChannelUsername
REQUIRE_CHANNEL=1

# Or private channel
# CHANNEL_CHAT_ID=-100xxxxxxxxxx
# CHANNEL_INVITE_LINK=https://t.me/+xxxxxx
# REQUIRE_CHANNEL=1
```

## Bot setup

1. Create a new bot with [@BotFather](https://t.me/BotFather) (separate token).
2. Configure:

```bash
cd hub
cp .env.example .env
# set HUB_BOT_TOKEN=...
```

3. Run:

```bash
pip install -r ../requirements.txt
python3 main.py
# or: ./run_bot.sh
```

## Commands

`/start` `/help` `/ping`
