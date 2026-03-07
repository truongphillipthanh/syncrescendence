# Response

**Response ID**: `RSP-20260306-codex-swarm-wave-2-lane-00-coordinator`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-2-lane-00-coordinator`
**Result state**: `complete`

## 1. Convergence Map Across Wave 2 Lanes

| Lane | Draft contribution | Converged use in the next pass |
| --- | --- | --- |
| 01 `KNOWLEDGE-COMPATIBILITY` | identifies the four live-facing knowledge docs that still teach bare `knowledge/references/` as a sovereign lane | include all four docs in the next direct-write pass |
| 02 `COMMS-DISPATCH-CLEANUP` | identifies the minimum communications-facing docs that still omit `communications/dispatches/` | include `communications/README.md`, `AGENTS.md`, and `WORK-LOOP.md`; merge its root README edits with Lane 01 and Lane 07 |
| 03 `REGISTRY-SEED-NORMALIZATION` | produces the authoritative schema-valid draft rows and keeps them at `adjudicated` | treat this as the seed/custody source of truth; do not populate the live registry yet |
| 04 `FIRST-CUSTODY-ARTIFACTS` | usefully sketches manifest and receipt shapes, but against stale seed assumptions | keep only as a draft pattern source; do not direct-write it without Lane 03 re-alignment |
| 05 `SIGMA-SUBTREE-SYNC` | bounds a safe first `knowledge/references/*` to `knowledge/sigma/references/*` sync tranche with receipts | defer execution to a later wave after compatibility notes and custody artifacts are ready |
| 06 `VALIDATOR-NORMALIZATION` | defines a thin validator posture tied to the ratified schema and custody law | defer implementation; use only as the enforcement split for a later tooling wave |
| 07 `MACRO-DRIFT-SCAN` | adds the missing macro anchor and highlights root/front-door drift | merge its macro wording into the same README cleanup pass, but do not expand scope beyond the top entry surfaces |

## 2. Collision Map

| Collision | Impacted lanes | Why material | Coordinator adjudication |
| --- | --- | --- | --- |
| Seed rows versus custody joins | 03, 04 | Lane 03 uses schema-valid `tdc-*` ids, tributary-root-relative `source_path`, `mf-*` family ids, and `record_state=adjudicated`; Lane 04 uses stale ids, different path forms, `mf-lineage-dual-witness-v1`, speculative promotion targets, and `record_state=scheduled` | Lane 03 wins. Lane 04 must be regenerated against Lane 03 before any manifest, receipt, or registry write occurs. |
| Speculative destination artifacts | 03, 04 | Lane 04 promotes memory, context-transition, and research-protocol families into files that do not exist in the live repo; Lane 03 correctly falls back to `retain_pedigree_rehoused` for those families | Lane 03 wins. Only the artifact-protocol family currently has a real live successor artifact. |
| Root README patch overlap | 01, 02, 07 | all three lanes touch `README.md`, but for different reasons: Sigma wording, dispatch wording, and macro anchor | merge into one root README edit in a single pass; do not stack competing patches. |
| Communications scope overlap | 02, 07 | both lanes target `communications/README.md`; Lane 02 fixes dispatch semantics while Lane 07 fixes stale `neosyncrescendence` and `future-lane` wording plus macro framing | merge both; they are complementary, not contradictory. |
| Sigma compatibility versus physical sync timing | 01, 05 | Lane 01 wants semantics corrected immediately; Lane 05 wants a later physical sync into `knowledge/sigma/references/` | correct semantics now, defer physical sync until manifest-and-receipt execution is authorized. |
| Validator timing | 03, 06 | Lane 06 is ready to validate structure, but the registry is still header-only and the custody set is not yet executed | keep validators out of the smallest pass; do not let tooling outrun live artifacts. |

## 3. Exact Smallest Safe Direct-Write Pass

The current repo already has the Wave 1 control plane, law files, `knowledge/sigma/`, and `communications/dispatches/`.

The smallest safe Wave 2 pass is therefore a live-facing compatibility cleanup only:

1. Update `knowledge/README.md`.
   - teach `knowledge/sigma/` as the live secondary tier
   - label `knowledge/references/` as compatibility housing for `knowledge/sigma/references/`
2. Update `knowledge/feedstock/README.md`.
   - route compaction to `knowledge/sigma/references/`
   - note promotion into `knowledge/sigma/`
   - preserve the current `knowledge/references/` tree as compatibility wording only
3. Update `knowledge/references/README.md`.
   - state explicitly that this is compatibility housing, not an independent sovereign lane
4. Update `communications/README.md`.
   - add `dispatches` to the lane map
   - replace stale `neosyncrescendence` and `future-lane` framing
   - add the macro split sentence: repo ratifies, exocortex coordinates, ontology projects
5. Update `README.md`.
   - add the macro doctrine anchor
   - expand the `communications/` bullet to include dispatches and retros
   - expand the `knowledge/` bullet to include Sigma
   - relabel `knowledge/references/neocorpus` as a compatibility path for Sigma references
6. Update `AGENTS.md`.
   - add `dispatches` to the one-artifact-one-class invariant
   - add `dispatches` to the `communications/` lane summary
7. Update `WORK-LOOP.md`.
   - change the metabolic rule to `prompts, responses, dispatches, and handoffs belong in communications lineage`
   - optionally add the narrow note that dispatch artifacts are for durable routing and receipt state, not every prompt

Explicit exclusions from the smallest safe pass:

- do not populate `orchestration/state/registry/tributary-disposition-registry.csv`
- do not write ledger events into `orchestration/state/registry/tributary-disposition-ledger.jsonl`
- do not write the Lane 04 manifests or receipts without first reconciling them to Lane 03
- do not create `knowledge/sigma/references/` or start the subtree sync in the same pass
- do not implement validator code or make the thin validator pack mandatory
- do not expand this pass to `BOOT.md` or `executive/README.md`; those are useful but secondary

## 4. Reasoning-Level-Aware Coordination Notes

- `extra high` Lane 03 overrides `high` Lane 04 on any seed-row, family-id, path-shape, or `record_state` dispute.
- `high` Lane 01 and `medium` Lane 02 define the minimum compatibility write set because they point at still-drifting live docs and align with the current repo state.
- `medium` Lane 07 is admitted only where it tightens front-door wording without enlarging the pass; its macro-anchor recommendations are adopted for `README.md` and `communications/README.md`, but its `BOOT.md` and `executive/README.md` suggestions stay deferred.
- `high` Lane 05 and `medium` Lane 06 remain downstream because both depend on post-cleanup execution state that does not yet exist in the repo.

## 5. Recommended Follow-On Waves

### Wave 3: Seed/Custody Re-Alignment

- regenerate the Lane 04 manifest and receipt drafts from the Lane 03 normalized rows
- keep memory, context-transition, research-protocols, and lineage families out of speculative promotion targets
- decide whether custody artifacts are being drafted as planning artifacts or executed as actual events before assigning `record_state`

### Wave 4: First Lawful Registry Population

- accept one hash serialization convention for `source_relpath_hash`
- insert only schema-valid Lane 03 rows
- keep rows out of the live registry until the linked custody artifacts are real and joinable

### Wave 5: Bounded Sigma Subtree Sync

- write the tranche manifest first
- create the four subtree/root receipts from Lane 05
- then mirror the bounded 39-file tranche into `knowledge/sigma/references/`
- keep `knowledge/references/` live as compatibility housing after the sync

### Wave 6: Thin Validator Rollout

- implement only hard-fail structural checks from Lane 06
- keep semantic adjudication, auto-repair, and migration logic out of scope

### Optional Front-Door Cleanup

- patch `BOOT.md` and `executive/README.md` with the macro anchor if a later orientation pass is already open

## 6. Status

`partial`

The coordinator synthesis is complete, and the smallest safe direct-write pass is merge-ready.

Wave 2 as a whole is only partially merge-ready because:

- the README compatibility cleanup is ready now
- the seed/custody package still has a real Lane 03 versus Lane 04 collision
- the registry remains intentionally unpopulated
- the Sigma subtree sync and validator rollout are still sequenced behind those earlier gates
