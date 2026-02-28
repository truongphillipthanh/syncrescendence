# Knowledge Graph (local)
Type: system
First seen: Phase 2A
Status: active

## What it is
Local Python script (`orchestration/00-ORCHESTRATION/scripts/knowledge_graph.py`) that ingests the entire repo and builds an in-memory entity-edge graph. Found 1,406 entities and 6,075 edges. Supports stats, query, and search operations.

## Relationships
- script: orchestration/00-ORCHESTRATION/scripts/knowledge_graph.py
- entities: 1,406 (1,055 files, 135 incidents, 86 canon_refs, 68 directives, 22 models, 15 concepts, 9 systems, 7 machines, 6 agents, 3 decisions)
- edges: 6,075 (4,870 mentions, 1,182 references, 16 dispatches_to, 5 runs_on, 2 uses)
- feeds: Entity memory (this directory)

## Current state
Active and operational. The primary tool for understanding repo connectivity. Does NOT persist to disk — rebuilds from repo on each run. Separate from Graphiti (which is the Docker-based graph memory service on Mac mini).
