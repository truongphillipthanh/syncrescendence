# Refined Symbolic Compression Rules
**Generated**: 2026-01-17T19:00:00
**Author**: Claude Code (Opus 4.5)
**RUN_ID**: 20260117_1900

---

## Purpose

Define concrete rules for "compress before archive" operations and what counts as sufficient compression. These rules operationalize the distinction between live content and archival content.

---

## I. Core Principle: Wells vs Rivers

From the Crashout Prevention Philosophy:

- **Rivers**: Transient information flows (conversations, sessions, temporal snapshots)
- **Wells**: Permanent deposits (Canon, state files, archived artifacts)

**Compression** transforms River content into Well-compatible form before archival.

---

## II. What Requires Compression Before Archive

### Category 1: Temporal Snapshots

**Definition**: Documents capturing state at a specific point in time that will become stale.

**Examples**:
- `frontier_models.md` - Model capabilities as of October 2025
- `platform_features.md` - Platform state as of specific date
- Research outputs with dated findings

**Compression Method**:
1. Extract timeless principles/patterns
2. Document what was learned (not just what was observed)
3. Add archive date to filename: `ARCH-{original_name}.md`
4. Preserve original in git history

**Sufficient Compression**:
- Original content preserved (via git)
- Archive prefix applied
- No integration required (content is historical reference only)

### Category 2: Session Artifacts

**Definition**: Documents created during a specific working session that captured intermediate state.

**Examples**:
- `previous_thread.md` - Prior conversation context
- `deviser1_continuity.md` - Session handoff notes
- `oracle_memories.md` - Session-specific reflections

**Compression Method**:
1. Identify any unique decisions or insights
2. If decisions present: Record in CANON-00008-RESOLUTIONS or REF-STANDARDS.md
3. If insights present: Integrate into relevant Canon document
4. Archive with ARCH- prefix

**Sufficient Compression**:
- Unique decisions extracted and recorded
- Unique insights integrated
- Original archived for provenance

### Category 3: Superseded Documents

**Definition**: Documents replaced by newer versions.

**Examples**:
- `BLITZKRIEG_44_DEPLOYMENT_GUIDE.md` - Superseded by 045, 046
- `ORACLE10_CONTEXT_v2.md` - Superseded by ORACLE10_CONTEXT_FINAL.md
- Old directive versions when consolidated

**Compression Method**:
1. Verify successor document exists and is complete
2. Diff for any unique content not in successor
3. If unique content found: Merge into successor
4. Archive original with ARCH- prefix

**Sufficient Compression**:
- Successor verified complete
- Unique content merged (if any)
- Original archived for lineage

### Category 4: Duplicate Content

**Definition**: Content that exists in multiple locations.

**Examples**:
- Root directives that also exist in `00-ORCHESTRATION/directives/`
- Oracle contexts with multiple versions
- Research content duplicated across passes

**Compression Method**:
1. Identify canonical version (most recent, most complete)
2. Diff all versions
3. Merge any unique content into canonical
4. Delete non-canonical duplicates (git preserves history)

**Sufficient Compression**:
- Single canonical version established
- All unique content merged
- Duplicates removed (not archived - git history sufficient)

---

## III. What Does NOT Require Compression

### Category A: Living Infrastructure

**Examples**:
- `00-ORCHESTRATION/state/*` - Active state files
- `tasks.csv`, `projects.csv` - Current ledgers
- `system_state.json`, `events.jsonl` - Real-time state

**Rule**: NEVER archive. These are operational. If stale, update rather than archive.

### Category B: Canon Documents

**Examples**:
- All files in `01-CANON/`

**Rule**: NEVER compress/archive Canon. Canon is the permanent record. If content is obsolete, it should be versioned within Canon (not moved to archive).

### Category C: Active Directives

**Examples**:
- Current directive series (044, 045, 046)

**Rule**: Directives in active execution should not be archived until superseded.

### Category D: Source Documents

**Examples**:
- `04-SOURCES/raw/*` - Original source material
- `04-SOURCES/processed/*` - Processed sources with citations

**Rule**: Sources are reference material. Archive only if explicitly integrated into Canon AND no longer needed for citation.

---

## IV. Compression Checklist

Before archiving any document, verify:

