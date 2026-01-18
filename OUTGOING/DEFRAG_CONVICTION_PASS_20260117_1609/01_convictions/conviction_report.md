# Conviction Report
## Enforceable Laws to Prevent Crashout-Class Failures
**Generated**: 2026-01-17

---

## I. THE FIVE INVARIANTS

These are non-negotiable system laws. Violating any one creates conditions for crashout.

### Invariant 1: OBJECTIVE LOCK
**Statement**: No work begins until the objective is explicitly stated and confirmed.

**Mechanism**:
- Principal states objective
- System confirms: "Objective locked: [restatement]"
- Only then: suggestions, planning, execution permitted

**Violation Consequence**: Drift, wasted effort, context pollution

---

### Invariant 2: TRANSLATION LAYER
**Statement**: All outputs must be intelligible to the Principal without requiring re-transmission.

**Mechanism**:
- Technical commands include: what it does, what happens if it fails
- Jargon is defined or avoided
- Error messages are interpreted

**Violation Consequence**: Retransmission burden, emotional overload

---

### Invariant 3: RECEIPTS (Closure Gate)
**Statement**: No completion claim without artifacts in the repository.

**Mechanism**:
- Execution produces: logs, commits, state updates
- Planning produces: plan packets
- Research produces: evidence packets
- All sessions produce: continuation packets if deletable

**Violation Consequence**: Implicit database formation, unverifiable work

---

### Invariant 4: CONTINUATION/DELETABILITY
**Statement**: Any conversation can be deleted without losing system state.

**Mechanism**:
- Continuation packet captures: summary, decisions, work done, work remaining, files to load
- Packet written to repo before session end
- "Safe to delete" explicitly stated

**Violation Consequence**: State trapped in ephemeral surface, crashout on discontinuity

---

### Invariant 5: REPO SOVEREIGNTY
**Statement**: The repository is the constitutional source of truth; web apps are cache.

**Mechanism**:
- All durable state lives in repo
- Platform memory is operational convenience only
- When mismatch: trust repo
- Protected zones (01-CANON, state/) require Principal approval to modify

**Violation Consequence**: Reality divergence, conflicting authorities, memory corruption

---

## II. THE CRASHOUT FAILURE CHAIN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CRASHOUT FAILURE CHAIN                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STAGE 1: IMPLICIT DATABASE FORMATION                                      │
│  ─────────────────────────────────────                                      │
│  State accumulates in conversation without externalization.                 │
│  Invariant Violated: RECEIPTS, CONTINUATION/DELETABILITY                   │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 2: CONTEXT DISCONTINUITY                                            │
│  ────────────────────────────                                               │
│  Memory glitch, UI loss, session end, model switch.                         │
│  Invariant Violated: REPO SOVEREIGNTY (state wasn't there)                 │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 3: INVISIBLE ASSUMPTION RESPONSE                                    │
│  ────────────────────────────────────────                                   │
│  System responds as if shared context exists when it doesn't.               │
│  Invariant Violated: TRANSLATION LAYER                                     │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 4: RETRANSMISSION BURDEN                                            │
│  ────────────────────────────────                                           │
│  Principal must re-explain everything.                                      │
│  Invariant Violated: OBJECTIVE LOCK (original objective lost)              │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 5: EMOTIONAL OVERLOAD → ABANDONMENT                                 │
│  ─────────────────────────────────────────                                  │
│  Frustration spikes; system appears hostile.                                │
│  All invariants failed; trust damaged.                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Invariant-to-Stage Mapping

| Stage | Primary Invariant Violated | Would Have Prevented |
|-------|---------------------------|---------------------|
| 1 | RECEIPTS, CONTINUATION | State externalization |
| 2 | REPO SOVEREIGNTY | State was in repo |
| 3 | TRANSLATION LAYER | Clear output |
| 4 | OBJECTIVE LOCK | Objective was recorded |
| 5 | (Cascade) | Any earlier invariant |

---

## III. WELLS VS RIVERS ABSTRACTION

### Definition

**Well**: A stable, addressable location where state accumulates and can be retrieved.
- Repository files
- CANON documents
- State vectors (system_state.json)
- Blackboard packets
- Execution logs

**River**: A transient flow that carries information but doesn't retain it.
- Conversation threads
- Platform memory (opaque, non-exportable)
- Context windows
- Real-time API responses

### Mapping to This Repo

| Category | Examples | Type |
|----------|----------|------|
| 01-CANON/ | CANON-*.md | Well (deep, protected) |
| 00-ORCHESTRATION/state/ | REF-*, ARCH-*, DYN-*, ledgers | Well (operational) |
| 00-ORCHESTRATION/blackboard/ | EVD, PLN, EXE, AUD packets | Well (structured) |
| 00-ORCHESTRATION/execution_logs/ | EXECUTION_LOG-*.md | Well (historical) |
| Claude Web conversations | Project memory | River (cache only) |
| ChatGPT threads | Memory fragments | River (unreliable) |
| Gemini sessions | No memory | River (stateless) |

### The Principle

**Rivers must flow INTO wells.** Information that matters must be externalized from rivers (conversations) into wells (repo) before the river disappears.

The crashout occurs when:
1. Rivers accumulate state that should be in wells
2. The river evaporates (session ends, memory glitches)
3. State is lost because it never reached a well

### Enforcement

- **Closure Gate**: Requires artifacts (well deposits) before completion
- **Continuation Packet**: Forces river-to-well transfer at session end
- **Repo Sovereignty**: Wells are authoritative; rivers are not

---

## IV. ENFORCEMENT MECHANISMS

### Mechanism 1: Three Gates in Cockpit Constitution

| Gate | Invariant Protected | Trigger |
|------|---------------------|---------|
| Objective Lock Gate | OBJECTIVE LOCK | Before any work |
| Dispatch Gate | TRANSLATION LAYER | Before platform routing |
| Closure Gate | RECEIPTS, CONTINUATION | Before completion claim |

### Mechanism 2: Packet Protocol

| Packet Type | Invariant Protected | When Created |
|-------------|---------------------|--------------|
| Evidence (EVD) | RECEIPTS | After research |
| Plan (PLN) | RECEIPTS | After planning |
| Execution (EXE) | RECEIPTS | After implementation |
| Audit (AUD) | RECEIPTS | After verification |
| Continuation (CONT) | CONTINUATION | At session end |

### Mechanism 3: Protected Zones

| Zone | Invariant Protected | Access Rule |
|------|---------------------|-------------|
| 01-CANON/ | REPO SOVEREIGNTY | Principal approval for changes |
| 00-ORCHESTRATION/state/ | REPO SOVEREIGNTY | Validation required |
| CLAUDE.md | REPO SOVEREIGNTY | Constitutional; rarely changed |

### Mechanism 4: Verification Commands

```bash
make verify              # Run all validation checks
git status               # Check uncommitted work
cat system_state.json    # Check state vector
tail events.jsonl        # Check recent events
```

---

## V. CONVICTION SUMMARY

**If you remember nothing else, remember this:**

1. **Lock objective first** — no suggestions until objective confirmed
2. **Translate for humans** — no unexplained jargon or commands
3. **Leave receipts** — no work without artifacts in repo
4. **Make it deletable** — continuation packet = safe to delete
5. **Trust the repo** — repository is truth; conversations are temporary

**These five convictions, enforced, prevent crashout.**
