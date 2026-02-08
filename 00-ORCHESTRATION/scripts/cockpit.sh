#!/usr/bin/env bash
# cockpit.sh — Syncrescendence Constellation Cockpit
# Creates a tmux session with 4 agent panes in 2x2 grid
# plus a watchers window for monitoring.
#
# NOTE: tmux.conf sets pane-base-index=1, so all panes are 1-indexed.
#
# Usage:
#   bash cockpit.sh              # Create/attach cockpit
#   bash cockpit.sh --launch     # Create cockpit AND launch agent CLIs
#   bash cockpit.sh --kill       # Kill the constellation session

set -euo pipefail

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
SESSION="constellation"

# ── Colors (Catppuccin Mocha) ───────────────────────────────────────────────
BLUE="#89b4fa"
GREEN="#a6e3a1"
YELLOW="#f9e2af"
MAUVE="#cba6f7"
BASE="#1e1e2e"
SURFACE1="#45475a"

# ── Agent launch commands ───────────────────────────────────────────────────
CMD_COMMANDER="cd '$REPO' && echo '--- COMMANDER (Claude Code / Opus) ---' && exec zsh"
CMD_ADJUDICATOR="cd '$REPO' && echo '--- ADJUDICATOR (Codex CLI) ---' && exec zsh"
CMD_CARTOGRAPHER="cd '$REPO' && echo '--- CARTOGRAPHER (Gemini CLI) ---' && exec zsh"
CMD_PSYCHE="cd '$REPO' && echo '--- PSYCHE/AJNA (OpenClaw) ---' && exec zsh"

if [[ "${1:-}" == "--launch" ]]; then
    CMD_COMMANDER="cd '$REPO' && claude --model opus"
    CMD_ADJUDICATOR="cd '$REPO' && codex --model claude-sonnet-4-5-20250929"
    CMD_CARTOGRAPHER="cd '$REPO' && gemini"
    CMD_PSYCHE="cd '$REPO' && openclaw tui --session main"
fi

if [[ "${1:-}" == "--kill" ]]; then
    tmux kill-session -t "$SESSION" 2>/dev/null && echo "Session '$SESSION' killed." || echo "No session '$SESSION' found."
    exit 0
fi

# ── Preflight ───────────────────────────────────────────────────────────────
if ! command -v tmux >/dev/null 2>&1; then
    echo "Error: tmux not found. Install: brew install tmux"
    exit 1
fi

# ── Create or attach ────────────────────────────────────────────────────────
if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "Session '$SESSION' exists. Attaching..."
    tmux attach -t "$SESSION"
    exit 0
fi

echo "Creating constellation cockpit..."

# ── Window 1: cockpit (2x2 agent grid) ─────────────────────────────────────
# Pane numbering with pane-base-index=1:
#   new-session creates pane 1 (Commander, top-left)
#   split-h from 1 creates pane 2 (Adjudicator, top-right)
#   split-v from 1 creates pane 3 (Cartographer, bottom-left)
#   split-v from 2 creates pane 4 (Psyche, bottom-right)

tmux new-session -d -s "$SESSION" -c "$REPO" -n cockpit -x 200 -y 50

# Pane 1: Commander (top-left) — created with the session
tmux send-keys -t "$SESSION":cockpit.1 "$CMD_COMMANDER" C-m

# Pane 2: Adjudicator (top-right)
tmux split-window -h -t "$SESSION":cockpit.1 -c "$REPO" -l 50%
tmux send-keys -t "$SESSION":cockpit.2 "$CMD_ADJUDICATOR" C-m

# Pane 3: Cartographer (bottom-left)
tmux select-pane -t "$SESSION":cockpit.1
tmux split-window -v -t "$SESSION":cockpit.1 -c "$REPO" -l 50%
tmux send-keys -t "$SESSION":cockpit.3 "$CMD_CARTOGRAPHER" C-m

# Pane 4: Psyche (bottom-right)
tmux select-pane -t "$SESSION":cockpit.2
tmux split-window -v -t "$SESSION":cockpit.2 -c "$REPO" -l 50%
tmux send-keys -t "$SESSION":cockpit.4 "$CMD_PSYCHE" C-m

# ── Apply pane titles and border styling ────────────────────────────────────
tmux select-pane -t "$SESSION":cockpit.1 -T "Commander"
tmux select-pane -t "$SESSION":cockpit.2 -T "Adjudicator"
tmux select-pane -t "$SESSION":cockpit.3 -T "Cartographer"
tmux select-pane -t "$SESSION":cockpit.4 -T "Psyche"

tmux set-option -t "$SESSION" pane-border-status top
tmux set-option -t "$SESSION" pane-border-format " #{pane_title} "
tmux set-option -t "$SESSION" pane-border-style "fg=$SURFACE1"
tmux set-option -t "$SESSION" pane-active-border-style "fg=$BLUE"

# ── Window 2: watchers (monitoring grid) ────────────────────────────────────
tmux new-window -t "$SESSION" -n watchers -c "$REPO"

# Pane 1: INBOX watcher / triage
tmux send-keys -t "$SESSION":watchers.1 \
  "cd '$REPO' && while true; do clear; echo '[INBOX triage]'; ls -la -INBOX/commander/00-INBOX0/ 2>/dev/null; echo; bash 00-ORCHESTRATION/scripts/triage_outgoing.sh 2>/dev/null || true; sleep 10; done" C-m

# Pane 2: git status
tmux split-window -h -t "$SESSION":watchers.1 -c "$REPO"
tmux send-keys -t "$SESSION":watchers.2 \
  "cd '$REPO' && while true; do clear; echo '[git status]'; git status --short; echo; git log --oneline -5; sleep 15; done" C-m

# Pane 3: Agent logs
tmux select-pane -t "$SESSION":watchers.1
tmux split-window -v -t "$SESSION":watchers.1 -c "$REPO"
tmux send-keys -t "$SESSION":watchers.3 \
  "tail -n 200 -F /tmp/syncrescendence-watch-*.log 2>/dev/null || echo 'No agent logs found. Waiting...'" C-m

# Pane 4: System monitor
tmux select-pane -t "$SESSION":watchers.2
tmux split-window -v -t "$SESSION":watchers.2 -c "$REPO"
tmux send-keys -t "$SESSION":watchers.4 \
  "btop 2>/dev/null || top" C-m

tmux set-option -t "$SESSION":watchers pane-border-status top
tmux set-option -t "$SESSION":watchers pane-border-format " #{pane_title} "

tmux select-pane -t "$SESSION":watchers.1 -T "INBOX Triage"
tmux select-pane -t "$SESSION":watchers.2 -T "Git Status"
tmux select-pane -t "$SESSION":watchers.3 -T "Agent Logs"
tmux select-pane -t "$SESSION":watchers.4 -T "System Monitor"

# ── Focus on cockpit window, Commander pane ─────────────────────────────────
tmux select-window -t "$SESSION":cockpit
tmux select-pane -t "$SESSION":cockpit.1

# ── Attach ──────────────────────────────────────────────────────────────────
echo "Constellation cockpit ready. Attaching..."
tmux attach -t "$SESSION"
