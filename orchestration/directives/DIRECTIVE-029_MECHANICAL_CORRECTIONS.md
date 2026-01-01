# DIRECTIVE-029: Mechanical Corrections
## Phase 3A — Prerequisite Structural Fixes

**Issued**: 2026-01-01
**Issued By**: Oracle8
**To**: Claude Code Desktop (Claude 2 or Claude 3)
**Priority**: HIGH
**Type**: Execution (non-destructive edits)

---

## PRINCIPAL'S MANDATE

> "Conduct both [mechanical corrections AND forensic semantic audit]. You have access to the actual files in the Project Files, and Claude 2 and 3 stand at the ready."

## ORACLE'S INTERPRETATION

These mechanical corrections clear the prerequisite layer for deeper semantic work. They are:
- File count updates (claims vs reality)
- Cross-reference fixes (wrong CANON IDs)
- Flowchart updates (old numbering scheme)

These do NOT require editorial judgment — they are factual corrections.

## ALTERNATIVES CONSIDERED

1. **Defer corrections until semantic audit complete** — Rejected: stale references confuse navigation
2. **Fix only critical errors** — Rejected: partial fixes leave inconsistency
3. **Complete all identified corrections** — CHOSEN: clean prerequisite layer

## RATIONALE (18-Lens Summary)

| Lens | Pass/Fail |
|------|-----------|
| First Principles | ✓ Corrections factually necessary |
| Elegance | ✓ Removes inconsistency |
| Agentify | ✓ Accurate cross-refs enable agent navigation |
| Six Sigma | ✓ Defect elimination |

**Threshold**: 16/18 pass — APPROVED

---

## MANDATORY FIRST STEP: VERIFICATION

Before ANY edits, verify these claims by running:

```bash
# Count actual CANON files
ls /path/to/syncrescendence/CANON*.md 2>/dev/null | wc -l
# Or if flat at root:
ls /path/to/syncrescendence/CANON-*.md | wc -l

# Verify CANON-00012 is Modal Sequence
head -20 CANON-00012-MODAL_SEQUENCE-cosmos.md

# Verify CANON-00008 is Resolutions
head -20 CANON-00008-RESOLUTIONS-cosmos.md

# Verify CANON-00001 is Origin (not Syncrescendence)
head -20 CANON-00001-ORIGIN-cosmos.md

# Verify CANON-00005 is Syncrescendence
head -20 CANON-00005-SYNCRESCENDENCE-cosmos.md
```

**Document actual output in execution log before proceeding.**

---

## CORRECTION SPECIFICATIONS

### HIGH PRIORITY (Navigation-Critical)

#### Correction 1: CANON-00010-OPERATIONS Line 237
**File**: `CANON-00010-OPERATIONS-cosmos.md`
**Line**: 237
**Current**: `**For complete Modal Sequence architecture**: CANON-00008`
**Correction**: `**For complete Modal Sequence architecture**: CANON-00012`
**Rationale**: Modal Sequence is CANON-00012. CANON-00008 is Resolutions.

#### Correction 2: CANON-00000-SCHEMA Line 35
**File**: `CANON-00000-SCHEMA-cosmos.md`
**Line**: 35
**Current**: `Navigate dependencies between all 17 CANON documents`
**Correction**: `Navigate dependencies between all **71 CANON documents**`
**Rationale**: Actual file count is 71, not 17.

#### Correction 3: CANON-00006-CORPUS Line 29
**File**: `CANON-00006-CORPUS-cosmos.md`
**Line**: 29
**Current**: `**28 Core CANON artifacts**`
**Correction**: `**71 CANON documents**`
**Rationale**: Actual file count is 71, not 28.

#### Correction 4: CANON-00008-RESOLUTIONS Line 969
**File**: `CANON-00008-RESOLUTIONS-cosmos.md`
**Line**: 969
**Current**: `Modal Sequence (CANON-00008) added throughout`
**Correction**: `Modal Sequence (CANON-00012) added throughout`
**Rationale**: Self-referential error. This document IS CANON-00008. Modal Sequence is CANON-00012.

### MEDIUM PRIORITY (Flowchart Accuracy)

