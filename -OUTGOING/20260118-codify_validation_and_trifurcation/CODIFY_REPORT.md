# Codify Report: Validation Protocol & Trifurcation Adjustments

**Date**: 2026-01-18
**Executor**: Claude Code (Opus 4.5)

## Summary

This bundle codifies two protocol changes:
1. **Repo Validation Protocol**: Standardized procedure for validating repository health
2. **Trifurcation Adjustments**: Updated output format (no explicit labels, follow-along audizable)

Additionally, all 9 legacy prompts now have YAML frontmatter, making ops_lint pass.

---

## What Changed

### 1. New Protocol: REF-REPO_VALIDATION_PROTOCOL.md

**Location**: `00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md`

Defines:
- When to run validation (post-migration, pre/post-commit, Blitzkrieg completion)
- What to check (structural, lint, directory sanity)
- How to produce reports in `-OUTGOING/`
- Remediation patterns for common failures

### 2. New Command: /repo_validate

**Location**: `.claude/commands/project/repo_validate.md`

Usage:
```
/repo_validate
```

Produces: `-OUTGOING/YYYYMMDD-repo_validation/VALIDATION_REPORT.md`

### 3. Updated: PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md

**Location**: `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md`

Changes:
- Removed requirement for explicit "Readable version:" / "Audizable version:" labels
- Readable content is inline (natural prose, no label needed)
- Audizable is a trailing artifact block (code fence labeled `audio` or after `---`)
- Follow-along alignment: audizable mirrors readable paragraph-by-paragraph
- Container format documented for automation ingestion

### 4. Updated: REF-AUDIZER_PROTOCOL.md

**Location**: `02-ENGINE/specs/REF-AUDIZER_PROTOCOL.md`

Changes:
- Added "Follow-Along Alignment" as core principle
- Added "No Over-Translation" principle (simplify structure, not soul)
- Emphasized paragraph-by-paragraph sync with readable content
- Documented integration with trifurcation workflow
- Added container format reference

### 5. Updated: REF-CHATGPT_CONTAINER_PROTOCOL.md

**Location**: `00-ORCHESTRATION/state/REF-CHATGPT_CONTAINER_PROTOCOL.md`

Changes:
- Added YAML frontmatter
- Documented "Container Grammar" concept
- Explained why markers over labels (deterministic, unambiguous)
- Added parsing rules documentation
- Linked to updated Deviser prompt

### 6. Backfilled: 9 Legacy Prompts with YAML Frontmatter

Files updated in `02-ENGINE/prompts/canonical/`:

| File | ID | Kind | Target |
|------|-----|------|--------|
| PROMPT-CHATGPT-canonical.md | chatgpt-canonical-system-prompt | system_prompt | chatgpt |
| PROMPT-CLAUDE-canonical.md | claude-canonical-system-prompt | system_prompt | claude |
| PROMPT-GEMINI-canonical.md | gemini-canonical-system-prompt | system_prompt | gemini |
| PROMPT-GROK-canonical.md | grok-canonical-system-prompt | system_prompt | grok |
| PROMPT-IMEP-CHATGPT-AUDITOR.md | imep-chatgpt-auditor | station_prompt | chatgpt |
| PROMPT-IMEP-CHATGPT-DEVISER.md | imep-chatgpt-deviser | station_prompt | chatgpt |
| PROMPT-IMEP-CLAUDE-AUDITOR.md | imep-claude-auditor | station_prompt | claude_code |
| PROMPT-IMEP-CLAUDE-ENGINEER.md | imep-claude-engineer | station_prompt | claude_code |
| PROMPT-IMEP-GEMINI-ORACLE.md | imep-gemini-oracle | station_prompt | gemini |

---

## Why These Changes

### Validation Protocol
- Standardizes what was previously ad-hoc validation runs
- Creates auditable trail in `-OUTGOING/`
- Enables `/repo_validate` command for quick health checks

### Trifurcation Adjustments
- Explicit labels ("Readable version:") felt bureaucratic and cluttered output
- Follow-along alignment makes audizable useful for read+listen mode
- Container grammar enables reliable automation without depending on human-facing text

### Frontmatter Backfill
- ops_lint was failing on 9 legacy files
- All PROMPT-* and REF-* files should be self-describing with frontmatter
- Enables future registry auto-generation and validation

---

## Verification Results

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
⚠ Found 17 legacy 'OUTGOING/' references
⚠ Found 51 lowercase 'outgoing/' references
✓ -INBOX/blitzkrieg_drop/ exists (3 files)
✓ Continuation packet type defined in schema

=== SUMMARY ===
⚠ 3 warnings (0 errors)
```

### Operations Lint

**Command**: `bash 02-ENGINE/scripts/ops_lint.sh`

**Result**: **PASS** (0 errors)

```
=== OPERATIONS ARTIFACT LINTER ===
Files checked: 17
Errors: 0
Warnings: 0

LINT PASSED: All checked files have valid frontmatter
```

---

## How to Test

### Test Validation Command
```bash
# Run the new /repo_validate command (or equivalent manual steps)
DATE=$(date +%Y%m%d)
mkdir -p "./-OUTGOING/${DATE}-repo_validation"
bash 00-ORCHESTRATION/scripts/structural_verify.sh
bash 02-ENGINE/scripts/ops_lint.sh
# Verify report is created in -OUTGOING/
```

### Test Trifurcation Format
In ChatGPT with Syncrescendence project:
1. Ask for substantive response
2. Verify: readable content inline (no "Readable version:" label)
3. Verify: audizable appears as trailing artifact block
4. Ask for "container format" output
5. Verify: markers (`===READABLE===`, etc.) present for automation

### Test Container Ingestion
```bash
# Create test input with markers
cat <<'EOF' > /tmp/test_container.txt
===READABLE===
Test readable content.

===AUDIZABLE===
Test audio script.

===END===
EOF

# Run ingestion
cat /tmp/test_container.txt | ./00-ORCHESTRATION/scripts/ingest_chatgpt_container.sh --date 20260118 --slug test --dry-run
```

---

## Files in This Bundle

```
-OUTGOING/20260118-codify_validation_and_trifurcation/
├── CODIFY_REPORT.md                    # This file
└── REF-REPO_VALIDATION_PROTOCOL.md     # Protocol copy (canonical in 00-ORCHESTRATION/state/)
```

## Files Changed in Repo

| Path | Change |
|------|--------|
| `.claude/commands/project/repo_validate.md` | Created |
| `00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md` | Created |
| `00-ORCHESTRATION/state/REF-CHATGPT_CONTAINER_PROTOCOL.md` | Updated (frontmatter, grammar docs) |
| `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md` | Updated v2.0.0 |
| `02-ENGINE/specs/REF-AUDIZER_PROTOCOL.md` | Updated v2.0.0 |
| `02-ENGINE/prompts/canonical/PROMPT-CHATGPT-canonical.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-CLAUDE-canonical.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-GEMINI-canonical.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-GROK-canonical.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-IMEP-CHATGPT-AUDITOR.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-IMEP-CHATGPT-DEVISER.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-IMEP-CLAUDE-AUDITOR.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-IMEP-CLAUDE-ENGINEER.md` | Frontmatter added |
| `02-ENGINE/prompts/canonical/PROMPT-IMEP-GEMINI-ORACLE.md` | Frontmatter added |

---

## Next Steps

1. **Commit changes**: `git add -A && git commit -m "feat: codify validation protocol + trifurcation adjustments"`
2. **Update ChatGPT project instructions**: Copy updated Deviser prompt to ChatGPT project settings
3. **Clean legacy references** (optional): Address the 3 warnings from structural verification
