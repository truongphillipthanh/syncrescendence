---
id: operations-inbox-migration-20260118
kind: archaeology
scope: repo
target: repo
date: 2026-01-18
---

# Operations Inbox Migration Receipt

**Date**: 2026-01-18
**Executor**: Claude Code (Opus 4.5)
**Directive**: Migrate -INBOX artifacts to 02-ENGINE canonical locations

## Files Migrated

| Original Path | New Path | Notes |
|---------------|----------|-------|
| `-INBOX/deviser_prompt_chatgpt.md` | `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md` | Added YAML frontmatter |
| `-INBOX/audizer.md` | `02-ENGINE/specs/REF-AUDIZER_PROTOCOL.md` | Added YAML frontmatter |
| `-INBOX/operations_artifact_taxonomy.md` | `02-ENGINE/registries/REF-OPERATIONS_ARTIFACT_TAXONOMY.md` | Fixed frontmatter format |
| `-INBOX/chatpgt_memory_policy.md` | `02-ENGINE/specs/REF-CHATGPT_MEMORY_POLICY.md` | Fixed typo in filename, added frontmatter |
| `-INBOX/chatgpt_global_memory1.md` | `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-GLOBAL_MEMORY_REGISTRATION.md` | Added YAML frontmatter |
| `-INBOX/chatgpt_syncrescendence_project_memory.md` | `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_MEMORY_ANCHOR-SYNCRESCENDENCE.md` | Added YAML frontmatter |

## Files Retained in -INBOX

| Path | Reason |
|------|--------|
| `-INBOX/blitzkrieg_drop/` | Sanctioned dropbox for blitzkrieg intake |
| `-INBOX/blitzkrieg_drop/context.md` | Active blitzkrieg context |
| `-INBOX/blitzkrieg_drop/directive-01.md` | Active directive |
| `-INBOX/blitzkrieg_drop/directive-02.md` | Active directive |

## New Files Created

| Path | Purpose |
|------|---------|
| `02-ENGINE/registries/REF-PROMPT_REGISTRY.md` | Index of all PROMPT-* files |
| `02-ENGINE/registries/REF-OPERATIONS_TREE.md` | Directory map for 02-ENGINE |
| `02-ENGINE/scripts/ops_lint.sh` | Frontmatter validation linter |

## Directories Created

- `02-ENGINE/prompts/chatgpt/`
- `02-ENGINE/specs/`
- `02-ENGINE/registries/`

## Files Redacted/Ignored

None. No secrets, tokens, or sensitive credentials were found in the migrated files.

## Backlog Updated

Added OPS-TAXONOMY work item to `00-ORCHESTRATION/state/DYN-BACKLOG.md` documenting:
- Completed work from this migration
- Remaining work (backfill legacy prompts, CI integration, etc.)

## Verification Commands

```bash
# Check -INBOX is clean (only blitzkrieg_drop remains)
ls -la -INBOX/

# Verify new files exist
ls -la 02-ENGINE/prompts/chatgpt/
ls -la 02-ENGINE/specs/
ls -la 02-ENGINE/registries/
ls -la 02-ENGINE/scripts/

# Run ops linter
bash 02-ENGINE/scripts/ops_lint.sh

# Run structural validator
bash 00-ORCHESTRATION/scripts/structural_verify.sh
```

## Notes

1. The directory is `02-ENGINE` (not `02-OPERATIONS` as referenced in some documents)
2. Legacy prompts in `02-ENGINE/prompts/canonical/` lack YAML frontmatter - marked for backfill
3. `-INBOX/blitzkrieg_drop/` retained as sanctioned intake dropbox per Blitzkrieg Protocol
