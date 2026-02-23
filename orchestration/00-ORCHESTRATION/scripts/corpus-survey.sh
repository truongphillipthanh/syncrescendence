#!/bin/bash
# corpus-survey.sh - Gemini CLI wrapper for corpus analysis
# Usage: ./corpus-survey.sh [output-dir]
#
# This script facilitates Gemini's analysis of the repository corpus
# using the GEMINI-CORPUS-SENSING-PROMPT.md structured prompt.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
OUTPUT_DIR="${1:--OUTGOING/$(date +%Y%m%d)-corpus-survey}"
PROMPT_FILE="orchestration/scripts/GEMINI-CORPUS-SENSING-PROMPT.md"

cd "$REPO_ROOT"
mkdir -p -- "$OUTPUT_DIR"

echo "=== CORPUS SURVEY ==="
echo "Repository: $(basename "$REPO_ROOT")"
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Generate file inventory
echo "Generating file inventory..."
find . -type f \( -name "*.md" -o -name "*.txt" -o -name "*.csv" -o -name "*.yaml" -o -name "*.json" \) \
  ! -path "./.git/*" ! -path "./node_modules/*" \
  -exec wc -c {} \; 2>/dev/null | sort -rn > "$OUTPUT_DIR/file_inventory.txt"

echo "File inventory generated: $OUTPUT_DIR/file_inventory.txt"
echo ""

# Count key metrics
echo "=== METRICS ==="
echo "CANON files: $(find "$REPO_ROOT/canon" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')"
echo "Source files: $(find "$REPO_ROOT/sources" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')"
echo "State files: $(find "$REPO_ROOT/orchestration/state" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo "-INBOX files: $(find "$REPO_ROOT/-INBOX" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo ""

# If gemini CLI is available, run full analysis
if command -v gemini &> /dev/null; then
    echo "=== RUNNING GEMINI SENSING SWEEP ==="
    echo "Using prompt: $PROMPT_FILE"
    echo ""
    gemini -p "$(cat "$PROMPT_FILE")" > "$OUTPUT_DIR/SENSING_REPORT.md"
    echo "Report generated: $OUTPUT_DIR/SENSING_REPORT.md"
else
    echo "Note: Gemini CLI not installed."
    echo ""
    echo "To run Gemini analysis manually:"
    echo "  1. Install: pip install google-generativeai"
    echo "  2. Run: gemini -p \"\$(cat $PROMPT_FILE)\" > \"$OUTPUT_DIR/SENSING_REPORT.md\""
    echo ""
    echo "For now, use the file inventory for manual analysis."
fi

echo ""
echo "=== SURVEY COMPLETE ==="
