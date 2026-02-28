# MECH: Task Orchestration System

**Scope**: Dependency management, parallel agent spawning, cross-session persistence

---

## Core Concept

```
TERM TaskOrchestration:
sutra: "From flat todo lists to dependency-aware orchestration—blocked tasks cannot begin until prerequisites complete"
gloss: Jan 2026 evolution transforms Claude from "smart assistant that loses track"
       to "orchestrator managing complex work with structure." Tasks have subjects,
       descriptions, owners, and blockedBy relationships. Persists within sessions
       (survives compaction) and across sessions.
spec:
    type: MECHANISM
    evolution_from: "Flat TodoWrite tool"
    key_differentiator: "Dependency graph enforcement"
    visual_tracking: "Terminal dashboard showing blocked/in_progress/completed"
end
```

---

## The Four Core Tools

### TaskCreate
Creates new task with metadata.

```json
{
  "tool": "TaskCreate",
  "subject": "Set up database connection",
  "description": "Configure PostgreSQL connection pool, create users table",
  "activeForm": "Setting up database connection",
  "metadata": {
    "priority": "high",
    "estimate": "30min"
  }
}
```

Tasks start with `status: pending` and no owner. Metadata stored for future features.

### TaskUpdate
Modify any aspect of existing task.

```json
{
  "tool": "TaskUpdate",
  "taskId": "3",
  "status": "in_progress",
  "owner": "backend-dev",
  "addBlockedBy": ["1", "2"]
}
```

**Critical**: `addBlocks` and `addBlockedBy` *append* to arrays—they don't replace.

### TaskGet
Retrieve full details of specific task.

```json
{
  "tool": "TaskGet",
  "taskId": "3"
}
```

Returns: subject, description, status, blocks, blockedBy.

### TaskList
See everything at once.

```json
{
  "tool": "TaskList"
}
```

Returns: All tasks with ID, subject, status, owner, blocked-by relationships.

---

## Dependency Model

```
NORM DependencyEnforcement:
sutra: "Blocked tasks ONLY unblock when related tasks marked completed"
gloss: When dependencies added via addBlockedBy: ["1", "2"], task #3 cannot
       start until tasks #1 AND #2 both completed. System enforces automatically.
spec:
    blocking_syntax: 'addBlockedBy: ["1", "2"]'
    unblocking_trigger: "Related tasks marked completed"
    enforcement: "Automatic—agent cannot start blocked work"
end
```

### Visual Representation

```
Tasks (2 done, 2 in progress, 16 open) · ctrl+t to hide tasks
✓ #1 Define article topic and angle (editor-in-chief)
✓ #2 Assign writer and set deadline
■ #3 Writer completes first draft (staff-writer)
□ #4 Conduct fact-checking ⚠ blocked by #3
□ #5 Perform substantive edit ⚠ blocked by #3
□ #6 Writer completes revisions ⚠ blocked by #4, #5
```

When #3 completes → #4 and #5 automatically unblock and become available.

---

## Task Storage

```
~/.claude/tasks/<list-id>/
├── 1.json
├── 2.json
├── 3.json
└── ...
```

### JSON Schema Per Task

```json
{
  "id": "23",
  "subject": "Test metadata functionality",
  "description": "Testing if metadata gets stored",
  "activeForm": "Testing metadata",
  "owner": "backend-dev",
  "status": "pending",
  "blocks": ["24", "25"],
  "blockedBy": ["1", "2"],
  "metadata": {
    "priority": "high",
    "estimate": "30min"
  }
}
```

### Access Patterns

```bash
# View all task lists
ls ~/.claude/tasks/

# View specific task list
ls ~/.claude/tasks/my-project/

# Read specific task
cat ~/.claude/tasks/my-project/1.json | jq
```

**Enables**: Backup/restore, git tracking of state, external tooling integration, cross-project templates.

---

## Persistence Modes

### Within Session (Default)
Tasks automatically survive context compaction. As conversation summarized, task state remains intact.

### Across Sessions

**Method 1: Environment Variable**
```bash
CLAUDE_CODE_TASK_LIST_ID="my-project-tasks" claude
```
Not picked up on next session.

