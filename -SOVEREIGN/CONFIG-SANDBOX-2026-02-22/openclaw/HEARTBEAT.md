# Heartbeat Configuration — Ajna (CSO)

## Interval
Every 30 minutes during working hours (9am-11pm)

## Infrastructure Health Checks (MANDATORY)

### Tier 1: Constellation Health (every heartbeat)
1. Read `orchestration/state/DYN-CONSTELLATION_HEALTH.md` — check all agent states
2. Check `-INBOX/ajna/00-INBOX0/` for TASK-*, CONFIRM-*, RESULT-* files
3. Check git log for commits by other agents since last heartbeat
4. Review ARCH-INTENTION_COMPASS.md for Sovereign intent signals

### Tier 2: Auto-Ingest Health (every 2nd heartbeat)
5. Verify auto-ingest loops are running: check for `.auto_ingest.lock` files in each agent's INBOX
6. Check for stale tasks in `10-IN_PROGRESS/` (>30 min = investigate)
7. Check for FAILED tasks in `50_FAILED/` — these may need retry or escalation
8. Review `auto_ingest.log` tails for ERROR or TIMEOUT entries

### Tier 3: Service Health (every 3rd heartbeat)
9. Check Docker health (Neo4j :7474, Graphiti :8001, Qdrant :6333) — on Mac mini
10. Check OpenClaw gateway health (localhost:18789)
11. Verify watchdog launchd agent: `launchctl list | grep syncrescendence`

### Tier 4: Cross-Machine Neural Bridge (every 6th heartbeat)
12. Test SSH to Mac mini: `ssh -o ConnectTimeout=5 mini hostname` — must return `M1-Mac-mini.local`
13. Test SCP readiness: `ssh mini "ls ~/Desktop/syncrescendence/-INBOX/ajna/00-INBOX0/" 2>/dev/null`
14. Verify SYNCRESCENDENCE_REMOTE_AGENT_HOST env vars are set in `~/.zshrc`
15. If SSH fails: alert Sovereign immediately — this is a vital organ failure

## Notification Criteria
Only notify Sovereign if:
- P0 task dispatched to you by Sovereign or Commander
- Agent conflict detected (merge collision, inbox deadlock)
- Infrastructure failure (Docker down, gateway unreachable, auto-ingest crashed)
- Strategic misalignment detected (execution diverging from Intention Compass)
- Budget depletion on any agent's model tier
- **Any agent showing ERROR or STALE in watchdog health for >5 minutes**
- **Auto-ingest loop crashed (missing lockfile + no running process)**

## Do NOT notify for:
- Routine task completions (write to execution log instead)
- Newsletter/marketing content
- Non-urgent status updates
- Things that can wait until next Sovereign session
- IDLE agents with empty inboxes (this is normal)

## Proactive Scanning
On each heartbeat, evaluate:
- Are any agents idle with empty inboxes? → Dispatch proactive work
- Are any tasks blocked >2 hours? → Escalate or reroute
- Has the Intention Compass been updated? → Realign priorities
- Are any model budgets approaching depletion? → Queue rebalancing
- **Are Psyche + Adjudicator both under heavy load?** → They share ChatGPT Plus; stagger dispatch
- **Is Cartographer rate-limited?** → Gemini free-tier; wait for reset, don't retry immediately

## Recovery Actions (Autonomous)
If heartbeat detects failure, take these actions WITHOUT waiting for Sovereign:
- Auto-ingest stale task (>30 min): Move back to INBOX0 for retry
- Crashed auto-ingest loop: Log the failure, dispatch alert to Commander
- FAILED task with no CONFIRM sent: Generate CONFIRM with FAILED status
- Stale lockfile (PID gone): Remove lockfile, note in log
