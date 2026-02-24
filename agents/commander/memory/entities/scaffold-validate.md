# scaffold_validate.sh
Type: file
First seen: Post INT-2210 (2026-02-22)
Status: active

## What it is
Structural validation script that verifies the repo scaffold integrity. Created as a direct response to the INT-2210 disaster where Commander demolished architecture without validation. Located at `orchestration/00-ORCHESTRATION/scripts/scaffold_validate.sh`.

## Relationships
- required_by: Phase Gate Rule (Constitutional Rule 4)
- referenced_by: 12 edges in knowledge graph (AGENTS.md, CLAUDE.md, canon rationale, deferred commitments, naming conventions)
- prevents: Structural changes without validation
- created_because: INT-2210 catastrophe

## Current state
Active and operational. Must pass before any structural changes (renames, dissolutions, reorganizations). Part of the phase gate triad: scaffold_validate passing + memory operational + rollback tested.
