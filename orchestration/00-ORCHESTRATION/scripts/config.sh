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

# Repository root (auto-detect from this file's location, override with SYNCRESCENDENCE_ROOT)
REPO_ROOT_DETECTED="$(cd "$_CONFIG_DIR/../../.." && pwd)"
SYNCRESCENDENCE_ROOT="${SYNCRESCENDENCE_ROOT:-$REPO_ROOT_DETECTED}"
REPO_ROOT="$SYNCRESCENDENCE_ROOT"

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

# ---------------------------------------------------------------------------
# Proprioceptive config assertions
# ---------------------------------------------------------------------------

_sync_config_fail() {
  local assumption="$1"
  local repair_hint="$2"
  local context="${3:-config}"
  {
    printf "[config:%s] FAIL\n" "$context"
    printf "assumption: %s\n" "$assumption"
    printf "repair: %s\n" "$repair_hint"
  } >&2
  if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
    return 1
  fi
  exit 1
}

sync_assert_dir() {
  local path="$1"
  local description="$2"
  if [[ -d "$path" ]]; then
    return 0
  fi
  _sync_config_fail \
    "directory exists for ${description}: ${path}" \
    "Set SYNCRESCENDENCE_ROOT correctly or create the directory." \
    "assert_dir"
}

sync_assert_file() {
  local path="$1"
  local description="$2"
  if [[ -f "$path" ]]; then
    return 0
  fi
  _sync_config_fail \
    "file exists for ${description}: ${path}" \
    "Restore the file from canon/state or regenerate it before running this script." \
    "assert_file"
}

sync_assert_env() {
  local var_name="$1"
  local description="$2"
  local value="${!var_name-}"
  if [[ -n "$value" ]]; then
    return 0
  fi
  _sync_config_fail \
    "environment variable is set for ${description}: ${var_name}" \
    "Export ${var_name} before running this script (for root: export SYNCRESCENDENCE_ROOT=/path/to/repo)." \
    "assert_env"
}

sync_config_preflight() {
  local script_name="${1:-unknown-script}"
  printf "[config:preflight] begin script=%s root=%s\n" "$script_name" "$REPO_ROOT" >&2

  sync_assert_env "SYNCRESCENDENCE_ROOT" "syncrescendence root override/anchor" || return 1

  sync_assert_dir "$ORCHESTRATION_DIR" "orchestration directory" || return 1
  sync_assert_dir "$CANON_DIR" "canon directory" || return 1
  sync_assert_dir "$ENGINE_DIR" "engine directory" || return 1
  sync_assert_dir "$SOURCES_DIR" "sources directory" || return 1
  sync_assert_dir "$PRAXIS_DIR" "praxis directory" || return 1
  sync_assert_dir "$AGENTS_DIR" "agents directory" || return 1

  sync_assert_file "$STATE_DIR/DYN-DEFERRED_COMMITMENTS.md" "deferred commitments state" || return 1
  sync_assert_file "$STATE_DIR/ARCH-INTENTION_COMPASS.md" "intention compass architecture state" || return 1

  printf "[config:preflight] pass script=%s\n" "$script_name" >&2
}

# Export for child-shell availability. Bash arrays remain shell-local by design.
export REPO_ROOT
export REPO_ROOT_DETECTED
export SYNCRESCENDENCE_ROOT
export SYNCRESCENDENCE_REPO_ROOT="$SYNCRESCENDENCE_ROOT"
export ORCHESTRATION_DIR ENGINE_DIR SOURCES_DIR PRAXIS_DIR AGENTS_DIR
export SOVEREIGN_DIR CANON_DIR COLLAB_DIR INBOX_DIR
export STATE_DIR SCRIPTS_DIR ARCHIVE_DIR TEMPLATES_DIR
export AGENTS AGENT_MACHINES
export SSH_MINI SSH_AIR GRAPHITI_ENDPOINT
export SSH_KEY_AJNA SSH_KEY_PSYCHE

unset _CONFIG_SOURCE _CONFIG_DIR _CONFIG_TARGET
