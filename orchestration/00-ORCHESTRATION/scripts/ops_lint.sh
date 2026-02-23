#!/usr/bin/env bash
#
# ops_lint.sh - Lightweight linter for engine artifacts
#
# Checks:
# - PROMPT-*.md files must have YAML frontmatter with: id, kind, scope, target
# - REF-*.md files must have YAML frontmatter with: id, kind, scope, target
#
# Usage: ./ops_lint.sh
# Exit: 0 on success, 1 on any failure

set -euo pipefail

# Get repo root
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || dirname "$(dirname "$(dirname "$(realpath "$0")")")")"
OPS_DIR="${REPO_ROOT}/engine"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

ERRORS=0
WARNINGS=0
CHECKED=0

log_pass() { echo -e "${GREEN}[PASS]${NC} $*"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $*"; ((ERRORS++)) || true; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $*"; ((WARNINGS++)) || true; }
log_info() { echo -e "[INFO] $*"; }

# Check if file has YAML frontmatter with required keys
check_frontmatter() {
    local file="$1"
    local rel_path="${file#$REPO_ROOT/}"
    local missing_keys=()

    ((CHECKED++)) || true

    # Check if file starts with ---
    if ! head -1 "$file" | grep -q '^---$'; then
        log_fail "$rel_path: Missing YAML frontmatter (no opening ---)"
        return 1
    fi

    # Extract frontmatter (between first --- and second ---)
    local frontmatter
    frontmatter=$(awk '/^---$/{if(++c==2)exit}c==1' "$file")

    if [[ -z "$frontmatter" ]]; then
        log_fail "$rel_path: Invalid YAML frontmatter (no closing ---)"
        return 1
    fi

    # Check required keys
    for key in id kind scope target; do
        if ! echo "$frontmatter" | grep -q "^${key}:"; then
            missing_keys+=("$key")
        fi
    done

    if [[ ${#missing_keys[@]} -gt 0 ]]; then
        log_fail "$rel_path: Missing required keys: ${missing_keys[*]}"
        return 1
    fi

    log_pass "$rel_path"
    return 0
}

echo "=== OPERATIONS ARTIFACT LINTER ==="
echo "Checking: ${OPS_DIR}"
echo ""

# Check PROMPT-*.md files (flat engine/)
echo "--- Checking PROMPT-*.md files (flat engine/) ---"
prompt_files=$(find "${OPS_DIR}" -maxdepth 1 -type f -name "PROMPT-*.md" 2>/dev/null || true)
if [[ -n "$prompt_files" ]]; then
    while IFS= read -r file; do
        check_frontmatter "$file" || true
    done <<< "$prompt_files"
else
    log_info "No PROMPT-*.md files found in engine/"
fi
echo ""

# Check REF-*.md files (flat engine/)
echo "--- Checking REF-*.md files (flat engine/) ---"
ref_files=$(find "${OPS_DIR}" -maxdepth 1 -type f -name "REF-*.md" 2>/dev/null || true)
if [[ -n "$ref_files" ]]; then
    while IFS= read -r file; do
        check_frontmatter "$file" || true
    done <<< "$ref_files"
else
    log_info "No REF-*.md files found in engine/"
fi
echo ""

# Summary
echo "=== SUMMARY ==="
echo "Files checked: $CHECKED"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"

if [[ $ERRORS -gt 0 ]]; then
    echo ""
    echo -e "${RED}LINT FAILED${NC}: $ERRORS error(s) found"
    exit 1
else
    echo ""
    echo -e "${GREEN}LINT PASSED${NC}: All checked files have valid frontmatter"
    exit 0
fi
