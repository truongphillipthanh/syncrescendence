#!/usr/bin/env bash
# Transforms CANON-XXXXX references to [[CANON-XXXXX-*]] backlinks
# Makes the corpus Obsidian-navigable by converting bare references to wiki-style links
#
# Usage: ./add_obsidian_backlinks.sh <directory>
# Example: ./add_obsidian_backlinks.sh 00-ORCHESTRATION/directives

set -e

DIR=${1:-.}

if [ ! -d "$DIR" ]; then
    echo "Error: Directory $DIR does not exist"
    exit 1
fi

echo "Adding Obsidian backlinks in $DIR..."

# Create a mapping file
MAPPING_FILE="/tmp/canon_mapping_$$.txt"
> "$MAPPING_FILE"

# Build mapping of CANON IDs to full filenames
for file in 01-CANON/CANON-*.md; do
    if [[ -f "$file" ]]; then
        basename=$(basename "$file" .md)
        # Extract the 5-digit ID
        id=$(echo "$basename" | grep -oE "[0-9]{5}")
        if [[ -n "$id" ]]; then
            echo "$id $basename" >> "$MAPPING_FILE"
        fi
    fi
done

echo "Loaded $(wc -l < "$MAPPING_FILE" | tr -d ' ') CANON files into lookup"

# Count before
BEFORE=$(grep -r "CANON-[0-9]\{5\}" "$DIR" --include="*.md" 2>/dev/null | grep -v "\[\[CANON-" | wc -l | tr -d ' ')
echo "Found $BEFORE bare references"

# Process files using sed with the mapping
UPDATED=0
find "$DIR" -name "*.md" -type f ! -path "./.git/*" ! -path "./01-CANON/sn-drafts/*" -print0 | while IFS= read -r -d '' file; do
    changed=false

    # For each mapping, create a sed replacement
    while read -r id fullname; do
        # Check if this file has bare references to this ID
        if grep -q "CANON-$id[^0-9-]" "$file" 2>/dev/null || grep -q "CANON-$id$" "$file" 2>/dev/null; then
            # Skip if already linked
            if ! grep -q "\[\[CANON-$id" "$file" 2>/dev/null; then
                # Replace CANON-XXXXX with [[fullname]]
                # Match CANON-XXXXX followed by non-digit, non-hyphen, or end of line
                sed -i '' -E "s/CANON-$id([^0-9-]|$)/[[$fullname]]\1/g" "$file"
                changed=true
            fi
        fi
    done < "$MAPPING_FILE"

    if [[ "$changed" == true ]]; then
        echo "Updated: $file"
        UPDATED=$((UPDATED + 1))
    fi
done

# Count after
AFTER=$(grep -r "\[\[CANON-[0-9]\{5\}" "$DIR" --include="*.md" 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "Complete!"
echo "Wiki-linked references: $AFTER"

# Cleanup
rm -f "$MAPPING_FILE"
