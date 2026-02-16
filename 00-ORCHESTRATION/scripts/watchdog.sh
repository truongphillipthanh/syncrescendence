#!/bin/bash
# Syncrescendence 4-Tier Self-Healing Watchdog
# Adapted from openclaw-self-healing (Ramsbaby, MIT)
# Runs every 60 seconds via launchd
#
# L0: launchd KeepAlive (handled by launchd itself)
# L1: PID verification + launchctl kickstart
# L2: HTTP health checks + config validation
# L3: Escalation to Commander inbox
# L4: Discord alert (via OpenClaw)

set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

LOG="/tmp/syncrescendence-watchdog.log"
RESTART_LOG="/tmp/syncrescendence-watchdog-restarts.log"
REPO_ROOT="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
INBOX="$REPO_ROOT/-INBOX/commander/00-INBOX0"
COCKPIT_SCRIPT="$REPO_ROOT/00-ORCHESTRATION/scripts/cockpit.sh"
TMUX_SESSION="constellation"

resolve_codex_model() {
    local SAFE_DEFAULT="gpt-5.2-codex"

    # 1. Explicit env override (launchd plists set this for guaranteed safety)
    if [ -n "${SYNCRESCENDENCE_CODEX_MODEL:-}" ]; then
        echo "$SYNCRESCENDENCE_CODEX_MODEL"
        return 0
    fi

    # 2. Runtime probe: ask codex directly for available models (most reliable)
    if command -v codex >/dev/null 2>&1; then
        local probe
        probe=$(codex models 2>/dev/null | head -20) || true
        if [ -n "$probe" ]; then
            for slug in "gpt-5.3-codex" "gpt-5.2-codex" "gpt-5-codex" "gpt-5.1-codex"; do
                if echo "$probe" | grep -qF "$slug"; then
                    echo "$slug"
                    return 0
                fi
            done
        fi
    fi

    # 3. Safe fallback (cache is not authoritative for entitlement checks)
    echo "$SAFE_DEFAULT"
}

CODEX_MODEL="$(resolve_codex_model)"
CODEX_REASONING_EFFORT="${SYNCRESCENDENCE_CODEX_REASONING_EFFORT:-high}"
resolve_codex_autonomy_flag() {
    if [ -n "${SYNCRESCENDENCE_CODEX_AUTONOMY_FLAG:-}" ]; then
        echo "$SYNCRESCENDENCE_CODEX_AUTONOMY_FLAG"
        return 0
    fi
    if ! command -v codex >/dev/null 2>&1; then
        echo "--full-auto"
        return 0
    fi
    local help_text
    help_text=$(codex --help 2>/dev/null || true)
    if echo "$help_text" | grep -q -- '--dangerously-bypass-approvals-and-sandbox'; then
        echo "--dangerously-bypass-approvals-and-sandbox"
        return 0
    fi
    if echo "$help_text" | grep -q -- '--full-auto'; then
        echo "--full-auto"
        return 0
    fi
    echo ""
}
CODEX_AUTONOMY_FLAG="$(resolve_codex_autonomy_flag)"
GEMINI_MODEL="${SYNCRESCENDENCE_GEMINI_MODEL:-gemini-2.5-pro}"
PSYCHE_BOOT_CMD="cd '$REPO_ROOT' && openclaw tui --session main --thinking high"
ADJUDICATOR_BOOT_CMD="cd '$REPO_ROOT' && codex ${CODEX_AUTONOMY_FLAG:+$CODEX_AUTONOMY_FLAG }-m '$CODEX_MODEL' -c 'model_reasoning_effort=\"$CODEX_REASONING_EFFORT\"'"
CARTOGRAPHER_BOOT_CMD="cd '$REPO_ROOT' && gemini -m '$GEMINI_MODEL' --yolo"
AGENT_SKILLS_DIR="${SYNCRESCENDENCE_AGENT_SKILLS_DIR:-$HOME/.agents/skills}"
if [ ! -d "$AGENT_SKILLS_DIR" ]; then
    for fallback in "/Users/home/.agents/skills" "/Users/system/.agents/skills"; do
        if [ -d "$fallback" ]; then
            AGENT_SKILLS_DIR="$fallback"
            break
        fi
    done
