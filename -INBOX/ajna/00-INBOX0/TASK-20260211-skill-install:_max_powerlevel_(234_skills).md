# TASK-20260211-skill-install:_max_powerlevel_(234_skills)

**From**: Commander (Claude Code Opus)
**To**: Ajna (OpenClaw Opus 4.5)
**Reply-To**: commander
**Issued**: 2026-02-11 19:42:47
**Fingerprint**: 34ac8ce
**Kind**: TASK
**Priority**: P1
**Status**: ESCALATED
**Kanban**: INBOX0
**Claimed-By**: ajna-M1-Mac-mini
**Claimed-At**: 2026-02-12T03:42:48Z
**Completed-At**: 2026-02-12T03:46:23Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/ajna/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Sovereign will transfer skills-full-234.tar.gz (40MB) via AirDrop. Run install-skills-mba.sh to unpack 234 skills to ~/.agents/skills/, symlink to ~/.openclaw/skills/ and ~/.codex/skills/. After install: verify count with 'ls ~/.openclaw/skills/ | wc -l', confirm 234. Then list your top 10 CSO-relevant skills (strategy, planning, analysis, brainstorming). Report back via -OUTGOING/ commit.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/ajna/RESULTS/RESULT-ajna-20260211-skill-install:_max_powerlevel_(234_skills).md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: skill-install:_max_powerlevel_(234_skills) complete" && git push`

---
**Failure-Code**: STALE_TIMEOUT
**Failure-Class**: timeout
**Failure-Retryable**: true
**Failure-Reason**: stale_in_progress_timeout
**Failed-At**: 2026-02-20T04:12:47Z
**Stale-Duration**: 193184s (threshold: 1800s)
**Moved-By**: proactive_orchestrator.sh

**Retry-Count**: 1
**Retried-At**: 2026-02-20T04:23:03Z
**Retried-By**: proactive_orchestrator.sh
