#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# skill_sync.sh — Instant skill synchronization across all agent platforms.
# Triggered by launchd WatchPaths on canonical skills directory.
# Replaces watchdog.sh 600s cooldown polling with event-driven sync.
# Safety: 5-second debounce prevents rapid-fire during bulk installs.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
LOG="/tmp/syncrescendence-skill-sync.log"
DEBOUNCE_FILE="/tmp/syncrescendence-skill-sync.debounce"
DEBOUNCE_SECONDS=5

# Skill directories — same as watchdog.sh
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

now() { date '+%Y-%m-%d %H:%M:%S'; }
log() { echo "[$(now)] $1" >> "$LOG"; }

# Debounce: skip if last run was within DEBOUNCE_SECONDS
if [ -f "$DEBOUNCE_FILE" ]; then
    last_epoch=$(cat "$DEBOUNCE_FILE" 2>/dev/null || echo 0)
    now_epoch=$(date +%s)
    if [ $((now_epoch - last_epoch)) -lt "$DEBOUNCE_SECONDS" ]; then
        exit 0
    fi
fi
date +%s > "$DEBOUNCE_FILE"

if [ ! -d "$AGENT_SKILLS_DIR" ]; then
    log "WARN: canonical skills dir not found ($AGENT_SKILLS_DIR), skipping"
    exit 0
fi

ensure_skill_links() {
    local target_dir="$1"
    local label="$2"
    local added=0
    local repaired=0

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
            continue
        fi
        ln -s "$src_skill" "$dst"
        added=$((added + 1))
    done < <(find "$AGENT_SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d ! -name '.*' | sort)

    if [ "$added" -gt 0 ] || [ "$repaired" -gt 0 ]; then
        log "sync ($label): added=$added repaired=$repaired"
    fi
}

log "=== Skill sync triggered ==="

ensure_skill_links "$CODEX_SKILLS_DIR" "codex"
ensure_skill_links "$OPENCLAW_SKILLS_DIR" "openclaw"
ensure_skill_links "$OPENCLAW_WORKSPACE_SKILLS_DIR" "openclaw-workspace"
ensure_skill_links "$CLAUDE_SKILLS_DIR" "claude"

log "=== Skill sync complete ==="
