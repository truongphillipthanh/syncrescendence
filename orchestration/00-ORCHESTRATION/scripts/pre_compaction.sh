#!/bin/bash
# Pre-compaction hook — fires on PreCompact event
# Ensures working state is persisted to filesystem before context compaction

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then exit 0; fi

echo "[Hook] Pre-compaction: checking for uncommitted work..."

# Policy override (explicit)
# - Set COMPACTION_OVERRIDE=1 to allow compaction to proceed even if dirty.
OVERRIDE="${COMPACTION_OVERRIDE:-0}"

DIRTY=0

# Check for uncommitted changes
if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
    DIRTY=1
    echo "[Hook] WARNING: Uncommitted changes detected. Persist state before compaction."
    git status --short 2>/dev/null || true
fi

# Check for untracked files in key directories
UNTRACKED=$(git ls-files --others --exclude-standard orchestration/state/ engine/ praxis/ 2>/dev/null | head -20)
if [ -n "$UNTRACKED" ]; then
    DIRTY=1
    echo "[Hook] WARNING: Untracked files in working directories:"
    echo "$UNTRACKED"
fi

if [ "$DIRTY" -eq 1 ] && [ "$OVERRIDE" != "1" ]; then
    echo "[Hook] BLOCKING COMPACTION: repo is dirty in protected dirs."
    echo "[Hook] To override (explicitly): COMPACTION_OVERRIDE=1"
    exit 2
fi

echo "[Hook] Pre-compaction check complete."
