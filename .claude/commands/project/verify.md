---
name: verify
description: Run comprehensive verification across the repository
allowed-tools: Bash(make:*), Bash(find:*), Bash(grep:*), Bash(wc:*), Bash(ls:*)
---
# Comprehensive Verification

Run all verification checks for Syncrescendence.

## Execution
```bash
# Structure checks
echo "=== Structure Verification ==="
echo -n "Subdirectories in wrong places: "
find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l

echo -n "Files at root: "
ls *.md 2>/dev/null | wc -l || echo "0"

# Ledger checks
echo ""
echo "=== Ledger Verification ==="
echo -n "tasks.csv rows: "
wc -l < 00-ORCHESTRATION/state/tasks.csv

echo -n "projects.csv rows: "
wc -l < 00-ORCHESTRATION/state/projects.csv

echo -n "sources.csv rows: "
wc -l < 04-SOURCES/sources.csv

# Content checks
echo ""
echo "=== Content Verification ==="
echo -n "Processed sources: "
ls 04-SOURCES/processed/*.md 2>/dev/null | wc -l || echo "0"

echo -n "CANON integrations: "
grep -l "SOURCE-" 01-CANON/*.md 2>/dev/null | wc -l || echo "0"

# Git status
echo ""
echo "=== Git Status ==="
git status --short

echo ""
echo "=== Verification Complete ==="
```

## Output
Report showing pass/fail for each category.
