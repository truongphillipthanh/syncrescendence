# Verification Plan
## Pre-Apply and Post-Apply Verification Steps
**Generated**: 2026-01-17

---

## I. VERIFICATION PHILOSOPHY

**Principle**: Every defrag operation must be verifiable before and after.

- **Pre-verification**: Confirm baseline state and conditions
- **Post-verification**: Confirm desired state achieved without regressions

---

## II. PRE-APPLY VERIFICATION

Run these checks BEFORE executing defrag_apply.sh:

### Check 1: APPLY Authorization
```bash
# Must pass
if [ -f "APPLY_DEFRAG_APPROVAL.txt" ] && grep -q "I_APPROVE_DEFRAG_APPLY" APPLY_DEFRAG_APPROVAL.txt; then
    echo "PASS: APPLY authorized"
else
    echo "FAIL: APPLY not authorized"
    exit 1
fi
```

### Check 2: Git Status Clean (or Known)
```bash
# Document current state
git status --porcelain > /tmp/pre_defrag_status.txt
echo "Pre-defrag untracked/modified files: $(wc -l < /tmp/pre_defrag_status.txt)"
```

### Check 3: Count Baseline Metrics
```bash
# Count orphans at root
ROOT_ORPHANS=$(ls *.md 2>/dev/null | grep -v CLAUDE.md | wc -l)
echo "Root MD orphans: $ROOT_ORPHANS"

# Count orphan directories
ROOT_DIRS=$(ls -d */ 2>/dev/null | grep -v -E '^(0[0-6]|OUTGOING|config|\.)' | wc -l)
echo "Root orphan directories: $ROOT_DIRS"

# Count .DS_Store files
DS_STORE=$(find . -name ".DS_Store" 2>/dev/null | wc -l)
echo ".DS_Store files: $DS_STORE"

# Count Oracle contexts
ORACLE_CONTEXTS=$(ls 00-ORCHESTRATION/oracle_contexts/ORACLE*.md 2>/dev/null | wc -l)
echo "Oracle contexts in correct location: $ORACLE_CONTEXTS"

# Count directives
DIRECTIVES=$(ls 00-ORCHESTRATION/directives/DIRECTIVE*.md 2>/dev/null | wc -l)
echo "Directives in correct location: $DIRECTIVES"
```

### Check 4: Verify Blockers Resolved
```bash
# Check DIRECTIVE-043 collision
COLLISION_A=$(ls DIRECTIVE-043A*.md 2>/dev/null | wc -l)
COLLISION_B=$(ls DIRECTIVE-043B*.md 2>/dev/null | wc -l)
if [ "$COLLISION_A" -gt 1 ] || [ "$COLLISION_B" -gt 1 ]; then
    echo "FAIL: DIRECTIVE-043 collision not resolved"
    echo "  043A variants: $COLLISION_A"
    echo "  043B variants: $COLLISION_B"
    exit 1
fi
echo "PASS: DIRECTIVE-043 collision resolved"
```

### Check 5: Backup Confirmation
```bash
# Ensure we can rollback
CURRENT_COMMIT=$(git rev-parse HEAD)
echo "Current commit: $CURRENT_COMMIT"
echo "Rollback command: git checkout $CURRENT_COMMIT -- ."
```

---

## III. POST-APPLY VERIFICATION

Run these checks AFTER executing defrag_apply.sh:

### Check 1: Zero Root Orphan MD Files (except CLAUDE.md)
```bash
ORPHAN_MD=$(ls *.md 2>/dev/null | grep -v CLAUDE.md | wc -l)
if [ "$ORPHAN_MD" -eq 0 ]; then
    echo "PASS: No orphan .md files at root"
else
    echo "FAIL: Found $ORPHAN_MD orphan .md files:"
    ls *.md | grep -v CLAUDE.md
fi
```

### Check 2: Zero Root Orphan Directories
```bash
ORPHAN_DIRS=$(ls -d */ 2>/dev/null | grep -v -E '^(0[0-6]|OUTGOING|config|\.)' | wc -l)
if [ "$ORPHAN_DIRS" -eq 0 ]; then
    echo "PASS: No orphan directories at root"
else
    echo "FAIL: Found $ORPHAN_DIRS orphan directories:"
    ls -d */ | grep -v -E '^(0[0-6]|OUTGOING|config|\.)'
fi
```

### Check 3: Zero .DS_Store Files
```bash
DS_COUNT=$(find . -name ".DS_Store" 2>/dev/null | wc -l)
if [ "$DS_COUNT" -eq 0 ]; then
    echo "PASS: No .DS_Store files"
else
    echo "FAIL: Found $DS_COUNT .DS_Store files"
fi
```

### Check 4: All Directives in Correct Location
```bash
ROOT_DIRECTIVES=$(ls DIRECTIVE*.md 2>/dev/null | wc -l)
PROPER_DIRECTIVES=$(ls 00-ORCHESTRATION/directives/DIRECTIVE*.md 2>/dev/null | wc -l)
if [ "$ROOT_DIRECTIVES" -eq 0 ]; then
    echo "PASS: No directives at root ($PROPER_DIRECTIVES in directives/)"
else
    echo "FAIL: $ROOT_DIRECTIVES directives still at root"
fi
```

### Check 5: All Oracle Contexts in Correct Location
```bash
ROOT_ORACLE=$(ls ORACLE*.md 2>/dev/null | wc -l)
PROPER_ORACLE=$(ls 00-ORCHESTRATION/oracle_contexts/ORACLE*.md 2>/dev/null | wc -l)
if [ "$ROOT_ORACLE" -eq 0 ]; then
    echo "PASS: No oracle contexts at root ($PROPER_ORACLE in oracle_contexts/)"
else
    echo "FAIL: $ROOT_ORACLE oracle contexts still at root"
fi
```

