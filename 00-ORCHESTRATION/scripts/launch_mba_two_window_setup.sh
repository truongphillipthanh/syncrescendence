#!/usr/bin/env bash
# launch_mba_two_window_setup.sh — one-command MBA launcher (iTerm 2 windows)
set -euo pipefail

REPO="$HOME/Desktop/syncrescendence"
cd "$REPO"

osascript 00-ORCHESTRATION/scripts/iterm_launch_psyche_and_commander.applescript
