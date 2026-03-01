# TASK-20260217-infrastructure_audit

**From**: orchestrator
**To**: Psyche (OpenClaw GPT-5.3-codex)
**Reply-To**: orchestrator
**Issued**: 2026-02-17 08:27:59
**Fingerprint**: 96d4055
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: —
**Receipts-To**: -OUTBOX/psyche/RESULTS
**Escalation-Contact**: orchestrator
**Escalation-Delay**: 10

---

## Objective

Run infrastructure coherence audit: verify launchd plists match template copies in orchestration/scripts/launchd-mini/, check that watchdog is running and reporting, verify Docker container restart policies, confirm auto-ingest supervisor is active. Report any drift between deployed and template configurations.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/psyche/RESULTS/RESULT-psyche-20260217-infrastructure_audit.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: infrastructure_audit complete" && git push`
