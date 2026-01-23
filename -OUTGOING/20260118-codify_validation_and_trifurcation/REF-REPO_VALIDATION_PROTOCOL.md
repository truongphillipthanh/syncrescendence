---
id: repo-validation-protocol
kind: protocol
scope: repo
target: repo
owner: Deviser
version: 1.0.0
---

# REF-REPO_VALIDATION_PROTOCOL

## Purpose

Standardized procedure for validating repository health, structural compliance, and artifact conformance. Produces auditable reports in `-OUTGOING/`.

## When to Run

- After any migration or bulk file operation
- Before/after git commits affecting structure
- As part of Blitzkrieg completion verification
- On-demand via `/repo_validate` command

## Validation Checks

### 1. Structural Verification

**Command**: `bash 00-ORCHESTRATION/scripts/structural_verify.sh`

**Checks**:
- `-INBOX/` and `-OUTGOING/` exist (not `OUTGOING/` or `outgoing/`)
- Root contains only zones 00-06 plus sanctioned exceptions
- No orphan files at root
- COCKPIT.md paths resolve
- No stale legacy path references
- Blitzkrieg infrastructure present
- Packet schema complete

**Pass Criteria**: 0 errors (warnings acceptable)

### 2. Operations Lint

**Command**: `bash 02-ENGINE/scripts/ops_lint.sh`

**Checks**:
- All `PROMPT-*.md` files have YAML frontmatter
- All `REF-*.md` files have YAML frontmatter
- Required keys present: `id`, `kind`, `scope`, `target`

**Pass Criteria**: 0 errors

### 3. Directory Sanity

**Checks**:
- Confirm `-INBOX/` exists
- Confirm `-OUTGOING/` exists
- Confirm `OUTGOING/` does NOT exist
- Confirm `outgoing/` does NOT exist
- List `-INBOX/` contents (should be transient only)

**Pass Criteria**: All existence checks pass

### 4. Git Status Summary

**Command**: `git status --short`

**Purpose**: Document uncommitted changes for audit trail

## Output

Validation produces a report at:
```
-OUTGOING/YYYYMMDD-repo_validation/VALIDATION_REPORT.md
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
mkdir -p "./-OUTGOING/${DATE}-repo_validation"

# Run checks
bash 00-ORCHESTRATION/scripts/structural_verify.sh > struct.log 2>&1
bash 02-ENGINE/scripts/ops_lint.sh > lint.log 2>&1

# Compile report
# (see command template for full logic)
```

## Remediation Patterns

| Failure | Remediation |
|---------|-------------|
| Missing frontmatter | Add YAML block with id, kind, scope, target |
| Legacy path refs | Update to `-OUTGOING/` or `-INBOX/` |
| Orphan root files | Move to appropriate zone |
| Missing directories | Create with `mkdir -p` |

## Integration

This protocol is codified as:
- `.claude/commands/project/repo_validate.md` - Claude Code command
- `00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md` - Canonical copy

## See Also

- `structural_verify.sh` - Core structural checks
- `ops_lint.sh` - Frontmatter linter
- `REF-OPERATIONS_ARTIFACT_TAXONOMY.md` - Naming and frontmatter requirements
