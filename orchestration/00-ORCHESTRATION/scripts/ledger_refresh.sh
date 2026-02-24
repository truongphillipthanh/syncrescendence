#!/bin/bash
# ledger_refresh.sh — DC-134 Live Ledger Sensing Automation
# Scans all DYN-LEDGER-*.md files, flags stale ones, checks MODEL-INDEX drift.
# Designed for launchd (no ~/.zshrc dependency).
#
# Usage:
#   ./ledger_refresh.sh                  # Report only (stdout JSON)
#   ./ledger_refresh.sh --auto-timestamp # Also update "Last Updated" on files touched today
#   ./ledger_refresh.sh --report-md      # Output markdown instead of JSON
#
# Exit codes: 0 = all fresh, 1 = stale ledgers found, 2 = error

set -euo pipefail

# --- Configuration (launchd-safe, no ~/.zshrc) ---
REPO_ROOT="${SYNCRESCENDENCE_REPO_ROOT:-/Users/system/syncrescendence}"
ENGINE_DIR="$REPO_ROOT/engine/02-ENGINE"
REPORT_DIR="$REPO_ROOT/orchestration/state"
STALE_THRESHOLD_DAYS=7
TODAY=$(date +%Y-%m-%d)
NOW_ISO=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# --- Frontier Registry (ground truth from CLAUDE.md / MEMORY.md) ---
# Format: "Platform|FlagshipModel|ExpectedVersion"
FRONTIER_REGISTRY=(
    "Anthropic|Claude Opus 4.6|claude-opus-4-6"
    "OpenAI|GPT-5.3-codex|gpt-5.3-codex"
    "Google|Gemini Pro 3.1|Gemini 3"
    "xAI|Grok 4|Grok 4"
    "Meta|Llama 4 Maverick|Llama 4"
    "Mistral|Mistral Large 3|Mistral Large 3"
    "DeepSeek|V3.2|V3.2"
    "Alibaba|Qwen-3-Max|Qwen-3"
)

# --- Parse flags ---
AUTO_TIMESTAMP=false
REPORT_MD=false
for arg in "$@"; do
    case "$arg" in
        --auto-timestamp) AUTO_TIMESTAMP=true ;;
        --report-md)      REPORT_MD=true ;;
        --help|-h)
            sed -n '2,9p' "$0"
            exit 0
            ;;
    esac
done

# --- Helper: days since a YYYY-MM-DD date ---
days_since() {
    local target_epoch
    local now_epoch
    # macOS date
    if date -j -f "%Y-%m-%d" "$1" "+%s" &>/dev/null; then
        target_epoch=$(date -j -f "%Y-%m-%d" "$1" "+%s")
        now_epoch=$(date "+%s")
    else
        # GNU date fallback
        target_epoch=$(date -d "$1" "+%s")
        now_epoch=$(date "+%s")
    fi
    echo $(( (now_epoch - target_epoch) / 86400 ))
}

# --- Collect ledger files (bash 3 compatible) ---
LEDGER_FILES=()
while IFS= read -r line; do
    LEDGER_FILES+=("$line")
done < <(find "$ENGINE_DIR" -name 'DYN-LEDGER-*.md' | sort)
MODEL_INDEX="$ENGINE_DIR/MODEL-INDEX.md"

# --- Scan each ledger ---
STALE_LEDGERS=()
FRESH_LEDGERS=()
JSON_ENTRIES=()

