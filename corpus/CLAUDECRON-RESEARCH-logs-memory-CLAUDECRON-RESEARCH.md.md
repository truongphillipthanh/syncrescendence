# Claude Code Scheduled Dispatch Research (2026-02-09)

## Executive Summary

Claude Code can be scheduled to run automatically at specified intervals using native OS schedulers (launchd on macOS, cron on Linux, Task Scheduler on Windows). The key enabler is the `--print` (or `-p`) flag, which runs Claude non-interactively and outputs results to stdout/files.

**Status**: THREE production-ready approaches exist:
1. **Direct launchd + `claude -p`** (simplest, no deps)
2. **Claudecron MCP server** (most flexible, natural language task config)
3. **claude-code-scheduler plugin** (cross-platform, git worktree isolation)

---

## 1. Core Technology: The `--print` Flag

### Basic Mechanism

```bash
claude -p "Your prompt here" [options]
```

**Key Flags for Automation**:
- `-p, --print` — Run non-interactively, output to stdout
- `--output-format` — text (default), json, or stream-json
- `--allowedTools` — Auto-approve specific tools (Bash,Read,Edit, etc.)
- `--json-schema` — Validate structured output against JSON schema
- `--continue` — Continue previous conversation
- `--resume [session-id]` — Resume specific session
- `--append-system-prompt` — Add custom instructions
- `--model` — Override default model (e.g., --model opus)
- `--settings` — Load project-specific settings
- `--add-dir` — Grant access to additional directories

### Example: Non-Interactive Code Review

```bash
claude -p "Review this code for security issues" \
  --allowedTools "Read" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}'
```

This outputs structured JSON with the result in the `result` field and structured output in `structured_output` field (if schema provided).

---

## 2. DIRECT APPROACH: launchd + `claude -p`

### Simplest Production Pattern

**Setup (5 minutes, no external deps)**:

1. Create bash wrapper script at `~/.syncrescendence/scripts/run_claude_task.sh`:

```bash
#!/bin/bash
set -euo pipefail

# Source environment (API keys, PATH, etc.)
source ~/.syncrescendence/.env || true

# Run Claude non-interactively
LOG_FILE="/tmp/syncrescendence-claude-task-$(date +%Y%m%d-%H%M%S).log"

claude -p "$1" \
  --allowedTools "Bash,Read,Edit" \
  --output-format json \
  --add-dir "/Users/home/Desktop/syncrescendence" \
  > "$LOG_FILE" 2>&1

echo "Task completed. Log: $LOG_FILE"

# Optional: Upload log to webhook
# curl -X POST http://localhost:8888/dispatch \
#   -d "task=claude_task&log=$(cat $LOG_FILE | base64)" 2>/dev/null || true
```

2. Create launchd plist at `~/Library/LaunchAgents/com.syncrescendence.claude-task-executor.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.claude-task-executor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/home/.syncrescendence/scripts/run_claude_task.sh</string>
        <string>Check the status of all Linear issues in the SYN team and summarize blockers</string>
    </array>
    <key>StartInterval</key>
    <integer>3600</integer>
    <key>StandardOutPath</key>
    <string>/tmp/claude-task-executor.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/claude-task-executor.log</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
```

3. Bootstrap:

```bash
chmod +x /Users/home/.syncrescendence/scripts/run_claude_task.sh
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.claude-task-executor.plist
```

4. Check:

```bash
launchctl list | grep claude-task
# Manual trigger (for testing):
launchctl start com.syncrescendence.claude-task-executor
# View logs:
tail -f /tmp/claude-task-executor.log
```

**STRENGTHS**:
- Zero external dependencies (just Claude + launchd)
- Native macOS, persists across restarts
- Simple to debug and modify
- Timestamp logging built-in
- Can chain multiple tasks

**LIMITATIONS**:
- Task prompt hardcoded in plist (update plist to change task)
- No natural language task definition
- No built-in task queue or retry logic

---

