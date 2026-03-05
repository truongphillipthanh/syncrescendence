# Webshell External Stage1 Runbook — CC84

**Date**: 2026-03-04  
**Status**: active  
**Class**: operator runbook

## Goal

Expose a narrow `/ops/*` surface through existing Cloudflare tunnel + Caddy while keeping callback writes authenticated and bounded.

## Preconditions

1. cloudflared tunnel is active for `syncrescendence.com` -> local Caddy `:8080`.
2. Caddy is using:
   - [ontology-api.Caddyfile.local](/Users/system/syncrescendence/orchestration/state/impl/ontology-api.Caddyfile.local)
3. webshell is running locally on `127.0.0.1:8890`.

## Step 1: Start webshell in secure mode

Generate token:

```bash
make webshell-generate-token
```

Run webshell:

```bash
make webshell-dev PORT=8890 CALLBACK_TOKEN="<token>"
```

Optional provider signature secrets:

```bash
make webshell-dev PORT=8890 CALLBACK_TOKEN="<token>" GITHUB_WEBHOOK_SECRET="<gh-secret>" SLACK_SIGNING_SECRET="<slack-secret>"
```

If you want strict signature requirements for supported providers:

```bash
make webshell-dev PORT=8890 CALLBACK_TOKEN="<token>" GITHUB_WEBHOOK_SECRET="<gh-secret>" SLACK_SIGNING_SECRET="<slack-secret>" ENFORCE_PROVIDER_SIGNATURES=1
```

## Step 2: Ensure Caddy routes `/ops/*`

Local Caddy config includes:

1. `@ops path /ops /ops/*`
2. `uri strip_prefix /ops`
3. `reverse_proxy 127.0.0.1:8890`

## Step 3: Validate local path routing

1. `curl http://127.0.0.1:8890/health`
2. `curl http://localhost:8080/ops/health`
3. `curl http://localhost:8080/ops/status`

## Step 4: Validate callback auth behavior

Without token (expected failure):

1. POST to `/ops/callbacks/generic` without `X-Sync-Token`
2. expect `503 callback_auth_not_configured` or `401 unauthorized`

With token (expected success):

```bash
curl -X POST "http://localhost:8080/ops/callbacks/generic" \
  -H "Content-Type: application/json" \
  -H "X-Sync-Token: <token>" \
  -d '{"event":"ops-callback-smoke"}'
```

Expected outputs:

1. `runtime/webshell/callbacks/inbox/CALLBACK-*.json`
2. `offices/commander/inbox/pending/TASK-callback-*.md`

## Step 5: Public edge verification

1. `curl https://syncrescendence.com/ops/health`
2. `curl https://syncrescendence.com/ops/status`

Do not expose callback endpoints publicly until token and provider signature posture is reviewed.

## Security posture

1. callbacks are fail-closed without token
2. github/slack signature verification can be enabled via secrets
3. signature freshness enforcement is active for Slack timestamp validation
4. secrets remain local and are never committed to repo
5. this stage is operational control-surface only, not product surface
