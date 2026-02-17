#!/bin/bash
# auto_ingest_all.sh — Persistent supervisor for all auto-ingest loops
# Runs as a long-lived launchd process (KeepAlive). Manages 4 agent loops as
# child processes. If a loop dies, the supervisor respawns it.
# Authority: Zero-offline hardening 2026-02-16
# NOTE: Must be compatible with /bin/bash 3.2 (macOS default). No declare -A.

REPO="/Users/home/Desktop/syncrescendence"
SCRIPT="${REPO}/00-ORCHESTRATION/scripts/auto_ingest_loop.sh"
SESSION="constellation"
LOG="/tmp/syncrescendence-auto-ingest-all.log"

# PID tracking (bash 3.2 compatible — parallel arrays)
AGENTS="commander adjudicator psyche cartographer"
PID_commander=0
PID_adjudicator=0
PID_psyche=0
PID_cartographer=0

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [supervisor] $*" >> "$LOG"; }

get_pane() {
    case "$1" in
        psyche)       echo "1.1" ;;
        commander)    echo "1.3" ;;
        adjudicator)  echo "1.5" ;;
        cartographer) echo "1.7" ;;
        *)            echo "" ;;
    esac
}

get_pid() {
    eval echo "\$PID_$1"
}

set_pid() {
    eval "PID_$1=$2"
}

is_alive() {
    local pid
    pid=$(get_pid "$1")
    [ "$pid" -gt 0 ] 2>/dev/null && kill -0 "$pid" 2>/dev/null
}

cleanup() {
    log "Supervisor shutting down — killing all loops"
    for agent in $AGENTS; do
        local pid
        pid=$(get_pid "$agent")
        if [ "$pid" -gt 0 ] 2>/dev/null; then
            kill "$pid" 2>/dev/null
        fi
    done
    exit 0
}

trap cleanup INT TERM

spawn_loop() {
    local agent="$1"
    local pane
    pane="$(get_pane "$agent")"

    # For tmux-based agents, need constellation session
    if [ "$agent" != "cartographer" ]; then
        if ! /opt/homebrew/bin/tmux has-session -t "$SESSION" 2>/dev/null; then
            return 1
        fi
    fi

    # Clear stale lockfile if needed
    local lockfile="${REPO}/-INBOX/${agent}/.auto_ingest.lock"
    if [ -f "$lockfile" ]; then
        local existing_pid
        existing_pid=$(/bin/cat "$lockfile" 2>/dev/null)
        if [ -n "$existing_pid" ] && kill -0 "$existing_pid" 2>/dev/null; then
            # Loop already running from another instance
            set_pid "$agent" "$existing_pid"
            return 0
        fi
        rm -f "$lockfile"
    fi

    /bin/bash "$SCRIPT" "$agent" "$REPO" "$SESSION" "$pane" >> "/tmp/syncrescendence-auto-ingest-${agent}.log" 2>&1 &
    set_pid "$agent" $!
    log "Spawned $agent loop (PID $!, pane $pane)"
}

log "=== Supervisor starting ==="

# Main supervisor loop
while true; do
    for agent in $AGENTS; do
        if ! is_alive "$agent"; then
            spawn_loop "$agent" || true
        fi
    done
    # Sleep and check every 15s
    sleep 15
done
