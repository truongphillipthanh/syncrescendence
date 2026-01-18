# Defrag Plan
## Ordered Operations to Reduce Entropy
**Generated**: 2026-01-17
**Mode**: READ-ONLY (APPLY not armed)
**Status**: PROPOSAL — requires Principal approval

---

## I. OBJECTIVES

1. **Relocate** all root orphans to canonical locations
2. **Resolve** DIRECTIVE-043 numbering collision
3. **Compress** obsolete files to symbolic archive
4. **Consolidate** duplicate directories
5. **Clean** detritus (DS_Store, temp files)

---

## II. EXECUTION PHASES

### Phase A: Detritus Removal (Safe, No Content Loss)
**Risk**: NONE

| Operation | Command Pattern |
|-----------|-----------------|
| Remove .DS_Store | `find . -name ".DS_Store" -delete` |
| Remove .tmp.driveupload/ | `rm -rf .tmp.driveupload/` |

**Verification**: `find . -name ".DS_Store" | wc -l` = 0

---

### Phase B: Directive Relocation (Low Risk)
**Risk**: LOW
**Requires**: DIRECTIVE-043 collision resolution first

#### B.1: Unambiguous Relocations

| Source | Destination |
|--------|-------------|
| `DIRECTIVE-042A_IIC_FOUNDATION.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042A.md` (verify or merge) |
| `DIRECTIVE-042B_MULTI_CLI.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042B.md` (verify or merge) |
| `DIRECTIVE-042C_OPERATIONAL_HYGIENE.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042C.md` |
| `DIRECTIVE-042D_GEMINI_VALIDATION.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042D.md` |
| `DIRECTIVE-044A.md` | `00-ORCHESTRATION/directives/DIRECTIVE-044A.md` |
| `DIRECTIVE-044B.md` | `00-ORCHESTRATION/directives/DIRECTIVE-044B.md` |
| `DIRECTIVE-045A.md` | `00-ORCHESTRATION/directives/DIRECTIVE-045A.md` |
| `DIRECTIVE-045B.md` | `00-ORCHESTRATION/directives/DIRECTIVE-045B.md` |
| `DIRECTIVE-046A.md` | `00-ORCHESTRATION/directives/DIRECTIVE-046A.md` |
| `DIRECTIVE-046B.md` | `00-ORCHESTRATION/directives/DIRECTIVE-046B.md` |

#### B.2: DIRECTIVE-043 Collision (PRINCIPAL DECISION REQUIRED)

**Current State**:
- `DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md`
- `DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md` (COLLISION)
- `DIRECTIVE-043B_CONTENT_STRATEGY.md`
- `DIRECTIVE-043B_OPERATIONAL_HYGIENE.md` (COLLISION)

**Options**:

| Option | 043A Winner | 043A Loser → | 043B Winner | 043B Loser → |
|--------|-------------|--------------|-------------|--------------|
| A | CONSTELLATION | INFRA→047A | CONTENT | OPS_HYG→047B |
| B | INFRASTRUCTURE | CONST→047A | OPS_HYG | CONTENT→047B |
| C | Merge both into single 043A | Archive loser | Merge both into single 043B | Archive loser |

**BLOCKED**: This defrag cannot proceed until Principal selects an option.

---

### Phase C: Oracle Context Consolidation (Low Risk)
**Risk**: LOW

| Operation | Source | Destination |
|-----------|--------|-------------|
| Relocate | `ORACLE13_CONTEXT.md` | `00-ORCHESTRATION/oracle_contexts/ORACLE13_CONTEXT.md` |
| Relocate | `ORACLE12_PEDIGREE.md` | Merge into `ORACLE12_CONTEXT.md` or archive |
| Relocate | `ORACLE12_PEDIGREE-045.md` | Merge into `ORACLE12_CONTEXT.md` or archive |
| Relocate | `ORACLE12_SESSION_DELIVERABLES.md` | Merge into `ORACLE12_CONTEXT.md` or archive |
| Archive | `ORACLE10_CONTEXT.md` | `05-ARCHIVE/ARCH-ORACLE10_CONTEXT.md` |
| Archive | `ORACLE10_CONTEXT_v2.md` | `05-ARCHIVE/ARCH-ORACLE10_CONTEXT_v2.md` |
| Archive | `ORACLE10_CONTEXT_v3.md` | `05-ARCHIVE/ARCH-ORACLE10_CONTEXT_v3.md` |
| Archive | `ORACLE10_CONTEXT_v4.md` | `05-ARCHIVE/ARCH-ORACLE10_CONTEXT_v4.md` |
| Archive | `ORACLE10_CONTEXT_root.md` | `05-ARCHIVE/ARCH-ORACLE10_CONTEXT_root.md` |
| Keep | `ORACLE10_CONTEXT_FINAL.md` | (canonical, no change) |
| Keep | `ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md` | (different purpose, no change) |

---

### Phase D: Canon Relocation (PROTECTED, MEDIUM RISK)
**Risk**: MEDIUM
**Requires**: Principal approval for any CANON modification

| Source | Destination | Notes |
|--------|-------------|-------|
| `CANON-31150-PLATFORM_CATALOG-*.md` | `01-CANON/CANON-31150-PLATFORM_CATALOG.md` | Canon file at root! |

---

### Phase E: Research Artifact Relocation (Low Risk)
**Risk**: LOW

