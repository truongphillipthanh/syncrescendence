#!/usr/bin/env bash
# config.sh - Syncrescendence central configuration
# Source this file: source "$(dirname "$0")/config.sh" OR source "$REPO_ROOT/orchestration/00-ORCHESTRATION/scripts/config.sh"

# Resolve this file path even when sourced via relative path or symlink.
_CONFIG_SOURCE="${BASH_SOURCE[0]}"
while [ -h "$_CONFIG_SOURCE" ]; do
  _CONFIG_DIR="$(cd -P "$(dirname "$_CONFIG_SOURCE")" && pwd)"
  _CONFIG_TARGET="$(readlink "$_CONFIG_SOURCE")"
  if [[ "$_CONFIG_TARGET" == /* ]]; then
    _CONFIG_SOURCE="$_CONFIG_TARGET"
  else
    _CONFIG_SOURCE="$_CONFIG_DIR/$_CONFIG_TARGET"
  fi
done
_CONFIG_DIR="$(cd -P "$(dirname "$_CONFIG_SOURCE")" && pwd)"

# Repository root (auto-detect from this file's location)
REPO_ROOT="$(cd "$_CONFIG_DIR/../../.." && pwd)"

# Directory structure
ORCHESTRATION_DIR="$REPO_ROOT/orchestration/00-ORCHESTRATION"
ENGINE_DIR="$REPO_ROOT/engine/02-ENGINE"
SOURCES_DIR="$REPO_ROOT/sources/04-SOURCES"
PRAXIS_DIR="$REPO_ROOT/praxis/05-SIGMA"
AGENTS_DIR="$REPO_ROOT/agents"
SOVEREIGN_DIR="$REPO_ROOT/-SOVEREIGN"
CANON_DIR="$REPO_ROOT/canon"
COLLAB_DIR="$REPO_ROOT/collab"
INBOX_DIR="$REPO_ROOT/-INBOX"

# Orchestration subdirectories
STATE_DIR="$ORCHESTRATION_DIR/state"
SCRIPTS_DIR="$ORCHESTRATION_DIR/scripts"
ARCHIVE_DIR="$ORCHESTRATION_DIR/archive"
TEMPLATES_DIR="$ORCHESTRATION_DIR/templates"

# Agent names and machine assignments
AGENTS=(commander adjudicator cartographer psyche ajna)
AGENT_MACHINES=(mini mini mini mini air)  # mac mini or macbook air

# SSH aliases
SSH_MINI="mini"
SSH_AIR="macbook-air"

# Graphiti
GRAPHITI_ENDPOINT="http://M1-Mac-mini.local:8001"

# Key paths
SSH_KEY_AJNA="$HOME/.ssh/id_ed25519_ajna"
SSH_KEY_PSYCHE="$HOME/.ssh/id_ed25519_ajna_to_psyche"

# Export for child-shell availability. Bash arrays remain shell-local by design.
export REPO_ROOT
export ORCHESTRATION_DIR ENGINE_DIR SOURCES_DIR PRAXIS_DIR AGENTS_DIR
export SOVEREIGN_DIR CANON_DIR COLLAB_DIR INBOX_DIR
export STATE_DIR SCRIPTS_DIR ARCHIVE_DIR TEMPLATES_DIR
export AGENTS AGENT_MACHINES
export SSH_MINI SSH_AIR GRAPHITI_ENDPOINT
export SSH_KEY_AJNA SSH_KEY_PSYCHE

unset _CONFIG_SOURCE _CONFIG_DIR _CONFIG_TARGET
