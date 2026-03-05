#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-/Users/system/syncrescendence}"
HOST="${WEBSHELL_HOST:-127.0.0.1}"
PORT="${WEBSHELL_PORT:-8890}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

ACCOUNT="${WEBSHELL_KEYCHAIN_ACCOUNT:-syncrescendence}"
CALLBACK_SERVICE="${WEBSHELL_CALLBACK_SERVICE:-syncrescendence-webshell-callback-token}"
GITHUB_SERVICE="${WEBSHELL_GITHUB_SERVICE:-syncrescendence-github-webhook-secret}"
SLACK_SERVICE="${WEBSHELL_SLACK_SERVICE:-syncrescendence-slack-signing-secret}"

read_secret() {
  local service="$1"
  security find-generic-password -w -s "$service" -a "$ACCOUNT" 2>/dev/null || true
}

CALLBACK_TOKEN="$(read_secret "$CALLBACK_SERVICE")"
if [ -z "$CALLBACK_TOKEN" ]; then
  echo "webshell launch failed: missing callback token in keychain service=$CALLBACK_SERVICE account=$ACCOUNT" >&2
  exit 1
fi

export SYNC_WEBSHELL_CALLBACK_TOKEN="$CALLBACK_TOKEN"

GITHUB_SECRET="$(read_secret "$GITHUB_SERVICE")"
if [ -n "$GITHUB_SECRET" ]; then
  export SYNC_WEBSHELL_GITHUB_WEBHOOK_SECRET="$GITHUB_SECRET"
fi

SLACK_SECRET="$(read_secret "$SLACK_SERVICE")"
if [ -n "$SLACK_SECRET" ]; then
  export SYNC_WEBSHELL_SLACK_SIGNING_SECRET="$SLACK_SECRET"
fi

# Keep signatures optional unless explicitly toggled.
export SYNC_WEBSHELL_ENFORCE_PROVIDER_SIGNATURES="${SYNC_WEBSHELL_ENFORCE_PROVIDER_SIGNATURES:-0}"

exec "$PYTHON_BIN" "$REPO_ROOT/operators/webshell/syncrescendence_dev_shell.py" \
  --repo-root "$REPO_ROOT" \
  --host "$HOST" \
  --port "$PORT"
