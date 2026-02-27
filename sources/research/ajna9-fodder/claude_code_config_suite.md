# The Definitive Claude Code Configuration Suite

This configuration suite operationalizes the patterns that emerge when independent practitioners converge on the same solutions. It synthesizes the "Fleet Commander" architecture, the "Architect-Builder" protocol, the graduated autonomy profiles, and the compounding engineering philosophy into a coherent, deployable package.

The design principles: separate thinking from doing, externalize state to the filesystem, make "done" machine-verifiable, and earn complexity incrementally.

---

## Directory Structure

```
project-root/
├── CLAUDE.md                      # Project constitution (lean, <100 lines)
├── CLAUDE.local.md                # Personal overrides (gitignored)
├── .mcp.json                      # MCP server definitions
├── .gitignore                     # Includes Claude-specific ignores
│
├── .claude/
│   ├── settings.json              # Runtime configuration
│   ├── settings.local.json        # Personal settings (gitignored)
│   │
│   ├── profiles/
│   │   ├── safe.settings.json     # Maximum caution
│   │   ├── standard.settings.json # Balanced default
│   │   └── yolo.settings.json     # Sandbox-only autonomy
│   │
│   ├── commands/
│   │   ├── commit.md              # Stage, message, commit
│   │   ├── commit-push-pr.md      # Full ship cycle
│   │   ├── plan.md                # Enter planning mode
│   │   ├── impl.md                # Execute from plan
│   │   ├── verify.md              # Run verification suite
│   │   ├── review.md              # Code review workflow
│   │   ├── status.md              # Project status report
│   │   ├── save-context.md        # Externalize before clear
│   │   └── debug.md               # Systematic debugging
│   │
│   ├── skills/
│   │   ├── plan-template.md       # How to write plans
│   │   ├── commit-messages.md     # Conventional commits
│   │   ├── refactor-safely.md     # Safe refactoring protocol
│   │   ├── tasks-operating.md     # Using the Tasks system
│   │   └── codemap-updater.md     # Maintain architecture docs
│   │
│   ├── agents/
│   │   ├── security-reviewer.md   # Security audit subagent
│   │   ├── code-reviewer.md       # General code review
│   │   ├── test-runner.md         # Test execution specialist
│   │   ├── doc-writer.md          # Documentation generator
│   │   ├── ralph-prompt.md        # Autonomous loop executor
│   │   └── oracle-pattern.md      # Multi-agent coordination
│   │
│   └── rules/
│       ├── code-style.md          # Language conventions
│       ├── testing.md             # Test requirements
│       ├── git.md                 # Git workflow rules
│       ├── security.md            # Security constraints
│       └── error-handling.md      # Error patterns
│
├── docs/
│   ├── architecture.md            # System design (referenced by CLAUDE.md)
│   ├── api.md                     # API documentation
│   └── CODEMAP.md                 # File/module map
│
├── scripts/
│   ├── format_on_write.sh         # Universal formatter hook
│   ├── switch-claude-profile.sh   # Profile switching utility
│   └── setup-worktrees.sh         # Parallel session setup
│
├── plan.md                        # Current implementation plan
├── SCRATCHPAD.md                  # Working notes (survives compaction)
└── SESSION_STATE.md               # Handoff state for context resets
```

---

## Core Files

### CLAUDE.md — The Project Constitution

```markdown
# [PROJECT_NAME]

[One-line description: what this is and why it exists]

## Ground Rules

1. **Separate thinking from doing.** Default to Plan Mode for non-trivial work.
2. **Make "done" verifiable.** Changes aren't done until tests/linters/typecheck pass.
3. **Prefer small, composable diffs.** One logical change per commit.
4. **Never guess state.** Inspect with Read/Grep/Glob before assuming.
5. **Do not touch secrets.** Never read/write .env, keys, tokens, credentials.

## Commands

```bash
npm run dev          # Development server
npm run build        # Production build
npm run test         # Test suite
npm run lint         # Lint check
npm run typecheck    # TypeScript validation
npm run verify       # All checks (lint + typecheck + test)
```

## Structure

`src/` — Source | `tests/` — Tests | `docs/` — Documentation

## Constraints

- NO implicit any — explicit types required
- ALWAYS test before commit
- NEVER commit secrets — environment variables only

## Gotchas

[Add discovered issues with # key — this section grows through use]

## Context (Progressive Disclosure)

@docs/architecture.md | @docs/api.md | @docs/CODEMAP.md
```

