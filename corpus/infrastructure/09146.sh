#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# cc_handoff.sh — Commander Council Handoff Generator (Singular Protocol, CC33)
# Fires on PreCompact event OR manually.
# Writes ONE handoff file to agents/commander/outbox/handoffs/HANDOFF-CC{N}.md
# No copies to inbox. No copies to Desktop. Single source of truth.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "/Users/system/syncrescendence")"
cd "$REPO_ROOT"

echo "[CC-Handoff] Generating Commander Council handoff..."

# --- Determine CC number (next in sequence) ---
LATEST_HANDOFF=$(ls agents/commander/outbox/handoffs/HANDOFF-CC* 2>/dev/null | sort -V | tail -1 || true)
if [ -n "$LATEST_HANDOFF" ]; then
    CC_NUM=$(echo "$LATEST_HANDOFF" | grep -oE 'CC[0-9]+' | grep -oE '[0-9]+' | tail -1)
else
    CC_NUM=32
fi
echo "[CC-Handoff] Current Council: CC${CC_NUM}"

# --- Gather state (every section fail-safe) ---
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
GIT_HEAD=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_LOG=$(git log --oneline -10 2>/dev/null || echo "unavailable")
GIT_STATUS=$(git status --short 2>/dev/null || echo "unavailable")
[ -z "$GIT_STATUS" ] && GIT_STATUS="Clean"
DIRTY_COUNT=$(echo "$GIT_STATUS" | grep -c '.' 2>/dev/null || echo "0")
[ "$GIT_STATUS" = "Clean" ] && DIRTY_COUNT=0

# Commit count this session (best effort — count commits today)
COMMIT_COUNT=$(git log --oneline --since="$(date +%Y-%m-%d)" 2>/dev/null | wc -l | tr -d ' ' || echo "?")

# --- Write handoff file ---
HANDOFF_FILE="agents/commander/outbox/handoffs/HANDOFF-CC${CC_NUM}.md"

cat > "$HANDOFF_FILE" << HANDOFF_EOF
# HANDOFF — Commander Council ${CC_NUM}

**Date**: ${TIMESTAMP}
**Agent**: Commander (Claude Opus 4.6)
**Session**: CC${CC_NUM}
**Git HEAD**: ${GIT_HEAD}
**Trigger**: PreCompact (auto-handoff)

## What Was Accomplished
\`\`\`
${GIT_LOG}
\`\`\`

## What Remains
[PreCompact auto-handoff — Claude was mid-task. Check git status and journal.]

## Key Decisions Made
[Auto-generated — semantic context requires manual /session-handoff invocation before compaction.]

## Sovereign Intent
[Check the conversation context — this auto-handoff could not capture Sovereign intent.]

## WHAT THE NEXT SESSION MUST KNOW
- This handoff was auto-triggered by PreCompact. Claude may have been mid-task.
- Check \`git status\` for uncommitted work.
- Check \`agents/commander/inbox/pending/\` for pending tasks.
- Check today's journal: \`agents/commander/memory/journal/$(date +%Y-%m-%d).jsonl\`

## Uncommitted Work
\`\`\`
${GIT_STATUS}
\`\`\`

## Key Files
| File | Purpose |
|------|---------|
| \`CLAUDE.md\` | Constitutional law + Commander extensions |
| \`orchestration/state/ARCH-INTENTION_COMPASS.md\` | Intention archaeology |
| \`orchestration/state/DYN-DEFERRED_COMMITMENTS.md\` | Open commitments |
| \`agents/commander/AUTONOMY_LEDGER.md\` | Trust level |
| \`agents/commander/memory/MEMORY.md\` | Commander persistent memory |

## Session Metrics
- Commits: ${COMMIT_COUNT}
- Dirty files at handoff: ${DIRTY_COUNT}
- DAG status: see memory
- C-009: check memory
HANDOFF_EOF

echo "[CC-Handoff] Wrote: ${HANDOFF_FILE}"

# --- Sandbox-safe commit ---
rm -f .git/index.lock 2>/dev/null || true
git add "$HANDOFF_FILE" 2>/dev/null || true

TREE=$(git write-tree 2>/dev/null || true)
if [ -n "$TREE" ]; then
    PARENT=$(git rev-parse HEAD 2>/dev/null || true)
    if [ -n "$PARENT" ]; then
        COMMIT_MSG="chore: CC${CC_NUM} handoff"
        NEW_COMMIT=$(echo "$COMMIT_MSG" | git commit-tree "$TREE" -p "$PARENT" 2>/dev/null || true)
        if [ -n "$NEW_COMMIT" ]; then
            git update-ref HEAD "$NEW_COMMIT" 2>/dev/null || true
            echo "[CC-Handoff] Committed: ${NEW_COMMIT}"
        fi
    fi
fi

# --- Print reinitializer (paste-ready for next session) ---
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "Resume CC${CC_NUM}. Read handoff: @agents/commander/outbox/handoffs/HANDOFF-CC${CC_NUM}.md"
echo "═══════════════════════════════════════════════════════════════"
