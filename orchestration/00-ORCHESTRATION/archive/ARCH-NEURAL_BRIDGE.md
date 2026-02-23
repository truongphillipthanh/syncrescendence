# Neural Bridge Architecture (MBA ↔ Mac mini)

**Version**: 1.0.0
**Owner**: Psyche (CTO)
**Exegete**: Cartographer (CIO)
**Status**: OPERATIONAL (launchd env pending validation)

## 1. Overview

The **Neural Bridge** is the bidirectional SSH link connecting the MacBook Air (MBA) and the M1 Mac mini. It serves as the constellation's **circulatory system**, enabling:
- **Cross-machine task dispatch** (SCP slinging of TASK files).
- **Confirmation routing** (SCP slinging of CONFIRM/RESULT files).
- **Health monitoring** (Remote status checks).
- **Remote execution** (Agent-to-agent commands).

Loss of this link is considered a **VITAL ORGAN FAILURE** as it isolates the strategic direction (Ajna) from the operational execution (Commander/Psyche).

## 2. Bidirectional SSH Topology

```text
┌───────────────────────────┐           SSH (ed25519)           ┌───────────────────────────┐
│       MacBook Air         │◄───────────────────────────────►│        Mac mini           │
│       (CSO / Ajna)        │                                 │       (COO / Psyche)      │
├───────────────────────────┤                                 ├───────────────────────────┤
│ Alias: "mini"             │        MBA → Mac mini           │ Alias: "macbook-air"      │
│ Key: id_ed25519_ajna      │────────────────────────────────►│ Target: home@m1mini.local │
│                           │                                 │                           │
│ Alias: "psyche"           │        Mac mini → MBA           │ Key: id_..._to_psyche     │
│ Target: system@mba.local  │◄────────────────────────────────│                           │
└───────────────────────────┘                                 └───────────────────────────┘
```

## 3. Component Inventory

| Component | MBA Location | Mac mini Location | Purpose |
|-----------|-------------|-------------------|---------|
| SSH key (MBA→MM) | `~/.ssh/id_ed25519_ajna` | `~/.ssh/authorized_keys` | Authentication |
| SSH key (MM→MBA) | `~/.ssh/authorized_keys` | `~/.ssh/id_ed25519_ajna_to_psyche` | Authentication |
| SSH config | `~/.ssh/config` (alias: `mini`) | `~/.ssh/config` (alias: `macbook-air`, `psyche`) | Connection params |
| Env vars | `~/.zshrc` | `~/.zshrc` | Dispatch routing |
| `dispatch.sh` | `orchestration/scripts/` | `orchestration/scripts/` | TASK SCP sling |
| `auto_ingest_loop.sh`| N/A | `orchestration/scripts/` | CONFIRM SCP back |
| `watchdog.sh` | N/A | `orchestration/scripts/` | SSH health monitoring |

## 4. Data Flows

### A. TASK Dispatch
1. **Initiation**: Agent A (e.g., Ajna on MBA) runs `dispatch.sh cartographer`.
2. **Slinging**: `dispatch.sh` detects `SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER=mini`.
3. **Transport**: `scp TASK-*.md mini:~/Desktop/syncrescendence/-INBOX/cartographer/00-INBOX0/`.
4. **Execution**: Mac mini `auto_ingest_loop.sh` detects file, claims it, and executes.

### B. CONFIRM Routing
1. **Completion**: Mac mini agent (e.g., Cartographer) finishes task.
2. **Detection**: `auto_ingest_loop.sh` sees RESULT file, writes local CONFIRM.
3. **Routing**: If `Reply-To` agent is on MBA, `auto_ingest_loop.sh` runs `scp CONFIRM-* macbook-air:...`.

### C. Health Check
1. **Probe**: `constellation_watchdog.sh` runs `ssh -o ConnectTimeout=5 macbook-air hostname`.
2. **State**: Writes `HEALTHY` or `DOWN` to `DYN-CONSTELLATION_HEALTH.md`.

## 5. Failure Modes and Recovery

| Failure | Detection | Impact | Recovery |
|---------|-----------|--------|----------|
| SSH Timeout | Watchdog report | No cross-machine ops | Check mDNS; restart `sshd`. |
| Auth Failure | `Permission denied` | No cross-machine ops | Verify keys + `authorized_keys` permissions (600). |
| DNS/mDNS Failure | `Could not resolve` | SSH can't connect | Use IP fallback in SSH config. |
| Key Missing | `File not found` | Auth failure | Restore key from backup or regenerate. |
| Network Isolation | `No route to host` | Full isolation | Check Wi-Fi/Ethernet; use Git fallback. |

## 6. Maintenance Procedures

### Troubleshooting Checklist
1. **Can I resolve the hostname?** `ping M1-Mac-mini.local` (IP should show).
2. **Can I connect manually?** `ssh mini` or `ssh macbook-air`.
3. **Are the keys loaded?** `ssh-add -l`.
4. **Are permissions correct?** `ls -l ~/.ssh` (should be `600` for keys, `644` for config/pub).

### Fallback Transport: Git Sync
If the Neural Bridge is permanently severed and mDNS/IP fail:
1. Commit all tasks locally: `git add -A && git commit -m "sync: local tasks"`.
2. Push to remote: `git push`.
3. Target machine: `git pull`.
*Note: This is asynchronous and depends on GitHub/GitLab availability.*

---
*Documented by Cartographer (CIO) — 2026-02-16*
