# CC72b Implementation Brief — What To Build First

**Date**: 2026-03-02  
**Purpose**: Narrow Oracle CC72b into implementation-grade next moves  
**Status**: Actionable for immediate repo work

---

## Verdict

Oracle's CC72b response is sufficient for the **reconciliation half** of the work and insufficient for the **final ontology/exocortex architecture lock**.

That means:
- Proceed now on repo-truth reconciliation, config scaffold implementation, and repo↔OpenClaw state synthesis.
- Do NOT yet treat Oracle's response as final authority for the full ontology or exocortex bridge design.

---

## What Is Safe To Lock Now

These are settled enough to implement:

1. **Ajna live truth must replace stale repo narrative**
   Ajna is already effectively rewired onto Claude Sonnet in OpenClaw. Current constitutional/orientation docs still narrate Ajna as Kimi-primary. That truth split is upstream of everything else.

2. **Only source-of-truth docs should be updated**
   Historical handoffs, archived strategy notes, and old prompts remain historical artifacts. Update current constitutional and orientation surfaces only.

3. **Config scaffold implementation is the next real build**
   The current `cat AGENTS.md CLAUDE-EXT.md > CLAUDE.md` pipeline is too thin for the live constellation state. The next build should be a minimal rendered + validated config system, not more prose about configuration.

4. **Memory must be layered before ontology**
   The next useful memory move is a deterministic repo↔OpenClaw synthesis loop. Do not add more memory backends yet.

5. **Ontology comes after state coherence**
   Build ontology only after the repo can truthfully reflect current runtime state and after memory synthesis exists.

---

## What Not To Lock Yet

These still need another engineering pass before implementation:

1. **Final ontology service shape**
   `FastAPI + SQLite` is plausible, but not yet canonically justified enough to treat as locked.

2. **Final exocortex ingestion model**
   The exocortex in this repo means the externalized SaaS/tooling layer. The exact bridge from that layer into ontology is still under-specified.

3. **Advanced memory stack**
   Graphiti, Qdrant, Honcho, Mem0, and similar options are still premature until the repo/OpenClaw synthesis loop is stable.

---

## First 5 Moves

### Move 1 — Reconcile current source-of-truth docs

Update only the living docs that define current reality:
- `AGENTS.md`
- `README.md`
- any current root/generated orientation that still presents Ajna as Kimi-primary

What to change:
- Ajna model and role status
- note that some historical documents still reflect pre-rewire state
- preserve historical artifacts without rewriting them

Success criterion:
- A new reader of the repo's current entrypoint docs no longer receives false state about Ajna.

### Move 2 — Create one explicit live-state artifact

Add a single current-state file under strategic state, for example:
- `00-ORCHESTRATION/state/TOOL-STACK-LIVE-STATE.md`

This file should record only:
- live OpenClaw model/auth/runtime facts
- channel state
- gateway state
- browser/tooling state
- unresolved blockers

Do not make it philosophical. It should be a factual operational snapshot.

Success criterion:
- repo truth now has one canonical place for March 2026 live harness state.

### Move 3 — Replace the `cat` config pipeline with the minimum viable rendered pipeline

Implement the smallest real config architecture:
- `render-configs.py`
- `validate-configs.py`
- `harness/`
- `machine/`
- `configs/`
- Makefile targets for `configs`, `validate`, and `reconcile`

Do not build the maximal constellation abstraction.
Do build:
- agent-specific subsetting
- harness-specific output
- machine-aware reconciliation
- path validation

Success criterion:
- `make configs` and `make validate` become real checks, not concatenation.

### Move 4 — Add repo↔OpenClaw reconciliation, not ontology

Before any ontology service:
- read OpenClaw runtime/config state
- normalize it into a repo artifact
- synthesize session/runtime deltas into repo memory

This can be script-first and local-only.

Success criterion:
- OpenClaw runtime facts can be pulled into the repo and compared against constitutional truth.

### Move 5 — Add a synthesis loop for memory

Implement one deterministic loop:
- transient OpenClaw/session state
- distilled into repo memory
- optionally promoted into canon later

Do not add graph memory yet.
Do not add vendor memory yet.

Success criterion:
- important runtime/decision state stops living only in OpenClaw files and threads.

---

## Exact Repo Targets To Touch First

### Touch now

- `/Users/system/syncrescendence/AGENTS.md`
- `/Users/system/syncrescendence/README.md`
- `/Users/system/syncrescendence/Makefile`
- `/Users/system/syncrescendence/00-ORCHESTRATION/state/`

### Add next

- `/Users/system/syncrescendence/render-configs.py`
- `/Users/system/syncrescendence/validate-configs.py`
- `/Users/system/syncrescendence/harness/`
- `/Users/system/syncrescendence/machine/`
- `/Users/system/syncrescendence/configs/`

### Do not touch yet

- historical handoffs
- archived Desktop strategy notes
- canon ontology gate files as part of a speculative rewrite
- Graphiti/Qdrant/Honcho integration files

---

## Operational Sequence

1. Update current repo truth so Ajna's live state is no longer contradicted by current docs.
2. Add one live-state artifact so runtime facts have a canonical landing zone.
3. Implement rendered/validated config generation.
4. Add local reconciliation from OpenClaw runtime into repo state.
5. Add memory synthesis loop.
6. Only then stage the next engineering pass for ontology/exocortex bridge design.

---

## Why This Order

If you build ontology before repo truth is coherent, you create a second lie.

If you add memory systems before synthesis exists, you create duplication.

If you leave current docs stale while implementing new config architecture, every agent keeps reasoning from contradictory premises.

So the order is:
- truth
- config
- reconciliation
- synthesis
- ontology

Not the reverse.

---

## Immediate Next Task

The first actual repo task should be:

**Reconcile current source-of-truth docs and add a live-state artifact, then implement the config scaffold.**

That is the highest-leverage sequence with the lowest architectural regret.
