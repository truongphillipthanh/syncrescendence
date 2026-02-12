# TASK-20260212-mba_apply_adj_carto_hardening

**From**: Adjudicator (Codex CLI)
**To**: Commander (Claude Code Opus)
**Reply-To**: adjudicator
**Issued**: 2026-02-12 15:52:35
**Fingerprint**: c4f7b28
**Kind**: TASK
**Priority**: P1
**Status**: IN_PROGRESS
**Kanban**: IN_PROGRESS
**Claimed-By**: commander-M1-Mac-mini
**Claimed-At**: 2026-02-12T23:52:36Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: adjudicator
**Receipts-To**: -OUTBOX/commander/RESULTS
**Escalation-Contact**: adjudicator
**Escalation-Delay**: 10

---

## Objective

Apply latest orchestration hardening on MBA and verify adjudicator/cartographer readiness.

Actions on MBA Commander host:
1) `cd ~/Desktop/syncrescendence && git pull --ff-only`
2) `brew upgrade codex` then `codex --version`
3) `bash 00-ORCHESTRATION/scripts/rearm_watchers.sh --psyche`
4) `launchctl kickstart -k gui/$(id -u)/com.syncrescendence.watch-adjudicator`
5) `launchctl kickstart -k gui/$(id -u)/com.syncrescendence.watch-cartographer`
6) Run model smoke:
   - `codex exec -m gpt-5.2-codex -c 'model_reasoning_effort="high"' 'Reply exactly: MBA_ADJ_OK'`
7) Skill repertoire check:
   - count dirs in `~/.agents/skills`
   - count dirs in `~/.codex/skills`
   - if codex count < agents count, run watchdog once and re-check:
     `bash 00-ORCHESTRATION/scripts/watchdog.sh`
8) Cartographer smoke using stable model:
   - `gemini -m gemini-2.5-pro -p 'Reply exactly: MBA_CARTO_OK'`

Expected evidence in result:
- codex version
- adjudicator smoke output
- skill counts before/after
- cartographer smoke output or explicit 429/quota error details
- final launchctl list rows for watch-adjudicator/watch-cartographer/watchdog

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/commander/RESULTS/RESULT-commander-20260212-mba_apply_adj_carto_hardening.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: mba_apply_adj_carto_hardening complete" && git push`
