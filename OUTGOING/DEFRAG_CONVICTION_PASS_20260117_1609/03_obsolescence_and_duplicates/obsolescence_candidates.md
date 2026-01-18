# Obsolescence Candidates
## Files Recommended for Archive with Symbolic Compression
**Generated**: 2026-01-17

---

## I. OBSOLESCENCE CRITERIA

A file is **obsolete** when:
1. Its content has been superseded by a newer version
2. Its temporal information is no longer accurate
3. Its purpose has been absorbed into another document
4. It serves no current operational function

**Rule**: Obsolete files are NOT deleted—they are COMPRESSED and ARCHIVED.

---

## II. COMPRESSION PROTOCOL

Before archiving, extract and preserve:

```
SYMBOLIC COMPRESSION FORMAT
===========================
# ARCH-[original-name].md

**Archived From**: [original path]
**Archived On**: [date]
**Superseded By**: [replacement file, if any]

## ESSENCE
[2-3 sentence distillation of what this document contained]

## KEY DECISIONS RECORDED
- [Decision 1]
- [Decision 2]

## INTEGRATION RECORD
[What was integrated elsewhere before archiving]

## RETRIEVAL
Original preserved in git history at commit [hash]
```

---

## III. OBSOLESCENCE CANDIDATES

### Tier 1: Clearly Obsolete (Compress Immediately)

| File | Reason | Superseded By |
|------|--------|---------------|
| `frontier_models.md` | Temporal snapshot from Oct 2025 | External model registries |
| `platform_features.md` | Temporal platform state | External docs |
| `BLITZKRIEG_44_DEPLOYMENT_GUIDE.md` | Superseded by 45 | BLITZKRIEG_45 |
| `BLITZKRIEG_45_DEPLOYMENT_GUIDE.md` | Superseded by CLAUDE.md spec | CLAUDE.md Blitzkrieg section |
| `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT.md` | Superseded by FINAL | ORACLE10_CONTEXT_FINAL.md |
| `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v2.md` | Superseded by FINAL | ORACLE10_CONTEXT_FINAL.md |
| `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v3.md` | Superseded by FINAL | ORACLE10_CONTEXT_FINAL.md |
| `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v4.md` | Superseded by FINAL | ORACLE10_CONTEXT_FINAL.md |
| `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_root.md` | Superseded by FINAL | ORACLE10_CONTEXT_FINAL.md |

### Tier 2: Session Artifacts (Compress for Continuity)

| File | Reason | Essence To Extract |
|------|--------|-------------------|
| `deviser1_continuity.md` | Session capture | Key decisions, handoff notes |
| `oracle_memories.md` | ChatGPT memory backup | Unique context not elsewhere |
| `oracle_process_archaelogy.md` | Process history | Lessons learned |
| `previous_thread.md` | Prior thread context | Continuation context |
| `rapport_contract.md` | Working document | If unique, integrate |

### Tier 3: Research Artifacts (Archive or Process)

| File | Action | Rationale |
|------|--------|-----------|
| `google_research.md` | RELOCATE to 04-SOURCES/raw/ | Research notes for processing |
| `openai_research.md` | RELOCATE to 04-SOURCES/raw/ | Research notes for processing |
| `DEEP_RESEARCH_PROMPT-*.md` (3 files) | RELOCATE to 04-SOURCES/raw/ | Research prompts |
| `agents/`, `claudecode/`, `codex/`, etc. | RELOCATE to 04-SOURCES/raw/ | Research directories |

### Tier 4: Working Documents (Decision Required)

| File | Options | Decision Needed |
|------|---------|-----------------|
| `checklist.md` | Archive or delete | Is it still active? |
| `INTERACTION_PARADIGM.md` | Archive or integrate | Does it have unique value? |
| `oracle_verification_manifest.md` | Archive | Historical checklist |
| `SOURCES_ANALYSIS_REPORT.md` | Archive or process | Analysis artifact |

---

