# Response

**Response ID**: `RSP-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization`
**Result state**: `complete`

## 1. Normalization Decisions

The first tranche can be normalized safely, but it should stop at `adjudicated` in draft form rather than being written directly into the live registry.

Applied normalizations:

1. `candidate_id` values are converted to schema-valid `tdc-*` ids.
2. `source_path` values are converted from absolute filesystem links to tributary-root-relative paths.
3. `merge_family_id` values are normalized to schema-valid `mf-*` family ids.
4. non-schema disposition language from the earlier seed draft is converted to exact registry enums.
5. families without a single already-ratified successor artifact are normalized to `retain_pedigree_rehoused` instead of being pointed at speculative canon or Sigma files.
6. all rows remain `adjudicated` so the control plane does not falsely imply that receipts or file moves already exist.

Hash convention used for this draft:

- `source_relpath_hash = sha256(<source_tributary>|<source_path>)`

This matches the schema requirement for deterministic hashing over tributary plus normalized source path while making the delimiter explicit for this tranche.

## 2. CSV-Ready Candidate Rows

```csv
candidate_id,schema_version,source_tributary,source_path,source_relpath_hash,artifact_class,artifact_format,lineage_witness,provenance_sensitivity,authority_score,present_relevance,compaction_yield,duplication_status,review_basis,chosen_disposition,destination_lane,destination_artifact_path,archive_manifest_path,receipt_path,external_pointer,merge_family_id,justification,record_state,intake_batch_id,last_action_at,last_action_by,dest_artifact_hash,supersedes_candidate_id,notes
tdc-artifact-protocol-old-0001,v1,syncrescendence_old,01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md,sha256:c2dff6201ffbf36bca98114762243ff8851aa53d5d4131efb3dd36e946251a01,law,md,family:artifact-protocol;role:old-explicit,low,5,5,4,duplicate_family,merged_adjudication,promote_live_law,orchestration/state/impl,orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md,pedigree/archive-manifests/MANIFEST-artifact-protocol-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md,none,mf-artifact-protocol-v1,Live artifact law already exists so this witness can be joined to a real successor artifact without inventing a new lane target.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,old-explicit-burden-witness
tdc-artifact-protocol-neo-0002,v1,syncrescendence_pre_schematic_design,neocanon/CANON-1003-ARTIFACT_PROTOCOL.md,sha256:c89bf7bff7b48036c27600f36d242606f587eab100c6de3257e8637590ef4a2a,law,md,family:artifact-protocol;role:neo-default,low,5,5,4,duplicate_family,merged_adjudication,promote_live_law,orchestration/state/impl,orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md,pedigree/archive-manifests/MANIFEST-artifact-protocol-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md,none,mf-artifact-protocol-v1,Neo is the default successor witness for a family already materially ratified in the live shell.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,neo-default-successor-witness
tdc-memory-architecture-old-0003,v1,syncrescendence_old,01-CANON/CANON-25000-MEMORY_ARCH-lattice.md,sha256:fd94c84ce02e0a4bd91e937858014930f99cafe14ce1baa4919e8d9dba4e0bb0,law,md,family:memory-architecture;role:old-explicit,low,5,4,4,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_old/01-CANON/CANON-25000-MEMORY_ARCH-lattice.md,pedigree/archive-manifests/MANIFEST-memory-architecture-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-memory-architecture-20260306-02.md,none,mf-memory-architecture-v1,The live shell has partial memory law but no single ratified successor artifact that can absorb this witness without overclaiming completion.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,old-witness-retained-until-shell-native-memory-artifact-exists
tdc-memory-architecture-neo-0004,v1,syncrescendence_pre_schematic_design,neocanon/CANON-3004-MEMORY_ARCHITECTURE.md,sha256:d2ed9c18ee7cf6c9734cfdbcf8fbcb70aa35e3b93109367bdc356ccd6a058c4b,law,md,family:memory-architecture;role:neo-default,low,5,4,4,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md,pedigree/archive-manifests/MANIFEST-memory-architecture-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-memory-architecture-20260306-02.md,none,mf-memory-architecture-v1,Neo is the preferred successor witness but the present shell still lacks one dedicated live destination artifact for the whole family.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,neo-witness-retained-until-shell-native-memory-artifact-exists
tdc-context-transition-old-0005,v1,syncrescendence_old,01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md,sha256:97d590f596f05ea58c013ca777b48ba7b9c356edd48cb7615d5641f4a88ac443,law,md,family:context-transition;role:old-explicit,low,4,5,4,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_old/01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md,pedigree/archive-manifests/MANIFEST-context-transition-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-context-transition-20260306-03.md,none,mf-context-transition-v1,Current communications law carries fragments of this family but not a full successor doctrine so custody retention is the honest first state.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,old-transition-taxonomy-must-remain-inspectable
tdc-context-transition-neo-0006,v1,syncrescendence_pre_schematic_design,neocanon/CANON-3005-CONTEXT_TRANSITION.md,sha256:6430bffea46a16cb749afc2355285a180f9354d0a26044132d5de025f895ab3c,law,md,family:context-transition;role:neo-default,low,4,5,4,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3005-CONTEXT_TRANSITION.md,pedigree/archive-manifests/MANIFEST-context-transition-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-context-transition-20260306-03.md,none,mf-context-transition-v1,Neo is the shell-fit witness but it should remain explicit in pedigree until a dedicated continuation artifact is ratified.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,neo-continuation-witness-retained-pending-live-artifact
tdc-research-protocols-old-0007,v1,syncrescendence_old,01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md,sha256:2bb8c00cd0935957f0c945a34883c5e74d7c945a0c6f615cb55c09556d84fdee,law,md,family:research-protocols;role:old-explicit,low,4,4,4,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_old/01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md,pedigree/archive-manifests/MANIFEST-research-protocols-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-research-protocols-20260306-04.md,none,mf-research-protocols-v1,The live shell has a knowledge lane contract but not a full ratified research doctrine so promotion would currently overstate completion.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,old-source-triad-and-threshold-detail-retained
tdc-research-protocols-neo-0008,v1,syncrescendence_pre_schematic_design,neocanon/CANON-3006-RESEARCH_PROTOCOLS.md,sha256:c627c00ff30b13be8f5a02175a7757136479f4429c439951fac1cfa96dfe6954,law,md,family:research-protocols;role:neo-default,low,4,4,4,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-3006-RESEARCH_PROTOCOLS.md,pedigree/archive-manifests/MANIFEST-research-protocols-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-research-protocols-20260306-04.md,none,mf-research-protocols-v1,Neo is the likely future Sigma anchor but today the lawful move is preservation with explicit witness identity rather than speculative promotion.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,neo-research-witness-retained-pending-dedicated-sigma-artifact
tdc-lineage-old-0009,v1,syncrescendence_old,01-CANON/CANON-00002-LINEAGE-cosmos.md,sha256:668e7b727fc15c088d3d6bfb058317e5ce5a6b5f112a44ed2ddf69e5834970a4,reference,md,family:lineage;role:old-explicit,medium,4,3,3,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md,pedigree/archive-manifests/MANIFEST-lineage-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-20260306-05.md,none,mf-lineage-v1,Lineage is custody-bearing ancestry rather than live law so the correct first move is explicit pedigree retention.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,old-tributary-debt-must-remain-visible
tdc-lineage-neo-0010,v1,syncrescendence_pre_schematic_design,neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md,sha256:a3b67d9192e798c1e0b389ceccc9266c8eb2935fddb18720e969eeed1f160c69,reference,md,family:lineage;role:neo-default,medium,4,3,3,duplicate_family,merged_adjudication,retain_pedigree_rehoused,pedigree/rehoused,pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md,pedigree/archive-manifests/MANIFEST-lineage-family-20260306.md,pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-20260306-05.md,none,mf-lineage-v1,Neo supplies the cleaner successor witness but ancestry should remain plural and inspectable under pedigree law.,adjudicated,PKT-20260306-codex-swarm-wave-2-lane-03-registry-seed-normalization,2026-03-06T23:54:30Z,codex_swarm.wave2.lane03,none,none,neo-lineage-summary-retained-without-erasing-old-witness
```

