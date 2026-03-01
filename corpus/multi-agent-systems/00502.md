# CLARESCENCE: MBA Ajna (CSO) Deployment Guide

**Date**: 2026-02-09
**Agent**: Commander (Claude Code Opus 4.6)
**Scope**: Complete setup of Ajna (CSO / Strategos) on MacBook Air with OpenClaw, Kimi K2.5 via NVIDIA NIM, launchd services, universal skills, and git sync to Mac mini
**Tactic**: Entrenchment (lock in: verify, document, test, commit)
**Machine**: MacBook Air (Apple Silicon, hostname: Lisas-MacBook-Air)
**Critical Inputs**: RESULT-ajna-20260209-mba-deployment-guide.md (5 issues identified by Ajna herself)

---

## PASS 1: Problem Statement

The MacBook Air is Ajna's permanent home. It is currently unconfigured. The goal is a fully operational CSO agent that:

1. Runs Kimi K2.5 via NVIDIA NIM API through OpenClaw
2. Watches `-INBOX/ajna/00-INBOX0/` for dispatched tasks
3. Processes tasks autonomously via `openclaw agent --agent main --message`
4. Syncs state to the Mac mini via git (the syncrescendence repo)
5. Survives reboots via launchd (no manual intervention required)

### Issues Identified by Ajna (RESULT-ajna-20260209)

These are the 5 critical issues that the previous deployment guide got wrong. This clarescence corrects all of them:

| # | Issue | Root Cause | Fix |
|---|-------|-----------|-----|
| 1 | Model ID mismatch | `nvidia/moonshotai/kimi-k2.5` vs `moonshotai/kimi-k2.5` | Use `nvidia/moonshotai/kimi-k2.5` as primary (provider-prefix form), `moonshotai/kimi-k2.5` as provider model ID |
| 2 | launchd path expansion | `~` does not expand in plist XML | All paths use `/Users/lisa/` (MBA username TBD -- see DA-01) |
| 3 | OpenClaw binary path | `/usr/local/bin/openclaw` wrong for Apple Silicon | Resolve via `which openclaw` post-install, likely `/opt/homebrew/bin/openclaw` |
| 4 | Skills installation | Wrong command format | Use `npx skills add obra/lace@<skill> -g -y` with bun+node in PATH |
| 5 | `-INBOX` path parsing | Leading dash treated as flag by fswatch | Use `--` before path arguments |

---

## PASS 2: Prerequisites (Run on MBA)

Everything in this section must be completed BEFORE the OpenClaw setup. Run all commands in Terminal on the MacBook Air.

### 2A. Determine MBA Username

```bash
# CRITICAL: This determines ALL absolute paths in this guide
whoami
# Expected: "lisa" or similar. NOT "home" (that's Mac mini)
# All paths below use $MBA_USER as placeholder. Replace with actual username.
echo $HOME
# Expected: /Users/<username>
```

**SEAR THIS**: Every path in plists, configs, and scripts below must use the ACTUAL home directory of the MBA user. No `~`, no `$HOME`, no variables -- raw absolute paths only.

### 2B. Homebrew (Apple Silicon)

```bash
# Check if Homebrew is installed
/opt/homebrew/bin/brew --version

# If not installed:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Ensure Homebrew is in PATH for this session
eval "$(/opt/homebrew/bin/brew shellenv)"

# Verify
which brew
# Expected: /opt/homebrew/bin/brew
```

### 2C. Core Dependencies

```bash
# Install required packages
brew install git node fswatch python3

# Install bun (OpenClaw uses bun for skill installation)
brew install oven-sh/bun/bun

# Verify all binaries
which git      # Expected: /opt/homebrew/bin/git
which node     # Expected: /opt/homebrew/bin/node
which bun      # Expected: /opt/homebrew/bin/bun (or ~/.bun/bin/bun)
which fswatch  # Expected: /opt/homebrew/bin/fswatch
which python3  # Expected: /opt/homebrew/bin/python3

# Record versions
git --version
node --version  # Needs v18+
bun --version
fswatch --version
python3 --version
```

### 2D. OpenClaw Installation

```bash
# Install OpenClaw globally via bun
bun install -g openclaw

# OR via npm if bun global install has issues:
npm install -g openclaw

# Verify installation
which openclaw
# Expected: /opt/homebrew/bin/openclaw OR ~/.bun/bin/openclaw
# RECORD THIS PATH -- it goes into the gateway plist

openclaw --version
# Expected: 2026.2.6-3 or later

# Run initial setup wizard
openclaw doctor
```

