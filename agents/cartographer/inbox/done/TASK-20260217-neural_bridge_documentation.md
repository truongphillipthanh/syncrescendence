# TASK-20260217-neural_bridge_documentation

**Priority**: P1
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: cartographer
**Reply-To**: commander
**CC**: commander
**Status**: COMPLETE
**Claimed-By**: cartographer-mini
**Claimed-At**: 2026-02-16T07:30:00Z
**Completed-At**: 2026-02-16T08:20:00Z
**Created**: 2026-02-17T04:25:00Z

---

## Objective

Comprehensively document the Neural Bridge architecture. This is the most critical infrastructure component — the MBA↔Mac mini SSH link that serves as the constellation's circulatory system. Documentation must be exhaustive enough that any agent can diagnose and recover connectivity issues autonomously.

## Deliverable 1: Update ARCH-UNPLUG_RECOVERY_ARCHITECTURE.md

Add a comprehensive Neural Bridge section to the existing recovery architecture document at:
`orchestration/state/ARCH-UNPLUG_RECOVERY_ARCHITECTURE.md`

Include:
1. ASCII diagram of the full bidirectional SSH topology
2. Key file inventory (both machines): SSH keys, configs, authorized_keys, env vars, scripts
3. Data flow diagram: TASK dispatch → SCP sling → auto-ingest → CONFIRM → SCP back
4. Failure mode table: what breaks, how to detect, how to recover
5. Dependency chain: what depends on SSH working (dispatch, CONFIRM routing, watchdog, health checks)

## Deliverable 2: Create ARCH-NEURAL_BRIDGE.md

Create a dedicated architecture document at:
`orchestration/state/ARCH-NEURAL_BRIDGE.md`

Comprehensive contents:

### 1. Overview
- What is the Neural Bridge (SSH bidirectional link)
- Why it's a vital organ (all cross-machine operations depend on it)
- Design principles: key-based auth, config aliases, env var routing, SCP transport

### 2. Component Inventory

| Component | MBA Location | Mac mini Location | Purpose |
|-----------|-------------|-------------------|---------|
| SSH key (MBA→MM) | ~/.ssh/id_ed25519_ajna | ~/.ssh/authorized_keys | Authentication |
| SSH key (MM→MBA) | ~/.ssh/authorized_keys | ~/.ssh/id_ed25519_ajna_to_psyche | Authentication |
| SSH config | ~/.ssh/config (alias: mini) | ~/.ssh/config (alias: macbook-air) | Connection params |
| Env vars | ~/.zshrc | ~/.zshrc | Dispatch routing |
| dispatch.sh | orchestration/scripts/ | orchestration/scripts/ | TASK SCP sling |
| auto_ingest_loop.sh | N/A (MBA doesn't run ingest) | orchestration/scripts/ | CONFIRM SCP back |
| constellation_watchdog.sh | N/A | orchestration/scripts/ | SSH health monitoring |

### 3. Data Flows
- TASK dispatch: MBA Commander → dispatch.sh → SCP to MM INBOX → auto-ingest picks up
- CONFIRM routing: MM agent completes → CONFIRM written → SCP to MBA INBOX
- Health check: watchdog SSH probe every 60s → writes to HEALTH.md
- Fallback: If SSH down → git push/pull as transport (slower but functional)

### 4. Failure Modes and Recovery

| Failure | Detection | Impact | Recovery |
|---------|-----------|--------|----------|
| SSH key corrupted/deleted | watchdog SSH check fails | No cross-machine dispatch | Regenerate key, re-authorize |
| Mac mini offline | SSH timeout | MBA isolated, local-only ops | Auto-boot → auto-login → SSH resumes |
| MBA offline | Mac mini watchdog detects | No CONFIRM delivery to MBA | Queue locally, SCP when restored |
| Network partition | Both sides timeout | Full isolation | Git as fallback transport |
| DNS/Bonjour failure | Hostname resolution fails | SSH can't connect | Use IP fallback in SSH config |
| authorized_keys permissions wrong | SSH rejects key | Auth failure | chmod 600 ~/.ssh/authorized_keys |

### 5. Health Monitoring
- Watchdog: `ssh -o ConnectTimeout=5 <alias> hostname` every 60s
- NEVER use ICMP ping (blocked by Stealth Mode firewall)
- Alert thresholds: 3 consecutive failures = critical
- Recovery action: log failure, attempt reconnection, alert Sovereign if persistent

### 6. Maintenance Procedures
- Key rotation procedure
- Adding new machines to the bridge
- Troubleshooting SSH "Too many authentication failures" (use IdentitiesOnly=yes)
- Verifying env vars match SSH config aliases

### 7. Verification Checklist
Run from MBA:
```bash
ssh mini hostname                              # Should return M1-Mac-mini.local
ssh mini "cat ~/Desktop/syncrescendence/CLAUDE.md | head -1"  # Should return "# Syncrescendence..."
```
Run from Mac mini:
```bash
ssh macbook-air hostname                       # Should return Lisa's MacBook Air hostname
ssh macbook-air "ls ~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/" # Should list files
```

## Write Result
Write to: `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260217-neural-bridge-documentation.md`
Write CONFIRM to: `-INBOX/commander/00-INBOX0/CONFIRM-cartographer-20260217-neural-bridge-documentation.md`

Git commit: `git add -A && git commit -m "docs(bridge): comprehensive Neural Bridge architecture — Cartographer CIO" && git push`
