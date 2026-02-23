# PRAC: Blitzkrieg Worktree Isolation

**Scope**: Git worktree parallelization for multi-agent Blitzkrieg execution
**Linear**: SYN-9 / IMPL-A-0005
**Status**: CANONICAL

---

## The Pattern

Git worktrees give each agent a separate working tree sharing the same `.git` history. No file locks, no race conditions, no coordination overhead.

```
TERM WorktreeBlitzkrieg:
sutra: "One worktree per lane, one agent per worktree—parallel without collision"
gloss: Blitzkrieg dispatches N agents simultaneously. Without isolation, they
       race on the same files. Worktrees eliminate this by giving each agent
       its own filesystem checkout from the same repository.
end
```

---

## Lane-to-Worktree Binding

| Lane | Agent | Role | Worktree | Branch |
|------|-------|------|----------|--------|
| A | Commander | COO | `syncrescendence-alpha` | `alpha/work` |
| B | Adjudicator | CQO | `syncrescendence-beta` | `beta/work` |
| C | Cartographer | CIO | `syncrescendence-gamma` | `gamma/work` |
| D | Psyche | CTO | `syncrescendence-delta` | `delta/work` |

Ajna (CSO) operates from MBA via git sync — not a local worktree.

---

## Zone Ownership

Each lane owns specific file domains to prevent merge conflicts:

| Lane | Primary Zone | Shared (read-only) |
|------|-------------|-------------------|
| A (Commander) | `orchestration/`, `CLAUDE.md`, ledgers | `canon/` (read) |
| B (Adjudicator) | `engine/` (quality), test scripts | `canon/` (read) |
| C (Cartographer) | `sources/research/`, `praxis/` | `canon/` (read) |
| D (Psyche) | `engine/` (automation), `.openclaw/` | `canon/` (read) |

**Rule**: `canon/` is write-protected during Blitzkrieg. Only the Commander (or Sovereign) merges CANON changes post-Blitzkrieg.

---

## Setup

### Prerequisites
- Git 2.30+ (worktree support)
- All agents have Claude Code / CLI access
- Current branch is clean (`git stash` if needed)

### Quick Start

```bash
# From repo root
bash orchestration/00-ORCHESTRATION/scripts/setup-worktrees.sh
```

This creates 3 worktrees (alpha/beta/gamma) alongside the main checkout. For 4-lane Blitzkrieg, add delta manually:

```bash
PARENT=$(dirname "$(git rev-parse --show-toplevel)")
git worktree add "$PARENT/syncrescendence-delta" -b delta/work
```

### Verify

```bash
git worktree list
# /Users/home/Desktop/syncrescendence               abc1234 [main]
# /Users/home/Desktop/syncrescendence-alpha          def5678 [alpha/work]
# /Users/home/Desktop/syncrescendence-beta           ghi9012 [beta/work]
# /Users/home/Desktop/syncrescendence-gamma          jkl3456 [gamma/work]
# /Users/home/Desktop/syncrescendence-delta          mno7890 [delta/work]
```

---

## Execution Workflow

### 1. Dispatch Phase
Sovereign assigns directives to lanes via dispatch.sh or direct instruction.

### 2. Parallel Execution
Each agent works in its worktree independently:
```bash
# Lane A (Commander)
cd ~/Desktop/syncrescendence-alpha
claude -p "Execute directive: ..."

# Lane B (Adjudicator)
cd ~/Desktop/syncrescendence-beta
codex exec "Execute directive: ..."
```

Or via cockpit tmux panes (each pane cds to its worktree).

### 3. Merge Phase
After all lanes complete:
```bash
# Commander merges from main worktree
cd ~/Desktop/syncrescendence
git merge alpha/work --no-ff -m "blitz: merge lane A — [summary]"
git merge beta/work --no-ff -m "blitz: merge lane B — [summary]"
git merge gamma/work --no-ff -m "blitz: merge lane C — [summary]"
git merge delta/work --no-ff -m "blitz: merge lane D — [summary]"
```

Resolve conflicts zone-by-zone. Zone ownership minimizes conflicts.

### 4. Cleanup
```bash
# Remove worktrees after merge
git worktree remove ../syncrescendence-alpha
git worktree remove ../syncrescendence-beta
git worktree remove ../syncrescendence-gamma
git worktree remove ../syncrescendence-delta

# Delete branches
git branch -d alpha/work beta/work gamma/work delta/work
```

---

## When to Use Worktrees vs Single-Tree

| Scenario | Approach |
|----------|----------|
| 2+ agents modifying different files simultaneously | Worktrees |
| Sequential agent handoff (one at a time) | Single tree + dispatch |
| Research-only agents (read, no write) | Single tree (read-safe) |
| Large refactoring across many files | Worktrees (isolation critical) |
| Quick fire-and-forget task | Single tree (overhead not worth it) |

---

## Anti-Patterns

1. **Two agents writing the same file in different worktrees** — zone ownership prevents this. If unavoidable, designate a merge resolver.
2. **Long-lived worktree branches** — merge frequently (every Blitzkrieg, not weekly). Divergence = merge pain.
3. **Worktrees without zone ownership** — random parallelism creates random conflicts. Always define zones first.
4. **Forgetting to cleanup** — orphan worktrees consume disk and create confusion. Always remove after merge.

