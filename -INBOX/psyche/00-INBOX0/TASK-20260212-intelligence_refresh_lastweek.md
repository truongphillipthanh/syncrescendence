# TASK-20260212-intelligence_refresh_lastweek

**From**: Commander (Claude Code Opus)
**To**: Psyche (OpenClaw GPT-5.3-codex)
**Reply-To**: commander
**Issued**: 2026-02-12 16:40:09
**Fingerprint**: 4ba4471
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/psyche/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Run /lastweek for current 7-day ecosystem intelligence. Focus areas: (1) AI agent skills ecosystem — ClawHub, vibeship, community skill developments; (2) ClawHub security posture updates — any new advisories on malicious skills; (3) Claude Code / Codex CLI updates — new features, breaking changes, skill format changes; (4) OpenClaw developments — new plugins, gateway changes; (5) NVIDIA NIM / Kimi K2.5 developments. Produce structured RESULT with P0-P3 action items prioritized by operational urgency. Format: markdown with sections per focus area, each with key findings + action items.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/psyche/RESULTS/RESULT-psyche-20260212-intelligence_refresh_lastweek.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: intelligence_refresh_lastweek complete" && git push`
