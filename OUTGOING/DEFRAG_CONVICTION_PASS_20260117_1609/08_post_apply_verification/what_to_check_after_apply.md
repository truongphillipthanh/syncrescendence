# What to Check After Apply
## Post-Defrag Verification Guide
**Generated**: 2026-01-17T16:09:00Z
**Status**: APPLY NOT ARMED — This is pre-apply documentation

---

## I. IMMEDIATE VERIFICATION (First 5 Minutes)

### Step 1: Run Automated Verification
```bash
cd /Users/system/Desktop/syncrescendence
./outgoing/DEFRAG_CONVICTION_PASS_20260117_1609/07_apply_scripts/post_apply_verify.sh
```

All tests should pass. If any fail, see Section V (Recovery).

---

### Step 2: Check Git Status
```bash
git status
```

**Expected**: Clean working tree, all changes committed.

**If dirty**: Review uncommitted changes, decide to commit or discard.

---

### Step 3: Verify Root Cleanliness
```bash
ls -la *.md
```

**Expected**: Only `CLAUDE.md` (and optionally `COCKPIT.md` if created)

**If other .md files**: Check if they are blocked items (DIRECTIVE-043, working docs)

---

## II. STRUCTURAL VERIFICATION

### Canonical Directories Should Exist
```bash
ls -d 0[0-6]-*/ 05-ARCHIVE/ OUTGOING/
```

**Expected**: All directories present.

### Oracle Contexts Consolidated
```bash
ls 00-ORCHESTRATION/oracle_contexts/ORACLE*.md
```

**Expected**: ORACLE10_CONTEXT_FINAL.md, ORACLE12_CONTEXT.md, ORACLE13_CONTEXT.md

### Archives Populated
```bash
ls 05-ARCHIVE/ARCH-*.md | wc -l
```

**Expected**: 5+ archived files

### Research in Raw
```bash
ls 04-SOURCES/raw/
```

**Expected**: Research directories and files relocated here

---

## III. CANON INTEGRITY

### Canon File Count
```bash
ls 01-CANON/CANON-*.md | wc -l
```

**Expected**: ~70 CANON files (including the relocated CANON-31150)

### No Canon at Root
```bash
ls CANON-*.md 2>/dev/null
```

**Expected**: No output (empty)

---

## IV. REMAINING BLOCKERS

After APPLY, these items still require Principal decision:

### Blocker 1: DIRECTIVE-043 Collision
**Current State**: Two files claim 043A, two claim 043B
**Required**: Principal selects Option A, B, or C from defrag_plan.md
**Location**: Root-level DIRECTIVE-043*.md files

### Blocker 2: Working Document Disposition
**Files**:
- `checklist.md`
- `INTERACTION_PARADIGM.md`
- `rapport_contract.md`

**Required**: Principal decides: Keep / Archive / Delete for each

### Blocker 3: Directory Consolidation
**Items**:
- `system_prompts/` → merge into 02-OPERATIONAL/prompts/?
- `.decisions/` → archive or delete?

**Required**: Principal reviews unique content before merging/deleting

---

## V. RECOVERY PROCEDURES

### If Verification Fails
1. **Identify failing tests** from post_apply_verify.sh output
2. **Check git log** for what changed: `git log --oneline -5`
3. **Selective restore** if needed: `git checkout HEAD~1 -- <file>`
4. **Full rollback** if critical: Run `defrag_rollback.sh`

### If Files Are Missing
```bash
# Find file in git history
git log --all --full-history -- "**/filename.md"

# Restore from specific commit
git checkout <commit> -- path/to/file
```

### If Build/Verify Fails
```bash
# Run standard verification
make verify

# Check for syntax errors in CSVs
head -1 00-ORCHESTRATION/state/tasks.csv
python3 -c "import csv; list(csv.reader(open('00-ORCHESTRATION/state/tasks.csv')))"
```

---

## VI. SUCCESS CHECKLIST

After APPLY, these should all be true:

- [ ] `post_apply_verify.sh` passes all tests
- [ ] No .DS_Store files anywhere
- [ ] No research directories at root
- [ ] No DEEP_RESEARCH_PROMPT-*.md at root
- [ ] No CANON files at root
- [ ] ORACLE contexts in oracle_contexts/
- [ ] Obsolete files in 05-ARCHIVE/ARCH-*
- [ ] Git history intact (git log shows all moves)
- [ ] make verify passes (if applicable)

---

## VII. NEXT STEPS AFTER SUCCESSFUL DEFRAG

1. **Resolve blockers** (DIRECTIVE-043, working docs)
2. **Consider creating COCKPIT.md** (see 06_patch_proposals/)
3. **Update system_state.json** to reflect defrag completion
4. **Create continuation packet** documenting this work
5. **Optional**: Commit defrag pass to outgoing/ for archaeology

---

## VIII. METRICS

Track defrag effectiveness:

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Root .md files | ~30+ | 1-2 | <5 |
| Root directories | ~10+ | 0 | 0 (except numbered) |
| Orphan CANON files | 1 | 0 | 0 |
| Oracle context drift | Yes | No | No |
| Obsolete files archived | 0 | 9+ | All identified |

---

**This document is pre-apply. Update after APPLY with actual verification results.**
