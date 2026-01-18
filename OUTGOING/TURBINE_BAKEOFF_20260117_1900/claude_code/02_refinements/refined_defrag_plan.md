# Refined Defrag Plan
**Generated**: 2026-01-17T19:00:00
**Author**: Claude Code (Opus 4.5)
**RUN_ID**: 20260117_1900
**Status**: READY FOR PRINCIPAL REVIEW

---

## Preamble

This refined plan consolidates the DEFRAG_CONVICTION_PASS_20260117_1609 with audit findings and teleology pass insights. It provides a single, authoritative move-map with rationale, risk assessment, and verification per operation.

**Execution Mode**: READ-ONLY until APPLY armed
**Arming Requirement**: Create `APPLY_DEFRAG_APPROVAL.txt` at repo root with exact content: `I_APPROVE_DEFRAG_APPLY`

---

## Move-Map

### PHASE A: Detritus Removal

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| A1 | `./**/.DS_Store` | DELETE | macOS metadata; no value | NONE | `find . -name ".DS_Store" \| wc -l` = 0 |
| A2 | `.tmp.driveupload/` | DELETE | Google Drive temp; empty | NONE | `ls -d .tmp.driveupload 2>/dev/null` = empty |

**Command**:
```bash
find . -name ".DS_Store" -delete
rm -rf .tmp.driveupload/
```

---

### PHASE B: Directive Relocation (Unambiguous)

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| B1 | `DIRECTIVE-042A_IIC_FOUNDATION.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042A_IIC_FOUNDATION.md` | Already exists as DIRECTIVE-042A.md; check for differences | LOW | Diff check; if duplicate, delete root copy |
| B2 | `DIRECTIVE-042B_MULTI_CLI.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042B_MULTI_CLI.md` | Already exists as DIRECTIVE-042B.md; check for differences | LOW | Diff check |
| B3 | `DIRECTIVE-042C_OPERATIONAL_HYGIENE.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042C.md` | New directive, not in directives/ | LOW | `ls 00-ORCHESTRATION/directives/DIRECTIVE-042C*` |
| B4 | `DIRECTIVE-042D_GEMINI_VALIDATION.md` | `00-ORCHESTRATION/directives/DIRECTIVE-042D.md` | New directive | LOW | `ls 00-ORCHESTRATION/directives/DIRECTIVE-042D*` |
| B5 | `DIRECTIVE-044A.md` | `00-ORCHESTRATION/directives/DIRECTIVE-044A.md` | Standard relocation | LOW | File exists at destination |
| B6 | `DIRECTIVE-044B.md` | `00-ORCHESTRATION/directives/DIRECTIVE-044B.md` | Standard relocation | LOW | File exists at destination |
| B7 | `DIRECTIVE-045A.md` | `00-ORCHESTRATION/directives/DIRECTIVE-045A.md` | Standard relocation | LOW | File exists at destination |
| B8 | `DIRECTIVE-045B.md` | `00-ORCHESTRATION/directives/DIRECTIVE-045B.md` | Standard relocation | LOW | File exists at destination |
| B9 | `DIRECTIVE-046A.md` | `00-ORCHESTRATION/directives/DIRECTIVE-046A.md` | Standard relocation | LOW | File exists at destination |
| B10 | `DIRECTIVE-046B.md` | `00-ORCHESTRATION/directives/DIRECTIVE-046B.md` | Standard relocation | LOW | File exists at destination |

**Command** (after collision resolution):
```bash
git mv DIRECTIVE-042C_OPERATIONAL_HYGIENE.md 00-ORCHESTRATION/directives/DIRECTIVE-042C.md
git mv DIRECTIVE-042D_GEMINI_VALIDATION.md 00-ORCHESTRATION/directives/DIRECTIVE-042D.md
git mv DIRECTIVE-044A.md 00-ORCHESTRATION/directives/
git mv DIRECTIVE-044B.md 00-ORCHESTRATION/directives/
git mv DIRECTIVE-045A.md 00-ORCHESTRATION/directives/
git mv DIRECTIVE-045B.md 00-ORCHESTRATION/directives/
git mv DIRECTIVE-046A.md 00-ORCHESTRATION/directives/
git mv DIRECTIVE-046B.md 00-ORCHESTRATION/directives/
```

---

### PHASE B2: DIRECTIVE-043 Collision Resolution (BLOCKER)

