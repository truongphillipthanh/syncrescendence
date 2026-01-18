# Drift Report
## Detecting Authority Conflicts and Semantic Drift
**Generated**: 2026-01-17

---

## I. WHAT IS DRIFT?

**Drift** occurs when:
1. Multiple documents claim authority over the same concept
2. Documents have diverged from their original purpose
3. Naming conventions have been applied inconsistently
4. Referenced targets no longer exist or have moved

---

## II. AUTHORITY CONFLICTS DETECTED

### Conflict 1: DIRECTIVE-043 Numbering Collision
**Type**: Governance failure
**Severity**: HIGH

| File | Claims To Be |
|------|--------------|
| `DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md` | 043A |
| `DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md` | 043A |
| `DIRECTIVE-043B_CONTENT_STRATEGY.md` | 043B |
| `DIRECTIVE-043B_OPERATIONAL_HYGIENE.md` | 043B |

**Analysis**: Two distinct directives share 043A; two share 043B. This is not versioning—these are different documents with colliding identifiers.

**Resolution Required**: Principal must determine:
- Which 043A is canonical, and renumber the other
- Which 043B is canonical, and renumber the other

---

### Conflict 2: ORACLE Context Multiplicity
**Type**: Version sprawl
**Severity**: MEDIUM

| Oracle | Files Found |
|--------|-------------|
| Oracle 10 | ORACLE10_CONTEXT.md, _v2.md, _v3.md, _v4.md, _FINAL.md, _root.md, COMPREHENSIVE_ARCHAEOLOGY.md |
| Oracle 12 | ORACLE12_CONTEXT.md, ORACLE12_PEDIGREE.md, ORACLE12_PEDIGREE-045.md, ORACLE12_SESSION_DELIVERABLES.md |
| Oracle 13 | ORACLE13_CONTEXT.md (at root—not in oracle_contexts/) |

**Analysis**: Oracle 10 has 7 variants; Oracle 12 has 4 files; Oracle 13 is misplaced at root.

**Resolution**:
- Oracle 10: Keep FINAL, archive rest
- Oracle 12: Consolidate into ORACLE12_CONTEXT.md in oracle_contexts/
- Oracle 13: Move to oracle_contexts/

---

### Conflict 3: Operational Hygiene Definition
**Type**: Concept split
**Severity**: LOW

| File | Location | Focus |
|------|----------|-------|
| `DIRECTIVE-042C_OPERATIONAL_HYGIENE.md` | root | Original hygiene spec? |
| `DIRECTIVE-043B_OPERATIONAL_HYGIENE.md` | root | Different hygiene spec? |

**Analysis**: Two directives claim "operational hygiene" in their name. Are these versions or distinct concepts?

**Resolution**: Read both, determine relationship, merge or distinguish.

---

### Conflict 4: System Prompts Location
**Type**: Directory duplication
**Severity**: MEDIUM

| Location | Contents |
|----------|----------|
| `system_prompts/` (root) | Unknown (old?) |
| `02-OPERATIONAL/prompts/` | Canonical prompts |

**Analysis**: Two directories may contain overlapping prompt definitions.

**Resolution**: Audit both, merge unique content to 02-OPERATIONAL/prompts/, delete root system_prompts/.

---

## III. SEMANTIC DRIFT PATTERNS

### Pattern 1: "Blitzkrieg" Concept Evolution

| File | Era | Meaning |
|------|-----|---------|
| BLITZKRIEG_44_DEPLOYMENT_GUIDE.md | Old | Deployment pattern |
| BLITZKRIEG_45_DEPLOYMENT_GUIDE.md | Newer | Updated deployment |
| CLAUDE.md (BLITZKRIEG MODEL SPECIFICATION) | Current | Model selection for parallel streams |

**Drift**: "Blitzkrieg" has evolved from deployment guides to model selection specification. Old deployment guides are now obsolete.

---

### Pattern 2: "Teleology" Pass Versioning

| Pass | Timestamp | Focus |
|------|-----------|-------|
| Pass 1 | 20260116_192327 | Initial visibility |
| Pass 2 | 20260116_203238 | Expanded |
| Pass 3 | 20260116_2330 | Ring 7 focus |
| Pass 4 | 20260117_1430 | Complete operational spec |

**Drift**: Each pass supersedes the previous for operational architecture. Pass 4 is canonical for the operational model.

**Note**: Earlier passes have historical value for archaeology but should not be consulted for current operations.

---

### Pattern 3: "Context" vs "Pedigree" vs "Deliverables"

Oracle documents use inconsistent naming:
- `*_CONTEXT.md` — Session context
- `*_PEDIGREE.md` — Lineage documentation
- `*_DELIVERABLES.md` — Session outputs
- `*_ARCHAEOLOGY.md` — Historical analysis

**Recommendation**: Standardize to `ORACLE{N}_CONTEXT.md` as the canonical pattern, with internal sections for pedigree/deliverables.

---

## IV. REFERENCE INTEGRITY ISSUES

### Issue 1: Broken References to Deleted Files
**Status**: Requires verification

Run this to find potential broken references:
```bash
# Find all markdown internal links
rg '\]\([^)]+\.md\)' --type md | head -50
```

### Issue 2: References to Root Files That Should Be Relocated
After relocating root orphans, references like `./DIRECTIVE-046A.md` will break.

**Mitigation**: Update references during relocation, or use canonical paths from start.

---

## V. NAMING CONVENTION DRIFT

### Current Conventions (Observed)

| Pattern | Example | Used In |
|---------|---------|---------|
| `DIRECTIVE-NNN[A-D]` | DIRECTIVE-046B | Execution directives |
| `CANON-NNNNN-TITLE` | CANON-00004-EVOLUTION | Canon documents |
| `REF-NAME` | REF-STANDARDS | Reference protocols |
| `DYN-NAME` | DYN-TREE | Dynamic state |
| `ARCH-NAME` | ARCH-* | Archaeological records |
| `SCAFF-NAME` | SCAFF-* | Scaffolding templates |
| `SOURCE-YYYYMMDD-NNN` | SOURCE-20260115-001 | Processed sources |

### Drift Observed

| Violation | File | Expected |
|-----------|------|----------|
| Unprefixed canon | Several in 01-CANON/ | CANON- prefix |
| Oracle at root | ORACLE13_CONTEXT.md | In oracle_contexts/ |
| Research at root | google_research.md | In 04-SOURCES/raw/ |

---

## VI. DRIFT RESOLUTION PRIORITY

| Priority | Issue | Action |
|----------|-------|--------|
| P0 | DIRECTIVE-043 collision | Principal decision required |
| P1 | Oracle 13 at root | Move to oracle_contexts/ |
| P1 | system_prompts/ duplicate | Audit and merge |
| P2 | Oracle 10 version sprawl | Archive non-FINAL versions |
| P2 | Root directive files | Relocate to directives/ |
| P3 | Blitzkrieg guides | Archive as historical |
| P3 | Naming convention cleanup | Enforce prefixes |

---

## VII. DRIFT PREVENTION RECOMMENDATIONS

1. **Directive Numbering Governance**: Check existing numbers before assigning new ones
2. **Single Source of Truth**: One file per concept, versions via git history
3. **Naming Enforcement**: Lint for convention violations
4. **Location Discipline**: Files must be in canonical directories, not root

---

**Drift is entropy. Detect early, resolve deliberately.**
