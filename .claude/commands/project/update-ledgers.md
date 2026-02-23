---
name: update-ledgers
description: Safely update CSV ledgers with atomic writes
allowed-tools: Read, Write, Bash(python:*), Bash(cp:*), Bash(mv:*)
---
# Update Ledgers Safely

Update: $ARGUMENTS

## Safety Protocol
1. **Backup**: `cp {ledger}.csv {ledger}.csv.bak.$(date +%Y%m%d%H%M%S)`
2. **Read**: Load current CSV content
3. **Modify**: Apply requested changes
4. **Validate**: Check required columns present, no malformed rows
5. **Write**: Write to temp file `{ledger}.csv.tmp`
6. **Verify**: Confirm temp file valid
7. **Rename**: `mv {ledger}.csv.tmp {ledger}.csv`
8. **Confirm**: Report changes made

## Supported Ledgers
- `orchestration/state/tasks.csv`
- `orchestration/state/projects.csv`
- `orchestration/state/sprints.csv`
- `orchestration/state/burndown.csv`
- `sources/sources.csv`

## Required Columns
- tasks.csv: id, project_id, name, type, status, priority, owner
- projects.csv: id, name, type, status, priority, owner
- sources.csv: id, filename, status, date_processed

## Error Handling
If validation fails:
- Do NOT proceed with rename
- Report specific validation error
- Keep backup intact
