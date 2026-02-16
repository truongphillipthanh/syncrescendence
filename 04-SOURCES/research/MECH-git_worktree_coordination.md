# MECH: Git Worktree Coordination

**Scope**: Worktree creation, zone isolation, conflict prevention, multi-agent patterns

---

## Core Concept

```
TERM WorktreeIsolation:
sutra: "Same .git history, independent working trees—parallel agents without race conditions"
gloss: Git worktrees create separate directory checkouts sharing the same repository
       history. Each worktree has completely independent file state. Multiple
       Claude instances can work on same codebase without file locks, conflicts,
       or race conditions. The gold standard for multi-agent coordination.
spec:
    type: MECHANISM
    isolation: "Independent file states per worktree"
    sharing: "Common .git history, refs, config"
    benefit: "No race conditions, no file locks"
    pattern: "One worktree per zone, one agent per worktree"
end
```

---

## Setup

### Create Worktrees

```bash
# Create isolated checkouts for parallel zones
git worktree add ../project-alpha -b zone/alpha main
git worktree add ../project-beta -b zone/beta main
git worktree add ../project-gamma -b zone/gamma main
git worktree add ../project-delta -b zone/delta main
```

This creates four separate directories:
```
parent/
├── project/           # Original (main branch)
├── project-alpha/     # zone/alpha branch
├── project-beta/      # zone/beta branch
├── project-gamma/     # zone/gamma branch
└── project-delta/     # zone/delta branch
```

### Launch Agents

```bash
# Terminal 1
cd ../project-alpha && claude --session alpha-feature

# Terminal 2
cd ../project-beta && claude --session beta-feature

# Terminal 3
cd ../project-gamma && claude --session gamma-feature
```

Or via tmux:
```bash
tmux new-session -s agents
tmux split-window -h
tmux split-window -v
# Each pane: cd to worktree, run claude
```

---

## Zone Ownership

### coordination.yaml

```yaml
zones:
  alpha:
    files:
      include: ["src/auth/**", "ledgers/*-alpha.csv"]
    ledger: "ledgers/tasks-alpha.csv"
    agent: "Account 1"

  beta:
    files:
      include: ["src/api/**", "ledgers/*-beta.csv"]
    ledger: "ledgers/tasks-beta.csv"
    agent: "Account 2"

  gamma:
    files:
      include: ["tests/**", "ledgers/*-gamma.csv"]
    ledger: "ledgers/tasks-gamma.csv"
    agent: "Account 3"

  delta:
    files:
      include: ["docs/**", "ledgers/*-delta.csv"]
    ledger: "ledgers/tasks-delta.csv"
    agent: "Gemini"
```

### CODEOWNERS Enforcement

```
# .github/CODEOWNERS
src/auth/**     @team-alpha
src/api/**      @team-beta
tests/**        @team-gamma
docs/**         @team-delta
```

### Verification Script

```bash
#!/bin/bash
# verify-zone.sh - Run in pre-commit hook
ZONE=$(git config --local zone.name)
FILES=$(git diff --cached --name-only)

for file in $FILES; do
  if ! echo "$file" | grep -q "^$(cat coordination.yaml | yq ".zones.$ZONE.files.include[]")" ; then
    echo "ERROR: $file not in zone $ZONE"
    exit 1
  fi
done
```

---

## Merge Strategy

```
NORM MergeStrategy:
sutra: "Long isolated branches, infrequent merges—AI agents bad at conflict resolution"
spec:
    frequency: "At natural breakpoints (feature complete, phase done)"
    avoid: "Continuous integration style frequent merges"
    rationale: "Merge conflicts require human judgment"
    pattern:
        1: "Agent completes feature in worktree"
        2: "Human reviews"
        3: "Human merges to main"
        4: "Other worktrees rebase if needed"
end
```

### Merge Workflow

```bash
# After zone/alpha feature complete
git checkout main
git merge --no-ff zone/alpha -m "feat(auth): complete OAuth implementation"

# Other worktrees update
cd ../project-beta
git fetch origin
git rebase origin/main
```

---

## Zone-Specific Ledgers

Instead of all agents writing to shared CSV:

```
ledgers/
├── tasks-alpha.csv    # Alpha zone only
├── tasks-beta.csv     # Beta zone only
├── tasks-gamma.csv    # Gamma zone only
├── tasks-delta.csv    # Delta zone only
└── tasks-main.csv     # Consolidated view (generated)
```

### Consolidation Script

```bash
#!/bin/bash
# consolidate-ledgers.sh

# Header
head -1 ledgers/tasks-alpha.csv > ledgers/tasks-main.csv

# Append all zone data
for zone in alpha beta gamma delta; do
  tail -n +2 ledgers/tasks-$zone.csv >> ledgers/tasks-main.csv
done
```

Run after zone work completes, before merge.

---

## Worktree Management

### List Worktrees
```bash
git worktree list
```

### Remove Worktree
```bash
git worktree remove ../project-alpha
```

### Prune Stale
```bash
git worktree prune
```

### Move Worktree
```bash
git worktree move ../project-alpha ../new-location
```

---

## Integration with Named Sessions

```bash
# Create worktree with corresponding session
git worktree add ../project-feature-x -b feature/x main
cd ../project-feature-x
claude --session feature-x-implementation

# Resume later
cd ../project-feature-x
claude --resume feature-x-implementation
```

---

## Typical Workflow

```
PROC WorktreeWorkflow:
    1: "Create worktrees for planned zones"

    2: "Define zone boundaries in coordination.yaml"

    3: "Launch Claude instances in separate terminals/tmux"

    4: "Agents work independently on assigned zones"

    5: "Zone-specific ledgers prevent CSV conflicts"

    6: "At sync points:"
        - Human reviews completed zones
        - Human merges to main
        - Other worktrees rebase if needed

    7: "Consolidate ledgers after merge"

    8: "Continue or prune completed worktrees"
end
```

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Single directory, multiple agents | Race conditions, conflicts | Use worktrees |
| Shared CSV across zones | Write conflicts | Zone-specific ledgers |
| Frequent merges | Conflict resolution overhead | Infrequent at breakpoints |
| No zone boundaries | Overlapping edits | coordination.yaml + CODEOWNERS |

---

## Cross-References

- [[SYNTHESIS-cross_platform_patterns]] → Architecture diagram with worktrees
- [[PRAC-parallel_claude_orchestration]] → Multi-instance management
- [[PRAC-ledger_management_patterns]] → CSV consolidation details
