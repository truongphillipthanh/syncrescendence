#!/usr/bin/env bash
# cockpit.sh — Syncrescendence Constellation Cockpit
# Creates a tmux session with a 4x2 grid layout:
#   Top row (75%):  4 agent CLI panes (always-on watchers)
#   Bottom row (25%): 4 Neovim editor panes (piped to agents above)
#
# Physical pane indices (tmux column-major: x first, then y):
#   ┌──────────┬──────────┬──────────┬──────────┐
#   │ PSYCHE   │ COMMANDER│ADJUDICATOR│CARTOGR. │  75% height
#   │ OpenClaw │Claude Code│ Codex CLI│Gemini CLI│  (agent CLIs)
#   │ pane 1   │ pane 3   │ pane 5   │ pane 7   │  (odd = agents)
#   ├──────────┼──────────┼──────────┼──────────┤
#   │  nvim    │  nvim    │  nvim    │  nvim    │  25% height
#   │ pane 2   │ pane 4   │ pane 6   │ pane 8   │  (even = editors)
#   └──────────┴──────────┴──────────┴──────────┘
#
# Logical keybindings (tmux.conf remaps for user ergonomics):
#   prefix+1=Psyche  prefix+2=Commander  prefix+3=Adjudicator  prefix+4=Cartographer
#   prefix+5=nvim    prefix+6=nvim       prefix+7=nvim          prefix+8=nvim
#
# Display: 5120x1440 ultrawide — center 4/6 lanes via osascript
# Flanking 1/6 on each side (~853px) left open for other apps
# NO AeroSpace — pure tmux + osascript positioning (AeroSpace conflicts with bounds)
#
# Usage:
#   cockpit              # Create/attach via alias
#   cockpit --launch     # Create cockpit AND launch agent CLIs
#   cockpit --launch-detached  # Create cockpit + launch agents, no attach
#   cockpit --resize     # Reposition window to center 4/6 (no session change)
#   cockpit --kill       # Kill the constellation session

set -euo pipefail

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
SESSION="constellation"
NVIM_BIN="/opt/homebrew/bin/nvim"  # Explicit path — never resolve to emacs
ATTACH_ON_READY=true
CODEX_MODEL="${SYNCRESCENDENCE_CODEX_MODEL:-gpt-5.2-codex}"
CODEX_REASONING_EFFORT="${SYNCRESCENDENCE_CODEX_REASONING_EFFORT:-high}"

# ── Display geometry (5120x1440, 6-lane grid, center 4) ─────────────────────
DISPLAY_W=5120
DISPLAY_H=1440
LANES=6
CENTER_LANES=4
LANE_W=$((DISPLAY_W / LANES))            # 853
WIN_LEFT=$((LANE_W))                      # 853  (skip 1 lane)
WIN_RIGHT=$((LANE_W + CENTER_LANES * LANE_W))  # 4267
WIN_TOP=0
WIN_BOTTOM=$DISPLAY_H                    # 1440

# ── Target pane dimensions (SEARED — do not change) ──────────────────────────
# 5120px ÷ 6 lanes = ~853px/lane → 93 chars/lane at font size 13
# tmux occupies center 4/6 (2/3) = 4 lanes = 4 × 93 = 372 chars + 3 borders = 375
# Each agent column = 1 lane = 93 chars wide
# Height: 1440px → 65 rows total window (includes status bar)
#   Status bar:           1 row
#   Top pane (agent CLI): 93×48  (FORCED by resize-pane -y 48)
#   Border between panes: 1 row
#   Bottom pane (nvim):   93×15  (auto: 65-1-48-1=15)
#   TOTAL CONTENT:        48+15 = 63 rows
# VERIFIED by Sovereign on 2026-02-08 via visual confirmation.
TARGET_COL_W=93
TARGET_TOP_H=48
TARGET_BOT_H=15

# ── Colors (Catppuccin Mocha) ───────────────────────────────────────────────
BLUE="#89b4fa"
GREEN="#a6e3a1"
YELLOW="#f9e2af"
MAUVE="#cba6f7"
RED="#f38ba8"
BASE="#1e1e2e"
SURFACE1="#45475a"

