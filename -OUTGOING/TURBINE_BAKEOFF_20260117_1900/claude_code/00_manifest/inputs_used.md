# Inputs Used
**Generated**: 2026-01-17T19:00:00
**RUN_ID**: 20260117_1900

## Primary Inputs

### 1. DEFRAG_CONVICTION_PASS_20260117_1609
**Path**: `OUTGOING/DEFRAG_CONVICTION_PASS_20260117_1609/`
**Contents Read**:
- `00_manifest/` - Environment and repo state at pass time
- `01_convictions/` - System invariants and crashout prevention philosophy
- `02_inventory/` - Root orphan census and classification
- `03_obsolescence_and_duplicates/` - Files flagged for archive/merge
- `04_defrag_plan/` - 8-phase move-map with rationale
- `05_symbolic_compression/` - Compression rules for temporal content
- `06_patch_proposals/` - Suggested modifications
- `07_apply_scripts/` - defrag_apply.sh, defrag_rollback.sh
- `08_post_apply_verification/` - post_apply_verify.sh, checklist

### 2. 00-ORCHESTRATION
**Path**: `00-ORCHESTRATION/`
**Contents Read**:
- `state/` - REF-PROCESSING_PATTERN.md, REF-STANDARDS.md (18 lenses)
- `directives/` - Existing canonical directives (DIRECTIVE-017 through DIRECTIVE-042B)
- `oracle_contexts/` - Oracle 10 variants, ORACLE_ARC.md
- `ORACLE12_CONTEXT.md` - Current oracle context
- `blackboard/` - Packet infrastructure (audits/, evidence/, executions/, plans/)
- `scripts/` - cleanup_root.sh, verify_all.sh

### 3. 01-CANON
**Path**: `01-CANON/`
**Contents Read**:
- Full directory listing (79 markdown files + .DS_Store)
- Naming convention analysis (CANON-[ID]-[TOPIC]-[CLASS].md)
- Size distribution (5.3K to 117K)
- Permission structure (public vs private read)

### 4. Teleology Passes
**Paths**:
- `OUTGOING/teleology_visibility_pass_20260116_192327/`
- `OUTGOING/teleology_visibility_pass_2_20260116_203238/`
- `OUTGOING/TELEOLOGY_RING7_PASS_3_20260116_2330/`
- `OUTGOING/TELEOLOGY_PASS_4_20260117_1430/`
**Contents Read**:
- Orphan identification across all passes
- Duplicate detection reports
- Drift analysis between schema versions
- Recommendations synthesized for defrag audit

### 5. Root Governance Documents
**Paths Read**:
- `CLAUDE.md` - Constitutional rules, directory structure, anti-patterns
- `Makefile` - Build commands (verify, update-ledgers, sync, tree)
- `.claude/settings.json`, `.claude/commands/project/*.md`

### 6. Root Orphan Files (Examined)
**Directives at Root**:
- DIRECTIVE-042A_IIC_FOUNDATION.md
- DIRECTIVE-042B_MULTI_CLI.md
- DIRECTIVE-042C_OPERATIONAL_HYGIENE.md
- DIRECTIVE-042D_GEMINI_VALIDATION.md
- DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md
- DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md (COLLISION)
- DIRECTIVE-043B_CONTENT_STRATEGY.md
- DIRECTIVE-043B_OPERATIONAL_HYGIENE.md (COLLISION)
- DIRECTIVE-044A.md, DIRECTIVE-044B.md
- DIRECTIVE-045A.md, DIRECTIVE-045B.md
- DIRECTIVE-046A.md, DIRECTIVE-046B.md

**Oracle Contexts at Root**:
- ORACLE12_PEDIGREE.md, ORACLE12_PEDIGREE-045.md
- ORACLE12_SESSION_DELIVERABLES.md
- ORACLE13_CONTEXT.md

**Research/Temporal at Root**:
- DEEP_RESEARCH_PROMPT-*.md (3 files)
- frontier_models.md, google_research.md, openai_research.md
- platform_features.md, previous_thread.md
- BLITZKRIEG_44_DEPLOYMENT_GUIDE.md, BLITZKRIEG_45_DEPLOYMENT_GUIDE.md

**Directories at Root**:
- agents/, claudecode/, clitool/, codex/, cowork/, promptengineering/, system_prompts/

## Files NOT Present (Checked)
- `ORPHANS_AT_ROOT_LEVEL` - Not found
- `APPLY_DEFRAG_APPROVAL.txt` - Not found (APPLY not armed)
- `coordination.yaml` - Not found

## Input Verification
All inputs successfully read and cross-referenced. No access errors encountered.