---

### CLAUDE.local.md — Personal Overrides

```markdown
# Local Overrides (not committed)

## My Preferences

- Prefer verbose explanations when debugging
- Use vim keybindings in examples
- My timezone: America/Los_Angeles

## Local Environment

- Database runs on port 5433 (not default 5432)
- Using pnpm instead of npm

## Current Focus

Working on: [current task description]
Branch: feature/[branch-name]
```

---

### .claude/settings.json — Standard Profile

```json
{
  "$schema": "https://claude.ai/schemas/claude-code-settings.json",
  
  "model": {
    "default": "claude-sonnet-4-20250514",
    "thinking": "claude-opus-4-20250514",
    "fast": "claude-haiku-4-20250514"
  },

  "permissions": {
    "defaultMode": "plan",
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Search",
      "Bash(cat *)",
      "Bash(ls *)",
      "Bash(find *)",
      "Bash(head *)",
      "Bash(tail *)",
      "Bash(wc *)",
      "Bash(git status)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(git show*)",
      "Bash(git branch*)",
      "Bash(git ls-files*)",
      "Bash(npm test*)",
      "Bash(npm run test*)",
      "Bash(npm run lint*)",
      "Bash(npm run typecheck*)",
      "Bash(npm run verify*)",
      "Bash(pnpm test*)",
      "Bash(pnpm run test*)",
      "Bash(yarn test*)",
      "Bash(make test*)",
      "Bash(make verify*)",
      "Bash(make lint*)"
    ],
    "ask": [
      "Write",
      "Edit",
      "MultiEdit",
      "Bash(git add *)",
      "Bash(git commit*)",
      "Bash(git push*)",
      "Bash(git checkout*)",
      "Bash(npm run build*)",
      "Bash(npm install*)",
      "Bash(curl *)",
      "Bash(wget *)",
      "Bash(docker *)",
      "Bash(gh *)"
    ],
    "deny": [
      "Bash(rm -rf /)*",
      "Bash(rm -rf ~)*",
      "Bash(sudo *)",
      "Bash(chmod 777 *)",
      "Bash(*> /etc/*)",
      "Bash(curl * | sh)",
      "Bash(wget * | sh)",
      "Bash(git push --force origin main)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(**/*.pem)",
      "Read(**/*.key)",
      "Write(./.env)",
      "Write(./.env.*)",
      "Write(./secrets/**)",
      "Write(**/*.pem)",
      "Write(**/*.key)"
    ]
  },

  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash scripts/format_on_write.sh \"$file\" 2>/dev/null || true"
          }
        ]
      },
      {
        "matcher": "Write(*.ts)|Write(*.tsx)|Edit(*.ts)|Edit(*.tsx)",
        "hooks": [
          {
            "type": "command",
            "command": "npm run typecheck --silent 2>/dev/null || echo 'TYPECHECK: issues detected'"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "intercept",
            "command": "echo \"$CLAUDE_TOOL_INPUT\" | grep -qE '(rm -rf [^.])|(DROP|DELETE.*WHERE)' && echo 'BLOCKED: Destructive operation requires confirmation' && exit 1 || exit 0"
          }
        ]
      }
    ]
  },

  "context": {
    "compactionThreshold": 0.7,
    "preserveFiles": [
      "CLAUDE.md",
      "plan.md",
      "SCRATCHPAD.md",
      "SESSION_STATE.md"
    ]
  },

  "behavior": {
    "autoCompact": true,
    "showThinking": true,
    "confirmDestructive": true,
    "testBeforeCommit": true
  }
}
```

---

### .claude/profiles/safe.settings.json — Maximum Caution

```json
{
  "model": "claude-opus-4-20250514",
  "permissions": {
    "defaultMode": "plan",
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash(cat *)",
      "Bash(ls *)",
      "Bash(git status)",
      "Bash(git diff*)",
      "Bash(git log*)"
    ],
    "ask": [
      "Write",
      "Edit",
      "MultiEdit",
      "Search",
      "Bash(npm *)",
      "Bash(git *)"
    ],
    "deny": [
      "Bash(rm *)",
      "Bash(sudo *)",
      "Bash(curl *)",
      "Bash(wget *)",
      "Read(./.env*)",
      "Read(./secrets/**)",
      "Write(./.env*)",
      "Write(./secrets/**)"
    ]
  }
}
```

