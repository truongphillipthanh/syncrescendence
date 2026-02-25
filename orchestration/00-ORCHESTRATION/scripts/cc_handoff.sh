#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# cc_handoff.sh — Commander Council PreCompact Handoff Generator
# Fires on PreCompact event. Generates a bulletproof handoff file for cold-start continuity.
# Uses git write-tree/commit-tree to avoid sandbox SIGKILL on large repos.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "/Users/system/syncrescendence")"
cd "$REPO_ROOT"

echo "[CC-Handoff] Generating Commander Council handoff..."

# --- Determine CC number ---
LATEST_HANDOFF=$(ls agents/commander/outbox/handoffs/HANDOFF-CC* 2>/dev/null | sort -V | tail -1 || true)
if [ -n "$LATEST_HANDOFF" ]; then
    CC_NUM=$(echo "$LATEST_HANDOFF" | grep -oE 'CC[0-9]+' | grep -oE '[0-9]+' | tail -1)
else
    CC_NUM=26
fi
# Same session — use current CC number
echo "[CC-Handoff] Current Council: CC${CC_NUM}"

# --- Gather state (every section fail-safe) ---
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
DATE_STAMP=$(date +"%Y%m%d%H%M")
GIT_HEAD=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_LOG=$(git log --oneline -10 2>/dev/null || echo "unavailable")
GIT_STATUS=$(git status --short 2>/dev/null || echo "unavailable")
[ -z "$GIT_STATUS" ] && GIT_STATUS="Clean"

# Trust level from autonomy ledger
TRUST_LEVEL="unavailable"
if [ -f "agents/commander/AUTONOMY_LEDGER.md" ]; then
    TRUST_LEVEL=$(head -20 agents/commander/AUTONOMY_LEDGER.md 2>/dev/null | grep -iE '(level|trust|current)' | head -3 || echo "see AUTONOMY_LEDGER.md")
    [ -z "$TRUST_LEVEL" ] && TRUST_LEVEL="see AUTONOMY_LEDGER.md"
fi

# Current priorities
PRIORITIES="unavailable"
if [ -f "${ORCHESTRATION_DIR#$REPO_ROOT/}/state/DYN-SESSION_STATE_BRIEF.md" ]; then
    PRIORITIES=$(cat orchestration/00-ORCHESTRATION/state/DYN-SESSION_STATE_BRIEF.md 2>/dev/null || echo "unavailable")
fi

# Deferred commitments (first 50 lines)
DEFERRED="unavailable"
if [ -f "${ORCHESTRATION_DIR#$REPO_ROOT/}/state/DYN-DEFERRED_COMMITMENTS.md" ]; then
    DEFERRED=$(head -50 orchestration/00-ORCHESTRATION/state/DYN-DEFERRED_COMMITMENTS.md 2>/dev/null || echo "unavailable")
elif [ -f "orchestration/state/DYN-DEFERRED_COMMITMENTS.md" ]; then
    DEFERRED=$(head -50 orchestration/state/DYN-DEFERRED_COMMITMENTS.md 2>/dev/null || echo "unavailable")
fi

# Pending inbox items
INBOX_ITEMS="(none)"
if [ -d "-INBOX/commander/00-INBOX0/" ]; then
    INBOX_ITEMS=$(ls -1 "-INBOX/commander/00-INBOX0/" 2>/dev/null | head -20 || echo "(none)")
    [ -z "$INBOX_ITEMS" ] && INBOX_ITEMS="(none)"
fi

# Pending tasks
PENDING_TASKS="(none)"
if [ -d "agents/commander/inbox/pending/" ]; then
    PENDING_TASKS=$(ls -1 agents/commander/inbox/pending/ 2>/dev/null | head -20 || echo "(none)")
    [ -z "$PENDING_TASKS" ] && PENDING_TASKS="(none)"
fi

# Open Sovereign decisions
SOVEREIGN_ITEMS="(none)"
if [ -d "-SOVEREIGN/" ]; then
    SOVEREIGN_ITEMS=$(ls -1 "-SOVEREIGN/" 2>/dev/null | grep -v '^antifragile-scaffold-archive$' | grep -v '^ARCHIVED$' | head -20 || echo "(none)")
    [ -z "$SOVEREIGN_ITEMS" ] && SOVEREIGN_ITEMS="(none)"
fi

# Today's journal
JOURNAL_ENTRIES="(none)"
JOURNAL_FILE="agents/commander/memory/journal/$(date +%Y-%m-%d).jsonl"
if [ -f "$JOURNAL_FILE" ]; then
    JOURNAL_ENTRIES=$(tail -5 "$JOURNAL_FILE" 2>/dev/null || echo "(none)")
    [ -z "$JOURNAL_ENTRIES" ] && JOURNAL_ENTRIES="(none)"
fi

# --- Write handoff file ---
HANDOFF_FILE="agents/commander/outbox/handoffs/HANDOFF-CC${CC_NUM}-AUTOCOMPACT-${DATE_STAMP}.md"

