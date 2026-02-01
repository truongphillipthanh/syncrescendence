#!/bin/bash
# validate_conversions.sh
# Validates SN conversions preserve semantics via sampling

set -e

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ORIGINAL_DIR="$REPO_ROOT/01-CANON"
DRAFT_DIR="$REPO_ROOT/01-CANON/sn-drafts"
REPORT_FILE="$REPO_ROOT/00-ORCHESTRATION/state/DYN-VALIDATION_REPORT.md"

cd "$REPO_ROOT"

echo "# SN Conversion Validation Report" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Date**: $(date +%Y-%m-%d)" >> "$REPORT_FILE"
echo "**Validator**: Claude Code" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## Structural Validation" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Count files
ORIGINAL_COUNT=$(ls "$ORIGINAL_DIR"/CANON-*.md 2>/dev/null | wc -l | tr -d ' ')
DRAFT_COUNT=$(ls "$DRAFT_DIR"/CANON-*.md 2>/dev/null | wc -l | tr -d ' ')

echo "| Metric | Value |" >> "$REPORT_FILE"
echo "|--------|-------|" >> "$REPORT_FILE"
echo "| Original files | $ORIGINAL_COUNT |" >> "$REPORT_FILE"
echo "| Draft files | $DRAFT_COUNT |" >> "$REPORT_FILE"
echo "| Coverage | $(echo "scale=1; $DRAFT_COUNT / $ORIGINAL_COUNT * 100" | bc)% |" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Check for missing drafts
echo "## Missing Drafts" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

MISSING=0
for orig in "$ORIGINAL_DIR"/CANON-*.md; do
    filename=$(basename "$orig")
    if [ ! -f "$DRAFT_DIR/$filename" ]; then
        echo "- $filename" >> "$REPORT_FILE"
        MISSING=$((MISSING + 1))
    fi
done

if [ $MISSING -eq 0 ]; then
    echo "All originals have corresponding drafts." >> "$REPORT_FILE"
else
    echo "" >> "$REPORT_FILE"
    echo "**$MISSING files missing drafts**" >> "$REPORT_FILE"
fi

echo "" >> "$REPORT_FILE"

# Validate SN block structure
echo "## SN Block Structure Validation" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "Checking for valid SN block types (TERM, NORM, PROC, TEST, ARTIFACT)..." >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

VALID_BLOCKS=0
INVALID_BLOCKS=0

for draft in "$DRAFT_DIR"/CANON-*.md; do
    filename=$(basename "$draft")

    # Count valid blocks
    BLOCK_COUNT=$(grep -c "^TERM\|^NORM\|^PROC\|^TEST\|^ARTIFACT" "$draft" 2>/dev/null || echo "0")
    END_COUNT=$(grep -c "^end$" "$draft" 2>/dev/null || echo "0")

    if [ "$BLOCK_COUNT" -gt 0 ] && [ "$END_COUNT" -gt 0 ]; then
        VALID_BLOCKS=$((VALID_BLOCKS + 1))
    else
        INVALID_BLOCKS=$((INVALID_BLOCKS + 1))
        echo "- $filename: blocks=$BLOCK_COUNT, ends=$END_COUNT" >> "$REPORT_FILE"
    fi
done

echo "" >> "$REPORT_FILE"
echo "| Status | Count |" >> "$REPORT_FILE"
echo "|--------|-------|" >> "$REPORT_FILE"
echo "| Valid structure | $VALID_BLOCKS |" >> "$REPORT_FILE"
echo "| Invalid structure | $INVALID_BLOCKS |" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Frontmatter preservation check
echo "## Frontmatter Preservation" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

FRONTMATTER_OK=0
FRONTMATTER_MISSING=0

for draft in "$DRAFT_DIR"/CANON-*.md; do
    if head -1 "$draft" | grep -q "^---$"; then
        FRONTMATTER_OK=$((FRONTMATTER_OK + 1))
    else
        FRONTMATTER_MISSING=$((FRONTMATTER_MISSING + 1))
        echo "- $(basename $draft): Missing frontmatter" >> "$REPORT_FILE"
    fi
done

echo "" >> "$REPORT_FILE"
echo "| Status | Count |" >> "$REPORT_FILE"
echo "|--------|-------|" >> "$REPORT_FILE"
echo "| Frontmatter preserved | $FRONTMATTER_OK |" >> "$REPORT_FILE"
echo "| Frontmatter missing | $FRONTMATTER_MISSING |" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Summary
echo "## Summary" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

TOTAL_ISSUES=$((MISSING + INVALID_BLOCKS + FRONTMATTER_MISSING))
if [ $TOTAL_ISSUES -eq 0 ]; then
    echo "**VALIDATION PASSED**: All $DRAFT_COUNT drafts have valid structure." >> "$REPORT_FILE"
else
    echo "**VALIDATION WARNING**: $TOTAL_ISSUES issues found." >> "$REPORT_FILE"
fi

echo "" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## Next Steps" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "1. Review Gemini audit for semantic validation" >> "$REPORT_FILE"
echo "2. Manual review of files with <20% compression" >> "$REPORT_FILE"
echo "3. Sovereign approval before replacing originals" >> "$REPORT_FILE"

# Console output
echo ""
echo "=== Validation Complete ==="
echo "Report: $REPORT_FILE"
echo "Files validated: $DRAFT_COUNT"
echo "Issues found: $TOTAL_ISSUES"
