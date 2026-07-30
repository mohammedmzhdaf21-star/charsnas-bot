# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is
Six independent Telegram study bots (python-telegram-bot, long polling). Each bot is a
self-contained Python program with its own `main.py`, `content.py`/`quiz_bank.py` (question
bank), `generate_pdfs.py` + `pdf_content.py` (PDF notes), and its own BotFather token env var:

- Medicine — repo root `main.py`, env `BOT_TOKEN`
- Hub (entry/router) — `hub/main.py`, env `HUB_BOT_TOKEN`
- Dentistry — `dentistry/main.py`, env `DENTISTRY_BOT_TOKEN`
- Pharmacy — `pharmacy/main.py`, env `PHARMACY_BOT_TOKEN`
- MLS — `mls/main.py`, env `MLS_BOT_TOKEN`
- Nursing — `nursing/main.py`, env `NURSING_BOT_TOKEN`

Shared dependencies for all bots come from the single top-level `requirements.txt`.

### Environment
- Python 3.12. Dependencies are installed into a virtualenv at `.venv` by the startup update
  script. Activate it with `. .venv/bin/activate` (or call `.venv/bin/python`).
- `python3.12-venv` (system package) is required to create the venv; it is already present in
  the VM snapshot, so the update script does not reinstall it.

### Running a bot (needs a real token)
- Each bot reads its token from a local `.env` file in that bot's own directory (loaded via
  `python-dotenv`). Copy `.env.example` to `.env` in the relevant folder and fill in a real
  BotFather token, e.g. root `BOT_TOKEN=...`. `main.py` exits immediately if the token is unset.
- Run with `.venv/bin/python main.py` (from the bot's folder) or the wrapper `./run_bot.sh`
  (auto-restarts on crash). There is NO local web UI — the only way to interact live is through
  the actual Telegram app against a bot whose token you control.
- Startup order in `main.py`: generate/refresh PDFs (`ensure_pdfs`), then `app.run_polling()`
  which calls Telegram `getMe`. A fake token boots fine but fails at `getMe` with
  `401 Unauthorized` (outbound network to `api.telegram.org` works from the VM).

### Testing / lint / build
- No test suite and no configured linter exist in this repo. Use `python -m py_compile <files>`
  as a syntax check.
- The quiz engine can be exercised without a token by importing `content` and calling
  `pick_question` / `present_question` / `format_question_prompt` / `format_question_result`
  (and the `pick_case` equivalents).
- PDF "build": `.venv/bin/python generate_pdfs.py` regenerates the `pdfs/` notes (8 pages each).
  Note the generated PDFs are committed and reportlab embeds a timestamp, so regenerating them
  produces a spurious diff — `git checkout -- pdfs/` to discard it unless you intend to update them.
