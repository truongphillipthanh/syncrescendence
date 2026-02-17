#!/usr/bin/env bash
# configure_auto_boot_recovery.sh
# Configures Mac mini for complete autonomous recovery after power loss
# Authority: Zero-offline hardening campaign 2026-02-16
# Run: sudo bash 00-ORCHESTRATION/scripts/configure_auto_boot_recovery.sh
#
# Recovery chain: Power restored → macOS boot → login → launchd → Docker → cockpit → agents
# Target: 0% → 100% operational in <120s (if auto-boot fires)

set -u

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
USER_HOME="$HOME"
LAUNCHD_DIR="${USER_HOME}/Library/LaunchAgents"
TMUX_CONF="${USER_HOME}/.tmux.conf"
ZSHRC="${USER_HOME}/.zshrc"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "=== Syncrescendence Auto-Boot Recovery Configuration ==="
log "User: $(whoami) | Repo: $REPO"
echo ""

# ── Phase 1: macOS Energy Saver + Scheduled Startup ──────────────────

log "[1/6] Configuring macOS auto-boot..."

# Auto-restart after power failure (UNRELIABLE on M1/M2 but set it anyway — defense in depth)
sudo systemsetup -setrestartpowerfailure on 2>/dev/null || log "WARN: setrestartpowerfailure failed (may need Full Disk Access)"
sudo systemsetup -setWaitForStartupAfterPowerFailure 30 2>/dev/null || true

# Scheduled startup: every day at 00:00 (reliable fallback if auto-boot fails)
sudo pmset repeat poweron MTWRFSU 00:00:00 2>/dev/null || log "WARN: pmset repeat failed"

# Also add: every 6 hours (reduces max delay from 24h to 6h)
# NOTE: pmset only supports ONE repeat schedule. Use cron for multi-schedule.
# The 00:00 schedule is the fallback anchor.

log "  Energy Saver: restart-after-power-failure ON"
log "  Scheduled startup: 00:00 daily (fallback)"

# ── Phase 2: Verify launchd agents ───────────────────────────────────

echo ""
log "[2/6] Verifying launchd agents..."

REQUIRED_PLISTS=(
    "com.syncrescendence.watchdog.plist"
)

for plist in "${REQUIRED_PLISTS[@]}"; do
    if [ -f "${LAUNCHD_DIR}/${plist}" ]; then
        log "  OK: ${plist}"
    else
        log "  MISSING: ${plist}"
    fi
done

# ── Phase 3: Docker Desktop auto-start ───────────────────────────────

echo ""
log "[3/6] Docker Desktop auto-start..."

# Docker Desktop auto-start is a GUI-only setting on macOS
# We create a launchd fallback that launches Docker if not running
DOCKER_PLIST="${LAUNCHD_DIR}/com.syncrescendence.docker-autostart.plist"
cat > "$DOCKER_PLIST" <<'DOCKER_EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.docker-autostart</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>docker info >/dev/null 2>&amp;1 || open -a Docker</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>StandardOutPath</key>
    <string>/tmp/syncrescendence-docker-autostart.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/syncrescendence-docker-autostart.log</string>
</dict>
</plist>
DOCKER_EOF

launchctl load "$DOCKER_PLIST" 2>/dev/null || log "  Agent already loaded"
log "  Created Docker auto-start watchdog (checks every 300s)"

# ── Phase 4: tmux-continuum activation ───────────────────────────────

echo ""
log "[4/6] Activating tmux-continuum..."

if ! grep -q "@continuum-restore 'on'" "$TMUX_CONF" 2>/dev/null; then
    cat >> "$TMUX_CONF" <<'TMUX_EOF'

# ── Syncrescendence: Auto-Restore tmux sessions (tmux-continuum) ─────
set -g @continuum-restore 'on'
set -g @continuum-save-interval '15'
TMUX_EOF
    log "  Added tmux-continuum config to ~/.tmux.conf"
else
    log "  tmux-continuum already configured"
fi

# ── Phase 5: Cockpit auto-launch launchd agent ──────────────────────

echo ""
log "[5/6] Creating cockpit auto-launch agent..."

COCKPIT_PLIST="${LAUNCHD_DIR}/com.syncrescendence.cockpit-autostart.plist"
cat > "$COCKPIT_PLIST" <<COCKPIT_EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.cockpit-autostart</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-l</string>
        <string>-c</string>
        <string>${REPO}/00-ORCHESTRATION/scripts/cockpit.sh --launch-detached</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/syncrescendence-cockpit-autostart.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/syncrescendence-cockpit-autostart.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
        <key>HOME</key>
        <string>${USER_HOME}</string>
        <key>TMUX_TMPDIR</key>
        <string>/private/tmp</string>
    </dict>
</dict>
</plist>
COCKPIT_EOF

launchctl load "$COCKPIT_PLIST" 2>/dev/null || log "  Agent already loaded"
log "  Created cockpit auto-launch agent (RunAtLoad)"

# ── Phase 6: Verification ────────────────────────────────────────────

echo ""
log "[6/6] Verification..."
echo ""
echo "=== Energy Saver ==="
sudo systemsetup -getrestartpowerfailure 2>/dev/null || echo "(check manually)"
pmset -g sched 2>/dev/null || echo "(no schedule)"
echo ""
echo "=== launchd agents ==="
launchctl list 2>/dev/null | grep syncrescendence | awk '{print "  " $3}' | sort
echo ""
echo "=== MANUAL STEPS STILL REQUIRED ==="
echo "  1. Docker Desktop → Settings → General → Enable 'Start Docker Desktop when you log in'"
echo "  2. System Settings → Users & Groups → Login Options → Auto-login (if no FileVault)"
echo "  3. cockpit.sh needs --launch-detached mode implemented"
echo ""
echo "=== RECOVERY TEST PROCEDURE ==="
echo "  1. cockpit --kill (or kill all agent CLIs)"
echo "  2. tmux kill-server"
echo "  3. Verify: tmux ls → 'no server running'"
echo "  4. Run: bash ${REPO}/00-ORCHESTRATION/scripts/cockpit.sh --launch-detached"
echo "  5. Verify: tmux ls → 'constellation' session with 8 panes"
echo "  6. Verify: cat ${REPO}/00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md"
echo ""
log "=== Configuration complete ==="
