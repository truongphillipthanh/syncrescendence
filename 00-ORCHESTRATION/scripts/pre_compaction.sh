#!/bin/bash
# Pre-compaction hook — fires on PreCompact event
# Ensures working state is persisted to filesystem before context compaction

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then exit 0; fi

echo "[Hook] Pre-compaction: checking for uncommitted work..."

# Check for uncommitted changes
if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
    echo "[Hook] WARNING: Uncommitted changes detected. Persist state before compaction."
    git status --short 2>/dev/null
fi

# Check for untracked files in key directories
UNTRACKED=$(git ls-files --others --exclude-standard 00-ORCHESTRATION/state/ 02-ENGINE/ 05-SIGMA/ 2>/dev/null | head -5)
if [ -n "$UNTRACKED" ]; then
    echo "[Hook] WARNING: Untracked files in working directories:"
    echo "$UNTRACKED"
fi

echo "[Hook] Pre-compaction check complete."