---

## Integration with Neo-Blitzkrieg

This pattern is Phase 3 of the Neo-Blitzkrieg execution model:
1. **Phase 1**: Directive decomposition (Sovereign)
2. **Phase 2**: Lane assignment (dispatch.sh)
3. **Phase 3**: Worktree isolation (this pattern)
4. **Phase 4**: Parallel execution
5. **Phase 5**: Merge + verification

---

## Coordination Schema (coordination.yaml)

Define zone ownership formally for automated enforcement:

```yaml
zones:
  alpha:
    files:
      include: ["src/auth/**", "ledgers/*-alpha.csv"]
    ledger: "ledgers/tasks-alpha.csv"
    agent: "Commander"

  beta:
    files:
      include: ["src/api/**", "ledgers/*-beta.csv"]
    ledger: "ledgers/tasks-beta.csv"
    agent: "Adjudicator"

  gamma:
    files:
      include: ["tests/**", "ledgers/*-gamma.csv"]
    ledger: "ledgers/tasks-gamma.csv"
    agent: "Cartographer"

  delta:
    files:
      include: ["docs/**", "ledgers/*-delta.csv"]
    ledger: "ledgers/tasks-delta.csv"
    agent: "Psyche"
```

### CODEOWNERS Enforcement

```
# .github/CODEOWNERS
src/auth/**     @team-alpha
src/api/**      @team-beta
tests/**        @team-gamma
docs/**         @team-delta
```

### Zone Verification Script

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
head -1 ledgers/tasks-alpha.csv > ledgers/tasks-main.csv
for zone in alpha beta gamma delta; do
  tail -n +2 ledgers/tasks-$zone.csv >> ledgers/tasks-main.csv
done
```

---

## Teleport: Local to Cloud

### Send to Cloud
```bash
# Prefix with & to send to web
& Analyze this codebase for performance bottlenecks
```
Creates background session on claude.ai/code that runs autonomously.

### Retrieve from Cloud
```bash
claude --teleport
```

### Distributed Pattern
```
Local Machine                    Cloud (claude.ai/code)
─────────────────────────────────────────────────────────
Agent 1 (backend)                Agent 6 (long analysis)
Agent 2 (frontend)               Agent 7 (batch processing)
Agent 3 (tests)                  Agent 8 (research)
Agent 4 (docs)
Agent 5 (orchestrator)
```

---

## File-Based Coordination (Oracle Pattern)

```
project/
├── tasks/
│   ├── task-001-auth.md        # Oracle creates
│   ├── task-002-api.md         # Oracle creates
│   └── task-003-tests.md       # Oracle creates
├── results/
│   ├── task-001-result.md      # Worker writes
│   └── task-002-result.md      # Worker writes
└── master_plan.md              # Oracle maintains
```

Workflow: Oracle (Opus) writes task specs → Workers (Sonnet) execute → Oracle reads results, updates plan. File system is the coordination bus — no complex networking.

---

## Resource Management

### Context Window per Agent
Each agent has independent 200K context — parallel agents multiply total capacity.

### API Rate Limits
Multiple instances may hit rate limits. Stagger launches or use multiple accounts.

### Cost Control
```bash
# Use cheaper models for routine work
claude --model sonnet --session routine-tasks
# Reserve expensive models for complex work
claude --model opus --session architecture-decisions
```

---

## Practical Limits

| Agents | Effectiveness |
|--------|---------------|
| 1-3 | Easy to manage, low overhead |
| 3-7 | **Optimal** — good parallelism, manageable coordination |
| 7-10 | Increasing overhead, human attention bottleneck |
| 10+ | Coordination costs exceed benefits |

**Bottleneck shifts**: From AI speed to human attention to integrate outputs.

---

## Worktree Management Commands

```bash
git worktree list              # List all worktrees
git worktree remove ../path    # Remove worktree
git worktree prune             # Prune stale entries
git worktree move ../old ../new  # Move worktree
```

---

## Named Sessions Integration

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

## Checklist: Starting Parallel Session

1. [ ] Create git worktrees for isolation
2. [ ] Define zone ownership (which agent edits what)
3. [ ] Start named sessions for each workstream
4. [ ] Set up file-based coordination (tasks/, results/)
5. [ ] Consider teleporting long tasks to cloud
6. [ ] Establish merge points and cadence

---

## Cross-References

- `orchestration/00-ORCHESTRATION/scripts/setup-worktrees.sh` — Setup script (70 lines)
- `engine/REF-ROSETTA_STONE.md` — Gap Analysis G5

---

## Consolidated From

- `praxis/05-SIGMA/mechanics/MECH-git_worktree_coordination.md` — Coordination schema, CODEOWNERS, zone verification script, zone-specific ledgers, worktree management commands, named sessions integration
- `praxis/05-SIGMA/practice/PRAC-parallel_claude_orchestration.md` — Teleport pattern, file-based Oracle coordination, resource management, practical limits, parallel session checklist