```
[ ] 1. CLASSIFICATION: What category is this document?
    - Temporal snapshot?
    - Session artifact?
    - Superseded document?
    - Duplicate content?
    - Something else? (may not need archival)

[ ] 2. EXTRACTION: Have I extracted unique value?
    - Decisions → RESOLUTIONS or state files
    - Insights → Canon documents
    - Patterns → REF-* files in state/
    - Nothing unique → Proceed to archive

[ ] 3. SUCCESSOR: If superseded, is successor complete?
    - Diff performed?
    - Unique content merged?
    - Successor verified?

[ ] 4. NAMING: Archive filename correct?
    - Format: ARCH-{original_name}.md
    - No date in filename (git has dates)
    - Descriptive name preserved

[ ] 5. LOCATION: Archive destination correct?
    - General archive → 05-ARCHIVE/
    - Historical context → 05-ARCHIVE/ with ARCH-ORACLE prefix
    - Directive archive → 05-ARCHIVE/ARCH-DIRECTIVE-{NUM}.md

[ ] 6. GIT: Will git preserve history?
    - Using `git mv` (not `mv`)?
    - Commit message descriptive?
```

---

## V. Compression Sufficiency Criteria

A document is **sufficiently compressed** when:

1. **Unique Content Preserved**: Any insights, decisions, or patterns unique to this document have been extracted and recorded in the appropriate permanent location (Canon, state files, or RESOLUTIONS).

2. **Lineage Traceable**: The archive filename and git history allow reconstruction of when this document existed and what it contained.

3. **No Orphan References**: Any documents that referenced this file have been updated with new paths (or reference is to git history).

4. **Archive Location Correct**: File is in 05-ARCHIVE/ with ARCH- prefix.

5. **No Redundancy**: If this was a duplicate, the canonical version is clearly identified and this copy is deleted (not archived - git is sufficient).

---

## VI. Decision Tree

```
START: Document at root needs action
    │
    ├─ Is it Canon? → NO ACTION AT ROOT (relocate to 01-CANON/)
    │
    ├─ Is it a current directive (044+)? → RELOCATE to 00-ORCHESTRATION/directives/
    │
    ├─ Is it a duplicate of existing canonical file?
    │   ├─ YES → DIFF, merge unique, DELETE (git preserves)
    │   └─ NO → Continue
    │
    ├─ Is it temporal/session-specific?
    │   ├─ YES → EXTRACT unique value, then ARCHIVE
    │   └─ NO → Continue
    │
    ├─ Is it superseded by newer version?
    │   ├─ YES → VERIFY successor, MERGE unique, ARCHIVE
    │   └─ NO → Continue
    │
    ├─ Is it research/source material?
    │   ├─ YES → RELOCATE to 04-SOURCES/
    │   └─ NO → Continue
    │
    └─ Is it operational infrastructure?
        ├─ YES → RELOCATE to appropriate numbered directory
        └─ NO → ASK PRINCIPAL for disposition
```

---

## VII. Examples

### Example 1: frontier_models.md

**Classification**: Temporal snapshot (October 2025 model data)
**Unique Value**: None - data obsolete, patterns already in Canon
**Action**: Archive directly
**Command**: `git mv frontier_models.md 05-ARCHIVE/ARCH-frontier_models.md`
**Sufficiency**: PASS - no extraction needed, lineage preserved

### Example 2: deviser1_continuity.md

**Classification**: Session artifact
**Unique Value Check**: Contains session handoff instructions
**Extraction**: Review for any decisions not in RESOLUTIONS
**Action**: Archive after extraction (if any)
**Command**: `git mv deviser1_continuity.md 05-ARCHIVE/ARCH-deviser1_continuity.md`
**Sufficiency**: PASS if extraction complete

### Example 3: DIRECTIVE-042A at root vs 00-ORCHESTRATION/directives/

**Classification**: Duplicate content
**Canonical Version**: The one in `00-ORCHESTRATION/directives/`
**Diff Check**: If identical, delete root copy; if different, merge
**Action**: Delete root copy (git preserves history)
**Command**: `rm DIRECTIVE-042A_IIC_FOUNDATION.md` (after verification)
**Sufficiency**: PASS - canonical version authoritative, git has history

---

## Summary

| Content Type | Compression Required? | Method | Destination |
|--------------|----------------------|--------|-------------|
| Temporal snapshots | Optional (extract if valuable) | ARCH- prefix | 05-ARCHIVE/ |
| Session artifacts | Yes (extract decisions/insights) | ARCH- prefix | 05-ARCHIVE/ |
| Superseded docs | Yes (merge unique content) | ARCH- prefix | 05-ARCHIVE/ |
| Duplicates | No (delete non-canonical) | DELETE | Git history |
| Living infrastructure | NEVER | N/A | Keep in place |
| Canon | NEVER | N/A | Keep in 01-CANON/ |
| Research/sources | No | RELOCATE | 04-SOURCES/ |
