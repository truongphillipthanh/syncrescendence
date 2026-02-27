# TASK-20260217-corpus_freshness

**From**: orchestrator
**To**: Cartographer (Gemini CLI)
**Reply-To**: orchestrator
**Issued**: 2026-02-17 08:28:01
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
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: orchestrator
**Escalation-Delay**: 10

---

## Objective

Survey the praxis corpus for freshness. Identify any mechanics/ or practice/ files not updated in the last 14 days. Check for orphaned references (files mentioned in indexes but missing). Report corpus health metrics: total files, average age, stalest file, any broken cross-references.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260217-corpus_freshness.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: corpus_freshness complete" && git push`
