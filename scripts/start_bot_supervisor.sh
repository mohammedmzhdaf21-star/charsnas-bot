#!/usr/bin/env bash
# Start (or restart) the bot supervisor inside a dedicated tmux session.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SESSION="${BOTS_SUPERVISOR_SESSION:-bots-supervisor}"
TMUX_CONF="/exec-daemon/tmux.portal.conf"

tmux_cmd() {
  if [[ -f "$TMUX_CONF" ]]; then
    tmux -f "$TMUX_CONF" "$@"
  else
    tmux "$@"
  fi
}

chmod +x "$ROOT/scripts/ensure_bots.sh" "$ROOT/scripts/bot_supervisor.sh" "$ROOT/scripts/start_bot_supervisor.sh"

# First bring every bot up immediately
bash "$ROOT/scripts/ensure_bots.sh"

if tmux_cmd has-session -t "=$SESSION" 2>/dev/null; then
  # Restart supervisor loop cleanly
  tmux_cmd send-keys -t "$SESSION:0.0" C-c 2>/dev/null || true
  sleep 0.5
  tmux_cmd send-keys -t "$SESSION:0.0" C-c 2>/dev/null || true
  sleep 0.5
  tmux_cmd send-keys -t "$SESSION:0.0" "cd $(printf %q "$ROOT") && bash scripts/bot_supervisor.sh" C-m
else
  tmux_cmd new-session -d -s "$SESSION" -c "$ROOT" -- bash -lc 'bash scripts/bot_supervisor.sh'
fi

echo "Bot supervisor running in tmux session: $SESSION"
echo "Check: tmux attach -t $SESSION"
echo "Status: bash scripts/ensure_bots.sh"