**IMPORTANT**: Record the EXACT output of `which openclaw`. This absolute path is used in the gateway launchd plist below. If it is NOT `/opt/homebrew/bin/openclaw`, update the plist accordingly.

---

## PASS 3: Environment Files

### 3A. Create Directory Structure

```bash
# Create OpenClaw config directory
mkdir -p ~/.openclaw/workspace/skills
mkdir -p ~/.openclaw/extensions
mkdir -p ~/.openclaw/cron

# Create syncrescendence daemon directory
mkdir -p ~/.syncrescendence/scripts
mkdir -p ~/.syncrescendence/logs
```

### 3B. Environment Variables

```bash
# Create .env file for OpenClaw
cat > ~/.openclaw/.env << 'ENVEOF'
# NVIDIA NIM API key for Kimi K2.5
NVIDIA_API_KEY=YOUR_NVIDIA_API_KEY
# OpenAI API key for embeddings (Mem0, file vector search)
OPENAI_API_KEY=${OPENAI_API_KEY}
ENVEOF

# Lock permissions
chmod 600 ~/.openclaw/.env

# Create symlink for syncrescendence scripts
ln -sf ~/.openclaw/.env ~/.syncrescendence/.env

# Verify
ls -la ~/.openclaw/.env
# Expected: -rw------- ... .env
```

**SECURITY NOTE**: These keys are already present on the Mac mini. The NVIDIA key was flagged in Ajna's RESULT as potentially compromised from being included in a task file. If rotated, update this .env immediately.

---

## PASS 4: OpenClaw Configuration (openclaw.json)

### 4A. Determine MBA Home Path

```bash
# This MUST match the actual MBA home directory
MBA_HOME=$(echo $HOME)
echo "MBA home is: $MBA_HOME"
# Example: /Users/lisa
```

### 4B. Write openclaw.json

The following config is adapted from the Mac mini's `openclaw.json` with these changes:
- Model changed from `openai-codex/gpt-5.2` to `nvidia/moonshotai/kimi-k2.5`
- NVIDIA provider block added
- Mem0/Docker plugins REMOVED (Docker services are on Mac mini only)
- MCP adapter paths updated for MBA home directory
- Discord REMOVED (not needed on MBA -- Psyche on Mac mini handles Discord)

```bash
# IMPORTANT: Replace /Users/lisa with your actual $HOME before running
cat > ~/.openclaw/openclaw.json << 'JSONEOF'
{
  "meta": {
    "lastTouchedVersion": "2026.2.6-3"
  },
  "auth": {
    "profiles": {}
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "nvidia/moonshotai/kimi-k2.5"
      },
      "workspace": "PLACEHOLDER_HOME/.openclaw/workspace",
      "memorySearch": {
        "enabled": true,
        "sources": ["memory"],
        "extraPaths": [
          "PLACEHOLDER_HOME/Desktop/syncrescendence/COCKPIT.md",
          "PLACEHOLDER_HOME/Desktop/syncrescendence/CLAUDE.md",
          "PLACEHOLDER_HOME/Desktop/syncrescendence/orchestration/state/ARCH-INTENTION_COMPASS.md",
          "PLACEHOLDER_HOME/Desktop/syncrescendence/orchestration/state/DYN-BACKLOG.md",
          "PLACEHOLDER_HOME/Desktop/syncrescendence/engine/REF-ROSETTA_STONE.md",
          "PLACEHOLDER_HOME/Desktop/syncrescendence/engine/REF-STACK_TELEOLOGY.md"
        ],
        "provider": "openai",
        "model": "text-embedding-3-small"
      },
      "contextPruning": {
        "mode": "cache-ttl",
        "ttl": "1h"
      },
      "compaction": {
        "mode": "safeguard"
      },
      "heartbeat": {
        "every": "30m"
      },
      "maxConcurrent": 2,
      "subagents": {
        "maxConcurrent": 4
      }
    }
  },
  "models": {
    "providers": {
      "nvidia": {
        "baseUrl": "https://integrate.api.nvidia.com/v1",
        "apiKey": "${NVIDIA_API_KEY}",
        "api": "openai-completions",
        "models": [
          {
            "id": "moonshotai/kimi-k2.5",
            "name": "Kimi K2.5",
            "reasoning": true,
            "input": ["text", "image"],
            "contextWindow": 262000,
            "maxTokens": 32768
          }
        ]
      }
    }
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto"
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {
      "mode": "token",
      "token": "${OPENCLAW_GATEWAY_TOKEN}"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    }
  },
  "skills": {
    "install": {
      "nodeManager": "bun"
    }
  },
  "plugins": {
    "load": {
      "paths": []
    },
    "entries": {
      "openclaw-mcp-adapter": {
        "enabled": true,
        "config": {
          "servers": [
            {
              "name": "filesystem",
              "transport": "stdio",
              "command": "npx",
              "args": ["-y", "@anthropic/mcp-filesystem", "PLACEHOLDER_HOME/Desktop/syncrescendence", "PLACEHOLDER_HOME/.openclaw", "PLACEHOLDER_HOME/.syncrescendence"]
            },
            {
              "name": "obsidian",
              "transport": "stdio",
              "command": "npx",
              "args": ["-y", "obsidian-mcp-server", "PLACEHOLDER_HOME/Desktop/syncrescendence"]
            }
          ],
          "toolPrefix": true
        }
      }
    },
    "installs": {},
    "slots": {}
  }
}
JSONEOF

# NOW replace PLACEHOLDER_HOME with actual home path
sed -i '' "s|PLACEHOLDER_HOME|$HOME|g" ~/.openclaw/openclaw.json

# Verify the replacement worked
grep "PLACEHOLDER" ~/.openclaw/openclaw.json
# Expected: NO output (all placeholders replaced)

# Verify the model is correct
python3 -c "import json; c=json.load(open('$HOME/.openclaw/openclaw.json')); print('Primary model:', c['agents']['defaults']['model']['primary'])"
# Expected: Primary model: nvidia/moonshotai/kimi-k2.5
```