fi
CODEX_SKILLS_DIR="${SYNCRESCENDENCE_CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
OPENCLAW_SKILLS_DIR="${SYNCRESCENDENCE_OPENCLAW_SKILLS_DIR:-$HOME/.openclaw/skills}"
OPENCLAW_WORKSPACE_SKILLS_DIR="${SYNCRESCENDENCE_OPENCLAW_WORKSPACE_SKILLS_DIR:-$HOME/.openclaw/workspace/skills}"
CLAUDE_SKILLS_DIR="${SYNCRESCENDENCE_CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
PLIST_TEMPLATE_DIR_MINI="$REPO_ROOT/00-ORCHESTRATION/scripts/launchd-mini"
PLIST_TEMPLATE_DIR_PSYCHE="$REPO_ROOT/00-ORCHESTRATION/scripts/launchd-psyche"
REQUIRED_WATCHERS_CRITICAL="watch-psyche watch-adjudicator watch-cartographer"
LOCK_DIR="/tmp/syncrescendence-watchdog.lock"
ESCALATION_STAMP="/tmp/syncrescendence-watchdog-escalation.epoch"
ESCALATION_COOLDOWN_SECONDS=900
SKILL_SYNC_LAST_RUN_FILE="/tmp/syncrescendence-watchdog-skill-sync.epoch"
SKILL_SYNC_EVERY_SECONDS="${SYNCRESCENDENCE_SKILL_SYNC_EVERY_SECONDS:-3600}"
UID_NUM=$(id -u)

now() { date '+%Y-%m-%d %H:%M:%S'; }
log() { echo "[$(now)] $1" >> "$LOG"; }
warn() { echo "[$(now)] WARN: $1" >> "$LOG"; }
crit() { echo "[$(now)] CRIT: $1" >> "$LOG"; }

# Single-instance guard: skip overlapping runs.
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    exit 0
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT

log "=== Watchdog run ==="

RESTART_COUNT=0
LAUNCHCTL_MANAGE_OK=true

LAUNCHCTL_PROBE=$(launchctl list 2>&1 || true)
if echo "$LAUNCHCTL_PROBE" | grep -qi 'Operation not permitted'; then
    LAUNCHCTL_MANAGE_OK=false
    warn "launchctl access restricted; entering degraded mode for this watchdog run."
elif [ -z "$(printf '%s' "$LAUNCHCTL_PROBE" | tr -d '[:space:]')" ]; then
    LAUNCHCTL_MANAGE_OK=false
    warn "launchctl returned empty output; entering degraded mode for this watchdog run."
fi

# ──────────────────────────────────────────────
# L1: PID Verification
# ──────────────────────────────────────────────
check_service() {
    local name="$1"
    local label="com.syncrescendence.$name"
    local pid
    local plist_path="$LAUNCH_AGENTS_DIR/$label.plist"

    if [ "$LAUNCHCTL_MANAGE_OK" != "true" ]; then
        warn "$name: launchctl unavailable; skipping service check."
        return 0
    fi

    pid=$(launchctl list 2>/dev/null | awk -v label="$label" '$3==label {print $1; found=1} END {if (!found) print ""}')

    if [ -z "$pid" ]; then
        if [ ! -f "$plist_path" ]; then
            if [ -f "$PLIST_TEMPLATE_DIR_MINI/$label.plist" ]; then
                mkdir -p "$LAUNCH_AGENTS_DIR"
                cp -f "$PLIST_TEMPLATE_DIR_MINI/$label.plist" "$plist_path"
                warn "$name: plist missing; installed from launchd-mini template."
            elif [ -f "$PLIST_TEMPLATE_DIR_PSYCHE/$label.plist" ]; then
                mkdir -p "$LAUNCH_AGENTS_DIR"
                cp -f "$PLIST_TEMPLATE_DIR_PSYCHE/$label.plist" "$plist_path"
                warn "$name: plist missing; installed from launchd-psyche template."
            fi
        fi
        if [ -f "$plist_path" ]; then
            warn "$name: launchd label absent. Bootstrapping from plist."
            launchctl bootstrap "gui/$UID_NUM" "$plist_path" 2>/dev/null || true
            launchctl kickstart -k "gui/$UID_NUM/$label" 2>/dev/null || true
            echo "$(now) bootstrap $name" >> "$RESTART_LOG"
            RESTART_COUNT=$((RESTART_COUNT + 1))
            pid=$(launchctl list 2>/dev/null | awk -v label="$label" '$3==label {print $1; found=1} END {if (!found) print ""}')
        fi
    fi

    if [ "$pid" = "-" ] || [ -z "$pid" ]; then
        warn "$name: not running (PID=$pid). Restarting via kickstart."
        launchctl kickstart -k "gui/$UID_NUM/$label" 2>/dev/null || true
        echo "$(now) kickstart $name" >> "$RESTART_LOG"
        RESTART_COUNT=$((RESTART_COUNT + 1))
    fi
}

