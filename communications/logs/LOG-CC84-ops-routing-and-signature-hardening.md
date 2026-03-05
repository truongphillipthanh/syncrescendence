# LOG-CC84 ops routing and signature hardening

## Objective

Promote the webshell from local-only visibility to controlled `/ops/*` routability through the existing Caddy/Cloudflare path while preserving fail-closed callback writes.

## Landed repo changes

1. webshell signature support:
   - [syncrescendence_dev_shell.py](/Users/system/syncrescendence/operators/webshell/syncrescendence_dev_shell.py)
   - GitHub HMAC verification (`X-Hub-Signature-256`)
   - Slack signature + timestamp verification (`X-Slack-Signature`, `X-Slack-Request-Timestamp`)
2. make targets:
   - [Makefile](/Users/system/syncrescendence/Makefile)
   - added `webshell-generate-token`
3. caddy routing docs/config:
   - [ontology-api.Caddyfile.local](/Users/system/syncrescendence/orchestration/state/impl/ontology-api.Caddyfile.local)
   - [ontology-api.Caddyfile.example](/Users/system/syncrescendence/orchestration/state/impl/ontology-api.Caddyfile.example)
   - [dev-webshell.Caddyfile.example](/Users/system/syncrescendence/orchestration/state/impl/dev-webshell.Caddyfile.example)
4. runbook:
   - [WEBSHELL-EXTERNAL-STAGE1-RUNBOOK-CC84.md](/Users/system/syncrescendence/orchestration/state/impl/WEBSHELL-EXTERNAL-STAGE1-RUNBOOK-CC84.md)
5. ontology compatibility fix after root-shell migration:
   - [operators/ontology/ontology_v1.py](/Users/system/syncrescendence/operators/ontology/ontology_v1.py)
   - corrected repo-root/schema path resolution in operator

## Host-local runtime change

The Homebrew Caddy service was importing a stale path. Updated host file:

- `/opt/homebrew/etc/Caddyfile`
- old: `/Users/system/syncrescendence/00-ORCHESTRATION/state/impl/ontology-api.Caddyfile.local`
- new: `/Users/system/syncrescendence/orchestration/state/impl/ontology-api.Caddyfile.local`

Then restarted service:

- `brew services restart caddy`

Ontology LaunchAgent was also retargeted and restarted:

- `/Users/system/Library/LaunchAgents/com.syncrescendence.ontology-v1.plist`
- old program path: `/Users/system/syncrescendence/ontology_v1.py`
- new program path: `/Users/system/syncrescendence/operators/ontology/ontology_v1.py`

## Verification

1. `caddy validate --config ... --adapter caddyfile` passed for all three Caddyfiles.
2. webshell callback hardening checks:
   - callback denied when no token
   - callback accepted with token
   - GitHub callback denied without signature, accepted with valid signature
   - Slack callback accepted with valid signature and fresh timestamp
3. routing checks:
   - `http://localhost:8080/ops/health` returns webshell health when webshell is running
4. ontology checks:
   - `http://127.0.0.1:8787/health` returns `200`
   - `http://localhost:8080/health` returns `200`
