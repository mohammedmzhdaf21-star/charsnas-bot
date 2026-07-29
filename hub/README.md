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

## Shared folder (channel + groups)

Telegram **shareable folders** can bundle your **channel** (and groups) into one link (`https://t.me/addlist/...`).

**Limitation:** Telegram does **not** allow bots inside shareable folders. Students still open Medicine / Dentistry / … from this hub bot.

### How to create the folder link

1. On Telegram: **Settings → Chat Folders → Create folder** (name it e.g. `CharaNas`)
2. Add your **channel** (and any discussion group)
3. Open the folder → **Share** / **Create invite link** → copy `https://t.me/addlist/...`
4. Put it in `hub/.env` as `FOLDER_INVITE_LINK=...` and restart the hub

Then `/start` shows **Add CharaNas folder**.

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
