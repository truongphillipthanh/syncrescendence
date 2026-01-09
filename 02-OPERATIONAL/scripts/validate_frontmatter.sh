#!/bin/bash
# validate_frontmatter.sh - Validate YAML frontmatter across CANON corpus
# Generated: 2025-12-30
# Directive: DIRECTIVE-020

set -e

CANON_DIR="/Users/system/Desktop/syncrescendence/CANON"
GENESIS_DIR="/Users/system/Desktop/syncrescendence/GENESIS"

# Counters
total=0
valid=0
missing_frontmatter=0
missing_fields=0

# Required fields
REQUIRED_FIELDS="id name identity tier type version status created updated"

echo "=== SYNCRESCENDENCE FRONTMATTER VALIDATION ==="
echo "=== Generated: $(date) ==="
echo ""

validate_file() {
    local file="$1"
    local errors=0
    local filename=$(basename "$file")

    ((total++))

    # Check if file has frontmatter (starts with ---)
    if ! head -1 "$file" | grep -q "^---$"; then
        echo "MISSING FRONTMATTER: $filename"
        ((missing_frontmatter++))
        return 1
    fi

    # Extract frontmatter (between first two --- lines)
    frontmatter=$(sed -n '1,/^---$/p' "$file" | tail -n +2 | head -n -1)

    # Check each required field
    for field in $REQUIRED_FIELDS; do
        if ! echo "$frontmatter" | grep -q "^$field:"; then
            echo "MISSING $field: $filename"
            ((errors++))
        fi
    done

    # Validate id format
    id=$(echo "$frontmatter" | grep "^id:" | head -1 | sed 's/id: *//')
    if [[ -n "$id" ]] && ! [[ "$id" =~ ^(CANON|GENESIS|OPERATIONAL|QUEUE|EXEMPLA)-[0-9]{3,5}$ ]]; then
        echo "INVALID ID FORMAT ($id): $filename"
        ((errors++))
    fi

    # Validate version format
    version=$(echo "$frontmatter" | grep "^version:" | head -1 | sed 's/version: *//')
    if [[ -n "$version" ]] && ! [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "INVALID VERSION FORMAT ($version): $filename"
        ((errors++))
    fi

    # Check ID matches filename
    file_id=$(echo "$filename" | grep -oE "CANON-[0-9]{5}" || echo "$filename" | grep -oE "GENESIS-[0-9]{3}" || true)
    if [[ -n "$file_id" ]] && [[ -n "$id" ]] && [[ "$file_id" != "$id" ]]; then
        echo "ID MISMATCH (file: $file_id, frontmatter: $id): $filename"
        ((errors++))
    fi

    if [[ $errors -gt 0 ]]; then
        ((missing_fields++))
        return 1
    else
        ((valid++))
        return 0
    fi
}

echo "--- CANON VALIDATION ---"
for file in "$CANON_DIR"/**/*.md "$CANON_DIR"/*.md; do
    if [[ -f "$file" ]]; then
        validate_file "$file" || true
    fi
done

echo ""
echo "--- GENESIS VALIDATION ---"
for file in "$GENESIS_DIR"/*.md; do
    if [[ -f "$file" ]]; then
        validate_file "$file" || true
    fi
done

echo ""
echo "=== VALIDATION SUMMARY ==="
echo "Total files checked: $total"
echo "Valid (all fields present): $valid"
echo "Missing frontmatter: $missing_frontmatter"
echo "Missing required fields: $missing_fields"
echo ""

if [[ $missing_frontmatter -eq 0 ]] && [[ $missing_fields -eq 0 ]]; then
    echo "STATUS: ALL PASS"
    exit 0
else
    echo "STATUS: ISSUES FOUND"
    exit 1
fi
