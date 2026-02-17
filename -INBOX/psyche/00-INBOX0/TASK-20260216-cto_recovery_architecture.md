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

CTO RESILIENCE ARCHITECTURE: The Sovereign will physically unplug the Mac mini. When power is restored, the entire constellation must self-heal to 100% operational. As CTO, design the recovery architecture.

### Context

Commander has already:
1. Written `00-ORCHESTRATION/scripts/configure_auto_boot_recovery.sh` — configures auto-boot, launchd agents, Docker fallback, tmux-continuum
2. Identified the critical gap: cockpit.sh needs a `--launch-detached` mode
3. Identified the FileVault blocker: if enabled, manual password required on boot

### Your Deliverable (CTO Assessment)

1. **Docker Auto-Recovery**:
   - Verify Docker Desktop "Start on login" is enabled on this machine
   - Check container restart policies: `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container>` for Neo4j, Graphiti, Qdrant, Chroma
   - Set restart policies to `unless-stopped` if not already: `docker update --restart unless-stopped <container>`
   - Verify containers come back after Docker daemon restart

2. **cockpit.sh --launch-detached Implementation**:
   - Read current `00-ORCHESTRATION/scripts/cockpit.sh`
   - Implement a `--launch-detached` flag that:
     a. Creates the `constellation` tmux session (if not exists)
     b. Creates all 8 panes with correct layout
     c. Launches Claude Code in pane 1.3
     d. Launches Codex CLI in pane 1.5
     e. Launches `gemini` TUI in pane 1.7 (for monitoring; headless runs separately)
     f. Launches OpenClaw TUI in pane 1.1
     g. Does NOT attach (returns control to launchd)
   - Commit the implementation

3. **Auto-Ingest Loop Auto-Start**:
   - Currently started manually in tmux ingest window
   - Create launchd agents OR modify cockpit.sh to also start auto-ingest loops
   - Each loop: `auto_ingest_loop.sh <agent> /Users/home/Desktop/syncrescendence constellation <pane>`

4. **FileVault Assessment**:
   - Check: `fdesetup status`
   - If ON: document the trade-off (security vs. autonomous boot)
   - Propose: Can we use a smart plug + Wake-on-LAN as alternative to auto-boot?

5. **End-to-End Recovery Test Plan**:
   - Step-by-step procedure to simulate power loss
   - Expected state at each phase
   - Verification commands

Write result to: `-OUTBOX/psyche/RESULTS/RESULT-psyche-20260216-cto_recovery_architecture.md`

Also commit any code changes you make (cockpit.sh, Docker config, launchd agents).