for f in "${LEDGER_FILES[@]}"; do
    basename=$(basename "$f")
    # Extract Last Updated date (first match)
    last_updated=$(grep -m1 '^\*\*Last Updated\*\*' "$f" 2>/dev/null | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' || echo "UNKNOWN")
    # Extract cadence
    cadence=$(grep -m1 '^\*\*Cadence\*\*' "$f" 2>/dev/null | sed 's/.*: *//' || echo "unknown")

    if [ "$last_updated" = "UNKNOWN" ]; then
        age_days=-1
        status="UNKNOWN"
        STALE_LEDGERS+=("$basename")
    else
        age_days=$(days_since "$last_updated")
        if [ "$age_days" -gt "$STALE_THRESHOLD_DAYS" ]; then
            status="STALE"
            STALE_LEDGERS+=("$basename")
        else
            status="FRESH"
            FRESH_LEDGERS+=("$basename")
        fi
    fi

    JSON_ENTRIES+=("{\"file\":\"$basename\",\"last_updated\":\"$last_updated\",\"age_days\":$age_days,\"cadence\":\"$cadence\",\"status\":\"$status\"}")

    # Auto-timestamp: if file was modified today (git or filesystem) and flag is set
    if $AUTO_TIMESTAMP && [ "$status" != "FRESH" ]; then
        # Check if file was modified today via filesystem mtime
        file_mdate=$(date -r "$f" +%Y-%m-%d 2>/dev/null || stat -c %y "$f" 2>/dev/null | cut -d' ' -f1)
        if [ "$file_mdate" = "$TODAY" ]; then
            # Update the Last Updated line
            if grep -q '^\*\*Last Updated\*\*' "$f"; then
                sed -i '' "s/^\*\*Last Updated\*\*: [0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/**Last Updated**: $TODAY/" "$f" 2>/dev/null || \
                sed -i "s/^\*\*Last Updated\*\*: [0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/**Last Updated**: $TODAY/" "$f"
            fi
        fi
    fi
done

# --- MODEL-INDEX drift check ---
MODEL_INDEX_DRIFTS=()
if [ -f "$MODEL_INDEX" ]; then
    mi_last_updated=$(grep -m1 '^\*\*Last Updated\*\*\|^\*\*Last Verified\*\*' "$MODEL_INDEX" 2>/dev/null | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' || echo "UNKNOWN")
    mi_age=-1
    if [ "$mi_last_updated" != "UNKNOWN" ]; then
        mi_age=$(days_since "$mi_last_updated")
    fi

    for entry in "${FRONTIER_REGISTRY[@]}"; do
        IFS='|' read -r platform flagship check_string <<< "$entry"
        # Check if the model index mentions this check_string
        if ! grep -qi "$check_string" "$MODEL_INDEX" 2>/dev/null; then
            MODEL_INDEX_DRIFTS+=("{\"platform\":\"$platform\",\"expected\":\"$flagship\",\"issue\":\"not_found_in_index\"}")
        fi
    done
fi

# --- Build report ---
stale_count=${#STALE_LEDGERS[@]}
fresh_count=${#FRESH_LEDGERS[@]}
drift_count=${#MODEL_INDEX_DRIFTS[@]}

if $REPORT_MD; then
    # Markdown output
    echo "# Ledger Refresh Report"
    echo "**Generated**: $NOW_ISO"
    echo "**Stale threshold**: ${STALE_THRESHOLD_DAYS} days"
    echo ""
    echo "## Summary"
    echo "- Total ledgers: ${#LEDGER_FILES[@]}"
    echo "- Fresh: $fresh_count"
    echo "- Stale/Unknown: $stale_count"
    echo "- MODEL-INDEX drifts: $drift_count"
    echo "- MODEL-INDEX last verified: ${mi_last_updated:-N/A} (${mi_age:-?} days ago)"
    echo ""
    echo "## Ledger Status"
    echo ""
    echo "| File | Last Updated | Age (days) | Cadence | Status |"
    echo "|------|-------------|------------|---------|--------|"
    for entry in "${JSON_ENTRIES[@]}"; do
        # Parse JSON-ish entry with parameter expansion
        file=$(echo "$entry" | grep -o '"file":"[^"]*"' | cut -d'"' -f4)
        lu=$(echo "$entry" | grep -o '"last_updated":"[^"]*"' | cut -d'"' -f4)
        age=$(echo "$entry" | grep -o '"age_days":[0-9-]*' | cut -d: -f2)
        cad=$(echo "$entry" | grep -o '"cadence":"[^"]*"' | cut -d'"' -f4)
        st=$(echo "$entry" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
        echo "| $file | $lu | $age | $cad | $st |"
    done
    echo ""
    if [ "$drift_count" -gt 0 ]; then
        echo "## MODEL-INDEX Drift Warnings"
        echo ""
        for d in "${MODEL_INDEX_DRIFTS[@]}"; do
            platform=$(echo "$d" | grep -o '"platform":"[^"]*"' | cut -d'"' -f4)
            expected=$(echo "$d" | grep -o '"expected":"[^"]*"' | cut -d'"' -f4)
            echo "- **$platform**: Expected \"$expected\" not found in MODEL-INDEX.md"
        done
    fi
else
    # JSON output
    entries_json=$(IFS=,; echo "${JSON_ENTRIES[*]}")
    drifts_json=""
    if [ "$drift_count" -gt 0 ]; then
        drifts_json=$(IFS=,; echo "${MODEL_INDEX_DRIFTS[*]}")
    fi
    cat <<ENDJSON
{
  "generated": "$NOW_ISO",
  "stale_threshold_days": $STALE_THRESHOLD_DAYS,
  "total_ledgers": ${#LEDGER_FILES[@]},
  "fresh_count": $fresh_count,
  "stale_count": $stale_count,
  "model_index_last_verified": "${mi_last_updated:-UNKNOWN}",
  "model_index_age_days": ${mi_age:--1},
  "model_index_drift_count": $drift_count,
  "ledgers": [$entries_json],
  "model_index_drifts": [$drifts_json]
}
ENDJSON
fi

# Exit code signals staleness
if [ "$stale_count" -gt 0 ] || [ "$drift_count" -gt 0 ]; then
    exit 1
fi
exit 0
