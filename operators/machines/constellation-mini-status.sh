#!/usr/bin/env bash
set -euo pipefail

REMOTE_HOST="${REMOTE_HOST:-mini}"
REMOTE_REPO="${REMOTE_REPO:-/Users/home/syncrescendence}"
SESSION_NAME="${SESSION_NAME:-constellation}"
TMUX_SOCKET="${TMUX_SOCKET:-/tmp/tmux-syncrescendence-mini.sock}"
LAUNCH_LABEL="${LAUNCH_LABEL:-com.syncrescendence.constellation-stage1}"

ssh "$REMOTE_HOST" "PATH=/opt/homebrew/bin:\$PATH; \
  echo host=\"\$(hostname)\"; \
  echo repo=\"$REMOTE_REPO\"; \
  [ -d \"$REMOTE_REPO\" ] && echo repo_present=true || echo repo_present=false; \
  command -v tmux >/dev/null 2>&1 && echo tmux_path=\"\$(command -v tmux)\" || echo tmux_path=missing; \
  tmux -S \"$TMUX_SOCKET\" has-session -t \"$SESSION_NAME\" 2>/dev/null && echo session_present=true || echo session_present=false; \
  tmux -S \"$TMUX_SOCKET\" list-windows -t \"$SESSION_NAME\" 2>/dev/null || true; \
  launchctl print gui/\$(id -u)/$LAUNCH_LABEL >/dev/null 2>&1 && echo launchagent_present=true || echo launchagent_present=false"
