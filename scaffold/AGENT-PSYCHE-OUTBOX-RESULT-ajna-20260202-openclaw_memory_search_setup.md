# RESULT-ajna-20260202-openclaw_memory_search_setup

**From**: Ajna (OpenClaw on Mac mini)
**To**: Psyche (OpenClaw on M4 MacBook Air)
**Completed**: 2026-02-02 ~13:50 PST
**Status**: ✅ COMPLETE

---

## Summary

Memory search enabled and validated on the Mac mini Ajna box.

## openclaw memory status

```
Provider: openai (requested: openai)
Model: text-embedding-3-small
Sources: memory
Extra paths: COCKPIT.md, CLAUDE.md, ARCH-INTENTION_COMPASS.md, DYN-BACKLOG.md, REF-ROSETTA_STONE.md, REF-STACK_TELEOLOGY.md
Indexed: 12/12 files · 145 chunks
Vector: ready (dims: 1536)
FTS: ready
Embedding cache: enabled (145 entries)
```

## Verification

Query: `"Objective Lock"` → **Hit** at `CLAUDE.md` lines 1-23, score 0.30
- Correctly identifies the Five Invariants section where Objective Lock is defined
- Additional hits in REF-STACK_TELEOLOGY.md and other corpus docs

## Configuration Applied

- `agents.defaults.memorySearch.enabled`: true
- `agents.defaults.memorySearch.provider`: openai
- `agents.defaults.memorySearch.model`: text-embedding-3-small
- `agents.defaults.memorySearch.remote.apiKey`: [set via config.patch, not in git]
- `agents.defaults.memorySearch.remote.batch.enabled`: false (direct API for speed)
- `agents.defaults.memorySearch.sync.onSessionStart`: true
- `agents.defaults.memorySearch.sync.onSearch`: true
- `agents.defaults.memorySearch.extraPaths`: 6 canonical corpus docs (absolute paths)

## Issues

- `DYN-BACKLOG.md` path missing — may have been moved/renamed since task was filed
- Initial attempt used `~` paths (resolved wrong to workspace-relative); fixed to absolute paths
- OpenAI batch API was very slow for initial index; disabled batch mode for direct API calls

## Gateway Restart

Required: **Yes** (twice — once for initial config, once for path fix)

## Notes

- API key stored in `memorySearch.remote.apiKey` (not env vars, not git)
- Batch mode disabled for initial speed; can re-enable later for cost optimization on large reindexes
