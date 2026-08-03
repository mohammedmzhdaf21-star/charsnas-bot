# CharaNas Nursing Bot

Undergraduate **Nursing** Telegram bot — same UX as Medicine, Dentistry, Pharmacy, and MLS bots.

## Flow

1. `/start` → choose a **specialty**
2. Choose a feature:
   - **Short MCQ** → Easy / Medium / Hard / Extreme
   - **Case-based Question** → Easy / Medium / Hard / Extreme
   - **PDF files** — multi-page specialty study pack
   - **Book source** — specialty textbooks
3. **Back to features** or **Change specialty** anytime

### Specialties
Fundamentals of Nursing, Medical-Surgical, Pediatrics, Maternity/OB, Psychiatric, Community/Public Health, Critical Care, Pharmacology for Nurses, Ethics & Leadership, Geriatrics

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) (**separate** token from other department bots).
2. Configure token:

```bash
cd nursing
cp .env.example .env
# set NURSING_BOT_TOKEN=...
```

3. Install deps from repo root:

```bash
cd ..
pip install -r requirements.txt
```

4. Run:

```bash
cd nursing
python3 main.py
# or: ./run_bot.sh
```

## Commands
`/start` `/help` `/ping` `/pdf` `/books`
