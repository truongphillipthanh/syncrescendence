# Ajna Slack Runbook — CC93

- Office: `ajna`
- Runtime: OpenClaw
- Channel mode: `socket`
- Canonical workspace: `syncrescendence`

## Purpose

Replace fragile click-by-click Slack setup with one durable manifest and a minimal runtime hydration path.

## Design Law

- Slack is the operator bus, not the constitutional archive.
- Tokens do not belong in repo artifacts.
- Repo stores manifest, doctrine, and pointer-only runtime state.
- macOS Keychain + local OpenClaw config hold the live secrets.

## Manifest Path

- [SLACK-APP-MANIFEST-CC93.json](/Users/system/syncrescendence/offices/ajna/platform/templates/SLACK-APP-MANIFEST-CC93.json)

## Apply Flow

1. In Slack app settings, open `App Manifest`.
2. Replace current manifest with the repo manifest.
3. Apply the manifest.
4. Confirm `Socket Mode` is enabled.
5. Install or reinstall the app to workspace.
6. Copy:
   - `Bot User OAuth Token` (`xoxb-...`)
   - `App-Level Token` (`xapp-...`) with `connections:write`

## Runtime Injection

Store the tokens in Keychain under service `syncrescendence`:

```bash
security add-generic-password -U -a "slack-bot-token" -s "syncrescendence" -w "<xoxb-token>"
security add-generic-password -U -a "slack-app-token" -s "syncrescendence" -w "<xapp-token>"
python3 operators/runtime/hydrate-openclaw-channels.py
openclaw gateway restart
openclaw channels status --probe --json
```

## Current Doctrine

- Broadest sane OpenClaw bot scopes live in the manifest.
- `chat:write.customize` is included so Ajna can present as its own office identity.
- `commands` and `files:*` are enabled to avoid a second rebuild when native Slack command use expands.
- If Slack app UI becomes brittle again, use the manifest path instead of manual scope clicking.