## 3. MCP APPROACH: Claudecron

### Architecture

Claudecron is an MCP server that runs as a Claude Code plugin. It manages scheduled tasks via three mechanisms:

1. **Cron schedules** (e.g., "0 2 * * *" = 2 AM daily)
2. **File watches** (trigger on file change)
3. **Lifecycle events** (on session start, on workspace open, etc.)

Task types:
- **Bash tasks** — Execute shell commands (builds, tests, backups)
- **Subagent tasks** — Run AI prompts using Claude SDK (code review, analysis)

### Installation

1. Clone and build:

```bash
git clone https://github.com/phildougherty/claudecron
cd claudecron/mcp-server
npm install && npm run build
```

2. Add to Claude desktop config at `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "claudecron": {
      "command": "node",
      "args": ["/path/to/claudecron/mcp-server/dist/server.js"]
    }
  }
}
```

3. Restart Claude Code (or new session will auto-load).

### Usage in Claude Code

Simply ask Claude:

> "Create a claudecron task that checks Linear SYN team blockers every 6 hours and posts a summary to the webhook."

Claude uses the `claudecron_add_task` MCP tool to create it. Config auto-saves to `~/.claude/claudecron/tasks.db` (SQLite).

**STRENGTHS**:
- Tasks defined via natural language ("Claude, create a task that...")
- Persistent task store (SQLite DB)
- Supports both bash and AI prompts
- Built-in task history/logging
- File watch triggers for reactive automation
- Task lifecycle management (list, run, delete via MCP tools)

**LIMITATIONS**:
- Requires MCP server to run (adds complexity vs direct launchd)
- Tasks only execute while Claude session is open OR when explicitly triggered by external scheduler
- Still needs launchd wrapper to auto-start tasks if Claude isn't running

---

## 4. PLUGIN APPROACH: claude-code-scheduler

### Architecture

A Claude Code **plugin** (not MCP) that registers with platform-specific schedulers:
- **macOS** → launchd
- **Linux** → crontab
- **Windows** → Task Scheduler

Task execution isolated via git worktrees (each task gets its own branch, auto-merges on success).

### Installation

1. Clone and install:

```bash
git clone https://github.com/jshchnz/claude-code-scheduler
cd claude-code-scheduler
npm install
```

2. Install as Claude Code plugin (check project README for current method).

3. Create `~/.claude/schedules.json`:

```json
{
  "tasks": [
    {
      "id": "daily-health-check",
      "schedule": "0 8 * * *",
      "description": "Daily corpus health check",
      "prompt": "Run health checks on the Syncrescendence corpus and report any issues",
      "autonomousMode": true,
      "autoApproveTools": ["Bash", "Read"]
    }
  ]
}
```

### How It Works

1. Plugin reads `schedules.json` at startup
2. Registers tasks with launchd/cron/Task Scheduler
3. At scheduled time, launchd invokes: `claude -p 'your prompt' --dangerously-skip-permissions`
4. If `gitWorktree: true`, task runs in isolated branch, auto-merges on success
5. Logs saved to `~/.claude/logs/<task-id>.log`
6. One-time tasks auto-delete after execution

**STRENGTHS**:
- Cross-platform (same config works on macOS, Linux, Windows)
- Git isolation for risky autonomy (worktree + auto-merge)
- Persistent config (version-controlled in repo)
- Natural language task definition
- Audit trail in logs

---

## 5. COMPARISON TABLE

| Feature | Direct launchd | Claudecron MCP | claude-code-scheduler |
|---------|---|---|---|
| **Setup time** | 5 min | 15 min | 15 min |
| **External deps** | None | MCP server | Plugin system |
| **Task storage** | Plist (XML) | SQLite DB | JSON file |
| **Task definition** | Shell script arg | Natural lang | JSON + natural lang |
| **Cron scheduling** | Yes | Yes | Yes |
| **File watch triggers** | No | Yes | No |
| **Auto-retry** | No | Possible | No |
| **Git worktree isolation** | No | No | Yes |
| **Cross-platform** | launchd only | Likely | Yes |
| **Logging** | File-based | SQLite + file | JSON logs |
| **Persistent store** | None (plist) | SQLite | JSON file |
| **Security** | Explicit flags | Configurable | Flags + worktree |
| **Recommended for** | Simple tasks | Complex workflows | Production autonomy |

