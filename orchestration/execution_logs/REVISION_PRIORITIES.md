# REVISION PRIORITIES
## DIRECTIVE-023 Phase 4 — Scripture Verification
**Generated**: 2025-12-30
**Purpose**: Ranked list of documents requiring content revision

---

## EXECUTIVE SUMMARY

**Total CANON Files Audited**: 64 (excluding CANON-99000)
**Files Requiring Revision**: 12 (🟡 MEDIUM priority)
**Files Aligned (No Action)**: 52 (🟢 LOW priority)

**Critical Finding**: No CRITICAL or HIGH priority issues remain. Phases 1-3 successfully resolved structural problems. Remaining issues are cosmetic.

---

## PRIORITY CLASSIFICATION

| Priority | Criteria | Action | Timeline |
|----------|----------|--------|----------|
| 🔴 CRITICAL | Core theory significantly misaligned | Requires immediate revision | Block other work |
| 🟠 HIGH | Important document with notable misalignment | Should be revised soon | Next directive |
| 🟡 MEDIUM | Minor misalignment or dated references | Update when convenient | Batch update |
| 🟢 LOW | Aligned with current understanding | No action needed | N/A |

---

## TIER 1: 🔴 CRITICAL PRIORITY

**None.**

No documents contain fundamental misalignment with evolved understanding. The scripture substantially embodies Oracle 0-6 accumulated wisdom.

---

## TIER 2: 🟠 HIGH PRIORITY

**None.**

Phases 1-3 successfully addressed all HIGH priority issues:
- Old chain names: RESOLVED (DIRECTIVE-022B)
- Old numbering: RESOLVED (DIRECTIVE-022A)
- Version fragmentation: RESOLVED (DIRECTIVE-022C)

---

## TIER 3: 🟡 MEDIUM PRIORITY (12 Documents)

### Issue Category A: Inline Version References

**Problem**: Documents contain "Version 2.3" or similar in body text, which now conflicts with frontmatter version 2.0.0.

**Affected Files**:

| # | File | Location | Current Text | Recommended Change |
|---|------|----------|--------------|-------------------|
| 1 | CANON-00000-SCHEMA-cosmos.md | Lines 18-25 | "Version: 2.3" in header block | Remove or update to "2.0" |
| 2 | CANON-00001-SYNCRESCENDENCE-cosmos.md | Line 19 | "Version: 2.3" | Remove or update to "2.0" |
| 3 | CANON-00005-STRATEGY-cosmos.md | Lines 17-24 | "Version: 2.3" header | Remove or update to "2.0" |

**Recommended Action**: Remove inline version references; rely on frontmatter only.

### Issue Category B: Dated AI Model References

**Problem**: References to GPT-4/Claude 3+ are dated; Claude Opus 4.5 and GPT-4o/4.1 now exist.

**Affected Files**:

| # | File | Lines | Current References | Notes |
|---|------|-------|-------------------|-------|
| 4 | CANON-00000-SCHEMA-cosmos.md | 131 | "GPT-4+, Claude 3+" | Update to current frontier |
| 5 | CANON-00001-SYNCRESCENDENCE-cosmos.md | 84, 588 | "GPT-4+, Claude 3+", "Claude Sonnet 4, GPT-4" | Update |
| 6 | CANON-00009-QUICKSTART-cosmos.md | 58, 289, 577 | "Claude and GPT-4" | Update |
| 7 | CANON-30000-INTELLIGENCE-chain.md | 152, 183 | "Claude/GPT-4 class", "GPT-4V" | Update |
| 8 | CANON-30200-POSITIONING-comet-INTELLIGENCE.md | 362, 433 | "GPT-4 still leading" | Dated assessment |
| 9 | CANON-31142-PLATFORM_GRAMMAR-satellite-IIC.md | 1340 | "ChatGPT-4" | Update |
| 10 | CANON-33111-BIZ_ENHANCE-satellite-BIZ.md | 50, 191 | "Claude, GPT-4, Gemini" | Update |
| 11 | CANON-34110-CURRICULUM-lunar-MASTERY.md | 442 | "Claude/GPT-4" | Update |
| 12 | CANON-34120-SYLLABUS-lunar-MASTERY.md | Multiple | "GPT-4 Turbo", "Claude Sonnet 4.5" | Mixed currency |