---

### .claude/profiles/yolo.settings.json — Sandbox Only

```json
{
  "model": "claude-opus-4-20250514",
  "permissions": {
    "defaultMode": "auto",
    "allow": [
      "Read",
      "Write",
      "Edit",
      "MultiEdit",
      "Glob",
      "Grep",
      "Search",
      "Bash(*)"
    ],
    "deny": [
      "Bash(sudo *)",
      "Read(./.env*)",
      "Read(./secrets/**)",
      "Read(**/*.pem)",
      "Read(**/*.key)",
      "Write(./.env*)",
      "Write(./secrets/**)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash scripts/format_on_write.sh \"$file\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

---

### .mcp.json — Tool Integrations

```json
{
  "$schema": "https://claude.ai/schemas/mcp-config.json",
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-filesystem", "--root", "."],
      "description": "File system operations in project directory"
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-git"],
      "description": "Git operations"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      },
      "description": "GitHub API (issues, PRs, repos)"
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      },
      "description": "PostgreSQL queries (read-only by default)"
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"],
      "description": "Persistent key-value memory across sessions"
    },
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-puppeteer"],
      "description": "Browser automation for testing"
    }
  },
  "globalShortcuts": {
    "db": "postgres",
    "gh": "github",
    "fs": "filesystem"
  }
}
```

---

## Commands

### .claude/commands/commit.md

```markdown
Review staged changes and create a commit:

1. Run `git diff --cached` to see staged changes
2. Analyze the changes for:
   - Coherence: Do all changes relate to a single purpose?
   - Completeness: Are there unstaged related changes to include?
   - Issues: Any obvious bugs, typos, or style violations?

3. If issues found, report them and ask whether to proceed

4. Generate commit message following conventional commits:
   - type(scope): description
   - Types: feat, fix, refactor, docs, test, chore, perf
   - Description: imperative mood, lowercase, no period
   - Body: explain what and why, not how

5. Run `git commit -m "<message>"`

6. Report: files changed, insertions, deletions

If nothing is staged, run `git status` and suggest what to stage.
```

---

### .claude/commands/commit-push-pr.md

```markdown
---
name: commit-push-pr
description: Commit changes, push branch, and open a PR
allowed-tools: Bash(git:*) Bash(gh:*) Read Grep
---

# Commit, Push, PR

Goal: ship a small, reviewable change with verification.

Steps:
1. Show summary: `git status --porcelain` and `git diff --stat`
2. Run verification: `make verify` or `npm test` or best available
3. Propose conventional-commit message (use commit-messages skill)
4. Commit, push to current branch
5. Open PR via `gh pr create --draft` (draft by default)
6. Print PR URL and review checklist

If `gh` is not installed or authenticated, stop after push and explain next steps.
```

---

### .claude/commands/plan.md

```markdown
---
name: plan
description: Create or update implementation plan
allowed-tools: Read Glob Grep Write
---

# Planning Mode

Create a rigorous implementation plan before execution.

Output to `plan.md` with this structure:

## Objective
What changes and what must NOT change

## Constraints
- Invariants to preserve
- Dependencies to respect
- Performance requirements

## Approach
Numbered steps with clear completion criteria

## Files to Touch
List every file that will be created/modified/deleted

## Risks & Unknowns
- What could go wrong
- How to resolve cheaply (inspect first)

## Verification Steps
Commands to prove the work is correct

## Rollback Strategy
How to undo if things go wrong

---

Do NOT write code until the plan is approved.
```

---

### .claude/commands/impl.md

```markdown
---
name: impl
description: Execute implementation from approved plan
allowed-tools: Read Write Edit Bash(*) Glob Grep
---

# Implementation Mode

Execute the approved plan in `plan.md`.

Protocol:
1. Read `plan.md` to load the approved approach
2. Execute steps in order
3. After each step:
   - Run relevant verification
   - Update plan.md to mark step complete
