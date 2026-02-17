# Adversarial Resilience Assessment — Power Loss Recovery (Mac mini)
**Date**: 2026-02-16
**Objective**: Achieve 100% autonomous recovery after Mac mini power loss.
**Method**: Read-only audit of recovery chain + repo scripts. No changes executed.

## A. Attack Surface Enumeration + Risk Rating + Current Defense + Proposed Fix
Risk scale: CRITICAL (blocks autonomous recovery) | HIGH (degrades within 1h) | MEDIUM (degrades within 24h) | LOW (cosmetic)

| ID | Chain Link | Failure Point | Risk | Current Defense | Proposed Fix (short) |
|---|---|---|---|---|---|
| R1 | Power restored → boot | `systemsetup -setrestartpowerfailure on` unreliable on M1/M2; setting may not be applied | CRITICAL | `configure_auto_boot_recovery.sh` sets it (lines 28-31) but no verification persistence | Add root LaunchDaemon to re-apply + verify on boot; add UPS fallback |
| R2 | Power restored → boot | `pmset repeat poweron MTWRFSU 00:00:00` only once daily; max 24h delay | CRITICAL | Script sets daily schedule (configure_auto_boot_recovery.sh:32-40) | Add boot schedule generator to create multiple one-time power-on events; reduce max delay |
| R3 | macOS login | FileVault ON blocks auto-login; manual password required | CRITICAL | None in repo (only manual note in configure_auto_boot_recovery.sh:166-169) | Disable FileVault or accept non-autonomous recovery; document as hard gate |
| R4 | macOS login | Auto-login not configured or breaks after OS update | CRITICAL | None | Add explicit checklist + verification command in recovery script |
| R5 | launchd | LaunchAgents only run after user login; if login blocked, nothing starts | CRITICAL | None | Convert critical tasks to LaunchDaemons where possible; ensure auto-login or provide hardware unlock |
| R6 | launchd | Missing launchd plists in repo for cockpit/autostart/docker/auto-ingest | HIGH | Only watchdog plist exists in repo | Commit plists to `00-ORCHESTRATION/launchd/` and install script |
| R7 | Docker Desktop | Docker auto-start GUI-only; fallback plist only created by script, not in repo | HIGH | `configure_auto_boot_recovery.sh` writes LaunchAgent to ~/Library/LaunchAgents (lines 66-93) | Commit docker-autostart plist + add readiness wait + container auto-start |
| R8 | Docker Desktop | Containers may not auto-start even if Docker starts | HIGH | None in scoped files | Add `docker compose up -d` post-ready hook and `restart: unless-stopped` |
| R9 | tmux constellation | tmux-continuum requires TPM plugin installed; config only sets options | HIGH | configure_auto_boot_recovery.sh adds `@continuum` options (lines 100-106) but does not install TPM | Add TPM install step or rely on cockpit launchd to create fresh session |
| R10 | tmux constellation | cockpit autostart LaunchAgent not committed or installed | CRITICAL | configure_auto_boot_recovery.sh writes LaunchAgent to user dir (lines 117-151), but not in repo | Commit cockpit-autostart plist + install/load script |
| R11 | 4 agent CLIs | `cockpit.sh` does not validate CLI binaries or auth; missing/expired tokens block agents | CRITICAL | None beyond tmux/nvim checks (cockpit.sh:208-217) | Add preflight CLI checks + credential health check LaunchAgent |
| R12 | 4 agent CLIs | Network not ready at boot; CLIs fail or hang | HIGH | None | Add delayed/backoff launch wrapper; retry on failure |
| R13 | Auto-ingest loops | Not auto-started; started manually in tmux | CRITICAL | None | Add per-agent LaunchAgents to run `auto_ingest_loop.sh` with KeepAlive |
| R14 | Auto-ingest loops | tmux socket mismatch post-reboot | HIGH | watchdog uses explicit socket; auto_ingest_loop uses plain tmux (auto_ingest_loop.sh:27) | Update auto_ingest_loop to use TMUX_SOCKET |
| R15 | Watchdog | LaunchAgent exists but no KeepAlive; if it exits, no monitoring | MEDIUM | com.syncrescendence.watchdog.plist RunAtLoad/StartInterval | Add KeepAlive and ThrottleInterval |
| R16 | Watchdog | Does not attempt self-heal when tmux missing | MEDIUM | Detects missing tmux and writes health file (constellation_watchdog.sh:30-44) | Add auto-restart hook to call cockpit --launch-detached |
| R17 | Credentials | API keys/OAuth/SSH may expire | CRITICAL | None | Add credential_health_check LaunchAgent + documentation for rotation |
| R18 | Disk full | /tmp or repo disk full prevents logs/results | HIGH | None | Add disk checks in watchdog + auto_ingest_loop |
| R19 | Config drift | MBA vs Mac mini configs diverge after reboot | MEDIUM | None | Add config_drift_check script + LaunchAgent |
| R20 | Remote dispatch | SSH/Tailscale down; Ajna unreachable | MEDIUM | dispatch.sh best-effort SCP only | Add retry queue + tailscale autostart check |
| R21 | Time skew | wrong clock affects timeouts and schedules | MEDIUM | None | Add NTP check at boot |
| R22 | Permissions | launchd agents fail due to PATH/HOME missing | HIGH | only watchdog plist has EnvironmentVariables | Standardize EnvironmentVariables in all plists |

