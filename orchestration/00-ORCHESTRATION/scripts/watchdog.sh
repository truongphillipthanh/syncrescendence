#!/usr/bin/env bash
# watchdog.sh — Long-lived watchdog daemon
# Runs forever and executes constellation health check every 60s.

set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO_ROOT="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
CHECK_SCRIPT="${REPO_ROOT}/orchestration/scripts/constellation_watchdog.sh"
INTERVAL_SECONDS="${SYNCRESCENDENCE_WATCHDOG_INTERVAL_SECONDS:-60}"
LOG="/tmp/syncrescendence-watchdog.log"

log() {
  printf '[%s] [watchdog-daemon] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG"
}

trap 'log "shutdown signal received"; exit 0' INT TERM

log "starting long-lived watchdog loop (interval=${INTERVAL_SECONDS}s)"

while true; do
  if [ ! -x "$CHECK_SCRIPT" ]; then
    log "ERROR: check script missing/executable: $CHECK_SCRIPT"
  else
    /bin/bash "$CHECK_SCRIPT" >> "$LOG" 2>&1
    rc=$?
    if [ "$rc" -ne 0 ]; then
      log "WARN: constellation_watchdog.sh exited rc=$rc"
    fi
  fi
  sleep "$INTERVAL_SECONDS"
done
