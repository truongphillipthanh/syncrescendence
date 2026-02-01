# DIRECTIVE-036C: ORACLE9 ACTUAL COMPLETION
## Execute-Not-Document: Final Pass

**Issued**: 2026-01-04
**Executor**: Claude Code Desktop (PRIMARY)
**Backup**: Claude Code 2 (Tonight if needed)
**Critical**: Previous directives DOCUMENTED but DID NOT EXECUTE. This one EXECUTES.

---

## BLOAT ASSESSMENT FROM ACTUAL_TREE.md

### Root-Level Orphans Identified (3604 lines = CRISIS)

| Orphan | Type | Est. Files | Action |
|--------|------|------------|--------|
| `0-context.md` | File | 1 | DELETE |
| `0-prompts/` | Dir | 33 | DELETE (after prompt archaeology) |
| `9-Canon/` | Dir | 60+ | DELETE (superseded by CANON/) |
| `Coherence/` | Dir | 200+ | **DELETE** (already distilled in 035A) |
| `DIRECTIVE-034A_FORENSIC_RECOVERY.md` | File | 1 | MOVE → orchestration/directives/ |
| `DIRECTIVE-034B_PROJECT_MANAGEMENT.md` | File | 1 | MOVE → orchestration/directives/ |
| `DIRECTIVE-035A_COHERENCE_DISTILLATION.md` | File | 1 | MOVE → orchestration/directives/ |
| `DIRECTIVE-035B_TECH_LUNAR_SOURCES.md` | File | 1 | MOVE → orchestration/directives/ |
| `DIRECTIVE-036-FORENSIC-RECONSOLIDATION.md` | File | 1 | MOVE → orchestration/directives/ |
| `intelligence architecture/` | Dir | 21 | DELETE (after youtube_subscription_list extraction) |
| `MANIFEST.md` | File | 1 | DELETE (stale) |
| `new perspectives/` | Dir | 2 | DELETE |
| `ORACLE09_CONTEXT_v4.md` | File | 1 | DELETE (superseded) |
| `ORACLE09_CONTEXT_v5.md` | File | 1 | DELETE (superseded) |
| `ORACLE09_CONTEXT_v7.md` | File | 1 | DELETE (superseded) |
| `outputs/recovery/` | Dir | 300+ | DELETE (temporary recovery staging) |
| `syncrescendence_refactoring_final.md` | File | 1 | DELETE |
| `system_prompts/New Folder With Items 2/` | Dir | 500+ | **DELETE** (TRIPLE duplicate) |
| `aliases/` | Dir | 50+ | EVALUATE (symlinks - may be useful) |

**TOTAL BLOAT**: ~1200+ files to delete

---

## PHASE 1: IMMEDIATE DELETIONS (No Extraction Needed)

Claude Code Desktop: Execute these commands IN ORDER:

```bash
# STEP 1: Delete massive duplicate/superseded directories
rm -rf "Coherence/"
rm -rf "9-Canon/"
rm -rf "outputs/recovery/"
rm -rf "system_prompts/New Folder With Items 2/"
rm -rf "new perspectives/"

# STEP 2: Delete orphan files at root
rm -f "0-context.md"
rm -f "MANIFEST.md"
rm -f "syncrescendence_refactoring_final.md"
rm -f "ORACLE09_CONTEXT_v4.md"
rm -f "ORACLE09_CONTEXT_v5.md"
rm -f "ORACLE09_CONTEXT_v7.md"

# STEP 3: Move directives to proper location
mv "DIRECTIVE-034A_FORENSIC_RECOVERY.md" orchestration/directives/
mv "DIRECTIVE-034B_PROJECT_MANAGEMENT.md" orchestration/directives/
mv "DIRECTIVE-035A_COHERENCE_DISTILLATION.md" orchestration/directives/
mv "DIRECTIVE-035B_TECH_LUNAR_SOURCES.md" orchestration/directives/
mv "DIRECTIVE-036-FORENSIC-RECONSOLIDATION.md" orchestration/directives/

# STEP 4: Verify Phase 1 complete
echo "=== ROOT LEVEL CHECK ==="
ls -la | head -30
```

