# SOVEREIGN-008: CANON-31150 Terminology Update

**Created**: 2026-02-02
**Priority**: LOW
**Blocking**: Nothing (cosmetic alignment)
**Requires**: Sovereign approval for protected zone modification

---

## Request

CANON-31150-PLATFORM_CAPABILITY_CATALOG.md uses deprecated terminology:
- "Deviser" (10 references) → should be "Vanguard"
- "Executor" → should be "Commander"
- "Oracle (Gemini)" → should be "Oracle (Grok)" per COCKPIT.md v2.2
- IMEP flow references → deprecated

The SN encoding at `canon/sn/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md` has 4 matching references.

## Proposed Action

1. Run `python3 orchestration/scripts/regenerate_canon.py` (already updated with correct terminology)
2. Or manually find/replace in both CANON-31150 files

## Risk

Low. These are label changes, not structural. All other operational files have already been updated (commit `9226cb1`).

---

**Decision**: [x] APPROVE  [ ] DEFER  [ ] REJECT
**Executed**: 2026-02-06 by Commander — CANON-31150 SN file updated, verbose file was already current
**Sovereign Review (2026-02-10)**: Confirmed COMPLETE. Already executed. No further action required.
