#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# ensure_docker_desktop.sh — Readiness gate only.
# Docker launch is handled by macOS Login Items.

set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

LOG="/tmp/syncrescendence-docker-autostart.log"
MAX_WAIT_SECONDS="${SYNCRESCENDENCE_DOCKER_WAIT_SECONDS:-180}"

log() {
  printf '[%s] [docker-gate] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG"
}

if docker info >/dev/null 2>&1; then
  log "Docker already ready"
  exit 0
fi

log "Waiting up to ${MAX_WAIT_SECONDS}s for Docker daemon..."
elapsed=0
while [ "$elapsed" -lt "$MAX_WAIT_SECONDS" ]; do
  if docker info >/dev/null 2>&1; then
    log "Docker became ready after ${elapsed}s"
    exit 0
  fi
  sleep 3
  elapsed=$((elapsed + 3))
done

log "ERROR: Docker not ready after ${MAX_WAIT_SECONDS}s"
exit 1
