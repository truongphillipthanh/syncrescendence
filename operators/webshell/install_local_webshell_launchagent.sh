#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PLIST_SRC="$REPO_ROOT/orchestration/state/impl/com.syncrescendence.webshell-ops.plist"
PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_DST="$PLIST_DIR/com.syncrescendence.webshell-ops.plist"
LABEL="com.syncrescendence.webshell-ops"
LOG_DIR="$HOME/Library/Logs/syncrescendence"

mkdir -p "$PLIST_DIR" "$LOG_DIR"
cp "$PLIST_SRC" "$PLIST_DST"

launchctl bootout "gui/$(id -u)" "$PLIST_DST" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$(id -u)" "$PLIST_DST"
launchctl kickstart -k "gui/$(id -u)/$LABEL"
launchctl print "gui/$(id -u)/$LABEL" | sed -n '1,120p'