**Collision State**:
- `DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md` (root)
- `DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md` (root)
- `DIRECTIVE-043B_CONTENT_STRATEGY.md` (root)
- `DIRECTIVE-043B_OPERATIONAL_HYGIENE.md` (root)

**Principal Decision Required**:

| Option | 043A Winner | 043B Winner | Losers Renumbered To |
|--------|-------------|-------------|---------------------|
| **A (RECOMMENDED)** | CONSTELLATION_ARCHITECTURE | CONTENT_STRATEGY | INFRASTRUCTURE→047A, OPS_HYG→047B |
| B | INFRASTRUCTURE_OPERATIONS | OPERATIONAL_HYGIENE | CONSTELLATION→047A, CONTENT→047B |
| C | Merge documents | Merge documents | Archive non-merged content |

**Recommendation Rationale**:
- Execution logs reference CONSTELLATION (EXECUTION_LOG-2026-01-11-043A.md)
- CONTENT_STRATEGY aligns with Chain Matrix documentation pattern
- INFRASTRUCTURE and OPS_HYG content can be absorbed into 047 series

**If Option A Selected**:
```bash
git mv DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md 00-ORCHESTRATION/directives/DIRECTIVE-043A.md
git mv DIRECTIVE-043B_CONTENT_STRATEGY.md 00-ORCHESTRATION/directives/DIRECTIVE-043B.md
git mv DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md 00-ORCHESTRATION/directives/DIRECTIVE-047A.md
git mv DIRECTIVE-043B_OPERATIONAL_HYGIENE.md 00-ORCHESTRATION/directives/DIRECTIVE-047B.md
```

---

### PHASE C: Oracle Context Consolidation

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| C1 | `ORACLE13_CONTEXT.md` (root) | `00-ORCHESTRATION/oracle_contexts/ORACLE13_CONTEXT.md` | Standard Oracle context location | LOW | File exists at destination |
| C2 | `ORACLE12_PEDIGREE.md` (root) | `05-ARCHIVE/ARCH-ORACLE12_PEDIGREE.md` | Superseded by ORACLE12_CONTEXT | LOW | Archive file created |
| C3 | `ORACLE12_PEDIGREE-045.md` (root) | `05-ARCHIVE/ARCH-ORACLE12_PEDIGREE-045.md` | Session-specific; historical only | LOW | Archive file created |
| C4 | `ORACLE12_SESSION_DELIVERABLES.md` (root) | `05-ARCHIVE/ARCH-ORACLE12_SESSION_DELIVERABLES.md` | Session artifact; historical only | LOW | Archive file created |

**Command**:
```bash
git mv ORACLE13_CONTEXT.md 00-ORCHESTRATION/oracle_contexts/
git mv ORACLE12_PEDIGREE.md 05-ARCHIVE/ARCH-ORACLE12_PEDIGREE.md
git mv ORACLE12_PEDIGREE-045.md 05-ARCHIVE/ARCH-ORACLE12_PEDIGREE-045.md
git mv ORACLE12_SESSION_DELIVERABLES.md 05-ARCHIVE/ARCH-ORACLE12_SESSION_DELIVERABLES.md
```

---

### PHASE D: Canon Relocation (REQUIRES PRINCIPAL APPROVAL)

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| D1 | `CANON-31150-PLATFORM_CATALOG-lunar-ACUMEN-planetary-INFORMATION.md` | `01-CANON/CANON-31150-PLATFORM_CATALOG-lunar-ACUMEN-planetary-INFORMATION.md` | Canon files belong in 01-CANON/ | MEDIUM | File exists in 01-CANON/, verify content intact |

**Command** (after approval):
```bash
git mv "CANON-31150-PLATFORM_CATALOG-lunar-ACUMEN-planetary-INFORMATION.md" 01-CANON/
```

---

