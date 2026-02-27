#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# rearm_watchers.sh — One-command re-arm for Syncrescendence launchd watchers
#
# What it does:
# - Copies repo-managed plists into ~/Library/LaunchAgents
# - bootout (if already loaded)
# - bootstrap + kickstart the jobs
#
# NOTE: launchd jobs may fail with "Operation not permitted" until you grant
# Full Disk Access to the relevant binaries (see docs in chat / README).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
# NOTE: We maintain two installable plist sets because the Mac mini runs as user "home"
# while this laptop runs as user "system".
# - mini mode installs from launchd-mini (hardcoded /Users/home/...)
# - psyche mode installs from launchd-psyche (hardcoded /Users/system/...)
PLIST_SRC_DIR="$REPO_ROOT/orchestration/scripts/launchd"
PLIST_DST_DIR="$HOME/Library/LaunchAgents"
GUI_DOMAIN="gui/$(id -u)"

mkdir -p "$PLIST_DST_DIR"

copy_plist() {
  local name="$1"
  cp -f "$PLIST_SRC_DIR/$name" "$PLIST_DST_DIR/$name"
}

load_job() {
  local name="$1"
  local dst="$PLIST_DST_DIR/$name"
  # bootout if present (ignore errors)
  launchctl bootout "$GUI_DOMAIN" "$dst" 2>/dev/null || true
  # bootstrap
  launchctl bootstrap "$GUI_DOMAIN" "$dst"
  # kickstart immediately
  local label
  label=$(plutil -extract Label raw -o - "$dst")
  launchctl kickstart -k "$GUI_DOMAIN/$label"
  echo "[rearm] loaded: $label"
}

echo "[rearm] repo: $REPO_ROOT"
MODE="psyche"
if [ "${1:-}" = "--mini" ]; then MODE="mini"; fi
if [ "${1:-}" = "--psyche" ] || [ -z "${1:-}" ]; then MODE="psyche"; fi

# Select source plist set by mode
if [ "$MODE" = "mini" ]; then
  PLIST_SRC_DIR="$REPO_ROOT/orchestration/scripts/launchd-mini"
else
  PLIST_SRC_DIR="$REPO_ROOT/orchestration/scripts/launchd-psyche"
fi

echo "[rearm] copying plists from: $PLIST_SRC_DIR"

# Always copy plists we might need
for p in \
  com.syncrescendence.watchdog.plist \
  com.syncrescendence.watch-psyche.plist \
  com.syncrescendence.watch-canon.plist \
  com.syncrescendence.watch-commander.plist \
  com.syncrescendence.watch-ajna.plist \
  com.syncrescendence.watch-adjudicator.plist \
  com.syncrescendence.watch-cartographer.plist
do
  if [ -f "$PLIST_SRC_DIR/$p" ]; then
    copy_plist "$p"
  fi
done

echo "[rearm] bootstrapping jobs into $GUI_DOMAIN (mode: $MODE) ..."

if [ "$MODE" = "psyche" ]; then
  load_job com.syncrescendence.watchdog.plist
  load_job com.syncrescendence.watch-psyche.plist
  load_job com.syncrescendence.watch-canon.plist
  load_job com.syncrescendence.watch-cartographer.plist
  echo "[rearm] NOTE: psyche mode loaded watchdog+psyche+canon+cartographer."
fi

if [ "$MODE" = "mini" ]; then
  load_job com.syncrescendence.watchdog.plist
  load_job com.syncrescendence.watch-ajna.plist
  load_job com.syncrescendence.watch-commander.plist
  load_job com.syncrescendence.watch-adjudicator.plist
  load_job com.syncrescendence.watch-cartographer.plist
  echo "[rearm] NOTE: mini mode loaded watchdog+ajna+commander+adjudicator+cartographer."
fi

echo "[rearm] done."