http_code() {
    local url="$1"
    local status
    status=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 5 "$url" 2>/dev/null || true)
    status="${status:0:3}"
    if ! echo "$status" | grep -Eq '^[0-9]{3}$'; then
        status="000"
    fi
    echo "$status"
}

ensure_skill_links() {
    local target_dir="$1"
    local label="$2"
    local added=0
    local repaired=0

    if [ ! -d "$AGENT_SKILLS_DIR" ]; then
        warn "skills sync skipped for $label: source dir missing ($AGENT_SKILLS_DIR)"
        return 0
    fi

    mkdir -p "$target_dir"
    while IFS= read -r src_skill; do
        local name dst
        name=$(basename "$src_skill")
        dst="$target_dir/$name"
        if [ -L "$dst" ]; then
            if [ ! -e "$dst" ]; then
                rm -f "$dst"
                ln -s "$src_skill" "$dst"
                repaired=$((repaired + 1))
            fi
            continue
        fi
        if [ -e "$dst" ]; then
            # Preserve local, non-symlink skill folders.
            continue
        fi
        ln -s "$src_skill" "$dst"
        added=$((added + 1))
    done < <(find "$AGENT_SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d ! -name '.*' | sort)

    if [ "$added" -gt 0 ] || [ "$repaired" -gt 0 ]; then
        log "skills sync ($label): added=$added repaired=$repaired"
    else
        log "skills sync ($label): no changes"
    fi
}

ensure_skill_repertoire() {
    local now_epoch last_epoch
    now_epoch=$(date +%s)
    last_epoch=0
    if [ -f "$SKILL_SYNC_LAST_RUN_FILE" ]; then
        last_epoch=$(cat "$SKILL_SYNC_LAST_RUN_FILE" 2>/dev/null || echo 0)
    fi

    if [ $((now_epoch - last_epoch)) -lt "$SKILL_SYNC_EVERY_SECONDS" ]; then
        log "skills sync: skipped (cooldown ${SKILL_SYNC_EVERY_SECONDS}s)"
        return 0
    fi

    ensure_skill_links "$CODEX_SKILLS_DIR" "codex"
    ensure_skill_links "$OPENCLAW_SKILLS_DIR" "openclaw"
    ensure_skill_links "$OPENCLAW_WORKSPACE_SKILLS_DIR" "openclaw-workspace"
    ensure_skill_links "$CLAUDE_SKILLS_DIR" "claude"

    echo "$now_epoch" > "$SKILL_SYNC_LAST_RUN_FILE"
}

resolve_pane_target() {
    local title="$1"
    tmux list-panes -t "$TMUX_SESSION":cockpit -F '#{pane_index}|#{pane_title}' 2>/dev/null \
      | awk -F'|' -v t="$title" '$2==t {print "'"$TMUX_SESSION"':cockpit." $1; exit}'
}

ensure_agent_pane() {
    local title="$1"
    local launch_cmd="$2"
    local pane_target current_cmd

    pane_target=$(resolve_pane_target "$title")
    if [ -z "$pane_target" ]; then
        warn "tmux pane missing for $title"
        return 1
    fi

    current_cmd=$(tmux display-message -p -t "$pane_target" '#{pane_current_command}' 2>/dev/null || true)
    if [ "$current_cmd" = "node" ]; then
        log "$title pane healthy (cmd=$current_cmd)"
        return 0
    fi

    warn "$title pane unhealthy (cmd=${current_cmd:-none}). Restarting agent command."
    tmux send-keys -t "$pane_target" C-c 2>/dev/null || true
    tmux send-keys -t "$pane_target" "$launch_cmd" C-m 2>/dev/null || true
    echo "$(now) tmux-restart $title cmd=${current_cmd:-none}" >> "$RESTART_LOG"
    RESTART_COUNT=$((RESTART_COUNT + 1))
    return 0
}

ensure_cockpit_agents() {
    if ! command -v tmux >/dev/null 2>&1; then
        warn "tmux not found; skipping cockpit self-heal."
        return 0
    fi

    local tmux_probe
    tmux_probe=$(tmux list-sessions 2>&1 || true)
    if echo "$tmux_probe" | grep -qi 'Operation not permitted'; then
        warn "tmux access restricted; skipping cockpit self-heal."
        return 0
    fi

    if [ ! -x "$COCKPIT_SCRIPT" ]; then
        warn "cockpit script missing or not executable: $COCKPIT_SCRIPT"
        return 0
    fi

    if ! tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
        warn "tmux session '$TMUX_SESSION' missing. Recreating in detached mode."
        if bash "$COCKPIT_SCRIPT" --launch-detached >> "$LOG" 2>&1; then
            echo "$(now) tmux-recreate $TMUX_SESSION" >> "$RESTART_LOG"
            RESTART_COUNT=$((RESTART_COUNT + 1))
        else
            warn "failed to recreate tmux session '$TMUX_SESSION'"
        fi
        return 0
    fi

    if [ -z "$(resolve_pane_target Psyche)" ] || [ -z "$(resolve_pane_target Adjudicator)" ]; then
        warn "tmux cockpit layout drift detected. Rebuilding session '$TMUX_SESSION'."
        tmux kill-session -t "$TMUX_SESSION" 2>/dev/null || true
        if bash "$COCKPIT_SCRIPT" --launch-detached >> "$LOG" 2>&1; then
            echo "$(now) tmux-rebuild $TMUX_SESSION" >> "$RESTART_LOG"
            RESTART_COUNT=$((RESTART_COUNT + 1))
        else
            warn "failed to rebuild tmux session '$TMUX_SESSION'"
        fi
        return 0
    fi

    ensure_agent_pane "Psyche" "$PSYCHE_BOOT_CMD"
    ensure_agent_pane "Adjudicator" "$ADJUDICATOR_BOOT_CMD"
    ensure_agent_pane "Cartographer" "$CARTOGRAPHER_BOOT_CMD"
}

# Check always-on services only (NOT interval-based: corpus-health, qmd-update)
for svc in chroma-server webhook-receiver; do
    check_service "$svc" 2>/dev/null || true
done

# Check critical watchers even if they are currently unloaded.
for watcher in $REQUIRED_WATCHERS_CRITICAL; do
    check_service "$watcher" 2>/dev/null || true
done

# Check any other loaded watcher agents (exclude watchdog itself).
if [ "$LAUNCHCTL_MANAGE_OK" = "true" ]; then
    while IFS= read -r watcher; do
        [ -z "$watcher" ] && continue
        case " $REQUIRED_WATCHERS_CRITICAL " in
            *" $watcher "*) continue ;;
        esac
        check_service "$watcher" 2>/dev/null || true
    done < <(
        launchctl list 2>/dev/null \
          | awk '$3 ~ /^com\.syncrescendence\.watch-/ {sub(/^com\.syncrescendence\./, "", $3); if ($3 != "watchdog") print $3}'
    )
