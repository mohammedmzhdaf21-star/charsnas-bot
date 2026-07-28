# CharaNas Medicine Bot

Telegram study bot for the **Undergraduate Medicine** department.

## Flow

1. `/start` → choose a **specialty** (Cardiology, Ophthalmology, Urology, …)
2. Then choose a feature:
   - **Short MCQ** — answer buttons; correct answer revealed after tap
   - **Case-based Question** — reveal answer button
   - **PDF files** — specialty study notes PDF
   - **Book source** — specialty textbooks
3. Tap **Change specialty** anytime to go back and pick another topic

Questions/cases do not repeat within a specialty until the full set is used.

## Setup

```bash
cp .env.example .env
# set BOT_TOKEN=...

pip install -r requirements.txt
python3 main.py
```
