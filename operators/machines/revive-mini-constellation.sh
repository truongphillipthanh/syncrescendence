#!/usr/bin/env bash
set -euo pipefail

REMOTE_HOST="${REMOTE_HOST:-mini}"
REMOTE_REPO="${REMOTE_REPO:-/Users/home/syncrescendence}"
SESSION_NAME="${SESSION_NAME:-constellation}"
TMUX_SOCKET="${TMUX_SOCKET:-/tmp/tmux-syncrescendence-mini.sock}"
FORCE_REBUILD="${FORCE_REBUILD:-0}"

ssh "$REMOTE_HOST" \
  "FORCE_REBUILD=$FORCE_REBUILD SESSION_NAME=$SESSION_NAME TMUX_SOCKET=$TMUX_SOCKET REPO_ROOT=$REMOTE_REPO \
   bash \"$REMOTE_REPO/operators/machines/constellation-mini-stage1.sh\""
