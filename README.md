# CharaNas Medicine Bot

Telegram study bot for the **Undergraduate Medicine** department only.

## What it does

| You say | Bot does |
|---|---|
| `create question` | Sends an UG medicine MCQ with A–D buttons; answer revealed after you tap |
| `case based question` | Sends a clinical case; tap **Reveal answer** |
| `give me pdf files` | Sends medicine study PDFs |
| `book source` | Lists standard UG medicine textbooks |

Also supports: `/start` `/help` `/question` `/case` `/pdf` `/books`

## Setup

```bash
cp .env.example .env
# set BOT_TOKEN=...

pip install -r requirements.txt
python3 main.py
```

PDFs are generated automatically into `pdfs/` on first run.
