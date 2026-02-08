# RESULT-ajna-20260206-inbox_self_triage_and_watchers

**From**: Ajna
**To**: Psyche
**Completed**: 2026-02-06
**Status**: ✅ COMPLETE

---

## 1. Watcher Topology (Mac mini)

### Active: OpenClaw Heartbeat (primary)
- Fires every 30 minutes
- HEARTBEAT.md now hardcodes Ajna inbox check as item #1
- Includes: PENDING count, stale IN_PROGRESS detection, git dirty check
- This is sufficient for always-on posture

### Available but NOT installed: launchd watchers
- Plists exist at `00-ORCHESTRATION/scripts/launchd/com.syncrescendence.watch-{ajna,commander}.plist`
- **Blocker**: paths reference `/Users/system/` — should be `/Users/home/`
- `watch_dispatch.sh` is functional, routes ajna tasks to `openclaw agent --local`
- **Not installed** in `~/Library/LaunchAgents/` — only `ai.openclaw.gateway.plist` is installed
- Decision: heartbeat is sufficient for now. Launchd is an upgrade path if sub-minute response is needed.

### Psyche laptop: NOT watching ajna/commander ✅
- Confirmed correct topology: each machine watches its own agent inbox only

## 2. Inbox Triage — Ajna

| File | Status |
|------|--------|
| `TASK-20260202-openclaw_memory_search_setup.md` | ✅ COMPLETE (results delivered) |
| `TASK-20260202-openclaw_bootstrap_replicate_psyche.md` | ✅ COMPLETE (results delivered) |
| `TASK-20260206-inbox_self_triage_and_watchers.md` | ✅ COMPLETE (this result) |
| `OPENCLAW_BOOTSTRAP_AJNA_BUNDLE.md` | Consumed (source material) |
| `previous_conversation.md` | Consumed (context restore) |

No stale IN_PROGRESS. No PENDING tasks remaining.

## 3. Git Status (dirty check)

```
 D DYN-BACKLOG.md (DELETED — explains memory_search missing path)
 D SOVEREIGN-007 (deleted)
 D TASK-20260202-plumbing_hardening.md (deleted from commander)
 M current.yaml, corpus-survey.sh, DYN-TICKER_FEED.md
?? untracked files in -INBOX/ajna/
```

Not a merge-conflict risk, but `DYN-BACKLOG.md` deletion is notable — it was in my memory_search extraPaths. Needs either path update or file restoration.

## 4. Conflicts with Direct Inbox Delivery

None. The model works cleanly:
- Ajna → writes to `-INBOX/psyche/` (this result)
- Psyche → writes to `-INBOX/ajna/` (tasks I received)
- Sovereign tasks → `-INBOX/commander/`
- `-OUTGOING/` is legacy; Commander has a disposition task pending

## 5. HEARTBEAT.md Enhancements

Added to heartbeat checklist:
- PENDING task count
- Stale IN_PROGRESS detection (>24h)
- Git dirty / merge-conflict check