### Check 6: Archive Files Created
```bash
ARCHIVE_COUNT=$(ls 05-ARCHIVE/ARCH-*.md 2>/dev/null | wc -l)
echo "Archive files created: $ARCHIVE_COUNT"
if [ "$ARCHIVE_COUNT" -ge 9 ]; then
    echo "PASS: Expected archive files present"
else
    echo "WARN: Fewer archive files than expected (expected ~9)"
fi
```

### Check 7: No Broken Internal Links
```bash
# Find all markdown links and verify targets exist
echo "Checking for broken internal links..."
BROKEN=0
for file in $(find . -name "*.md" -not -path "./.git/*" -not -path "./OUTGOING/*"); do
    # Extract relative links
    links=$(grep -oE '\]\([^)]+\.md\)' "$file" | grep -oE '[^(]+\.md' | grep -v '^http')
    for link in $links; do
        dir=$(dirname "$file")
        target="$dir/$link"
        if [ ! -f "$target" ] && [ ! -f "./$link" ]; then
            echo "BROKEN: $file -> $link"
            BROKEN=$((BROKEN + 1))
        fi
    done
done
if [ "$BROKEN" -eq 0 ]; then
    echo "PASS: No broken internal links found"
else
    echo "WARN: Found $BROKEN potentially broken links (manual review recommended)"
fi
```

### Check 8: Git Status Shows Only Expected Changes
```bash
# Compare to pre-defrag status
git status --porcelain > /tmp/post_defrag_status.txt
echo "Post-defrag changes:"
cat /tmp/post_defrag_status.txt
```

### Check 9: Canon Integrity
```bash
# Verify canon files not corrupted
CANON_COUNT=$(ls 01-CANON/CANON*.md 2>/dev/null | wc -l)
echo "Canon documents: $CANON_COUNT"
# Add checksum verification if needed
```

---

## IV. VERIFICATION SCRIPT

Create as `post_apply_verify.sh`:

```bash
#!/bin/bash
# Post-Apply Verification Script
# Generated: 2026-01-17

echo "=== DEFRAG POST-APPLY VERIFICATION ==="
echo "Running at: $(date)"
echo ""

PASS=0
FAIL=0
WARN=0

check() {
    if eval "$1"; then
        echo "✓ PASS: $2"
        PASS=$((PASS + 1))
    else
        echo "✗ FAIL: $2"
        FAIL=$((FAIL + 1))
    fi
}

warn_check() {
    if eval "$1"; then
        echo "✓ PASS: $2"
        PASS=$((PASS + 1))
    else
        echo "⚠ WARN: $2"
        WARN=$((WARN + 1))
    fi
}

# Core checks
check '[ $(ls *.md 2>/dev/null | grep -v CLAUDE.md | wc -l) -eq 0 ]' "No orphan .md at root"
check '[ $(ls -d */ 2>/dev/null | grep -v -E "^(0[0-6]|OUTGOING|config|\.)" | wc -l) -eq 0 ]' "No orphan dirs at root"
check '[ $(find . -name ".DS_Store" | wc -l) -eq 0 ]' "No .DS_Store files"
check '[ $(ls DIRECTIVE*.md 2>/dev/null | wc -l) -eq 0 ]' "No directives at root"
check '[ $(ls ORACLE*.md 2>/dev/null | wc -l) -eq 0 ]' "No oracle contexts at root"

# Expected outcomes
warn_check '[ $(ls 05-ARCHIVE/ARCH-*.md 2>/dev/null | wc -l) -ge 9 ]' "Archive files created"
warn_check '[ $(ls 00-ORCHESTRATION/directives/DIRECTIVE*.md 2>/dev/null | wc -l) -ge 10 ]' "Directives in place"

echo ""
echo "=== SUMMARY ==="
echo "PASS: $PASS"
echo "FAIL: $FAIL"
echo "WARN: $WARN"

if [ "$FAIL" -gt 0 ]; then
    echo ""
    echo "DEFRAG VERIFICATION FAILED"
    exit 1
else
    echo ""
    echo "DEFRAG VERIFICATION PASSED"
    exit 0
fi
```

---

## V. VERIFICATION CHECKLIST (Manual)

### Before Apply
- [ ] Read defrag_plan.md completely
- [ ] Confirm DIRECTIVE-043 collision resolved
- [ ] Confirm system_prompts/ audit complete
- [ ] Create APPLY_DEFRAG_APPROVAL.txt with correct content
- [ ] Run pre-apply verification commands
- [ ] Note current git commit for rollback

### After Apply
- [ ] Run post_apply_verify.sh
- [ ] Review any WARN or FAIL items
- [ ] Spot-check 3 relocated files for content integrity
- [ ] Verify no new orphans created
- [ ] Commit defrag changes with descriptive message
- [ ] Update DYN-TREE.md to reflect new structure

---

## VI. ROLLBACK VERIFICATION

If rollback needed:

```bash
# Revert to pre-defrag state
git checkout <pre-defrag-commit> -- .

# Verify rollback
ls *.md | head -10  # Should show orphans again
ls DIRECTIVE*.md    # Should show root directives
ls ORACLE*.md       # Should show root oracles

echo "Rollback complete. Verify state matches pre-defrag."
```

---

**Verification is non-negotiable. No operation is complete until verified.**
