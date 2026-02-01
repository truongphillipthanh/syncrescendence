#!/bin/bash
# watch_dispatch.sh — Watch for dispatch files and trigger processing
# Usage: bash watch_dispatch.sh [TWIN_NAME]
# Requires: fswatch (brew install fswatch) or can use polling fallback
#
# This script is designed to run as a background process on the target machine:
#   - On M1 Mac mini: watches for DISPATCH-AJNA-* files
#   - On M4 MacBook Air: watches for DISPATCH-PSYCHE-* files
#
# Integration options:
#   1. launchd plist (recommended for always-on)
#   2. tmux/screen session
#   3. Hazel rule (GUI alternative)

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

TWIN="${1:-PSYCHE}"
WATCH_DIR="$REPO_ROOT/00-ORCHESTRATION/state"
PATTERN="DISPATCH-${TWIN}-*.md"
POLL_INTERVAL=30  # seconds

echo "[Watch] Watching for $PATTERN in $WATCH_DIR"
echo "[Watch] Twin: $TWIN | Poll interval: ${POLL_INTERVAL}s"
echo "[Watch] Press Ctrl+C to stop"

# Check if fswatch is available
if command -v fswatch &>/dev/null; then
    echo "[Watch] Using fswatch (event-driven, low overhead)"
    fswatch -0 --event Created --event Updated "$WATCH_DIR" | while IFS= read -r -d '' file; do
        BASENAME=$(basename "$file")
        if [[ "$BASENAME" == DISPATCH-${TWIN}-* ]] && grep -q "Status: PENDING" "$file" 2>/dev/null; then
            echo "[Watch] $(date '+%H:%M:%S') New dispatch detected: $BASENAME"
            echo "[Watch] Content preview:"
            grep "^## Task:" "$file" 2>/dev/null
            echo "[Watch] ---"
            # Hook point: trigger OpenClaw or other processor here
            # Example: openclaw process "$file"
        fi
    done
else
    echo "[Watch] fswatch not found. Using polling fallback (${POLL_INTERVAL}s interval)"
    echo "[Watch] Install fswatch for event-driven watching: brew install fswatch"
    while true; do
        for file in "$WATCH_DIR"/DISPATCH-${TWIN}-*.md; do
            [ -f "$file" ] || continue
            if grep -q "Status: PENDING" "$file" 2>/dev/null; then
                BASENAME=$(basename "$file")
                echo "[Watch] $(date '+%H:%M:%S') Pending dispatch: $BASENAME"
                grep "^## Task:" "$file" 2>/dev/null
            fi
        done
        sleep "$POLL_INTERVAL"
    done
fi
