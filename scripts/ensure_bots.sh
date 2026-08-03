#!/usr/bin/env bash
# Ensure every CharaNas Telegram bot has a live tmux session + python process.
# Safe to run repeatedly (idempotent). Uses flock to avoid overlapping runs.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONF="${BOTS_CONF:-$ROOT/scripts/bots.conf}"
LOCK="${BOTS_LOCK:-/tmp/charanas-ensure-bots.lock}"
LOG="${BOTS_ENSURE_LOG:-$ROOT/scripts/bots_ensure.log}"
TMUX_CONF="/exec-daemon/tmux.portal.conf"

tmux_cmd() {
  if [[ -f "$TMUX_CONF" ]]; then
    tmux -f "$TMUX_CONF" "$@"
  else
    tmux "$@"
  fi
}

log() {
  local msg="[$(date -Is)] $*"
  echo "$msg" | tee -a "$LOG" >/dev/null
  echo "$msg"
}

pane_cmds() {
  local session="$1"
  local tty
  tty="$(tmux_cmd list-panes -t "$session" -F '#{pane_tty}' 2>/dev/null | head -n 1 || true)"
  [[ -n "$tty" ]] || return 0
  local pts="${tty#/dev/}"
  ps -t "$pts" -o cmd= 2>/dev/null || true
}

bot_alive() {
  local session="$1"
  local cmds
  cmds="$(pane_cmds "$session")"
  grep -Eq '(^|/)python3( |$).*main\.py|[[:space:]]python3 main\.py' <<<"$cmds"
}

run_loop_alive() {
  local session="$1"
  local cmds
  cmds="$(pane_cmds "$session")"
  grep -Eq 'run_bot\.sh' <<<"$cmds"
}

ensure_one() {
  local session="$1"
  local rel="$2"
  local start_cmd="$3"
  local dir="$ROOT/$rel"
  [[ "$rel" == "." ]] && dir="$ROOT"

  if [[ ! -d "$dir" ]]; then
    log "SKIP $session — missing dir $dir"
    return 0
  fi
  if [[ ! -f "$dir/run_bot.sh" && ! -f "$dir/main.py" ]]; then
    log "SKIP $session — no run_bot.sh/main.py in $dir"
    return 0
  fi

  if ! tmux_cmd has-session -t "=$session" 2>/dev/null; then
    log "CREATE session $session in $dir"
    tmux_cmd new-session -d -s "$session" -c "$dir" -- "${SHELL:-bash}" -l
    sleep 0.5
  fi

  if bot_alive "$session"; then
    log "OK $session — python main.py running"
    return 0
  fi

  if run_loop_alive "$session"; then
    # Loop exists but python is down — wait briefly for restart
    sleep 4
    if bot_alive "$session"; then
      log "OK $session — recovered via run_bot loop"
      return 0
    fi
  fi

  log "RESTART $session — starting: $start_cmd"
  # Interrupt any stuck foreground command, then launch the restart loop
  tmux_cmd send-keys -t "$session:0.0" C-c 2>/dev/null || true
  sleep 0.4
  tmux_cmd send-keys -t "$session:0.0" C-c 2>/dev/null || true
  sleep 0.4
  # Clear any buffered partial line
  tmux_cmd send-keys -t "$session:0.0" C-u 2>/dev/null || true
  tmux_cmd send-keys -t "$session:0.0" "cd $(printf %q "$dir") && $start_cmd" C-m
  sleep 3
  if bot_alive "$session"; then
    log "STARTED $session"
  else
    log "WARN $session — start sent but python not detected yet"
  fi
}

main() {
  exec 9>"$LOCK"
  if ! flock -n 9; then
    echo "[$(date -Is)] another ensure_bots is running — skip"
    exit 0
  fi

  if [[ ! -f "$CONF" ]]; then
    log "ERROR missing $CONF"
    exit 1
  fi

  local line session rel cmd
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" =~ ^[[:space:]]*# ]] && continue
    IFS='|' read -r session rel cmd <<<"$line"
    session="$(echo "$session" | xargs)"
    rel="$(echo "$rel" | xargs)"
    cmd="$(echo "$cmd" | xargs)"
    [[ -n "$session" && -n "$rel" && -n "$cmd" ]] || continue
    ensure_one "$session" "$rel" "$cmd"
  done <"$CONF"
}

main "$@"
