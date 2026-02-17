#!/bin/bash
# create_execution_log.sh — Generate an execution log entry in staging
# Usage: bash create_execution_log.sh "DIRECTIVE_ID" "OUTCOME" [DETAILS]
# Appends to DYN-EXECUTION_STAGING.md for later compaction into wisdom
# Can also be called without args to auto-generate from git state

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi

STAGING="$REPO_ROOT/00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
FINGERPRINT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")

DIRECTIVE_ID="${1:-AUTO}"
OUTCOME="${2:-SUCCESS}"
DETAILS="${3:-}"

# Auto-detect from recent git activity if no directive specified
if [ "$DIRECTIVE_ID" = "AUTO" ]; then
    RECENT_MSG=$(git log --oneline -1 2>/dev/null || echo "no commits")
    DIRECTIVE_ID="SESSION-$(date '+%Y%m%d-%H%M')"
    if [ -z "$DETAILS" ]; then
        DETAILS="$RECENT_MSG"
    fi
fi

# Gather session metrics
COMMITS_TODAY=$(git log --oneline --since="6 hours ago" 2>/dev/null | wc -l | tr -d ' ')
FILES_CHANGED=$(git diff --stat HEAD~${COMMITS_TODAY}..HEAD 2>/dev/null | tail -1 || echo "unknown")

# Create staging file with header if it doesn't exist
if [ ! -f "$STAGING" ]; then
    cat > "$STAGING" << 'HEADER'
# Execution Log Staging
**Auto-managed by create_execution_log.sh**
**Compacts into ARCH-EXECUTION_HISTORY.md when threshold reached**
**Threshold**: 10 entries triggers compaction

---
HEADER
fi

# Deduplication guard: skip if this HEAD fingerprint was already logged
if grep -q "Fingerprint.*$FINGERPRINT" "$STAGING" 2>/dev/null; then
    echo "[Execution] Skipped: fingerprint $FINGERPRINT already in staging"
    exit 0
fi

# Append execution log entry
cat >> "$STAGING" << EOF

### $DIRECTIVE_ID | $TIMESTAMP
- **Branch**: $BRANCH | **Fingerprint**: $FINGERPRINT
- **Outcome**: $OUTCOME
- **Commits**: $COMMITS_TODAY | **Changes**: $FILES_CHANGED
- **Details**: $DETAILS
EOF

# Count entries and auto-compact if threshold reached
ENTRY_COUNT=$(grep -c "^### " "$STAGING" 2>/dev/null || echo "0")
echo "[Execution] Logged $DIRECTIVE_ID: $OUTCOME ($ENTRY_COUNT entries in staging)"
if [ "$ENTRY_COUNT" -ge 10 ]; then
    echo "[Execution] THRESHOLD REACHED ($ENTRY_COUNT/10). Auto-compacting..."
    bash "$REPO_ROOT/00-ORCHESTRATION/scripts/compact_wisdom.sh"
    # Stage and commit the compaction
    git add "$STAGING" \
        "$REPO_ROOT/00-ORCHESTRATION/archive/ARCH-EXECUTION_HISTORY.md" \
        "$REPO_ROOT/00-ORCHESTRATION/archive/ARCH-DIRECTIVE_COMPENDIUM.md" \
        2>/dev/null
    git commit -m "chore: auto-compact wisdom at threshold ($ENTRY_COUNT entries)" 2>/dev/null
    echo "[Execution] Compaction committed."
fi
