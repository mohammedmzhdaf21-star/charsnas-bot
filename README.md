# CharaNas Bots

Telegram study bots for CharaNas undergraduate departments.

| Bot | Folder | Run |
|---|---|---|
| **Medicine** | repo root (`main.py`) | `python3 main.py` |
| **Dentistry** | `dentistry/` | `cd dentistry && python3 main.py` |

Each bot needs its **own** BotFather token (do not run two bots with the same token).

## Medicine bot

See root files: specialties → Short MCQ / Case / PDF / Books → Easy–Extreme.

```bash
cp .env.example .env   # BOT_TOKEN=...
pip install -r requirements.txt
python3 main.py
```

## Dentistry bot

```bash
cd dentistry
cp .env.example .env   # DENTISTRY_BOT_TOKEN=...
pip install -r ../requirements.txt
python3 main.py
```

Details: [dentistry/README.md](dentistry/README.md)
