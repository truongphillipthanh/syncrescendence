> **ARCHIVED**: 2026-02-23 | Reason: CONSOLIDATED into MECH-context_compaction_strategies.md
> **Origin**: praxis/05-SIGMA/practice/
> **Archived by**: Commander (DC-205 Phase 2C overlap consolidation)

# PRAC: Ralph Pattern Execution

**Scope**: Fresh context loops, static prompts, avoiding compaction entirely

---

## The Insight

```
TERM RalphPattern:
sutra: "Wipe the whiteboard after every task—AI operates in smartest mode with fresh context"
gloss: Ralph isn't about running AI in a loop. Any script can do that. Ralph works
       because it keeps AI operating at peak capability by wiping context completely
       after each task. No compaction, no growing memory files, no accumulated noise.
spec:
    type: PRACTICE
    creator: "Jeff Huntley"
    key_insight: "LLMs get worse as context grows—fresh start every time"
    anti_pattern: "Anthropic's official plugin uses compaction, defeating the purpose"
end
```

---

## Why It Works

Context window is like a whiteboard:
- **Clean**: AI reads instructions clearly, executes precisely
- **Full**: AI wading through noise to find signal, forgets things, contradicts itself

**Ralph solves this** by wiping the whiteboard after every single task.

---

## The Canonical Implementation

One bash while loop:

```bash
#!/bin/bash
# ralph.sh

while true; do
    claude -p "$(cat prompt.md)" --max-turns 50

    # Check if all tasks complete
    if grep -q "passes: true" prd.md && ! grep -q "passes: false" prd.md; then
        echo "All tasks complete!"
        break
    fi

    sleep 5
done
```

**That's it.** No compaction. No growing memory files. No clever additions.

---

## Required Files

### prompt.md (Static Instructions)
```markdown
# Instructions

1. Read prd.md for the task list
2. Find the highest priority incomplete task (passes: false)
3. Implement it
4. Run validation steps
5. Only mark passes: true if everything checks out
6. Exit when done with this task

Do NOT attempt multiple tasks in one session.
```

**Critical**: This file NEVER changes. Static prompt, fresh every loop.

### prd.md (Task List)
```markdown
# Tasks

## Task 1: Set up database
- Category: backend
- Description: Configure PostgreSQL connection pool
- Validation: `npm run test:db` passes
- passes: false

## Task 2: Create user model
- Category: backend
- Description: User schema with email, password hash
- Validation: `npm run test:user` passes
- passes: false

## Task 3: Auth endpoints
- Category: backend
- Description: Login, logout, refresh token
- Validation: `npm run test:auth` passes
- passes: false
```

Each task has:
- Clear category
- Specific description of done
- Concrete validation steps
- `passes: true/false` flag

### activity.md (Log File)
```markdown
# Activity Log

Each loop appends what happened. Gives visibility without bloating context
(AI reads it fresh each time).
```

### settings.json (Sandbox)
```json
{
  "permissions": {
    "allow": ["Bash(npm run *)"],
    "deny": ["Bash(rm -rf *)"]
  }
}
```

Constrain the damage radius.

---

## Exit Condition

Loop only stops when **every single task** shows `passes: true`.

```bash
# Check completion
if grep -q "passes: true" prd.md && ! grep -q "passes: false" prd.md; then
    exit 0
fi
```

---

## Common Mistakes

### Mistake 1: Using Compaction
Anthropic's official plugin compacts instead of wiping.

**Problem**: AI doesn't know what's actually important. It guesses. Critical information disappears.

**Solution**: Fresh context every loop. No compaction.

### Mistake 2: Growing Memory Files
Popular approach: agent updates `agents.md` every iteration.

**Problem**: Models verbose by default. Each loop adds tokens. Ten iterations in, context stuffed before task starts.

**Solution**: Keep prompt static. Only thing that changes is `passes: true/false` flag.

### Mistake 3: Max Iterations Cap
Plugin adds max iterations and completion conditions.

**Problem**: Cuts off discovery. Ralph finds bugs you didn't know existed.

**Solution**: Let it run until all tasks pass. Trust the exit condition.

---

## Variations That Work

### Parallel Ralphs
Multiple instances, different tasks, same codebase:
```bash
# Terminal 1
TASK_FILTER="backend" ./ralph.sh

# Terminal 2
TASK_FILTER="frontend" ./ralph.sh

# Terminal 3
TASK_FILTER="tests" ./ralph.sh
```

### Browser Validation
Instead of just tests, AI opens app and clicks through flows:
```markdown
- Validation: Open browser, login, verify redirect works
```

### GitHub Issues as Tasks
Ralph picks most important open issue, implements, closes:
```bash
gh issue list --state open --limit 1 > current_issue.md
claude -p "Implement $(cat current_issue.md)"
gh issue close $(cat current_issue.md | grep '#')
```

**All work because**: Fresh context every loop.

---

## Cost Math

| Setup | Cost | Outcome |
|-------|------|---------|
| Correct (fresh context) | ~$30-50 | Working proof of concept |
| Wrong (compaction/growing files) | ~$300 | Broken mess, rebuild manually |

**Typical run**: 10-20 iterations at $2-3 each.

---

## When to Use Ralph

**Good for**:
- Proof of concepts
- Validating architecture
- Overnight builds
- Exploratory implementation

**Not for**:
- Production engineering (needs human review)
- Edge cases requiring judgment
- Architectural decisions requiring context

---

## The Bottom Line

Ralph works because it respects how AI actually functions:
- Limited context
- Maximum focus
- Clean resets

**The moment you add**:
- Compaction
- Growing files
- Accumulated state

...you're fighting the architecture instead of working with it.

---

## Quick Start

```bash
# 1. Create files
mkdir ralph-project && cd ralph-project
touch prompt.md prd.md activity.md

# 2. Write prompt.md (static instructions)
# 3. Write prd.md (task breakdown with passes: false)

# 4. Create prd by asking Claude
claude -p "Break down this project into tasks with validation steps: [your idea]" > prd.md

# 5. Run ralph
while true; do
    claude -p "$(cat prompt.md)" --max-turns 50
    grep -q "passes: false" prd.md || break
    sleep 5
done
```

Budget: 15-25 iterations for most projects.

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → Context degradation problem
- [[MECH-context_compaction_strategies]] → Why compaction fails
- [[MECH-headless_mode_automation]] → -p flag for scripting
