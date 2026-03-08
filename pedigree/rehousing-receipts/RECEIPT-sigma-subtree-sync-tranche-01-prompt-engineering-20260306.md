# RECEIPT-sigma-subtree-sync-tranche-01-prompt-engineering-20260306

```yaml
receipt_id: RECEIPT-sigma-subtree-sync-tranche-01-prompt-engineering-20260306-01
receipt_type: subtree-sync
label: "Mirror Sigma tranche 01 prompt-engineering subtree into housed compatibility destination"
timestamp_utc: "2026-03-08T06:51:12Z"
actor: codex_parallel_session
source_root: knowledge/references/neocorpus/prompt-engineering
destination_root: knowledge/sigma/references/neocorpus/prompt-engineering
artifact_class: reference-subtree
reason: "Mirror the bounded prompt-engineering reference subtree into Sigma housing while leaving the source tree live as compatibility housing."
disposition: compatibility_mirror_written
authority_status: not-live-authority
cautionary_status: none
content_integrity: exact-copy
related_manifest: pedigree/archive-manifests/MANIFEST-sigma-subtree-sync-tranche-01-20260306.md
compatibility_statement: "The source subtree remains live at knowledge/references/neocorpus/prompt-engineering after this sync as compatibility housing."
notes_on_execution:
  - "Verification used source and destination file counts plus a clean diff -qr result."
parity_witness:
  verification_mode: relative_file_inventory_plus_diff_qr
  source_file_count: 4
  destination_file_count: 4
  diff_qr_status: clean
  status: counts-and-content-match
  mirrored_files:
    - constellation-prompting-formulas.md
    - context-engineering-post-prompt-paradigm.md
    - prompt-architecture-structural-design.md
    - prompt-optimization-production-rigor.md
```
