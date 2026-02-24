#!/usr/bin/env bash
# DC-115: Export Graphiti/Neo4j env vars for non-login shells (launchd, cron).
# Source this in any script that needs to talk to Graphiti/Neo4j.
# CRITICAL: launchd does NOT source ~/.zshrc. This file is the workaround.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
ENV_FILE="$REPO_ROOT/.env.graphiti"

if [ -f "$ENV_FILE" ]; then
    set -a
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    set +a
fi

# Graphiti base URL (for memsync and other clients)
export GRAPHITI_BASE="${GRAPHITI_BASE:-http://localhost:8001}"
