# memsync
Type: concept
First seen: Phase 1 (memory pipeline)
Status: stale

## What it is
The memory synchronization daemon concept — intended to sync agent memory state across the constellation. Referenced as `memsync_daemon.py` in MEMORY.md but the file does NOT exist at the documented path (`orchestration/00-ORCHESTRATION/scripts/memsync_daemon.py`).

## Relationships
- referenced_by: 12 files (CLAUDE.md, AGENTS.md, intention compass, memory architecture, deferred commitments, multiple prompts)
- conceptual_part_of: Memory pipeline (Phase 1)
- missing_implementation: `memsync_daemon.py` not found

## Current state
BROKEN. The daemon file does not exist despite being documented in MEMORY.md and CLAUDE.md. The concept is referenced in 12 files across the knowledge graph but has no running implementation. This is a known gap — memory pipeline Phase 1 was declared COMPLETE but memsync hardening (DC-114/115) remains P1.
