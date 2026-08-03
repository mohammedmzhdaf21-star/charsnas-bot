#!/usr/bin/env bash
# Keep the Telegram bot running; restart on crash.
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1

while true; do
  echo "$(date -Is) starting bot"
  python3 main.py || true
  echo "$(date -Is) bot exited — restarting in 3s"
  sleep 3
done
