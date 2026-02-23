#!/bin/bash
# compact_wisdom.sh — Compact staged directives/logs into wisdom compendiums
# Triggered manually or when staging threshold (10 entries) is reached
# Appends staging entries to compendiums and clears staging files

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi

DIR_STAGING="$REPO_ROOT/orchestration/state/DYN-DIRECTIVE_STAGING.md"
EXEC_STAGING="$REPO_ROOT/orchestration/state/DYN-EXECUTION_STAGING.md"
DIR_COMPENDIUM="$REPO_ROOT/orchestration/archive/ARCH-DIRECTIVE_COMPENDIUM.md"
EXEC_HISTORY="$REPO_ROOT/orchestration/archive/ARCH-EXECUTION_HISTORY.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

COMPACTED=0

# Compact directives if staging exists and has entries
if [ -f "$DIR_STAGING" ]; then
    DIR_COUNT=$(grep -c "^### DIRECTIVE-" "$DIR_STAGING" 2>/dev/null || echo "0")
    if [ "$DIR_COUNT" -gt 0 ]; then
        echo "[Compact] Compacting $DIR_COUNT directive(s) into compendium..."

        # Append compaction header and entries to compendium
        echo "" >> "$DIR_COMPENDIUM"
        echo "### Compaction: $TIMESTAMP ($DIR_COUNT entries)" >> "$DIR_COMPENDIUM"
        echo "" >> "$DIR_COMPENDIUM"

        # Extract entries (everything after the header line "---")
        sed -n '/^### DIRECTIVE-/,$p' "$DIR_STAGING" >> "$DIR_COMPENDIUM"

        # Reset staging file
        cat > "$DIR_STAGING" << 'HEADER'
# Directive Staging
**Auto-managed by create_directive.sh**
**Compacts into ARCH-DIRECTIVE_COMPENDIUM.md when threshold reached**
**Threshold**: 10 entries triggers compaction

---
HEADER
        echo "[Compact] $DIR_COUNT directive(s) compacted into ARCH-DIRECTIVE_COMPENDIUM.md"
        COMPACTED=$((COMPACTED + DIR_COUNT))
    fi
fi

# Compact execution logs if staging exists and has entries
if [ -f "$EXEC_STAGING" ]; then
    EXEC_COUNT=$(grep -c "^### " "$EXEC_STAGING" 2>/dev/null || echo "0")
    if [ "$EXEC_COUNT" -gt 0 ]; then
        echo "[Compact] Compacting $EXEC_COUNT execution log(s) into history..."

        # Append compaction header and entries to history
        echo "" >> "$EXEC_HISTORY"
        echo "### Compaction: $TIMESTAMP ($EXEC_COUNT entries)" >> "$EXEC_HISTORY"
        echo "" >> "$EXEC_HISTORY"

        # Extract entries
        sed -n '/^### /,$p' "$EXEC_STAGING" >> "$EXEC_HISTORY"

        # Reset staging file
        cat > "$EXEC_STAGING" << 'HEADER'
# Execution Log Staging
**Auto-managed by create_execution_log.sh**
**Compacts into ARCH-EXECUTION_HISTORY.md when threshold reached**
**Threshold**: 10 entries triggers compaction

---
HEADER
        echo "[Compact] $EXEC_COUNT execution log(s) compacted into ARCH-EXECUTION_HISTORY.md"
        COMPACTED=$((COMPACTED + EXEC_COUNT))
    fi
fi

if [ "$COMPACTED" -eq 0 ]; then
    echo "[Compact] Nothing to compact. Staging files empty or missing."
else
    echo "[Compact] Total compacted: $COMPACTED entries. Staging files reset."
fi
