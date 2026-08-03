# CharaNas MLS Bot

Undergraduate **Medical Laboratory Science (MLS)** Telegram bot — same UX as Medicine, Dentistry, and Pharmacy bots.

## Flow

1. `/start` → choose a **specialty**
2. Choose a feature:
   - **Short MCQ** → Easy / Medium / Hard / Extreme
   - **Case-based Question** → Easy / Medium / Hard / Extreme
   - **PDF files** — multi-page specialty study pack
   - **Book source** — specialty textbooks
3. **Back to features** or **Change specialty** anytime

### Specialties
Hematology, Clinical Chemistry, Medical Microbiology, Immunology & Serology, Blood Bank / Transfusion, Histopathology, Parasitology, Molecular Diagnostics, Lab QA & Safety, Urinalysis & Body Fluids

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) (**separate** token from other department bots).
2. Configure token:

```bash
cd mls
cp .env.example .env
# set MLS_BOT_TOKEN=...
```

3. Install deps from repo root:

```bash
cd ..
pip install -r requirements.txt
```

4. Run:

```bash
cd mls
python3 main.py
# or: ./run_bot.sh
```

## Commands
`/start` `/help` `/ping` `/pdf` `/books`
