#!/usr/bin/env bash
# launch_cockpit_when_docker_ready.sh
# Launches constellation cockpit only after Docker daemon is confirmed ready.

set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
LOG="/tmp/syncrescendence-cockpit-autostart.log"
DOCKER_HELPER="${REPO}/00-ORCHESTRATION/scripts/ensure_docker_desktop.sh"
COCKPIT_SCRIPT="${REPO}/00-ORCHESTRATION/scripts/cockpit.sh"
MAX_WAIT_SECONDS="${SYNCRESCENDENCE_DOCKER_WAIT_SECONDS:-120}"
SLEEP_SECONDS=2

log() {
  printf '[%s] [cockpit-autostart] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG"
}

cd "$REPO" 2>/dev/null || true

# First, proactively ensure Docker Desktop is started.
if [ -x "$DOCKER_HELPER" ]; then
  "$DOCKER_HELPER" >> "$LOG" 2>&1 || true
fi

attempts=$((MAX_WAIT_SECONDS / SLEEP_SECONDS))
if [ "$attempts" -lt 1 ]; then attempts=1; fi

for _ in $(seq 1 "$attempts"); do
  if docker info >/dev/null 2>&1; then
    log "Docker ready; launching cockpit detached"
    bash "$COCKPIT_SCRIPT" --launch-detached >> "$LOG" 2>&1
    rc=$?
    log "cockpit exit rc=${rc}"
    exit "$rc"
  fi
  sleep "$SLEEP_SECONDS"
done

log "ERROR: Docker not ready after ${MAX_WAIT_SECONDS}s; skipping cockpit launch this cycle"
exit 1