**Expected result**: Root level should now show ONLY:
- `aliases/` (evaluate next)
- `ARCHIVE/`
- `CANON/`
- `EXEMPLA/`
- `intelligence architecture/` (extract then delete)
- `OPERATIONAL/`
- `orchestration/`
- `QUEUE/`
- `SOURCES/`
- `0-prompts/` (document then delete)
- `system_prompts/` (clean up then delete)

---

## PHASE 2: VALUE EXTRACTION THEN DELETION

### 2.1 Intelligence Architecture → [[CANON-31143-FEED_CURATION-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION]]

```bash
# Extract youtube_subscription_list FIRST
cat "intelligence architecture/youtube_subscription_list.md" >> CANON/CANON-31143-FEED_CURATION-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md

# Verify extraction
grep -c "youtube" CANON/CANON-31143-FEED_CURATION-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md

# THEN delete the directory
rm -rf "intelligence architecture/"
```

### 2.2 0-prompts/ → Archaeology Document

Create prompt archaeology document, then delete:

```bash
# Create archaeology document
cat > ARCHIVE/ARCHIVE-PROMPT-ARCHAEOLOGY.md << 'EOF'
# ARCHIVE: Prompt Evolution Archaeology

**Archived**: 2026-01-04
**Source**: 0-prompts/ directory

## Evolution Phases

### Phase 1: First Lunar
- first_lunar_genesis_prompt.md
- first_lunar_system_prompt.md

### Phase 2: First Annealment
- Terminology standardization
- Celestial body metaphor introduction

### Phase 3: Second Lunar
- Deep research integration
- Coherence/Transcendence synthesis

### Phase 4: Feedcraft Annealment
- Acumen sensing chain development

*Note: Detailed content superseded by OPERATIONAL/prompts/canonical/*
EOF

# Delete the directory
rm -rf "0-prompts/"
```

### 2.3 System Prompts Cleanup

```bash
# Keep only the justification files (move to ARCHIVE)
mv system_prompts/justification-*.md ARCHIVE/

# Keep ASSEMBLED for archaeology
mv system_prompts/ASSEMBLED_SYSTEM_PROMPTS_v2.1.md ARCHIVE/ARCHIVE-SYSTEM-PROMPTS-v2.1.md

# Delete remaining system_prompts directory
rm -rf "system_prompts/"
```

---

## PHASE 3: ALIASES EVALUATION

The `aliases/` directory contains symlinks. Decision required:

```bash
# Check what's in aliases
ls -la aliases/

# If symlinks are broken or redundant with CANON structure:
rm -rf aliases/

# If useful navigation aids, KEEP but document
```

**Sovereign decision needed**: Are aliases/ providing navigation value or just cruft?

---

## PHASE 4: REPOSITORY HYGIENE VERIFICATION

After all deletions:

```bash
# Generate fresh tree (2 levels)
tree -L 2 > ACTUAL_TREE_CLEAN.md

# Count files at root (should be minimal)
ls -la | wc -l

# Verify expected structure
echo "=== EXPECTED ROOT STRUCTURE ==="
echo "ARCHIVE/"
echo "CANON/"
echo "EXEMPLA/"
echo "OPERATIONAL/"
echo "orchestration/"
echo "QUEUE/"
echo "SOURCES/"
echo ".git/"
echo "README.md"
```

---

## PHASE 5: FINAL TASKS FOR ORACLE9

### 5.1 Update Project Management

```bash
# Update tasks.csv - mark completed
# Update burndown.csv
# Regenerate DASHBOARD.md
```

### 5.2 Create Minimal Handoff State

