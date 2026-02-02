#!/bin/bash
# watch_dispatch.sh — Watch for task files in an agent's -INBOX folder
# Usage: bash watch_dispatch.sh [AGENT_NAME]
# Requires: fswatch (brew install fswatch) or uses polling fallback
#
# This script is designed to run as a background process on the target machine:
#   - On M1 Mac mini: bash watch_dispatch.sh ajna
#   - On M4 MacBook Air: bash watch_dispatch.sh psyche
#   - On primary machine: bash watch_dispatch.sh commander
#
# Integration options:
#   1. launchd plist (recommended for always-on)
#   2. tmux/screen session
#   3. Hazel rule (GUI alternative)

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

AGENT="${1:-psyche}"
WATCH_DIR="$REPO_ROOT/-INBOX/$AGENT"
POLL_INTERVAL=30  # seconds

# Validate agent folder exists
if [ ! -d "$WATCH_DIR" ]; then
    echo "[Watch] Error: $WATCH_DIR does not exist"
    echo "[Watch] Valid agents: commander, adjudicator, cartographer, psyche, ajna"
    exit 1
fi

echo "[Watch] Watching -INBOX/$AGENT/ for task files"
echo "[Watch] Directory: $WATCH_DIR"
echo "[Watch] Poll interval: ${POLL_INTERVAL}s"
echo "[Watch] Press Ctrl+C to stop"
echo ""

process_task() {
    local file="$1"
    local basename=$(basename "$file")

    echo "[Watch] $(date '+%H:%M:%S') New task detected: $basename"

    # Mark IN_PROGRESS (Self-Discovery pattern: agent claims work)
    if command -v sed &>/dev/null; then
        sed -i '' 's/Status: PENDING/Status: IN_PROGRESS/' "$file" 2>/dev/null
    fi

    # Show task preview
    if grep -q "^## Objective" "$file" 2>/dev/null; then
        echo "[Watch] Objective:"
        sed -n '/^## Objective/,/^---/p' "$file" | head -5
    fi

    echo "[Watch] ---"

    # Route to agent-specific CLI
    local task_content
    task_content="$(cat "$file")"
    case "$AGENT" in
        commander)
            claude -p "$task_content" 2>&1
            ;;
        adjudicator)
            codex "$task_content" 2>&1
            ;;
        cartographer)
            gemini "$task_content" 2>&1
            ;;
        psyche|ajna)
            openclaw agent --local -m "$task_content" 2>&1
            ;;
        *)
            echo "[Watch] No CLI handler configured for agent: $AGENT"
            return 1
            ;;
    esac

    local exit_code=$?

    # Mark completion status based on CLI exit code
    if [ $exit_code -eq 0 ]; then
        sed -i '' 's/Status: IN_PROGRESS/Status: COMPLETE/' "$file" 2>/dev/null
        echo "[Watch] $(date '+%H:%M:%S') Task completed: $basename"
    else
        sed -i '' 's/Status: IN_PROGRESS/Status: FAILED/' "$file" 2>/dev/null
        echo "[Watch] $(date '+%H:%M:%S') Task FAILED (exit $exit_code): $basename"
    fi
}

# Check if fswatch is available
if command -v fswatch &>/dev/null; then
    echo "[Watch] Using fswatch (event-driven, low overhead)"
    echo ""
    fswatch -0 --event Created --event Updated "$WATCH_DIR" | while IFS= read -r -d '' file; do
        BASENAME=$(basename "$file")
        # Only process TASK-*.md files with PENDING status
        if [[ "$BASENAME" == TASK-* ]] && [[ "$BASENAME" == *.md ]] && grep -q "Status: PENDING" "$file" 2>/dev/null; then
            process_task "$file"
        fi
    done
else
    echo "[Watch] fswatch not found. Using polling fallback (${POLL_INTERVAL}s interval)"
    echo "[Watch] Install fswatch for event-driven watching: brew install fswatch"
    echo ""
    while true; do
        for file in "$WATCH_DIR"/TASK-*.md; do
            [ -f "$file" ] || continue
            if grep -q "Status: PENDING" "$file" 2>/dev/null; then
                process_task "$file"
            fi
        done
        sleep "$POLL_INTERVAL"
    done
fi
