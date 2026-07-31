# CharaNas Bots

Telegram study bots for CharaNas undergraduate departments.

| Bot | Folder | Env var | Telegram |
|---|---|---|---|
| **Hub (entry)** | `hub/` | `HUB_BOT_TOKEN` | routes to the bots below |
| **Medicine** | repo root | `BOT_TOKEN` | `@CharanasMedicine_bot` |
| **Dentistry** | `dentistry/` | `DENTISTRY_BOT_TOKEN` | `@Charanasdentistry_bot` |
| **Pharmacy** | `pharmacy/` | `PHARMACY_BOT_TOKEN` | `@Charanaspharmacy_bot` |
| **MLS** | `mls/` | `MLS_BOT_TOKEN` | `@CharanasMLS_bot` |
| **Nursing** | `nursing/` | `NURSING_BOT_TOKEN` | set username after BotFather create |

Each bot needs its **own** BotFather token.

## Recommended entry point

Run the **hub** bot so students pick Medicine / Dentistry / Pharmacy / MLS / Nursing, then open that department bot:

```bash
cd hub
cp .env.example .env   # HUB_BOT_TOKEN=...
python3 main.py
```

## Department bots

```bash
# Medicine
cp .env.example .env && python3 main.py

# Dentistry
cd dentistry && cp .env.example .env && python3 main.py

# Pharmacy
cd pharmacy && cp .env.example .env && python3 main.py

# MLS (Medical Laboratory Science)
cd mls && cp .env.example .env && python3 main.py

# Nursing
cd nursing && cp .env.example .env && python3 main.py
```

Details: [hub/README.md](hub/README.md) · [dentistry/README.md](dentistry/README.md) · [pharmacy/README.md](pharmacy/README.md) · [mls/README.md](mls/README.md) · [nursing/README.md](nursing/README.md)

## Question Input bot

Admin/content bot to add Short MCQs, cases, PDFs, and book sources into a department specialty.

```bash
cd question_input
cp .env.example .env   # set QUESTION_INPUT_BOT_TOKEN from @BotFather
./run_bot.sh
```

Flow: content type → department → specialty → (difficulty) → count → enter each item with choices.
Short MCQs are written into that specialty’s `question_banks/*.json` and appear in the linked department bot.