4. If verification fails:
   - Fix the issue
   - Re-run verification
   - Do not proceed until passing
5. When all steps complete:
   - Run full verification suite
   - Update plan.md status to Complete

Rules:
- One step at a time
- Verify after each change
- Do not skip steps
- Do not add steps without approval
```

---

### .claude/commands/verify.md

```markdown
---
name: verify
description: Run the strongest verification available
allowed-tools: Bash(make:*) Bash(npm:*) Bash(pnpm:*) Bash(yarn:*) Read Grep
---

# Verify

Run checks in descending preference:
- `make verify`
- `make test`
- `npm run verify`
- `npm test` / `pnpm test` / `yarn test`
- Language-specific: `pytest`, `go test ./...`, `cargo test`

Report:
- What ran
- What passed/failed
- Next fix step if failing
```

---

### .claude/commands/save-context.md

```markdown
---
name: save-context
description: Externalize state before clearing context
allowed-tools: Read Write Glob
---

# Save Context

Before clearing or compacting, preserve critical state.

1. Update SESSION_STATE.md with:
   ```markdown
   # Session State Handoff
   *Last Updated: [timestamp]*
   
   ## Current Context
   - **Active Task**: [link to plan.md item]
   - **Last Action**: [what was just done]
   - **Critical Context**: [variables, file paths in focus]
   
   ## Instructions for Next Session
   1. Read `plan.md`
   2. Resume work on [task]
   3. Watch out for [known issues]
   ```

2. Update plan.md with current progress

3. Add any new gotchas to CLAUDE.md

4. Confirm state is externalized

5. Now safe to run `/clear` or `/compact`
```

---

### .claude/commands/status.md

```markdown
---
name: status
description: Report project and session status
allowed-tools: Read Bash(git:*) Glob
---

# Status Report

Generate a status report covering:

## Git State
- Current branch
- Uncommitted changes
- Recent commits (last 5)

## Plan Progress
- Read plan.md
- Report completion percentage
- List blocked/in-progress items

## Context Health
- Approximate context usage
- Files currently loaded
- Recommendation: compact/continue/clear

## Next Actions
- Highest priority incomplete task
- Any blockers to resolve
```

---

### .claude/commands/debug.md

```markdown
---
name: debug
description: Systematic debugging workflow
allowed-tools: Read Bash(*) Grep Glob Search
---

# Debug Protocol

Systematic approach to finding and fixing bugs.

## Phase 1: Reproduce
1. Understand the expected vs actual behavior
2. Find minimal reproduction steps
3. Verify the bug is reproducible

## Phase 2: Isolate
1. Identify the module/function where bug manifests
2. Trace the data flow backward
3. Find the point where behavior diverges from expected

## Phase 3: Diagnose
1. Form hypothesis about root cause
2. Add logging/inspection to verify hypothesis
3. Confirm understanding before fixing

## Phase 4: Fix
1. Make minimal change to fix root cause
2. Remove diagnostic code
3. Verify fix doesn't break other tests

## Phase 5: Verify
1. Confirm original bug is fixed
2. Run full test suite
3. Check for regressions

## Phase 6: Document
1. Add regression test if not already covered
2. Document gotcha in CLAUDE.md if pattern-worthy
```

---

### .claude/commands/review.md

```markdown
---
name: review
description: Code review workflow
allowed-tools: Read Bash(git:*) Grep Glob
---

# Code Review

Review changes for quality and correctness.

1. Get the diff:
   - `git diff` for unstaged
   - `git diff --cached` for staged
   - `git diff main...HEAD` for branch changes

2. Review for:
   - Correctness: Does it do what it claims?
   - Completeness: Missing edge cases?
   - Style: Consistent with codebase?
   - Security: Any vulnerabilities introduced?
   - Performance: Any obvious inefficiencies?
   - Tests: Are changes tested?

3. Report findings:
   - Critical issues (must fix)
   - Suggestions (should consider)
   - Nitpicks (optional improvements)

4. If requested, apply fixes directly
```

---

## Skills

### .claude/skills/plan-template.md

```markdown
---
name: plan-template
description: When asked to plan, produce a plan with verification and rollback
---

When producing a plan, include:

