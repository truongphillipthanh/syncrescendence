# SOVEREIGN-012: Credential Rotation Required

**Status**: FULLY RESOLVED
**Priority**: P0-Critical
**Date**: 2026-02-09
**Resolved**: 2026-02-10
**From**: Commander (Deep Audit)

---

## Finding

**16 tracked files** in the repository contain plaintext API credentials:

### Affected Credentials
1. **Linear API key** (`lin_api_S34H...`)
2. **ClickUp API token** (`pk_126030...`)
3. **OpenAI API key** (`sk-proj-JZg...`)
4. **Neo4j password** (`graphiti_memory_2026`)

### Affected Files (tracked in git history)
- `orchestration/state/impl/clarescence/CLARESCENCE-2026-02-09-mba-ajna-setup.md`
- `orchestration/state/impl/clarescence/CLARESCENCE-2026-02-09-ecosystem-bifurcated-analysis.md`
- `orchestration/state/impl/GUIDE-MCP-AUTH-SETUP.md`
- `orchestration/state/impl/tooling/OUTFITMENT-SYNC.md`
- `sources/research/openai_research.md`
- Multiple `-INBOX/` and `-OUTGOING/` task/result files

### Risk Assessment
- **Repository is PRIVATE** on GitHub (not public exposure)
- **Git history retains credentials** even if removed from files now
- **Linear/ClickUp**: Workspace-level tokens, moderate risk
- **OpenAI**: Project-scoped key, can be rotated
- **Neo4j**: Local-only (localhost), low risk

## Sovereign Decision Required

1. **Rotate keys?** Generate new API keys for Linear, ClickUp, OpenAI
2. **Scrub git history?** Use `git filter-repo` to remove credential patterns (destructive, requires force push)
3. **Environment variable migration?** Replace inline credentials with `$ENV_VAR` references in all files
4. **Accept risk?** Private repo, no external collaborators — document and move on

### Commander Recommendation
Option 3 (env var migration) for new files + Option 1 (rotate) for Linear/ClickUp/OpenAI. Skip git history scrub (Option 2) — too destructive for a private repo with no external exposure. Accept Neo4j password risk since it's localhost-only.

---

## Resolution (2026-02-10)

**Sovereign Decision**: Proceed with recommendation (Option 3 env var migration + Option 1 rotate).

**Executed**:
1. **Env var migration**: All plaintext credentials redacted from repo files. Replaced with `${ENV_VAR}` references. Credentials stored in `~/.syncrescendence/.env` (already gitignored).
2. **MEMORY.md redacted**: Commander's auto-memory updated to reference env vars instead of plaintext keys.
3. **Files cleaned**: `CLARESCENCE-2026-02-09-mba-ajna-setup.md` — 2x OpenAI key + 2x gateway token redacted.

**Phase 2 — Key Rotation COMPLETE (2026-02-10)**:
- **Linear API key**: Rotated to `lin_api_Rfay...` — verified working
- **ClickUp API token**: Rotated to `pk_126030281_QU0M...` — verified working
- **OpenAI API key**: Rotated to `sk-proj-xr3e...` — verified working
- **Google AI Studio key**: New key added `AIzaSyBT0g...` — verified (45 models accessible)
- **OpenClaw .env synced**: `~/.openclaw/.env` updated with new OpenAI key
- **All 4 keys verified via live API calls** — 2026-02-10
- Git history scrub SKIPPED per recommendation (private repo, no external exposure)

*Filed by Commander as part of Deep Audit 2026-02-09. Fully resolved 2026-02-10.*
