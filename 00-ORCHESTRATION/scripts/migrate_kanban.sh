#!/bin/bash
# migrate_kanban.sh — One-time migration from flat inbox/outgoing to kanban structure
# Usage: bash migrate_kanban.sh [--dry-run]
#
# This script:
#   1. Creates kanban subdirectories for all agents
#   2. Creates -OUTBOX/<agent>/RESULTS/ and ARTIFACTS/ directories
#   3. Moves existing files into correct kanban folders based on status/suffix
#   4. Moves -OUTGOING RESULT files to -OUTBOX/<agent>/RESULTS/
#   5. Removes iCloud " 2" duplicate files
#
# Protocol: DYN-DISPATCH_KANBAN_PROTOCOL.md
# Safe to run multiple times (idempotent moves; skips files already in place)

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

DRY_RUN=false
if [ "${1:-}" = "--dry-run" ]; then
    DRY_RUN=true
    echo "[Migrate] DRY RUN — no files will be moved or deleted"
fi

AGENTS="commander adjudicator cartographer psyche ajna"
KANBAN_LANES="00-INBOX0 10-IN_PROGRESS 20-WAITING 30-BLOCKED 40-DONE 50_FAILED 90_ARCHIVE RECEIPTS"

moved=0
deleted=0
created=0
skipped=0

do_mkdir() {
    local dir="$1"
    if [ ! -d "$dir" ]; then
        if [ "$DRY_RUN" = true ]; then
            echo "  [mkdir] $dir"
        else
            mkdir -p "$dir"
        fi
        (( created++ )) || true
    fi
}

do_mv() {
    local src="$1"
    local dest="$2"
    if [ ! -f "$src" ]; then
        return
    fi
    if [ -f "$dest" ]; then
        echo "  [skip] $src (destination exists)"
        (( skipped++ )) || true
        return
    fi
    if [ "$DRY_RUN" = true ]; then
        echo "  [mv] $(basename "$src") → $(dirname "$dest" | sed "s|$REPO_ROOT/||")"
    else
        mv "$src" "$dest"
    fi
    (( moved++ )) || true
}

do_rm() {
    local file="$1"
    if [ ! -f "$file" ]; then
        return
    fi
    if [ "$DRY_RUN" = true ]; then
        echo "  [rm] $(basename "$file") (iCloud duplicate)"
    else
        rm -f "$file"
    fi
    (( deleted++ )) || true
}

echo "=== KANBAN MIGRATION ==="
echo "Repo: $REPO_ROOT"
echo ""

# === Step 1: Create kanban directories ===
echo "--- Step 1: Create kanban directories ---"
for agent in $AGENTS; do
    for lane in $KANBAN_LANES; do
        do_mkdir "$REPO_ROOT/-INBOX/$agent/$lane"
    done
done

# === Step 2: Create -OUTBOX directories ===
echo "--- Step 2: Create -OUTBOX directories ---"
for agent in $AGENTS; do
    do_mkdir "$REPO_ROOT/-OUTBOX/$agent/RESULTS"
    do_mkdir "$REPO_ROOT/-OUTBOX/$agent/ARTIFACTS"
done
echo ""

# === Step 3: Delete iCloud " 2" duplicates ===
echo "--- Step 3: Clean iCloud duplicates ---"
while IFS= read -r -d '' file; do
    do_rm "$file"
done < <(find "$REPO_ROOT/-INBOX" "$REPO_ROOT/-OUTGOING" -name "* 2*" -type f -print0 2>/dev/null)
echo ""

