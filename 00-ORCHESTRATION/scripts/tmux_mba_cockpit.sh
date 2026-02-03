#!/usr/bin/env bash
# tmux_mba_cockpit.sh — single-window cockpit for MacBook Air
#
# Layout (one tmux window):
#   [ Left column ~70% ] | [ Right column ~30% ]
#   top-left (~66%): openclaw tui (Psyche)
#   bot-left (~34%): watcher logs + quick triage
#   right: Commander (special forces mode)
#
# Note: inbox watching should be done by launchd watchers (psyche_boot.sh), not by the TUI.

set -euo pipefail

REPO="$HOME/Desktop/syncrescendence"
SESSION="sync-mba"

cd "$REPO"

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found. Install: brew install tmux"
  exit 1
fi

# Create session if absent
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -c "$REPO" -n cockpit

  # Split into left/right (right = 30%)
  tmux split-window -h -t "$SESSION":cockpit -p 30 -c "$REPO"

  # Split left pane into top/bottom (bottom = 34%)
  tmux select-pane -t "$SESSION":cockpit.0
  tmux split-window -v -t "$SESSION":cockpit -p 34 -c "$REPO"

  # Top-left: OpenClaw TUI
  tmux send-keys -t "$SESSION":cockpit.0 "cd '$REPO' && openclaw tui --session main" C-m

  # Bottom-left: logs + quick triage loop
  tmux send-keys -t "$SESSION":cockpit.2 "cd '$REPO' && while true; do clear; echo '[psyche+canon watcher logs]'; tail -n 80 /tmp/syncrescendence-watch-psyche.log /tmp/syncrescendence-watch-canon.log 2>/dev/null || true; echo; echo '[triage_outgoing]'; bash 00-ORCHESTRATION/scripts/triage_outgoing.sh 2>/dev/null || true; sleep 5; done" C-m

  # Right: Commander lane
  tmux send-keys -t "$SESSION":cockpit.1 "cd '$REPO' && bash 00-ORCHESTRATION/scripts/commander_special_forces.sh" C-m

  tmux select-pane -t "$SESSION":cockpit.0
fi

tmux attach -t "$SESSION"