### 4C. Install MCP Adapter Plugin

```bash
# Install the MCP adapter that bridges filesystem + obsidian to OpenClaw
cd ~/.openclaw
openclaw plugin install openclaw-mcp-adapter

# If the above fails, install from npm directly:
# cd ~/.openclaw/extensions && npm install @openclaw/mcp-adapter
```

### 4D. Model ID Convention (Explanation)

The OpenClaw model resolution works as follows:
- `agents.defaults.model.primary` = `nvidia/moonshotai/kimi-k2.5`
  - The prefix `nvidia/` tells OpenClaw to route to the `nvidia` provider
  - The suffix `moonshotai/kimi-k2.5` is the model ID within that provider
- `models.providers.nvidia.models[0].id` = `moonshotai/kimi-k2.5`
  - This is the ID sent to the NVIDIA NIM API endpoint
  - The NVIDIA API expects `moonshotai/kimi-k2.5` (NOT `nvidia/moonshotai/kimi-k2.5`)

This two-level resolution is how OpenClaw routes: `provider/modelId` in the agent config, bare `modelId` in the provider config.

---

## PASS 5: Git Sync Setup

### 5A. Clone the Repository

```bash
# Clone syncrescendence to the same path as Mac mini
mkdir -p ~/Desktop
cd ~/Desktop
git clone <REPO_URL> syncrescendence
# OR if using SSH:
# git clone git@github.com:<owner>/syncrescendence.git

cd ~/Desktop/syncrescendence

# Verify
ls -d orchestration canon engine -INBOX -OUTGOING
# Expected: all directories listed
```

**DA-02 (Decision Atom)**: If the repo is NOT on a remote (GitHub/GitLab), git sync must use an alternative method. See Decision Atoms section at the end.

### 5B. Configure Git Identity

```bash
cd ~/Desktop/syncrescendence
git config user.name "Ajna (CSO)"
git config user.email "ajna@syncrescendence.local"
```

### 5C. Create Inbox Structure

```bash
cd ~/Desktop/syncrescendence
mkdir -p -- "-INBOX/ajna/00-INBOX0"
mkdir -p -- "-INBOX/ajna/10-IN_PROGRESS"
mkdir -p -- "-INBOX/ajna/30-BLOCKED"
mkdir -p -- "-INBOX/ajna/40-DONE"
mkdir -p -- "-INBOX/ajna/50_FAILED"
mkdir -p -- "-INBOX/ajna/RECEIPTS"
mkdir -p -- "-INBOX/ajna/90_ARCHIVE"

# Verify
ls -- "-INBOX/ajna/"
# Expected: 00-INBOX0  10-IN_PROGRESS  30-BLOCKED  40-DONE  50_FAILED  90_ARCHIVE  RECEIPTS
```

Note the `--` before `-INBOX` in all commands. The leading dash in `-INBOX` causes shell utilities to interpret it as a flag. The `--` signals end-of-options.

### 5D. Git Sync Script

