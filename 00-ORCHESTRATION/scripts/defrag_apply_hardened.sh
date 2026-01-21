#!/usr/bin/env bash
# DEFRAG APPLY - HARDENED VERSION
# Constitutional cleanup with portable paths and safety checks
#
# Version: 4.0.0
# Created: 2026-01-18
# Authority: STRUCTURAL_STABILIZATION_PASS
#
# SAFETY:
# - Requires APPLY_DEFRAG_APPROVAL.txt with exact content
# - Creates git stash backup before any changes
# - Fails fast on any error
# - Validates no lowercase outgoing/ exists

set -euo pipefail

# PORTABLE REPO ROOT (Constitutional Rule #11)
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "ERROR: Not in a git repository"
    exit 1
}

cd "$REPO_ROOT"

TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
LOG_FILE="$REPO_ROOT/00-ORCHESTRATION/state/DYN-DEFRAG_APPLY_LOG_${TIMESTAMP}.md"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Logging
log() { echo "[$( date '+%H:%M:%S' )] $1" | tee -a "$LOG_FILE"; }
error() { echo -e "${RED}[$( date '+%H:%M:%S' )] ERROR: $1${NC}" | tee -a "$LOG_FILE"; exit 1; }
warn() { echo -e "${YELLOW}[$( date '+%H:%M:%S' )] WARN: $1${NC}" | tee -a "$LOG_FILE"; }
pass() { echo -e "${GREEN}[$( date '+%H:%M:%S' )] ✓ $1${NC}" | tee -a "$LOG_FILE"; }

# Initialize log
cat > "$LOG_FILE" << EOF
# Defrag Apply Log (Hardened)
**Started**: $(date '+%Y-%m-%d %H:%M:%S')
**Repo**: $REPO_ROOT
**Mode**: APPLY

---

## Pre-Flight Checks

EOF

echo "=== DEFRAG APPLY (HARDENED) ==="
echo "Repo: $REPO_ROOT"
echo ""

# PRE-FLIGHT CHECK 1: Approval file
log "Checking approval file..."
if [ ! -f "$REPO_ROOT/APPLY_DEFRAG_APPROVAL.txt" ]; then
    error "APPLY_DEFRAG_APPROVAL.txt not found. Create it with content: I_APPROVE_DEFRAG_APPLY"
fi

APPROVAL_CONTENT=$(cat "$REPO_ROOT/APPLY_DEFRAG_APPROVAL.txt" | tr -d '\n')
if [ "$APPROVAL_CONTENT" != "I_APPROVE_DEFRAG_APPLY" ]; then
    error "APPLY_DEFRAG_APPROVAL.txt must contain exactly: I_APPROVE_DEFRAG_APPLY"
fi
pass "Approval verified"

# PRE-FLIGHT CHECK 2: No legacy OUTGOING/ or lowercase outgoing/ (Constitutional Rule #4)
# Canonical form is now -OUTGOING/
log "Checking exchange directory invariants..."
LEGACY_OUTGOING=$(ls -1 "$REPO_ROOT" 2>/dev/null | grep -E "^(OUTGOING|outgoing)$" || true)

if [ -n "$LEGACY_OUTGOING" ]; then
    error "VIOLATION: legacy '$LEGACY_OUTGOING/' exists. Canonical form is -OUTGOING/. Migrate with: git mv $LEGACY_OUTGOING -OUTGOING"
fi

# Ensure -OUTGOING/ exists
if [ ! -d "$REPO_ROOT/-OUTGOING" ]; then
    log "Creating -OUTGOING/..."
    mkdir -p "$REPO_ROOT/-OUTGOING"
fi

# Ensure -INBOX/ exists
if [ ! -d "$REPO_ROOT/-INBOX" ]; then
    log "Creating -INBOX/..."
    mkdir -p "$REPO_ROOT/-INBOX"
fi

pass "-OUTGOING/ and -INBOX/ exist; no legacy forms"

# PRE-FLIGHT CHECK 3: Git backup
log "Creating git stash backup..."
git stash push -u -m "pre-defrag-hardened-$TIMESTAMP" 2>/dev/null || log "No changes to stash (clean working directory)"
pass "Backup created (or working directory was clean)"

echo "" >> "$LOG_FILE"
echo "## Execution Log" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# PHASE 1: DIRECTIVE ORPHANS
log "=== PHASE 1: DIRECTIVE ORPHANS ==="

DIRECTIVES_MOVED=0
DIRECTIVES_DELETED=0

