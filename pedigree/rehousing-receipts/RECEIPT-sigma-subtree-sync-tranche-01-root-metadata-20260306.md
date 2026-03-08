# RECEIPT-sigma-subtree-sync-tranche-01-root-metadata-20260306

```yaml
receipt_id: RECEIPT-sigma-subtree-sync-tranche-01-root-metadata-20260306-01
receipt_type: subtree-sync
label: "Mirror Sigma tranche 01 root metadata into housed compatibility destination"
timestamp_utc: "2026-03-08T06:51:12Z"
actor: codex_parallel_session
source_path:
  - knowledge/references/README.md
  - knowledge/references/NEOCORPUS-CATEGORY-INDEX-v1.md
  - knowledge/references/NEOCORPUS-INTERNALIZATION-v1.md
destination_path:
  - knowledge/sigma/references/README.md
  - knowledge/sigma/references/NEOCORPUS-CATEGORY-INDEX-v1.md
  - knowledge/sigma/references/NEOCORPUS-INTERNALIZATION-v1.md
artifact_class: reference-root-metadata
reason: "Materialize the Sigma housed root metadata for tranche 01 while preserving knowledge/references as the live compatibility housing."
disposition: compatibility_mirror_written
authority_status: not-live-authority
cautionary_status: none
content_integrity: exact-copy
related_manifest: pedigree/archive-manifests/MANIFEST-sigma-subtree-sync-tranche-01-20260306.md
compatibility_statement: "The source files remain live at knowledge/references after this sync as the compatibility form of knowledge/sigma/references."
notes_on_execution:
  - "The destination files were copied without editing source or destination content."
  - "Pairwise SHA-256 hashes match for all three mirrored files."
parity_witness:
  verification_mode: sha256_pairwise_plus_count_equality
  source_file_count: 3
  destination_file_count: 3
  status: counts-and-hashes-match
  files:
    - relative_path: README.md
      source_sha256: f9c684385ab845adb407111cc7c12f13cc08f886fe13c14645fa0b8d3ff686e6
      destination_sha256: f9c684385ab845adb407111cc7c12f13cc08f886fe13c14645fa0b8d3ff686e6
    - relative_path: NEOCORPUS-CATEGORY-INDEX-v1.md
      source_sha256: fbfe37aacb34d18e8c05d02b2d2de7fdc9699d98a16a51fc6de03d62f1d2d9d2
      destination_sha256: fbfe37aacb34d18e8c05d02b2d2de7fdc9699d98a16a51fc6de03d62f1d2d9d2
    - relative_path: NEOCORPUS-INTERNALIZATION-v1.md
      source_sha256: ccc865ecb621682ec4d32261e31a19bd7644e8e9bd4ea09c293e1fa08b4d8454
      destination_sha256: ccc865ecb621682ec4d32261e31a19bd7644e8e9bd4ea09c293e1fa08b4d8454
```
