# TASK: Document autonomous orchestration architecture

**Status**: PENDING
**Priority**: P1
**Reply-To**: commander
**CC**: commander
**To**: cartographer
**Timeout**: 300

## Objective

Create `00-ORCHESTRATION/state/ARCH-AUTONOMOUS_ORCHESTRATION.md` documenting the full autonomous orchestration system being built right now. This is the architecture document for how the constellation self-heals, self-dispatches, and self-coordinates.

Research the current scripts to understand the system, then document:

### Section 1: System Overview
- The constellation has 5 agents across 2 machines (MBA + Mac mini)
- Task lifecycle: dispatch → SCP sling → auto_ingest → execution → RESULT → CONFIRM → SCP-back
- Three automation layers: auto_ingest (task execution), watchdog (health monitoring), proactive_orchestrator (work generation)

### Section 2: Auto-Ingest System
- auto_ingest_supervisor.sh spawns loops for each agent
- auto_ingest_loop.sh polls INBOX0, dispatches to agent CLI, monitors completion
- Retry logic: transient failures auto-retry up to 3x, then escalate to -SOVEREIGN/
- CONFIRM SCP-back: cross-machine delivery of completion signals

### Section 3: Health Watchdog
- constellation_watchdog.sh runs every 60s via launchd
- Monitors 4 agent panes + Neural Bridge SSH + Docker
- Health-triggered recovery: heartbeat for STALE, interrupt for stuck, Docker restart for DOWN
- Sovereign alerts for unrecoverable errors

### Section 4: Proactive Orchestrator
- proactive_orchestrator.sh runs every 5 minutes via launchd
- Cleans stale IN_PROGRESS tasks (>30min → FAILED)
- Writes DYN-CONSTELLATION_STATE.md (cross-agent awareness)
- Dispatches health checks to idle agents

### Section 5: Recovery Chain (Boot to Operational)
- Power → POST → auto-boot → macOS → auto-login (FileVault off) → launchd → Docker (Login Items) → tmux (cockpit) → auto-ingest → watchdog → orchestrator → OPERATIONAL

### Section 6: State Machine Diagram
Document the task state machine:
```
00-INBOX0 (PENDING) → 10-IN_PROGRESS (CLAIMED) → 40-DONE (COMPLETE)
                                                 → 50_FAILED (FAILED)
                                                     → 00-INBOX0 (RETRY, up to 3x)
                                                     → -SOVEREIGN/ (ESCALATION)
```

### Section 7: Failure Modes and Recovery
Table of failure modes, detection method, and automated recovery action.

Read the actual scripts (auto_ingest_loop.sh, constellation_watchdog.sh, auto_ingest_supervisor.sh, dispatch.sh) to document accurately. Do NOT make assumptions — verify against code.

**Reply-To**: commander
**CC**: commander
