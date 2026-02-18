#!/bin/bash
# auto_ingest_supervisor.sh — Persistent supervisor for all auto-ingest loops
# Launchd target label: com.syncrescendence.auto-ingest-supervisor

# bash 3.2 compatible (macOS default)
set -u

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# Neural Bridge: load cross-machine dispatch env vars
# launchd does NOT source ~/.zshrc — parse only SYNCRESCENDENCE_REMOTE_AGENT_HOST_* safely.
load_bridge_env_from_zshrc() {
    [ -f "${HOME}/.zshrc" ] || return 0
    while IFS= read -r line; do
        case "$line" in
            export\ SYNCRESCENDENCE_REMOTE_AGENT_HOST_*=*)
                key=$(printf '%s' "$line" | sed -E 's/^export[[:space:]]+([^=]+)=.*/\1/')
                val=$(printf '%s' "$line" | sed -E 's/^export[[:space:]]+[^=]+=//; s/^"//; s/"$//')
                case "$key" in
                    SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA)
                        [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA="$val"
                        ;;
                    SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER)
                        [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER="$val"
                        ;;
                    SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR)
                        [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR="$val"
                        ;;
                    SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER)
                        [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER="$val"
                        ;;
                    SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE)
                        [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE="$val"
                        ;;
                esac
                ;;
        esac
    done < "${HOME}/.zshrc"
}

load_bridge_env_from_zshrc
: "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA:=macbook-air}"
: "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER:=local}"
: "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR:=local}"
: "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER:=local}"
: "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE:=local}"

export SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
SCRIPT="${REPO}/00-ORCHESTRATION/scripts/auto_ingest_loop.sh"
INTEGRITY_GATE_SCRIPT="${REPO}/00-ORCHESTRATION/scripts/repo_integrity_gate.sh"
SESSION="${SYNCRESCENDENCE_TMUX_SESSION:-constellation}"
LOG="/tmp/syncrescendence-auto-ingest-supervisor.log"
INTEGRITY_CHECK_INTERVAL="${SYNCRESCENDENCE_INTEGRITY_CHECK_INTERVAL:-120}"
LAST_INTEGRITY_CHECK=0
INTEGRITY_OK_CACHE=1

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
    case "$1" in
        commander) echo "$PID_commander" ;;
        adjudicator) echo "$PID_adjudicator" ;;
        psyche) echo "$PID_psyche" ;;
        cartographer) echo "$PID_cartographer" ;;
        *) echo 0 ;;
    esac
}

set_pid() {
    case "$1" in
        commander) PID_commander="$2" ;;
        adjudicator) PID_adjudicator="$2" ;;
        psyche) PID_psyche="$2" ;;
        cartographer) PID_cartographer="$2" ;;
    esac
}

is_alive() {
    local pid
    pid=$(get_pid "$1")
    [ "$pid" -gt 0 ] 2>/dev/null && kill -0 "$pid" 2>/dev/null
}

wait_for_tmux() {
    local max_wait="${SYNCRESCENDENCE_TMUX_WAIT_SECONDS:-120}"
    local elapsed=0
    while [ "$elapsed" -lt "$max_wait" ]; do
        if /opt/homebrew/bin/tmux has-session -t "$SESSION" 2>/dev/null; then
            return 0
        fi
        sleep 2
        elapsed=$((elapsed + 2))
    done
    return 1
}

cleanup() {
    log "Supervisor shutting down — killing all loops"
    for agent in $AGENTS; do
        pid=$(get_pid "$agent")
        if [ "$pid" -gt 0 ] 2>/dev/null; then
            kill "$pid" 2>/dev/null || true
        fi
    done
    exit 0
}

trap cleanup INT TERM

integrity_ok() {
    local now
    now=$(date +%s)
    if [ "$((now - LAST_INTEGRITY_CHECK))" -lt "$INTEGRITY_CHECK_INTERVAL" ]; then
        [ "$INTEGRITY_OK_CACHE" -eq 1 ]
        return
    fi

    LAST_INTEGRITY_CHECK="$now"
    if [ -f "$INTEGRITY_GATE_SCRIPT" ]; then
        if bash "$INTEGRITY_GATE_SCRIPT" --repo "$REPO" --context auto_ingest_supervisor --quiet; then
            INTEGRITY_OK_CACHE=1
            return 0
        fi
        INTEGRITY_OK_CACHE=0
        log "INTEGRITY_GUARD: loop spawn paused until integrity restored"
        return 1
    fi

    INTEGRITY_OK_CACHE=1
    return 0
}

spawn_loop() {
    local agent="$1"
    local pane
    pane="$(get_pane "$agent")"

    if ! integrity_ok; then
        return 1
    fi

    if [ "$agent" != "cartographer" ]; then
        if ! wait_for_tmux; then
            log "tmux session '$SESSION' not ready yet; delaying $agent loop"
            return 1
        fi
    fi

    # Clear stale /tmp lock (new location)
    local tmp_lock="/tmp/auto_ingest_${agent}.lock"
    if [ -f "$tmp_lock" ]; then
        existing_pid=$(/bin/cat "$tmp_lock" 2>/dev/null)
        if [ -n "$existing_pid" ] && kill -0 "$existing_pid" 2>/dev/null; then
            set_pid "$agent" "$existing_pid"
            return 0
        fi
        rm -f "$tmp_lock"
    fi

    SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA="$SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA" \
    SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER="$SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER" \
    SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR="$SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR" \
    SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER="$SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER" \
    SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE="$SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE" \
    /bin/bash "$SCRIPT" "$agent" "$REPO" "$SESSION" "$pane" >> "/tmp/syncrescendence-auto-ingest-${agent}.log" 2>&1 &
    set_pid "$agent" $!
    log "Spawned $agent loop (PID $!, pane $pane) [bridge AJNA=$SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA]"
}

log "=== Supervisor starting ==="

while true; do
    for agent in $AGENTS; do
        if ! is_alive "$agent"; then
            spawn_loop "$agent" || true
        fi
    done
    sleep 15
done
