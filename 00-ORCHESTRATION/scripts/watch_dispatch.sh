#!/bin/bash
# watch_dispatch.sh — Watch for task files in an agent's -INBOX folder
# Usage: bash watch_dispatch.sh [AGENT_NAME]
# Requires: fswatch (brew install fswatch) or uses polling fallback
#
# IO Model v2: Claim-locking prevents duplicate consumers.
# Flow: detect PENDING → atomic claim (rename) → process → complete/fail → ledger append
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
HOSTNAME_SHORT=$(hostname -s 2>/dev/null || echo "local")
SCRIPTS_DIR="$REPO_ROOT/00-ORCHESTRATION/scripts"

# Validate agent folder exists
if [ ! -d "$WATCH_DIR" ]; then
    echo "[Watch] Error: $WATCH_DIR does not exist"
    echo "[Watch] Valid agents: commander, adjudicator, cartographer, psyche, ajna"
    exit 1
fi

echo "[Watch] Watching -INBOX/$AGENT/ for task files"
echo "[Watch] Directory: $WATCH_DIR"
echo "[Watch] Poll interval: ${POLL_INTERVAL}s"
echo "[Watch] Claim tag: ${AGENT}-${HOSTNAME_SHORT}"
echo "[Watch] Press Ctrl+C to stop"
echo ""

claim_task() {
    local file="$1"
    local basename
    basename=$(basename "$file")
    local claimed_name="${file}.claimed-by-${AGENT}-${HOSTNAME_SHORT}"

    # Atomic claim via rename — if this fails, another watcher claimed it first
    if ! mv "$file" "$claimed_name" 2>/dev/null; then
        echo "[Watch] $(date '+%H:%M:%S') Claim failed (already claimed): $basename" >&2
        return 1
    fi

    # Update in-body lifecycle truth (Status + Claimed-By/At)
    if [ -f "$claimed_name" ]; then
        python3 - "$claimed_name" "$AGENT" "$HOSTNAME_SHORT" << 'PY'
import sys
from datetime import datetime, timezone

path, agent, host = sys.argv[1:4]
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
claim_tag = f"{agent}-{host}"

lines = open(path, 'r', encoding='utf-8').read().splitlines(True)

def set_field(name: str, value: str):
    """Upsert a markdown header field like **Status**: VALUE."""
    key = f"**{name}**:"
    for i, line in enumerate(lines):
        if line.startswith(key):
            lines[i] = f"{key} {value}\n"
            return
    # Insert after Priority if present, else after Fingerprint, else near top
    insert_after = None
    for marker in ("**Priority**:", "**Fingerprint**:", "**Issued**:"):
        for i, line in enumerate(lines):
            if line.startswith(marker):
                insert_after = i
                break
        if insert_after is not None:
            break
    if insert_after is None:
        insert_after = 0
    lines.insert(insert_after + 1, f"{key} {value}\n")

set_field("Status", "IN_PROGRESS")
set_field("Claimed-By", claim_tag)
set_field("Claimed-At", now)

open(path, 'w', encoding='utf-8').write(''.join(lines))
PY
    else
        echo "[Watch] WARNING: claimed file missing before status update: $claimed_name" >&2
    fi

    echo "[Watch] $(date '+%H:%M:%S') Claimed: $basename" >&2

    # Append ledger: CLAIM event
    if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
        # Important: do not contaminate stdout (stdout is used to return claimed filename)
        bash "$SCRIPTS_DIR/append_ledger.sh" CLAIM "$AGENT" "$AGENT" "$basename" >/dev/null 2>&1 || true
    fi

    echo "$claimed_name"
}

