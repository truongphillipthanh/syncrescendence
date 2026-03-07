# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-05-first-custody-execution`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: make the first custody artifacts real by aligning manifests, receipts, and preserved witness copies exactly to the Wave 2 Lane 03 normalized rows
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-05-FIRST-CUSTODY-EXECUTION.md`

## Decision Envelope

- **Trigger**: Wave 2 normalized the seed rows and showed that the earlier custody draft was stale; the next honest move is real custody execution, not more speculative drafting
- **Selected approach**: directly create the row-aligned manifests, receipts, and preserved copies required by the normalized seed families
- **Alternatives considered**:
  - populating the live registry first — rejected because receipts and preserved destinations must exist before registry insertion
  - preserving everything under one tranche manifest — rejected because the normalized rows already separate family identities and join paths
- **Assumptions**:
  - [RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md) is binding for ids, paths, families, and dispositions
- **Inherited constraints**:
  - edit only the assigned files plus your response artifact
  - do not touch the live registry CSV or ledger JSONL
  - do not invent new destination artifacts for memory, context-transition, research-protocols, or lineage

## Assigned Live Files

Create or update exactly these files:

- [pedigree/archive-manifests/MANIFEST-artifact-protocol-family-20260306.md](/Users/system/syncrescendence/pedigree/archive-manifests/MANIFEST-artifact-protocol-family-20260306.md)
- [pedigree/archive-manifests/MANIFEST-memory-architecture-family-20260306.md](/Users/system/syncrescendence/pedigree/archive-manifests/MANIFEST-memory-architecture-family-20260306.md)
- [pedigree/archive-manifests/MANIFEST-context-transition-family-20260306.md](/Users/system/syncrescendence/pedigree/archive-manifests/MANIFEST-context-transition-family-20260306.md)
- [pedigree/archive-manifests/MANIFEST-research-protocols-family-20260306.md](/Users/system/syncrescendence/pedigree/archive-manifests/MANIFEST-research-protocols-family-20260306.md)
- [pedigree/archive-manifests/MANIFEST-lineage-family-20260306.md](/Users/system/syncrescendence/pedigree/archive-manifests/MANIFEST-lineage-family-20260306.md)
- [pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md)
- [pedigree/rehousing-receipts/RECEIPT-preserve-copy-memory-architecture-20260306-02.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-preserve-copy-memory-architecture-20260306-02.md)
- [pedigree/rehousing-receipts/RECEIPT-preserve-copy-context-transition-20260306-03.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-preserve-copy-context-transition-20260306-03.md)
- [pedigree/rehousing-receipts/RECEIPT-preserve-copy-research-protocols-20260306-04.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-preserve-copy-research-protocols-20260306-04.md)
- [pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-20260306-05.md](/Users/system/syncrescendence/pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-20260306-05.md)
- [pedigree/rehoused/syncrescendence_old/01-CANON/CANON-25000-MEMORY_ARCH-lattice.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_old/01-CANON/CANON-25000-MEMORY_ARCH-lattice.md)
- [pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md)
- [pedigree/rehoused/syncrescendence_old/01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_old/01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md)
- [pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3005-CONTEXT_TRANSITION.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3005-CONTEXT_TRANSITION.md)
- [pedigree/rehoused/syncrescendence_old/01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_old/01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md)
- [pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3006-RESEARCH_PROTOCOLS.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3006-RESEARCH_PROTOCOLS.md)
- [pedigree/rehoused/syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md)
- [pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md](/Users/system/syncrescendence/pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md)

## Anchors

- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md)
- [PEDIGREE-CUSTODY-LAW-v1.md](/Users/system/syncrescendence/pedigree/PEDIGREE-CUSTODY-LAW-v1.md)
- [WITNESS-EXTERNALIZATION-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WITNESS-EXTERNALIZATION-LAW-v1.md)

## Required Output

1. create the manifests and receipts so they align exactly to the normalized Lane 03 rows
2. preserve the eight retained witness files under the exact `pedigree/rehoused/` paths listed above
3. use `authority_status: not-live-authority` and lawful cautionary metadata everywhere required
4. do not create speculative successor doctrine files for memory, context-transition, research-protocols, or lineage
5. keep the artifact-protocol family linked to the existing live law artifact rather than inventing a new derivative
6. write a short response artifact listing created files, copied witnesses, any ambiguity encountered, and validation run
7. run `git diff --check`
8. report `complete / partial / blocked`
