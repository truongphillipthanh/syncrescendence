# Corpus Survey Report

**Date**: 2026-01-19
**Git HEAD**: `46fd3da463d676c3932480ca32226f69cbd01330`
**Executor**: Claude Code (Opus 4.5)

---

## Git Status Summary

Modified files (18 tracked, 2 new directories):
- `.DS_Store`, `.obsidian/workspace.json`
- `00-ORCHESTRATION/scripts/` (2 files)
- `00-ORCHESTRATION/state/` (4 files)
- `02-ENGINE/prompts/canonical/` (9 files)
- `CLAUDE.md`, `COCKPIT.md`
- Deleted files from legacy `OUTGOING/` (now staged in `-OUTGOING/`)
- New directories: `-INBOX/`, `-OUTGOING/`

---

## Archives Found

| Archive | Size | SHA256 |
|---------|------|--------|
| `00-ORCHESTRATION.zip` | 648K | `b8a15431a2a2eac6559104d903e7d1ac4875a2e4931a317f2c2d29d3bcc22b69` |
| `DEFRAG_CONVICTION_PASS_20260117_1609.zip` | 62K | `b33fd79a467e4b7cd9e02d6594f3a70ed7f91e462da3eb8a1306d1a402b28ad3` |
| `RING7_PHASESHIFT_PASS_20260116_2219.zip` | 36K | `45023dc7f3a3aacffd285d1fb6961474c58276e735bd4a11fc19419443e0a624` |
| `TELEOLOGY_PASS_4_20260117_1430.zip` | 42K | `f04042f8e00ff44619d0227bf32d087aa483c0606107debcffa808340260929c` |
| `TELEOLOGY_RING7_PASS_3_20260116_2330.zip` | 47K | `f3a6add2dc7ba1cb952cf75dd8231c96b4a3dec724deb566f088064b7466f9de` |
| `teleology_visibility_pass_2_20260116_203238.zip` | 102K | `b632068f1b0f1eee4e6204024d8d63acc37f2dffd5aa0b6f6313b1836e479dca` |
| `teleology_visibility_pass_20260116_192327.zip` | 110K | `54a47176e843b0c2ad245d065c0e796b01bd8d2f2bca0c1ea4ec129991ceb1ab` |

**Location**: All archives in `-OUTGOING/`

---

## Extraction Summary

All 7 archives extracted to: `/tmp/corpus_survey_extracted/20260119/`

| Archive | Status |
|---------|--------|
| 00-ORCHESTRATION | Extracted |
| DEFRAG_CONVICTION_PASS_20260117_1609 | Extracted |
| RING7_PHASESHIFT_PASS_20260116_2219 | Extracted |
| TELEOLOGY_PASS_4_20260117_1430 | Extracted |
| TELEOLOGY_RING7_PASS_3_20260116_2330 | Extracted |
| teleology_visibility_pass_2_20260116_203238 | Extracted |
| teleology_visibility_pass_20260116_192327 | Extracted |

---

## High-Level Findings

### Repository Health
- **Total files**: 784 (excluding .git, .obsidian, .tmp, .DS_Store)
- **Primary extension**: `.md` (577 files, 73%)
- **Validation**: PASS (structural_verify: 0 errors, 3 warnings; ops_lint: 0 errors)

### Key Issues Identified
1. **Legacy path references**: 49 files still reference `OUTGOING/` or `outgoing/` (should be `-OUTGOING/`)
2. **Audizable marker drift**: Recent ripple (2026-01-19) retired `===AUDIZABLE===` markers in favor of final-fence convention, but 9 files still contain legacy markers
3. **Config/coordination references**: 25 stale references to `config/coordination` path

### Archive Contents Analysis
- Archives contain historical passes (teleology, defrag, ring7 phaseshift)
- `00-ORCHESTRATION.zip` appears to be a full backup of the orchestration zone
- Evidence of multi-model bakeoff (TURBINE_BAKEOFF_20260117_1900) comparing Claude Code vs Codex CLI

---

## Validation Heartbeat

### Structural Verification
```
✓ -OUTGOING/ exists
✓ -INBOX/ exists
✓ Only sanctioned directories at root
✓ No orphan files at root
✓ All COCKPIT.md paths resolve
⚠ Found 25 references to config/coordination
⚠ Found 18 legacy 'OUTGOING/' references
⚠ Found 60 lowercase 'outgoing/' references
✓ -INBOX/blitzkrieg_drop/ exists (3 files)
✓ Continuation packet type defined in schema

SUMMARY: 3 warnings (0 errors)
```

### Operations Lint
```
Files checked: 17
Errors: 0
Warnings: 0

LINT PASSED: All checked files have valid frontmatter
```

---

## Recommended Next Actions

1. **Fix legacy path references**: Batch update 49 files from `OUTGOING/` to `-OUTGOING/`
2. **Clean audizable marker remnants**: Complete the ripple from 2026-01-19 in evidence files
3. **Archive decision**: Determine if historical zip files should be moved to `05-MEMORY/` or remain in `-OUTGOING/` as export capsules
4. **Config/coordination cleanup**: Update or remove 25 stale path references post-defrag
5. **Commit staged changes**: 18 modified files need commit to stabilize state
