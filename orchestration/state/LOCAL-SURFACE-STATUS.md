# Local Surface Status

**Captured**: 2026-03-13T06:55:21Z

## Auth Surfaces

- `claude` authenticated: `True`
- `claude` email: `icloud.truongphillipthanh@gmail.com`
- `claude` organization: `icloud.truongphillipthanh@gmail.com's Organization`
- `claude` billing type: `stripe_subscription`
- `gcloud` authenticated: `True`
- `gcloud` active account: `syncrescendence@gmail.com`
- `gcloud` keychain pointer present: `True`
- `wrangler` authenticated: `None`
- `wrangler` email: `None`
- `wrangler` account id: `None`
- Cloudflare account-id keychain pointer present: `True`
- Manus keychain pointer present: `True`
- Manus API reachable: `True`

## OpenClaw Channels

- `slack` running: `True`
- `slack` probe ok: `True`
- `slack` last inbound observed: `None`
- `slack` last outbound observed: `None`
- `slack` workspace: `syncrescendence` (`T0AJD6Z6MM5`)
- `discord` running: `True`
- `discord` probe ok: `True`
- `discord` last inbound observed: `None`
- `discord` last outbound observed: `None`
- `discord` bot: `Ajna` (`1469043297174421618`)

## Ontology Domain Readiness

- Local API reachable: `True`
- Local proxy reachable: `True`
- macOS resolver sees domain: `True`
- `dig` sees public records: `True`
- Direct public edge health reachable: `True`
- Default local domain health reachable: `True`

## Tunnel

- `cloudflared` installed: `True`
- Cloudflare tunnel cert present: `True`
- Local tunnel config present: `True`
- Named tunnel present: `True`
- Tunnel LaunchAgent loaded: `True`
- Tunnel LaunchAgent state: `active`

## Reading

- Local auth and serving surfaces can be checked without exposing secrets in repo artifacts.
- Slack and Discord may be healthy and authenticated before any real inbound/outbound traffic is observed.
- If `dig` and direct edge health are green while default local curl still fails, the public cutover is live and only the local resolver is stale.
- CLI and Keychain status should remain pointer-only; credentials stay local.
