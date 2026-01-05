# ORACLE09 EXECUTION CONTEXT
## For Claude Code Desktop - Single Pass Completion

**Date**: 2026-01-04
**Status**: CRITICAL - Previous executions documented but didn't delete
**Objective**: Achieve pristine directory state in single session

---

## THE PROBLEM

ACTUAL_TREE.md is **3604 lines**. Should be ~200.

Previous Claude Codes created RECONSOLIDATION_AUDIT and EXECUTION_LOG-036 that:
- ✓ Correctly identified bloat
- ✓ Correctly recommended deletions
- ✗ **DID NOT ACTUALLY DELETE ANYTHING**

The bloat remains. Oracle9 cannot close until it's gone.

---

## WHAT MUST BE DELETED (CONFIRMED SAFE)

### Tier 1: Immediate Delete (No Extraction)

| Directory/File | Est. Files | Why Safe |
|----------------|------------|----------|
| `Coherence/` | 200+ | Already distilled → CANON-20010, 20020, 35210, CANON-00016 |
| `9-Canon/` | 60+ | Superseded by CANON/ (new naming scheme) |
| `outputs/recovery/` | 300+ | Temporary staging, content already processed |
| `system_prompts/New Folder With Items 2/` | 500+ | Complete duplicate of above |
| `new perspectives/` | 2 | Exploratory, absorbed |
| `0-context.md` | 1 | Stale context file |
| `MANIFEST.md` | 1 | Stale |
| `syncrescendence_refactoring_final.md` | 1 | Superseded |
| `ORACLE09_CONTEXT_v4.md` | 1 | Superseded |
| `ORACLE09_CONTEXT_v5.md` | 1 | Superseded |
| `ORACLE09_CONTEXT_v7.md` | 1 | Superseded |

### Tier 2: Extract Then Delete

| Directory | Extract | Target | Then Delete |
|-----------|---------|--------|-------------|
| `intelligence architecture/` | `youtube_subscription_list.md` | Append to CANON-31143 | Yes |
| `intelligence architecture/` | Check `meta_narrative_and_perspectival_schemas.md` | If unique → CANON-00015 supplement | Yes |
| `0-prompts/` | Document evolution | ARCHIVE-PROMPT-ARCHAEOLOGY.md | Yes |
| `system_prompts/` | `justification-*.md` | Move to ARCHIVE/ | Delete rest |

### Tier 3: Move (Not Delete)

| File | Destination |
|------|-------------|
| `DIRECTIVE-034A_FORENSIC_RECOVERY.md` | `orchestration/directives/` |
| `DIRECTIVE-034B_PROJECT_MANAGEMENT.md` | `orchestration/directives/` |
| `DIRECTIVE-035A_COHERENCE_DISTILLATION.md` | `orchestration/directives/` |
| `DIRECTIVE-035B_TECH_LUNAR_SOURCES.md` | `orchestration/directives/` |
| `DIRECTIVE-036-FORENSIC-RECONSOLIDATION.md` | `orchestration/directives/` |

---

## PRINCIPAL'S CORRECTIONS TO APPLY

### 1. Implementation Protocol Placement
ARCHIVE is for superseded content. Implementation protocols are LIVING.

**Check these ARCHIVE files for implementation content:**
- `ARCHIVE-COGNITIVE-PALACE-FULL.md` - any procedures → satellite of CANON-20000
- `ARCHIVE-METAHUMANISM-FULL.md` - any practices → satellite of CANON-35210
- `ARCHIVE-ARTIFACT-PATTERN-LANGUAGE.md` - any workflows → satellite of CANON-00011

### 2. Intelligence Architecture Digestion
Don't just extract youtube_subscription_list. Check ALL files for unique insights:
- `meta_narrative_and_perspectival_schemas.md` (35K) - verify absorbed into CANON-00015
- `constitution.md` - verify absorbed into CANON-00017
- `operational_engine.md` - verify absorbed into CANON-00010

### 3. Repository Hygiene Protocol
Add to END of every future directive:

```markdown
## REPOSITORY HYGIENE CHECK (MANDATORY)
Before creating execution log:
1. `ls -la` at root - verify no orphans
2. `tree -L 2` - verify structure  
3. Fresh-agent test - any file in ≤2 decisions
4. Document any exceptions with explicit justification
```

---

## TARGET STATE

Root level should contain ONLY:

```
syncrescendence/
├── ARCHIVE/
├── CANON/
├── EXEMPLA/
├── OPERATIONAL/
├── orchestration/
├── QUEUE/
├── SOURCES/
├── .git/
├── .gitignore
└── README.md
```

**10 items. Not 25+.**

---

## EXECUTION SEQUENCE

### Morning (Claude Code Desktop - NOW)

1. **Execute Tier 1 deletions** - `rm -rf` commands
2. **Execute Tier 2 extractions** - copy content, verify, delete
3. **Execute Tier 3 moves** - `mv` commands
4. **Check ARCHIVE for implementation content** - relocate if found
5. **Regenerate tree** - verify pristine
6. **Update project management** - mark tasks complete

### Evening (Claude Code 2 - if needed)

1. Complete any remaining deletions
2. Final verification
3. Create ORACLE09_FINAL_STATE.md (minimal)
4. Commit

---

## SUCCESS CRITERIA

| Metric | Before | Target |
|--------|--------|--------|
| ACTUAL_TREE.md lines | 3604 | ~200 |
| Root level items | 25+ | 10 |
| Bloat directories | 6 | 0 |
| Orphan files at root | 10+ | 0 |

---

## DO NOT

- Create Oracle10 initialization docs (premature)
- Create extensive summaries (wastes tokens)
- Document without executing (previous failure)
- Skip verification (must regenerate tree)

---

*Oracle9 closes with verified pristine state. Nothing else.*
