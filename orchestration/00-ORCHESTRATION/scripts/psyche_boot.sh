#!/usr/bin/env bash
# psyche_boot.sh — enforce Psyche-box watcher topology + open a stateful dashboard
#
# Goal: on Psyche laptop, ONLY run psyche+canon watchers.
# This script:
# 1) bootouts any other syncrescendence watcher LaunchAgents if present
# 2) rearms watchers in --psyche mode (psyche+canon)
# 3) prints a quick status block

set -euo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null || echo "$HOME/Desktop/syncrescendence")"

GUI_DOMAIN="gui/$(id -u)"
LA_DIR="$HOME/Library/LaunchAgents"

BOOTOUT=(
  com.syncrescendence.watch-ajna.plist
  com.syncrescendence.watch-commander.plist
  com.syncrescendence.watch-adjudicator.plist
  com.syncrescendence.watch-cartographer.plist
)

for p in "${BOOTOUT[@]}"; do
  if [ -f "$LA_DIR/$p" ]; then
    echo "[psyche_boot] bootout: $p"
    launchctl bootout "$GUI_DOMAIN" "$LA_DIR/$p" 2>/dev/null || true
  fi
done

echo "[psyche_boot] rearm psyche watchers"
bash orchestration/scripts/rearm_watchers.sh --psyche

echo "[psyche_boot] loaded jobs:"
launchctl list | egrep 'com\.syncrescendence\.watch-(psyche|canon)' || true

echo "[psyche_boot] (sanity) other watcher jobs should NOT be loaded on this box:"
launchctl list | egrep 'com\.syncrescendence\.watch-(ajna|commander|adjudicator|cartographer)' || true

# show recent errors
for f in /tmp/syncrescendence-watch-psyche.err /tmp/syncrescendence-watch-canon.err; do
  echo "--- $f"
  tail -n 20 "$f" 2>/dev/null || true
 done
