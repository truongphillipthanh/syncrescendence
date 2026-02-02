#!/usr/bin/env bash
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
PLIST_SRC_DIR="$REPO_ROOT/00-ORCHESTRATION/scripts/launchd"
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
echo "[rearm] copying plists from: $PLIST_SRC_DIR"

copy_plist com.syncrescendence.watch-psyche.plist
copy_plist com.syncrescendence.watch-canon.plist

# Optional: only load these on the machine that actually runs them
if [ -f "$PLIST_SRC_DIR/com.syncrescendence.watch-commander.plist" ]; then
  copy_plist com.syncrescendence.watch-commander.plist
fi
if [ -f "$PLIST_SRC_DIR/com.syncrescendence.watch-ajna.plist" ]; then
  copy_plist com.syncrescendence.watch-ajna.plist
fi

echo "[rearm] bootstrapping jobs into $GUI_DOMAIN ..."
load_job com.syncrescendence.watch-psyche.plist
load_job com.syncrescendence.watch-canon.plist

# These two should usually only run on their respective hosts
if [ -f "$PLIST_DST_DIR/com.syncrescendence.watch-commander.plist" ]; then
  echo "[rearm] NOTE: commander watcher plist present; load only if this machine runs Commander."
fi
if [ -f "$PLIST_DST_DIR/com.syncrescendence.watch-ajna.plist" ]; then
  echo "[rearm] NOTE: ajna watcher plist present; load only if this machine runs Ajna."
fi

echo "[rearm] done."
