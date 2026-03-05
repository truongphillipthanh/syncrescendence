#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:$PATH"

SESSION_NAME="${SESSION_NAME:-${1:-constellation}}"
REPO_ROOT="${REPO_ROOT:-/Users/home/syncrescendence}"
TMUX_SOCKET="${TMUX_SOCKET:-/tmp/tmux-syncrescendence-mini.sock}"
FORCE_REBUILD="${FORCE_REBUILD:-0}"
LOCK_DIR="${LOCK_DIR:-/tmp/syncrescendence-constellation-stage1.lock}"

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux is not available on PATH" >&2
  exit 1
fi

if [ ! -d "$REPO_ROOT" ]; then
  echo "repo path missing: $REPO_ROOT" >&2
  exit 1
fi

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "constellation lock exists at $LOCK_DIR; another bootstrap may be running" >&2
  exit 1
fi
trap 'rmdir "$LOCK_DIR" >/dev/null 2>&1 || true' EXIT

tmx() {
  tmux -S "$TMUX_SOCKET" "$@"
}

shell_cmd() {
  local role="$1"
  printf 'cd %q && printf %q && exec zsh -l' \
    "$REPO_ROOT" \
    "$role shell ready in $REPO_ROOT\n"
}

watch_cmd() {
  local office="$1"
  printf 'cd %q && printf %q && while true; do python3 operators/runtime/office_inbox_watch.py --office %q --repo-root %q --claimed-by %q; rc=$?; printf %q "$rc"; sleep 2; done' \
    "$REPO_ROOT" \
    "$office watcher online in $REPO_ROOT\n" \
    "$office" \
    "$REPO_ROOT" \
    "$office-watcher" \
    "$office watcher exited with rc=%s; restarting in 2s\n"
}

if tmx has-session -t "$SESSION_NAME" 2>/dev/null; then
  if [ "$FORCE_REBUILD" = "1" ]; then
    tmx kill-session -t "$SESSION_NAME"
  else
    echo "constellation session already exists; leaving running session intact"
    tmx list-windows -t "$SESSION_NAME"
    exit 0
  fi
fi

tmx new-session -d -s "$SESSION_NAME" -n psyche "$(watch_cmd 'psyche')"
tmx new-window -t "$SESSION_NAME" -n adjudicator "$(watch_cmd 'adjudicator')"
tmx new-window -t "$SESSION_NAME" -n cartographer "$(watch_cmd 'cartographer')"
tmx new-window -t "$SESSION_NAME" -n ops "cd \"$REPO_ROOT\" && printf 'Ops shell ready in %s\n' \"$REPO_ROOT\" && printf 'Suggested checks: make tooling-surface-status ; openclaw channels status --probe --json ; tmux -S %s list-windows -t %s\n' \"$TMUX_SOCKET\" \"$SESSION_NAME\" && exec zsh -l"

tmx set-option -t "$SESSION_NAME" remain-on-exit on
tmx select-window -t "$SESSION_NAME:psyche"
tmx list-windows -t "$SESSION_NAME"
