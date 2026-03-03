# Rosetta / Intent / Backlog Triad Reconstitution v1

**Date**: 2026-03-02  
**Status**: first-pass triad recovery design  
**Purpose**: define how Rosetta Stone, Intent Compass, and Backlog should be restored as constitutional, executive, and program layers in the new shell

---

## 1. Problem Statement

The current repo exhibits a structural contradiction:

- Rosetta Stone is still referenced as constitutional vocabulary authority
- Intent Compass is still referenced as executive priority authority
- Backlog and implementation map are live and working

But:

- the live authoritative Rosetta path is unresolved
- the live authoritative Intent Compass path is unresolved
- the backlog does not visibly bind upward to those layers in a strict way

That means the system can execute work while its constitutional and executive anchors are partly ghosted.

This document defines the required reconstitution.

---

## 2. Triad Roles

### Rosetta

Role:

- constitutional vocabulary substrate
- term pedigree
- ontology alignment reference
- shared conceptual DNA

Rosetta answers:

- what does this term mean here?
- what are the canonical categories?
- what concept families exist?
- which terms are live, historical, deprecated, or superseded?

### Intent Compass

Role:

- executive steering vector
- priority and campaign layer
- active direction for the current system

Intent Compass answers:

- what matters now?
- what is active, deferred, parked, resolved?
- what intentions are steering current work?

### Backlog / Program

Role:

- administrative work program
- executable queue
- dependencies, owners, venues, phases

Backlog answers:

- what gets built next?
- by whom?
- where?
- in what order?

Backlog must not answer why in the absence of Intent, or what a term means in the absence of Rosetta.

---

## 3. The Required Flow

The lawful direction is:

`Rosetta -> Intent -> Program -> Execution -> Reconciliation -> Ontology`

This means:

- vocabulary constrains intention language
- intention constrains program
- program constrains execution
- execution emits runtime and communications artifacts
- reconciliation distills these into repo truth
- ontology projects the result downstream

Forbidden reverse authority:

- program redefining intention
- ontology redefining Rosetta
- runtime state redefining program

---

## 4. Rosetta As Two Surfaces

The redesign should split Rosetta into two linked surfaces.

### A. Rosetta Pedigree

Purpose:

- preserve historical evolution
- keep original conceptual inventions
- retain supersession chain
- provide archaeology

Properties:

- rich
- historical
- not the main everyday constitutional surface

### B. Rosetta Constitutional Surface

Purpose:

- provide compact, active vocabulary authority
- support ontology gate and constitutional usage
- expose current term set cleanly

Properties:

- small enough to be operational
- explicitly current
- references pedigree for depth and history

This solves two problems at once:

- preserves originality
- avoids turning Rosetta into an unusable mega-file

---

## 5. Intent Compass As Two Surfaces

The same split should likely be used for Intent.

### A. Intent Pedigree / Archaeology

Purpose:

- preserve the history of intentions, campaigns, and supersessions
- retain why certain priorities existed

### B. Live Intent Compass

Purpose:

- expose only the current steering layer

Contents:

- active intentions
- deferred intentions
- parked intentions
- resolved intentions with lightweight references
- campaign groupings
- review cadence

This prevents executive law from becoming a full narrative graveyard.

---

## 6. Program Binding Rules

Every program artifact must bind upward.

### For every backlog item

Require:

- `program_id`
- `intention_refs`
- `rosetta_refs`
- `owner`
- `venue`
- `phase`

### Why this matters

Without upward binding:

- backlog becomes bureaucratic clutter
- implementation drifts from intention
- constitutional vocabulary stops steering actual work

### What should happen to unbound items

- quarantine
- or route to an "unbound-program" review list until bound properly

There should be no silently floating work.

---

## 7. Deferred Commitments

Historical evidence shows deferred commitments evaporate.

Therefore:

- a deferred commitment that changes direction belongs in executive layer
- a deferred commitment that is an implementation obligation belongs in program layer
- a deferred commitment should never live only in memory prose

Recommended split:

- `executive/deferred/` for steering commitments
- `program/deferred/` or program-level status flags for work commitments

---

## 8. Candidate Physical Surfaces

This is the likely logical physical shape:

```text
constitution/
  vocabulary/
    ROSETTA-STONE.md
    pedigree/
  boundaries/
  ontology-gates/

executive/
  INTENT-COMPASS.md
  pedigree/
  campaigns/
  deferred/

program/
  IMPLEMENTATION-BACKLOG.md
  IMPLEMENTATION-MAP.md
  tranches/
```

This does not require immediate physical renaming of the whole repo.
It does require the logical distinction to be made explicit immediately.

---

## 9. Recovery Sequence

### Step 1: Recover Rosetta references

Tasks:

- enumerate all current references to Rosetta
- identify what terms are still operationally required by ontology, canon, and playbooks
- define the constitutional Rosetta surface
- preserve pedigree separately

### Step 2: Recover Intent references

Tasks:

- enumerate all current references to Intent Compass
- reconstruct the currently active executive layer from live state, program docs, and historical references
- split current vs historical

### Step 3: Rebind program artifacts

Tasks:

- add intention and Rosetta binding to implementation backlog and map
- surface unbound items explicitly

### Step 4: Add validators

Validators should fail if:

- a program item has no intention binding
- a program item has no vocabulary binding when it clearly should
- Rosetta/Intent references point to ghost paths

---

## 10. Edge Cases

### Case: Rosetta term exists only historically

Action:

- keep in pedigree
- not in active constitutional surface unless still used

### Case: Intention is historically important but not active

Action:

- move to resolved/archived executive pedigree
- keep a traceable status, not active steering

### Case: Program item spans multiple intentions

Action:

- support multiple `intention_refs`
- require one primary reference when possible

### Case: Program item has no clear Rosetta term

Action:

- either add a justified vocabulary relation
- or explicitly mark as vocabulary-gap requiring constitutional review

This may be how genuine new categories enter the system.

---

## 11. Summary

The triad is not optional ornamentation.

It is the minimum structure required so the shell knows:

- what it means
- what it wants
- what it is doing

Right now only the third is robustly surfaced.
This reconstitution exists to restore the first two.
