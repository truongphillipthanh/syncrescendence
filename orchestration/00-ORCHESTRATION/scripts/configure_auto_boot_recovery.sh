#!/usr/bin/env bash
# configure_auto_boot_recovery.sh
# Comprehensive unplug-recovery hardening installer (user launchd domain).

set -euo pipefail

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
LAUNCHD_DIR="$HOME/Library/LaunchAgents"
TPL_DIR="$REPO/orchestration/scripts/launchd-mini"
UID_NUM="$(id -u)"

log() { printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*"; }

log "=== Syncrescendence unplug-recovery configuration ==="
log "Repo: $REPO"

mkdir -p "$LAUNCHD_DIR"

# Ensure wrappers are executable
chmod +x \
  "$REPO/orchestration/scripts/ensure_docker_desktop.sh" \
  "$REPO/orchestration/scripts/launch_cockpit_when_docker_ready.sh" \
  "$REPO/orchestration/scripts/auto_ingest_supervisor.sh" \
  "$REPO/orchestration/scripts/auto_ingest_all.sh" \
  "$REPO/orchestration/scripts/auto_ingest_loop.sh"

PLISTS=(
  com.syncrescendence.docker-autostart.plist
  com.syncrescendence.cockpit-autostart.plist
  com.syncrescendence.auto-ingest-supervisor.plist
  com.syncrescendence.watchdog.plist
)

log "Installing launch agents..."
for plist in "${PLISTS[@]}"; do
  src="$TPL_DIR/$plist"
  dst="$LAUNCHD_DIR/$plist"
  if [ ! -f "$src" ]; then
    log "WARN: missing template $src"
    continue
  fi
  cp -f "$src" "$dst"
  plutil -lint "$dst" >/dev/null
  log "  installed $plist"
done

# Best-effort login-item backup for Docker Desktop
osascript <<'OSA' >/dev/null 2>&1 || true
tell application "System Events"
  if not (exists login item "Docker") then
    make login item at end with properties {path:"/Applications/Docker.app", hidden:false}
  end if
end tell
OSA

log "Reloading launchd services..."
for label in \
  com.syncrescendence.docker-autostart \
  com.syncrescendence.cockpit-autostart \
  com.syncrescendence.auto-ingest-supervisor; do
  launchctl bootout "gui/$UID_NUM/$label" >/dev/null 2>&1 || true
  launchctl bootstrap "gui/$UID_NUM" "$LAUNCHD_DIR/${label}.plist"
  launchctl kickstart -k "gui/$UID_NUM/$label" || true
  log "  active $label"
done

# Remove legacy supervisor label to avoid duplicate loop managers.
launchctl bootout "gui/$UID_NUM/com.syncrescendence.auto-ingest-all" >/dev/null 2>&1 || true
rm -f "$LAUNCHD_DIR/com.syncrescendence.auto-ingest-all.plist"

log "=== Verification snapshot ==="
launchctl list | grep -E 'com\.syncrescendence\.(docker-autostart|cockpit-autostart|auto-ingest-supervisor|watchdog)' || true

log "Done."
