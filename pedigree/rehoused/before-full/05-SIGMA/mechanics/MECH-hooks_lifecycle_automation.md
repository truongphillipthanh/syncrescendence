# MECH: Hooks Lifecycle Automation

**Scope**: PreToolUse guards, PostToolUse polish, governance patterns, intelligent workflows

---

## Core Concept

```
TERM HookSystem:
sutra: "Deterministic control points injected at lifecycle events—validate, polish, checkpoint"
gloss: Hooks are the nervous system of automation. They fire at specific events,
       enabling guardrails (block dangerous ops), polish (auto-format), and
       governance (audit logging) without polluting agent context.
spec:
    type: MECHANISM
    purpose: "Inject logic into agent lifecycle"
    advantage: "Deterministic—unlike prompts, hooks ALWAYS fire"
    configuration: ["settings.json", ".claude/hooks/"]
end
```

---

## Hook Types

| Hook | Fires When | Common Use |
|------|------------|------------|
| **PreToolUse** | Before tool executes | Validation, security guards |
| **PostToolUse** | After tool completes | Formatting, feedback loops |
| **UserPromptSubmit** | User sends message | Context injection |
| **PreCompact** | Before compaction | State backup |
| **Stop** | Session ends | Audit, cleanup |
| **Notification** | Permission requests | Custom handling |

---

## Configuration Format

```json
// settings.json or .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "tool == \"Bash\" && tool_input.command matches \"rm\"",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'DANGEROUS: rm detected' && exit 2"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {"type": "command", "command": "python -m black $file"}
        ]
      }
    ]
  }
}
```

---

## Matcher Syntax

### Tool-Based Matching
```json
"matcher": "tool == \"Bash\""
"matcher": "Write(*.py)"
"matcher": "Edit && .ts/.tsx/.js/.jsx"
```

### Command Pattern Matching
```json
"matcher": "tool == \"Bash\" && tool_input.command matches \"(npm|pnpm|yarn|cargo|pytest)\""
"matcher": "tool == \"Bash\" && tool_input.command matches \"git push\""
```

### File Pattern Matching
```json
"matcher": "Write(*.md)"
"matcher": "Edit && .ts/.tsx"
```

---

## PreToolUse Patterns

### The Sentinel (Security Guard)
Block dangerous operations before execution.

```json
{
  "PreToolUse": [{
    "matcher": "tool == \"Bash\" && tool_input.command matches \"rm -rf\"",
    "hooks": [{
      "type": "command",
      "command": "echo 'BLOCKED: rm -rf requires manual execution' && exit 2"
    }]
  }]
}
```

**Exit code 2 blocks the action** and forces agent to reconsider.

### State Validation
Ensure prerequisites before action.

```json
{
  "PreToolUse": [{
    "matcher": "Write(src/**/*)",
    "hooks": [{
      "type": "command",
      "command": "git diff --quiet || echo 'Warning: uncommitted changes'"
    }]
  }]
}
```

### tmux Reminder
Suggest session persistence for long-running commands.

```json
{
  "PreToolUse": [{
    "matcher": "tool == \"Bash\" && tool_input.command matches \"(npm|pnpm|yarn|cargo|pytest)\"",
    "hooks": [{
      "type": "command",
      "command": "if [ -z \"$TMUX\" ]; then echo '[Hook] Consider tmux for session persistence' >&2; fi"
    }]
  }]
}
```

---

## PostToolUse Patterns

### The Auto-Linter
Format code immediately after writes.

```json
{
  "PostToolUse": [{
    "matcher": "Write(*.py)",
    "hooks": [{"type": "command", "command": "python -m black $file"}]
  }, {
    "matcher": "Write(*.ts) || Write(*.tsx) || Write(*.js)",
    "hooks": [{"type": "command", "command": "prettier --write $file"}]
  }]
}
```

**Benefit**: Agent never wastes tokens fixing indentation—every edit syntactically perfect before agent sees it again.

### TypeScript Check
Run type checker after edits.

```json
{
  "PostToolUse": [{
    "matcher": "Edit && .ts/.tsx",
    "hooks": [{"type": "command", "command": "tsc --noEmit"}]
  }]
}
```

### Console.log Warning
Catch debug statements.