### PHASE E: Research Artifact Relocation

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| E1 | `DEEP_RESEARCH_PROMPT-Claude_Code_Ecosystem.md` | `04-SOURCES/raw/DEEP_RESEARCH_PROMPT-Claude_Code_Ecosystem.md` | Research prompt; source material | LOW | File exists |
| E2 | `DEEP_RESEARCH_PROMPT-Google_Ecosystem.md` | `04-SOURCES/raw/DEEP_RESEARCH_PROMPT-Google_Ecosystem.md` | Research prompt; source material | LOW | File exists |
| E3 | `DEEP_RESEARCH_PROMPT-OpenAI_Ecosystem.md` | `04-SOURCES/raw/DEEP_RESEARCH_PROMPT-OpenAI_Ecosystem.md` | Research prompt; source material | LOW | File exists |
| E4 | `google_research.md` | `04-SOURCES/processed/google_research.md` | Research output | LOW | File exists |
| E5 | `openai_research.md` | `04-SOURCES/processed/openai_research.md` | Research output | LOW | File exists |
| E6 | `SOURCES_ANALYSIS_REPORT.md` | `04-SOURCES/SOURCES_ANALYSIS_REPORT.md` | Source analysis | LOW | File exists |
| E7 | `agents/` | `04-SOURCES/raw/agents/` | Research collection | LOW | Directory exists |
| E8 | `claudecode/` | `04-SOURCES/raw/claudecode/` | Research collection | LOW | Directory exists |
| E9 | `clitool/` | `04-SOURCES/raw/clitool/` | Research collection | LOW | Directory exists |
| E10 | `codex/` | `04-SOURCES/raw/codex/` | Research collection | LOW | Directory exists |
| E11 | `cowork/` | `04-SOURCES/raw/cowork/` | Research collection | LOW | Directory exists |
| E12 | `promptengineering/` | `04-SOURCES/raw/promptengineering/` | Research collection | LOW | Directory exists |
| E13 | `Stop Using Claude Code Like This*.md` | `04-SOURCES/raw/` | External article | LOW | File exists |
| E14 | `Why I Stopped Using MCPs*.md` | `04-SOURCES/raw/` | External article | LOW | File exists |

**Command**:
```bash
git mv DEEP_RESEARCH_PROMPT-*.md 04-SOURCES/raw/
git mv google_research.md 04-SOURCES/processed/
git mv openai_research.md 04-SOURCES/processed/
git mv SOURCES_ANALYSIS_REPORT.md 04-SOURCES/
git mv agents/ 04-SOURCES/raw/
git mv claudecode/ 04-SOURCES/raw/
git mv clitool/ 04-SOURCES/raw/
git mv codex/ 04-SOURCES/raw/
git mv cowork/ 04-SOURCES/raw/
git mv promptengineering/ 04-SOURCES/raw/
git mv "Stop Using Claude Code Like This (Use Sub-Agents Instead).md" 04-SOURCES/raw/
git mv "Why I Stopped Using MCPs in Claude Code (And What I Use Instead).md" 04-SOURCES/raw/
```

---

### PHASE F: Obsolete File Compression (Archive)

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| F1 | `frontier_models.md` | `05-ARCHIVE/ARCH-frontier_models.md` | Temporal snapshot; obsolete | LOW | Archive created |
| F2 | `platform_features.md` | `05-ARCHIVE/ARCH-platform_features.md` | Temporal snapshot; obsolete | LOW | Archive created |
| F3 | `BLITZKRIEG_44_DEPLOYMENT_GUIDE.md` | `05-ARCHIVE/ARCH-BLITZKRIEG_44_DEPLOYMENT_GUIDE.md` | Superseded by 045, 046 | LOW | Archive created |
| F4 | `BLITZKRIEG_45_DEPLOYMENT_GUIDE.md` | `05-ARCHIVE/ARCH-BLITZKRIEG_45_DEPLOYMENT_GUIDE.md` | Superseded by 046 | LOW | Archive created |
| F5 | `deviser1_continuity.md` | `05-ARCHIVE/ARCH-deviser1_continuity.md` | Session artifact | LOW | Archive created |
| F6 | `oracle_memories.md` | `05-ARCHIVE/ARCH-oracle_memories.md` | Session artifact | LOW | Archive created |
| F7 | `oracle_process_archaelogy.md` | `05-ARCHIVE/ARCH-oracle_process_archaeology.md` | Spelling fix + archive | LOW | Archive created |
| F8 | `oracle_verification_manifest.md` | `05-ARCHIVE/ARCH-oracle_verification_manifest.md` | Session artifact | LOW | Archive created |
| F9 | `previous_thread.md` | `05-ARCHIVE/ARCH-previous_thread.md` | Session artifact | LOW | Archive created |

