# CharaNas Dentistry Bot

Undergraduate **Dentistry** Telegram bot — same UX as the Medicine bot.

## Flow

1. `/start` → choose a **specialty**
2. Choose a feature:
   - **Short MCQ** → Easy / Medium / Hard / Extreme
   - **Case-based Question** → Easy / Medium / Hard / Extreme
   - **PDF files** — multi-page specialty study pack
   - **Book source** — specialty textbooks
3. **Back to features** or **Change specialty** anytime

### Specialties
Oral Surgery, Orthodontics, Periodontics, Endodontics, Prosthodontics, Pediatric Dentistry, Oral Medicine & Pathology, Restorative Dentistry, Oral Radiology, Dental Anatomy

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) (separate from the medicine bot).
2. Configure token:

```bash
cd dentistry
cp .env.example .env
# set DENTISTRY_BOT_TOKEN=...
```

3. Install deps from repo root (same requirements):

```bash
cd ..
pip install -r requirements.txt
```

4. Run:

```bash
cd dentistry
python3 main.py
# or: ./run_bot.sh
```

## Commands
`/start` `/help` `/ping` `/pdf` `/books`
