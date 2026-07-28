# Charsnas Telegram Bot

Simple echo bot built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) and copy the token.
2. Configure the token:

```bash
cp .env.example .env
# edit .env and set BOT_TOKEN=...
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the bot:

```bash
python3 main.py
```

## Usage

- Send `/start` — bot replies with a greeting
- Send any text — bot echoes it back
