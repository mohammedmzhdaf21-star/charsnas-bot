# CharaNas Pharmacy Bot

Undergraduate **Pharmacy** Telegram bot — same UX as the Medicine and Dentistry bots.

## Flow

1. `/start` → choose a **specialty**
2. Choose a feature:
   - **Short MCQ** → Easy / Medium / Hard / Extreme
   - **Case-based Question** → Easy / Medium / Hard / Extreme
   - **PDF files** — multi-page specialty study pack
   - **Book source** — specialty textbooks
3. **Back to features** or **Change specialty** anytime

### Specialties
Pharmacology, Clinical Pharmacy, Pharmaceutics, Pharmacokinetics, Medicinal Chemistry, Pharmacognosy, Pharmacy Practice, Hospital Pharmacy, Toxicology, Pharmaceutical Microbiology

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) (**separate** token from medicine/dentistry).
2. Configure token:

```bash
cd pharmacy
cp .env.example .env
# set PHARMACY_BOT_TOKEN=...
```

3. Install deps from repo root:

```bash
cd ..
pip install -r requirements.txt
```

4. Run:

```bash
cd pharmacy
python3 main.py
# or: ./run_bot.sh
```

## Commands
`/start` `/help` `/ping` `/pdf` `/books`
