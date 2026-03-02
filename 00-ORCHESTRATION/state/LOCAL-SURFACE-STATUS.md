# Local Surface Status

**Captured**: 2026-03-02T04:22:55Z

## Auth Surfaces

- `gcloud` authenticated: `True`
- `gcloud` active account: `icloud.truongphillipthanh@gmail.com`
- `gcloud` keychain pointer present: `True`
- `wrangler` authenticated: `True`
- `wrangler` email: `icloud.truongphillipthanh@gmail.com`
- `wrangler` account id: `b76f644c19db95eb0dfc2b6db1e7186d`
- Cloudflare account-id keychain pointer present: `True`
- Manus keychain pointer present: `True`
- Manus API reachable: `True`

## Ontology Domain Readiness

- Local API reachable: `True`
- Local proxy reachable: `True`
- Public DNS resolves: `False`
- Public domain health reachable: `False`

## Reading

- Local auth and serving surfaces can be checked without exposing secrets in repo artifacts.
- Public cutover remains blocked until DNS and edge routing make `syncrescendence.com` resolve and serve `/health`.
- CLI and Keychain status should remain pointer-only; credentials stay local.