# ── Agent launch commands (default: shell with banner) ────────────────────────
CMD_PSYCHE="cd '$REPO' && echo '── PSYCHE (OpenClaw TUI / GPT-5.3-codex) ──' && exec zsh"
CMD_COMMANDER="cd '$REPO' && echo '── COMMANDER (Claude Code / Opus 4.6) ──' && exec zsh"
CMD_ADJUDICATOR="cd '$REPO' && echo '── ADJUDICATOR (Codex CLI) ──' && exec zsh"
CMD_CARTOGRAPHER="cd '$REPO' && echo '── CARTOGRAPHER (Gemini CLI) ──' && exec zsh"

# (nvim panes launch via split-window command — no send-keys race condition)

# ── Position Ghostty window to center 4/6 of ultrawide ──────────────────────
position_window() {
    osascript -e "
        tell application \"Ghostty\"
            set bounds of front window to {${WIN_LEFT}, ${WIN_TOP}, ${WIN_RIGHT}, ${WIN_BOTTOM}}
        end tell
    " 2>/dev/null || {
        echo "Warning: Could not position Ghostty window via osascript."
        echo "  Ensure Ghostty is frontmost and System Events access is granted."
    }
    sleep 0.5  # Let Ghostty redraw at new size before tmux queries dimensions
}

# ── Handle flags ──────────────────────────────────────────────────────────────
case "${1:-}" in
    --launch)
        CMD_PSYCHE="cd '$REPO' && openclaw tui --session main --thinking high"
        CMD_COMMANDER="cd '$REPO' && claude --dangerously-skip-permissions"
        CMD_ADJUDICATOR="cd '$REPO' && codex --full-auto -m '$CODEX_MODEL' -c 'model_reasoning_effort=\"$CODEX_REASONING_EFFORT\"'"
        CMD_CARTOGRAPHER="cd '$REPO' && gemini --yolo"
        ;;
    --launch-detached)
        CMD_PSYCHE="cd '$REPO' && openclaw tui --session main --thinking high"
        CMD_COMMANDER="cd '$REPO' && claude --dangerously-skip-permissions"
        CMD_ADJUDICATOR="cd '$REPO' && codex --full-auto -m '$CODEX_MODEL' -c 'model_reasoning_effort=\"$CODEX_REASONING_EFFORT\"'"
        CMD_CARTOGRAPHER="cd '$REPO' && gemini --yolo"
        ATTACH_ON_READY=false
        ;;
    --resize|--fix)
        echo "Repositioning Ghostty to center 4/6 (${WIN_LEFT},${WIN_TOP} → ${WIN_RIGHT},${WIN_BOTTOM})..."
        position_window
        if tmux has-session -t "$SESSION" 2>/dev/null; then
            sleep 1  # Let Ghostty settle
            # Force SEARED pane heights: top=49, bottom=14
            echo "Forcing pane heights: top=${TARGET_TOP_H}, bottom=${TARGET_BOT_H}..."
            for pane_info in $(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}:#{pane_top}' 2>/dev/null); do
                pid="${pane_info%%:*}"
                ptop="${pane_info##*:}"
                # Top panes have pane_top near 0 (0 or 1 for border); bottom panes have higher values
                if [[ "$ptop" -le 2 ]]; then
                    tmux resize-pane -t "$pid" -y "$TARGET_TOP_H"
                fi
            done
            W=$(tmux display -t "$SESSION" -p '#{window_width}' 2>/dev/null || echo "?")
            H=$(tmux display -t "$SESSION" -p '#{window_height}' 2>/dev/null || echo "?")
            echo "Cockpit now: ${W}x${H}"
            tmux list-panes -t "$SESSION":cockpit -F '  #{pane_title}: #{pane_width}x#{pane_height}'
        fi
        exit 0
        ;;
    --kill)
        tmux kill-session -t "$SESSION" 2>/dev/null \
            && echo "Session '$SESSION' killed." \
            || echo "No session '$SESSION' found."
        exit 0
        ;;
    --help|-h)
        echo "cockpit.sh — Syncrescendence Constellation Cockpit"
        echo ""
        echo "Usage:"
        echo "  cockpit              Create/attach (default: shell banners)"
        echo "  cockpit --launch     Create AND launch agent CLIs"
        echo "  cockpit --launch-detached  Create AND launch agent CLIs (no attach)"
        echo "  cockpit --resize     Reposition window to center 4/6"
        echo "  cockpit --kill       Kill constellation session"
        echo ""
        echo "Layout: 4x2 grid on 5120x1440 center 4/6 lanes"
        echo "  Top 75%:  Psyche | Commander | Adjudicator | Cartographer"
        echo "  Bot 25%:  nvim | nvim      | nvim        | nvim"
        exit 0
        ;;