- **Objective**: What changes and what must not change
- **Constraints / Invariants**: Rules that cannot be violated
- **Approach**: Numbered steps with completion criteria
- **Files to Touch**: Every file created/modified/deleted
- **Risks / Unknowns**: What could go wrong + cheap resolution
- **Verification Steps**: Commands to prove correctness
- **Rollback Strategy**: How to undo safely
```

---

### .claude/skills/commit-messages.md

```markdown
---
name: commit-messages
description: Generate conventional commit messages
---

Format: `type(scope): description`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code restructuring (no behavior change)
- `docs`: Documentation only
- `test`: Adding/fixing tests
- `chore`: Maintenance tasks
- `perf`: Performance improvement

Rules:
- Description in imperative mood ("add" not "added")
- Lowercase, no period at end
- Under 72 characters for subject
- Body explains what and why (not how)

Examples:
- `feat(auth): add password reset flow`
- `fix(api): handle null response from payment gateway`
- `refactor(utils): extract date formatting to shared module`
```

---

### .claude/skills/refactor-safely.md

```markdown
---
name: refactor-safely
description: Safe code refactoring with verification
---

# Safe Refactoring Protocol

## Pre-Refactor
1. Verify tests exist for code being changed
2. Run tests — must pass before changes
3. Identify all callers of the code

## During Refactor
1. Small, incremental changes
2. One logical change per commit
3. Functionality must remain identical
4. Run tests after each change

## Post-Refactor
1. Run full test suite
2. Review diff for unintended changes
3. Commit: `refactor(scope): what changed`

## Red Flags
- Tests don't cover the code → write tests first
- Behavior changes → that's not refactoring
- Too many files changing → break into smaller refactors
```

---

### .claude/skills/tasks-operating.md

```markdown
---
name: tasks-operating
description: Use the Task system for multi-step work with dependencies
---

When work has multiple dependent steps:
- Create tasks with clear subjects and definitions of done
- Use `blockedBy`/`blocks` to prevent premature work
- Store key decisions in task descriptions (survives compaction)
- Close tasks only after verification

If Tasks are not available, emulate with markdown checklist:
```markdown
- [ ] #1 Task name [no dependencies]
- [ ] #2 Task name [blocked by #1]
- [ ] #3 Task name [blocked by #1, #2]
```
```

---

## Agents

### .claude/agents/security-reviewer.md

```markdown
---
name: security-reviewer
description: Security-focused code reviewer (read-only)
tools: Read Grep Glob
model: claude-opus-4-20250514
---

You are a security-focused code reviewer.

When analyzing code:
1. Check authn/authz gaps and privilege escalation paths
2. Look for injection vulnerabilities (SQL, command, XSS)
3. Identify sensitive data exposure (logs, errors, client leaks)
4. Flag insecure dependency or crypto usage
5. Note missing validation/sanitization at boundaries

Output:
- Findings grouped by severity: critical/high/medium/low
- Concrete file references with line numbers
- Minimal remediation steps

You do NOT modify code. You report findings only.
```

---

### .claude/agents/code-reviewer.md

```markdown
---
name: code-reviewer
description: General code review subagent
tools: Read Grep Glob
---

You are a code reviewer focused on quality and maintainability.

Review for:
- Correctness: Logic errors, edge cases
- Clarity: Naming, structure, comments
- Consistency: Style alignment with codebase
- Complexity: Unnecessary complication
- Coverage: Are changes tested?

Output:
- Issues by severity
- Specific suggestions with file/line references
- Praise for good patterns worth preserving

Be constructive. Explain why, not just what.
```

---

### .claude/agents/ralph-prompt.md

```markdown
---
name: ralph
description: Autonomous execution loop for task lists
tools: Read Write Edit Bash(*)
---

# Autonomous Execution Prompt

You are executing tasks from a predefined plan. Each loop iteration starts fresh.

## Instructions

1. Read `plan.md` to understand the full task list
2. Find the highest-priority task where status is incomplete
3. Implement that single task completely
4. Run validation steps defined in the task
5. If validation passes, mark task complete in plan.md
6. If validation fails, fix and retry (max 3 attempts)
7. Exit when all tasks complete

## Rules

- One task per iteration
- Complete implementation, not scaffolding
- Verify your own work before marking complete
- Do not modify tasks you're not working on
- Do not add new tasks without approval

## On Completion