# === Step 4: Migrate -INBOX files per agent ===
echo "--- Step 4: Migrate -INBOX files ---"
for agent in $AGENTS; do
    agent_dir="$REPO_ROOT/-INBOX/$agent"
    echo "  Agent: $agent"

    # Process files directly in the agent root (flat structure)
    for file in "$agent_dir"/*; do
        [ -f "$file" ] || continue
        basename=$(basename "$file")

        # Skip .gitkeep and .DS_Store
        case "$basename" in
            .gitkeep|.DS_Store) continue ;;
        esac

        # Skip files already in kanban subdirs
        file_dir=$(dirname "$file")
        if [ "$file_dir" != "$agent_dir" ]; then
            continue
        fi

        # Route by filename suffix and kind
        # NOTE: RECEIPT/RESULT/RESPONSE patterns MUST come before suffix patterns
        # to prevent RECEIPT-*.md.complete from matching *.md.complete first
        case "$basename" in
            # RECEIPT and RESULT files → RECEIPTS/ (regardless of suffix)
            RECEIPT-*|RESULT-*.md)
                do_mv "$file" "$agent_dir/RECEIPTS/$basename"
                ;;

            # RESPONSE files → 90_ARCHIVE/
            RESPONSE-*.md)
                do_mv "$file" "$agent_dir/90_ARCHIVE/$basename"
                ;;

            # OPENCLAW_BOOTSTRAP, previous_conversation → 90_ARCHIVE/
            OPENCLAW_BOOTSTRAP*|previous_conversation*)
                do_mv "$file" "$agent_dir/90_ARCHIVE/$basename"
                ;;

            # Completed files (suffix .complete)
            *.md.complete)
                clean_name="${basename%.complete}"
                do_mv "$file" "$agent_dir/40-DONE/$clean_name"
                ;;

            # Failed files (suffix .failed)
            *.md.failed)
                clean_name="${basename%.failed}"
                do_mv "$file" "$agent_dir/50_FAILED/$clean_name"
                ;;

            # Claimed files (suffix .claimed-by-*)
            *.claimed-by-*)
                # Extract original name: everything before .claimed-by-
                clean_name=$(echo "$basename" | sed 's/\.claimed-by-.*//')
                do_mv "$file" "$agent_dir/10-IN_PROGRESS/$clean_name"
                ;;

            # TASK-*.md and SURVEY-*.md (plain, no suffix) → check status
            TASK-*.md|SURVEY-*.md)
                if grep -q "Status.*PENDING" "$file" 2>/dev/null; then
                    do_mv "$file" "$agent_dir/00-INBOX0/$basename"
                elif grep -q "Status.*IN_PROGRESS" "$file" 2>/dev/null; then
                    do_mv "$file" "$agent_dir/10-IN_PROGRESS/$basename"
                elif grep -q "Status.*COMPLETE" "$file" 2>/dev/null; then
                    do_mv "$file" "$agent_dir/40-DONE/$basename"
                elif grep -q "Status.*FAILED" "$file" 2>/dev/null; then
                    do_mv "$file" "$agent_dir/50_FAILED/$basename"
                else
                    # Default: treat as pending (move to INBOX0)
                    do_mv "$file" "$agent_dir/00-INBOX0/$basename"
                fi
                ;;

            # Other .md files (adjudicator-macmini, ajna's questions, etc.) → 90_ARCHIVE/
            *.md)
                do_mv "$file" "$agent_dir/90_ARCHIVE/$basename"
                ;;
        esac
    done
done
echo ""

# === Step 5: Migrate -OUTGOING RESULT files to -OUTBOX ===
echo "--- Step 5: Migrate -OUTGOING RESULT files to -OUTBOX ---"
for file in "$REPO_ROOT/-OUTGOING"/RESULT-*.md; do
    [ -f "$file" ] || continue
    basename=$(basename "$file")

    # Extract agent name from RESULT-<agent>-YYYYMMDD-topic.md
    agent=$(echo "$basename" | sed -n 's/^RESULT-\([a-z]*\)-.*/\1/p')
    if [ -n "$agent" ] && echo "$AGENTS" | grep -qw "$agent"; then
        do_mv "$file" "$REPO_ROOT/-OUTBOX/$agent/RESULTS/$basename"
    else
        echo "  [skip] $basename (cannot determine agent)"
        (( skipped++ )) || true
    fi
done

# Migrate EVIDENCE and DISPATCH files to -OUTGOING (keep in place as staging)
echo ""

# === Step 6: Add .gitkeep to empty kanban dirs ===
echo "--- Step 6: Add .gitkeep to new directories ---"
for agent in $AGENTS; do
    for lane in $KANBAN_LANES; do
        lane_dir="$REPO_ROOT/-INBOX/$agent/$lane"
        if [ -d "$lane_dir" ] && [ -z "$(ls -A "$lane_dir" 2>/dev/null)" ]; then
            if [ "$DRY_RUN" = false ]; then
                touch "$lane_dir/.gitkeep"
            fi
        fi
    done
    for sub in RESULTS ARTIFACTS; do
        sub_dir="$REPO_ROOT/-OUTBOX/$agent/$sub"
        if [ -d "$sub_dir" ] && [ -z "$(ls -A "$sub_dir" 2>/dev/null)" ]; then
            if [ "$DRY_RUN" = false ]; then
                touch "$sub_dir/.gitkeep"
            fi
        fi
    done
done

echo ""
echo "=== MIGRATION SUMMARY ==="
echo "  Directories created: $created"
echo "  Files moved: $moved"
echo "  iCloud duplicates deleted: $deleted"
echo "  Files skipped (already in place): $skipped"

if [ "$DRY_RUN" = true ]; then
    echo ""
    echo "This was a DRY RUN. Run without --dry-run to execute."
fi
