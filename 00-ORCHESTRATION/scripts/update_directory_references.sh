#!/bin/bash
# Update all references to renamed directories
# 02-ENGINE → 02-ENGINE
# 05-MEMORY → 05-MEMORY

set -euo pipefail

echo "Updating directory references..."

# Find all files and update references
find . -type f \( -name "*.md" -o -name "*.yaml" -o -name "*.py" -o -name "*.sh" \) ! -path "./.git/*" -print0 | while IFS= read -r -d '' file; do
    # Skip binary files
    if file "$file" | grep -q text; then
        # Update 02-ENGINE → 02-ENGINE
        sed -i '' 's|02-ENGINE|02-ENGINE|g' "$file" 2>/dev/null || true

        # Update 05-MEMORY → 05-MEMORY
        sed -i '' 's|05-MEMORY|05-MEMORY|g' "$file" 2>/dev/null || true
    fi
done

echo "✓ Directory references updated"

# Verify no orphaned references remain
echo ""
echo "Verifying no orphaned references..."

OPERATIONAL_COUNT=$(find . -type f \( -name "*.md" -o -name "*.yaml" -o -name "*.py" -o -name "*.sh" \) ! -path "./.git/*" -exec grep -l "02-ENGINE" {} \; 2>/dev/null | wc -l | tr -d ' ')
ARCHIVE_COUNT=$(find . -type f \( -name "*.md" -o -name "*.yaml" -o -name "*.py" -o -name "*.sh" \) ! -path "./.git/*" -exec grep -l "05-MEMORY" {} \; 2>/dev/null | wc -l | tr -d ' ')

if [ "$OPERATIONAL_COUNT" -eq 0 ] && [ "$ARCHIVE_COUNT" -eq 0 ]; then
    echo "✓ No orphaned references found"
else
    echo "⚠️  Found $OPERATIONAL_COUNT files with '02-ENGINE' and $ARCHIVE_COUNT files with '05-MEMORY'"
    exit 1
fi

echo ""
echo "Directory rename complete!"
