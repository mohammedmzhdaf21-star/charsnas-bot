#!/usr/bin/env bash
# Install CharaNas bots on a Linux VPS for true 24/7 uptime.
#
# Usage (from this repo, with SSH access to the VPS):
#   bash deploy/setup_vps.sh ubuntu@YOUR_VPS_IP
#   bash deploy/setup_vps.sh ubuntu@YOUR_VPS_IP ~/.ssh/id_ed25519
#
# Prerequisites on your laptop/agent:
#   - SSH access to the VPS
#   - Local .env files already filled (tokens)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-}"
IDENTITY="${2:-}"
REMOTE_DIR="${REMOTE_DIR:-/opt/charsnas-bot}"
REMOTE_USER_HOME=""

if [[ -z "$TARGET" ]]; then
  echo "Usage: bash deploy/setup_vps.sh user@vps-ip [ssh-private-key]"
  exit 1
fi

SSH_OPTS=(-o StrictHostKeyChecking=accept-new)
if [[ -n "$IDENTITY" ]]; then
  SSH_OPTS+=(-i "$IDENTITY")
fi

ssh_run() {
  ssh "${SSH_OPTS[@]}" "$TARGET" "$@"
}

scp_to() {
  scp "${SSH_OPTS[@]}" "$@"
}

echo "==> Checking SSH to $TARGET"
ssh_run 'uname -a && whoami'

echo "==> Installing system packages"
ssh_run 'sudo apt-get update -y && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip python3-venv tmux git'

echo "==> Syncing repo to $REMOTE_DIR"
ssh_run "sudo mkdir -p '$REMOTE_DIR' && sudo chown \"\$USER\":\"\$USER\" '$REMOTE_DIR'"
# Prefer git clone if remote is empty and origin is available
if ssh_run "test -d '$REMOTE_DIR/.git'"; then
  ssh_run "cd '$REMOTE_DIR' && git fetch --all && git checkout main || true && git pull --ff-only || true"
else
  tar -C "$ROOT" \
    --exclude='.git' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='venv' \
    --exclude='.venv' \
    --exclude='deploy/ssh' \
    -czf - . | ssh "${SSH_OPTS[@]}" "$TARGET" "tar -C '$REMOTE_DIR' -xzf -"
fi

echo "==> Copying bot .env files (tokens)"
for envf in \
  .env \
  dentistry/.env \
  pharmacy/.env \
  mls/.env \
  nursing/.env \
  hub/.env \
  question_input/.env
do
  if [[ -f "$ROOT/$envf" ]]; then
    ssh_run "mkdir -p '$REMOTE_DIR/$(dirname "$envf")'"
    scp_to "$ROOT/$envf" "$TARGET:$REMOTE_DIR/$envf"
    ssh_run "chmod 600 '$REMOTE_DIR/$envf'"
    echo "  copied $envf"
  else
    echo "  WARN missing local $envf"
  fi
done

echo "==> Installing Python deps"
ssh_run "cd '$REMOTE_DIR' && python3 -m pip install --user -r requirements.txt"

echo "==> Installing systemd service"
ssh_run "sed 's#/opt/charsnas-bot#$REMOTE_DIR#g; s#User=ubuntu#User='\"\$USER\"'#g' '$REMOTE_DIR/deploy/charanas-bots.service' | sudo tee /etc/systemd/system/charanas-bots.service >/dev/null"
ssh_run 'sudo systemctl daemon-reload && sudo systemctl enable --now charanas-bots && sudo systemctl status charanas-bots --no-pager | head -n 20'

echo "==> Done. Bots should be live 24/7 on $TARGET"
echo "    Check: ssh $TARGET 'sudo systemctl status charanas-bots'"
echo "    Logs:  ssh $TARGET 'journalctl -u charanas-bots -f'"
