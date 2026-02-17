#!/usr/bin/env bash
# ensure_docker_desktop.sh
# Idempotent Docker Desktop starter + readiness gate for launchd.

set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
LOG="/tmp/syncrescendence-docker-autostart.log"
MAX_WAIT_SECONDS="${SYNCRESCENDENCE_DOCKER_WAIT_SECONDS:-120}"
SLEEP_SECONDS=2

log() {
  printf '[%s] [docker-autostart] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG"
}

cd "$REPO" 2>/dev/null || true

if docker info >/dev/null 2>&1; then
  log "Docker daemon already ready"
  exit 0
fi

if ! pgrep -f "Docker Desktop" >/dev/null 2>&1; then
  log "Docker Desktop not running; launching via open -a Docker"
  open -a Docker >/dev/null 2>&1 || log "WARN: open -a Docker failed"
else
  log "Docker Desktop process exists but daemon not ready yet"
fi

attempts=$((MAX_WAIT_SECONDS / SLEEP_SECONDS))
if [ "$attempts" -lt 1 ]; then attempts=1; fi

for _ in $(seq 1 "$attempts"); do
  if docker info >/dev/null 2>&1; then
    log "Docker daemon became ready"
    exit 0
  fi
  sleep "$SLEEP_SECONDS"
done

log "ERROR: Docker daemon not ready after ${MAX_WAIT_SECONDS}s"
exit 1
