# /repo_validate

Run repository validation checks and produce an auditable report.

## Behavior

1. Create output directory: `-OUTGOING/YYYYMMDD-repo_validation/`
2. Capture git HEAD and status
3. Run structural verification: `bash orchestration/scripts/verify_all.sh`
4. Run operations lint: `bash orchestration/scripts/ops_lint.sh`
5. Verify directory sanity (exchange dirs exist, legacy dirs absent)
6. Compile results into `VALIDATION_REPORT.md`

## Output

Creates: `-OUTGOING/YYYYMMDD-repo_validation/VALIDATION_REPORT.md`

Report includes:
- Timestamp and git HEAD
- Git status summary
- Structural verification: PASS/FAIL + warnings
- Operations lint: PASS/FAIL + failing files
- Directory sanity checks
- Next actions if failures detected

## Implementation

```bash
# Get date and create output directory
DATE=$(date +%Y%m%d)
mkdir -p "./-OUTGOING/${DATE}-repo_validation"

# Capture git state
GIT_HEAD=$(git rev-parse HEAD)
GIT_STATUS=$(git status --short)

# Run structural verification
STRUCT_OUTPUT=$(bash orchestration/scripts/verify_all.sh 2>&1)
STRUCT_EXIT=$?

# Run ops lint
LINT_OUTPUT=$(bash orchestration/scripts/ops_lint.sh 2>&1)
LINT_EXIT=$?

# Check directory sanity
INBOX_EXISTS=$([[ -d "./-INBOX" ]] && echo "YES" || echo "NO")
OUTGOING_EXISTS=$([[ -d "./-OUTGOING" ]] && echo "YES" || echo "NO")
LEGACY_OUTGOING=$([[ -d "OUTGOING" ]] && echo "EXISTS (BAD)" || echo "NO (correct)")
LEGACY_LOWER=$([[ -d "outgoing" ]] && echo "EXISTS (BAD)" || echo "NO (correct)")
INBOX_CONTENTS=$(find ./-INBOX -maxdepth 2 -print 2>/dev/null)

# Determine overall status
STRUCT_STATUS=$([[ $STRUCT_EXIT -eq 0 ]] && echo "PASS" || echo "FAIL")
LINT_STATUS=$([[ $LINT_EXIT -eq 0 ]] && echo "PASS" || echo "FAIL")
```

Write compiled report to `-OUTGOING/${DATE}-repo_validation/VALIDATION_REPORT.md`.

## Pass Criteria

- Structural verification: 0 errors (warnings OK)
- Operations lint: 0 errors
- Directory sanity: All checks pass

## Usage

Invoke with:
```
/repo_validate
```

Or run the validation commands manually and compile the report.
