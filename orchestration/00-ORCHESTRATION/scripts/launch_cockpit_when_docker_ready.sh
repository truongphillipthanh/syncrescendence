#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# launch_cockpit_when_docker_ready.sh
# Periodic idempotent cockpit health launcher:
# - if constellation exists: repair degraded panes only
# - if constellation missing: wait for Docker gate, then launch detached

set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
LOG="/tmp/syncrescendence-cockpit-autostart.log"
DOCKER_HELPER="${REPO}/orchestration/scripts/ensure_docker_desktop.sh"
COCKPIT_SCRIPT="${REPO}/orchestration/scripts/cockpit.sh"
SESSION="${SYNCRESCENDENCE_TMUX_SESSION:-constellation}"
MAX_WAIT_SECONDS="${SYNCRESCENDENCE_DOCKER_WAIT_SECONDS:-180}"
SLEEP_SECONDS=3
TMUX_SOCKET="/private/tmp/tmux-$(id -u)/default"
TMUX_BIN="/opt/homebrew/bin/tmux -S ${TMUX_SOCKET}"

log() {
  printf '[%s] [cockpit-autostart] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG"
}

check_pane_health() {
  local pane="$1"
  local expected="$2"
  local cmd
  cmd=$(${TMUX_BIN} display-message -p -t "${SESSION}:${pane}" '#{pane_current_command}' 2>/dev/null || true)

  case "$cmd" in
    zsh|bash|sh|fish|"")
      log "Pane ${pane} degraded to '${cmd:-none}'; re-launching"
      ${TMUX_BIN} send-keys -t "${SESSION}:${pane}" C-c 2>/dev/null || true
      ${TMUX_BIN} send-keys -t "${SESSION}:${pane}" "$expected" C-m 2>/dev/null || true
      ;;
    *)
      log "Pane ${pane} healthy (${cmd})"
      ;;
  esac
}

cd "$REPO" 2>/dev/null || true

if ${TMUX_BIN} has-session -t "$SESSION" 2>/dev/null; then
  log "Constellation session already running; performing pane health check"
  check_pane_health "1.1" "cd '$REPO' && openclaw tui --session main --thinking high"
  check_pane_health "1.3" "cd '$REPO' && claude --dangerously-skip-permissions"
  check_pane_health "1.5" "cd '$REPO' && codex -m gpt-5.2-codex -c 'model_reasoning_effort=\"high\"'"
  check_pane_health "1.7" "cd '$REPO' && gemini -m gemini-2.5-pro --yolo"
  exit 0
fi

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
