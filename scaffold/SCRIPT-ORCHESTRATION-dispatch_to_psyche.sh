#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# dispatch_to_psyche.sh — Create a task dispatch file for Psyche
# Usage: bash dispatch_to_psyche.sh "TOPIC" "TASK_DESCRIPTION"
# Writes a task file to agents/psyche/inbox/ for autonomous processing
#
# For dispatching to other agents, use dispatch.sh instead.

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi

# Dispatch to Psyche via the generic dispatcher
bash "$REPO_ROOT/orchestration/scripts/dispatch.sh" psyche "$1" "$2"