**Recommended Action**:
- Update to "Claude 4+ (including Opus 4.5), GPT-4o/4.1+" as current frontier
- Maintain capability-focused framing over specific model versions
- Add note that model references are time-stamped (current as of December 2025)

### Issue Category C: Dated Month/Year References

**Problem**: Specific dates like "October 2025" or "November 2025" will quickly become stale.

**Affected Files** (overlaps with above):
- CANON-00000: "November 10, 2025" in header
- CANON-00001: "November 10, 2025" in header, "October 2025" line 588
- CANON-00005: "November 10, 2025" in header
- CANON-34120: "October 2025" in tool list

**Recommended Action**: Either remove specific dates from prose headers (use frontmatter dates only) or replace with relative references ("As of late 2025...").

---

## TIER 4: 🟢 LOW PRIORITY (52 Documents)

These documents require **no revision** at this time:

### cosmos/ tier (8 of 11 aligned):
- CANON-00002 (CORPUS)
- CANON-00003 (EVALUATION)
- CANON-00004 (RESOLUTIONS)
- CANON-00006 (OPERATIONS)
- CANON-00007 (ARTIFACT_PROTOCOL)
- CANON-00008 (MODAL_SEQUENCE)
- CANON-00010 (CONTENT_PROTOCOL) — minor GPT-4 ref acceptable

### core/ tier (2 of 2 aligned):
- CANON-10000 (CELESTIAL_BODY)
- CANON-11000 (FACETS)

### lattice/ tier (8 of 8 aligned):
- CANON-20000 through CANON-25100 — all aligned

### chains/ tier (34 of 43 aligned):
- All CANON-30xxx except 30000, 30200
- All CANON-31xxx except 31142
- All CANON-32xxx
- CANON-33000, 33100, 33110, 33112
- All CANON-34xxx except 34110, 34120
- All CANON-35xxx

---

## TIER 5: ⬜ SKIP (1 Document)

| File | Reason |
|------|--------|
| CANON-99000-HISTORICAL-meta.md | Intentionally preserves historical content |

---

## RECOMMENDED EXECUTION APPROACH

### Option A: Batch Update (Recommended)

Execute as single directive (DIRECTIVE-024) with three parallel streams:

**Stream A**: Version Reference Cleanup (3 files)
- Remove inline version text from cosmos/ headers
- Effort: LOW (simple deletions)

**Stream B**: AI Model Updates (9 files)
- Update model references to current frontier
- Add temporal disclaimer
- Effort: MEDIUM (requires careful wording)

**Stream C**: Date Reference Updates (4 files)
- Convert specific dates to relative references
- Effort: LOW (simple replacements)

**Total Estimated Effort**: 2-3 hours of editing

### Option B: Opportunistic Updates

Address these issues when files are modified for other reasons. Accept that some dated references will persist until touched.

**Trade-off**: Lower immediate effort but ongoing technical debt.

---

## VERIFICATION CHECKLIST

After revisions, verify:

- [ ] No inline "Version X.X" text remaining in cosmos/ tier
- [ ] All AI model references updated to December 2025 frontier
- [ ] No specific month/year dates in document headers
- [ ] Frontmatter `updated:` field reflects revision date
- [ ] No new issues introduced

---

## DEPENDENCIES

### Before These Revisions
- Phase 3 complete (✅ DONE)
- GENESIS layer established (✅ DONE)

### After These Revisions
- CURRENT_STATE.md updated
- Commit with clear message

---

## SUCCESS CRITERIA

✅ All 12 MEDIUM priority documents revised
✅ No CRITICAL or HIGH issues exist
✅ AI model references current
✅ Version references consistent
✅ Date references appropriately relative

---

## VERSION HISTORY

**v1.0.0** (2025-12-30): Initial revision priorities for DIRECTIVE-023
- 0 CRITICAL, 0 HIGH, 12 MEDIUM, 52 LOW documents classified
- Execution approach recommended

---

*Revision priorities documented. The corpus is substantially aligned; remaining issues are cosmetic and can be addressed at convenience.*
