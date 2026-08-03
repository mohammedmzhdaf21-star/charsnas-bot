#!/usr/bin/env bash
# Keep all CharaNas bots alive 24/7 while this host is up.
# Runs ensure_bots.sh on a short interval forever.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INTERVAL="${BOTS_SUPERVISOR_INTERVAL:-30}"
LOG="${BOTS_SUPERVISOR_LOG:-$ROOT/scripts/bots_supervisor.log}"
ENSURE="$ROOT/scripts/ensure_bots.sh"

export PYTHONUNBUFFERED=1

log() {
  local msg="[$(date -Is)] $*"
  echo "$msg" | tee -a "$LOG"
}

cd "$ROOT"
chmod +x "$ENSURE" 2>/dev/null || true

log "bot supervisor starting (interval=${INTERVAL}s)"
while true; do
  if ! bash "$ENSURE" >>"$LOG" 2>&1; then
    log "ensure_bots exited non-zero — will retry"
  fi
  sleep "$INTERVAL"
done