fi

# Keep cockpit agents alive and skill repertoire fully linked.
ensure_cockpit_agents
ensure_skill_repertoire

# ──────────────────────────────────────────────
# L2: HTTP Health Checks
# ──────────────────────────────────────────────
check_http() {
    local name="$1"
    local url="$2"
    local label="com.syncrescendence.$3"
    local status

    status=$(http_code "$url")

    if [ "$status" != "200" ]; then
        if [ "$LAUNCHCTL_MANAGE_OK" = "true" ]; then
            crit "$name: HTTP health check failed (status=$status). Restarting."
            launchctl kickstart -k "gui/$UID_NUM/$label" 2>/dev/null || true
            echo "$(now) http-restart $name status=$status" >> "$RESTART_LOG"
            RESTART_COUNT=$((RESTART_COUNT + 1))
        else
            warn "$name: HTTP health check failed (status=$status) but launchctl is unavailable; skipping restart."
        fi
    else
        log "$name: healthy (HTTP $status)"
    fi
}

check_http "Chroma" "http://localhost:8765/health" "chroma-server"
check_http "Webhook" "http://localhost:8888/health" "webhook-receiver"

# OpenClaw gateway (info only — we don't manage it via launchctl)
OC_STATUS=$(http_code "http://localhost:18789/health")
if [ "$OC_STATUS" != "200" ]; then
    warn "OpenClaw gateway: not responding (status=$OC_STATUS). Cannot auto-restart."
