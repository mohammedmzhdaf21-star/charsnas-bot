# CharaNas Bots

Telegram study bots for CharaNas undergraduate departments.

| Bot | Folder | Env var | Telegram |
|---|---|---|---|
| **Hub (entry)** | `hub/` | `HUB_BOT_TOKEN` | routes to the bots below |
| **Medicine** | repo root | `BOT_TOKEN` | `@CharanasMedicine_bot` |
| **Dentistry** | `dentistry/` | `DENTISTRY_BOT_TOKEN` | `@Charanasdentistry_bot` |
| **Pharmacy** | `pharmacy/` | `PHARMACY_BOT_TOKEN` | `@Charanaspharmacy_bot` |

Each bot needs its **own** BotFather token.

## Recommended entry point

Run the **hub** bot so students pick Medicine / Dentistry / Pharmacy, then open that department bot:

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
```

Details: [hub/README.md](hub/README.md) · [dentistry/README.md](dentistry/README.md) · [pharmacy/README.md](pharmacy/README.md)