**Method 2: Settings Configuration**
```json
// .claude/settings.json
{
  "env": {
    "CLAUDE_CODE_TASK_LIST_ID": "billion-dollar-saas"
  }
}
```
Tasks persist between completely separate conversations.

**Maintenance**: Archive or clean up after each task set completes—full list given to Claude each session.

---

## Agent Assignment and Parallel Execution

### Step 1: Claude Creates and Assigns Tasks
```json
{ "taskId": "4", "owner": "fact-checker" }
{ "taskId": "5", "owner": "senior-editor" }
```

### Step 2: Claude Spawns Agents with Instructions
```json
{
  "subagent_type": "general-purpose",
  "model": "haiku",
  "prompt": "You are fact-checker. Call TaskList, find tasks where owner: fact-checker, complete them. Mark in_progress when starting, completed when done.",
  "description": "Fact-checker agent"
}
```

### Step 3: Agent Self-Discovery
Spawned agent:
1. Calls `TaskList` to see all tasks
2. Filters for `owner` matching its name
3. Calls `TaskUpdate` to mark `in_progress`
4. Does the work
5. Calls `TaskUpdate` to mark `completed`

### Parallel Spawn Pattern
Multiple Task calls in single message = parallel execution:

```json
// Three agents, running simultaneously, all updating same task list
{ "subagent_type": "general-purpose", "prompt": "You are fact-checker...", "model": "haiku" }
{ "subagent_type": "general-purpose", "prompt": "You are senior-editor...", "model": "haiku" }
{ "subagent_type": "Bash", "prompt": "Run test suite and report...", "model": "haiku" }
```

No conflicts—shared task list acts as coordination layer.

---

## Model Selection for Task Agents

| Type | Capabilities | Use When |
|------|--------------|----------|
| **general-purpose** | Read, write, edit, search, execute | Most implementation work |
| **Bash** | Terminal only | Git ops, tests, builds |
| **Explore** | Read and search only | "Where is X?" questions |
| **Plan** | Read-only, architecture focus | Design before implementation |

### Model Tiers

| Model | Use For |
|-------|---------|
| `haiku` | Running commands, simple searches |
| `sonnet` | Moderate complexity, most coding |
| `opus` | Architecture decisions, nuanced problems |

---

## Example: Complex Refactor

```
// Investigation first—can't plan without understanding
{ "subject": "Investigate current session implementation" }
{ "subject": "Research JWT best practices" }

// Planning blocked by investigation
{ "subject": "Design JWT implementation plan", "addBlockedBy": ["1", "2"] }

// Implementation blocked by planning
{ "subject": "Implement JWT authentication", "addBlockedBy": ["3"] }
{ "subject": "Update all protected routes", "addBlockedBy": ["4"] }
{ "subject": "Add token refresh mechanism", "addBlockedBy": ["4"] }

// Testing blocked by implementation
{ "subject": "Write integration tests", "addBlockedBy": ["5", "6"] }
```

**Key insight**: Tasks #1 and #2 run in parallel (no dependencies), but #3 waits for both.

---

## When to Use Tasks

**Use for**:
- Multi-step work (3+ steps)
- Anything with dependencies
- Work spanning sessions
- Complex refactors or features
- Delegating to multiple agents

**Skip for**:
- Quick one-off questions
- Simple single-file edits
- Anything finished in one shot

---

## Best Practices

1. **Let Claude break down work**: Say what you want, let it create structure
2. **Dependencies are your friend**: Prevent "built Y but forgot X it depends on"
3. **Use meaningful owner names**: "backend-dev" better than "agent1"
4. **Check TaskList when stuck**: It's your source of truth
5. **activeForm matters**: Good: "Running database migrations" / Bad: "Doing stuff"

---

## Anti-Patterns

- **Manual task micromanagement**: Let Claude decompose
- **Circular dependencies**: System doesn't detect—results in deadlock
- **Over-granular tasks**: Each task should be meaningful unit
- **Ignoring blocked status**: Working around dependencies defeats purpose

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → TaskSystem TERM block
- [[MECH-skill_system_architecture]] → Subagent pairing in skills
- [[PRAC-parallel_claude_orchestration]] → Multi-instance coordination
