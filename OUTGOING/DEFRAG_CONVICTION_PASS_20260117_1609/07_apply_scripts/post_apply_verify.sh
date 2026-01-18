#!/bin/bash
# POST-APPLY VERIFICATION SCRIPT
# Generated: 2026-01-17T16:09:00Z
#
# PURPOSE: Verify defrag operations succeeded
# USAGE: Run after defrag_apply.sh completes

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
PASS_COUNT=0
FAIL_COUNT=0

# -----------------------------------------------------------------------------
# TEST FUNCTIONS
# -----------------------------------------------------------------------------
test_pass() {
    echo "  PASS: $1"
    ((PASS_COUNT++))
}

test_fail() {
    echo "  FAIL: $1"
    ((FAIL_COUNT++))
}

test_check() {
    local DESCRIPTION="$1"
    local COMMAND="$2"

    if eval "$COMMAND" >/dev/null 2>&1; then
        test_pass "$DESCRIPTION"
    else
        test_fail "$DESCRIPTION"
    fi
}

# -----------------------------------------------------------------------------
# VERIFICATION TESTS
# -----------------------------------------------------------------------------
run_tests() {
    echo "=========================================="
    echo "POST-APPLY VERIFICATION"
    echo "=========================================="
    echo ""

    cd "$REPO_ROOT"

    # --- Test Group 1: Detritus Removal ---
    echo "[1] Detritus Removal"

    DS_COUNT=$(find . -name ".DS_Store" 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$DS_COUNT" -eq 0 ]]; then
        test_pass "No .DS_Store files"
    else
        test_fail "Found $DS_COUNT .DS_Store files"
    fi

    if [[ ! -d ".tmp.driveupload" ]]; then
        test_pass "No .tmp.driveupload directory"
    else
        test_fail ".tmp.driveupload still exists"
    fi

    echo ""

    # --- Test Group 2: Oracle Contexts ---
    echo "[2] Oracle Context Consolidation"

    if [[ ! -f "ORACLE13_CONTEXT.md" ]]; then
        test_pass "ORACLE13_CONTEXT.md not at root"
    else
        test_fail "ORACLE13_CONTEXT.md still at root"
    fi

    if [[ -f "00-ORCHESTRATION/oracle_contexts/ORACLE13_CONTEXT.md" ]] || \
       [[ ! -f "ORACLE13_CONTEXT.md" ]]; then
        test_pass "Oracle contexts in proper location (or already handled)"
    else
        test_fail "Oracle contexts not properly relocated"
    fi

    echo ""

    # --- Test Group 3: Research Relocation ---
    echo "[3] Research Artifact Relocation"

    RESEARCH_AT_ROOT=$(ls -1 "${REPO_ROOT}/"DEEP_RESEARCH_PROMPT-*.md 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$RESEARCH_AT_ROOT" -eq 0 ]]; then
        test_pass "No DEEP_RESEARCH_PROMPT-*.md at root"
    else
        test_fail "Found $RESEARCH_AT_ROOT research prompts at root"
    fi

    for DIR in agents claudecode clitool codex cowork promptengineering; do
        if [[ ! -d "${REPO_ROOT}/${DIR}" ]]; then
            test_pass "Research dir $DIR not at root"
        else
            test_fail "Research dir $DIR still at root"
        fi
    done

    echo ""

    # --- Test Group 4: Archive Existence ---
    echo "[4] Archive Verification"

    if [[ -d "05-ARCHIVE" ]]; then
        test_pass "05-ARCHIVE directory exists"
    else
        test_fail "05-ARCHIVE directory missing"
    fi

    ARCH_COUNT=$(ls -1 05-ARCHIVE/ARCH-*.md 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$ARCH_COUNT" -gt 0 ]]; then
        test_pass "Found $ARCH_COUNT archived files"
    else
        test_fail "No archived files found"
    fi

    echo ""

    # --- Test Group 5: Root Cleanliness ---
    echo "[5] Root Cleanliness"

    # Check for expected files only
    UNEXPECTED=$(ls -1 *.md 2>/dev/null | grep -v -E '^(CLAUDE\.md|COCKPIT\.md)$' | wc -l | tr -d ' ')
    if [[ "$UNEXPECTED" -lt 5 ]]; then
        test_pass "Root relatively clean (${UNEXPECTED} unexpected .md files)"
    else
        test_fail "Root has $UNEXPECTED unexpected .md files"
        echo "    Unexpected files:"
        ls -1 *.md 2>/dev/null | grep -v -E '^(CLAUDE\.md|COCKPIT\.md)$' | head -10 | sed 's/^/      /'
    fi

    echo ""

    # --- Test Group 6: Canon Location ---
    echo "[6] Canon Verification"

    if [[ ! -f "CANON-31150-PLATFORM_CAPABILITY_CATALOG.md" ]]; then
        test_pass "No CANON file at root"
    else
        test_fail "CANON file still at root"
    fi

    CANON_COUNT=$(ls -1 01-CANON/CANON-*.md 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$CANON_COUNT" -gt 50 ]]; then
        test_pass "01-CANON/ contains $CANON_COUNT CANON files"
    else
        test_fail "01-CANON/ only contains $CANON_COUNT files (expected 50+)"
    fi

    echo ""

    # --- Test Group 7: Git Status ---
    echo "[7] Git Status"

    UNCOMMITTED=$(git status --porcelain | wc -l | tr -d ' ')
    if [[ "$UNCOMMITTED" -eq 0 ]]; then
        test_pass "No uncommitted changes"
    else
        test_fail "Found $UNCOMMITTED uncommitted changes"
        git status --short | head -10 | sed 's/^/      /'
    fi

    echo ""
}

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
print_summary() {
    echo "=========================================="
    echo "VERIFICATION SUMMARY"
    echo "=========================================="
    echo ""
    echo "  Passed: $PASS_COUNT"
    echo "  Failed: $FAIL_COUNT"
    echo ""

    if [[ "$FAIL_COUNT" -eq 0 ]]; then
        echo "STATUS: ALL TESTS PASSED"
        echo ""
        echo "Defrag apply verified successfully."
        exit 0
    else
        echo "STATUS: SOME TESTS FAILED"
        echo ""
        echo "Review failures above. Consider:"
        echo "  - Running defrag_apply.sh again"
        echo "  - Manual intervention for specific files"
        echo "  - Running defrag_rollback.sh if needed"
        exit 1
    fi
}

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
main() {
    run_tests
    print_summary
}

main "$@"