for file in DIRECTIVE-042A_IIC_FOUNDATION.md DIRECTIVE-042B_MULTI_CLI.md \
            DIRECTIVE-042C_OPERATIONAL_HYGIENE.md DIRECTIVE-042D_GEMINI_VALIDATION.md \
            DIRECTIVE-044A.md DIRECTIVE-044B.md DIRECTIVE-045A.md DIRECTIVE-045B.md \
            DIRECTIVE-046A.md DIRECTIVE-046B.md; do
    if [ -f "$REPO_ROOT/$file" ]; then
        # Extract base name for comparison
        base_name=$(echo "$file" | sed 's/_.*\.md/.md/')

        if [ -f "$REPO_ROOT/00-ORCHESTRATION/directives/$base_name" ]; then
            # Compare for duplicates
            if diff -q "$REPO_ROOT/$file" "$REPO_ROOT/00-ORCHESTRATION/directives/$base_name" > /dev/null 2>&1; then
                log "  DELETE (duplicate): $file"
                git rm "$file"
                ((DIRECTIVES_DELETED++)) || true
            else
                log "  MOVE (unique): $file → 00-ORCHESTRATION/directives/"
                git mv "$file" "00-ORCHESTRATION/directives/"
                ((DIRECTIVES_MOVED++)) || true
            fi
        else
            log "  MOVE: $file → 00-ORCHESTRATION/directives/"
            git mv "$file" "00-ORCHESTRATION/directives/"
            ((DIRECTIVES_MOVED++)) || true
        fi
    fi
done

pass "Phase 1 complete: $DIRECTIVES_MOVED moved, $DIRECTIVES_DELETED deleted"

# PHASE 2: ORACLE ORPHANS
log "=== PHASE 2: ORACLE ORPHANS ==="

ORACLES_MOVED=0
for file in ORACLE12_PEDIGREE.md ORACLE12_PEDIGREE-045.md ORACLE12_SESSION_DELIVERABLES.md; do
    if [ -f "$REPO_ROOT/$file" ]; then
        log "  MOVE: $file → 00-ORCHESTRATION/directives/"
        git mv "$file" "00-ORCHESTRATION/directives/"
        ((ORACLES_MOVED++)) || true
    fi
done

pass "Phase 2 complete: $ORACLES_MOVED moved"

# PHASE 3: CANON RECONCILIATION
log "=== PHASE 3: CANON RECONCILIATION ==="

CANON_ROOT="CANON-31150-PLATFORM_CATALOG-lunar-ACUMEN-planetary-INFORMATION.md"
if [ -f "$REPO_ROOT/$CANON_ROOT" ]; then
    log "  DELETE (01-CANON version is authoritative): $CANON_ROOT"
    git rm "$CANON_ROOT"
    pass "Phase 3 complete: root CANON duplicate removed"
else
    log "  SKIP: $CANON_ROOT not found"
    pass "Phase 3 complete: already reconciled"
fi

# PHASE 4: GOVERNANCE FILES
log "=== PHASE 4: GOVERNANCE FILES ==="

for file in INTERACTION_PARADIGM.md checklist.md rapport_contract.md; do
    if [ -f "$REPO_ROOT/$file" ]; then
        dest_name="ARCH-$(echo $file | tr '[:lower:]' '[:upper:]' | sed 's/\.MD$//')"
        log "  ARCHIVE: $file → 00-ORCHESTRATION/state/$dest_name.md"
        git mv "$file" "00-ORCHESTRATION/state/$dest_name.md"
    fi
done

pass "Phase 4 complete"

# PHASE 5: RESEARCH FILES
log "=== PHASE 5: RESEARCH FILES ==="

for file in grok.md perplexity.md; do
    if [ -f "$REPO_ROOT/$file" ]; then
        log "  MOVE: $file → 04-SOURCES/raw/"
        git mv "$file" "04-SOURCES/raw/"
    fi
done

pass "Phase 5 complete"

# PHASE 6: CONFIG/ MIGRATION
log "=== PHASE 6: CONFIG/ MIGRATION ==="

if [ -d "$REPO_ROOT/config" ]; then
    [ -f "config/MCP_SETUP.md" ] && git mv "config/MCP_SETUP.md" "02-OPERATIONAL/" && log "  MOVE: config/MCP_SETUP.md → 02-OPERATIONAL/"
    [ -f "config/coordination.yaml" ] && git mv "config/coordination.yaml" "02-OPERATIONAL/" && log "  MOVE: config/coordination.yaml → 02-OPERATIONAL/"
    [ -f "config/mcp.json.template" ] && git mv "config/mcp.json.template" "06-EXEMPLA/" && log "  MOVE: config/mcp.json.template → 06-EXEMPLA/"

    # Remove empty directory
    if [ -z "$(ls -A config 2>/dev/null)" ]; then
        rmdir config && log "  DELETE: empty config/"
    else
        warn "config/ not empty after migration - manual cleanup required"
    fi
    pass "Phase 6 complete"