else
    log "OpenClaw gateway: healthy (HTTP $OC_STATUS)"
fi

# Docker services (info only — managed by Docker Desktop, not launchctl)
for svc_info in "Neo4j:7474:/" "Graphiti:8001:/healthcheck" "Qdrant:6333:/healthz"; do
    SVC_NAME=$(echo "$svc_info" | cut -d: -f1)
    SVC_PORT=$(echo "$svc_info" | cut -d: -f2)
    SVC_PATH=$(echo "$svc_info" | cut -d: -f3)
    SVC_STATUS=$(http_code "http://localhost:${SVC_PORT}${SVC_PATH}")
    if [ "$SVC_STATUS" != "200" ]; then
        warn "$SVC_NAME (Docker): not responding (status=$SVC_STATUS)"
    else
        log "$SVC_NAME (Docker): healthy (HTTP $SVC_STATUS)"
    fi
done

# ──────────────────────────────────────────────
# L2: Config Validation
# ──────────────────────────────────────────────
if ! python3 -c "import json; json.load(open('$HOME/.openclaw/openclaw.json'))" 2>/dev/null; then
    crit "openclaw.json is corrupt or unparseable!"
fi

# Verify critical repo files exist
for f in CLAUDE.md COCKPIT.md; do
    if [ ! -f "$REPO_ROOT/$f" ]; then
        warn "Missing critical file: $f"
    fi
done

# ──────────────────────────────────────────────
# L3: Escalation (restart loop detection)
# ──────────────────────────────────────────────
RECENT_RESTARTS=0
if [ -f "$RESTART_LOG" ]; then
    HOUR_AGO=$(date -v-1H '+%Y-%m-%d %H:%M:%S' 2>/dev/null || date '+%Y-%m-%d %H:%M:%S')
    RECENT_RESTARTS=$(awk -v cutoff="$HOUR_AGO" '$0 >= cutoff' "$RESTART_LOG" 2>/dev/null | wc -l | tr -d ' ')
fi

if [ "$RECENT_RESTARTS" -gt 3 ]; then
    NOW_EPOCH=$(date +%s)
    LAST_ESCALATION_EPOCH=0
    if [ -f "$ESCALATION_STAMP" ]; then
        LAST_ESCALATION_EPOCH=$(cat "$ESCALATION_STAMP" 2>/dev/null || echo 0)
    fi
    if [ $((NOW_EPOCH - LAST_ESCALATION_EPOCH)) -lt "$ESCALATION_COOLDOWN_SECONDS" ]; then
        warn "ESCALATION suppressed: cooldown active (${ESCALATION_COOLDOWN_SECONDS}s)."
    else
        crit "ESCALATION: $RECENT_RESTARTS restarts in last hour. Creating Commander task."
        TASK_FILE="$INBOX/TASK-WATCHDOG-$(date +%Y%m%d%H%M%S).md"
        mkdir -p "$INBOX"
        cat > "$TASK_FILE" << TASK
---
Status: PENDING
Priority: P0
Reply-To: watchdog
CC: commander
---
# WATCHDOG ESCALATION: Service restart loop detected

**Time**: $(now)
**Restarts in last hour**: $RECENT_RESTARTS

## Recent restart log
$(tail -10 "$RESTART_LOG")

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
TASK
        echo "$NOW_EPOCH" > "$ESCALATION_STAMP"
        log "Escalation task created: $TASK_FILE"
    fi
fi

# ──────────────────────────────────────────────
# Summary
# ──────────────────────────────────────────────
log "Watchdog complete. Restarts this run: $RESTART_COUNT. Recent (1h): $RECENT_RESTARTS."