**Command**:
```bash
git mv frontier_models.md 05-ARCHIVE/ARCH-frontier_models.md
git mv platform_features.md 05-ARCHIVE/ARCH-platform_features.md
git mv BLITZKRIEG_44_DEPLOYMENT_GUIDE.md 05-ARCHIVE/ARCH-BLITZKRIEG_44_DEPLOYMENT_GUIDE.md
git mv BLITZKRIEG_45_DEPLOYMENT_GUIDE.md 05-ARCHIVE/ARCH-BLITZKRIEG_45_DEPLOYMENT_GUIDE.md
git mv deviser1_continuity.md 05-ARCHIVE/ARCH-deviser1_continuity.md
git mv oracle_memories.md 05-ARCHIVE/ARCH-oracle_memories.md
git mv oracle_process_archaelogy.md 05-ARCHIVE/ARCH-oracle_process_archaeology.md
git mv oracle_verification_manifest.md 05-ARCHIVE/ARCH-oracle_verification_manifest.md
git mv previous_thread.md 05-ARCHIVE/ARCH-previous_thread.md
```

---

### PHASE G: Directory Consolidation

| # | From | To | Rationale | Risk | Verification |
|---|------|-----|-----------|------|--------------|
| G1 | `system_prompts/` | Audit then merge unique to `02-OPERATIONAL/prompts/` | Redundant structure | MEDIUM | No data loss; unique content preserved |
| G2 | `.decisions/` | Verify content in `00-ORCHESTRATION/state/ARCH-DESIGN_DECISIONS.md` | Already archived | LOW | Content verified present |

**Command** (after audit):
```bash
# Audit system_prompts first
diff -rq system_prompts/ 02-OPERATIONAL/prompts/
# If unique content found, merge; otherwise:
rm -rf system_prompts/

# .decisions/ - verify then remove
cat .decisions/DESIGN_DECISIONS.md
# If matches ARCH-DESIGN_DECISIONS.md:
rm -rf .decisions/
```

---

### PHASE H: Working Document Disposition (REQUIRES PRINCIPAL INPUT)

| # | File | Options | Recommendation |
|---|------|---------|----------------|
| H1 | `checklist.md` | Keep / Archive / Delete | Archive → `05-ARCHIVE/ARCH-checklist.md` |
| H2 | `INTERACTION_PARADIGM.md` | Keep / Integrate / Archive | Integrate key concepts → REF-STANDARDS.md, Archive original |
| H3 | `rapport_contract.md` | Keep / Integrate / Archive | Archive → `05-ARCHIVE/ARCH-rapport_contract.md` |

**Command** (if recommendations accepted):
```bash
git mv checklist.md 05-ARCHIVE/ARCH-checklist.md
# Manual: Extract key concepts from INTERACTION_PARADIGM.md to REF-STANDARDS.md
git mv INTERACTION_PARADIGM.md 05-ARCHIVE/ARCH-INTERACTION_PARADIGM.md
git mv rapport_contract.md 05-ARCHIVE/ARCH-rapport_contract.md
```

---

## Execution Order

```
PHASE A (Detritus)
    → PHASE C (Oracle Contexts)
    → PHASE E (Research) [parallel-safe]
    → PHASE F (Obsolete) [parallel-safe]
    → PHASE B (Directives) [after B2 collision resolution]
    → PHASE D (Canon) [after approval]
    → PHASE G (Directories) [after audit]
    → PHASE H (Working docs) [after decisions]
```

---

## Success Criteria

| Criterion | Command | Expected |
|-----------|---------|----------|
| Zero orphan MD at root | `ls *.md 2>/dev/null \| grep -v CLAUDE.md \| wc -l` | 0 |
| Zero orphan dirs at root | `ls -d */ \| grep -vE '^(0[0-6]\|OUTGOING\|config)/'` | 0 |
| Zero .DS_Store | `find . -name ".DS_Store" \| wc -l` | 0 |
| Directives relocated | `ls 00-ORCHESTRATION/directives/DIRECTIVE-04*.md \| wc -l` | 12+ |
| Canon intact | `ls 01-CANON/CANON*.md \| wc -l` | 80 |
| Archives created | `ls 05-ARCHIVE/ARCH-*.md \| wc -l` | 12+ |
| Git history clean | `git status --porcelain` | Empty (all committed) |

---

## Rollback Procedure

If any phase fails:
1. `git reset --hard HEAD^` (revert last commit)
2. Or selective: `git checkout HEAD~1 -- <file_path>`
3. Or archive extraction: Copy from `05-ARCHIVE/ARCH-*`

All operations are reversible via git history.
