# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-06-sigma-subtree-sync-execution`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: execute the bounded 39-file compatibility mirror into `knowledge/sigma/references/` with manifest and subtree receipts while preserving source-path liveliness
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-06-SIGMA-SUBTREE-SYNC-EXECUTION.md`

## Decision Envelope

- **Trigger**: Wave 2 bounded a safe first Sigma sync tranche and explicitly kept it separate from broad neocorpus migration
- **Selected approach**: directly create the `knowledge/sigma/references/` mirror for tranche 01 plus one manifest and four subtree receipts
- **Alternatives considered**:
  - delaying the mirror until registry population — rejected because the mirror is operationally useful and already bounded
  - copying the whole `knowledge/references/` tree — rejected because it would outrun receipt discipline
- **Assumptions**:
  - the source tree remains live as compatibility housing after this pass
- **Inherited constraints**:
  - edit only the assigned files plus your response artifact
  - do not modify source files under `knowledge/references/`
  - do not rewrite citations or broader docs in this lane

## Assigned Live Files

Create or update exactly these targets:

- [knowledge/sigma/references/README.md](/Users/system/syncrescendence/knowledge/sigma/references/README.md)
- [knowledge/sigma/references/NEOCORPUS-CATEGORY-INDEX-v1.md](/Users/system/syncrescendence/knowledge/sigma/references/NEOCORPUS-CATEGORY-INDEX-v1.md)
- [knowledge/sigma/references/NEOCORPUS-INTERNALIZATION-v1.md](/Users/system/syncrescendence/knowledge/sigma/references/NEOCORPUS-INTERNALIZATION-v1.md)
- [knowledge/sigma/references/neocorpus/claude-code](/Users/system/syncrescendence/knowledge/sigma/references/neocorpus/claude-code)
- [knowledge/sigma/references/neocorpus/multi-agent-systems](/Users/system/syncrescendence/knowledge/sigma/references/neocorpus/multi-agent-systems)
- [knowledge/sigma/references/neocorpus/prompt-engineering](/Users/system/syncrescendence/knowledge/sigma/references/neocorpus/prompt-engineering)
- [pedigree/archive-manifests/MANIFEST-sigma-subtree-sync-tranche-01-20260306.md](/Users/system/syncrescendence/pedigree/archive-manifests/MANIFEST-sigma-subtree-sync-tranche-01-20260306.md)
- [pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-root-metadata-20260306.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-root-metadata-20260306.md)
- [pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-claude-code-20260306.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-claude-code-20260306.md)
- [pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-multi-agent-systems-20260306.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-multi-agent-systems-20260306.md)
- [pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-prompt-engineering-20260306.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-prompt-engineering-20260306.md)

## Anchors

- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-05-SIGMA-SUBTREE-SYNC.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-05-SIGMA-SUBTREE-SYNC.md)
- [PEDIGREE-CUSTODY-LAW-v1.md](/Users/system/syncrescendence/pedigree/PEDIGREE-CUSTODY-LAW-v1.md)

## Required Output

1. mirror exactly the bounded tranche identified in Wave 2:
   - the three root metadata files
   - `knowledge/references/neocorpus/claude-code/**`
   - `knowledge/references/neocorpus/multi-agent-systems/**`
   - `knowledge/references/neocorpus/prompt-engineering/**`
2. do not alter the source files
3. create the tranche manifest and four subtree receipts
4. state clearly in the manifest and receipts that the source tree remains live as compatibility housing
5. verify destination counts against source counts for each included subtree
6. write a short response artifact listing copied file counts, created artifacts, and validation run
7. run `git diff --check`
8. report `complete / partial / blocked`
