# Tighten Report: Audizable Convention & Smoketest Cleanup

**Date**: 2026-01-19
**Executor**: Claude Code (Opus 4.5)

## Summary

This bundle tightens the codification pass by:
1. Canonicalizing the audizable delimiter convention to single source of truth
2. Normalizing all files to use `===AUDIZABLE===` format (not `---AUDIZABLE---` or code fences)
3. Verifying no smoketest duplication issues exist

---

## What Changed

### 1. Canonicalized Audizable Delimiter Format

**Canonical format** (enforced everywhere):
```
===AUDIZABLE===
[plain text audio script here - no markdown, TTS-optimized]
===END===
```

This format:
- Is deterministically parsed by `ingest_chatgpt_container.py`
- Uses `===` delimiters for unambiguous machine parsing
- Is consistent with the container grammar in REF-CHATGPT_CONTAINER_PROTOCOL.md

### 2. Files Normalized

| File | Change |
|------|--------|
| `02-OPERATIONAL/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md` | Updated to use `===AUDIZABLE===` format |
| `02-OPERATIONAL/specs/REF-AUDIZER_PROTOCOL.md` | Added canonical delimiter section, removed `audio` fence reference |
| `-INBOX/chatgpt_syncrescendence_smoketest_v2.md` | Updated delimiter from `---AUDIZABLE---` to `===AUDIZABLE===` |
| `-INBOX/chatgpt_syncrescendence_smoketest_v3.md` | Updated delimiter from `---AUDIZABLE---` to `===AUDIZABLE===` |
| `-INBOX/chatgpt_global_memory_update_prompt.md` | Updated from `---FILE: audizable.txt---` to `===AUDIZABLE===` |

### 3. Smoketest Duplication Status

**Finding**: No actual content duplication found in smoketest files. The v2 and v3 files are distinct versions with different test steps.

---

## Before/After Summary

### Before
Multiple competing conventions existed:
- `===AUDIZABLE===` (ingestion script standard)
- `` ```audio `` code fence (mentioned in some docs)
- `---AUDIZABLE---` / `---END AUDIZABLE---` (suggested in smoketest)
- `---FILE: audizable.txt---` (global memory prompt)

### After
Single canonical convention across all documents:
```
===AUDIZABLE===
[content]
===END===
```

---

## Files Touched

| Path | Operation |
|------|-----------|
| `02-OPERATIONAL/specs/REF-AUDIZER_PROTOCOL.md` | Updated |
| `02-OPERATIONAL/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md` | Updated |
| `-INBOX/chatgpt_syncrescendence_smoketest_v2.md` | Updated |
| `-INBOX/chatgpt_syncrescendence_smoketest_v3.md` | Updated |
| `-INBOX/chatgpt_global_memory_update_prompt.md` | Updated |

---

## Validation Results

### Structural Verification

**Command**: `bash 00-ORCHESTRATION/scripts/structural_verify.sh`

**Result**: **PASS** (0 errors, 3 warnings)

```
=== STRUCTURAL VERIFICATION ===
✓ -OUTGOING/ exists
✓ -INBOX/ exists
✓ Only sanctioned directories at root
✓ No orphan files at root
✓ All COCKPIT.md paths resolve
⚠ Found 25 references to config/coordination
⚠ Found 20 legacy 'OUTGOING/' references
⚠ Found 55 lowercase 'outgoing/' references
✓ -INBOX/blitzkrieg_drop/ exists (3 files)
✓ Continuation packet type defined in schema

=== SUMMARY ===
⚠ 3 warnings (0 errors)
```

### Operations Lint

**Command**: `bash 02-OPERATIONAL/scripts/ops_lint.sh`

**Result**: **PASS** (0 errors)

```
=== OPERATIONS ARTIFACT LINTER ===
Files checked: 17
Errors: 0
Warnings: 0

LINT PASSED: All checked files have valid frontmatter
```

---

## Not Changed

- `00-ORCHESTRATION/state/REF-CHATGPT_CONTAINER_PROTOCOL.md` - Already uses canonical `===AUDIZABLE===` format
- `00-ORCHESTRATION/scripts/ingest_chatgpt_container.py` - Already parses canonical format
- The 3 warnings from structural verification are pre-existing legacy reference issues, not related to this tightening pass

---

## Files in This Bundle

```
-OUTGOING/20260119-tighten_audizable_and_smoketest/
└── TIGHTEN_REPORT.md    # This file
```

---

## Next Steps

1. **Update ChatGPT memories**: Use the updated `chatgpt_global_memory_update_prompt.md` to sync global preferences
2. **Clean legacy references** (optional): Address the 3 warnings from structural verification
3. **Test ingestion**: Verify container ingestion works with updated smoketest format