When all tasks show complete:
1. Run full test suite
2. Report summary
3. Exit cleanly

## On Failure

If stuck after 3 attempts:
1. Log failure details to SCRATCHPAD.md
2. Mark task with `blocked: true`
3. Move to next task
4. Continue execution

Do not loop indefinitely on a single failing task.
```

---

### .claude/agents/oracle-pattern.md

```markdown
---
name: oracle
description: Hierarchical multi-agent coordination pattern
---

# Oracle Pattern: Multi-Agent Coordination

## Architecture

```
┌─────────────────────────────────────────────┐
│              Oracle (Opus 4.5)              │
│  - Maintains master plan                    │
│  - Decomposes work into tasks               │
│  - Delegates to workers                     │
│  - Integrates results                       │
└──────────────────┬──────────────────────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Worker 1 │ │ Worker 2 │ │ Worker 3 │
│ (Sonnet) │ │ (Sonnet) │ │ (Haiku)  │
│ Feature  │ │ Tests    │ │ Docs     │
└──────────┘ └──────────┘ └──────────┘
```

## Communication via Filesystem

```
.claude/
├── oracle/
│   ├── master-plan.md      # Oracle's plan
│   ├── task-queue.md       # Pending tasks
│   └── decisions.md        # Architectural decisions
└── workers/
    ├── worker-1/
    │   ├── current-task.md
    │   ├── status.md
    │   └── output.md
    └── worker-2/
        └── ...
```

## Running

Terminal 1 (Oracle):
```bash
claude --model opus --prompt-file .claude/agents/oracle-prompt.md
```

Terminals 2-4 (Workers):
```bash
claude --model sonnet --workdir .claude/workers/worker-1
claude --model sonnet --workdir .claude/workers/worker-2
claude --model haiku --workdir .claude/workers/worker-3
```

Use git worktrees for file isolation between workers.
```

---

## Scripts

### scripts/format_on_write.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

FILE="${1:-}"
if [[ -z "$FILE" ]]; then
  echo "format_on_write.sh: missing file path" >&2
  exit 2
fi

ext="${FILE##*.}"

# Only run formatters if they exist (best effort)
have() { command -v "$1" >/dev/null 2>&1; }

case "$ext" in
  py)
    if have black; then black -q "$FILE"; fi
    if have isort; then isort -q "$FILE"; fi
    ;;
  js|ts|jsx|tsx|json|css|scss|md|yaml|yml)
    if have prettier; then prettier --write --log-level error "$FILE"; fi
    ;;
  go)
    if have gofmt; then gofmt -w "$FILE"; fi
    ;;
  rs)
    if have rustfmt; then rustfmt --quiet "$FILE"; fi
    ;;
  *)
    # no-op for unknown extensions
    ;;
esac
```

---

### scripts/switch-claude-profile.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

PROFILE="${1:-standard}"
PROFILES_DIR=".claude/profiles"
SETTINGS_FILE=".claude/settings.json"

if [[ ! -f "$PROFILES_DIR/$PROFILE.settings.json" ]]; then
  echo "Unknown profile: $PROFILE"
  echo "Available profiles:"
  ls -1 "$PROFILES_DIR" | sed 's/.settings.json$//'
  exit 1
fi

cp "$PROFILES_DIR/$PROFILE.settings.json" "$SETTINGS_FILE"
echo "Switched to profile: $PROFILE"
```

---

### scripts/setup-worktrees.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

# Create isolated worktrees for parallel Claude sessions
BRANCH_PREFIX="${1:-claude}"
NUM_WORKERS="${2:-3}"

for i in $(seq 1 $NUM_WORKERS); do
  BRANCH="$BRANCH_PREFIX/worker-$i"
  WORKTREE="../$(basename "$PWD")-worker-$i"
  
  if [[ ! -d "$WORKTREE" ]]; then
    git worktree add "$WORKTREE" -b "$BRANCH" 2>/dev/null || \
    git worktree add "$WORKTREE" "$BRANCH"
    echo "Created worktree: $WORKTREE (branch: $BRANCH)"
  else
    echo "Worktree exists: $WORKTREE"
  fi
done

echo ""
echo "Run Claude in each worktree:"
for i in $(seq 1 $NUM_WORKERS); do
  echo "  cd ../$(basename "$PWD")-worker-$i && claude"
done
```