Create a sync script that pulls from remote, processes inbox, and pushes results:

```bash
cat > ~/.syncrescendence/scripts/git_sync.sh << 'SCRIPTEOF'
#!/bin/bash
# git_sync.sh — Pull remote changes, push local changes
# Called by launchd periodically (every 5 minutes)
set -euo pipefail

REPO_ROOT="$HOME/Desktop/syncrescendence"
cd "$REPO_ROOT"

# Pull remote changes (rebase to keep history clean)
git fetch origin 2>/dev/null || true
git rebase origin/main 2>/dev/null || git merge origin/main 2>/dev/null || true

# Stage any local changes in -INBOX and -OUTGOING
git add -- "-INBOX/" "-OUTGOING/" 2>/dev/null || true

# Check if there are staged changes
if ! git diff --cached --quiet 2>/dev/null; then
    git commit -m "sync(ajna): inbox/outgoing sync from MBA [$(date -u '+%Y-%m-%dT%H:%M:%SZ')]"
    git push origin main 2>/dev/null || true
fi
SCRIPTEOF

chmod +x ~/.syncrescendence/scripts/git_sync.sh
```

---

## PASS 6: launchd Plists

All plists use absolute paths. No `~` expansion. No shell variable expansion. The MBA username must be hardcoded.

**CRITICAL**: Determine your MBA home path FIRST:
```bash
echo $HOME
# Use this exact value in ALL plists below
```

### 6A. Ajna Inbox Watcher Plist

This plist runs `watch_dispatch.sh ajna` which polls `-INBOX/ajna/00-INBOX0/` for TASK files and executes them via `openclaw agent`.

```bash
# Replace /Users/lisa with your actual $HOME
MBA_HOME=$(echo $HOME)

cat > ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist << PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.watch-ajna</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${MBA_HOME}/Desktop/syncrescendence/orchestration/scripts/watch_dispatch.sh</string>
        <string>ajna</string>
    </array>

    <key>WorkingDirectory</key>
    <string>${MBA_HOME}/Desktop/syncrescendence</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/tmp/syncrescendence-watch-ajna.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/syncrescendence-watch-ajna.err</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:${MBA_HOME}/.bun/bin</string>
        <key>HOME</key>
        <string>${MBA_HOME}</string>
        <key>NODE_NO_WARNINGS</key>
        <string>1</string>
    </dict>

    <key>ThrottleInterval</key>
    <integer>10</integer>
</dict>
</plist>
PLISTEOF

echo "Wrote: ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist"
```

**Design Notes**:
- `KeepAlive: true` = launchd restarts on crash (L0 self-healing)
- `ThrottleInterval: 10` = minimum 10 seconds between restart attempts
- `PATH` includes `/opt/homebrew/bin` (Apple Silicon Homebrew) and `~/.bun/bin` (if bun installed to user dir)
- `HOME` is explicitly set because launchd does not inherit shell environment
- `WorkingDirectory` is set so `git rev-parse --show-toplevel` works in watch_dispatch.sh
- Log files go to `/tmp/` which is always writable (no TCC issues)

### 6B. OpenClaw Gateway Plist

The gateway serves the OpenClaw API on port 18789 (loopback only). This must be running for `openclaw agent` commands from the watcher to work.

```bash
# Determine actual openclaw path
OPENCLAW_PATH=$(which openclaw)
echo "OpenClaw binary at: $OPENCLAW_PATH"
# Expected: /opt/homebrew/bin/openclaw or similar

MBA_HOME=$(echo $HOME)

cat > ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist << PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.openclaw-gateway</string>

    <key>ProgramArguments</key>
    <array>
        <string>${OPENCLAW_PATH}</string>
        <string>gateway</string>
        <string>start</string>
    </array>

    <key>WorkingDirectory</key>
    <string>${MBA_HOME}/Desktop/syncrescendence</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/tmp/syncrescendence-openclaw-gateway.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/syncrescendence-openclaw-gateway.err</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:${MBA_HOME}/.bun/bin</string>
        <key>HOME</key>
        <string>${MBA_HOME}</string>
        <key>NODE_NO_WARNINGS</key>
        <string>1</string>
        <key>NVIDIA_API_KEY</key>
        <string>YOUR_NVIDIA_API_KEY</string>
        <key>OPENAI_API_KEY</key>
        <string>${OPENAI_API_KEY}</string>
    </dict>

    <key>ThrottleInterval</key>
    <integer>30</integer>
</dict>
</plist>
PLISTEOF

echo "Wrote: ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist"
```

