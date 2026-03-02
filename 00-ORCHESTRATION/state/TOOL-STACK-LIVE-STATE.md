# Tool Stack Live State

**Date**: 2026-03-02  
**Purpose**: factual live runtime snapshot for repo↔harness reconciliation  
**Status**: ACTIVE reference for current tool-stack truth

---

## Live Runtime Facts

- `syncrescendence.com` is secured
- OpenClaw gateway is live on the MacBook Air at `127.0.0.1:18789`
- Ajna's current primary model in live OpenClaw config is `anthropic/claude-sonnet-4-5`
- OpenClaw workspace path is `/Users/system/.openclaw/workspace`
- Browser is not denied in OpenClaw
- Ajna has `playwright-mcp` skill installed
- Slack channel is currently disabled
- Discord channel is currently disabled
- `exec`, `process`, and `apply_patch` remain denied in OpenClaw

## Current Truth Split

- Repo constitutional/orientation docs were written during pre-rewire state and some still narrate Ajna as Kimi-primary
- Live OpenClaw runtime has already moved Ajna onto Claude Sonnet
- Config scaffold upgrade has been designed but not yet implemented
- Memory remains split across repo memory, OpenClaw workspace memory, and session logs

## Immediate Blockers

1. Repo truth still needs reconciliation to live Ajna/OpenClaw truth
2. Rendered + validated config pipeline is not implemented yet
3. Repo↔OpenClaw reconciliation loop does not exist yet
4. Memory synthesis loop does not exist yet
5. `gcloud` still needs one-time browser OAuth
6. `wrangler` still needs one-time browser OAuth

## Authority

- Strategic architecture: `engine/CC65-TOOL-STACK-FINAL.md`
- Current narrowing brief: `engine/CC72b-IMPLEMENTATION-BRIEF.md`
- This file is the factual runtime snapshot, not the long-term architecture
