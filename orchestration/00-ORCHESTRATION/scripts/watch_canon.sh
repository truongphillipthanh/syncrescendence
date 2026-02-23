#!/bin/bash
# watch_canon.sh — Monitor state/ for data changes and trigger CANON regeneration
#
# Usage:
#   ./watch_canon.sh              # Watch and auto-regenerate
#   ./watch_canon.sh --once       # Single regeneration pass (no watch)
#   ./watch_canon.sh --dry-run    # Show what would regenerate
#
# Requires: fswatch (brew install fswatch), python3, jinja2
# Watches: orchestration/state/platform_capabilities.json
#          orchestration/state/DYN-TICKER_FEED.md
#          engine/MODEL-INDEX.md

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
STATE_DIR="$REPO_ROOT/orchestration/state"
REGENERATE_SCRIPT="$SCRIPT_DIR/regenerate_canon.py"
LOG_FILE="$STATE_DIR/DYN-CANON_REGEN_LOG.md"

# Template registry (maps CANON IDs → data sources + watch paths)
REGISTRY_FILE="$REPO_ROOT/orchestration/templates/template_registry.json"

# Build watch paths from registry + defaults
build_watch_paths() {
    local paths=()
    # Always watch the registry itself
    paths+=("$REGISTRY_FILE")
    # Extract watch_paths from registry via Python
    if [ -f "$REGISTRY_FILE" ] && command -v python3 &>/dev/null; then
        while IFS= read -r p; do
            paths+=("$REPO_ROOT/$p")
        done < <(python3 -c "
import json, sys
with open('$REGISTRY_FILE') as f:
    reg = json.load(f)
for entry in reg.values():
    for wp in entry.get('watch_paths', []):
        print(wp)
" 2>/dev/null)
    fi
    printf '%s\n' "${paths[@]}" | sort -u
}

WATCH_PATHS=()
while IFS= read -r p; do
    WATCH_PATHS+=("$p")
done < <(build_watch_paths)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

log() {
    echo -e "${GREEN}[Canon]${NC} $(date '+%H:%M:%S') $1"
}

warn() {
    echo -e "${YELLOW}[Canon]${NC} $(date '+%H:%M:%S') $1"
}

error() {
    echo -e "${RED}[Canon]${NC} $(date '+%H:%M:%S') $1"
}

append_regen_log() {
    local trigger="$1"
    local status="$2"
    local canon_ids="${3:-unknown}"
    local timestamp
    timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')

    if [ ! -f "$LOG_FILE" ]; then
        cat > "$LOG_FILE" << 'HEADER'
# CANON Regeneration Log
## Append-only log of automated CANON regenerations

| Timestamp | Trigger | Status | CANON IDs |
|-----------|---------|--------|-----------|
HEADER
    fi

    echo "| $timestamp | $trigger | $status | $canon_ids |" >> "$LOG_FILE"
}

regenerate() {
    local trigger="${1:-manual}"
    local lockdir="/tmp/syncrescendence-canon.lock"

    # Prevent overlapping regen runs
    if ! mkdir "$lockdir" 2>/dev/null; then
        warn "Regen already in progress (lock: $lockdir). Skipping."
        return 0
    fi
    trap 'rmdir "$lockdir" 2>/dev/null' RETURN

    log "Regenerating CANON files (trigger: $trigger)..."

    local output
    if output=$(python3 "$REGENERATE_SCRIPT" --all --json 2>&1); then
        # Extract CANON IDs from JSON output
        local ids
        ids=$(echo "$output" | python3 -c "import sys,json; d=json.load(sys.stdin); print(','.join(r['canon_id'] for r in d.get('results',[]) if r.get('success')))" 2>/dev/null || echo "unknown")
        log "Regeneration complete."
        append_regen_log "$trigger" "SUCCESS" "$ids"
        return 0
    else
        error "Regeneration FAILED."
        append_regen_log "$trigger" "FAILED" "none"
        return 1
    fi
}

# Parse arguments
MODE="watch"
for arg in "$@"; do
    case "$arg" in
        --once)
            MODE="once"
            ;;
        --dry-run)
            MODE="dry-run"
            ;;
        --help|-h)
            echo "Usage: watch_canon.sh [--once|--dry-run|--help]"
            echo ""
            echo "  --once     Single regeneration pass (no watch)"
            echo "  --dry-run  Show what would regenerate"
            echo "  --help     Show this help"
            exit 0
            ;;
    esac
done

# Check prerequisites
if ! command -v python3 &>/dev/null; then
    error "python3 not found"
    exit 1
fi

if [ ! -f "$REGENERATE_SCRIPT" ]; then
    error "regenerate_canon.py not found at $REGENERATE_SCRIPT"
    exit 1
fi

case "$MODE" in
    dry-run)
        echo "CANON Regeneration Dry Run"
        echo "========================="
        echo ""
        echo "Watched paths:"
        for path in "${WATCH_PATHS[@]}"; do
            if [ -f "$path" ]; then
                echo "  [EXISTS] $path"
            else
                echo "  [MISSING] $path"
            fi
        done
        echo ""
        echo "Regeneration script: $REGENERATE_SCRIPT"
        echo "Available CANON templates:"
        python3 "$REGENERATE_SCRIPT" --list 2>&1
        ;;

    once)
        regenerate "manual"
        ;;

    watch)
        if ! command -v fswatch &>/dev/null; then
            error "fswatch not found. Install with: brew install fswatch"
            exit 1
        fi

        log "Starting CANON watch daemon..."
        log "Monitoring ${#WATCH_PATHS[@]} paths for changes."
        echo ""

        # Build fswatch path list (only existing files)
        EXISTING_PATHS=()
        for path in "${WATCH_PATHS[@]}"; do
            if [ -f "$path" ]; then
                EXISTING_PATHS+=("$path")
                log "  Watching: $(basename "$path")"
            else
                warn "  Skipping (not found): $(basename "$path")"
            fi
        done

        if [ ${#EXISTING_PATHS[@]} -eq 0 ]; then
            error "No watched files exist. Create platform_capabilities.json to begin."
            exit 1
        fi

        echo ""
        log "Watching for changes... (Ctrl+C to stop)"

        # Debounce: wait 2 seconds after last change before regenerating
        fswatch -o --latency 2 "${EXISTING_PATHS[@]}" | while read -r _; do
            log "Change detected!"
            regenerate "fswatch"
        done
        ;;
esac