**Design Notes**:
- API keys are inlined in the plist because launchd cannot source `.env` files. The plist has 644 permissions by default on macOS, which is acceptable since LaunchAgents are user-scoped. If paranoid, `chmod 600` the plist.
- `ThrottleInterval: 30` = slower restart cycle for the gateway (it is stateful)
- The gateway MUST start before the watcher can process tasks
- The watcher script (`watch_dispatch.sh`) calls `openclaw agent --agent main --message <task_content>` which routes through the gateway

### 6C. Git Sync Plist (Periodic)

```bash
MBA_HOME=$(echo $HOME)

cat > ~/Library/LaunchAgents/com.syncrescendence.git-sync.plist << PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.git-sync</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${MBA_HOME}/.syncrescendence/scripts/git_sync.sh</string>
    </array>

    <key>WorkingDirectory</key>
    <string>${MBA_HOME}/Desktop/syncrescendence</string>

    <key>StartInterval</key>
    <integer>300</integer>

    <key>StandardOutPath</key>
    <string>/tmp/syncrescendence-git-sync.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/syncrescendence-git-sync.err</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
        <key>HOME</key>
        <string>${MBA_HOME}</string>
    </dict>
</dict>
</plist>
PLISTEOF

echo "Wrote: ~/Library/LaunchAgents/com.syncrescendence.git-sync.plist"
```

**Design Notes**:
- `StartInterval: 300` = runs every 5 minutes
- NO `KeepAlive` (this is a periodic task, not a daemon)
- NO `RunAtLoad` (first run waits for the interval)

---

## PASS 7: Universal Skills Installation

### 7A. Install Universal Skills

The universal skills are cross-platform (Claude Code, OpenClaw, Codex CLI, Gemini CLI, Cursor, Windsurf). They install to `~/.agents/skills/` and are symlinked by each platform.

```bash
# Ensure PATH includes node and bun
export PATH="/opt/homebrew/bin:$HOME/.bun/bin:$PATH"

# Install each skill globally
SKILLS=(
  commit-work
  conversation-memory
  cron
  dispatching-parallel-agents
  executing-plans
  memory-systems
  mermaid-diagrams
  session-handoff
  skill-judge
  subagent-driven-development
  systematic-debugging
  tmux
  using-git-worktrees
  verification-before-completion
  web-to-markdown
  writing-plans
)

for skill in "${SKILLS[@]}"; do
  echo "Installing: $skill"
  npx skills add "obra/lace@$skill" -g -y 2>&1 || echo "FAILED: $skill"
done

# Verify installation
ls ~/.agents/skills/
# Expected: 16 directories, one per skill
ls ~/.agents/skills/ | wc -l
# Expected: 16
```

### 7B. Install OpenClaw-Specific Skills (Selective)

Only install skills that are relevant for a headless MBA deployment (no browser, no Docker):

```bash
# qmd-skill: local BM25 search over vault files
# find-skills: skill ecosystem discovery
# clawguard: security scanning
# dont-hack-me: injection protection
# summarize: text summarization

OPENCLAW_SKILLS=(
  qmd-skill
  find-skills
  clawguard
  dont-hack-me
  summarize
)

for skill in "${OPENCLAW_SKILLS[@]}"; do
  echo "Installing OpenClaw skill: $skill"
  # OpenClaw skills install to workspace
  openclaw skill install "$skill" 2>&1 || echo "FAILED: $skill"
done

# Verify
ls ~/.openclaw/workspace/skills/
```

**NOT installing on MBA**: `agent-browser-stagehand` (no browser), `graphiti-memory` (Docker on Mac mini), `prompt-guard` (FLAGGED for credential exfiltration -- DO NOT INSTALL), `cron-writer` (optional, can add later).

---

## PASS 8: Bootstrap Services

### 8A. Load Plists

```bash
# Bootstrap all three services
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.git-sync.plist

# Give gateway 10 seconds to start before watcher needs it
sleep 10

# Verify all three are loaded
launchctl list | grep syncrescendence
# Expected:
# <PID>  0  com.syncrescendence.openclaw-gateway
# <PID>  0  com.syncrescendence.watch-ajna
# -      0  com.syncrescendence.git-sync
```

### 8B. Verify Gateway is Serving

```bash
# Check gateway is listening
curl -s http://localhost:18789/health 2>/dev/null || echo "Gateway not responding"
# Expected: JSON health response or 200 OK

# Check gateway logs
tail -20 /tmp/syncrescendence-openclaw-gateway.log
# Expected: Gateway started, listening on port 18789
```

