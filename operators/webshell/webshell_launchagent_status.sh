#!/usr/bin/env bash
set -euo pipefail

LABEL="${WEBSHELL_LAUNCH_LABEL:-com.syncrescendence.webshell-ops}"
PORT="${WEBSHELL_PORT:-8890}"

echo "== launchctl =="
launchctl print "gui/$(id -u)/$LABEL" | sed -n '1,120p'
echo
echo "== health =="
curl -fsS "http://127.0.0.1:${PORT}/health" || true
echo