## B. Proposed Fixes (Exact Changes)
Each item includes file path + line numbers for existing files, or “NEW FILE” for additions.

### B1) Auto-boot reapply + schedule fanout
**Targets**: R1, R2, R21

**NEW FILE**: `00-ORCHESTRATION/scripts/boot_reapply_power_settings.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
sudo systemsetup -setrestartpowerfailure on
sudo systemsetup -setWaitForStartupAfterPowerFailure 30 || true
# Create 4 one-time power-on events over next 24h (6h spacing)
now=$(date +%s)
for h in 6 12 18 24; do
  ts=$(date -r $((now + h*3600)) +%m/%d/%y\ %H:%M:%S)
  sudo pmset schedule poweron "$ts" || true
done
sudo systemsetup -getrestartpowerfailure || true
pmset -g sched || true
```

**NEW FILE**: `00-ORCHESTRATION/launchd/com.syncrescendence.power_reapply.plist`
```xml
<key>Label</key>
<string>com.syncrescendence.power_reapply</string>
<key>ProgramArguments</key>
<array>
  <string>/bin/bash</string>
  <string>-l</string>
  <string>-c</string>
  <string>/Users/home/Desktop/syncrescendence/00-ORCHESTRATION/scripts/boot_reapply_power_settings.sh</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>StartInterval</key>
<integer>21600</integer>
```

### B2) Auto-login hard gate documentation
**Targets**: R3, R4, R5

**File**: `00-ORCHESTRATION/scripts/configure_auto_boot_recovery.sh` (lines 166-169)
Add a hard-gate block after line 166:
```bash
echo "HARD GATE: FileVault must be OFF for autonomous recovery."
echo "Verify: fdesetup status"
echo "If FileVault is ON, autonomous recovery is impossible."
```

### B3) Commit and install cockpit autostart plist
**Targets**: R6, R10, R22

**NEW FILE**: `00-ORCHESTRATION/launchd/com.syncrescendence.cockpit-autostart.plist`
```xml
<key>Label</key>
<string>com.syncrescendence.cockpit-autostart</string>
<key>ProgramArguments</key>
<array>
  <string>/bin/bash</string>
  <string>-l</string>
  <string>-c</string>
  <string>/Users/home/Desktop/syncrescendence/00-ORCHESTRATION/scripts/cockpit.sh --launch-detached</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>KeepAlive</key>
<true/>
<key>EnvironmentVariables</key>
<dict>
  <key>PATH</key>
  <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
  <key>HOME</key>
  <string>/Users/home</string>
  <key>TMUX_TMPDIR</key>
  <string>/private/tmp</string>
</dict>
```

### B4) Dockers autostart + readiness
**Targets**: R7, R8, R22

**NEW FILE**: `00-ORCHESTRATION/launchd/com.syncrescendence.docker-autostart.plist`
```xml
<key>Label</key>
<string>com.syncrescendence.docker-autostart</string>
<key>ProgramArguments</key>
<array>
  <string>/bin/bash</string>
  <string>-l</string>
  <string>-c</string>
  <string>/Users/home/Desktop/syncrescendence/00-ORCHESTRATION/scripts/docker_autostart.sh</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>StartInterval</key>
<integer>300</integer>
```

**NEW FILE**: `00-ORCHESTRATION/scripts/docker_autostart.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
open -a Docker || true
for i in $(seq 1 60); do
  docker info >/dev/null 2>&1 && break
  sleep 2
done
# Start required stacks (edit path):
if [ -f /Users/home/Desktop/syncrescendence/docker-compose.yml ]; then
  docker compose -f /Users/home/Desktop/syncrescendence/docker-compose.yml up -d || true
fi
```

### B5) tmux-continuum install or bypass
**Targets**: R9

**File**: `00-ORCHESTRATION/scripts/configure_auto_boot_recovery.sh` (after line 95)
```bash
# Ensure TPM installed for continuum
if [ ! -d "$HOME/.tmux/plugins/tpm" ]; then
  git clone https://github.com/tmux-plugins/tpm "$HOME/.tmux/plugins/tpm" || true
fi
# Plugin install requires tmux session; rely on cockpit autostart for recovery
```

### B6) CLI preflight + credential health
**Targets**: R11, R17

**File**: `00-ORCHESTRATION/scripts/cockpit.sh` (after line 208)
```bash
for bin in claude codex gemini openclaw; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    echo "Error: $bin not found in PATH"
    exit 1
  fi
done
```