## 3. Why The Old Seed Draft Needed Correction

The earlier seed set was directionally right about which families matter first, but not yet safe for registry population.

The corrections are:

1. absolute desktop paths are replaced with normalized tributary-relative `source_path` values
2. non-schema ids such as `cand-*` are replaced with valid `tdc-*` identities
3. non-schema dual-witness family ids are replaced with `mf-*` values or removed
4. speculative targets such as future canon or Sigma files are removed unless a real ratified destination artifact already exists
5. dual-witness families that still lack one shell-native successor artifact are normalized to pedigree retention rather than false promotion

That yields a row set the schema can accept without pretending that Wave 2 has already executed custody moves or doctrinal compaction.

## 4. Top Failure Modes If Populated Prematurely Or Incorrectly

1. Writing the memory context or research families as live promotions now would falsely claim that dedicated successor artifacts already exist in the repo.
2. Carrying forward absolute source paths would make the control plane host-specific and break the repo-relative invariant.
3. Reusing non-schema disposition labels such as the older merge vocabulary would reintroduce validator drift into the authoritative registry.
4. Advancing these rows beyond `adjudicated` before receipts and manifests exist would overstate custody execution and break joinability with pedigree law.
5. Dropping the shared `mf-*` family ids would make sibling witnesses look unrelated and would erase the explicit dual-witness constraint the ratified witness law requires.
6. Treating the lineage family as promotable live doctrine would flatten ancestry into present authority and lose the custody boundary that `pedigree/` is supposed to enforce.
7. Using an inconsistent `source_relpath_hash` serialization across lanes would create duplicate-detection churn even if the visible paths are identical.

## 5. Status

`complete`

The first tranche is normalized into ten schema-valid draft rows. They are ready for the next wave to draft matching manifests and receipts, but they should not be inserted into the live registry until those custody artifacts exist and the hash serialization convention is accepted for the whole control plane.
