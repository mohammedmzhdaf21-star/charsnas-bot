#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1
while true; do
  echo "$(date -Is) starting hub bot"
  python3 main.py || true
  echo "$(date -Is) hub bot exited — restarting in 3s"
  sleep 3
done
