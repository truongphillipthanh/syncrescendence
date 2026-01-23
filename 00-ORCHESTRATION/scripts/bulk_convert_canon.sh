#!/bin/bash
# bulk_convert_canon.sh
# Converts all CANON files to SN format

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SCRIPT="$REPO_ROOT/00-ORCHESTRATION/scripts/convert_canon.py"
INPUT_DIR="$REPO_ROOT/01-CANON"
OUTPUT_DIR="$REPO_ROOT/01-CANON/sn-drafts"
METRICS_FILE="$REPO_ROOT/00-ORCHESTRATION/state/DYN-CANON_CONVERSION_METRICS.csv"

cd "$REPO_ROOT"

# Initialize metrics
echo "file,original_words,converted_words,compression_pct,status" > "$METRICS_FILE"

# Counters
success_count=0
error_count=0
total_orig=0
total_conv=0

# Process each CANON file
for file in "$INPUT_DIR"/CANON-*.md; do
    filename=$(basename "$file")

    # Skip if already in sn-drafts
    if [[ "$file" == *"/sn-drafts/"* ]]; then
        continue
    fi

    echo "Converting: $filename"

    # Get original word count
    orig_words=$(wc -w < "$file" | tr -d ' ')
    total_orig=$((total_orig + orig_words))

    # Convert
    if python3 "$SCRIPT" "$file" "$OUTPUT_DIR/$filename" 2>/dev/null; then
        # Get converted word count
        conv_words=$(wc -w < "$OUTPUT_DIR/$filename" | tr -d ' ')
        total_conv=$((total_conv + conv_words))

        # Calculate compression
        if [ "$orig_words" -gt 0 ]; then
            compression=$(echo "scale=1; (1 - $conv_words / $orig_words) * 100" | bc)
        else
            compression="0.0"
        fi

        echo "$filename,$orig_words,$conv_words,$compression,success" >> "$METRICS_FILE"
        echo "  ✓ $orig_words → $conv_words words ($compression% reduction)"
        success_count=$((success_count + 1))
    else
        echo "$filename,$orig_words,0,0,error" >> "$METRICS_FILE"
        echo "  ✗ Conversion failed"
        error_count=$((error_count + 1))
    fi
done

# Summary
echo ""
echo "=== Conversion Summary ==="
echo "Files processed: $((success_count + error_count))"
echo "Successful: $success_count"
echo "Errors: $error_count"
echo "Original total: $total_orig words"
echo "Converted total: $total_conv words"
if [ "$total_orig" -gt 0 ]; then
    overall=$(echo "scale=1; (1 - $total_conv / $total_orig) * 100" | bc)
    echo "Overall compression: $overall%"
fi
