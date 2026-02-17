# PRAC: Ledger Management Patterns

**Scope**: Zone-specific CSVs, consolidation, conflict prevention, ground truth

---

## The Problem

Multiple agents writing to shared `tasks.csv` creates:
- Write conflicts (simultaneous edits)
- Race conditions (overwrites)
- Merge hell (conflicting changes)

**Solution**: Zone-specific ledgers with automated consolidation.

---

## Zone-Specific Pattern

```
ledgers/
├── tasks-alpha.csv    # Alpha zone only
├── tasks-beta.csv     # Beta zone only
├── tasks-gamma.csv    # Gamma zone only
├── tasks-delta.csv    # Delta zone only
└── tasks-main.csv     # Consolidated (generated, not edited)
```

Each agent writes only to their zone's CSV. No conflicts possible.

---

## CSV Structure

```csv
id,zone,status,priority,description,assigned,created,updated
ALPHA-001,alpha,in_progress,high,"Implement OAuth flow",Account1,2026-01-25,2026-01-25
ALPHA-002,alpha,pending,medium,"Add refresh token handling",Account1,2026-01-25,2026-01-25
```

**Required fields**:
- `id`: Zone-prefixed unique identifier
- `zone`: Owning zone (matches filename)
- `status`: pending, in_progress, completed, blocked
- `priority`: high, medium, low

---

## coordination.yaml Integration

```yaml
zones:
  alpha:
    ledger: "ledgers/tasks-alpha.csv"
    id_prefix: "ALPHA"
    owner: "Account1"

  beta:
    ledger: "ledgers/tasks-beta.csv"
    id_prefix: "BETA"
    owner: "Account2"
```

Agents check their zone's configuration before any ledger write.

---

## Consolidation Script

```bash
#!/bin/bash
# consolidate-ledgers.sh

OUTPUT="ledgers/tasks-main.csv"
TEMP="ledgers/.tasks-main-temp.csv"

# Header from first file
head -1 ledgers/tasks-alpha.csv > "$TEMP"

# Append data from all zones (skip headers)
for zone in alpha beta gamma delta; do
  if [[ -f "ledgers/tasks-$zone.csv" ]]; then
    tail -n +2 "ledgers/tasks-$zone.csv" >> "$TEMP"
  fi
done

# Atomic replacement
mv "$TEMP" "$OUTPUT"

echo "Consolidated $(wc -l < "$OUTPUT") entries to $OUTPUT"
```

**Run**: After zone work completes, before merge to main.

---

## Atomic Update Pattern

Never edit CSV in place:

```bash
# Wrong
echo "new,row" >> ledgers/tasks-alpha.csv

# Right
TEMP=$(mktemp)
cat ledgers/tasks-alpha.csv > "$TEMP"
echo "new,row" >> "$TEMP"
# Validate TEMP has correct structure
mv "$TEMP" ledgers/tasks-alpha.csv
```

---

## Validation Before Write

```bash
#!/bin/bash
# validate-ledger.sh

FILE="$1"

# Check header
if ! head -1 "$FILE" | grep -q "id,zone,status"; then
  echo "ERROR: Invalid header in $FILE"
  exit 1
fi

# Check for duplicate IDs
DUPS=$(cut -d, -f1 "$FILE" | sort | uniq -d)
if [[ -n "$DUPS" ]]; then
  echo "ERROR: Duplicate IDs: $DUPS"
  exit 1
fi

echo "Ledger valid: $FILE"
```

---

## Git Integration

```bash
# Pre-commit hook
#!/bin/bash

# Validate all changed ledgers
for file in $(git diff --cached --name-only | grep "ledgers/tasks-.*\.csv"); do
  ./scripts/validate-ledger.sh "$file" || exit 1
done

# Regenerate consolidated view
./scripts/consolidate-ledgers.sh
git add ledgers/tasks-main.csv
```

---

## Reading Across Zones

Agents needing full view read consolidated file:

```markdown
# In CLAUDE.md

To see all tasks: Read ledgers/tasks-main.csv
To update YOUR zone's tasks: Write to ledgers/tasks-{zone}.csv
NEVER write to tasks-main.csv (generated file)
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Writing to tasks-main.csv | Overwritten on consolidation | Write to zone CSV only |
| No ID prefix | Collisions between zones | Use zone-prefixed IDs |
| Non-atomic updates | Corruption on crash | Temp file + move |
| No validation | Invalid data accumulates | Pre-commit validation |

---

## Cross-References

- [[MECH-git_worktree_coordination]] → Zone ownership setup
- [[SYNTHESIS-cross_platform_patterns]] → Multi-agent architecture
- [[PRAC-oracle_to_executor_handoff]] → State tracking
