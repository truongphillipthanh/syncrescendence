# Cloudflared Ontology Stage 1

**Date**: 2026-03-02  
**Purpose**: Cloudflare Tunnel cutover path for exposing the ontology API without relying on direct inbound networking

## Why This Exists

Direct DNS resolution alone is not enough if the local machine is not yet reachable from the public Internet on `443`.

`cloudflared` gives a narrower Stage 1 path:

- keep the ontology API local on `127.0.0.1:8787`
- keep Caddy local on `http://127.0.0.1:8080`
- let Cloudflare Tunnel carry `syncrescendence.com` traffic to the local proxy

This preserves the current boundary contract:

- repo remains authority
- ontology remains projection
- domain remains typed API surface
- no dashboard or second write path is introduced

## Current Local Prerequisites

These are already true on this machine:

- `cloudflared` is installed
- ontology API is healthy on `127.0.0.1:8787`
- local Caddy proxy is healthy on `http://localhost:8080/health`
- Cloudflare account and zone exist for `syncrescendence.com`

## Remaining External Steps

1. Authenticate `cloudflared` with Cloudflare:

```bash
cloudflared tunnel login
```

This opens a browser authorization flow and creates `~/.cloudflared/cert.pem`.

2. Create a named tunnel:

```bash
cloudflared tunnel create syncrescendence-ontology
```

3. Copy the generated tunnel UUID into:

- `00-ORCHESTRATION/state/impl/cloudflared-ontology.yml.example`

4. Route DNS through the tunnel:

```bash
cloudflared tunnel route dns syncrescendence-ontology syncrescendence.com
cloudflared tunnel route dns syncrescendence-ontology www.syncrescendence.com
```

5. Run the tunnel against the local Caddy proxy:

```bash
cloudflared tunnel --config /Users/system/syncrescendence/00-ORCHESTRATION/state/impl/cloudflared-ontology.yml.example run syncrescendence-ontology
```

6. After `https://syncrescendence.com/health` is healthy, switch selected event projection to the domain path.

## Verification

Local:

```bash
curl http://127.0.0.1:8787/health
curl http://localhost:8080/health
```

Public:

```bash
curl https://syncrescendence.com/health
curl https://www.syncrescendence.com/health
```

Repo-safe status:

```bash
make tooling-surface-status
```

## What This Does Not Solve

- Cloudflare login/approval if interactive auth is still required
- nameserver activation if the zone is not fully active yet
- Zero Trust / Access policy, which is optional and downstream for this API-first stage
