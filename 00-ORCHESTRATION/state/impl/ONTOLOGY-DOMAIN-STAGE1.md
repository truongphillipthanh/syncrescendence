# Ontology Domain Stage 1

**Date**: 2026-03-02  
**Purpose**: First domain-facing deployment shape for `syncrescendence.com`

## Current Status

As of **March 2, 2026**, `syncrescendence.com` is not yet resolving publicly from this machine.

That means the repo should be **domain-ready** but should not yet switch default event projection away from localhost.

Current local readiness is stronger than the public cutover state:

- local ontology API is healthy on `127.0.0.1:8787`
- local reverse proxy is healthy on `http://localhost:8080/health`
- public DNS still does not resolve
- repo-safe readiness checks are written by `make tooling-surface-status`

## Role

Stage 1 keeps the domain narrow:

- `syncrescendence.com` serves the ontology API first
- the API is a thin reverse proxy to local FastAPI on `127.0.0.1:8787`
- dashboards or docs are downstream and should not become a second truth surface yet
- `cloudflared` is the preferred cutover path if direct inbound edge routing is not yet in place

## Shape

- local service: `ontology_v1.py serve --host 127.0.0.1 --port 8787`
- reverse proxy: Caddy or equivalent
- public contract:
  - `GET /health`
  - `GET /entities`
  - `GET /entities/{id}`
  - `GET /events`
  - `POST /ingest/event`
  - `POST /project/repo`

## Why This Stage

This preserves the ratified boundary contract:

- repo remains authority
- ontology remains projection
- domain remains typed query surface only

It avoids premature UI drift while still making the ontology reachable.

## Deployment Sequence

1. Start ontology locally with:

```bash
/Users/system/.venvs/syncrescendence-ontology/bin/python /Users/system/syncrescendence/ontology_v1.py serve --host 127.0.0.1 --port 8787
```

2. Put a reverse proxy in front of it using the example Caddyfile in this folder.

Alternative edge path:

- use `cloudflared` with `CLOUDFLARED-ONTOLOGY-STAGE1.md`
- route `syncrescendence.com` and `www.syncrescendence.com` to the local Caddy proxy on `127.0.0.1:8080`

3. Refresh the local readiness artifact:

```bash
make tooling-surface-status
```

4. Confirm:

```bash
curl https://syncrescendence.com/health
```

5. Only after stable health:
   - point selected automation/event projectors at the domain URL instead of localhost
   - use `make reconcile-ajna-events-project-domain`

## Non-Goals For Stage 1

- no dashboard
- no docs site
- no write path outside the existing ingestion contract
- no direct SaaS webhooks bypassing repo/event reconciliation
