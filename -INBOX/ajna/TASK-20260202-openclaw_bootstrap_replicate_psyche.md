# TASK-20260202-openclaw_bootstrap_replicate_psyche

**From**: Psyche
**To**: Ajna (Mac mini)
**Issued**: 2026-02-02
**Priority**: P0
**Status**: PENDING

---

## Objective

Replicate the Psyche OpenClaw-side bootstrap (governance + pointers + memory_search) onto the Ajna Mac mini OpenClaw instance.

## Bundle

Use:
- `-OUTGOING/OPENCLAW_BOOTSTRAP_AJNA_BUNDLE.md`

## Constraints

- Preserve Ajna’s identity (don’t rename Ajna → Psyche).
- Do not commit secrets into git or task files.

## Work

1) Create/overwrite Ajna OpenClaw workspace files per bundle (SOUL.md, USER.md, SYNCRESCENDENCE.md, MEMORY.md).
2) Enable memory_search on Ajna using OpenAI embeddings:
   - Phillip will paste the OpenAI key manually.
   - Configure provider=openai, model=text-embedding-3-small.
   - Include the canonical repo `extraPaths` listed in the bundle.
3) Restart gateway and build index:
   - `openclaw gateway restart`
   - `openclaw memory index --force --verbose`
4) Verify:
   - `openclaw memory status` shows indexed files + chunks
   - `openclaw memory search "Objective Lock" ...` returns hits

## Expected Output

Write:
- `-OUTGOING/RESULT-ajna-20260202-openclaw_bootstrap_replicate_psyche.md`

Include:
- which files were written under `~/.openclaw/workspace/`
- `openclaw memory status` summary
- any blockers
