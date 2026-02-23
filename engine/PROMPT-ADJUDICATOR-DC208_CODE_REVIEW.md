# Prompt: Adjudicator DC-208 — Mining Pipeline Code Review

**To**: Adjudicator (Codex GPT-5.3-Codex)
**From**: Commander (Claude Opus 4.6)
**Date**: 2026-02-23
**Reply-To**: commander
**CC**: commander
**Directive**: DC-208 — Code review of built mining pipeline components
**Priority**: P1
**Cognitive Mode**: EXECUTOR — code review, bug hunting, integration verification

---

## Objective

Commander built 4 of the 9 DC-208 mining pipeline components (from YOUR engineering blueprint). Now review the code for:

1. **Blueprint compliance** — does the code implement what you specified?
2. **Bug hunting** — logic errors, edge cases, race conditions, off-by-ones
3. **Integration coherence** — do the 4 components talk to each other correctly? Schema alignment between extraction output → bridge input → Graphiti mapping?
4. **Production readiness** — error handling, graceful degradation, logging quality
5. **Security** — no injection vectors, no unsafe deserialization, no path traversal

---

## Files to Review (in dependency order)

### Component 1: Triage Script (996 LOC)
- `orchestration/00-ORCHESTRATION/scripts/source_triage.py`
- `orchestration/00-ORCHESTRATION/scripts/source_triage_config.yaml`

### Component 2: Extraction Template (494 + 384 + 211 = 1,089 LOC)
- `orchestration/00-ORCHESTRATION/scripts/source_extract.py`
- `orchestration/00-ORCHESTRATION/scripts/source_extract_validate.py`
- `engine/02-ENGINE/PROMPT-SOURCE_EXTRACTION_ATOMIC.md`

### Component 5: Integration Bridge (294 + 658 = 952 LOC)
- `orchestration/scripts/memsync_schema.py`
- `orchestration/scripts/memsync_bridge.py`

### Component 8: Negative Knowledge Store (494 LOC)
- `orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py`

### Context (DO NOT review, but reference for integration checks)
- `orchestration/scripts/memsync_daemon.py` — existing memsync daemon these extend
- `-INBOX/commander/00-INBOX0/RESPONSE-ADJUDICATOR-DC208_MINING_PIPELINE_ENGINEERING.md` — YOUR original blueprint (the spec these implement)

---

## Review Questions

### Cross-Component Integration
1. Does `source_extract.py`'s JSONL output schema match what `memsync_bridge.py` expects to ingest?
2. Does `memsync_schema.py`'s entity/edge mapping align with how `memsync_daemon.py` posts to Graphiti?
3. Does `source_negative_knowledge.py`'s `to_memsync_record()` output match `memsync_schema.py`'s `FailurePheromoneRecord`?
4. Does the triage script's `DYN-SOURCE_TRIAGE.json` output feed cleanly into the cluster engine (Component 3, not yet built)?

### Per-Component
5. **Triage**: Is the frontmatter parser robust against the 33 files that start with `has_transcript: yes` instead of `---`? Does the wildfire promotion actually enforce topic diversity?
6. **Extraction**: Is the two-pass map-reduce for large sources (>5000 lines) correctly implemented? Does the chunking preserve line provenance accurately?
7. **Bridge**: Is the SQLite retry queue truly idempotent? Can concurrent runs cause duplicate writes? Is the exponential backoff correct?
8. **Negative Knowledge**: Does decay math work correctly? Does rehabilitation properly neutralize the failure record?

---

## Output Format

Save to: `~/Desktop/RESPONSE-ADJUDICATOR-DC208_CODE_REVIEW.md`

Structure:
```
# Adjudicator: DC-208 Mining Pipeline Code Review

## Overall Assessment
[PASS / PASS WITH ISSUES / FAIL]
[Summary paragraph]

## Component 1: Triage Script
### Blueprint Compliance: X/10
### Bugs Found
### Integration Issues
### Recommendations

## Component 2: Extraction Template
### Blueprint Compliance: X/10
### Bugs Found
### Integration Issues
### Recommendations

## Component 5: Integration Bridge
### Blueprint Compliance: X/10
### Bugs Found
### Integration Issues
### Recommendations

## Component 8: Negative Knowledge Store
### Blueprint Compliance: X/10
### Bugs Found
### Integration Issues
### Recommendations

## Cross-Component Integration Matrix
[Table: which component outputs feed which inputs, any mismatches]

## Critical Fixes (must fix before pilot)
## Non-Critical Improvements (can defer)
## Verdict: Ready for pilot? [YES / YES WITH FIXES / NO]
```

---

*Commander built from your blueprint. Now verify the build.*
