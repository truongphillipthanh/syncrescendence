# Quick Wins Queue
## Low-Effort, High-Value Tasks
### Generated: 2025-12-29 22:40 UTC

---

## Summary

This document catalogs actionable improvements requiring minimal effort but delivering meaningful value. Tasks are prioritized by impact-to-effort ratio.

**Legend**:
- Effort: (10m) = ~10 minutes, (30m) = ~30 minutes, (1h) = ~1 hour
- Impact: LOW / MEDIUM / HIGH

---

## 1. Documentation Gaps

### Missing READMEs

| Directory | Priority | Effort | Impact | Notes |
|-----------|----------|--------|--------|-------|
| `/` (root) | HIGH | (30m) | HIGH | No top-level README for repository |
| `/orchestration/` | MEDIUM | (15m) | HIGH | Add navigation README for orchestration subsystem |
| `/function/` | HIGH | (20m) | HIGH | Explain 0-distill/1-transform/2-expand structure |
| `/system_prompts/` | MEDIUM | (15m) | MEDIUM | Document prompt organization and usage |
| `/intelligence_architecture/` | LOW | (15m) | MEDIUM | Explain thesis development structure |
| `/prompt_engineering/` | LOW | (10m) | LOW | Document manual purpose and usage |
| `/legacy_salvage/` | LOW | (10m) | LOW | Explain archaeological intent |
| `/scaffold_files/` | LOW | (10m) | LOW | Brief content overview |
| `/context/` | LOW | (5m) | LOW | Single file; minimal README needed |

**Quick Win**: Create `/README.md` with high-level repository orientation. Estimated: 30 minutes. Impact: HIGH.

### Incomplete Sections in Documents

| Document | Section | Issue |
|----------|---------|-------|
| CANON-00007 (Artifact Protocol) | Cross-references | Uses legacy CANON-1 through CANON-17 |
| CANON-00000 (Schema) | ASCII diagrams | Need translation legend for legacy numbers |
| CANON-31120 (Tone Library) | Status | Still marked "v1.0 Beta" - needs finalization |
| CANON-31122 (Rhetorical Calibration) | Status | Still marked "v1.0 Beta" - needs finalization |

---

## 2. Broken Links / Stale References

### Internal References Needing Update

| Location | Current Reference | Should Be | Effort |
|----------|------------------|-----------|--------|
| CANON-00007 line 1 | `CANON-17:` | `CANON-00007:` | (5m) |
| CANON-00007 throughout | CANON-1 through CANON-17 | 5-digit equivalents | (1h) |
| CANON-00000 diagrams | CANON-1 through CANON-17 | 5-digit equivalents | (30m) |
| CANON-21000 header | CANON-09 through CANON-14 | CANON-30000 through CANON-35000 | (5m) |
| CANON-35110 header | CANON-07 | CANON-35100 | (2m) |
| CANON-34120 header | CANON-06 | CANON-34100 | (2m) |

**Quick Win**: Fix single-line header references in CANON-21000, 35110, 34120. Estimated: 10 minutes total. Impact: MEDIUM.

### External Links to Verify

No external links detected in CANON documents (by design - corpus is self-contained).

---

## 3. Naming Inconsistencies

### Version Format in Filenames

| Current Pattern | Files | Standard | Action |
|----------------|-------|----------|--------|
| `V1` (caps) | 1 file | `v1_0` | Rename CANON-23000-lattice-LUNAR_NAVIGATION-V1.md |
| `v2.2` (dot) | 4 files | `v2_2` | Rename to underscore format |
| No version | 12 files | Add version | Add version suffix to filename |

**Affected files needing rename**:
1. `CANON-23000-lattice-LUNAR_NAVIGATION-V1.md` → `CANON-23000-lattice-LUNAR_NAVIGATION-v1_0.md`
2. `CANON-22000-lattice-INTERFERENCE_PATTERN-v2.2.md` → `CANON-22000-lattice-INTERFERENCE_PATTERN-v2_2.md`
3. `CANON-32110-chain-INSIGHT-planetary-COHERENCE-lunar-SYSTEM-v2_2.md` → (already underscore, good)
4. `CANON-33110-chain-EXPERTISE-planetary-EFFICACY-lunar-BUSINESS_OPERATION_BACKBONE-v2_2.md` → (already underscore, good)

