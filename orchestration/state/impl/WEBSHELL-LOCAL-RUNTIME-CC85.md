# WEBSHELL LOCAL RUNTIME CC85

## Objective

Run webshell as a persistent local operator surface with secrets sourced from macOS Keychain instead of plaintext shell history or repo files.

## Artifacts

1. launchagent plist:
   - [com.syncrescendence.webshell-ops.plist](/Users/system/syncrescendence/orchestration/state/impl/com.syncrescendence.webshell-ops.plist)
2. keychain helper:
   - [webshell_keychain.sh](/Users/system/syncrescendence/operators/webshell/webshell_keychain.sh)
3. launch runner:
   - [webshell_launchagent_runner.sh](/Users/system/syncrescendence/operators/webshell/webshell_launchagent_runner.sh)
4. install/status helpers:
   - [install_local_webshell_launchagent.sh](/Users/system/syncrescendence/operators/webshell/install_local_webshell_launchagent.sh)
   - [webshell_launchagent_status.sh](/Users/system/syncrescendence/operators/webshell/webshell_launchagent_status.sh)

## Secrets model

Keychain account:

- `syncrescendence` (default, override via `WEBSHELL_KEYCHAIN_ACCOUNT`)

Keychain services:

- `syncrescendence-webshell-callback-token` (required)
- `syncrescendence-github-webhook-secret` (optional)
- `syncrescendence-slack-signing-secret` (optional)

Webshell env fallback reads:

- `SYNC_WEBSHELL_CALLBACK_TOKEN`
- `SYNC_WEBSHELL_GITHUB_WEBHOOK_SECRET`
- `SYNC_WEBSHELL_SLACK_SIGNING_SECRET`
- `SYNC_WEBSHELL_ENFORCE_PROVIDER_SIGNATURES`

## Commands

```bash
make webshell-keychain-init-callback
make webshell-keychain-status
make webshell-launchagent-install
make webshell-launchagent-status
```

## Guardrails

1. bind stays on `127.0.0.1` by default.
2. callback write path remains fail-closed without callback token.
3. provider signature checks can be staged as optional, then switched to strict with:
   - `SYNC_WEBSHELL_ENFORCE_PROVIDER_SIGNATURES=1`
