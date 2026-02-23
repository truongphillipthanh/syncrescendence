#!/bin/bash
# Wrapper for corpus_health_check.py — launchd compatible
export PYTHONUNBUFFERED=1
export HOME=/Users/home
export PATH="/Users/home/.syncrescendence/venv/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
exec /Users/home/.syncrescendence/venv/bin/python3 -u /Users/home/.syncrescendence/scripts/corpus_health_check.py