#### Correction 5: CANON-00000-SCHEMA Flowchart (Lines 288-334)
**File**: `CANON-00000-SCHEMA-cosmos.md`
**Section**: Dependency Flowchart (lines ~273-334)

The flowchart uses **old numbering** where:
- CANON-00001 was "Syncrescendent Core" → Now CANON-00001 is ORIGIN
- CANON-00008 was "Energy States" / "Modal Sequence" → Now CANON-00008 is RESOLUTIONS

**Required Changes**:

Line 288-289:
```
CURRENT:
       CANON-00001          CANON-00008
  (Syncrescendent Core) (Energy States)

SHOULD BE:
       CANON-00005          CANON-00012
    (Syncrescendence)   (Modal Sequence)
```

Line 321-322:
```
CURRENT:
     CANON-00000         CANON-00008 CANON-00007
    (This Schema)   (Modal Sequence) (Production)

SHOULD BE:
     CANON-00000         CANON-00012 CANON-00007
    (This Schema)   (Modal Sequence) (Evaluation)
```

Line 346 (Critical Path section):
```
CURRENT: 3. **CANON-00005 Syncrescendent Core** (30 minutes)
CORRECT: Already correct (CANON-00005 IS Syncrescendence)

CURRENT: 4. **CANON-00008: Energy States** (20 minutes)
SHOULD BE: 4. **CANON-00012: Modal Sequence** (20 minutes)
```

#### Correction 6: CANON-00006-CORPUS Line 1438 (if exists)
**File**: `CANON-00006-CORPUS-cosmos.md`
**Issue**: Reference to CANON-00001 for "What is Syncrescendence?"
**Current**: Points to CANON-00001
**Correction**: Point to CANON-00005

**Verify line number exists before editing** — corpus is 1804 lines, line 1438 should exist.

### LOW PRIORITY (Terminology)

#### Correction 7: CANON-00002-LINEAGE Line 84
**File**: `CANON-00002-LINEAGE-cosmos.md`
**Line**: 84
**Current**: `The **Coherence Chain** directly addresses meaning-making`
**Correction**: `The **Insight Chain** directly addresses meaning-making`
**Rationale**: Coherence is the planetary body within Insight Chain. The Chain itself is "Insight."

---

## EXECUTION PHASES

### Phase A: Verification (5 minutes)
1. Run all verification commands above
2. Document actual output
3. Confirm line numbers match (documents may have shifted)

### Phase B: High Priority Corrections (10 minutes)
1. Corrections 1-4 (single line changes)
2. Verify each change with `grep` after

### Phase C: Flowchart Corrections (15 minutes)
1. Correction 5 (CANON-00000-SCHEMA flowchart)
2. This requires careful multi-line editing
3. Preserve ASCII art formatting

### Phase D: Remaining Corrections (5 minutes)
1. Corrections 6-7
2. Final verification

---

## VERIFICATION PROTOCOL

After ALL corrections, run:

```bash
# Verify no remaining old references
grep -r "CANON-00008.*Modal" *.md
grep -r "17 CANON" *.md
grep -r "28 Core CANON" *.md
grep -r "CANON-00001.*Syncrescen" *.md

# These should return EMPTY or only historical/quoted references
```

---

## EXECUTION LOG REQUIREMENTS

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-01-029.md`

Include:
1. **PRE-EXECUTION SURVEY**: Actual verification command output
2. **PHASE-BY-PHASE EXECUTION**: Each correction with before/after
3. **POST-EXECUTION VERIFICATION**: grep outputs showing corrections applied
4. **ORACLE DECISIONS ENCODED**: This directive implements COSMOS_ALIGNMENT_REPORT findings
5. **STATUS**: COMPLETE/INCOMPLETE/BLOCKED

---

## SUCCESS CRITERIA

- [ ] All 7 corrections applied
- [ ] Verification grep commands return empty (or only valid historical refs)
- [ ] Flowchart accurately reflects current CANON numbering
- [ ] Execution log saved with evidence

---

## CONTEXT DOCUMENT

Include ORACLE_CONTEXT_v2.md with this directive per constitutional requirement.

---

*Mechanical corrections clear the path. Semantic work follows.*