---

## 6. RECOMMENDED IMPLEMENTATION ROADMAP

### Phase 1: Immediate (This Week)

**Use: Direct launchd + `claude -p`**

Why: Zero dependencies, already installed, proven pattern in your system (qmd-update, corpus-health, etc.).

**Tasks to schedule**:
1. Hourly Linear status check → post blockers to webhook
2. Hourly ClickUp inbox → dispatch to Commander
3. 6-hourly Graphiti memory flush → push Neo4j snapshots
4. Daily corpus health audit → regenerate qmd index

### Phase 2: Consolidation (Week 2)

**Install: Claudecron MCP server** (if task definition becomes bottleneck)

Why: Allows "Claude, add a task that updates memory every hour" without plist edits.

### Phase 3: Advanced (Month 2)

**Consider: claude-code-scheduler plugin** (if autonomy/git safety becomes priority)

Why: Git worktree isolation means risky tasks can run safely.

---

## 7. PRACTICAL EXAMPLES

### Example 1: Hourly Linear Status Check

**File**: `~/.syncrescendence/scripts/run_claude_linear_check.sh`

```bash
#!/bin/bash
set -euo pipefail
source ~/.syncrescendence/.env || true

PROMPT="
Fetch all Linear issues in the SYN team with status 'In Progress' or 'Blocked'. 
For each:
1. List the issue ID, title, assignee
2. Note any blockers or dependencies
3. Estimate hours to unblock

Return as JSON with structure: {\"blockers\": [{\"issue\": \"SYN-XXX\", \"title\": \"...\", \"blocker\": \"...\", \"eta_hours\": N}]}
"

LOG_FILE="/tmp/syncrescendence-linear-check-$(date +%Y%m%d-%H%M%S).log"

claude -p "$PROMPT" \
  --allowedTools "Bash(curl *),Read" \
  --output-format json \
  > "$LOG_FILE" 2>&1

# Extract JSON and post to webhook
if command -v jq &> /dev/null; then
  RESULT=$(jq -r '.result' < "$LOG_FILE" 2>/dev/null || echo "")
  if [ -n "$RESULT" ]; then
    curl -X POST http://localhost:8888/dispatch \
      -H "Content-Type: application/json" \
      -d "{\"event\": \"linear-check\", \"payload\": $RESULT}" 2>/dev/null || true
  fi
fi
```

### Example 2: Using `--continue` for Multi-Step Tasks

```bash
#!/bin/bash
set -euo pipefail

# Step 1: Analyze
SESSION_ID=$(claude -p "Analyze the last 10 commits and identify patterns" \
  --output-format json | jq -r '.session_id')

# Step 2: Continue conversation
claude -p "Based on those patterns, suggest 3 improvements to the workflow" \
  --resume "$SESSION_ID" \
  --output-format json

# Step 3: Final summary
claude -p "Create a concise summary of the improvements" \
  --resume "$SESSION_ID" \
  --output-format text
```

### Example 3: Structured Output with Schema

```bash
claude -p "Extract all environment variables used in the codebase" \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "variables": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "used_in": {"type": "array", "items": {"type": "string"}},
            "required": {"type": "boolean"}
          }
        }
      }
    },
    "required": ["variables"]
  }' | jq '.structured_output.variables[] | select(.required) | .name'
```

---

## 8. SECURITY CONSIDERATIONS

### For Unattended Execution

1. **API Key Management**:
   ```bash
   chmod 600 ~/.syncrescendence/.env
   export ANTHROPIC_API_KEY=$(grep ANTHROPIC_API_KEY ~/.syncrescendence/.env | cut -d'=' -f2)
   ```