---

## State Files

### plan.md — Implementation Plan Template

```markdown
# Implementation Plan

> Status: Planning | Active | Blocked | Complete

## Objective
[What changes and what must NOT change]

## Constraints
- [Invariant 1]
- [Invariant 2]

## Approach

### Phase 1: [Name]
- [ ] Step 1.1: [Description]
- [ ] Step 1.2: [Description]

### Phase 2: [Name]
- [ ] Step 2.1: [Description] (blocked by Phase 1)
- [ ] Step 2.2: [Description]

## Files to Touch
- `src/module.ts` — modify
- `src/newfile.ts` — create
- `tests/module.test.ts` — modify

## Risks & Unknowns
- [Risk 1] → [Mitigation]
- [Unknown 1] → [How to resolve cheaply]

## Verification
```bash
npm run typecheck
npm run test
npm run build
```

## Rollback
```bash
git checkout main -- src/
```
```

---

### SESSION_STATE.md — Handoff Template

```markdown
# Session State Handoff

*Last Updated: [timestamp]*

## Current Context
- **Active Task**: [Link to plan.md item]
- **Last Action**: [What was just completed/attempted]
- **Critical Context**: [Variables, file paths, decisions in working memory]

## Key Decisions This Session
- [Decision 1]: [Rationale]
- [Decision 2]: [Rationale]

## Instructions for Next Session
1. Read `plan.md` for full context
2. Resume work on [specific task]
3. Watch out for [known issue/gotcha]

## Files Currently In Focus
- `src/auth/login.ts` — implementing password validation
- `tests/auth/login.test.ts` — need to add edge case tests
```

---

### SCRATCHPAD.md — Working Notes

```markdown
# Scratchpad

Working notes that survive context compaction.

## Current Thinking
[Freeform notes about approach, alternatives considered]

## Questions to Resolve
- [ ] Question 1?
- [ ] Question 2?

## Debugging Notes
[Observations, hypotheses, test results]

## References
- [Link or file path]
- [Link or file path]
```

---

## .gitignore Additions

```gitignore
# Claude Code local files
CLAUDE.local.md
.claude/settings.local.json
SESSION_STATE.md
SCRATCHPAD.md

# Keep plan.md tracked for team visibility
# !plan.md
```

---

## Quick Reference

### Thinking Levels

| Trigger | Budget | Use For |
|---------|--------|---------|
| `think` | ~4K tokens | Moderate complexity |
| `think hard` | ~8K tokens | Complex problems |
| `think harder` | ~16K tokens | Very complex |
| `ultrathink` | ~32K tokens | Architecture, hard bugs |

### Mode Switching

| Action | Effect |
|--------|--------|
| `Shift+Tab` once | Cycle input modes |
| `Shift+Tab` twice | Toggle Plan Mode |
| `Esc` | Cancel current operation |
| `Ctrl+C` | Interrupt Claude |

### Key Built-in Commands

| Command | Purpose |
|---------|---------|
| `/init` | Initialize CLAUDE.md |
| `/compact` | Compress context |
| `/clear` | Clear conversation |
| `/cost` | Show token usage |
| `/help` | List all commands |

### Context Health

| Threshold | Action |
|-----------|--------|
| <40% | Continue normally |
| 40-60% | Consider proactive compaction |
| 60-80% | Strongly recommend compact |
| 80%+ | Quality degradation likely |

### Autonomy Profiles

| Profile | Use Case |
|---------|----------|
| `safe` | Production systems, learning, high-risk work |
| `standard` | Normal development (default) |
| `yolo` | Sandboxed prototyping, throwaway spikes |

Switch with: `bash scripts/switch-claude-profile.sh [profile]`

---

## Implementation Checklist

1. **Initialize**: Copy this structure to your project root
2. **Customize CLAUDE.md**: Add your project-specific commands, structure, constraints
3. **Configure MCP**: Update `.mcp.json` with your tokens/paths
4. **Set Profile**: Start with `standard`, adjust as needed
5. **Create plan.md**: For your first non-trivial task
6. **Compound**: Every mistake → update CLAUDE.md or add a rule

The configuration earns complexity over time. Start lean, add what repeated friction reveals you need.
