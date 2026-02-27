# Graphiti
Type: system
First seen: Phase 1 (memory pipeline)
Status: active (buggy)

## What it is
Graph memory service (v0.22.0 by Zep AI) running in Docker on Mac mini. Provides episodic and semantic memory via Neo4j backend. Reachable from MBA at `http://M1-Mac-mini.local:8001`.

## Relationships
- depends_on: Neo4j 5.26.0
- runs_on: Mac mini (Docker)
- feeds: Memory pipeline (Phase 4 target)
- bug: Do NOT pass `uuid` in `/messages` payload — causes NodeNotFoundError crash

## Current state
Running but has known bugs. Background worker crash kills ALL queue processing — must `docker restart graphiti` to recover. `/clear` + restart needed to wipe stale queue. Endpoint is unsecured (security gap identified in Council 25). Phase 4 target for full integration (Graphiti /triples, backfill, query tools).
