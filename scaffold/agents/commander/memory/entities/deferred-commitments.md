# Deferred Commitments
Type: file
First seen: Phase 1
Status: active

## What it is
The phased plan of all open, deferred, and completed commitments. Located at `orchestration/state/DYN-DEFERRED_COMMITMENTS.md`. Must be checked at directive initialization (Protocol A.1b).

## Relationships
- referenced_by: 10+ edges in knowledge graph
- checked_by: Commander at every session start
- contains: DC-* directive commitments organized by phase
- references: scaffold_validate.sh, Neo4j, memsync
- location: orchestration/state/DYN-DEFERRED_COMMITMENTS.md

## Current state
Active. Contains the full execution critical path from Phase 0 through Phase 5. Phase 2 substantially complete. DC-114/115 (memsync hardening) remain P1. DC-147/148/150 builds are P1, parallel with Phase 3.
