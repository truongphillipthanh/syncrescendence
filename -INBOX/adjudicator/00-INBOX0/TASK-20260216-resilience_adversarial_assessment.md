# TASK-20260216-resilience_adversarial_assessment

**Priority**: P0
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: adjudicator
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T00:00:00Z

---

## Objective

ADVERSARIAL RESILIENCE ASSESSMENT: The Sovereign will physically unplug the Mac mini power cable. When power is restored, the constellation must reach 100% operational state AUTONOMOUSLY. Your job: enumerate every single point of failure in the recovery chain and rate each one.

### The Recovery Chain (assess each link)

1. **Power restored → Mac mini boots**: `systemsetup -setrestartpowerfailure on` (documented UNRELIABLE on M1/M2). `pmset repeat poweron MTWRFSU 00:00:00` as fallback (max 24h delay).

2. **macOS login**: Auto-login requires FileVault disabled. If FileVault is ON, manual password entry is required — this is a hard blocker for fully autonomous recovery.

3. **launchd agents fire**: 12+ agents with RunAtLoad. Verify they ALL actually start after reboot. Check for dependency ordering issues (Docker must be ready before containers, tmux must exist before cockpit).

4. **Docker Desktop starts**: GUI-only auto-start setting. We added a launchd fallback (`com.syncrescendence.docker-autostart.plist`). Does it actually work? Docker Desktop startup takes 30-60s — do containers auto-start?

5. **tmux constellation session recreated**: tmux-continuum can auto-restore if activated. But tmux-continuum needs a terminal to trigger it. Without a GUI terminal, it doesn't fire. We need cockpit.sh --launch-detached as a launchd agent.

6. **4 agent CLIs launched**: cockpit.sh must launch Claude Code, Codex CLI, Gemini CLI, OpenClaw in correct panes. Each CLI needs its own initialization.

7. **Auto-ingest loops started**: auto_ingest_loop.sh for each agent. Currently started manually in tmux ingest window.

8. **Watchdog resumes monitoring**: Already a launchd agent (RunAtLoad). Should auto-start.

### Your Deliverable

Write a RESULT file with:

1. **Attack Surface Enumeration**: Every single point of failure, numbered
2. **Risk Rating**: CRITICAL (blocks autonomous recovery) | HIGH (degrades within 1h) | MEDIUM (degrades within 24h) | LOW (cosmetic)
3. **Current Defense**: What protection exists now (if any)
4. **Proposed Fix**: Specific code/config change needed
5. **Dependency Graph**: Which fixes must be applied in what order

Write result to: `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260216-resilience_adversarial_assessment.md`
