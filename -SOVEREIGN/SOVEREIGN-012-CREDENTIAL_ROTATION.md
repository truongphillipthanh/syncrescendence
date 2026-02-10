# SOVEREIGN-012: Credential Rotation Required

**Status**: PENDING
**Priority**: P0-Critical
**Date**: 2026-02-09
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
- `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-09-mba-ajna-setup.md`
- `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-09-ecosystem-bifurcated-analysis.md`
- `00-ORCHESTRATION/state/impl/GUIDE-MCP-AUTH-SETUP.md`
- `00-ORCHESTRATION/state/impl/tooling/OUTFITMENT-SYNC.md`
- `04-SOURCES/research/openai_research.md`
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

*Filed by Commander as part of Deep Audit 2026-02-09*