cat > "$HANDOFF_FILE" << HANDOFF_EOF
# HANDOFF — Commander Council ${CC_NUM} — Auto-Compaction

**Date**: ${TIMESTAMP}
**Agent**: Commander (Claude Opus 4.6, MacBook Air)
**Session**: CC${CC_NUM}
**Git HEAD**: ${GIT_HEAD}
**Trust Level**: ${TRUST_LEVEL}
**Trigger**: PreCompact (context approaching limit)

---

## SESSION STATE AT COMPACTION

### Recent Commits (this session)
\`\`\`
${GIT_LOG}
\`\`\`

### Uncommitted Work
\`\`\`
${GIT_STATUS}
\`\`\`

### Current Priorities
${PRIORITIES}

### Open Sovereign Decisions
\`\`\`
${SOVEREIGN_ITEMS}
\`\`\`

### Pending Inbox
\`\`\`
${INBOX_ITEMS}
\`\`\`

### Pending Tasks
\`\`\`
${PENDING_TASKS}
\`\`\`

### Autonomy Ledger
${TRUST_LEVEL}

### Today's Journal (last 5 entries)
\`\`\`
${JOURNAL_ENTRIES}
\`\`\`

### Deferred Commitments (first 50 lines)
\`\`\`
${DEFERRED}
\`\`\`

---

## WHAT THE NEXT SESSION MUST KNOW

- [AUTO-GENERATED] This handoff was triggered by PreCompact, not by session completion.
- [AUTO-GENERATED] The agent may have been mid-task. Check git status and journal for in-progress work.
- [AUTO-GENERATED] Load this file + MEMORY.md + the latest CC responses for full context.
- [AUTO-GENERATED] Review \`-INBOX/commander/00-INBOX0/\` for any unprocessed triangulation responses.

---

## KEY FILES

| File | Purpose |
|------|---------|
| \`CLAUDE.md\` | Constitutional law + Commander extensions |
| \`orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md\` | Intention archaeology |
| \`orchestration/00-ORCHESTRATION/state/DYN-SESSION_STATE_BRIEF.md\` | Session priorities |
| \`orchestration/00-ORCHESTRATION/state/DYN-DEFERRED_COMMITMENTS.md\` | Open commitments |
| \`agents/commander/AUTONOMY_LEDGER.md\` | Trust level + gate progress |
| \`agents/commander/memory/MEMORY.md\` | Commander persistent memory |
| \`-INBOX/commander/00-INBOX0/INDEX-TRIANGULATION_RESPONSES.md\` | Triangulation response index |
| \`engine/REF-ROSETTA_STONE.md\` | Terminology reconciliation |
| \`canon/CANON-25500-ARCHITECTURE_RATIONALE-lattice.md\` | Architecture rationale |
HANDOFF_EOF

echo "[CC-Handoff] Wrote: ${HANDOFF_FILE}"

# --- Copy to Commander inbox for next-session cold-start ---
cp "$HANDOFF_FILE" "-INBOX/commander/00-INBOX0/HANDOFF-LATEST.md" 2>/dev/null || echo "[CC-Handoff] WARNING: Could not copy to inbox"
echo "[CC-Handoff] Copied to -INBOX/commander/00-INBOX0/HANDOFF-LATEST.md"

# --- Print initializer for Sovereign to paste into fresh session ---
echo ""
echo "=== PASTE THIS INTO FRESH CLAUDE CODE SESSION ==="
echo "Resume CC${CC_NUM}. Rehydrate from: @agents/commander/outbox/handoffs/HANDOFF-CC${CC_NUM}-AUTOCOMPACT-${DATE_STAMP}.md"
echo "================================================="

# --- Sandbox-safe commit (git write-tree → commit-tree → update-ref) ---
# Clean up any stale lock
rm -f .git/index.lock 2>/dev/null || true

git add "$HANDOFF_FILE" 2>/dev/null || true

TREE=$(git write-tree 2>/dev/null || true)
if [ -n "$TREE" ]; then
    PARENT=$(git rev-parse HEAD 2>/dev/null || true)
    if [ -n "$PARENT" ]; then
        COMMIT_MSG="chore: auto-compaction handoff CC${CC_NUM} (${DATE_STAMP})"
        NEW_COMMIT=$(echo "$COMMIT_MSG" | git commit-tree "$TREE" -p "$PARENT" 2>/dev/null || true)
        if [ -n "$NEW_COMMIT" ]; then
            git update-ref HEAD "$NEW_COMMIT" 2>/dev/null || true
            echo "[CC-Handoff] Committed: ${NEW_COMMIT}"
        else
            echo "[CC-Handoff] WARNING: commit-tree failed; handoff file is unstaged"
        fi
    fi
else
    echo "[CC-Handoff] WARNING: write-tree failed; handoff file written but not committed"
fi

echo "[CC-Handoff] Done. Next session: load ${HANDOFF_FILE}"
