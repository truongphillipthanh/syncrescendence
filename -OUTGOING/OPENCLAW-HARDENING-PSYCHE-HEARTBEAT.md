# Heartbeat Configuration — Psyche (CTO)

## Interval
Every 30 minutes during working hours (9am-11pm)

## Infrastructure Health Checks (MANDATORY)

### Tier 1: Constellation Health (every heartbeat)
1. Read `00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md` — check all agent states
2. Check `-INBOX/psyche/00-INBOX0/` for TASK-*, CONFIRM-*, RESULT-* files
3. Check git log for commits by other agents since last heartbeat
4. Review ARCH-INTENTION_COMPASS.md for Sovereign intent signals

### Tier 2: Auto-Ingest Health (every 2nd heartbeat)
5. Verify auto-ingest loops are running: check for `.auto_ingest.lock` files in each agent's INBOX
6. Check for stale tasks in `10-IN_PROGRESS/` (>30 min = investigate)
7. Check for FAILED tasks in `50_FAILED/` — these may need retry or escalation
8. Review `auto_ingest.log` tails for ERROR or TIMEOUT entries

### Tier 3: Service Health (every 3rd heartbeat)
9. Check Docker health: `docker ps --format '{{.Names}} {{.Status}}'`
   - Neo4j (:7474), Graphiti (:8001), Qdrant (:6333), Chroma (:8765)
10. Check OpenClaw gateway health: `curl -s http://localhost:18789/health`
11. Verify watchdog launchd: `launchctl list | grep syncrescendence`
12. Verify tmux constellation session: `tmux has-session -t constellation`

### Tier 4: Pipeline Cohesion (every 6th heartbeat)
13. Verify all auto-ingest loops running (check all 4 agent lockfiles + PIDs)
14. Verify cross-machine dispatch env vars: `env | grep SYNCRESCENDENCE_REMOTE`
15. Check disk space: `df -h /Users/home`

## Notification Criteria
Only notify Sovereign if:
- P0 task dispatched by Sovereign or Ajna
- Infrastructure failure (Docker down, gateway unreachable, auto-ingest crashed)
- Agent conflict (merge collision, inbox deadlock)
- Policy violation detected (Constitutional Rules breach)
- Budget depletion on any agent's model tier
- **Any agent showing ERROR or STALE in watchdog health for >5 minutes**
- **Auto-ingest loop crashed (missing lockfile + no running process)**
- **Docker container exited unexpectedly**

## Do NOT notify for:
- Routine task completions
- IDLE agents with empty inboxes (normal state)
- Non-urgent status updates
- Things that can wait until next Sovereign session

## Proactive Scanning
On each heartbeat, evaluate:
- Are any agents idle with empty inboxes? → Check if dispatch queue has work
- Are any tasks blocked >2 hours? → Escalate or reroute
- Are Docker services degraded? → Restart containers
- **Are you + Adjudicator both under heavy load?** → Stagger — shared ChatGPT Plus pool
- **Is Cartographer rate-limited?** → Gemini free-tier; don't retry immediately
- **Is the watchdog daemon running?** → `launchctl list | grep syncrescendence.watchdog`

## Recovery Actions (Autonomous — YOUR SPECIAL DUTY AS CTO)
As CTO, you are the system cohesion guardian. Take these actions WITHOUT waiting for Sovereign:
- Docker container down: `docker restart <container_name>`
- Auto-ingest stale task (>30 min): Move back to INBOX0 for retry
- Crashed auto-ingest loop: Restart it in tmux ingest window
- OpenClaw gateway down: `launchctl kickstart -k gui/$(id -u)/com.openclaw.gateway`
- Stale lockfile (PID gone): Remove lockfile, restart loop
- Watchdog daemon stopped: `launchctl load ~/Library/LaunchAgents/com.syncrescendence.watchdog.plist`
