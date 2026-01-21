# DIRECTIVE: DIR-YYYYMMDD-NAME

## Preamble
```bash
# Run immediately upon receiving this directive:
make log-init DIRECTIVE=NAME
```

## Context
[Why this directive exists—link to Oracle decision or preceding work]

## Objective
[What success looks like]

## Constraints
[Hard boundaries that must not be violated]

## Deliverables
- [ ] Item 1
- [ ] Item 2

## Verification
```bash
# Commands to prove completion
```

## Postamble
```bash
# Run after all deliverables complete:
make log STATUS=COMPLETE DIRECTIVE=NAME
git add 00-ORCHESTRATION/execution_logs/
git commit -m "log(DIR-YYYYMMDD-NAME): [summary]"
```

Append execution evidence to log file before committing.