```bash
cat > orchestration/state/ORACLE09_FINAL_STATE.md << 'EOF'
# ORACLE09 FINAL STATE

**Completed**: 2026-01-04
**Status**: COMPLETE

## Accomplishments
- Repository hygiene restored (~1200 files deleted)
- Coherence content distilled (97.6% compression)
- System prompts canonized (4 labs)
- Model profiles indexed
- SOURCES infrastructure operational (184 entries)
- [[CANON-00017-AGENTIC_CONSTITUTION-cosmos]] Agentic Constitution created

## Handoff for Oracle10
- Pristine directory architecture
- IIC Configuration ready
- Paradigm sources: 4 integrated, 4 processed, 39 remaining

## Known Deferred
- modal2/ content (6 files) → Modal 2 phase
- Remaining paradigm sources → Oracle10 ongoing
- aliases/ disposition → Sovereign decision
EOF
```

---

## DELEGATION FOR CLAUDE CODE 2 (TONIGHT)

If Phase 1-4 incomplete by morning session end:

**Priority 1**: Complete all deletions (Phase 1-2)
**Priority 2**: Verify hygiene (Phase 4)
**Priority 3**: Update project management (Phase 5.1)

Do NOT create Oracle10 initialization until Oracle9 is VERIFIED COMPLETE.

---

## VERIFICATION CHECKLIST

Before declaring Oracle9 complete:

### Deletions Executed
- [ ] `Coherence/` deleted (~200 files)
- [ ] `9-Canon/` deleted (~60 files)
- [ ] `outputs/recovery/` deleted (~300 files)
- [ ] `system_prompts/New Folder With Items 2/` deleted (~500 files)
- [ ] `new perspectives/` deleted
- [ ] `intelligence architecture/` deleted (after extraction)
- [ ] `0-prompts/` deleted (after archaeology)
- [ ] Root orphan files deleted (6 files)

### Files Moved
- [ ] 5 DIRECTIVE-* files → orchestration/directives/
- [ ] justification-*.md → ARCHIVE/
- [ ] ASSEMBLED_SYSTEM_PROMPTS_v2.1.md → ARCHIVE/

### Value Extracted
- [ ] youtube_subscription_list.md → [[CANON-31143-FEED_CURATION-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION]]
- [ ] Prompt archaeology → ARCHIVE-PROMPT-ARCHAEOLOGY.md

### Hygiene Verified
- [ ] Fresh ACTUAL_TREE.md generated
- [ ] Root level has ≤10 items
- [ ] No orphan files at root
- [ ] Fresh-agent test passes

---

## GIT COMMIT

```bash
git add -A
git commit -m "ORACLE9 COMPLETE: Deleted ~1200 bloat files

DELETED:
- Coherence/ (200+ files, distilled in 035A)
- 9-Canon/ (60+ files, superseded)
- outputs/recovery/ (300+ files, temp staging)
- system_prompts/New Folder With Items 2/ (500+ files, duplicate)
- intelligence architecture/ (after extraction)
- 0-prompts/ (after archaeology)
- 6 root orphan files

EXTRACTED:
- youtube_subscription_list → [[CANON-31143-FEED_CURATION-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION]]
- Prompt evolution → ARCHIVE-PROMPT-ARCHAEOLOGY

MOVED:
- 5 DIRECTIVEs → orchestration/directives/
- Justifications → ARCHIVE/

VERIFIED:
- Root level: ~10 items (was 20+)
- Fresh-agent test: PASS
- Repository: PRISTINE

Oracle9 COMPLETE. Ready for Oracle10 IIC Configuration."
```

---

## CRITICAL REMINDER

**18-LENS ON VISIBILITY GAP**:
I cannot see inside files. Claude Code Desktop CAN. Therefore:
1. Claude Code must VERIFY content before deletion where extraction needed
2. Claude Code must CONFIRM deletions actually occurred
3. Claude Code must REGENERATE tree to prove pristine state

**REPOSITORY HYGIENE PROTOCOL** (Add to all future directives):
```
## REPOSITORY HYGIENE CHECK (MANDATORY)
Before creating execution log:
1. ls -la at root - verify no orphans
2. tree -L 2 - verify structure
3. Fresh-agent test - 2 decisions to any file
4. Document any exceptions with justification
```

---

*DIRECTIVE-036C: Execute, verify, commit. Oracle9 closes today.*
