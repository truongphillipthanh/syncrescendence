#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# cockpit_startup.sh — Syncrescendence Constellation Startup Health Check
# DC-130: Cockpit activation sequence
# Runs FROM MacBook Air. Mac mini commands go through `ssh mini`.
# NEVER uses ping (blocked by Stealth Mode on both machines).
#
# Usage:
#   cockpit_startup.sh           # Full health check (connectivity + processes + docker + scaffold + memsync)
#   cockpit_startup.sh --quick   # Quick check (connectivity + processes only)
#   cockpit_startup.sh --json    # Output JSON report instead of terminal
#   cockpit_startup.sh --quiet   # Suppress terminal output, exit code only (0=healthy, 1=degraded, 2=critical)

set -uo pipefail

REPO="${SYNCRESCENDENCE_PATH:-$HOME/syncrescendence}"
SCRIPTS_DIR="${REPO}/orchestration/00-ORCHESTRATION/scripts"
REPORT_DIR="${REPO}/orchestration/state"
REPORT_FILE="${REPORT_DIR}/DYN-COCKPIT_STARTUP_REPORT.md"
JSON_FILE="${REPORT_DIR}/DYN-COCKPIT_STARTUP_REPORT.json"
MINI_HOST="mini"
TMUX_SESSION="constellation"
DOCKER_BIN="/Applications/Docker.app/Contents/Resources/bin/docker"

# ── Modes ────────────────────────────────────────────────────────────────────
MODE_QUICK=false
MODE_JSON=false
MODE_QUIET=false

for arg in "$@"; do
    case "$arg" in
        --quick)  MODE_QUICK=true ;;
        --json)   MODE_JSON=true ;;
        --quiet)  MODE_QUIET=true ;;
        --help|-h)
            echo "cockpit_startup.sh — Constellation startup health check"
            echo ""
            echo "Usage:"
            echo "  cockpit_startup.sh           Full health check"
            echo "  cockpit_startup.sh --quick   Connectivity + processes only"
            echo "  cockpit_startup.sh --json    JSON report output"
            echo "  cockpit_startup.sh --quiet   Exit code only (0=ok, 1=degraded, 2=critical)"
            exit 0
            ;;
    esac
done

# ── Colors ───────────────────────────────────────────────────────────────────
if [[ -t 1 ]] && [[ "$MODE_QUIET" == "false" ]]; then
    C_RESET="\033[0m"
    C_BOLD="\033[1m"
    C_GREEN="\033[32m"
    C_YELLOW="\033[33m"
    C_RED="\033[31m"
    C_CYAN="\033[36m"
    C_DIM="\033[2m"
else
    C_RESET="" C_BOLD="" C_GREEN="" C_YELLOW="" C_RED="" C_CYAN="" C_DIM=""
fi

# ── State tracking ───────────────────────────────────────────────────────────
declare -a CHECK_NAMES=()
declare -a CHECK_STATUSES=()
declare -a CHECK_DETAILS=()
CRITICAL_COUNT=0
WARN_COUNT=0
OK_COUNT=0

record() {
    local name="$1" status="$2" detail="$3"
    CHECK_NAMES+=("$name")
    CHECK_STATUSES+=("$status")
    CHECK_DETAILS+=("$detail")
    case "$status" in
        OK)       ((OK_COUNT++)) ;;
        WARN)     ((WARN_COUNT++)) ;;
        CRITICAL) ((CRITICAL_COUNT++)) ;;
    esac
}

status_icon() {
    case "$1" in
        OK)       echo -e "${C_GREEN}[OK]${C_RESET}" ;;
        WARN)     echo -e "${C_YELLOW}[WARN]${C_RESET}" ;;
        CRITICAL) echo -e "${C_RED}[CRIT]${C_RESET}" ;;
    esac
}

emit() {
    [[ "$MODE_QUIET" == "true" ]] && return
    echo -e "$@"
}

# ── Timestamp ────────────────────────────────────────────────────────────────
TS_START=$(date +%s)
TS_ISO=$(date '+%Y-%m-%d %H:%M:%S')

emit ""
emit "${C_BOLD}${C_CYAN}=== SYNCRESCENDENCE COCKPIT STARTUP ===${C_RESET}"
emit "${C_DIM}${TS_ISO} | MacBook Air -> Mac mini${C_RESET}"
emit ""

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 1: SSH connectivity to Mac mini (Neural Bridge)
# ══════════════════════════════════════════════════════════════════════════════
emit "${C_BOLD}[1] Neural Bridge (SSH to Mac mini)${C_RESET}"

MINI_HOSTNAME=""
if MINI_HOSTNAME=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$MINI_HOST" hostname 2>/dev/null); then
    record "neural_bridge" "OK" "Connected: ${MINI_HOSTNAME}"
    emit "  $(status_icon OK) Connected to ${MINI_HOSTNAME}"
