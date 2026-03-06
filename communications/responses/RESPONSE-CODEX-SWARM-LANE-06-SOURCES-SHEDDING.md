# Response

**Response ID**: `RSP-20260306-sources-shedding`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-lane-06-sources-shedding`
**Result state**: `complete`
**Receipt artifacts**:
  - `communications/responses/RESPONSE-CODEX-SWARM-LANE-06-SOURCES-SHEDDING.md`
  - `orchestration/state/impl/TRIBUTARY-UNIFICATION-AND-COMPACTION-v1.md`
  - `orchestration/state/impl/EXOCORTEX-CONTROL-PLANE-CC91.md`
  - `pedigree/archive-manifests/pre-schematic-design.md`

## Returned Content

The repo should stop behaving like the primary residence of raw source mass. The inspected tributaries already show the right split:

- the live repo is small and high-yield: `knowledge/references` is about 207 files, `pedigree` about 75 files, `knowledge/feedstock` about 17 files
- the historical burden is concentrated elsewhere: `corpus` is about 6,310 files / 97 MB and `04-SOURCES` about 2,218 files / 28 MB
- the repo already has a lawful pattern for manifests and receipts under `pedigree/archive-manifests/`, `pedigree/rehousing-receipts/`, and `knowledge/feedstock/receipts/`

The shedding policy should therefore treat source and log matter as a disposition problem with four primary outcomes:

1. `retain_live_reference`
   Use when the artifact is already compacted into a durable lesson, reference, runbook, law, receipt, or manifest that is actively queryable in the successor shell.
2. `externalize_with_manifest`
   Use when the artifact body still matters, but mostly as reserve material. Move the raw body to exocortex or external archive storage and keep an in-repo manifest, pointer, provenance fields, and promotion history.
3. `compact_then_externalize`
   Use when raw matter still has unrealized yield. First extract a bounded lesson, synthesis, or topic reference; then externalize the raw body and retain only the compacted derivative plus manifest.
4. `cull_with_receipt`
   Use when the artifact has low present yield, low uniqueness, and no active doctrinal or evidentiary role. Delete the local body only after recording a durable receipt.

## Disposition Policy For Old Sources And Old Logs

### Old source bodies

Raw source bodies should not remain in-repo merely because they were once collected. Keep in-repo only:

- compacted references and extracted lessons
- manifests that describe archived families
- receipts showing how, when, and why a body was moved or culled
- a thin set of provenance-critical exemplars

Default rule for old source bodies:

- if already represented by a neocorpus or reference synthesis, `externalize_with_manifest`
- if not yet represented but still strategically dense, `compact_then_externalize`
- if strategically stale, duplicative, or low-signal, `cull_with_receipt`

### Old logs

Logs should be treated more aggressively than sources because they usually carry less reusable epistemic density and more sediment.

Keep in-repo only logs that are:

- legal or operational receipts
- irreplaceable provenance for a migration, rehousing, or verification event
- the minimal exemplars needed to reconstruct how a doctrine or operator emerged

Everything else should be:

- compacted into summaries if it still teaches something
- externalized if it may need occasional forensic access
- culled with receipt if it is exhausted conversational exhaust

## Criteria For What Remains In-Repo Vs What Becomes Exocortex Or External Storage

### Remains in-repo

An artifact family should remain in-repo when at least one of these is true:

- it is a compacted lesson rather than a raw body
- it is a manifest, receipt, registry, promotion ledger, or disposition record
- it is current law, runbook, or control-plane state
- it is a provenance anchor needed to defend how a live artifact was derived
- it is small, high-value, and repeatedly consulted

This matches the current high-yield families already visible in the shell:

- `knowledge/references/neocorpus/*`
- `pedigree/archive-manifests/*`
- `pedigree/rehousing-receipts/*`
- `pedigree/originals/*`
- `knowledge/feedstock/receipts/*`
- current implementation runbooks and control-plane artifacts such as `EXOCORTEX-CONTROL-PLANE-CC91.md`

### Becomes exocortex or external storage with manifest

A family should be externalized when most of the retained value is reserve access rather than daily live use. Externalization is appropriate when:

- the family is large and flat
- the family is mostly raw source bodies or historical logs
- the family has already yielded compacted references, lessons, or runbooks
- provenance matters, but local residency does not
- retrieval can be mediated by manifest plus pointer instead of by direct repo presence

Minimum manifest payload for an externalized family:

- source tributary
- original root/path or path pattern
- artifact family name
- count and size at time of move
- disposition date
- external location pointer
- promotion/compaction status
- retained in-repo derivatives
- rationale

## Criteria For `cull_with_receipt`

`cull_with_receipt` is lawful only when all of the following hold:

1. the artifact is a raw body or exhausted log, not a compacted lesson
2. it has no live operational, legal, or constitutional role
3. it is duplicative, superseded, or recoverable from another authoritative location
4. its epistemic payload has either already been extracted or judged too low to justify compaction
5. provenance can still be reconstructed from the receipt and any retained manifest

Each cull receipt should minimally preserve:

- artifact or family identifier
- original location
- class: source, log, transcript, notebook, scratch, duplicate
- date culled
- culling rationale
- whether extraction existed before cull
- replacement artifact if one exists
- operator or lane responsible

`cull_with_receipt` should be the default for:

- duplicate raw captures
- stale scratch logs and dead-end audit traces
- conversational exhaust with no unique findings
- old source bodies whose lessons already exist in `knowledge/references` or stronger synthesis

It should not be used for:

- manifests
- receipts
- original exemplars
- lineage documents that explain major architectural turns
- unique notebooks whose synthesis has not yet been promoted

## Top Candidate Families For Immediate Shedding

These are the strongest immediate shedding candidates because they are high-volume, mostly raw, and already appear at least partly compacted elsewhere.

1. `corpus` raw source families in dense topical clusters already represented in `knowledge/references/neocorpus/`
   Strongest examples: `02S-multi-agent-systems` with 1,977 files, `01F-ai-models` with 1,166 files, `02S-claude-code` with 339 files, `03P-openclaw` with 284 files, `01F-prompt-engineering` with 109 files, `03P-vibe-coding` with 129 files.
   Policy: keep the neocorpus references in-repo; externalize the raw corpus bodies by family with manifests.
2. `corpus` status-heavy signal and research matter that has not been promoted into durable law
   The atlas shows 4,090 `1-signal` files and 971 `3-research` files. These are the first place where historical inertia can masquerade as importance.
   Policy: if a family lacks a derivative reference after triage, compact a small subset and externalize or cull the rest.
3. `corpus` handoff, audit, and adjudication chains
   Sample naming patterns include `handoff-*` and `audit-*`, indicating conversational and process sediment rather than durable doctrine.
   Policy: preserve only summary derivatives and receipts; cull or externalize the raw chains.
4. `04-SOURCES/research-notebooks`
   This subtree alone carries about 441 files across topic notebooks.
   Policy: keep promoted syntheses and exceptional notebooks with unique framework value; externalize the bulk notebook bodies with notebook-level manifests.
5. `04-SOURCES/research`
   This subtree carries about 95 files and functions as earlier intake bulk.
   Policy: fold any still-useful matter into feedstock or references, then externalize the raw family.
6. Legacy processed and index sediment under `04-SOURCES/processed`, `_meta`, and `_index`
   These are transitional scaffolds from an earlier shell, not appropriate as permanent live burden.
   Policy: preserve family-level manifests and selected reconciliation receipts, then cull or externalize the rest.

## Top Candidate Families That Must Remain

These families should remain in-repo because they carry either high epistemic yield in compacted form or irreplaceable provenance.

1. `knowledge/references/neocorpus/*`
   This is the extracted lesson layer. It is already the right replacement for raw source warehousing.
2. `pedigree/archive-manifests/*`
   These are the durable receipts for offloaded tributaries and are required for provenance-preserving shedding.
3. `pedigree/rehousing-receipts/*` and `knowledge/feedstock/receipts/*`
   These establish the chain of custody for movement, ingestion, and transformation.
4. `pedigree/originals/*`
   The set is small and functions as authenticity reserve. This is exactly the kind of thin exemplar layer that should survive even after broad shedding.
5. Tributary lineage and migration law documents
   Especially `TRIBUTARY-UNIFICATION-AND-COMPACTION-v1.md` and related implementation doctrine, because these documents explain why disposition decisions were lawful.
6. Current control-plane manifests, status artifacts, and runbooks
   Especially the CC91 family, because it is active operational provenance, not historical sediment.
7. Any unique notebook or source family whose synthesis has not yet been promoted and still carries distinct frameworks unavailable elsewhere
   In practice this is a small exception class, not a license to keep entire directories live.

## Net Policy

The repo should retain receipts, manifests, compacted references, promotion history, and a thin authenticity reserve. Raw source bodies and exhausted logs should leave the live shell unless they are still awaiting first-order compaction or carry singular provenance value.

The near-term shedding order should be:

1. externalize dense raw `corpus` families that already have neocorpus coverage
2. externalize or cull `handoff-*`, `audit-*`, and similar process sediment in `corpus`
3. externalize most of `04-SOURCES/research-notebooks` and `04-SOURCES/research` behind notebook-level and family-level manifests
4. preserve and strengthen the in-repo manifest and receipt layer so every shedding act remains queryable

The crucial distinction is simple:

- source bodies and logs are burden unless still yielding
- extracted lessons, manifests, and receipts are institutional memory and must remain