process_task() {
    local claimed_file="$1"
    local original_basename="$2"

    echo "[Watch] $(date '+%H:%M:%S') Processing: $original_basename"

    # Show task preview
    if grep -q "^## Objective" "$claimed_file" 2>/dev/null; then
        echo "[Watch] Objective:"
        sed -n '/^## Objective/,/^---/p' "$claimed_file" | head -5
    fi

    echo "[Watch] ---"

    # Route to agent-specific CLI
    local task_content
    task_content="$(cat "$claimed_file")"
    case "$AGENT" in
        commander)
            claude -p "$task_content" 2>&1
            ;;
        adjudicator)
            codex exec "$task_content" 2>&1
            ;;
        cartographer)
            echo "$task_content" | gemini -p "You are responding to a task dispatch. Do NOT use any tools. Simply read the objective and respond with text only." 2>&1
            ;;
        psyche|ajna)
            # Use Gateway-routed agent turn (no --local; stable in daemonized environments)
            # NOTE: openclaw agent requires a session selector; we target the default agent id "main".
            openclaw agent --agent main --message "$task_content" --timeout 600 2>&1
            ;;
        *)
            echo "[Watch] No CLI handler configured for agent: $AGENT"
            return 1
            ;;
    esac

    local exit_code=$?

    # Update in-body lifecycle truth then rename accordingly and append ledger
    python3 - "$claimed_file" "$exit_code" << 'PY'
import sys
from datetime import datetime, timezone

path = sys.argv[1]
exit_code = int(sys.argv[2])
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

lines = open(path, 'r', encoding='utf-8').read().splitlines(True)

def set_field(name: str, value: str):
    key = f"**{name}**:"
    for i, line in enumerate(lines):
        if line.startswith(key):
            lines[i] = f"{key} {value}\n"
            return
    # Insert after Claimed-At if present, else after Status
    insert_after = None
    for marker in ("**Claimed-At**:", "**Status**:"):
        for i, line in enumerate(lines):
            if line.startswith(marker):
                insert_after = i
                break
        if insert_after is not None:
            break
    if insert_after is None:
        insert_after = 0
    lines.insert(insert_after + 1, f"{key} {value}\n")

set_field("Status", "COMPLETE" if exit_code == 0 else "FAILED")
set_field("Completed-At", now)
set_field("Exit-Code", str(exit_code))

open(path, 'w', encoding='utf-8').write(''.join(lines))
PY

    if [ $exit_code -eq 0 ]; then
        local complete_name="${claimed_file%.claimed-by-*}.complete"
        mv "$claimed_file" "$complete_name" 2>/dev/null || true
        echo "[Watch] $(date '+%H:%M:%S') Task completed: $original_basename"
        if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
            bash "$SCRIPTS_DIR/append_ledger.sh" COMPLETE "$AGENT" "—" "$original_basename" >/dev/null 2>&1 || true
        fi
    else
        local failed_name="${claimed_file%.claimed-by-*}.failed"
        mv "$claimed_file" "$failed_name" 2>/dev/null || true
        echo "[Watch] $(date '+%H:%M:%S') Task FAILED (exit $exit_code): $original_basename"
        if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
            bash "$SCRIPTS_DIR/append_ledger.sh" FAILED "$AGENT" "—" "$original_basename" >/dev/null 2>&1 || true
        fi
    fi
}

handle_task() {
    local file="$1"
    local basename=$(basename "$file")

    # Only process TASK-*.md files with PENDING status
    if [[ "$basename" != TASK-* ]] || [[ "$basename" != *.md ]]; then
        return
    fi

    if ! grep -q "Status.*PENDING" "$file" 2>/dev/null; then
        return
    fi

    # Attempt atomic claim
    local claimed_file
    claimed_file=$(claim_task "$file") || return 0

    # Process the claimed task
    process_task "$claimed_file" "$basename"
}

# Check if fswatch is available
if command -v fswatch &>/dev/null; then
    echo "[Watch] Using fswatch (event-driven, low overhead)"
    echo ""
    # NOTE: some fswatch builds/platforms do not reliably emit the specific event filters.
    # We watch the directory and handle any signaled path.
    fswatch -0 "$WATCH_DIR" | while IFS= read -r -d '' file; do
        handle_task "$file"
    done
else
    echo "[Watch] fswatch not found. Using polling fallback (${POLL_INTERVAL}s interval)"
    echo "[Watch] Install fswatch for event-driven watching: brew install fswatch"
    echo ""
    while true; do
        for file in "$WATCH_DIR"/TASK-*.md; do
            [ -f "$file" ] || continue
            handle_task "$file"
        done
        sleep "$POLL_INTERVAL"
    done
fi
