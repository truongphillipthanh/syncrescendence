#!/usr/bin/env bash
# mba-cockpit.sh — MacBook Air Constellation Cockpit (2-pane)
# Creates a tmux session with a 2-column layout:
#   Left:  Ajna (OpenClaw / Kimi K2.5 / CSO)
#   Right: Commander (Claude Code / Opus 4.6 / COO)
#
# MBA = kinetic cockpit (INT-P015). Lightweight, no ultrawide geometry.
#
# Usage:
#   mba-cockpit              # Create/attach (shells with banners)
#   mba-cockpit --launch     # Create AND launch agent CLIs
#   mba-cockpit --kill       # Kill the session

set -euo pipefail

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
SESSION="mba-constellation"

# ── Agent launch commands (default: shell with banner) ────────────────────
CMD_AJNA="cd '$REPO' && echo '── AJNA (OpenClaw TUI / Kimi K2.5 / CSO) ──' && exec zsh"
CMD_COMMANDER="cd '$REPO' && echo '── COMMANDER (Claude Code / Opus 4.6 / COO) ──' && exec zsh"

# ── Handle flags ──────────────────────────────────────────────────────────
case "${1:-}" in
    --launch)
        CMD_AJNA="cd '$REPO' && openclaw tui --session main"
        CMD_COMMANDER="cd '$REPO' && claude --dangerously-skip-permissions"
        ;;
    --kill)
        tmux kill-session -t "$SESSION" 2>/dev/null \
            && echo "Session '$SESSION' killed." \
            || echo "No session '$SESSION' found."
        exit 0
        ;;
    --help|-h)
        echo "mba-cockpit.sh — MBA Constellation Cockpit (2-pane)"
        echo ""
        echo "Usage:"
        echo "  mba-cockpit              Create/attach (default: shell banners)"
        echo "  mba-cockpit --launch     Create AND launch agent CLIs"
        echo "  mba-cockpit --kill       Kill session"
        echo ""
        echo "Layout: 2-column (50/50)"
        echo "  Left:  Ajna (CSO / OpenClaw / Kimi K2.5)"
        echo "  Right: Commander (COO / Claude Code / Opus 4.6)"
        exit 0
        ;;
esac

# ── Preflight ─────────────────────────────────────────────────────────────
if ! command -v tmux >/dev/null 2>&1; then
    echo "Error: tmux not found. Install: brew install tmux"
    exit 1
fi

# ── Create or attach ──────────────────────────────────────────────────────
if tmux has-session -t "$SESSION" 2>/dev/null; then
    PANE_COUNT=$(tmux list-panes -t "$SESSION" 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$PANE_COUNT" -ne 2 ]]; then
        echo "Stale session detected ($PANE_COUNT panes, expected 2). Killing and recreating..."
        tmux kill-session -t "$SESSION"
    else
        echo "Session '$SESSION' exists. Attaching..."
        exec tmux attach -t "$SESSION"
    fi
fi

echo "Creating MBA cockpit (2-pane)..."

# ── Create session with Ajna pane (left) ──────────────────────────────────
tmux new-session -d -s "$SESSION" -c "$REPO" -n cockpit

AJNA_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}')

# ── Split horizontally for Commander pane (right) ─────────────────────────
tmux split-window -h -t "$AJNA_ID" -c "$REPO" -l 50%
COMMANDER_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

# ── Send commands ─────────────────────────────────────────────────────────
tmux send-keys -t "$AJNA_ID" "$CMD_AJNA" C-m
tmux send-keys -t "$COMMANDER_ID" "$CMD_COMMANDER" C-m

# ── Apply pane titles ─────────────────────────────────────────────────────
tmux select-pane -t "$AJNA_ID" -T "Ajna (CSO)"
tmux select-pane -t "$COMMANDER_ID" -T "Commander (COO)"

# ── Pane border styling ──────────────────────────────────────────────────
tmux set-option -t "$SESSION" pane-border-status top
tmux set-option -t "$SESSION" pane-border-format " #{pane_title} "
tmux set-option -t "$SESSION" pane-border-style "fg=#45475a"
tmux set-option -t "$SESSION" pane-active-border-style "fg=#89b4fa"
tmux set-option -t "$SESSION":cockpit allow-rename off

# ── Focus on Commander pane ───────────────────────────────────────────────
tmux select-pane -t "$COMMANDER_ID"

# ── Report ────────────────────────────────────────────────────────────────
W=$(tmux display -t "$SESSION" -p '#{window_width}' 2>/dev/null || echo "?")
H=$(tmux display -t "$SESSION" -p '#{window_height}' 2>/dev/null || echo "?")
echo "MBA cockpit: ${W}x${H} | Ajna (left) + Commander (right)"
echo "Attaching..."
exec tmux attach -t "$SESSION"
