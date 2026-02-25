#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# Wrapper for webhook_receiver.py — launchd compatible
export PYTHONUNBUFFERED=1
export HOME=/Users/home
export PATH="/Users/home/.syncrescendence/venv/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
exec /Users/home/.syncrescendence/venv/bin/python3 -u /Users/home/.syncrescendence/scripts/webhook_receiver.py