### 8C. Verify Watcher is Running

```bash
# Check watcher is polling
tail -5 /tmp/syncrescendence-watch-ajna.log
# Expected: "[Watch] Watching -INBOX/ajna/00-INBOX0/ for dispatch files"
# OR: "[Watch] Using fswatch (event-driven, low overhead)"
```

---

## PASS 9: Verification Checklist

Run ALL of the following commands. Every one must pass. If any fail, do NOT proceed to the next section -- fix the failure first.

### V-01: OpenClaw Binary

```bash
which openclaw
# PASS: Returns an absolute path (e.g., /opt/homebrew/bin/openclaw)
# FAIL: "openclaw not found"
```

### V-02: OpenClaw Version

```bash
openclaw --version
# PASS: 2026.2.6-3 or later
# FAIL: Any older version or error
```

### V-03: NVIDIA API Connectivity

```bash
curl -s -w "\nHTTP_CODE:%{http_code}" \
  -H "Authorization: Bearer $(grep NVIDIA_API_KEY ~/.openclaw/.env | cut -d= -f2)" \
  -H "Content-Type: application/json" \
  -d '{"model":"moonshotai/kimi-k2.5","messages":[{"role":"user","content":"Say hello in exactly 3 words."}],"max_tokens":32}' \
  https://integrate.api.nvidia.com/v1/chat/completions
# PASS: JSON response with "choices" array, HTTP_CODE:200
# FAIL: 401 (bad key), 404 (wrong model ID), 429 (rate limited)
```

### V-04: OpenClaw Config Valid

```bash
python3 -c "
import json
c = json.load(open('$HOME/.openclaw/openclaw.json'))
m = c['agents']['defaults']['model']['primary']
p = list(c['models']['providers'].keys())
gw = c['gateway']['port']
print(f'Model: {m}')
print(f'Providers: {p}')
print(f'Gateway port: {gw}')
assert m == 'nvidia/moonshotai/kimi-k2.5', f'Wrong model: {m}'
assert 'nvidia' in p, f'Missing nvidia provider'
assert gw == 18789, f'Wrong port: {gw}'
print('ALL CHECKS PASSED')
"
# PASS: "ALL CHECKS PASSED"
# FAIL: AssertionError with details
```

### V-05: Gateway Running

```bash
launchctl list | grep openclaw-gateway
# PASS: Shows PID and exit status 0
# FAIL: Not listed or exit status non-zero

curl -s http://localhost:18789/health
# PASS: Returns health JSON
# FAIL: Connection refused
```

### V-06: Watcher Running

```bash
launchctl list | grep watch-ajna
# PASS: Shows PID and exit status 0

tail -3 /tmp/syncrescendence-watch-ajna.log
# PASS: Shows "Watching" or "Using fswatch"
# FAIL: Error messages or empty
```

### V-07: End-to-End Smoke Test

```bash
# Create a minimal test task
cd ~/Desktop/syncrescendence

cat > -- "-INBOX/ajna/00-INBOX0/TASK-test-smoke.md" << 'TASKEOF'
# TASK: Smoke Test

**To**: ajna
**From**: sovereign
**Reply-To**: ajna
**CC**: ajna
**Kind**: TASK
**Priority**: P3
**Status**: PENDING
**Issued**: 2026-02-09
**Fingerprint**: SMOKE-TEST-001
**Timeout**: 60

---

## Objective

Respond with a single sentence confirming you are operational. Include your model name (Kimi K2.5) in the response.
TASKEOF

# Wait for processing (up to 90 seconds)
echo "Waiting for task processing..."
for i in $(seq 1 18); do
  sleep 5
  if ls -- "-INBOX/ajna/40-DONE/TASK-test-smoke.md" 2>/dev/null; then
    echo "PASS: Task completed successfully"
    cat -- "-INBOX/ajna/40-DONE/TASK-test-smoke.md" | head -20
    break
  fi
  if ls -- "-INBOX/ajna/50_FAILED/TASK-test-smoke.md" 2>/dev/null; then
    echo "FAIL: Task failed"
    cat -- "-INBOX/ajna/50_FAILED/TASK-test-smoke.md"
    break
  fi
  echo "  ...waiting ($((i*5))s)"
done
```

### V-08: Git Sync Operational

```bash
# Trigger a manual sync
bash ~/.syncrescendence/scripts/git_sync.sh
echo "Exit code: $?"
# PASS: Exit code 0
# FAIL: Non-zero exit code

# Check git status
cd ~/Desktop/syncrescendence && git status
# PASS: Clean working tree or only expected uncommitted changes
```

