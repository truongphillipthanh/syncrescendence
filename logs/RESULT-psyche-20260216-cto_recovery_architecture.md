# RESULT — CTO Recovery Architecture (Read-Only Assessment)

**Task**: TASK-20260216-cto_recovery_architecture  
**Mode**: READ-ONLY ANALYTICAL (no code/config changes applied)  
**Host**: Mac mini (`M1-Mac-mini.local`)  
**Timestamp**: 2026-02-16 16:xx PST

---

## Executive Verdict

Current recovery posture is **NOT 100% autonomous after physical unplug**.

### Hard blockers
1. **FileVault is ON** (`fdesetup status` => `FileVault is On.`) → autonomous post-power-loss login is blocked.
2. **Docker daemon currently down** (cannot connect to `/Users/home/.docker/run/docker.sock`).
3. **Auto-start launch agents for Docker and cockpit are not installed** in `~/Library/LaunchAgents`.
4. **Auto-ingest loops are not launchd-managed** (currently manual tmux processes; only 3 running: psyche/adjudicator/cartographer).

### Good news
- `cockpit.sh --launch-detached` is **already implemented** and matches pane requirements.
- Constellation tmux topology exists and `cockpit` window has 8 panes.
- tmux-continuum settings/plugins are present.

---

## 1) Docker Auto-Recovery Assessment

## 1.1 Docker Desktop "Start on login"
- **Status**: **UNVERIFIED** (non-interactive/GUI setting; no reliable headless read succeeded in this run).
- **Observed runtime**:
  - `docker version` client works, daemon unreachable.
  - Error: `Cannot connect to the Docker daemon at unix:///Users/home/.docker/run/docker.sock. Is the docker daemon running?`
  - `pgrep -fl Docker` shows only helper `com.docker.vmnetd`, not full Docker Desktop app process.

**CTO judgment**: treat as **NOT guaranteed enabled** until explicitly confirmed in GUI.

## 1.2 Restart policies (Neo4j / Graphiti / Qdrant / Chroma)
- **Status**: **BLOCKED by daemon down** (cannot run `docker inspect` now).
- **Required command set (once daemon is up):**
  - `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' neo4j`
  - `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' graphiti`
  - `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' qdrant`
  - `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' chroma`
- If not `unless-stopped`:
  - `docker update --restart unless-stopped neo4j graphiti qdrant chroma`

## 1.3 Verify comeback after daemon restart
When Docker daemon is restored:
1. `docker ps -a --format '{{.Names}}|{{.Status}}'`
2. restart Docker Desktop daemon/app
3. wait until `docker info` succeeds
4. re-run `docker ps -a` and service-level health checks

**Note**: Prior docs indicate `chroma` may be launchd-managed Python service (`com.syncrescendence.chroma-server`) rather than Docker container in this stack. Validate actual runtime topology before forcing Docker policy for Chroma.

---

## 2) cockpit.sh --launch-detached Implementation Check

**Result**: **ALREADY IMPLEMENTED** (no new implementation required).

Evidence from `orchestration/scripts/cockpit.sh`:
- Usage advertises detached mode (`--launch-detached`) and no-attach semantics.
- Flag handler sets:
  - `CMD_PSYCHE`: `openclaw tui --session main --thinking high`
  - `CMD_COMMANDER`: `claude --dangerously-skip-permissions`
  - `CMD_ADJUDICATOR`: `codex ...`
  - `CMD_CARTOGRAPHER`: `gemini -m ... --yolo`
  - `ATTACH_ON_READY=false`
- Session creation logic builds 8-pane cockpit layout and sends commands to top panes.
- Footer respects detached mode:
  - if attached => `exec tmux attach -t "$SESSION"`
  - else => prints ready and exits.

### Pane mapping check vs requirement
- OpenClaw in **1.1** ✅
- Claude Code in **1.3** ✅
- Codex in **1.5** ✅
- Gemini in **1.7** ✅

### Drift note
`configure_auto_boot_recovery.sh` still prints manual step "cockpit.sh needs --launch-detached mode implemented" (stale text; now false). Update recommended for operator clarity.

---

## 3) Auto-Ingest Loop Auto-Start Architecture

Current state:
- Auto-ingest loops are manual tmux-started processes.
- Running now (from `ps`): **adjudicator, psyche, cartographer**.
- Missing from this machine loop set: **commander** (and ajna is remote lane).

