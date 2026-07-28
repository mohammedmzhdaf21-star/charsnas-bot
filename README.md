# CharaNas Medicine Bot

Telegram study bot for the **Undergraduate Medicine** department only.

## What it does

On `/start`, the bot shows four feature buttons:

| Button | Action |
|---|---|
| `Short MCQ` | UG medicine MCQ with A–D buttons; answer revealed after you tap |
| `Case-based Question` | Clinical case; tap **Reveal answer** |
| `PDF files` | Sends medicine study PDFs |
| `Book source` | Lists standard UG medicine textbooks |

Also supports: `/help` `/question` `/case` `/pdf` `/books`

## Setup

```bash
cp .env.example .env
# set BOT_TOKEN=...

pip install -r requirements.txt
python3 main.py
```

PDFs are generated automatically into `pdfs/` on first run.