| Source | Destination |
|--------|-------------|
| `DEEP_RESEARCH_PROMPT-Claude_Code_Ecosystem.md` | `04-SOURCES/raw/` |
| `DEEP_RESEARCH_PROMPT-Google_Ecosystem.md` | `04-SOURCES/raw/` |
| `DEEP_RESEARCH_PROMPT-OpenAI_Ecosystem.md` | `04-SOURCES/raw/` |
| `google_research.md` | `04-SOURCES/raw/` |
| `openai_research.md` | `04-SOURCES/raw/` |
| `SOURCES_ANALYSIS_REPORT.md` | `04-SOURCES/raw/` |
| `agents/` | `04-SOURCES/raw/agents/` |
| `claudecode/` | `04-SOURCES/raw/claudecode/` |
| `clitool/` | `04-SOURCES/raw/clitool/` |
| `codex/` | `04-SOURCES/raw/codex/` |
| `cowork/` | `04-SOURCES/raw/cowork/` |
| `promptengineering/` | `04-SOURCES/raw/promptengineering/` |
| `"Stop Using Claude Code Like This*.md"` | `04-SOURCES/raw/` |
| `"Why I Stopped Using MCPs*.md"` | `04-SOURCES/raw/` |

---

### Phase F: Obsolete File Compression (Low Risk)
**Risk**: LOW

| Source | Compressed To |
|--------|---------------|
| `frontier_models.md` | `05-ARCHIVE/ARCH-frontier_models.md` |
| `platform_features.md` | `05-ARCHIVE/ARCH-platform_features.md` |
| `BLITZKRIEG_44_DEPLOYMENT_GUIDE.md` | `05-ARCHIVE/ARCH-BLITZKRIEG_44.md` |
| `BLITZKRIEG_45_DEPLOYMENT_GUIDE.md` | `05-ARCHIVE/ARCH-BLITZKRIEG_45.md` |
| `deviser1_continuity.md` | `05-ARCHIVE/ARCH-deviser1_continuity.md` |
| `oracle_memories.md` | `05-ARCHIVE/ARCH-oracle_memories.md` |
| `oracle_process_archaelogy.md` | `05-ARCHIVE/ARCH-oracle_process_archaeology.md` |
| `previous_thread.md` | `05-ARCHIVE/ARCH-previous_thread.md` |
| `oracle_verification_manifest.md` | `05-ARCHIVE/ARCH-oracle_verification_manifest.md` |

---

### Phase G: Directory Consolidation (Medium Risk)
**Risk**: MEDIUM

| Operation | Source | Destination | Notes |
|-----------|--------|-------------|-------|
| Audit then Merge | `system_prompts/` | `02-OPERATIONAL/prompts/` | Keep unique content only |
| Audit then Delete | `.decisions/` | Archive unique, delete rest | Old decisions dir |

---

### Phase H: Working Document Decisions (Principal Required)
**Risk**: LOW
**Status**: BLOCKED pending Principal input

| File | Recommendation | Principal Options |
|------|----------------|-------------------|
| `checklist.md` | Archive | Keep / Archive / Delete |
| `INTERACTION_PARADIGM.md` | Integrate or Archive | Integrate / Archive |
| `rapport_contract.md` | Integrate or Archive | Integrate / Archive |

---

## III. EXECUTION ORDER

```
1. Phase A: Detritus Removal          ← Can run immediately
2. Phase C: Oracle Context            ← Can run after A
3. Phase E: Research Relocation       ← Can run in parallel with C
4. Phase F: Obsolete Compression      ← Can run in parallel with C, E
5. Phase B: Directive Relocation      ← BLOCKED on 043 decision
6. Phase D: Canon Relocation          ← Requires Principal approval
7. Phase G: Directory Consolidation   ← Requires audit
8. Phase H: Working Documents         ← Requires Principal input
```

---

## IV. BLOCKERS

| ID | Blocker | Required From | Severity |
|----|---------|---------------|----------|
| BLK-001 | DIRECTIVE-043 collision resolution | Principal | HIGH |
| BLK-002 | Canon relocation approval | Principal | MEDIUM |
| BLK-003 | Working document disposition | Principal | LOW |

---

## V. SUCCESS CRITERIA

| Criterion | Verification |
|-----------|--------------|
| Zero orphan files at root | `ls *.md | grep -v CLAUDE.md | wc -l` = 0 |
| Zero orphan directories at root | `ls -d */ | grep -v -E '^(0[0-6]|OUTGOING|config|\.)'` = 0 |
| DIRECTIVE-043 collision resolved | Only one 043A, one 043B exist |
| All Oracle contexts in oracle_contexts/ | `ls 00-ORCHESTRATION/oracle_contexts/ORACLE*.md` |
| Zero .DS_Store files | `find . -name ".DS_Store" | wc -l` = 0 |
| All obsolete files compressed | Check 05-ARCHIVE/ARCH-* count |

---

## VI. ROLLBACK STRATEGY

All operations preserve originals:
- Relocations: git tracks the move
- Compressions: original content in git history
- Deletions: only after git commit

**Rollback command**: `git checkout HEAD~1 -- <path>`

---

**This plan requires APPLY_DEFRAG_APPROVAL.txt to execute. Until then, it is READ-ONLY analysis.**