## IV. COMPRESSION TEMPLATES

### Template: Temporal Snapshot Compression

```markdown
# ARCH-frontier_models.md

**Archived From**: /frontier_models.md
**Archived On**: 2026-01-17
**Superseded By**: N/A (temporal content doesn't have successors)

## ESSENCE
Point-in-time snapshot of frontier AI model capabilities as of October 2025.
Documented Claude 3.5 Sonnet, GPT-4 Turbo, Gemini 1.5 Pro specifications.
Now obsolete as all models have been updated.

## KEY DECISIONS RECORDED
- None (reference document only)

## INTEGRATION RECORD
No integrations—content was reference-only.

## RETRIEVAL
Original preserved in git history at commit [TBD during APPLY]
```

### Template: Session Continuity Compression

```markdown
# ARCH-deviser1_continuity.md

**Archived From**: /deviser1_continuity.md
**Archived On**: 2026-01-17
**Superseded By**: N/A (continuity captured)

## ESSENCE
ChatGPT Deviser station continuity capture from session [date].
Documented [key context] to enable session handoff.

## KEY DECISIONS RECORDED
- [List key decisions if any]

## INTEGRATION RECORD
Context integrated into ORACLE[N]_CONTEXT.md

## RETRIEVAL
Original preserved in git history at commit [TBD during APPLY]
```

### Template: Version Supersession Compression

```markdown
# ARCH-ORACLE10_CONTEXT_v2.md

**Archived From**: /00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v2.md
**Archived On**: 2026-01-17
**Superseded By**: ORACLE10_CONTEXT_FINAL.md

## ESSENCE
Version 2 of Oracle 10 session context. Intermediate version
capturing [specific additions over v1]. Now superseded by FINAL.

## KEY DECISIONS RECORDED
- [Any decisions unique to this version]

## INTEGRATION RECORD
All valuable content carried forward to FINAL.

## RETRIEVAL
Original preserved in git history at commit [TBD during APPLY]
```

---

## V. COMPRESSION EXECUTION ORDER

When APPLY is armed, process in this order:

1. **Temporal snapshots first** (no dependencies)
   - frontier_models.md
   - platform_features.md
   - BLITZKRIEG_44, BLITZKRIEG_45

2. **Version chains** (oldest first)
   - ORACLE10_CONTEXT.md → v2 → v3 → v4 → root
   - (Keep FINAL, COMPREHENSIVE_ARCHAEOLOGY)

3. **Session artifacts** (verify no active references)
   - deviser1_continuity.md
   - oracle_memories.md
   - oracle_process_archaelogy.md
   - previous_thread.md

4. **Working documents** (Principal decision)
   - checklist.md
   - INTERACTION_PARADIGM.md
   - rapport_contract.md

---

## VI. NON-OBSOLETE (KEEP)

These files are NOT obsolete despite appearing old:

| File | Reason to Keep |
|------|----------------|
| `ORACLE10_CONTEXT_FINAL.md` | Canonical Oracle 10 context |
| `ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md` | Different purpose (archaeology, not context) |
| `ORACLE12_CONTEXT.md` (in oracle_contexts/) | Current Oracle 12 context |
| `ORACLE13_CONTEXT.md` | Current Oracle—needs relocation, not archival |
| All files in `01-CANON/` | Constitutional—never archive without Principal |
| All `REF-*.md` files | Reference protocols—stable |
| All `DYN-*.md` files | Live state—never archive |

---

## VII. SUMMARY

| Category | Count | Action |
|----------|-------|--------|
| Clearly obsolete | 9 | COMPRESS → ARCHIVE |
| Session artifacts | 5 | COMPRESS → ARCHIVE |
| Research artifacts | 8+ | RELOCATE → 04-SOURCES/raw/ |
| Working documents | 4 | Principal decision |
| **TOTAL requiring action** | **26+** | |

---

**Obsolescence is not failure—it's the natural end of a document's lifecycle. Compress the essence, archive the original, and move forward.**
