# TASK-20260216-cto_recovery_architecture

**Priority**: P0
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: psyche
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T00:00:00Z

---

## Objective

CTO RESILIENCE ARCHITECTURE: The Sovereign will physically unplug the Mac mini. Design and implement the recovery architecture so the constellation self-heals to 100%.

### Actions Required

1. Docker: verify container restart policies (set to unless-stopped), verify Docker auto-start
2. cockpit.sh: implement --launch-detached mode (create tmux session + launch all 4 CLIs without attaching)
3. Auto-ingest loops: create launchd agents or integrate into cockpit.sh so they auto-start
4. FileVault: check fdesetup status, document trade-off
5. End-to-end test plan: step-by-step recovery simulation procedure

Commander wrote configure_auto_boot_recovery.sh in 00-ORCHESTRATION/scripts/ — review and enhance it.

Write to: -OUTBOX/psyche/RESULTS/RESULT-psyche-20260216-cto_recovery_architecture.md
Also commit any code changes.
