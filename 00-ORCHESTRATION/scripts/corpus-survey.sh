#!/bin/bash
# corpus-survey.sh - Gemini CLI wrapper for corpus analysis
# Usage: ./corpus-survey.sh [query]
#
# This script facilitates Gemini's analysis of the repository corpus
# by providing structured context and query handling.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
QUERY="${1:-Analyze the repository structure and summarize key patterns}"

# Generate context snapshot
echo "=== CORPUS SURVEY ==="
echo "Repository: $(basename "$REPO_ROOT")"
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "Query: $QUERY"
echo ""

# Generate tree for context
echo "=== STRUCTURE ==="
tree -L 2 -I 'node_modules|.git|__pycache__|*.pyc|.DS_Store' "$REPO_ROOT" 2>/dev/null || find "$REPO_ROOT" -maxdepth 2 -type d -not -path '*/\.*' | head -50
echo ""

# Count key metrics
echo "=== METRICS ==="
echo "CANON files: $(find "$REPO_ROOT/01-CANON" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')"
echo "Source files: $(find "$REPO_ROOT/04-SOURCES" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')"
echo "State files: $(find "$REPO_ROOT/00-ORCHESTRATION/state" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo ""

# If gemini CLI is available, pass the query
if command -v gemini &> /dev/null; then
    echo "=== GEMINI ANALYSIS ==="
    echo "$QUERY" | gemini
else
    echo "Note: Gemini CLI not installed. Install with: pip install google-generativeai"
    echo "For now, use the context above to perform manual analysis."
fi
