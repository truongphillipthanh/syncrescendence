#!/bin/zsh
# cleanup_root.sh
# Enforce root cleanliness by relocating pollution files

set -e

echo "=== Root Cleanup Script ==="
echo ""

# Define acceptable root files
ACCEPTABLE=(
    "CLAUDE.md"
    "Makefile"
    "README.md"
    ".gitignore"
)

# Find .md files at root
echo "Scanning root for .md files..."
ROOT_MD=$(ls *.md 2>/dev/null || true)

for file in $ROOT_MD; do
    # Skip acceptable files
    if [[ " ${ACCEPTABLE[@]} " =~ " ${file} " ]]; then
        echo "  ✓ $file (acceptable)"
        continue
    fi

    echo "  ⚠ Found pollution: $file"

    # Determine disposition based on filename pattern
    if [[ "$file" == DIRECTIVE-* ]]; then
        echo "    → Moving to 00-ORCHESTRATION/directives/"
        mv "$file" 00-ORCHESTRATION/directives/
    elif [[ "$file" == ORACLE*CONTEXT* || "$file" == ORACLE*_INIT* ]]; then
        echo "    → Moving to 00-ORCHESTRATION/oracle_contexts/"
        mv "$file" 00-ORCHESTRATION/oracle_contexts/
    elif [[ "$file" == EXECUTION_LOG-* ]]; then
        echo "    → Moving to 00-ORCHESTRATION/execution_logs/"
        mv "$file" 00-ORCHESTRATION/execution_logs/
    elif [[ "$file" == *research* || "$file" == *optimization* || "$file" == *analysis* || "$file" == *architecture* ]]; then
        # Research artifacts get dated prefix
        DATE=$(date +%Y%m%d)
        SLUG=$(echo "$file" | sed 's/.md$//' | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
        NEWNAME="RESEARCH-${DATE}-${SLUG}.md"
        echo "    → Archiving as 05-MEMORY/$NEWNAME"
        mv "$file" "05-MEMORY/$NEWNAME"
    else
        echo "    → Default: Archiving to 05-MEMORY/"
        mv "$file" 05-MEMORY/
    fi
done

echo ""
echo "=== Cleanup Complete ==="

# Verify
echo ""
echo "Root .md files remaining:"
ls *.md 2>/dev/null || echo "  (none except acceptable)"
