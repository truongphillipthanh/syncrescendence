# Codex Swarm — Tributary Unification v1

**Date**: 2026-03-06  
**Status**: operator-side swarm coordination design  
**Purpose**: define a safe faux-worktree fan-out strategy for parallel Codex sessions working on tributary unification and compaction

---

## 0. Why This Exists

The shell now has enough structure that multiple Codex sessions can productively work in parallel.

What it does not yet have is native in-session swarming.

The correct workaround is:

**manual multi-session fan-out with strict write isolation, unique return paths, and one coordinator session responsible for synthesis.**

This document defines:

- how many lanes are feasible
- which lanes can run in parallel
- what each lane should read
- what each lane is allowed to write
- where each lane returns its output

---

## 1. Feasible Parallelism

### Conservative

- `4` worker lanes
- `1` coordinator lane

Use this when:

- you want low merge pressure
- the shell is already busy with other active work
- you want high confidence and low coordination overhead

### Recommended

- `6` worker lanes
- `1` coordinator lane

This is the current sweet spot.

Why:

- enough differentiation to split the tributaries meaningfully
- low enough write pressure to avoid stepping on shared files
- high enough parallelism to materially accelerate the bridge

### Optional Extension

- `+1` exocortex/ontology lane

Use this if you want to pull future-facing externalization and registry design forward in parallel with the doctrinal bridge.

### Hard Ceiling Without Real Worktrees

- `8` worker lanes
- `1` coordinator lane

Beyond this, coordination cost, duplicate reading, and response integration burden will likely outrun throughput gains.

---

## 2. Swarm Law

All swarm sessions must obey these rules.

1. Each session writes to exactly one assigned response file.
2. No worker session edits shared law, backlog, or root files.
3. No worker session commits, rebases, or branches.
4. No worker session runs broad mutation commands or generators.
5. Every claim must cite the actual repo path(s) it depends on.
6. If uncertain, mark uncertainty explicitly instead of smoothing it away.
7. The current shell remains the receiver; no lane may propose reviving predecessor topology wholesale.

The coordinator lane may later propose actual integration edits, but should still avoid writing outside its own assigned response file during the first pass.

---

## 3. Write Isolation

All worker lanes are read-heavy and write-light.

Each lane writes only to:

- one unique file in [communications/responses](/Users/system/syncrescendence/communications/responses)

This keeps the sessions from colliding while still preserving lawful lineage.

---

## 4. Core Lane Set

### Lane 01 — Receiver Fit

Purpose:

- map the current shell’s receiving capacity
- identify missing destination surfaces
- determine where tributary artifacts should land in the present architecture

Packet:

- [PACKET-CODEX-SWARM-LANE-01-RECEIVER-FIT.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-01-RECEIVER-FIT.md)

### Lane 02 — Pre-Schematic Doctrine

Purpose:

- mine `neocanon`, `neocorpus`, and `neosyncrescendence`
- identify what should become live law, live reference, or pedigree

Packet:

- [PACKET-CODEX-SWARM-LANE-02-PRE-SCHEMATIC-DOCTRINE.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-02-PRE-SCHEMATIC-DOCTRINE.md)

### Lane 03 — Old Canon Authenticity

Purpose:

- triage `01-CANON`
- preserve authentic doctrine and identify stale or superseded zones

Packet:

- [PACKET-CODEX-SWARM-LANE-03-OLD-CANON-AUTHENTICITY.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-03-OLD-CANON-AUTHENTICITY.md)

### Lane 04 — Sigma and Orchestration Compaction

Purpose:

- triage `05-SIGMA`, `00-ORCHESTRATION`, and select `02-ENGINE` material
- identify playbook, validated-pattern, and operator candidates

Packet:

- [PACKET-CODEX-SWARM-LANE-04-SIGMA-AND-ORCHESTRATION.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-04-SIGMA-AND-ORCHESTRATION.md)

### Lane 05 — Sovereign and Offices

Purpose:

- triage `-SOVEREIGN`, `agents`, `-INBOX`, `-OUTBOX`, and `collab`
- identify what becomes executive, office, communications, or pedigree matter

Packet:

- [PACKET-CODEX-SWARM-LANE-05-SOVEREIGN-AND-OFFICES.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-05-SOVEREIGN-AND-OFFICES.md)

### Lane 06 — Sources and Shedding

Purpose:

- triage `04-SOURCES` and large corpus-like raw source sediment
- define what should remain feedstock/reference, what should be externalized, and what should be culled with receipts

Packet:

- [PACKET-CODEX-SWARM-LANE-06-SOURCES-SHEDDING.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-06-SOURCES-SHEDDING.md)

### Optional Lane 07 — Exocortex and Ontology

Purpose:

- define how the connectorized exocortex and ontology projection become the future unifier of cognitive organs rather than a second canon

Packet:

- [PACKET-CODEX-SWARM-LANE-07-EXOCORTEX-ONTOLOGY.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-07-EXOCORTEX-ONTOLOGY.md)

### Lane 00 — Coordinator

Purpose:

- synthesize worker responses
- identify convergence, collisions, and next merge steps

Packet:

- [PACKET-CODEX-SWARM-LANE-00-COORDINATOR.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-LANE-00-COORDINATOR.md)

---

## 5. Launch Order

Recommended launch order:

1. Lane 01
2. Lane 02
3. Lane 03
4. Lane 04
5. Lane 05
6. Lane 06
7. optional Lane 07
8. Lane 00 last, once at least two worker responses exist

Reason:

- coordinator synthesis is better once some worker outputs have actually landed
- worker lanes are mostly independent

---

## 6. Integration Rule

The first swarm wave should not directly edit live law.

The first wave should produce:

- lane-local response artifacts
- candidate promotion lists
- disposition tables
- conflict reports
- open questions

Then a separate integration session can:

- compare the worker outputs
- resolve collisions
- draft actual repo deltas

This preserves quality and prevents swarm fan-out from turning into simultaneous governance edits.

---

## 7. Success Criteria

This swarm scaffold is successful when:

- multiple Codex sessions can run in parallel without trampling each other
- each lane returns one intelligible artifact
- the coordinator can synthesize those artifacts into a mergeable migration program
- tributary unification stops being a single-threaded burden

