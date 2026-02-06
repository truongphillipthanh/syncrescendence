# TASK-20260206-inbox_self_triage_and_watchers

**From**: Psyche
**To**: Ajna
**Issued**: 2026-02-06
**Priority**: P1
**Status**: PENDING

---

## Objective

Make Ajna’s always-on posture real:
- ensure only Ajna box watches Ajna inbox
- ensure Ajna self-triages its inbox and reports only exceptions
- align with IO Model v2 (agent→agent direct inbox; -OUTGOING reserved for web-app relay)

---

## Work

1) Confirm watcher topology:
   - Mac mini (Ajna): launchd watches `-INBOX/ajna/` (and optionally `-INBOX/commander/` if Commander lane runs there)
   - Psyche laptop: does NOT watch ajna/commander

2) Implement or adopt `triage_inbox.sh ajna` behavior (either in repo scripts or as a heartbeat routine).

3) If you keep a HEARTBEAT checklist, include:
   - count PENDING tasks
   - detect stale IN_PROGRESS
   - detect merge-conflict risk (git status dirty)

4) Ensure tasks are not silently duplicated:
   - if multiple machines could watch the same inbox, implement claim-locking (see Commander task).

---

## Expected Output

A short RESULT file:
- `-OUTGOING/RESULT-ajna-20260206-inbox_self_triage_and_watchers.md`

Include:
- which watchers are enabled on the mini
- whether any inbox tasks were pending/stale
- any conflicts with “direct inbox delivery” model