else
    record "neural_bridge" "CRITICAL" "SSH to mini failed (timeout or refused)"
    emit "  $(status_icon CRITICAL) Cannot reach Mac mini via SSH"
    # If bridge is down, everything remote fails — skip remote checks
    if [[ "$MODE_QUICK" == "true" ]]; then
        emit ""
        emit "${C_RED}${C_BOLD}CRITICAL: Neural Bridge down. Cannot proceed.${C_RESET}"
    fi
fi

BRIDGE_UP=false
[[ "${CHECK_STATUSES[-1]}" == "OK" ]] && BRIDGE_UP=true

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 2: tmux constellation session on Mac mini
# ══════════════════════════════════════════════════════════════════════════════
emit "${C_BOLD}[2] tmux constellation session${C_RESET}"

if [[ "$BRIDGE_UP" == "true" ]]; then
    PANE_LIST=""
    if PANE_LIST=$(ssh -o ConnectTimeout=5 "$MINI_HOST" "tmux list-panes -t ${TMUX_SESSION}:cockpit -F '#{pane_id}:#{pane_title}' 2>/dev/null"); then
        PANE_COUNT=$(echo "$PANE_LIST" | wc -l | tr -d ' ')
        record "tmux_session" "OK" "${PANE_COUNT} panes in cockpit window"
        emit "  $(status_icon OK) Session '${TMUX_SESSION}' alive (${PANE_COUNT} panes)"
    else
        record "tmux_session" "CRITICAL" "Session '${TMUX_SESSION}' not found on Mac mini"
        emit "  $(status_icon CRITICAL) Session '${TMUX_SESSION}' not found"
    fi
else
    record "tmux_session" "CRITICAL" "Skipped (bridge down)"
    emit "  $(status_icon CRITICAL) Skipped (bridge down)"
fi

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 3: Agent CLI processes alive in their panes
# ══════════════════════════════════════════════════════════════════════════════
emit "${C_BOLD}[3] Agent CLI processes${C_RESET}"

# Agent pane mapping from CLAUDE.md Operational Registry
declare -A AGENT_PANES=(
    [psyche]="1.1"
    [commander]="1.3"
    [adjudicator]="1.5"
    [cartographer]="1.7"
)
declare -A AGENT_CLI=(
    [psyche]="openclaw"
    [commander]="claude"
    [adjudicator]="codex"
    [cartographer]="gemini"
)

if [[ "$BRIDGE_UP" == "true" ]] && [[ "${CHECK_STATUSES[1]}" == "OK" ]]; then
    for agent in psyche commander adjudicator cartographer; do
        pane="${AGENT_PANES[$agent]}"
        cli="${AGENT_CLI[$agent]}"
        # Capture last 5 lines from the pane to check for signs of life
        PANE_CONTENT=$(ssh -o ConnectTimeout=5 "$MINI_HOST" \
            "tmux capture-pane -t ${TMUX_SESSION}:${pane} -p -S -5 2>/dev/null" 2>/dev/null || echo "")

        # Check if the CLI process is running in the pane's shell
        PANE_PID=$(ssh -o ConnectTimeout=5 "$MINI_HOST" \
            "tmux list-panes -t ${TMUX_SESSION}:${pane} -F '#{pane_pid}' 2>/dev/null" 2>/dev/null || echo "")

        PROC_ALIVE=false
        if [[ -n "$PANE_PID" ]]; then
            # Check if any child of the pane shell matches the expected CLI
            CHILD_PROCS=$(ssh -o ConnectTimeout=5 "$MINI_HOST" \
                "ps -o comm= -p \$(pgrep -P ${PANE_PID} 2>/dev/null) 2>/dev/null || echo ''" 2>/dev/null || echo "")
            if echo "$CHILD_PROCS" | grep -qi "$cli"; then
                PROC_ALIVE=true
            fi
        fi

        if [[ "$PROC_ALIVE" == "true" ]]; then
            record "agent_${agent}" "OK" "${cli} running in pane ${pane}"
            emit "  $(status_icon OK) ${agent} (${cli}) alive in pane ${pane}"
        elif [[ -n "$PANE_CONTENT" ]]; then
            # Pane exists but CLI may not be running
            record "agent_${agent}" "WARN" "Pane ${pane} exists but ${cli} process not detected"
            emit "  $(status_icon WARN) ${agent}: pane ${pane} exists, ${cli} not detected"
        else
            record "agent_${agent}" "CRITICAL" "Pane ${pane} empty or unreachable"
            emit "  $(status_icon CRITICAL) ${agent}: pane ${pane} unreachable"
        fi
    done
