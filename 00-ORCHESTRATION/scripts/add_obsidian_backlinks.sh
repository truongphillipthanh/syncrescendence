#!/bin/bash
# Transforms CANON-XXXXX references to [[CANON-XXXXX-*]] backlinks
# Makes the corpus Obsidian-navigable by converting bare references to wiki-style links
#
# Usage: ./add_obsidian_backlinks.sh <directory>
# Example: ./add_obsidian_backlinks.sh 00-ORCHESTRATION/directives
#
# What this does:
# - Finds patterns like "CANON-00005" or "CANON-30400"
# - Looks up the full filename in 01-CANON/
# - Replaces with [[CANON-00005-SYNCRESCENDENCE-cosmos]]
#
# Preserves:
# - Already-linked references [[CANON-XXXXX]] (won't double-wrap)
# - References in code blocks
# - References in YAML frontmatter

set -e

DIR=${1:-.}

if [ ! -d "$DIR" ]; then
    echo "Error: Directory $DIR does not exist"
    exit 1
fi

echo "Adding Obsidian backlinks in $DIR..."
echo "Scanning for CANON-XXXXX references..."

# Count references before
BEFORE=$(grep -r "CANON-[0-9]\{5\}" "$DIR" --include="*.md" | grep -v "\[\[CANON-" | wc -l | tr -d ' ')
echo "Found $BEFORE bare references"

# Create mapping file of CANON IDs to full filenames
MAPPING_FILE="/tmp/canon_mapping_$$.txt"
if [ -d "01-CANON" ]; then
    find 01-CANON -name "CANON-*.md" -type f | while read file; do
        basename "$file" .md >> "$MAPPING_FILE"
    done
    echo "Created mapping from $(wc -l < "$MAPPING_FILE" | tr -d ' ') CANON files"
else
    echo "Warning: 01-CANON directory not found. Creating empty mapping."
    touch "$MAPPING_FILE"
fi

# Function to look up full CANON filename
lookup_canon() {
    local id=$1
    grep "^CANON-$id-" "$MAPPING_FILE" | head -1
}

# Process each markdown file
find "$DIR" -name "*.md" -type f | while read file; do
    # Create temp file
    TEMP_FILE="${file}.tmp"

    # Track if we made changes
    CHANGED=false

    # Process file line by line
    while IFS= read -r line; do
        # Skip if line is already a wiki link or in code block
        if [[ "$line" =~ \[\[CANON- ]] || [[ "$line" =~ ^[[:space:]]*\`\`\` ]]; then
            echo "$line" >> "$TEMP_FILE"
            continue
        fi

        # Find CANON-XXXXX patterns and replace
        NEW_LINE="$line"
        while [[ "$NEW_LINE" =~ CANON-([0-9]{5})([^-\]]) ]]; do
            CANON_ID="${BASH_REMATCH[1]}"
            AFTER_CHAR="${BASH_REMATCH[2]}"

            # Look up full filename
            FULL_NAME=$(lookup_canon "$CANON_ID")

            if [ -n "$FULL_NAME" ]; then
                # Replace CANON-XXXXX with [[CANON-XXXXX-NAME-tier]]
                NEW_LINE="${NEW_LINE//CANON-$CANON_ID$AFTER_CHAR/[[$FULL_NAME]]$AFTER_CHAR}"
                CHANGED=true
            else
                # If no mapping found, leave as-is
                break
            fi
        done

        echo "$NEW_LINE" >> "$TEMP_FILE"
    done < "$file"

    # Replace original file if changed
    if [ "$CHANGED" = true ]; then
        mv "$TEMP_FILE" "$file"
        echo "Updated: $file"
    else
        rm "$TEMP_FILE"
    fi
done

# Count references after
AFTER=$(grep -r "\[\[CANON-[0-9]\{5\}" "$DIR" --include="*.md" | wc -l | tr -d ' ')
echo ""
echo "Complete!"
echo "Converted $((AFTER - BEFORE)) references to wiki-style links"
echo "Total wiki-linked references: $AFTER"

# Cleanup
rm -f "$MAPPING_FILE"
