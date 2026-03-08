# MANIFEST-sigma-subtree-sync-tranche-01-20260306

```yaml
manifest_id: MANIFEST-sigma-subtree-sync-tranche-01-20260306-01
manifest_type: tranche
label: "Sigma subtree sync tranche 01 mirrored into housed compatibility destination"
source_tributary: syncrescendence
source_root: knowledge/references
source_scope:
  - knowledge/references/README.md
  - knowledge/references/NEOCORPUS-CATEGORY-INDEX-v1.md
  - knowledge/references/NEOCORPUS-INTERNALIZATION-v1.md
  - knowledge/references/neocorpus/claude-code/**
  - knowledge/references/neocorpus/multi-agent-systems/**
  - knowledge/references/neocorpus/prompt-engineering/**
created_at_utc: "2026-03-08T06:51:12Z"
created_by: codex_parallel_session
disposition_status: compatibility_mirror_written
authority_status: not-live-authority
cautionary_status: none
summary: "Mirror the bounded 39-file tranche from knowledge/references into knowledge/sigma/references while keeping the source tree live as compatibility housing."
artifact_classes:
  - reference-root-metadata
  - reference-subtree
receipt_links:
  - pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-root-metadata-20260306.md
  - pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-claude-code-20260306.md
  - pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-multi-agent-systems-20260306.md
  - pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-prompt-engineering-20260306.md
external_pointers: []
retained_derivatives:
  - knowledge/sigma/references/README.md
  - knowledge/sigma/references/NEOCORPUS-CATEGORY-INDEX-v1.md
  - knowledge/sigma/references/NEOCORPUS-INTERNALIZATION-v1.md
  - knowledge/sigma/references/neocorpus/claude-code/**
  - knowledge/sigma/references/neocorpus/multi-agent-systems/**
  - knowledge/sigma/references/neocorpus/prompt-engineering/**
notes_on_ambiguity: []
compatibility_rule: "knowledge/references remains live as the compatibility form of knowledge/sigma/references after this tranche."
included_counts:
  root_metadata_files: 3
  claude_code_files: 14
  multi_agent_systems_files: 18
  prompt_engineering_files: 4
  total_files: 39
verification_summary:
  root_metadata:
    source_file_count: 3
    destination_file_count: 3
    sha256_pairwise_status: match
  claude_code:
    source_file_count: 14
    destination_file_count: 14
    parity_status: match
  multi_agent_systems:
    source_file_count: 18
    destination_file_count: 18
    parity_status: match
  prompt_engineering:
    source_file_count: 4
    destination_file_count: 4
    parity_status: match
excluded_scope:
  - knowledge/references/neocorpus/openclaw/**
  - knowledge/references/neocorpus/ai-memory-retrieval/**
  - knowledge/references/neocorpus/infrastructure/**
  - all other knowledge/references/** material not named in source_scope
covered_scopes:
  - receipt_path: pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-root-metadata-20260306.md
    source_scope:
      - knowledge/references/README.md
      - knowledge/references/NEOCORPUS-CATEGORY-INDEX-v1.md
      - knowledge/references/NEOCORPUS-INTERNALIZATION-v1.md
    destination_scope:
      - knowledge/sigma/references/README.md
      - knowledge/sigma/references/NEOCORPUS-CATEGORY-INDEX-v1.md
      - knowledge/sigma/references/NEOCORPUS-INTERNALIZATION-v1.md
    file_count: 3
  - receipt_path: pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-claude-code-20260306.md
    source_scope:
      - knowledge/references/neocorpus/claude-code/**
    destination_scope:
      - knowledge/sigma/references/neocorpus/claude-code/**
    file_count: 14
  - receipt_path: pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-multi-agent-systems-20260306.md
    source_scope:
      - knowledge/references/neocorpus/multi-agent-systems/**
    destination_scope:
      - knowledge/sigma/references/neocorpus/multi-agent-systems/**
    file_count: 18
  - receipt_path: pedigree/rehousing-receipts/RECEIPT-sigma-subtree-sync-tranche-01-prompt-engineering-20260306.md
    source_scope:
      - knowledge/references/neocorpus/prompt-engineering/**
    destination_scope:
      - knowledge/sigma/references/neocorpus/prompt-engineering/**
    file_count: 4
```
