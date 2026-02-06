---
id: REF-CLARESCENCE_RUNBOOK
kind: REF
scope: system
target: syncrescendence
status: draft
updated: 2026-02-04
---

# /claresce — Clarescence Runbook

> **Clarescence** is the value-guided progressive refinement meta-operation (Rosetta #169).  
> This runbook turns it into a *repeatable operator procedure* with artifacts and decision triggers.

## When to invoke

Invoke **/claresce** whenever you hit a decision that:
- changes a **truth surface** (what is canonical),
- changes **lifecycle semantics** (what “done”/“claimed” means),
- affects **automation** (watchers, hooks, cron),
- affects **sovereignty/portability** (lock-in risk),
- adds/changes **interfaces** across agents/tools/platforms.

### Lightweight vs full
- **Partial clarescence (passes 1–3)**: local tactical decisions; low blast radius.
- **Full clarescence (passes 1–10)**: any decision that affects the substrate (σ-7) or creates irreversible coupling.

---

## Inputs (minimum viable packet)

Provide:
- **Topic**: what decision/path is being claresced
- **Current state**: relevant files + observed drift/conflicts
- **Options** (if any)
- **Constraints**: time/energy/cost/policies

---

## Outputs (required artifacts)

### 1) Clarescence record
Write one record per claresced decision:
- Location (choose one):
  - `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-YYYY-MM-DD-<slug>.md`
  - or embed in an existing DecisionAtom file (if that’s the canonical pattern)

### 2) DecisionAtom (if a decision is made)
If the clarescence converges to a binding choice, produce a DecisionAtom with:
- decision statement
- canonical truth surface (what becomes ground truth)
- reversibility + rollback path
- falsifier

### 3) Backlog + ledger updates
- Add/adjust implementation tasks in `IMPLEMENTATION-MAP.md` + `IMPLEMENTATION-BACKLOG.md`
- Append to `DYN-GLOBAL_LEDGER.md` with event `DECISION` (or other appropriate event)

---

## The 10-pass procedure (operator form)

For each pass, write **1–5 bullets max** (digestible), and only expand where the pass reveals conflict.

1) **Triumvirate Calibration**
- Destination / why now
- Current state / what’s broken
- Fit-to-destination verdict

2) **18+ Lenses**
- Quick scorecard: which lenses pass/fail and why (aim ≥12/18)

3) **CANON Coherence**
- What canonical docs say
- Where reality diverges

4) **Omni-Qualities**
- How this improves Omniscience/Omnipresence/Omnipotence/Omnibenevolence (or harms them)

5) **Five Faces**
- Sensing / Meaning / Intention / Embodiment / Harmony alignment

6) **Rosetta Precision**
- Term alignment; propose updates if terms drift

7) **Backlog Coherence**
- What it unblocks; what it creates; priority

8) **nth-order effects**
- What breaks; what compounds; what new dependencies appear

9) **Energy state**
- Is it sustainable to implement now? If not, stage it.

10) **Authenticity gate**
- Does this preserve sovereignty + optionality? Would Sovereign-at-peak-clarity approve?

---

## Standard output format (copy/paste)

```
CLARESCENCE: <topic>
Fidelity: partial|full
Passes run: 1-3 | 1-10
Convergent Path: <single best path>
Rationale (digest): <3-7 bullets>
Dependencies created/updated: <ids>
Falsifier: <what would make this wrong>
Confidence: low|medium|high
```

---

## Trigger list for current substrate work (σ-7)

Automatically claresce these categories:
- DB boundary: `model_db.py` vs Tech Stack DB (CANON-30300)
- Task lifecycle truth: filename suffixes vs in-body status
- Ledger event set + atomicity
- Worktree naming + branch policy
- Native swarm paradigm adoption (platform swarms)