```json
{
  "PostToolUse": [{
    "matcher": "Edit",
    "hooks": [{
      "type": "command",
      "command": "grep -l 'console.log' $file && echo 'WARNING: console.log detected'"
    }]
  }]
}
```

---

## PreCompact Patterns

### The Black Box Recorder
Save critical state before compaction.

```json
{
  "PreCompact": [{
    "matcher": "*",
    "hooks": [{
      "type": "command",
      "command": "cat plan.md > .claude/backup_plan.md && git status > .claude/backup_state.txt"
    }]
  }]
}
```

Ensures even if compaction is lossy, critical state saved externally.

---

## Stop Patterns

### Session Audit
Verify state at session end.

```json
{
  "Stop": [{
    "matcher": "*",
    "hooks": [{
      "type": "command",
      "command": "git status && git diff --stat"
    }]
  }]
}
```

### Console.log Audit
Check all modified files before session ends.

```json
{
  "Stop": [{
    "matcher": "*",
    "hooks": [{
      "type": "command",
      "command": "git diff --name-only | xargs grep -l 'console.log' || true"
    }]
  }]
}
```

---

## Intelligent Git Workflow

Complete pattern for checkpoint commits:

```json
{
  "PostToolUse": [{
    "matcher": "Write(*) || Edit(*)",
    "hooks": [{
      "type": "command",
      "command": "git add -A && git commit -m 'checkpoint: $file' --no-verify"
    }]
  }],
  "Stop": [{
    "matcher": "*",
    "hooks": [{
      "type": "command",
      "command": "git rebase -i --autosquash HEAD~20 && git commit --amend -m 'Task complete'"
    }]
  }]
}
```

Creates checkpoint commit on every file change, squashes into meaningful task commit at end.

---

## Hook in Skills Frontmatter

Skills can define their own hooks:

```yaml
---
name: code-review
description: Comprehensive code review
hooks:
  PostToolUse:
    - matcher: "Read(*)"
      command: "echo 'Reviewed: $file'"
---
```

---

## Practical Configuration

### @affaanmustafa's Production Setup

```json
{
  "PreToolUse": [
    {"matcher": "npm|pnpm|yarn|cargo|pytest", "hooks": ["tmux reminder"]},
    {"matcher": "Write && .md file", "hooks": ["block unless README/CLAUDE"]},
    {"matcher": "git push", "hooks": ["open editor for review"]}
  ],
  "PostToolUse": [
    {"matcher": "Edit && .ts/.tsx/.js/.jsx", "hooks": ["prettier --write"]},
    {"matcher": "Edit && .ts/.tsx", "hooks": ["tsc --noEmit"]},
    {"matcher": "Edit", "hooks": ["grep console.log warning"]}
  ],
  "Stop": [
    {"matcher": "*", "hooks": ["check modified files for console.log"]}
  ]
}
```

---

## Creating Hooks Conversationally

Use the `hookify` plugin:

```bash
/plugin install hookify@claude-plugins-official
```

Then describe what you want:
```
"Create a hook that runs eslint after every JavaScript file edit"
```

---

## Anti-Patterns

### Write-Time Hooks Frustrating Agents
Heavy PostToolUse hooks on every Write can slow agent down, causing frustration loops.

**Better**: Run formatters, not full test suites.

### Silent Hook Failures
Hooks failing without clear error messages cause mysterious behavior.

**Better**: Verbose output during development, comprehensive error handling.

### Overly Broad Matchers
```json
{"matcher": "*", "hooks": ["expensive_operation"]}
```
Runs on EVERY tool use—kills performance.

**Better**: Specific matchers for specific operations.

---

## Hook Summary Table

| Pattern | Hook | Matcher | Action |
|---------|------|---------|--------|
| Security Guard | PreToolUse | `rm -rf` | exit 2 (block) |
| Auto-Format | PostToolUse | `Write(*.py)` | black |
| Type Check | PostToolUse | `Edit && .ts` | tsc --noEmit |
| State Backup | PreCompact | `*` | dump to files |
| Audit | Stop | `*` | git status |

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → HookLifecycle TERM block
- [[MECH-skill_system_architecture]] → Hooks in skill frontmatter
- [[PRAC-parallel_claude_orchestration]] → Hooks in multi-instance setups
