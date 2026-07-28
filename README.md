# CharaNas Medicine Bot

Telegram study bot for the **Undergraduate Medicine** department.

## Flow

1. `/start` → choose a **specialty**
2. Choose a feature:
   - **Short MCQ** → then **Easy / Medium / Hard / Extreme**
   - **Case-based Question** → then **Easy / Medium / Hard / Extreme**
   - **PDF files** — multi-page specialty study pack with schematic figures
   - **Book source** — specialty textbooks
3. **Back to features** or **Change specialty** anytime

Higher difficulties use longer, trickier stems. Questions/cases do not repeat within a specialty+difficulty pool until the set is exhausted.

## Setup

```bash
cp .env.example .env
# set BOT_TOKEN=...

pip install -r requirements.txt
python3 main.py
```
