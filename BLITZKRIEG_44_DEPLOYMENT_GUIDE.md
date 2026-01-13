# BLITZKRIEG 44 DEPLOYMENT GUIDE
## Minor Housekeeping Blitzkrieg — Oracle 12

**Date**: 2026-01-11
**Classification**: MINOR (not dependent on Deep Research)
**Model Specification**: Sonnet 4.5 (both streams) — tactical, clear instructions

---

## PACKAGE CONTENTS

1. `ORACLE12_PEDIGREE.md` — Context for both streams
2. `DIRECTIVE-044A.md` — Stream A: Intention Compass + Tech Tree Audit
3. `DIRECTIVE-044B.md` — Stream B: Model Specification Protocol + Infrastructure

---

## DEPLOYMENT SEQUENCE

### Step 1: Prepare Claude 2 (Stream A)
1. Open Claude Code terminal (or new Claude 2 web session)
2. Navigate to repository root
3. Upload/provide: `ORACLE12_PEDIGREE.md` + `DIRECTIVE-044A.md`
4. Issue: "Execute DIRECTIVE-044A. Read the pedigree first."

### Step 2: Prepare Claude 3 (Stream B) — Simultaneous
1. Open separate Claude Code terminal (or Claude 3 web session)
2. Navigate to repository root
3. Upload/provide: `ORACLE12_PEDIGREE.md` + `DIRECTIVE-044B.md`
4. Issue: "Execute DIRECTIVE-044B. Read the pedigree first."

### Step 3: Verify Completion
Wait for both streams to complete, then verify:

```bash
# Stream A deliverables
ls 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
ls 00-ORCHESTRATION/state/ARCH-TECH_TREE_AUDIT.md

# Stream B deliverables
grep "BLITZKRIEG MODEL SPECIFICATION" CLAUDE.md
grep "model_routing" config/coordination.yaml

# Ledger updates
grep "TASK-08[89]" 00-ORCHESTRATION/state/tasks.csv
grep "TASK-09[01]" 00-ORCHESTRATION/state/tasks.csv
```

---

## EXPECTED OUTCOMES

| Stream | Deliverable | Lines |
|--------|-------------|-------|
| A | ARCH-INTENTION_COMPASS.md updated | +20 |
| A | ARCH-TECH_TREE_AUDIT.md created | ~60 |
| B | CLAUDE.md updated | +30 |
| B | coordination.yaml updated | +15 |
| Both | tasks.csv | +4 tasks |

---

## POST-BLITZKRIEG STATE

| Metric | Before | After |
|--------|--------|-------|
| New intentions captured | 0 | 11 |
| Tech tree audit | none | complete |
| Model specification | informal | formalized |
| coordination.yaml version | 2.0 | 2.1 |
| CLAUDE.md version | 2.0 | 2.1 |
| New tasks | 0 | 4 (TASK-088-091) |

---

## NOTES

This is a **minor** blitzkrieg. Unlike comprehensive blitzkriegs (like 43), this:
- Uses Sonnet 4.5 (not Opus)
- Has clear tactical instructions
- Takes 30-45 min per stream (not 60-90)
- Is housekeeping, not architectural

The **Claude Code Deep Research prompt** is being prepared separately and is NOT part of this blitzkrieg (different dependency chain).

---

*Blitzkrieg 44 ready for deployment | 2026-01-11*
