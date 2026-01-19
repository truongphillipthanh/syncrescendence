#!/usr/bin/env bash
# STRUCTURAL VERIFICATION SCRIPT
# Validates constitutional compliance for Syncrescendence repository
#
# Version: 1.0.1
# Created: 2026-01-18
# Authority: STRUCTURAL_STABILIZATION_PASS
#
# Usage: ./structural_verify.sh [--fix]
#   --fix: Attempt to fix violations (where safe)

set -euo pipefail

# Derive repo root portably (Constitutional Rule #11)
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "ERROR: Not in a git repository"
    exit 1
}

cd "$REPO_ROOT"

# Configuration
REPORT_FILE="$REPO_ROOT/00-ORCHESTRATION/state/DYN-STRUCTURAL_VERIFY_REPORT.md"
FIX_MODE=false
ERRORS=0
WARNINGS=0

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --fix) FIX_MODE=true; shift ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Logging functions
log_pass() { echo -e "${GREEN}✓${NC} $1"; }
log_fail() { echo -e "${RED}✗${NC} $1"; ((ERRORS++)) || true; }
log_warn() { echo -e "${YELLOW}⚠${NC} $1"; ((WARNINGS++)) || true; }
log_info() { echo "  $1"; }

# Initialize report
cat > "$REPORT_FILE" << EOF
# Structural Verification Report
**Generated**: $(date '+%Y-%m-%d %H:%M:%S')
**Repo Root**: $REPO_ROOT

---

## Checks

| Check | Status | Details |
|-------|--------|---------|
EOF

append_report() {
    echo "$1" >> "$REPORT_FILE"
}

echo "=== STRUCTURAL VERIFICATION ==="
echo "Repo: $REPO_ROOT"
echo ""

# CHECK 1: No lowercase outgoing/ directory
# Note: macOS filesystem is case-insensitive, so we check the actual directory name
echo "--- Check 1: Casing Invariant (outgoing/ vs OUTGOING/) ---"

# Use ls to get the actual casing of the directory
ACTUAL_OUTGOING=$(ls -1 "$REPO_ROOT" 2>/dev/null | grep -i "^outgoing$" || true)

if [ -z "$ACTUAL_OUTGOING" ]; then
    log_pass "No outgoing directory at root (OK - may not exist yet)"
    append_report "| Casing Invariant | PASS | No outgoing directory |"
elif [ "$ACTUAL_OUTGOING" = "OUTGOING" ]; then
    log_pass "OUTGOING/ exists with correct uppercase casing"
    append_report "| Casing Invariant | PASS | OUTGOING/ uppercase |"
else
    log_fail "VIOLATION: lowercase '$ACTUAL_OUTGOING/' exists at root (should be OUTGOING/)"
    append_report "| Casing Invariant | FAIL | $ACTUAL_OUTGOING/ wrong casing |"
    if $FIX_MODE; then
        log_info "Fix: Rename to OUTGOING/ manually: git mv $ACTUAL_OUTGOING OUTGOING"
    fi
fi

# CHECK 2: Sanctioned root structure only
echo ""
echo "--- Check 2: Root Structure (zones 00-06 + exceptions) ---"

# Get all root directories (macOS compatible)
FORBIDDEN_DIRS=""
FORBIDDEN_COUNT=0