esac

# ── Preflight ───────────────────────────────────────────────────────────────
if ! command -v tmux >/dev/null 2>&1; then
    echo "Error: tmux not found. Install: brew install tmux"
    exit 1
fi

if [[ ! -x "$NVIM_BIN" ]]; then
    echo "Error: nvim not found at $NVIM_BIN"
    exit 1
fi

# ── Create or attach ────────────────────────────────────────────────────────
if tmux has-session -t "$SESSION" 2>/dev/null; then
    # Verify pane count — if wrong, kill and recreate (stale resurrect sessions break layout)
    PANE_COUNT=$(tmux list-panes -t "$SESSION":cockpit 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$PANE_COUNT" -ne 8 ]]; then
        echo "Stale session detected ($PANE_COUNT panes, expected 8). Killing and recreating..."
        tmux kill-session -t "$SESSION"
    else
        if [[ "$ATTACH_ON_READY" == "true" ]]; then
            echo "Session '$SESSION' exists. Repositioning and attaching..."
        else
            echo "Session '$SESSION' exists. Repositioning (detached mode)..."
        fi
        position_window
        if [[ "$ATTACH_ON_READY" == "true" ]]; then
            exec tmux attach -t "$SESSION"
        fi
        exit 0
    fi
fi

echo "Creating constellation cockpit (4x2 grid)..."

# ── Step 0: Position Ghostty BEFORE creating tmux session ────────────────────
# tmux inherits the terminal dimensions at session creation time.
# We must resize Ghostty first so tmux gets the full 4/6-lane cell grid.
position_window

# ── Window 1: cockpit (4x2 grid) ──────────────────────────────────────────
#
# Split strategy — column-major pane ordering:
#
#   tmux indices are assigned by position (x first, then y within column).
#   After all 8 panes exist, indices stabilize as:
#     Col 1: pane 1(Psyche-top), pane 2(nvim-bottom)
#     Col 2: pane 3(Commander-top), pane 4(nvim-bottom)
#     Col 3: pane 5(Adjudicator-top), pane 6(nvim-bottom)
#     Col 4: pane 7(Cartographer-top), pane 8(nvim-bottom)
#
#   Horizontal splits: 25%|25%|25%|25% (4 equal columns)
#   Vertical splits: 75% top (agent) | 25% bottom (nvim)

tmux new-session -d -s "$SESSION" -c "$REPO" -n cockpit

# ── Top row: 4 agent CLI columns (equal width) ──────────────────────────────
PSYCHE_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}')

tmux split-window -h -t "$PSYCHE_ID" -c "$REPO" -l 75%
COMMANDER_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

tmux split-window -h -t "$COMMANDER_ID" -c "$REPO" -l 67%
ADJUDICATOR_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

tmux split-window -h -t "$ADJUDICATOR_ID" -c "$REPO" -l 50%
CARTOGRAPHER_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

# ── Bottom row: 4 Neovim editor panes ──────────────────────────────────────
# nvim is passed DIRECTLY to split-window as the pane command.
# This eliminates the send-keys race condition that killed nvim in 3/4 panes.
# When nvim exits (:q), the pane closes — that's intentional and correct.

tmux split-window -v -t "$CARTOGRAPHER_ID" -c "$REPO/-INBOX/cartographer" -l 25% "$NVIM_BIN"
NVIM_CART_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

tmux split-window -v -t "$ADJUDICATOR_ID" -c "$REPO/-INBOX/adjudicator" -l 25% "$NVIM_BIN"
NVIM_ADJ_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

tmux split-window -v -t "$COMMANDER_ID" -c "$REPO/-INBOX/commander" -l 25% "$NVIM_BIN"
NVIM_CMD_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

