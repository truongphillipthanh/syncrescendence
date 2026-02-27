# MECH: Headless Mode Automation

**Scope**: `-p` flag, output formats, max-turns limiting, CI/CD integration

---

## Core Concept

```
TERM HeadlessMode:
sutra: "Claude Code as Unix filter—pipe in, pipe out, embed in scripts"
gloss: The -p flag turns Claude Code into a scriptable automation tool. No
       interactive prompts, structured output, max-turn limits. Embeddable in
       bash scripts, cron jobs, GitHub Actions.
spec:
    type: MECHANISM
    flag: "-p (print/prompt mode)"
    purpose: "Non-interactive execution for automation"
    integration: [bash_scripts, cron_jobs, github_actions, ci_pipelines]
end
```

---

## Basic Usage

```bash
# Simple prompt execution
claude -p "Analyze this code for vulnerabilities"

# With input piping
cat issue.json | claude -p "Triage this issue and create a plan"

# Output to file
claude -p "Generate test cases for auth module" > tests.md
```

---

## Key Flags

| Flag | Purpose |
|------|---------|
| `-p` / `--print` | Non-interactive mode |
| `--output-format json` | Structured JSON output |
| `--output-format text` | Plain text output |
| `--max-turns N` | Limit agentic iterations |
| `--dangerously-skip-permissions` | Full autonomy (⚠️ requires sandboxing) |

---

## Output Formats

### Text (Default)
```bash
claude -p "Summarize this file" --output-format text
```
Returns plain text response.

### JSON
```bash
claude -p "List all API endpoints" --output-format json
```
Returns structured JSON for parsing:
```json
{
  "response": "...",
  "tool_calls": [...],
  "tokens_used": 1234
}
```

---

## Max-Turns Limiting

```bash
# Limit to 5 agentic loops
claude -p "Refactor auth module" --max-turns 5
```

**Use cases**:
- Prevent runaway tasks
- Budget control (token limits)
- CI/CD timeout management
- Proof-of-concept validation

**Ralph pattern caveat**: Sometimes you WANT unlimited turns for discovery. Max-turns caps that exploration.

---

## Scripting Patterns

### Triage Agent Script
```bash
#!/bin/bash
# triage_agent.sh

gh issue list --limit 1 --json body > issue.json
cat issue.json | claude -p "Analyze this issue. If bug, verify. If feature, create plan." > triage_report.md
```

### Batch Processing
```bash
#!/bin/bash
# process_files.sh

for file in src/**/*.ts; do
    claude -p "Review $file for security issues" --max-turns 3 >> security_report.md
done
```

### CI/CD Integration
```yaml
# .github/workflows/review.yml
jobs:
  code-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Claude Review
        run: |
          claude -p "Review PR diff for issues" \
            --output-format json \
            --max-turns 10 > review.json
```

---

## Permission Modes

### Default (Interactive)
```bash
claude -p "Run tests"
# Will prompt for permission on each action
```

### Pre-Allowed Commands
```json
// settings.json
{
  "permissions": {
    "allow": ["Bash(npm run test:*)"],
    "ask": ["Bash(git push:*)"],
    "deny": ["Bash(rm:*)"]
  }
}
```

### Full Autonomy (Dangerous)
```bash
claude -p "Full refactor" --dangerously-skip-permissions
```

**⚠️ MANDATORY**: Only use in isolated environment (Docker, VM). Never on host machine.

---

## Sandboxed Execution

```bash
# Docker pattern
docker run -v $(pwd):/workspace claude-code \
    -p "Refactor authentication" \
    --dangerously-skip-permissions

# With network isolation
docker run --network none -v $(pwd):/workspace claude-code \
    -p "Analyze codebase" \
    --dangerously-skip-permissions
```

**Principle**: If agent hallucinates `rm -rf /` or installs malicious package, damage contained to disposable container.

---

## GitHub Actions Integration

```yaml
name: Claude Code Review
on:
  issue_comment:
    types: [created]

jobs:
  claude-code:
    if: contains(github.event.comment.body, '@.claude')
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          instruction: ${{ github.event.comment.body }}
```

**Pattern**:
1. Developer creates PR
2. Comments `@.claude review for security issues`
3. Claude Code spins up in Actions
4. Reviews code, posts findings as PR comment

---

## Cron Job Pattern

```bash
# crontab -e
0 2 * * * /path/to/nightly_audit.sh
```

```bash
#!/bin/bash
# nightly_audit.sh

cd /path/to/project
claude -p "Run security audit and generate report" \
    --max-turns 20 \
    --output-format json > /var/log/audit_$(date +%Y%m%d).json
```

---

## Output Handling

### Parse JSON Response
```bash
result=$(claude -p "List files to modify" --output-format json)
files=$(echo $result | jq -r '.response')
```

### Error Handling
```bash
if ! claude -p "Run tests" --max-turns 5; then
    echo "Claude execution failed"
    exit 1
fi
```

### Chaining Commands
```bash
# Analysis → Plan → Execute
claude -p "Analyze codebase" > analysis.md
claude -p "Create migration plan based on analysis.md" > plan.md
claude -p "Execute step 1 of plan.md" --max-turns 10
```

---

## Configuration for Headless

```json
// settings.json
{
  "headless": {
    "default_output_format": "json",
    "default_max_turns": 10,
    "timeout_ms": 300000
  },
  "permissions": {
    "defaultMode": "acceptEdits"
  }
}
```

---

## Anti-Patterns

### Unlimited Turns Without Timeout
```bash
# Bad: can run forever, burn tokens
claude -p "Fix all bugs"
```

**Better**: Set max-turns and timeout.

### Skip-Permissions on Host
```bash
# NEVER DO THIS
claude -p "Clean up" --dangerously-skip-permissions
```

**Always**: Use Docker/VM isolation.

### Ignoring Exit Codes
```bash
# Bad: continues even if Claude fails
claude -p "Run tests"
deploy.sh
```

**Better**: Check exit codes, handle failures.

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → AccessPoints, -p flag
- [[PRAC-ralph_pattern_execution]] → Headless in fresh context loops
- [[MECH-hooks_lifecycle_automation]] → Hooks in automated pipelines
