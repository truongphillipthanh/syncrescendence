---
name: blitzkrieg
description: Rapid batch processing of multiple items
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---
# Blitzkrieg Processing Mode

Ultrathink about optimal strategy, then execute rapid processing.

Target: $ARGUMENTS (or all pending if not specified)

## Pre-flight
1. Count pending items in target area
2. Assess complexity distribution
3. Check context capacity (use /compact if >60% full)
4. Verify ledgers unlocked

## Execution Phases

### Phase 1: Triage (5 min max)
- Categorize by type and complexity
- Identify dependencies
- Flag special handling needs

### Phase 2: Parallel Processing
- Simple items first (momentum)
- Group related items (efficiency)
- Use verification between batches

### Phase 3: Ledger Consolidation
- Batch all updates (single atomic operation per ledger)
- Validate cross-references
- Update processing_log

### Phase 4: Verification
- Run /project:verify
- Report success/failure counts
- Stage failures for review

## Constraints
- Maximum 10 items per session
- Stop on critical validation failure
- Document assumptions

## Output
Summary: X/Y processed, Z minutes, follow-ups needed