tmux split-window -v -t "$PSYCHE_ID" -c "$REPO/-INBOX/psyche" -l 25% "$NVIM_BIN"
NVIM_PSYCHE_ID=$(tmux list-panes -t "$SESSION":cockpit -F '#{pane_id}' | tail -1)

# ── Send commands to agent panes (top row) ─────────────────────────────────
tmux send-keys -t "$PSYCHE_ID" "$CMD_PSYCHE" C-m
tmux send-keys -t "$COMMANDER_ID" "$CMD_COMMANDER" C-m
tmux send-keys -t "$ADJUDICATOR_ID" "$CMD_ADJUDICATOR" C-m
tmux send-keys -t "$CARTOGRAPHER_ID" "$CMD_CARTOGRAPHER" C-m

# nvim panes already running — launched directly by split-window above
# No send-keys needed. No race condition. No timing hacks.

# Psyche and Adjudicator model selection/reasoning are explicit in launch commands.

# ── Apply pane titles ────────────────────────────────────────────────────────
tmux select-pane -t "$PSYCHE_ID" -T "Psyche"
tmux select-pane -t "$COMMANDER_ID" -T "Commander"
tmux select-pane -t "$ADJUDICATOR_ID" -T "Adjudicator"
tmux select-pane -t "$CARTOGRAPHER_ID" -T "Cartographer"
tmux select-pane -t "$NVIM_PSYCHE_ID" -T "nvim-Psyche"
tmux select-pane -t "$NVIM_CMD_ID" -T "nvim-Commander"
tmux select-pane -t "$NVIM_ADJ_ID" -T "nvim-Adjudicator"
tmux select-pane -t "$NVIM_CART_ID" -T "nvim-Cartographer"

# ── Pane border styling ─────────────────────────────────────────────────────
tmux set-option -t "$SESSION" pane-border-status top
tmux set-option -t "$SESSION" pane-border-format " #{pane_title} "
tmux set-option -t "$SESSION" pane-border-style "fg=$SURFACE1"
tmux set-option -t "$SESSION" pane-active-border-style "fg=$BLUE"
tmux set-option -t "$SESSION":cockpit allow-rename off

# ── Window 2: watchers (monitoring grid) ────────────────────────────────────
tmux new-window -t "$SESSION" -n watchers -c "$REPO"

# Pane 1: INBOX watcher / triage
tmux send-keys -t "$SESSION":watchers.1 \
  "cd '$REPO' && while true; do clear; echo '[INBOX triage]'; ls -la -- -INBOX/commander/00-INBOX0/ 2>/dev/null; echo; bash 00-ORCHESTRATION/scripts/triage_outgoing.sh 2>/dev/null || true; sleep 10; done" C-m

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

# ── SEARED DIMENSIONS — Force exact pane heights (49 agent / 14 nvim) ────────
# WHY: Percentage-based splits (-l 25%) are unreliable because:
#   1. Ghostty may still be resizing when tmux calculates percentages
#   2. tmux-continuum can restore stale layouts with wrong proportions
#   3. `exec tmux attach` triggers a terminal resize → tmux redistributes proportionally
#      This UNDOES any resize-pane that ran before the attach.
#
# FIX: A tmux hook that fires AFTER client attachment, enforcing absolute heights.
# This background process that runs resize-pane AFTER the attach completes.
# Together they guarantee heights survive attach, reattach, and terminal resize.
#
# MATH: Window height 65 = status(1) + top(48) + border(1) + bottom(15)
#        48 + 15 = 63 content rows. Sovereign-verified 2026-02-08.
#
# DO NOT CHANGE THESE NUMBERS. They are verified against 5120x1440 @ font 13.
# If you think they're wrong, you're looking at a stale tmux session.
# Run: cockpit --kill && cockpit

# Resize command that enforces SEARED heights on all top panes
RESIZE_CMD="tmux resize-pane -t $PSYCHE_ID -y $TARGET_TOP_H 2>/dev/null; \
tmux resize-pane -t $COMMANDER_ID -y $TARGET_TOP_H 2>/dev/null; \
tmux resize-pane -t $ADJUDICATOR_ID -y $TARGET_TOP_H 2>/dev/null; \
tmux resize-pane -t $CARTOGRAPHER_ID -y $TARGET_TOP_H 2>/dev/null"

