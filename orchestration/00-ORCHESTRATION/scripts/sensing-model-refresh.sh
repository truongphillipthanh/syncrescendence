#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# sensing-model-refresh.sh - Automated Frontier AI Model Sensing
# Usage: ./sensing-model-refresh.sh
#
# This script scans the web for new AI model releases and updates
# the Syncrescendence MODEL-INDEX.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
PROMPT="Research latest model releases from Anthropic, OpenAI, Google, Meta, Mistral, and Alibaba. Compare against current MODEL-INDEX.md and produce a structured update report with last_verified timestamps."

cd "$REPO_ROOT"

echo "=== FRONTIER MODEL SENSING ==="
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Check for Gemini CLI
if ! command -v gemini &> /dev/null; then
    echo "ERROR: Gemini CLI not found. Required for sensing."
    exit 1
fi

# Run sensing
echo "Executing Gemini sensing sweep..."
REPORT=$(gemini -p "$PROMPT")

# Output to inbox for processing
OUTPUT_FILE="agents/cartographer/inbox/pending/REPORT-MODEL-REFRESH-$(date +%Y%m%d).md"
echo "$REPORT" > "$OUTPUT_FILE"

echo "Sensing report generated: $OUTPUT_FILE"
echo "=== SENSING COMPLETE ==="