**NEW FILE**: `00-ORCHESTRATION/scripts/credential_health_check.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
command -v claude >/dev/null 2>&1 || echo "WARN: claude missing"
command -v codex >/dev/null 2>&1 || echo "WARN: codex missing"
command -v gemini >/dev/null 2>&1 || echo "WARN: gemini missing"
command -v openclaw >/dev/null 2>&1 || echo "WARN: openclaw missing"
ssh -o BatchMode=yes -o ConnectTimeout=3 ajna "exit" 2>/dev/null || echo "WARN: SSH ajna failed"
```

### B7) Auto-ingest LaunchAgents + tmux socket
**Targets**: R13, R14

**File**: `00-ORCHESTRATION/scripts/auto_ingest_loop.sh` (line 27)
```bash
TMUX_SOCKET="/private/tmp/tmux-$(id -u)/default"
TMUX_BIN="/opt/homebrew/bin/tmux -S ${TMUX_SOCKET}"
```

**NEW FILES** (one per agent):
- `00-ORCHESTRATION/launchd/com.syncrescendence.auto_ingest.commander.plist`
- `00-ORCHESTRATION/launchd/com.syncrescendence.auto_ingest.adjudicator.plist`
- `00-ORCHESTRATION/launchd/com.syncrescendence.auto_ingest.cartographer.plist`
- `00-ORCHESTRATION/launchd/com.syncrescendence.auto_ingest.psyche.plist`
Each should run:
```xml
<key>ProgramArguments</key>
<array>
  <string>/bin/bash</string>
  <string>-l</string>
  <string>-c</string>
  <string>/Users/home/Desktop/syncrescendence/00-ORCHESTRATION/scripts/auto_ingest_loop.sh <agent> /Users/home/Desktop/syncrescendence constellation <pane></string>
</array>
<key>RunAtLoad</key><true/>
<key>KeepAlive</key><true/>
```

### B8) Watchdog KeepAlive + self-heal
**Targets**: R15, R16, R18

**File**: `00-ORCHESTRATION/launchd/com.syncrescendence.watchdog.plist` (after line 19)
```xml
<key>KeepAlive</key>
<dict>
  <key>SuccessfulExit</key><false/>
</dict>
<key>ThrottleInterval</key><integer>30</integer>
```

**File**: `00-ORCHESTRATION/scripts/constellation_watchdog.sh` (after line 37)
```bash
if [ -x "${REPO_DIR}/00-ORCHESTRATION/scripts/cockpit.sh" ]; then
  log "Attempting cockpit auto-restart (detached)"
  "${REPO_DIR}/00-ORCHESTRATION/scripts/cockpit.sh" --launch-detached >/dev/null 2>&1 || true
fi
```

### B9) Disk + CPU pressure checks
**Targets**: R18, R21

**File**: `00-ORCHESTRATION/scripts/constellation_watchdog.sh` (after line 107)
```bash
disk_pct=$(df -Pk "$REPO_DIR" | awk "NR==2{gsub(/%/, "", $5); print $5}")
echo "Disk usage: ${disk_pct}%"
```

### B10) Config drift check
**Targets**: R19

**NEW FILE**: `00-ORCHESTRATION/scripts/config_drift_check.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
REPO="$HOME/Desktop/syncrescendence"
cd "$REPO"
git fetch --quiet || true
LOCAL=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
REMOTE=$(git rev-parse --short origin/main 2>/dev/null || echo "unknown")
if [ "$LOCAL" != "$REMOTE" ]; then
  echo "CONFIG DRIFT: local $LOCAL vs origin/main $REMOTE"
  exit 2
fi
exit 0
```

### B11) Network readiness
**Targets**: R12, R20

**NEW FILE**: `00-ORCHESTRATION/scripts/network_ready.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
for i in $(seq 1 60); do
  ping -c 1 1.1.1.1 >/dev/null 2>&1 && exit 0
  sleep 2
done
exit 1
```
Use this as a wrapper before launching CLIs in cockpit-autostart and docker-autostart scripts.

## C. Dependency Graph (Fix Order)
1. **Autologin gate** (FileVault off / auto-login on) — without this, no LaunchAgents run. (R3, R4, R5)
2. **Power restore reliability** — ensure system auto-boot and scheduled wake. (R1, R2)
3. **Launchd foundations** — commit + install cockpit-autostart, docker-autostart, watchdog KeepAlive. (R6, R7, R10, R15)
4. **tmux + cockpit** — ensure tmux-continuum or rely on cockpit autostart to create fresh session. (R9)
5. **CLI preflight + credentials** — prevent silent startup failures. (R11, R17)
6. **Auto-ingest loops** — LaunchAgents for each agent after cockpit is up. (R13, R14)
7. **Docker readiness + containers** — only after Docker desktop is running. (R7, R8)
8. **Network readiness + remote dispatch** — enable cross-machine recovery. (R12, R20)
9. **Config drift + disk/CPU checks** — keep system from degrading post-boot. (R18, R19, R21)

## D. Criticality Summary
- **Hard blockers for autonomous recovery**: FileVault/auto-login, auto-boot reliability, cockpit autostart, CLI credential availability, auto-ingest autostart.
- **Most fragile chain links**: Power restore, login gate, cockpit autostart, CLI auth.