# Hook: enforce heights after EVERY client attach (survives detach/reattach)
tmux set-hook -t "$SESSION" client-attached "run-shell 'sleep 0.3 && $RESIZE_CMD'"

# Hook: enforce heights after EVERY window resize (terminal size changes)
tmux set-hook -t "$SESSION" window-resized "run-shell '$RESIZE_CMD'"

# Pre-attach resize (for the dimension report below)
sleep 1
eval "$RESIZE_CMD"

# ── Re-set pane titles (nvim panes may have been overwritten by zsh) ────────
tmux select-pane -t "$NVIM_PSYCHE_ID" -T "nvim-Psyche"
tmux select-pane -t "$NVIM_CMD_ID" -T "nvim-Commander"
tmux select-pane -t "$NVIM_ADJ_ID" -T "nvim-Adjudicator"
tmux select-pane -t "$NVIM_CART_ID" -T "nvim-Cartographer"

# ── Focus on cockpit window, Commander pane ─────────────────────────────────
tmux select-window -t "$SESSION":cockpit
tmux select-pane -t "$COMMANDER_ID"

# ── Report + verify dimensions ────────────────────────────────────────────────
ACTUAL_W=$(tmux display -t "$SESSION" -p '#{window_width}' 2>/dev/null || echo "?")
ACTUAL_H=$(tmux display -t "$SESSION" -p '#{window_height}' 2>/dev/null || echo "?")
PANE_W=$(tmux display -t "$PSYCHE_ID" -p '#{pane_width}' 2>/dev/null || echo "?")
PANE_H_TOP=$(tmux display -t "$PSYCHE_ID" -p '#{pane_height}' 2>/dev/null || echo "?")
PANE_H_BOT=$(tmux display -t "$NVIM_PSYCHE_ID" -p '#{pane_height}' 2>/dev/null || echo "?")
echo "Cockpit: ${ACTUAL_W}x${ACTUAL_H} total | pane: ${PANE_W}x${PANE_H_TOP} agent + ${PANE_H_BOT} nvim"
echo "Target:  ${TARGET_COL_W}x${TARGET_TOP_H} agent + ${TARGET_BOT_H} nvim"
echo "Window:  ${WIN_LEFT},${WIN_TOP} → ${WIN_RIGHT},${WIN_BOTTOM} (${CENTER_LANES}/${LANES} of ${DISPLAY_W}x${DISPLAY_H})"

# Warn if dimensions are wrong
if [[ "$PANE_H_TOP" != "?" ]] && [[ "$PANE_H_TOP" -ne "$TARGET_TOP_H" ]]; then
    echo ""
    echo "WARNING: Top pane height is ${PANE_H_TOP} (expected ${TARGET_TOP_H})."
    echo "  Attempting emergency resize..."
    tmux resize-pane -t "$PSYCHE_ID" -y "$TARGET_TOP_H" 2>/dev/null
    tmux resize-pane -t "$COMMANDER_ID" -y "$TARGET_TOP_H" 2>/dev/null
    tmux resize-pane -t "$ADJUDICATOR_ID" -y "$TARGET_TOP_H" 2>/dev/null
    tmux resize-pane -t "$CARTOGRAPHER_ID" -y "$TARGET_TOP_H" 2>/dev/null
    echo "  Re-verified. If still wrong: cockpit --kill && cockpit"
fi
if [[ "$PANE_W" != "?" ]] && (( PANE_W < 50 )); then
    echo ""
    echo "WARNING: Pane width is ${PANE_W} (expected ~${TARGET_COL_W})."
    echo "  Ghostty may be constrained by a tiling WM or fullscreen mode."
    echo "  Run: cockpit --resize"
fi

# ── Attach ──────────────────────────────────────────────────────────────────
if [[ "$ATTACH_ON_READY" == "true" ]]; then
    echo "Constellation cockpit ready. Attaching..."
    exec tmux attach -t "$SESSION"
fi
echo "Constellation cockpit ready (detached mode)."
