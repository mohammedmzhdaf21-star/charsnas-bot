# CharaNas Hub Bot

Entry bot that links users to the department study bots:

- Medicine → `@CharanasMedicine_bot`
- Dentistry → `@Charanasdentistry_bot`
- Pharmacy → `@Charanaspharmacy_bot`

## Flow

1. User sends `/start`
2. Hub shows **Medicine / Dentistry / Pharmacy** buttons
3. Tapping a button opens that department bot in Telegram

## Setup

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
