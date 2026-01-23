# ORCHESTRATION Index

## Purpose
Living infrastructure for system coordination. Contains directives, execution logs, state ledgers, and operational scripts.

## Directory Structure

### /directives/
Active and historical directives.
- **Current**: DIRECTIVE-041 through DIRECTIVE-046
- **Historical**: DIRECTIVE-018 through DIRECTIVE-040 (completed)

Directives use suffixes for parallel execution:
- A/B/C = Parallel lanes
- Oracle numbers (O9, O11, etc.) = Oracle session assignments

### /execution_logs/
Timestamped logs of directive execution.

Format: `EXECUTION_LOG-YYYY-MM-DD-NNNX.md`

Where:
- YYYY-MM-DD = Execution date
- NNN = Directive number
- X = Lane suffix (A/B/C) if applicable

### /state/
Dynamic ledgers and reference documents.

**Prefix conventions**:
- `DYN-*` = Dynamic (changes frequently, updated by automation)
- `REF-*` = Reference (stable, rarely changes, constitutional)
- `ARCH-*` = Archaeological (frozen historical record, read-only)
- `SCAFF-*` = Scaffolding (temporary, to be integrated or deleted)

**Key files**:
- `DYN-TASKS.csv` — Active task ledger (ground truth)
- `DYN-PROJECTS.csv` — Project tracking
- `DYN-TREE.md` — Current directory tree
- `DYN-DASHBOARD.md` — System status dashboard
- `REF-STANDARDS.md` — The 18 evaluative lenses
- `REF-PROCESSING_PATTERN.md` — Source processing workflow
- `REF-OPERATIONAL_TOPOLOGY.md` — Multi-Claude coordination map

### /scripts/
Automation and utility scripts.

### /automation/
Hazel rules and Keyboard Maestro macros (specifications).

## Quick Start

1. **Check active work**: See `/directives/DIRECTIVE-046*.md`
2. **Check system state**: See `/state/DYN-DASHBOARD.md`
3. **Check task backlog**: See `/state/DYN-TASKS.csv`
4. **Check processing pattern**: See `/state/REF-PROCESSING_PATTERN.md`

## Protected Status

The `/state/` directory is PROTECTED. Deletions require Principal approval.
Dynamic files (DYN-*) can be modified by automation.
Reference files (REF-*) require explicit approval to modify.