else
    for agent in psyche commander adjudicator cartographer; do
        record "agent_${agent}" "CRITICAL" "Skipped (tmux session down)"
        emit "  $(status_icon CRITICAL) ${agent}: skipped (session down)"
    done
fi

# ── Quick mode stops here ────────────────────────────────────────────────────
if [[ "$MODE_QUICK" == "true" ]]; then
    emit ""
    emit "${C_DIM}--quick mode: skipping Docker, scaffold, memsync checks${C_RESET}"
else

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 4: Docker containers on Mac mini (Neo4j, Graphiti, Qdrant)
# ══════════════════════════════════════════════════════════════════════════════
emit "${C_BOLD}[4] Docker containers (Mac mini)${C_RESET}"

EXPECTED_CONTAINERS=("neo4j" "graphiti" "qdrant")

if [[ "$BRIDGE_UP" == "true" ]]; then
    DOCKER_PS=$(ssh -o ConnectTimeout=5 "$MINI_HOST" \
        "${DOCKER_BIN} ps --format '{{.Names}}:{{.Status}}' 2>/dev/null" 2>/dev/null || echo "DOCKER_FAIL")

    if [[ "$DOCKER_PS" == "DOCKER_FAIL" ]]; then
        record "docker_engine" "CRITICAL" "Docker not responding on Mac mini"
        emit "  $(status_icon CRITICAL) Docker engine not responding"
        for c in "${EXPECTED_CONTAINERS[@]}"; do
            record "container_${c}" "CRITICAL" "Skipped (Docker down)"
        done
    else
        record "docker_engine" "OK" "Docker responding"
        emit "  $(status_icon OK) Docker engine responding"

        for c in "${EXPECTED_CONTAINERS[@]}"; do
            # Match container name (case-insensitive, partial match)
            MATCH=$(echo "$DOCKER_PS" | grep -i "$c" || echo "")
            if [[ -n "$MATCH" ]]; then
                STATUS=$(echo "$MATCH" | head -1 | cut -d: -f2-)
                if echo "$STATUS" | grep -qi "up"; then
                    record "container_${c}" "OK" "${STATUS}"
                    emit "  $(status_icon OK) ${c}: ${STATUS}"
                else
                    record "container_${c}" "WARN" "${STATUS}"
                    emit "  $(status_icon WARN) ${c}: ${STATUS}"
                fi
            else
                record "container_${c}" "CRITICAL" "Container not found"
                emit "  $(status_icon CRITICAL) ${c}: not running"
            fi
        done
    fi
else
    record "docker_engine" "CRITICAL" "Skipped (bridge down)"
    emit "  $(status_icon CRITICAL) Skipped (bridge down)"
    for c in "${EXPECTED_CONTAINERS[@]}"; do
        record "container_${c}" "CRITICAL" "Skipped (bridge down)"
    done
fi

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 5: scaffold_validate.sh (structural health)
# ══════════════════════════════════════════════════════════════════════════════
emit "${C_BOLD}[5] Scaffold validation${C_RESET}"

SCAFFOLD_SCRIPT="${SCRIPTS_DIR}/scaffold_validate.sh"
if [[ -x "$SCAFFOLD_SCRIPT" ]]; then
    SCAFFOLD_OUT=$(bash "$SCAFFOLD_SCRIPT" 2>&1) && SCAFFOLD_RC=$? || SCAFFOLD_RC=$?
    if [[ "$SCAFFOLD_RC" -eq 0 ]]; then
        record "scaffold" "OK" "All structural checks passed"
        emit "  $(status_icon OK) scaffold_validate.sh passed"
    else
        FAIL_LINES=$(echo "$SCAFFOLD_OUT" | grep -iE "FAIL|ERROR|WARN" | head -3)
        record "scaffold" "WARN" "Exit ${SCAFFOLD_RC}: ${FAIL_LINES}"
        emit "  $(status_icon WARN) scaffold_validate.sh exit ${SCAFFOLD_RC}"
        emit "  ${C_DIM}${FAIL_LINES}${C_RESET}"
    fi
else
    record "scaffold" "WARN" "scaffold_validate.sh not found or not executable"
    emit "  $(status_icon WARN) scaffold_validate.sh not found at ${SCAFFOLD_SCRIPT}"
fi

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 6: memsync daemon status
# ══════════════════════════════════════════════════════════════════════════════
emit "${C_BOLD}[6] Memsync daemon${C_RESET}"

# Check if memsync is running as a launchd service or direct process
MEMSYNC_PID=$(pgrep -f "memsync_daemon" 2>/dev/null || echo "")
MEMSYNC_LAUNCHD=$(launchctl list 2>/dev/null | grep -i "memsync" || echo "")

if [[ -n "$MEMSYNC_PID" ]]; then
    record "memsync" "OK" "Running (PID: ${MEMSYNC_PID})"
    emit "  $(status_icon OK) memsync_daemon running (PID: ${MEMSYNC_PID})"
