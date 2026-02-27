# Dispatch System (auto_ingest)
Type: system
First seen: 2026-02-17 (replaced watch_dispatch.sh)
Status: active

## What it is
The sole task dispatch system. `auto_ingest_loop.sh` polls agent inboxes every 30s. `dispatch.sh` creates TASK-*.md files and handles cross-machine SCP delivery. watch_dispatch.sh is DEPRECATED (caused race conditions).

## Relationships
- script: orchestration/00-ORCHESTRATION/scripts/dispatch.sh
- loop: orchestration/00-ORCHESTRATION/scripts/auto_ingest_loop.sh (per-agent)
- replaces: watch_dispatch.sh (deprecated 2026-02-17)
- uses: Neural Bridge for cross-machine SCP
- env_vars: SYNCRESCENDENCE_REMOTE_AGENT_HOST_<AGENT>

## Current state
Active. The canonical way to dispatch tasks. Task lifecycle: dispatch.sh creates pending -> auto_ingest moves to active -> agent executes -> result to outbox -> done/failed -> CONFIRM sent back. NEVER re-enable watch_dispatch.sh.