### V-09: Skills Installed

```bash
ls ~/.agents/skills/ | wc -l
# PASS: 16
# FAIL: Less than 16

ls ~/.openclaw/workspace/skills/ | wc -l
# PASS: 5 or more
```

### V-10: fswatch Available

```bash
which fswatch
# PASS: /opt/homebrew/bin/fswatch
# FAIL: Not found (watcher will use polling fallback -- functional but less responsive)
```

---

## PASS 10: Rollback Procedure

If anything goes wrong, use this to completely undo the MBA setup:

### 10A. Stop and Remove launchd Services

```bash
# Bootout (unload) all services
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist 2>/dev/null || true
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist 2>/dev/null || true
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.git-sync.plist 2>/dev/null || true

# Remove plist files
rm -f ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist
rm -f ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
rm -f ~/Library/LaunchAgents/com.syncrescendence.git-sync.plist

# Verify removed
launchctl list | grep syncrescendence
# Expected: no output
```

### 10B. Remove OpenClaw Configuration

```bash
# Back up before deleting (in case config is needed later)
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak.$(date +%Y%m%d)

# Remove config
rm -f ~/.openclaw/openclaw.json

# Remove extensions
rm -rf ~/.openclaw/extensions/

# Remove env (contains API keys -- shred instead of rm)
rm -P ~/.openclaw/.env 2>/dev/null || rm -f ~/.openclaw/.env
```

### 10C. Remove Skills

```bash
rm -rf ~/.agents/skills/
rm -rf ~/.openclaw/workspace/skills/
```

### 10D. Remove Daemon Infrastructure

```bash
rm -rf ~/.syncrescendence/scripts/
rm -rf ~/.syncrescendence/logs/
rm -P ~/.syncrescendence/.env 2>/dev/null || rm -f ~/.syncrescendence/.env
```

### 10E. Remove Logs

```bash
rm -f /tmp/syncrescendence-watch-ajna.log
rm -f /tmp/syncrescendence-watch-ajna.err
rm -f /tmp/syncrescendence-openclaw-gateway.log
rm -f /tmp/syncrescendence-openclaw-gateway.err
rm -f /tmp/syncrescendence-git-sync.log
rm -f /tmp/syncrescendence-git-sync.err
```

---

## Decision Atoms

