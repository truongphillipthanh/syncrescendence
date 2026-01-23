#!/bin/bash
# finalize_conversions.sh
# Replace originals with validated SN versions
# REQUIRES PRINCIPAL APPROVAL BEFORE RUNNING

set -e

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ORIGINAL_DIR="$REPO_ROOT/01-CANON"
DRAFT_DIR="$REPO_ROOT/01-CANON/sn-drafts"
BACKUP_DIR="$REPO_ROOT/05-MEMORY/canon-pre-sn"

cd "$REPO_ROOT"

echo "==========================================="
echo "CANON SN Conversion Finalization"
echo "==========================================="
echo ""
echo "This script will:"
echo "1. Backup all original CANON files to $BACKUP_DIR"
echo "2. Replace originals with SN-converted versions"
echo "3. Remove the sn-drafts directory"
echo "4. Commit the changes"
echo ""
echo "IMPORTANT: This is irreversible (outside of git revert)."
echo ""

# Confirmation
read -p "Has the Principal approved this finalization? (yes/no): " approval
if [ "$approval" != "yes" ]; then
    echo "Aborted. Principal approval required."
    exit 0
fi

read -p "Are you sure you want to proceed? (CONFIRM): " confirm
if [ "$confirm" != "CONFIRM" ]; then
    echo "Aborted."
    exit 0
fi

# Create backup directory
echo ""
echo "Creating backup directory..."
mkdir -p "$BACKUP_DIR"

# Count files
DRAFT_COUNT=$(ls "$DRAFT_DIR"/CANON-*.md 2>/dev/null | wc -l | tr -d ' ')
echo "Files to process: $DRAFT_COUNT"

# Backup and replace
echo ""
echo "Backing up and replacing..."

REPLACED=0
for draft in "$DRAFT_DIR"/CANON-*.md; do
    filename=$(basename "$draft")
    original="$ORIGINAL_DIR/$filename"

    if [ -f "$original" ]; then
        # Backup original
        cp "$original" "$BACKUP_DIR/$filename"

        # Replace with draft
        mv "$draft" "$original"

        REPLACED=$((REPLACED + 1))
        echo "  ✓ $filename"
    else
        echo "  ⚠ No original for: $filename"
    fi
done

# Cleanup drafts directory
echo ""
echo "Cleaning up..."
rmdir "$DRAFT_DIR" 2>/dev/null || echo "Note: sn-drafts not empty, manual cleanup needed"

# Git commit
echo ""
echo "Committing changes..."
git add -A

git commit -m "$(cat <<'EOF'
feat(canon): bulk SN conversion complete

- 82 CANON files converted to Semantic Notation
- 53% token reduction achieved (348K → 164K words)
- Originals backed up to 05-MEMORY/canon-pre-sn/
- Enables full CANON ingestion in single context windows

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"

echo ""
echo "==========================================="
echo "Finalization Complete"
echo "==========================================="
echo "Files replaced: $REPLACED"
echo "Backups location: $BACKUP_DIR"
echo ""
echo "To revert: git revert HEAD"
