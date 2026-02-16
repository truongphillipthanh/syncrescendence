# PRAC: Parallel Claude Orchestration

**Scope**: Multi-instance patterns, git worktrees, teleport, named sessions

---

## The Pattern

```
PROC ParallelOrchestration:
sutra: "Multiple Claude instances on same repo—worktrees isolate, teleport bridges, files coordinate"
gloss: Running 5-10+ Claude instances in parallel multiplies throughput. Key enablers:
       git worktrees prevent file conflicts, named sessions enable resumption,
       teleport moves work between local and cloud.
spec:
    type: PRACTICE
    scale: "3-7 concurrent workers optimal; beyond 10 coordination overhead dominates"
    isolation: "Git worktrees or separate directories"
    coordination: "File-based handoffs, not message passing"
end
```

---

## Setup: Git Worktrees

```bash
# Create isolated checkouts for parallel agents
git worktree add ../agent-backend feature/backend-refactor
git worktree add ../agent-frontend feature/frontend-redesign
git worktree add ../agent-docs feature/documentation

# Each agent launched in its worktree
cd ../agent-backend && claude --session backend-refactor
cd ../agent-frontend && claude --session frontend-redesign
```

**Benefits**:
- Same .git history, separate working trees
- No file locks or race conditions
- Independent branches, clean merges

---

## Zone Ownership

Assign agents to orthogonal zones to prevent conflicts:

| Agent | Zone | Files |
|-------|------|-------|
| Backend Agent | Backend | `src/backend/**` |
| Frontend Agent | Frontend | `src/frontend/**` |
| Docs Agent | Documentation | `docs/**` |
| Test Agent | Testing | `tests/**` |

**Rule**: Agents should not edit same files simultaneously.

---

## Named Sessions

```bash
# Create/resume named sessions
claude --session feature-auth     # Auth feature work
claude --session bug-fix-login    # Bug fix work
claude --session refactor-db      # Database refactor

# Resume specific session
claude --resume feature-auth
```

**Benefits**:
- Clear workstream identification
- Resumable across time
- Parallel management

---

## Terminal Organization

### Boris Cherny's Pattern
5 local terminal tabs + 5-10 web sessions:

```
┌─────────────────────────────────────────────────────────┐
│ Tab 1: agent-backend  │ Tab 2: agent-frontend          │
│ Tab 3: agent-tests    │ Tab 4: agent-docs              │
│ Tab 5: orchestrator   │                                │
└─────────────────────────────────────────────────────────┘
```

**Pro tip**: Use multiple monitors to watch agents work simultaneously.

### tmux Alternative
```bash
# Create tmux session with panes
tmux new-session -s agents
tmux split-window -h
tmux split-window -v

# Each pane runs different agent
```

---

## Teleport: Local ↔ Cloud

### Send to Cloud
```bash
# Prefix with & to send to web
& Analyze this codebase for performance bottlenecks
```

Creates background session on claude.ai/code that runs autonomously.

### Retrieve from Cloud
```bash
# Teleport session back to local
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

**Use case**: Start locally, identify long-running task, teleport to cloud, continue local work.

---

## File-Based Coordination

### Oracle Pattern Setup
```
project/
├── tasks/
│   ├── task-001-auth.md        # Oracle creates
│   ├── task-002-api.md         # Oracle creates
│   └── task-003-tests.md       # Oracle creates
├── results/
│   ├── task-001-result.md      # Worker writes
│   ├── task-002-result.md      # Worker writes
│   └── task-003-result.md      # Worker writes
└── master_plan.md              # Oracle maintains
```

### Workflow
1. Oracle (Opus) writes task specs to `tasks/`
2. Workers (Sonnet) watch `tasks/`, execute, write to `results/`
3. Oracle reads `results/`, updates `master_plan.md`, issues new tasks

**No complex networking**—file system is the coordination bus.

---

## Parallel Merge Strategy

```bash
# Long isolated branches with infrequent merges
# Each agent works on own branch

# At sync points:
git checkout main
git merge --no-ff feature/backend-refactor
git merge --no-ff feature/frontend-redesign
```

**Cadence**: Merge at natural breakpoints (feature complete, phase done), not continuously.

**Why**: AI agents bad at resolving merge conflicts. Minimize merge frequency.

---

## Resource Management

### Context Window per Agent
Each agent has independent 200K context—parallel agents multiply total capacity.

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
| 3-7 | **Optimal**—good parallelism, manageable coordination |
| 7-10 | Increasing overhead, human attention bottleneck |
| 10+ | Coordination costs exceed benefits |

**Bottleneck shifts**: From AI speed → Human attention to integrate outputs.

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

- [[SYNTHESIS-claude_code_architecture]] → WorktreeIsolation, AccessPoints
- [[MECH-task_orchestration]] → Parallel agent spawning
- [[PRAC-ralph_pattern_execution]] → Alternative: fresh context loops