**Quick Win**: Rename 2 files with inconsistent version format. Estimated: 5 minutes. Impact: LOW.

### Header/Filename Version Mismatch

| File | Filename Version | Header Version | Action |
|------|------------------|----------------|--------|
| CANON-30000-chain-INTELLIGENCE-v1_1.md | v1_1 | v1.0.0 | Sync to v1.1 |

**Quick Win**: Sync header version in CANON-30000. Estimated: 2 minutes. Impact: LOW.

### Inconsistent Hierarchical Naming

| Issue | Files | Standard |
|-------|-------|----------|
| `ring` vs `planetary` | CANON-35xxx uses `ring`, others use `planetary` | By design - Wisdom uses ring structure |
| `-v2_3` suffix position | Varies (end vs middle) | Keep at end of filename |

**No action needed** - variations are intentional based on document structure.

---

## 4. Orphan Content

### Files Not Integrated Into Any System

| File | Location | Status | Recommendation |
|------|----------|--------|----------------|
| `generate-views.sh` | /scripts/ | Functional but undocumented | Add to README or integrate into orchestration |
| `.claude/settings.local.json` | /.claude/ | Active | Already integrated |
| `primer.txt` | /legacy_salvage/ | Archaeological | Leave as-is or move to archive |
| Various .xml files | /legacy_salvage/ | Archaeological | Document in legacy_salvage README |

### Content Worth Elevating

| Content | Current Location | Recommendation |
|---------|------------------|----------------|
| `context_engineering.md` | /orchestration/reference/research/ | Consider extracting key patterns to CANON |
| `MULTI_AGENT_ORCHESTRATION_METHODOLOGY.md` | /orchestration/reference/research/ | Integrate into orchestration docs |
| `operational_engine.md` | /orchestration/queue/PENDING_REVIEW/ | Complete review and either archive or integrate |

**Quick Win**: Review and disposition `operational_engine.md` (already in queue). Estimated: 15 minutes. Impact: MEDIUM.

---

## 5. Low-Hanging Fruit Summary

### Tier 1: Immediate (< 15 minutes each)

| Task | Effort | Impact | Priority |
|------|--------|--------|----------|
| Fix header references in CANON-21000, 35110, 34120 | 10m | MEDIUM | 1 |
| Rename CANON-23000 version format | 2m | LOW | 2 |
| Sync CANON-30000 header version | 2m | LOW | 3 |
| Create placeholder /function/README.md | 10m | MEDIUM | 4 |

### Tier 2: Quick Sessions (15-30 minutes each)

| Task | Effort | Impact | Priority |
|------|--------|--------|----------|
| Create root /README.md | 30m | HIGH | 1 |
| Create /orchestration/README.md | 15m | HIGH | 2 |
| Update CANON-00000 with legacy number legend | 20m | MEDIUM | 3 |
| Review operational_engine.md disposition | 15m | MEDIUM | 4 |

### Tier 3: Focused Work (1+ hours)

| Task | Effort | Impact | Priority |
|------|--------|--------|----------|
| Update CANON-00007 numbering throughout | 1-2h | HIGH | 1 |
| Promote beta documents to v1.0 | 1h | MEDIUM | 2 |
| Add versions to 12 unversioned files | 1h | LOW | 3 |

---

## Execution Tracking

| Task | Status | Completed By | Date |
|------|--------|--------------|------|
| - | - | - | - |

*Add rows as tasks are completed.*

---

## Notes

- Tasks should be completed in parallel with larger directive work where appropriate
- Quick wins provide visible progress between major initiatives
- Some tasks (like CANON-00007 update) may warrant their own directive

---

*Generated by DIRECTIVE-008 execution*
*For Oracle synthesis: This queue represents low-risk, high-value maintenance work that can be parallelized or used as "interstitial" tasks between major directives.*