2. **Tool Approval**:
   - Use `--allowedTools` to whitelist only necessary tools
   - NEVER use `--dangerously-skip-permissions` in production
   - Example: `--allowedTools "Bash(curl *),Read"` only allows curl + file reads

3. **Workspace Trust**:
   - launchd spawns in background (no interactive prompt)
   - `-p` mode automatically skips workspace trust dialog
   - Ensure launchd script runs in trusted directory only

4. **Logging**:
   - All stdout/stderr captured to dated logs
   - Consider log rotation if high-frequency tasks
   - Logs may contain API responses—rotate/delete regularly

---

## 9. INTEGRATION WITH SYNCRESCENDENCE

### Current System State

Your system already has:
- 12 launchd services running (qmd-update, corpus-health, webhook-receiver, etc.)
- Template: `/Users/home/Library/LaunchAgents/com.syncrescendence.*.plist`
- Wrapper scripts: `/Users/home/.syncrescendence/scripts/run_*.sh`
- Log consolidation at `/tmp/syncrescendence-*.log`
- Webhook receiver at `http://localhost:8888/dispatch` (expects JSON)
- Linear API key at `~/.syncrescendence/.env`
- ClickUp API key at `~/.syncrescendence/.env`

### Proposed New Tasks

1. **claude-linear-check** (hourly) — Fetch blockers, post to webhook
2. **claude-clickup-sync** (hourly) — Sync ClickUp tasks to Linear/inbox
3. **claude-memory-flush** (6-hourly) — Push Graphiti memory snapshots
4. **claude-corpus-insight** (daily 6 AM) — Generate memory insights
5. **claude-session-review** (daily 9 PM) — Summarize daily sessions, commit changes

### MCP Availability in launchd Context

**Key limitation**: launchd background process ≠ Claude Code interactive session.

Therefore:
- `--allowedTools "Bash,Read,Edit"` work fine in launchd
- Linear MCP, Graphiti MCP, Qdrant MCP work IF those MCP servers are loaded
- **Current recommendation**: Use `Bash` + `curl` to call APIs directly (REST), not MCP tools

Example:
```bash
# This works in launchd:
claude -p "Fetch Linear SYN team issues" \
  --allowedTools "Bash(curl *)"

# This might NOT work in launchd (needs MCP server):
claude -p "Fetch Linear SYN team issues" \
  --allowedTools "linear__*"
```

If you want MCP tools in launchd, you'd need to:
1. Start a persistent Claude Code MCP gateway
2. Load MCP servers explicitly via `--mcp-config` flag
3. Use direct REST API calls instead

---

## 10. FINAL RECOMMENDATION

**Immediate action (Phase 1)**:

1. Create 5 launchd + `claude -p` tasks using the pattern in Example 1
2. Use REST APIs (curl) directly, not MCP tools
3. Post results to webhook at `localhost:8888/dispatch`
4. Test each one manually before scheduling

**Rationale**:
- Zero infrastructure changes
- Leverages existing launchd pattern (qmd-update, corpus-health)
- Avoids complexity of MCP servers in background processes
- Integrates with existing webhook receiver

**Validation**:
- All 5 tasks running → P0 DONE
- Webhook logs show incoming dispatch events → P1 DONE
- Commander autonomous loop handles dispatch → P2

---

## References

- [Claude Code Headless Docs](https://code.claude.com/docs/en/headless)
- [Claudecron GitHub](https://github.com/phildougherty/claudecron)
- [claude-code-scheduler GitHub](https://github.com/jshchnz/claude-code-scheduler)
- [SmartScope Claude Cron Guide](https://smartscope.blog/en/generative-ai/claude/claude-code-cron-automation-guide/)
- [runCLAUDErun - Native macOS Scheduler](https://runclauderun.com/)
- Your launchd template: `~/Library/LaunchAgents/com.syncrescendence.qmd-update.plist` (on Mac mini)
