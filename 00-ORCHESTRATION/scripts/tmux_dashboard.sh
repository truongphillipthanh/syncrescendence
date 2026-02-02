#!/usr/bin/env bash
# tmux_dashboard.sh — attach/create a Syncrescendence dashboard tmux session
#
# Intended use: run after psyche_boot.sh or mini_boot.sh.
# Provides a single iTerm command to open a consistent "window formation".

set -euo pipefail

SESSION="sync"
REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found. Install: brew install tmux"
  exit 1
fi

if tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux attach -t "$SESSION"
  exit 0
fi

tmux new-session -d -s "$SESSION" -c "$REPO" -n "watchers"

# Pane 0: triage (refresh every 10s)
tmux send-keys -t "$SESSION":watchers.0 "cd '$REPO' && while true; do clear; echo '[triage]'; bash 00-ORCHESTRATION/scripts/triage_outgoing.sh 2>/dev/null || true; sleep 10; done" C-m

# Pane 1: watcher logs
 tmux split-window -h -t "$SESSION":watchers -c "$REPO"
 tmux send-keys -t "$SESSION":watchers.1 "tail -n 200 -F /tmp/syncrescendence-watch-psyche.log /tmp/syncrescendence-watch-canon.log 2>/dev/null" C-m

# Pane 2: gateway + memory status
 tmux split-window -v -t "$SESSION":watchers.1 -c "$REPO"
 tmux send-keys -t "$SESSION":watchers.2 "while true; do echo '--- gateway'; openclaw gateway status | head -n 18; echo '--- memory'; openclaw memory status; sleep 30; done" C-m

# Pane 3: git status
 tmux split-window -v -t "$SESSION":watchers.0 -c "$REPO"
 tmux send-keys -t "$SESSION":watchers.3 "while true; do echo '--- git status'; git status --short; sleep 15; done" C-m

 tmux select-layout -t "$SESSION":watchers tiled
 tmux attach -t "$SESSION"
