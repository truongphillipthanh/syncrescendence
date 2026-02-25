# SIEGE CC28 — Lane 4: Dream Cycle (Circadian Sync)

**Agent**: Commander (Claude Code)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Build `circadian_sync.py` — Adjudicator Spec 2. A between-session consolidation script that "dreams" — replays journals and handoffs, deduplicates, classifies retain/forget, and appends consolidated memory.

## SPEC (from Adjudicator CC28 + Diviner's Sleep Consolidation concept)

### Architecture
```
Trigger (launchd nightly OR manual at close)
    -> circadian_sync.py
Inputs:
  - agents/commander/memory/journal/*.jsonl (session_brief + session_end + manual)
  - git log range since last sync
  - agents/commander/outbox/handoffs/HANDOFF-*.md (if dir exists, else agents/commander/outbox/HANDOFF-*.md)
  - DYN-DEFERRED_COMMITMENTS.md
Process:
  normalize -> deduplicate -> retain/forget classify -> summarize rationale-preserving
Outputs:
  - MEMORY_CONSOLIDATION.md (append-only cycles)
  - FORGET_CANDIDATES.jsonl (negative selection ledger)
  - DYN-DREAM_QUALITY.jsonl (+ md summary)
  - circadian_state.json (cursor, last commit, last ts)
```

### Process Details
1. **Load cursor** from `circadian_state.json` — get `last_commit`, `last_timestamp`
2. **Collect inputs since cursor**:
   - Journal entries from `agents/commander/memory/journal/*.jsonl` with timestamp > last_timestamp
   - Git log entries from `last_commit..HEAD`
   - New HANDOFF files (by mtime)
3. **Normalize**: Extract key facts from each source into uniform format: `{source, timestamp, fact, context, decision_ids}`
4. **Deduplicate**: Content-hash dedup — same fact from journal + git log = keep one
5. **Retain/Forget classify**:
   - RETAIN: decisions with rationale, architectural changes, new intentions, blockers, phase transitions
   - FORGET candidates: routine commits, repeated status updates, mechanical operations, stale context
   - Two-step forget: `candidate` first, then `confirmed` after N=3 cycles without reference
6. **Summarize**: Rationale-preserving compression — keep the WHY, compress the WHAT
7. **Write outputs**:
   - Append one cycle block to `MEMORY_CONSOLIDATION.md` with source commit range
   - Append forget candidates to `FORGET_CANDIDATES.jsonl`
   - Append quality metrics to `DYN-DREAM_QUALITY.jsonl`
   - Update `circadian_state.json` cursor

### Safety Rails (from Adjudicator)
- Guard: exit if active CLI process detected (check for running claude/codex processes) or dirty protected dirs
- Dream quality metric gates append — below threshold writes only as draft
- State cursor + content hash dedupe prevents duplicate cycles
- Strict fallback: include raw "unparsed excerpts" section for anything the parser can't handle
- NEVER write to canon/ or praxis/ directly — only to commander's memory space

### CLI
```bash
# Normal run
python3 orchestration/00-ORCHESTRATION/scripts/circadian_sync.py \
  --repo-root /Users/system/syncrescendence

# Dry run (show decisions without writing)
python3 orchestration/00-ORCHESTRATION/scripts/circadian_sync.py \
  --repo-root /Users/system/syncrescendence \
  --dry-run

# Force run even if active session detected
python3 orchestration/00-ORCHESTRATION/scripts/circadian_sync.py \
  --repo-root /Users/system/syncrescendence \
  --force
```

### Output Locations
- `agents/commander/memory/MEMORY_CONSOLIDATION.md` — append-only dream log
- `agents/commander/memory/sync/FORGET_CANDIDATES.jsonl` — negative selection ledger
- `agents/commander/memory/sync/circadian_state.json` — cursor state
- `orchestration/00-ORCHESTRATION/state/DYN-DREAM_QUALITY.jsonl` — quality metrics

### LaunchD Plist
Also create `orchestration/00-ORCHESTRATION/scripts/launchd/com.syncrescendence.circadian-sync.plist`:
- Run daily at 04:00
- WorkingDirectory: repo root
- EnvironmentVariables: SYNCRESCENDENCE_ROOT (do NOT rely on ~/.zshrc — launchd doesn't source it)
- StandardOutPath/StandardErrorPath: `orchestration/state/circadian.stdout.log` / `.stderr.log`

## CONSTRAINTS
- Write to `orchestration/00-ORCHESTRATION/scripts/circadian_sync.py`
- Write plist to `orchestration/00-ORCHESTRATION/scripts/launchd/com.syncrescendence.circadian-sync.plist`
- ~500 LOC target for the Python script
- Use only stdlib
- Commit with prefix `feat: CC28-L4 circadian sync (dream cycle consolidation)`
- Run with `--dry-run` and verify output before committing
- Do NOT modify any files outside your lane
