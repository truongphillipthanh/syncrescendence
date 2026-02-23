#!/usr/bin/env bash
# post_commit_ledger.sh — Lightweight post-commit ledger check
# Triggered by PostToolUse hook after git commit commands
# Checks if any ledger files need updating based on what was committed
#
# This is a FAST check (<2s). It does NOT perform updates — it flags
# ledgers that may need attention so the agent can invoke
# update_universal_ledger skill if needed.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then exit 0; fi

STATE_DIR="$REPO_ROOT/00-ORCHESTRATION/state"
STAGING="$STATE_DIR/DYN-EXECUTION_STAGING.md"

# Get the files changed in the most recent commit
CHANGED_FILES=$(git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null || echo "")
if [ -z "$CHANGED_FILES" ]; then
    exit 0
fi

NEEDS_UPDATE=""

# Check if task-related files changed (implies tasks.csv may need updating)
if echo "$CHANGED_FILES" | grep -qE "(agents/.*/inbox/|TASK-|DIRECTIVE-|RESULT-)"; then
    NEEDS_UPDATE="${NEEDS_UPDATE}tasks.csv "
fi

# Check if project-level files changed (implies projects.csv may need updating)
if echo "$CHANGED_FILES" | grep -qE "(IMPLEMENTATION-MAP|DYN-BACKLOG|PROJ-)"; then
    NEEDS_UPDATE="${NEEDS_UPDATE}projects.csv "
fi

# Check if orchestration state changed (implies execution staging)
if echo "$CHANGED_FILES" | grep -qE "(00-ORCHESTRATION/state/)"; then
    NEEDS_UPDATE="${NEEDS_UPDATE}execution-staging "
fi

# Check if CANON files changed (may need source tracking)
if echo "$CHANGED_FILES" | grep -qE "(01-CANON/)"; then
    NEEDS_UPDATE="${NEEDS_UPDATE}sources.csv "
fi

# Report if anything flagged
if [ -n "$NEEDS_UPDATE" ]; then
    echo "[PostCommit] Ledger check: may need updating — ${NEEDS_UPDATE}"

    # Append a lightweight note to execution staging if it exists
    if [ -f "$STAGING" ]; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
        COMMIT_HASH=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
        COMMIT_MSG=$(git log --format='%s' -1 2>/dev/null || echo "unknown")
        printf "\n> **%s** | Commit \`%s\`: %s — Ledger check: %s\n" \
            "$TIMESTAMP" "$COMMIT_HASH" "$COMMIT_MSG" "$NEEDS_UPDATE" >> "$STAGING"
    fi
fi