elif [[ -n "$MEMSYNC_LAUNCHD" ]]; then
    # launchd knows about it but process may not be running
    LAUNCHD_STATUS=$(echo "$MEMSYNC_LAUNCHD" | awk '{print $1}')
    if [[ "$LAUNCHD_STATUS" == "-" ]]; then
        record "memsync" "WARN" "Registered in launchd but not running"
        emit "  $(status_icon WARN) Registered in launchd but not running"
    else
        record "memsync" "OK" "launchd managed (${MEMSYNC_LAUNCHD})"
        emit "  $(status_icon OK) launchd managed"
    fi
else
    record "memsync" "WARN" "Not running (no process or launchd entry found)"
    emit "  $(status_icon WARN) memsync_daemon not detected"
fi

fi  # end of non-quick checks

# ══════════════════════════════════════════════════════════════════════════════
# REPORT GENERATION
# ══════════════════════════════════════════════════════════════════════════════
TS_END=$(date +%s)
DURATION=$((TS_END - TS_START))

# Overall status
OVERALL="HEALTHY"
[[ "$WARN_COUNT" -gt 0 ]] && OVERALL="DEGRADED"
[[ "$CRITICAL_COUNT" -gt 0 ]] && OVERALL="CRITICAL"

emit ""
emit "${C_BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${C_RESET}"
case "$OVERALL" in
    HEALTHY)  emit "${C_GREEN}${C_BOLD}CONSTELLATION STATUS: HEALTHY${C_RESET} (${OK_COUNT} OK)" ;;
    DEGRADED) emit "${C_YELLOW}${C_BOLD}CONSTELLATION STATUS: DEGRADED${C_RESET} (${OK_COUNT} OK, ${WARN_COUNT} WARN)" ;;
    CRITICAL) emit "${C_RED}${C_BOLD}CONSTELLATION STATUS: CRITICAL${C_RESET} (${OK_COUNT} OK, ${WARN_COUNT} WARN, ${CRITICAL_COUNT} CRIT)" ;;
esac
emit "${C_DIM}Completed in ${DURATION}s${C_RESET}"
emit ""

# ── Markdown report ──────────────────────────────────────────────────────────
mkdir -p "$REPORT_DIR" 2>/dev/null || true
{
    echo "# Cockpit Startup Report"
    echo "**Timestamp**: ${TS_ISO}"
    echo "**Overall**: ${OVERALL}"
    echo "**Duration**: ${DURATION}s"
    echo "**Mode**: $(if [[ "$MODE_QUICK" == "true" ]]; then echo "quick"; else echo "full"; fi)"
    echo ""
    echo "| Check | Status | Detail |"
    echo "|-------|--------|--------|"
    for i in "${!CHECK_NAMES[@]}"; do
        echo "| ${CHECK_NAMES[$i]} | ${CHECK_STATUSES[$i]} | ${CHECK_DETAILS[$i]} |"
    done
    echo ""
    echo "---"
    echo "*Generated by cockpit_startup.sh at ${TS_ISO}*"
} > "$REPORT_FILE"

# ── JSON report ──────────────────────────────────────────────────────────────
{
    echo "{"
    echo "  \"timestamp\": \"${TS_ISO}\","
    echo "  \"overall\": \"${OVERALL}\","
    echo "  \"duration_s\": ${DURATION},"
    echo "  \"mode\": \"$(if [[ "$MODE_QUICK" == "true" ]]; then echo "quick"; else echo "full"; fi)\","
    echo "  \"counts\": { \"ok\": ${OK_COUNT}, \"warn\": ${WARN_COUNT}, \"critical\": ${CRITICAL_COUNT} },"
    echo "  \"checks\": ["
    for i in "${!CHECK_NAMES[@]}"; do
        COMMA=""
        [[ $i -lt $((${#CHECK_NAMES[@]} - 1)) ]] && COMMA=","
        # Escape double quotes in detail
        SAFE_DETAIL=$(echo "${CHECK_DETAILS[$i]}" | sed 's/"/\\"/g')
        echo "    { \"name\": \"${CHECK_NAMES[$i]}\", \"status\": \"${CHECK_STATUSES[$i]}\", \"detail\": \"${SAFE_DETAIL}\" }${COMMA}"
    done
    echo "  ]"
    echo "}"
} > "$JSON_FILE"

if [[ "$MODE_JSON" == "true" ]] && [[ "$MODE_QUIET" == "false" ]]; then
    cat "$JSON_FILE"
fi

# ── Exit code ────────────────────────────────────────────────────────────────
case "$OVERALL" in
    HEALTHY)  exit 0 ;;
    DEGRADED) exit 1 ;;
    CRITICAL) exit 2 ;;
esac