## Recommended architecture (launchd-first)
Use **one LaunchAgent per local agent** with `RunAtLoad + KeepAlive`:
- `com.syncrescendence.auto-ingest.psyche`
- `com.syncrescendence.auto-ingest.commander`
- `com.syncrescendence.auto-ingest.adjudicator`
- `com.syncrescendence.auto-ingest.cartographer`

ProgramArguments per agent:
`/bin/bash -l -c '/Users/home/Desktop/syncrescendence/orchestration/scripts/auto_ingest_loop.sh <agent> /Users/home/Desktop/syncrescendence constellation <pane>'`

Pane map:
- psyche → `1.1`
- commander → `1.3`
- adjudicator → `1.5`
- cartographer → `1.7`

### Ordering dependency control
Because launchd has no strict dependency graph for user agents, add a tiny wrapper that waits until:
- `tmux has-session -t constellation`
- `tmux list-panes -t constellation:cockpit` contains expected pane

Then exec `auto_ingest_loop.sh`.

### Additional hardening
`auto_ingest_loop.sh` currently uses plain tmux binary without explicit socket binding. For post-reboot determinism, align it with watchdog pattern (`-S /private/tmp/tmux-$(id -u)/default`).

---

## 4) FileVault Assessment + Smart Plug / WoL

`fdesetup status` => **FileVault is On**.

### CTO trade-off
- **Security**: FileVault ON protects disk at rest.
- **Autonomy**: Full autonomous boot-to-operations after hard power loss is **not possible** with FileVault ON, because pre-boot unlock requires credentials.

### Smart plug + Wake-on-LAN viability
- **Smart plug**: can restore/cycle power, but cannot satisfy FileVault pre-boot unlock.
- **Wake-on-LAN**: useful from sleep states; does not solve FileVault unlock after cold boot from unplug event.

**Conclusion**: smart plug/WoL are **insufficient** for true 100% autonomous post-unplug recovery when FileVault remains ON.

### Viable paths
1. **Autonomy-first**: Disable FileVault + enable auto-login (operationally autonomous, lower at-rest security).
2. **Security-first**: Keep FileVault ON + accept manual unlock step after outage.
3. **Mitigated compromise**: Keep FileVault ON + UPS to avoid hard power-loss/cold-boot path (reduces outage frequency, does not eliminate unlock requirement for true cold boot).

---

## 5) End-to-End Recovery Test Plan (Power-Loss Simulation)

## Phase A — Pre-check
1. Confirm critical agents loaded:
   - `launchctl list | rg 'com\.syncrescendence\.(watch|watchdog|docker-autostart|cockpit-autostart|auto-ingest)'`
2. Confirm cockpit detached bootstrap works:
   - `bash orchestration/scripts/cockpit.sh --launch-detached`
3. Confirm baseline services:
   - `tmux list-windows -t constellation`
   - `docker info`
   - `docker ps -a --format '{{.Names}}|{{.Status}}'`

## Phase B — Simulate outage
1. Physically unplug Mac mini power.
2. Wait >=30s.
3. Reconnect power.

## Phase C — Boot/login gate
1. Observe whether system reaches logged-in desktop autonomously.
2. If FileVault prompt appears, mark **autonomous recovery FAIL (expected with FileVault ON)**.

## Phase D — Post-login auto-heal checks
1. Launchd:
   - `launchctl list | rg 'com\.syncrescendence'`
2. Docker:
   - `docker info`
   - `docker ps -a --format '{{.Names}}|{{.Status}}'`
3. Cockpit/tmux:
   - `tmux ls`
   - `tmux list-panes -t constellation:cockpit -F 'pane=#{pane_index} title=#{pane_title} cmd=#{pane_current_command}'`
4. Ingest loops:
   - `ps aux | rg 'auto_ingest_loop\.sh'`
5. Health artifacts:
   - `cat orchestration/state/DYN-CONSTELLATION_HEALTH.md`

## Success criteria
- Logged-in session available without human intervention (currently blocked by FileVault).
- Docker daemon up and required containers/services healthy.
- `constellation` session present with expected panes.
- All 4 local auto-ingest loops running.
- Watchdog reporting healthy/non-critical state.

---

## Prioritized Remediation Sequence

1. **Decision gate**: FileVault security posture vs full autonomy requirement.
2. Install/load missing LaunchAgents: docker-autostart + cockpit-autostart.
3. Add launchd-managed auto-ingest loops for all local lanes.
4. Bring Docker daemon up; enforce container restart policies (`unless-stopped`).
5. Run physical unplug recovery drill and capture evidence.

---

## Read-Only Receipt
- No source code was modified.
- No plists were created/loaded by this assessment.
- No commits were made.
