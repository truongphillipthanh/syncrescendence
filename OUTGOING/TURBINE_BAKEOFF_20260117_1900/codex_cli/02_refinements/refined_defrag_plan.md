# Refined Defrag Plan (Read-Only)

## Preconditions
- APPLY gate must be armed with APPLY_DEFRAG_APPROVAL.txt containing I_APPROVE_DEFRAG_APPLY.
- DIRECTIVE-043A and DIRECTIVE-043B winners selected and loser renumbering approved.
- Canon relocation approved for any CANON file moves.
- Working document disposition decided (checklist.md, INTERACTION_PARADIGM.md, rapport_contract.md).

## Preflight Checks (Update)
- Root orphan directory check should ignore both `OUTGOING/` and `outgoing/`:
  - `ls -d */ | rg -v '^(0[0-6]|OUTGOING|outgoing|config|\.)'`
- Confirm root orphans list for execution scope:
  - `ls *.md | rg -v '^CLAUDE.md$'`

## Phase A: Detritus Removal (safe)
- Remove `.DS_Store` and `.tmp.driveupload/` only after APPLY.

## Phase B: Directive Relocation (blocked)
- Exact moves (post-approval, after collision resolution):
  - DIRECTIVE-042A_IIC_FOUNDATION.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042A.md (verify/merge first)
  - DIRECTIVE-042B_MULTI_CLI.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042B.md (verify/merge first)
  - DIRECTIVE-042C_OPERATIONAL_HYGIENE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042C.md
  - DIRECTIVE-042D_GEMINI_VALIDATION.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042D.md
  - DIRECTIVE-044A.md -> 00-ORCHESTRATION/directives/DIRECTIVE-044A.md
  - DIRECTIVE-044B.md -> 00-ORCHESTRATION/directives/DIRECTIVE-044B.md
  - DIRECTIVE-045A.md -> 00-ORCHESTRATION/directives/DIRECTIVE-045A.md
  - DIRECTIVE-045B.md -> 00-ORCHESTRATION/directives/DIRECTIVE-045B.md
  - DIRECTIVE-046A.md -> 00-ORCHESTRATION/directives/DIRECTIVE-046A.md
  - DIRECTIVE-046B.md -> 00-ORCHESTRATION/directives/DIRECTIVE-046B.md
- Collision resolution required before moving:
  - DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-043A.md (winner)
  - DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md -> 00-ORCHESTRATION/directives/DIRECTIVE-047A.md (loser renumbered) or archive
  - DIRECTIVE-043B_CONTENT_STRATEGY.md -> 00-ORCHESTRATION/directives/DIRECTIVE-043B.md (winner)
  - DIRECTIVE-043B_OPERATIONAL_HYGIENE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-047B.md (loser renumbered) or archive

## Phase C: Oracle Context Consolidation
- ORACLE13_CONTEXT.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE13_CONTEXT.md
- ORACLE12_PEDIGREE.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE12_PEDIGREE.md (or compress to 05-ARCHIVE)
- ORACLE12_PEDIGREE-045.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE12_PEDIGREE-045.md (or compress to 05-ARCHIVE)
- ORACLE12_SESSION_DELIVERABLES.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE12_SESSION_DELIVERABLES.md (or compress to 05-ARCHIVE)
- ORACLE10_CONTEXT.md -> 05-ARCHIVE/ARCH-ORACLE10_CONTEXT.md (symbolic compression required)
- ORACLE10_CONTEXT_v2.md -> 05-ARCHIVE/ARCH-ORACLE10_CONTEXT_v2.md (symbolic compression required)
- ORACLE10_CONTEXT_v3.md -> 05-ARCHIVE/ARCH-ORACLE10_CONTEXT_v3.md (symbolic compression required)
- ORACLE10_CONTEXT_v4.md -> 05-ARCHIVE/ARCH-ORACLE10_CONTEXT_v4.md (symbolic compression required)
- ORACLE10_CONTEXT_root.md -> 05-ARCHIVE/ARCH-ORACLE10_CONTEXT_root.md (symbolic compression required)
- ORACLE10_CONTEXT_FINAL.md stays in 00-ORCHESTRATION/oracle_contexts/
- ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md stays in 00-ORCHESTRATION/oracle_contexts/

