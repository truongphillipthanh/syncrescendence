#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# sync_openclaw_skills.sh — Mirror OpenClaw workspace skills between machines (no secrets)
#
# Purpose:
# - Keep Ajna (mini) and Psyche (laptop) with the same "outfitment" in ~/.openclaw/workspace/skills
# - Copies ONLY skill/plugin code (NOT ~/.openclaw/openclaw.json, NOT credentials)
#
# Typical usage:
#   # On Ajna (mini), pull from Psyche:
#   bash sync_openclaw_skills.sh --pull --from psyche --persona ajna
#
#   # On Psyche, pull from Ajna:
#   bash sync_openclaw_skills.sh --pull --from ajna --persona psyche
#
# Requirements:
# - ssh access between machines (recommend SSH config aliases: "ajna" and "psyche")
# - rsync available on both sides (macOS has it)
#
# Safety:
# - This script never touches ~/.openclaw/openclaw.json or ~/.openclaw/credentials
# - It excludes node_modules by default (we want source-of-truth dirs; install/build happens locally if needed)

set -euo pipefail

MODE=""
FROM_HOST=""
PERSONA=""
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage:
  sync_openclaw_skills.sh --pull --from <ssh-host-alias> --persona <ajna|psyche> [--dry-run]

Examples:
  bash sync_openclaw_skills.sh --pull --from psyche --persona ajna
  bash sync_openclaw_skills.sh --pull --from ajna --persona psyche --dry-run
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --pull) MODE="pull"; shift ;;
    --from) FROM_HOST="$2"; shift 2 ;;
    --persona) PERSONA="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1"; usage; exit 2 ;;
  esac
done

if [ -z "$MODE" ] || [ -z "$FROM_HOST" ] || [ -z "$PERSONA" ]; then
  usage; exit 2
fi

SRC_DIR="/Users/${USER}/.openclaw/workspace/skills/"
# NOTE: we pull from a remote; remote path must be explicit per remote user.
# We assume remote user == host persona user. Override via SSH config if needed.
# We'll probe remote $HOME to derive correct path.

DST_DIR="$HOME/.openclaw/workspace/skills/"
mkdir -p "$DST_DIR"

# Skill allowlist: keep this conservative; expand as needed.
SKILLS=(
  "supermemory"
  "hindsight"
  "graphiti-memory"
  "agent-browser-stagehand"
  "prompt-guard"
  "cron-writer"
  "dont-hack-me"
  "find-skills"
  "clawguard"
  "qmd-skill"
  "summarize"
)

RSYNC_FLAGS=("-a" "--delete" "--prune-empty-dirs")
if [ "$DRY_RUN" = "1" ]; then
  RSYNC_FLAGS+=("-n" "-v")
fi

# Excludes: keep installs local
EXCLUDES=(
  "--exclude" "**/node_modules"
  "--exclude" "**/.git"
  "--exclude" "**/.DS_Store"
  "--exclude" "**/dist"
)

# Resolve remote HOME
REMOTE_HOME=$(ssh "$FROM_HOST" 'printf %s "$HOME"' 2>/dev/null || true)
if [ -z "$REMOTE_HOME" ]; then
  echo "[sync] ERROR: could not ssh to $FROM_HOST" >&2
  exit 1
fi

REMOTE_SKILLS_DIR="$REMOTE_HOME/.openclaw/workspace/skills"

echo "[sync] persona: $PERSONA"
echo "[sync] from: $FROM_HOST:$REMOTE_SKILLS_DIR"
echo "[sync] to:   $DST_DIR"

for s in "${SKILLS[@]}"; do
  echo "[sync] syncing: $s"
  rsync "${RSYNC_FLAGS[@]}" "${EXCLUDES[@]}" \
    "$FROM_HOST:$REMOTE_SKILLS_DIR/$s/" "$DST_DIR/$s/" \
    || echo "[sync] WARN: failed or missing on source: $s" >&2

done

echo "[sync] done. Next: run 'openclaw doctor --fix' and restart gateway if plugin loads changed."