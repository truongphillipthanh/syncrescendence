#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# create_directive.sh — Generate a new directive entry in staging
# Usage: bash create_directive.sh "TITLE" "SUMMARY" [STREAM]
# Appends to DYN-DIRECTIVE_STAGING.md for later compaction into wisdom

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi

STAGING="$REPO_ROOT/orchestration/state/DYN-DIRECTIVE_STAGING.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
DATE=$(date '+%Y-%m-%d')

# Get next directive number from compendium + staging
LAST_COMPENDIUM=$(grep -oP 'DIRECTIVE-\K[0-9]+' "$REPO_ROOT/orchestration/archive/ARCH-DIRECTIVE_COMPENDIUM.md" 2>/dev/null | sort -n | tail -1 || echo "048")
LAST_STAGING=$(grep -oP 'DIRECTIVE-\K[0-9]+' "$STAGING" 2>/dev/null | sort -n | tail -1 || echo "0")
NEXT_NUM=$((LAST_COMPENDIUM > LAST_STAGING ? LAST_COMPENDIUM + 1 : LAST_STAGING + 1))
DIRECTIVE_ID=$(printf "DIRECTIVE-%03d" $NEXT_NUM)

TITLE="${1:-UNTITLED}"
SUMMARY="${2:-No summary provided}"
STREAM="${3:-A}"

# Create staging file with header if it doesn't exist
if [ ! -f "$STAGING" ]; then
    cat > "$STAGING" << 'HEADER'
# Directive Staging
**Auto-managed by create_directive.sh**
**Compacts into ARCH-DIRECTIVE_COMPENDIUM.md when threshold reached**
**Threshold**: 10 entries triggers compaction

---
HEADER
fi

# Append directive entry
cat >> "$STAGING" << EOF

### $DIRECTIVE_ID | $TITLE
- **Issued**: $TIMESTAMP
- **Stream**: $STREAM
- **Summary**: $SUMMARY
- **Status**: ISSUED
EOF

# Count entries and warn if threshold reached
ENTRY_COUNT=$(grep -c "^### DIRECTIVE-" "$STAGING" 2>/dev/null || echo "0")
echo "[Directive] Created $DIRECTIVE_ID: $TITLE ($ENTRY_COUNT entries in staging)"
if [ "$ENTRY_COUNT" -ge 10 ]; then
    echo "[Directive] THRESHOLD REACHED ($ENTRY_COUNT/10). Run compact_wisdom.sh to compact into compendium."
fi
