# REF-REPO_VALIDATION_PROTOCOL

## Purpose

Standardized procedure for validating repository health, structural compliance, and artifact conformance. Produces auditable reports in `agents/commander/outbox/`.

## When to Run

- After any migration or bulk file operation
- Before/after git commits affecting structure
- As part of Blitzkrieg completion verification
- On-demand via `/repo_validate` command

## Validation Checks

### 1. Structural Verification

**Command**: `bash orchestration/scripts/verify_all.sh`

**Checks**:
- `agents/`, `-SOVEREIGN/` exist
- Root contains only zones 00, 01, 02, 04, 05 plus sanctioned exceptions
- No orphan files at root
- README.md paths resolve
- Ledger integrity (DYN-TASKS.csv, DYN-PROJECTS.csv, DYN-SOURCES.csv)
- CANON file count and integration status

**Pass Criteria**: 0 errors (warnings acceptable)

### 2. Operations Lint

**Command**: `bash orchestration/scripts/ops_lint.sh`

**Checks**:
- Prefix naming conventions enforced across engine/
- Cross-reference validation (no broken internal links)

**Pass Criteria**: 0 errors

### 3. Directory Sanity

**Checks**:
- Confirm `agents/`/inbox exists
- Confirm `agents/` exists with per-agent outbox/
- Confirm `OUTGOING/` does NOT exist
- Confirm `outgoing/` does NOT exist
- List `agents/`/inbox contents (should be transient only)

**Pass Criteria**: All existence checks pass

### 4. Git Status Summary

**Command**: `git status --short`

**Purpose**: Document uncommitted changes for audit trail

## Output

Validation produces a report at:
```
agents/commander/outbox/YYYYMMDD-repo_validation/VALIDATION_REPORT.md
```

Report includes:
1. Timestamp and git HEAD
2. Each check with PASS/FAIL and output
3. Warnings summary
4. Next actions if any failures

## Automation

### Via Command

```bash
# From Claude Code
/repo_validate
```

### Manual

```bash
DATE=$(date +%Y%m%d)
mkdir -p "./agents/commander/outbox/${DATE}-repo_validation"

# Run checks
bash orchestration/scripts/verify_all.sh > struct.log 2>&1
bash orchestration/scripts/ops_lint.sh > lint.log 2>&1

# Compile report
# (see command template for full logic)
```

## Remediation Patterns

| Failure | Remediation |
|---------|-------------|
| Missing frontmatter | Add YAML block with id, kind, scope, target |
| Legacy path refs | Update to `agents/<agent>/outbox/` or `agents/<agent>/inbox/` |
| Orphan root files | Move to appropriate zone |
| Missing directories | Create with `mkdir -p` |

## Integration

This protocol is codified as:
- `.claude/commands/project/repo_validate.md` - Claude Code command
- `orchestration/state/REF-REPO_VALIDATION_PROTOCOL.md` - Canonical copy

## See Also

- `orchestration/scripts/verify_all.sh` — Core structural + ledger checks
- `orchestration/scripts/ops_lint.sh` — Operations linter
- `engine/README.md` — Prefix conventions and file counts
