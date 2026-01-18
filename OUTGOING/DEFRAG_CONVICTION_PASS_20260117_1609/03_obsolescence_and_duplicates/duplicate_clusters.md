# Duplicate Clusters Analysis
## Near-Duplicate Detection and Winner Selection
**Generated**: 2026-01-17

---

## I. DETECTION METHODOLOGY

Duplicates identified by:
1. Filename pattern similarity
2. Numbering collisions (same DIRECTIVE-NNN at multiple locations)
3. Content overlap (superseded versions)
4. Same conceptual purpose at different locations

---

## II. DUPLICATE CLUSTERS

### Cluster 1: DIRECTIVE-042 Variants
**Files**:
- `DIRECTIVE-042A_IIC_FOUNDATION.md` (root)
- `DIRECTIVE-042B_MULTI_CLI.md` (root)
- `DIRECTIVE-042C_OPERATIONAL_HYGIENE.md` (root)
- `DIRECTIVE-042D_GEMINI_VALIDATION.md` (root)
- `00-ORCHESTRATION/directives/DIRECTIVE-042A.md`
- `00-ORCHESTRATION/directives/DIRECTIVE-042B.md`

**Analysis**: Root-level versions appear to be the same as or variants of directives/ versions.

**Winner**: Files in `00-ORCHESTRATION/directives/` (canonical location)

**Action**:
- Verify root versions match directives/ versions
- If match: DELETE root versions
- If differ: COMPRESS root versions to archive, keep directives/

**Risk**: MEDIUM — need to verify content before action

---

### Cluster 2: DIRECTIVE-043 Duplicates
**Files**:
- `DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md` (root)
- `DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md` (root) — **NAMING COLLISION**
- `DIRECTIVE-043B_CONTENT_STRATEGY.md` (root)
- `DIRECTIVE-043B_OPERATIONAL_HYGIENE.md` (root) — **NAMING COLLISION**

**Analysis**: Two different files share 043A numbering; two different files share 043B numbering. This is a governance failure.

**Winner**: Need content review to determine which is canonical

**Action**:
- Read both 043A files to determine actual purpose
- Rename or re-number the non-canonical one
- Move winners to `00-ORCHESTRATION/directives/`
- COMPRESS and archive the losers

**Risk**: HIGH — numbering collision indicates process failure

---

### Cluster 3: Oracle Context Variants
**Files**:
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT.md`
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v2.md`
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v3.md`
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v4.md`
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_FINAL.md`
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_root.md`
- `00-ORCHESTRATION/oracle_contexts/ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md`

**Analysis**: Multiple versions of Oracle 10 context. FINAL should be canonical.

**Winner**: `ORACLE10_CONTEXT_FINAL.md`

**Action**:
- Keep FINAL as canonical
- Keep COMPREHENSIVE_ARCHAEOLOGY (different purpose)
- Archive v1-v4 and root (version history)

**Risk**: LOW — versions are historical; FINAL is clearly marked

---

### Cluster 4: ORACLE12 Documents at Root
**Files**:
- `ORACLE12_PEDIGREE.md` (root)
- `ORACLE12_PEDIGREE-045.md` (root)
- `ORACLE12_SESSION_DELIVERABLES.md` (root)
- `00-ORCHESTRATION/ORACLE12_CONTEXT.md`

**Analysis**: Multiple Oracle 12 docs at root, one in orchestration.

**Winner**: `00-ORCHESTRATION/ORACLE12_CONTEXT.md` (correct location)

**Action**:
- Verify root versions are captured in ORACLE12_CONTEXT.md
- RELOCATE root files to oracle_contexts/ or COMPRESS to archive

**Risk**: LOW — just location issue

---

### Cluster 5: Teleology Bundles
**Files**:
- `OUTGOING/teleology_visibility_pass_20260116_192327/` + `.zip`
- `OUTGOING/teleology_visibility_pass_2_20260116_203238/` + `.zip`
- `OUTGOING/TELEOLOGY_RING7_PASS_3_20260116_2330/` + `.zip`
- `OUTGOING/TELEOLOGY_PASS_4_20260117_1430/` + `.zip`
- `OUTGOING/RING7_PHASESHIFT_PASS_20260116_2219/` + `.zip`
- `OUTGOING/RING7_PHASESHIFT_PASS_20260116_212500/`

**Analysis**: These are intentional versioned bundles, not duplicates. However:
- Zipped versions duplicate unzipped directories
- Pass 4 supersedes earlier passes for operational architecture

**Winner**: Latest pass (Pass 4) for operational architecture

**Action**:
- Keep all for archaeology (intentional versioning)
- Consider: remove directories where .zip exists (redundant)
- Or: remove .zip where directory exists (easier to browse)

**Risk**: LOW — just storage optimization

---

### Cluster 6: System Prompts Directory
**Files**:
- `system_prompts/` (root)
- `02-OPERATIONAL/prompts/` (proper location)

**Analysis**: Old `system_prompts/` directory at root; newer structure in `02-OPERATIONAL/prompts/`.

**Winner**: `02-OPERATIONAL/prompts/`

**Action**:
- Check if system_prompts/ content is already in 02-OPERATIONAL/prompts/
- If yes: DELETE system_prompts/
- If no: MERGE unique content, then DELETE

**Risk**: MEDIUM — need to verify content isn't lost

---

### Cluster 7: Continuity/Memory Documents
**Files**:
- `deviser1_continuity.md` (root)
- `oracle_memories.md` (root)
- `previous_thread.md` (root)
- `oracle_process_archaelogy.md` (root)

**Analysis**: These are all session continuity captures at root. Should be archived.

**Winner**: None — all should be archived or integrated

**Action**:
- COMPRESS each to symbolic compression
- RELOCATE to 05-ARCHIVE/ with ARCH- prefix
- Or integrate valuable content into CANON

**Risk**: LOW — historical preservation

---

## III. WINNER SELECTION CRITERIA

| Criterion | Weight |
|-----------|--------|
| In canonical location | HIGH |
| More recent timestamp | MEDIUM |
| Marked "FINAL" | HIGH |
| More complete content | MEDIUM |
| Referenced by other docs | HIGH |

---

## IV. SUMMARY TABLE

| Cluster | Winner Location | Losers Action | Risk |
|---------|-----------------|---------------|------|
| 1 (042) | 00-ORCHESTRATION/directives/ | DELETE root or COMPRESS | MEDIUM |
| 2 (043) | TBD after review | RENAME/RENUMBER, COMPRESS | HIGH |
| 3 (Oracle10) | FINAL | ARCHIVE versions | LOW |
| 4 (Oracle12) | 00-ORCHESTRATION/ | RELOCATE | LOW |
| 5 (Teleology) | Keep all (versioned) | Optimize storage | LOW |
| 6 (Prompts) | 02-OPERATIONAL/prompts/ | MERGE or DELETE | MEDIUM |
| 7 (Continuity) | Archive all | COMPRESS → ARCHIVE | LOW |

---

## V. IMMEDIATE ACTION REQUIRED

**Cluster 2 (DIRECTIVE-043)** requires Principal review:
- Two files claim to be 043A
- Two files claim to be 043B
- This is a numbering collision that must be resolved

**UNKNOWN**: Which 043A is canonical?
**VERIFICATION STEP**: Read both files, compare purposes, decide winner

---

**Duplicates create confusion. Resolve them with clear winners and symbolic compression of losers.**