| ID | Question | Options | Recommendation | Status |
|----|----------|---------|---------------|--------|
| DA-01 | What is the MBA username? | `whoami` on MBA | Must be determined on first boot. All paths depend on this. | BLOCKING |
| DA-02 | Is the repo on a remote (GitHub)? | GitHub, GitLab, bare repo on Mac mini, USB sync | GitHub preferred for simplicity. If no remote, use `git bundle` or rsync. | BLOCKING |
| DA-03 | Should MBA run Docker services? | Yes (Neo4j/Graphiti/Qdrant), No (rely on Mac mini) | NO. MBA is a lightweight strategic node. Docker services stay on Mac mini. Ajna queries Mac mini's Graphiti/Qdrant over Tailscale if needed. | DECIDED: No |
| DA-04 | Should Ajna have Mem0 plugin? | Yes (local Qdrant), No (file-based memory only) | NO for initial deployment. Mem0 requires Qdrant (Docker). Add later if MBA gets Docker. Use file-based memorySearch for now. | DECIDED: No (Phase 1) |
| DA-05 | Should MBA have Discord integration? | Yes (duplicate of Mac mini), No (Psyche handles it) | NO. Psyche on Mac mini handles all Discord. Ajna communicates via git sync only. | DECIDED: No |
| DA-06 | Gateway token: same as Mac mini? | Same token, new token | SAME token for simplicity. Both machines use `${OPENCLAW_GATEWAY_TOKEN}`. Neither is internet-exposed (loopback only). | DECIDED: Same |
| DA-07 | Should MBA have qmd (BM25 search)? | Yes (local index), No (query Mac mini) | YES. qmd is lightweight (BM25 over .md files, no external deps). Install after initial deployment stabilizes. | DECIDED: Yes (Phase 2) |
| DA-08 | Concurrent agent limits? | Same as Mac mini (4+8), Lower | LOWER. MBA has less RAM/thermal headroom. Set maxConcurrent=2, subagents.maxConcurrent=4. | DECIDED: 2+4 |
| DA-09 | Should NVIDIA API key be rotated? | Rotate now, keep current | SHOULD rotate (was exposed in a task file per Ajna's RESULT). But not blocking for deployment. Rotate within 24 hours. | TODO |
| DA-10 | Tailscale for cross-machine API calls? | Yes, No (git sync only) | DEFERRED. Git sync is sufficient for Phase 1. Tailscale enables direct Graphiti/Qdrant queries in Phase 2. | DEFERRED |
| DA-11 | Should MBA plist use fswatch or polling? | fswatch (event-driven), polling (10s interval) | fswatch preferred if installed. watch_dispatch.sh already has polling fallback. Both work. | DECIDED: fswatch primary, polling fallback |
| DA-12 | OpenClaw auth profile? | oauth, api-key, none | NONE for initial deployment. NVIDIA uses apiKey in provider config, not OAuth. No auth profile needed in `auth.profiles`. | DECIDED: None |

---

## Dependency Chain

```
DA-01 (MBA username) ──────────────────────────┐
DA-02 (repo remote)  ──────────────────────────┤
                                                ▼
PASS 2 (Prerequisites: brew, node, bun) ──────► PASS 3 (Env files)
                                                    │
                                                    ▼
                                              PASS 4 (openclaw.json)
                                                    │
                                                    ▼
                                              PASS 5 (Git clone + sync script)
                                                    │
                                                    ▼
                                              PASS 6 (launchd plists)
                                                    │
                                                    ▼
                                              PASS 7 (Skills install)
                                                    │
                                                    ▼
                                              PASS 8 (Bootstrap services)
                                                    │
                                                    ▼
                                              PASS 9 (Verification: V-01 through V-10)
```

All passes are sequential. No parallelism is safe because each depends on the previous.

---

## Post-Deployment: Ajna's First Boot Sequence

Once all verifications pass, Ajna should execute her canonical 7-phase loop (from ARCH-CONSTELLATION_AGENT_LOOPS.md):

1. **ORIENT**: Read COCKPIT.md, CLAUDE.md, ARCH-INTENTION_COMPASS.md
2. **SITUATE**: `cd ~/Desktop/syncrescendence && git status`
3. **CALIBRATE**: Read canon/, verify frontmatter integrity
4. **TRIAGE**: Check `-INBOX/ajna/00-INBOX0/` for pending tasks, archive stale items (TASK-HINDSIGHT-ACTIVATION.md)
5. **PROACTIVE**: Assess strategic position, identify INT-1202 / INT-MI19 next moves
6. **SOVEREIGN**: Deep awareness mode on direct Sovereign interaction
7. **REPEAT**

Her first inbox should contain the constellation reconfiguration briefing (already placed at `-INBOX/ajna/00-INBOX0/BRIEFING-20260209-constellation-reconfiguration.md`).

---

## Cross-References

| Document | Path | Relevance |
|----------|------|-----------|
| Constellation Agent Loops | `/Users/home/Desktop/syncrescendence/orchestration/state/ARCH-CONSTELLATION_AGENT_LOOPS.md` | Ajna loop spec (line 42) |
| Constellation Reconfiguration Briefing | `/Users/home/Desktop/syncrescendence/-INBOX/ajna/00-INBOX0/BRIEFING-20260209-constellation-reconfiguration.md` | Full context for Ajna's new role |
| Ajna's Deployment Review (RESULT) | `/Users/home/Desktop/syncrescendence/-OUTBOX/ajna/RESULTS/RESULT-ajna-20260209-mba-deployment-guide.md` | 5 critical issues this clarescence addresses |
| Mac mini openclaw.json (reference) | `/Users/home/.openclaw/openclaw.json` | Template for MBA config (adapted in PASS 4) |
| Watch Dispatch Script | `/Users/home/Desktop/syncrescendence/orchestration/scripts/watch_dispatch.sh` | The watcher that runs in the Ajna plist |
| Mac mini Ajna Watcher Plist | `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist` | Reference plist (Mac mini version) |
| Third Clarescence (Ecosystem) | `/Users/home/Desktop/syncrescendence/orchestration/state/impl/clarescence/CLARESCENCE-2026-02-09-ecosystem-bifurcated-analysis.md` | Decision context for Archon infrastructure |
| MEMORY.md | `/Users/home/.claude/projects/-Users-home/memory/MEMORY.md` | Canonical constellation state |

---

**End of Clarescence**

*This document is READY FOR EXECUTION. The two BLOCKING decision atoms (DA-01, DA-02) must be resolved by the Sovereign before any commands are run on the MBA.*