## Phase D: Canon Relocation (protected)
- CANON-31150-PLATFORM_CATALOG-lunar-ACUMEN-planetary-INFORMATION.md -> 01-CANON/CANON-31150-PLATFORM_CATALOG.md (Principal approval required)

## Phase E: Research Artifact Relocation
- DEEP_RESEARCH_PROMPT-Claude_Code_Ecosystem.md -> 04-SOURCES/raw/
- DEEP_RESEARCH_PROMPT-Google_Ecosystem.md -> 04-SOURCES/raw/
- DEEP_RESEARCH_PROMPT-OpenAI_Ecosystem.md -> 04-SOURCES/raw/
- google_research.md -> 04-SOURCES/raw/
- openai_research.md -> 04-SOURCES/raw/
- SOURCES_ANALYSIS_REPORT.md -> 04-SOURCES/raw/
- agents/ -> 04-SOURCES/raw/agents/
- claudecode/ -> 04-SOURCES/raw/claudecode/
- clitool/ -> 04-SOURCES/raw/clitool/
- codex/ -> 04-SOURCES/raw/codex/
- cowork/ -> 04-SOURCES/raw/cowork/
- promptengineering/ -> 04-SOURCES/raw/promptengineering/
- Stop Using Claude Code Like This (Use Sub-Agents Instead).md -> 04-SOURCES/raw/
- Why I Stopped Using MCPs in Claude Code (And What I Use Instead).md -> 04-SOURCES/raw/

## Phase F: Obsolete File Compression
- frontier_models.md -> 05-ARCHIVE/ARCH-frontier_models.md (symbolic compression required)
- platform_features.md -> 05-ARCHIVE/ARCH-platform_features.md (symbolic compression required)
- BLITZKRIEG_44_DEPLOYMENT_GUIDE.md -> 05-ARCHIVE/ARCH-BLITZKRIEG_44.md (symbolic compression required)
- BLITZKRIEG_45_DEPLOYMENT_GUIDE.md -> 05-ARCHIVE/ARCH-BLITZKRIEG_45.md (symbolic compression required)
- deviser1_continuity.md -> 05-ARCHIVE/ARCH-deviser1_continuity.md (symbolic compression required)
- oracle_memories.md -> 05-ARCHIVE/ARCH-oracle_memories.md (symbolic compression required)
- oracle_process_archaelogy.md -> 05-ARCHIVE/ARCH-oracle_process_archaeology.md (symbolic compression required)
- previous_thread.md -> 05-ARCHIVE/ARCH-previous_thread.md (symbolic compression required)
- oracle_verification_manifest.md -> 05-ARCHIVE/ARCH-oracle_verification_manifest.md (symbolic compression required)

## Phase G: Directory Consolidation (audit required)
- system_prompts/ -> 02-OPERATIONAL/prompts/ (merge unique content; archive before deletion)
- .decisions/ (if present) -> 05-ARCHIVE/ARCH-decisions/ (archive unique, then remove)

## Phase H: Working Documents (Principal decision)
- checklist.md -> 05-ARCHIVE/ARCH-checklist.md or retain
- INTERACTION_PARADIGM.md -> integrate into 02-OPERATIONAL/ or archive
- rapport_contract.md -> integrate into 02-OPERATIONAL/ or archive

## Post-Apply Verification (update)
- Orphan directory check should exclude both outgoing variants:
  - `ls -d */ | rg -v '^(0[0-6]|OUTGOING|outgoing|config|\.)'`
- Validate no root directives or oracle contexts remain.
- Run link integrity scan for moved files.
