# CharaNas Bots

Telegram study bots for CharaNas undergraduate departments.

| Bot | Folder | Env var | Run |
|---|---|---|---|
| **Medicine** | repo root (`main.py`) | `BOT_TOKEN` | `python3 main.py` |
| **Dentistry** | `dentistry/` | `DENTISTRY_BOT_TOKEN` | `cd dentistry && python3 main.py` |
| **Pharmacy** | `pharmacy/` | `PHARMACY_BOT_TOKEN` | `cd pharmacy && python3 main.py` |

Each bot needs its **own** BotFather token. Do not run two bots with the same token.

## Medicine

```bash
cp .env.example .env   # BOT_TOKEN=...
pip install -r requirements.txt
python3 main.py
```

## Dentistry

```bash
cd dentistry
cp .env.example .env   # DENTISTRY_BOT_TOKEN=...
python3 main.py
```

## Pharmacy

```bash
cd pharmacy
cp .env.example .env   # PHARMACY_BOT_TOKEN=...
python3 main.py
```

Details: [dentistry/README.md](dentistry/README.md) · [pharmacy/README.md](pharmacy/README.md)
