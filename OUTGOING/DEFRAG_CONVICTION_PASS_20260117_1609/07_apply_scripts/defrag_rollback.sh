#!/bin/bash
# DEFRAG ROLLBACK SCRIPT
# Generated: 2026-01-17T16:09:00Z
#
# PURPOSE: Reverse defrag operations if something went wrong
# METHOD: Git-based rollback (relies on defrag_apply.sh using git mv)

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"

# -----------------------------------------------------------------------------
# SAFETY CHECK
# -----------------------------------------------------------------------------
safety_check() {
    echo "=========================================="
    echo "DEFRAG ROLLBACK"
    echo "=========================================="
    echo ""
    echo "This will attempt to reverse the defrag apply."
    echo ""
    echo "Current HEAD: $(git rev-parse HEAD)"
    echo "Current branch: $(git branch --show-current)"
    echo ""

    # Show last few commits
    echo "Recent commits:"
    git log --oneline -5
    echo ""

    read -p "Continue with rollback? (yes/no): " CONFIRM
    if [[ "$CONFIRM" != "yes" ]]; then
        echo "Rollback cancelled."
        exit 0
    fi
}

# -----------------------------------------------------------------------------
# OPTION 1: FULL RESET (Undo entire defrag commit)
# -----------------------------------------------------------------------------
full_reset() {
    echo ""
    echo "OPTION 1: Full reset to pre-defrag state"
    echo ""

    # Find the defrag commit
    local DEFRAG_COMMIT=$(git log --oneline --grep="chore(defrag)" -1 --format="%H")

    if [[ -z "$DEFRAG_COMMIT" ]]; then
        echo "ERROR: Cannot find defrag commit"
        echo "Try manual rollback with: git log --oneline"
        exit 1
    fi

    echo "Found defrag commit: $DEFRAG_COMMIT"
    echo "Will reset to: ${DEFRAG_COMMIT}^"
    echo ""

    read -p "Proceed with full reset? (yes/no): " CONFIRM
    if [[ "$CONFIRM" != "yes" ]]; then
        echo "Full reset cancelled."
        return
    fi

    git reset --hard "${DEFRAG_COMMIT}^"
    echo "Reset complete. Current HEAD: $(git rev-parse HEAD)"
}

# -----------------------------------------------------------------------------
# OPTION 2: SELECTIVE RESTORE (Restore specific files)
# -----------------------------------------------------------------------------
selective_restore() {
    echo ""
    echo "OPTION 2: Selective file restore"
    echo ""
    echo "To restore a specific file from before defrag:"
    echo ""
    echo "  git checkout HEAD~1 -- <filepath>"
    echo ""
    echo "Examples:"
    echo "  git checkout HEAD~1 -- frontier_models.md"
    echo "  git checkout HEAD~1 -- ORACLE13_CONTEXT.md"
    echo ""
    echo "To see what files changed in defrag:"
    echo "  git diff --name-only HEAD~1"
    echo ""
}

# -----------------------------------------------------------------------------
# OPTION 3: ARCHIVE EXTRACTION (Restore from 05-ARCHIVE/)
# -----------------------------------------------------------------------------
archive_restore() {
    echo ""
    echo "OPTION 3: Archive extraction"
    echo ""
    echo "Archived files are in 05-ARCHIVE/ with ARCH- prefix."
    echo ""
    echo "To restore to original location:"
    echo "  git mv 05-ARCHIVE/ARCH-filename.md ./filename.md"
    echo ""
    echo "Current archives:"
    ls -la "${REPO_ROOT}/05-ARCHIVE/ARCH-"*.md 2>/dev/null || echo "  (none found)"
    echo ""
}

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
main() {
    cd "$REPO_ROOT"

    safety_check

    echo ""
    echo "Rollback options:"
    echo "  1) Full reset (undo entire defrag commit)"
    echo "  2) Selective restore (restore specific files)"
    echo "  3) Archive extraction (restore from 05-ARCHIVE/)"
    echo "  4) Cancel"
    echo ""

    read -p "Select option (1-4): " OPTION

    case "$OPTION" in
        1) full_reset ;;
        2) selective_restore ;;
        3) archive_restore ;;
        4) echo "Cancelled." ;;
        *) echo "Invalid option" ;;
    esac
}

main "$@"