else
    log "  SKIP: config/ already migrated"
    pass "Phase 6 complete (already done)"
fi

# PHASE 7: SYSTEM_PROMPTS/ ARCHIVE
log "=== PHASE 7: SYSTEM_PROMPTS/ ARCHIVE ==="

if [ -d "$REPO_ROOT/system_prompts" ]; then
    mkdir -p "05-ARCHIVE/ARCH-SYSTEM_PROMPTS_EVOLUTION_20260102"

    for file in system_prompts/*; do
        if [ -f "$file" ]; then
            git mv "$file" "05-ARCHIVE/ARCH-SYSTEM_PROMPTS_EVOLUTION_20260102/"
            log "  ARCHIVE: $(basename $file)"
        fi
    done

    if [ -z "$(ls -A system_prompts 2>/dev/null)" ]; then
        rmdir system_prompts && log "  DELETE: empty system_prompts/"
    fi
    pass "Phase 7 complete"
else
    log "  SKIP: system_prompts/ already archived"
    pass "Phase 7 complete (already done)"
fi

# PHASE 8: .decisions/ CLEANUP
log "=== PHASE 8: .decisions/ CLEANUP ==="

if [ -d "$REPO_ROOT/.decisions" ]; then
    if [ -f ".decisions/DESIGN_DECISIONS.md" ]; then
        if [ -f "00-ORCHESTRATION/state/ARCH-DESIGN_DECISIONS.md" ]; then
            if diff -q ".decisions/DESIGN_DECISIONS.md" "00-ORCHESTRATION/state/ARCH-DESIGN_DECISIONS.md" > /dev/null 2>&1; then
                git rm ".decisions/DESIGN_DECISIONS.md"
                log "  DELETE (duplicate): .decisions/DESIGN_DECISIONS.md"
            else
                git mv ".decisions/DESIGN_DECISIONS.md" "00-ORCHESTRATION/state/ARCH-DESIGN_DECISIONS_ROOT.md"
                log "  MOVE (unique): .decisions/DESIGN_DECISIONS.md"
            fi
        else
            git mv ".decisions/DESIGN_DECISIONS.md" "00-ORCHESTRATION/state/ARCH-DESIGN_DECISIONS.md"
            log "  MOVE: .decisions/DESIGN_DECISIONS.md"
        fi
    fi

    if [ -z "$(ls -A .decisions 2>/dev/null)" ]; then
        rmdir .decisions && log "  DELETE: empty .decisions/"
    fi
    pass "Phase 8 complete"
else
    log "  SKIP: .decisions/ already cleaned"
    pass "Phase 8 complete (already done)"
fi

# PHASE 9: -OUTGOING/ CLEANUP
log "=== PHASE 9: -OUTGOING/ CLEANUP ==="

if [ -d "$REPO_ROOT/-OUTGOING" ]; then
    cd "$REPO_ROOT/-OUTGOING"

    CLEANED=0
    for dir in DEFRAG_CONVICTION_PASS_20260117_1609 \
               RING7_PHASESHIFT_PASS_20260116_2219 \
               TELEOLOGY_PASS_4_20260117_1430 \
               TELEOLOGY_RING7_PASS_3_20260116_2330 \
               teleology_visibility_pass_20260116_192327 \
               teleology_visibility_pass_2_20260116_203238; do
        if [ -d "$dir" ] && [ -f "${dir}.zip" ]; then
            rm -rf "$dir"
            log "  DELETE (redundant): $dir/ (zip exists)"
            ((CLEANED++)) || true
        fi
    done

    cd "$REPO_ROOT"
    pass "Phase 9 complete: $CLEANED redundant directories removed"
else
    log "  SKIP: -OUTGOING/ not found"
    pass "Phase 9 complete"
fi

# FINALIZE
echo "" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "**Completed**: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"

log ""
log "=== DEFRAG COMPLETE ==="
log ""
log "Next steps:"
log "  1. Run verification: ./00-ORCHESTRATION/scripts/structural_verify.sh"
log "  2. Update COCKPIT.md if paths changed (config/ → 02-OPERATIONAL/)"
log "  3. Review changes: git status"
log "  4. Commit: git add -A && git commit -m 'chore(defrag): structural stabilization pass'"
log "  5. Remove approval: rm APPLY_DEFRAG_APPROVAL.txt"
