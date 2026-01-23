# GEMINI CLI ORACLE TASK: CANON Deep Sensing

**Directive**: DIR-20260123-CANON-ANNEALMENT
**Date**: 2026-01-23
**From**: Claude Code (EXECUTOR)
**To**: Gemini CLI (ORACLE)

---

## Objective

Analyze the full CANON corpus for:
1. Semantic redundancy across documents
2. Monolith split recommendations
3. SN conversion validation

---

## Context

Bulk SN conversion complete:
- 82 files converted
- 53% overall compression (348K → 164K words)
- Drafts in `01-CANON/sn-drafts/`

Your 1M+ context window enables full corpus analysis impossible for other models.

---

## Files to Ingest

**Priority Order**:
1. `00-ORCHESTRATION/notation/symbols.yaml` — SN glossary (read first)
2. All 82 files in `01-CANON/CANON-*.md` — Original corpus
3. All 82 files in `01-CANON/sn-drafts/CANON-*.md` — Converted drafts

---

## Analysis Tasks

### Task 1: Redundancy Detection

Identify content that appears in multiple CANON files:
- Repeated definitions
- Duplicate explanations
- Overlapping scope

Output format:
```
REDUNDANCY:
  files: [file1, file2, ...]
  content: "<duplicated content summary>"
  recommendation: merge_into | deduplicate | keep_both
  rationale: "<why this recommendation>"
```

### Task 2: Monolith Split Recommendations

For files with >5K original words, assess whether splitting would improve:
- Navigability
- Semantic coherence per document
- Cross-reference clarity

Output format:
```
SPLIT:
  source: CANON-XXXXX
  original_words: N
  recommended_satellites:
    - name: "<satellite name>"
      content_scope: "<what goes here>"
      estimated_words: N
  rationale: "<why split helps>"
```

### Task 3: SN Conversion Validation

For each converted file, assess:
- Semantic preservation: Is meaning intact?
- Information loss: What's missing?
- Compression quality: Was compression appropriate?

Output format:
```
VALIDATION:
  file: CANON-XXXXX
  semantic_preserved: true | false
  issues: ["<issue1>", "<issue2>"]
  information_loss: none | minimal | significant
  confidence: 0.0-1.0
```

### Task 4: Cross-Reference Integrity

Identify broken or orphaned references:
- CANON files that reference non-existent documents
- Circular dependencies that could be simplified
- Missing backlinks

---

## Output Format

Generate: `ARCH-GEMINI_CANON_AUDIT-20260123.md`

Structure:
```markdown
# Gemini CANON Audit Report

**Date**: 2026-01-23
**Model**: gemini-2.0-flash-thinking-exp
**Corpus Size**: 82 CANON files + 82 SN drafts

## Executive Summary
[3-5 bullet points of key findings]

## Redundancy Analysis
[All REDUNDANCY blocks]

## Monolith Split Recommendations
[All SPLIT blocks]

## SN Validation Summary
[Aggregate statistics + problem files]

## Cross-Reference Integrity
[Issues found]

## Recommendations
[Prioritized action items]
```

---

## Execution Command

```bash
gemini -m gemini-2.0-flash-thinking-exp \
  --context-file 00-ORCHESTRATION/notation/symbols.yaml \
  --context-file "01-CANON/CANON-*.md" \
  --context-file "01-CANON/sn-drafts/CANON-*.md" \
  --prompt "$(cat 00-ORCHESTRATION/gemini_prompts/CANON_AUDIT.md)" \
  --output 00-ORCHESTRATION/state/ARCH-GEMINI_CANON_AUDIT-20260123.md
```

---

## Success Criteria

- [ ] All 82 original files analyzed
- [ ] All 82 SN drafts validated
- [ ] Redundancy report with actionable recommendations
- [ ] Monolith split plans for files >5K words
- [ ] Validation confidence scores average ≥0.85

---

**END GEMINI ORACLE TASK**
