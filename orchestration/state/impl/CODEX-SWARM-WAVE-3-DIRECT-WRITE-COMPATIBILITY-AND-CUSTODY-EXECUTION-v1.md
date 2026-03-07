# Codex Swarm — Wave 3 Direct-Write Compatibility And Custody Execution v1

**Date**: 2026-03-06
**Status**: staged
**Purpose**: execute the smallest safe direct-write wave after Wave 2 synthesis without prematurely populating the live registry

## 0. Why Wave 3 Exists

Wave 2 finished the interpretive work.

The repo now has enough agreement to stop drafting around the real work and to perform the first bounded write wave:

- correct the live-facing front doors
- make the first custody artifacts real
- preserve the first retained witnesses under `pedigree/rehoused/`
- execute the first bounded Sigma reference mirror
- clarify the hash convention that will later govern registry population

Primary anchors:

- [SYNCRESCENDENCE-HOLISTIC-STRATEGIC-ENDEAVOR-v1.md](/Users/system/syncrescendence/knowledge/canon/SYNCRESCENDENCE-HOLISTIC-STRATEGIC-ENDEAVOR-v1.md)
- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md)

## 1. Recommended Parallelism

Recommended:

- `6` core worker lanes
- `1` optional front-door macro lane
- `1` optional schema-clarification lane
- `1` coordinator lane

## 2. Wave 3 Swarm Law

All sessions must obey:

1. direct-write only the files explicitly assigned to your lane
2. also write only your assigned response artifact under `communications/responses/`
3. do not edit the live registry CSV or ledger JSONL in this wave
4. do not change contract-law conclusions from Waves 1 and 2 unless a direct repo contradiction forces it
5. use repo-relative paths in all manifests, receipts, and summaries
6. if you are copying preserved or mirrored bodies, preserve content exactly unless the packet explicitly authorizes wording cleanup
7. run `git diff --check` in your worktree before closing
8. if your assigned files collide with another lane, stop and report blocked rather than improvising a merge

## 3. Lane Set

### Lane 01 — Knowledge Compatibility Direct Write

Goal:

- directly patch the knowledge front doors so the repo stops teaching bare `knowledge/references/` as the sovereign secondary lane

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-01-KNOWLEDGE-COMPATIBILITY-DIRECT-WRITE.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-01-KNOWLEDGE-COMPATIBILITY-DIRECT-WRITE.md)

### Lane 02 — Root README Macro Cleanup

Goal:

- patch the root README so it names Sigma correctly, includes dispatches, and exposes the macro doctrine anchor

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-02-ROOT-README-MACRO-CLEANUP.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-02-ROOT-README-MACRO-CLEANUP.md)

### Lane 03 — Communications Direct Write

Goal:

- patch the communications front doors and constitutional summary surfaces so dispatches and communications lineage are taught correctly

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-03-COMMS-DISPATCH-DIRECT-WRITE.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-03-COMMS-DISPATCH-DIRECT-WRITE.md)

### Optional Lane 04 — Boot And Executive Macro Cleanup

Goal:

- patch `BOOT.md` and `executive/README.md` so stateless rehydration front doors name the macro doctrine and successor-shell role cleanly

Recommended reasoning:

- `medium`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-04-BOOT-EXECUTIVE-MACRO-CLEANUP.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-04-BOOT-EXECUTIVE-MACRO-CLEANUP.md)

### Lane 05 — First Custody Execution

Goal:

- make the first custody artifacts real by aligning manifests, receipts, and preserved copies exactly to the Wave 2 Lane 03 normalized rows

Recommended reasoning:

- `extra high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-05-FIRST-CUSTODY-EXECUTION.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-05-FIRST-CUSTODY-EXECUTION.md)

### Lane 06 — Sigma Subtree Sync Tranche 01 Execution

Goal:

- execute the bounded 39-file compatibility mirror into `knowledge/sigma/references/` with manifest and subtree receipts while preserving source-path liveliness

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-06-SIGMA-SUBTREE-SYNC-EXECUTION.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-06-SIGMA-SUBTREE-SYNC-EXECUTION.md)

### Optional Lane 07 — Registry Hash Convention Clarification

Goal:

- ratify the exact `source_relpath_hash` serialization in the schema and state the remaining gate before live registry population

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-07-REGISTRY-HASH-CONVENTION.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-07-REGISTRY-HASH-CONVENTION.md)

### Lane 00 — Coordinator

Goal:

- synthesize the direct-write wave, confirm what became real, and stage the next wave for live registry population and later validator rollout

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-3-LANE-00-COORDINATOR.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-3-LANE-00-COORDINATOR.md)

## 4. Launch Order

Recommended launch order:

1. Lane 01
2. Lane 02
3. Lane 03
4. Lane 05
5. Lane 06
6. optional Lane 04
7. optional Lane 07
8. Lane 00 last

## 5. Success Criteria

Wave 3 succeeds when:

- the live-facing READMEs and constitutional summaries stop teaching stale Sigma and dispatch topology
- the first retained witness families are actually present under `pedigree/rehoused/`
- the first custody manifests and receipts are real and joinable
- `knowledge/sigma/references/` exists as a bounded compatibility mirror with manifest and subtree receipts
- the hash convention blocking later registry population is explicit
- the next wave can focus on live registry population and later validator rollout rather than reopening compatibility law