for item in "$REPO_ROOT"/*/; do
    [ -d "$item" ] || continue
    dir=$(basename "$item")

    # Skip hidden directories
    case "$dir" in
        .*) continue ;;
    esac

    # Check if sanctioned
    case "$dir" in
        0[0-6]-*) ;; # Numbered zones - OK
        OUTGOING) ;; # Sanctioned exception - OK
        *)
            FORBIDDEN_DIRS="$FORBIDDEN_DIRS $dir"
            ((FORBIDDEN_COUNT++)) || true
            ;;
    esac
done

if [ $FORBIDDEN_COUNT -gt 0 ]; then
    log_fail "VIOLATION: Unsanctioned root directories found:"
    for dir in $FORBIDDEN_DIRS; do
        log_info "  - $dir/"
    done
    append_report "| Root Structure | FAIL | Unsanctioned:$FORBIDDEN_DIRS |"
else
    log_pass "Only sanctioned directories at root"
    append_report "| Root Structure | PASS | Zones 00-06 + OUTGOING |"
fi

# CHECK 3: Orphan files at root (except CLAUDE.md, COCKPIT.md, Makefile)
echo ""
echo "--- Check 3: Root Orphan Files ---"

ORPHAN_FILES=""
ORPHAN_COUNT=0

for item in "$REPO_ROOT"/*; do
    [ -f "$item" ] || continue
    file=$(basename "$item")

    # Skip hidden files
    case "$file" in
        .*) continue ;;
    esac

    # Check if sanctioned
    case "$file" in
        CLAUDE.md|COCKPIT.md|Makefile) ;; # Sanctioned - OK
        APPLY_DEFRAG_APPROVAL.txt) ;; # Temporary approval file - OK
        *)
            ORPHAN_FILES="$ORPHAN_FILES $file"
            ((ORPHAN_COUNT++)) || true
            ;;
    esac
done

if [ $ORPHAN_COUNT -gt 0 ]; then
    log_fail "VIOLATION: Orphan files at root ($ORPHAN_COUNT files):"
    count=0
    for file in $ORPHAN_FILES; do
        log_info "  - $file"
        ((count++)) || true
        [ $count -ge 10 ] && break
    done
    if [ $ORPHAN_COUNT -gt 10 ]; then
        log_info "  ... and $((ORPHAN_COUNT - 10)) more"
    fi
    append_report "| Root Orphans | FAIL | $ORPHAN_COUNT orphan files |"
else
    log_pass "No orphan files at root"
    append_report "| Root Orphans | PASS | Only sanctioned files |"
fi

# CHECK 4: COCKPIT.md paths are valid
echo ""
echo "--- Check 4: COCKPIT.md Path Validity ---"

if [ -f "COCKPIT.md" ]; then
    # Extract paths from COCKPIT.md markdown links
    BROKEN_PATHS=""
    BROKEN_COUNT=0

    while IFS= read -r path; do
        if [ ! -e "$path" ]; then
            BROKEN_PATHS="$BROKEN_PATHS $path"
            ((BROKEN_COUNT++)) || true
        fi
    done < <(grep -o '\](\.\/[^)]*' COCKPIT.md 2>/dev/null | sed 's/\](\.\///' || true)

    if [ $BROKEN_COUNT -gt 0 ]; then
        log_fail "COCKPIT.md contains broken paths:"
        for path in $BROKEN_PATHS; do
            log_info "  - $path"
        done
        append_report "| COCKPIT Paths | FAIL | $BROKEN_COUNT broken |"
    else
        log_pass "All COCKPIT.md paths resolve"
        append_report "| COCKPIT Paths | PASS | All paths valid |"
    fi
else
    log_fail "COCKPIT.md not found at root"
    append_report "| COCKPIT Paths | FAIL | File missing |"
fi

# CHECK 5: No references to config/coordination.yaml (post-defrag)
echo ""
echo "--- Check 5: Stale Path References ---"

# Check for references to paths that will move during defrag
# Exclude OUTGOING/ and 05-ARCHIVE/ which contain historical references
STALE_REFS=$(grep -r "config/coordination" --include="*.md" --include="*.yaml" --include="*.sh" . 2>/dev/null | grep -v "OUTGOING/" | grep -v "05-ARCHIVE/" | wc -l | tr -d ' ')

if [ "$STALE_REFS" -gt 0 ]; then
    log_warn "Found $STALE_REFS references to config/coordination (may need update after defrag)"
    append_report "| Stale References | WARN | $STALE_REFS config/ references |"
else
    log_pass "No stale config/ references in active files"
    append_report "| Stale References | PASS | No stale paths |"
fi

# CHECK 6: Lowercase outgoing/ references in docs
echo ""
echo "--- Check 6: Lowercase 'outgoing/' in Documentation ---"

# Count lowercase references, excluding proper OUTGOING/ references
LOWERCASE_REFS=$(grep -rn "outgoing/" --include="*.md" --include="*.sh" . 2>/dev/null | grep -v "OUTGOING/" | wc -l | tr -d ' ')

if [ "$LOWERCASE_REFS" -gt 0 ]; then
    log_warn "Found $LOWERCASE_REFS lowercase 'outgoing/' references in docs"
    log_info "(Run: grep -rn 'outgoing/' --include='*.md' | grep -v OUTGOING)"
    append_report "| Lowercase Refs | WARN | $LOWERCASE_REFS in docs |"
else
    log_pass "No lowercase outgoing/ references"
    append_report "| Lowercase Refs | PASS | None found |"
fi

# CHECK 7: Continuation packet schema exists
echo ""
echo "--- Check 7: Packet Schema Completeness ---"

if [ -f "00-ORCHESTRATION/schemas/packet_protocol.json" ]; then
    if grep -q '"continuation"' "00-ORCHESTRATION/schemas/packet_protocol.json"; then
        log_pass "Continuation packet type defined in schema"
        append_report "| Packet Schema | PASS | Continuation type exists |"
    else
        log_warn "Continuation packet type not in schema"
        append_report "| Packet Schema | WARN | Missing continuation type |"
    fi
else
    log_fail "packet_protocol.json not found"
    append_report "| Packet Schema | FAIL | Schema missing |"
fi

# SUMMARY
echo ""
echo "=== SUMMARY ==="
append_report ""
append_report "---"
append_report ""
append_report "## Summary"
append_report ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    log_pass "All checks passed"
    append_report "**Result**: ALL CHECKS PASSED"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    log_warn "$WARNINGS warnings (0 errors)"
    append_report "**Result**: $WARNINGS WARNINGS (review recommended)"
    exit 0
else
    log_fail "$ERRORS errors, $WARNINGS warnings"
    append_report "**Result**: $ERRORS ERRORS, $WARNINGS WARNINGS"
    exit 1
fi
