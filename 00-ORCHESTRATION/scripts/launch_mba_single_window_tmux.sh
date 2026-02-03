#!/usr/bin/env bash
# launch_mba_single_window_tmux.sh — one-command MBA launcher (psyche_boot + tmux cockpit)
set -euo pipefail

REPO="$HOME/Desktop/syncrescendence"
cd "$REPO"

git pull
bash 00-ORCHESTRATION/scripts/psyche_boot.sh
bash 00-ORCHESTRATION/scripts/tmux_mba_cockpit.sh
