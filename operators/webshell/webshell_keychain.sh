#!/usr/bin/env bash
set -euo pipefail

ACCOUNT="${WEBSHELL_KEYCHAIN_ACCOUNT:-syncrescendence}"
CALLBACK_SERVICE="${WEBSHELL_CALLBACK_SERVICE:-syncrescendence-webshell-callback-token}"
GITHUB_SERVICE="${WEBSHELL_GITHUB_SERVICE:-syncrescendence-github-webhook-secret}"
SLACK_SERVICE="${WEBSHELL_SLACK_SERVICE:-syncrescendence-slack-signing-secret}"

usage() {
  cat <<'EOF'
Usage:
  webshell_keychain.sh status
  webshell_keychain.sh init-callback-token
  webshell_keychain.sh set-callback-token <token>
  webshell_keychain.sh set-github-secret <secret>
  webshell_keychain.sh set-slack-secret <secret>
EOF
}

present() {
  local service="$1"
  if security find-generic-password -w -s "$service" -a "$ACCOUNT" >/dev/null 2>&1; then
    echo "present"
  else
    echo "missing"
  fi
}

store_secret() {
  local service="$1"
  local value="$2"
  security add-generic-password -U -a "$ACCOUNT" -s "$service" -w "$value" >/dev/null
  echo "stored: $service"
}

generate_token() {
  python3 -c "import secrets; print(secrets.token_urlsafe(32))"
}

cmd="${1:-status}"
case "$cmd" in
  status)
    echo "account=$ACCOUNT"
    echo "callback_token=$(present "$CALLBACK_SERVICE") service=$CALLBACK_SERVICE"
    echo "github_secret=$(present "$GITHUB_SERVICE") service=$GITHUB_SERVICE"
    echo "slack_secret=$(present "$SLACK_SERVICE") service=$SLACK_SERVICE"
    ;;
  init-callback-token)
    if [ "$(present "$CALLBACK_SERVICE")" = "present" ]; then
      echo "callback token already present"
      exit 0
    fi
    token="$(generate_token)"
    store_secret "$CALLBACK_SERVICE" "$token"
    ;;
  set-callback-token)
    [ $# -ge 2 ] || { usage; exit 1; }
    store_secret "$CALLBACK_SERVICE" "$2"
    ;;
  set-github-secret)
    [ $# -ge 2 ] || { usage; exit 1; }
    store_secret "$GITHUB_SERVICE" "$2"
    ;;
  set-slack-secret)
    [ $# -ge 2 ] || { usage; exit 1; }
    store_secret "$SLACK_SERVICE" "$2"
    ;;
  *)
    usage
    exit 1
    ;;
esac
