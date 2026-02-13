#!/usr/bin/env bash
# mba-commander-init.sh — One-shot initialization for Commander on MacBook Air
# Run this ONCE on MBA to configure Claude Code MCP servers + aliases.
#
# Prerequisites (already done per RESULT-mba-commander-20260211):
#   - Claude Code installed at /opt/homebrew/bin/claude
#   - 16 universal skills installed
#   - 5 hooks configured in .claude/settings.json
#   - OpenClaw gateway running on port 18789
#   - Git sync operational
#
# This script adds:
#   1. Project-scoped MCP servers to ~/.claude.json
#   2. mba-cockpit alias to ~/.zshrc
#   3. Verification checks
#
# Usage:
#   cd ~/Desktop/syncrescendence
#   bash 00-ORCHESTRATION/scripts/mba-commander-init.sh

set -euo pipefail

echo "=== MBA Commander Initialization ==="
echo "Machine: $(hostname)"
echo "User:    $(whoami)"
echo "Home:    $HOME"
echo "Date:    $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo ""

REPO="$HOME/Desktop/syncrescendence"
CLAUDE_JSON="$HOME/.claude.json"
ENV_FILE="$HOME/.syncrescendence/.env"

# ── Preflight checks ─────────────────────────────────────────────────────
echo "[1/6] Preflight checks..."

if [[ ! -x "$(which claude 2>/dev/null)" ]]; then
    echo "FAIL: claude not found in PATH"
    exit 1
fi
echo "  Claude Code: $(which claude)"

if [[ ! -d "$REPO" ]]; then
    echo "FAIL: Repository not found at $REPO"
    exit 1
fi
echo "  Repository: $REPO"

if [[ ! -f "$ENV_FILE" ]]; then
    echo "WARN: $ENV_FILE not found. MCP servers requiring API keys may fail."
fi

# ── Source API keys from .env ─────────────────────────────────────────────
echo ""
echo "[2/6] Loading API keys from $ENV_FILE..."

LINEAR_TOKEN=""
CLICKUP_TOKEN=""
CLICKUP_TEAM=""

if [[ -f "$ENV_FILE" ]]; then
    LINEAR_TOKEN=$(grep -E '^LINEAR_API_KEY=' "$ENV_FILE" 2>/dev/null | cut -d= -f2- || true)
    CLICKUP_TOKEN=$(grep -E '^CLICKUP_API_KEY=' "$ENV_FILE" 2>/dev/null | cut -d= -f2- || true)
    CLICKUP_TEAM=$(grep -E '^CLICKUP_TEAM_ID=' "$ENV_FILE" 2>/dev/null | cut -d= -f2- || true)
fi

# Fallback for ClickUp team ID (known constant)
CLICKUP_TEAM="${CLICKUP_TEAM:-9013504382}"

echo "  LINEAR_API_KEY: ${LINEAR_TOKEN:+present (${#LINEAR_TOKEN} chars)}${LINEAR_TOKEN:-MISSING}"
echo "  CLICKUP_API_KEY: ${CLICKUP_TOKEN:+present (${#CLICKUP_TOKEN} chars)}${CLICKUP_TOKEN:-MISSING}"

# ── Write MCP configuration ──────────────────────────────────────────────
echo ""
echo "[3/6] Configuring MCP servers in ~/.claude.json..."

# Export keys for Python to read via os.environ
export LINEAR_TOKEN="${LINEAR_TOKEN:-}"
export CLICKUP_TOKEN="${CLICKUP_TOKEN:-}"
export CLICKUP_TEAM="${CLICKUP_TEAM:-9013504382}"

# Use python3 for safe JSON manipulation (jq may not be installed)
python3 << 'PYEOF'
import json
import os
import sys

claude_json_path = os.path.expanduser("~/.claude.json")
home = os.path.expanduser("~")
repo = f"{home}/Desktop/syncrescendence"

# Read existing config
try:
    with open(claude_json_path, 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {}
except json.JSONDecodeError:
    print(f"ERROR: {claude_json_path} is malformed JSON. Back up and fix manually.")
    sys.exit(1)

# Ensure projects key exists
if 'projects' not in config:
    config['projects'] = {}

project_key = repo
if project_key not in config['projects']:
    config['projects'][project_key] = {}

project = config['projects'][project_key]

# Ensure required keys
project.setdefault('allowedTools', [])
project.setdefault('mcpContextUris', [])
project.setdefault('enabledMcpjsonServers', [])
project.setdefault('disabledMcpjsonServers', [])
project.setdefault('hasTrustDialogAccepted', True)
project.setdefault('hasCompletedProjectOnboarding', True)

# Define MBA-appropriate MCP servers
# NOTE: No Graphiti (requires Neo4j Docker on Mac mini)
# NOTE: No Qdrant (requires Docker on Mac mini)
# NOTE: No Chrome DevTools / Playwright (MBA is lightweight)
mcp_servers = {
    "obsidian": {
        "type": "stdio",
        "command": "npx",
        "args": [
            "@mauricio.wolff/mcp-obsidian@latest",
            repo
        ],
        "env": {}
    },
    "filesystem": {
        "type": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            repo,
            f"{home}/Documents"
        ],
        "env": {}
    },
    "gemini-mcp": {
        "type": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "gemini-mcp-tool"
        ],
        "env": {}
    }
}

# Add Linear if token available
linear_token = os.environ.get("LINEAR_TOKEN", "")
if linear_token:
    mcp_servers["linear"] = {
        "type": "http",
        "url": "https://mcp.linear.app/mcp",
        "headers": {
            "Authorization": f"Bearer {linear_token}"
        }
    }

# Add ClickUp if token available
clickup_token = os.environ.get("CLICKUP_TOKEN", "")
clickup_team = os.environ.get("CLICKUP_TEAM", "9013504382")
if clickup_token:
    mcp_servers["clickup"] = {
        "type": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "clickup-mcp-server"
        ],
        "env": {
            "CLICKUP_TEAM_ID": clickup_team,
            "CLICKUP_API_TOKEN": clickup_token
        }
    }

project['mcpServers'] = mcp_servers

# Write back
with open(claude_json_path, 'w') as f:
    json.dump(config, f, indent=2)

server_names = list(mcp_servers.keys())
print(f"  Configured {len(server_names)} MCP servers: {', '.join(server_names)}")
print(f"  Project key: {project_key}")
PYEOF

# ── Verify python script worked ──────────────────────────────────────────
if [[ $? -ne 0 ]]; then
    echo "FAIL: MCP configuration failed"
    exit 1
fi

# ── Install mba-cockpit alias ────────────────────────────────────────────
echo ""
echo "[4/6] Installing mba-cockpit alias..."

MBA_COCKPIT_SCRIPT="$REPO/00-ORCHESTRATION/scripts/mba-cockpit.sh"
if [[ -f "$MBA_COCKPIT_SCRIPT" ]]; then
    chmod +x "$MBA_COCKPIT_SCRIPT"

    # Add alias to .zshrc if not already present
    if ! grep -q 'alias mba-cockpit' "$HOME/.zshrc" 2>/dev/null; then
        echo "" >> "$HOME/.zshrc"
        echo "# Syncrescendence MBA Cockpit" >> "$HOME/.zshrc"
        echo "alias mba-cockpit='bash $MBA_COCKPIT_SCRIPT'" >> "$HOME/.zshrc"
        echo "  Added alias: mba-cockpit → $MBA_COCKPIT_SCRIPT"
    else
        echo "  Alias already exists in .zshrc"
    fi
else
    echo "  WARN: $MBA_COCKPIT_SCRIPT not found. Alias not set."
fi

# ── Create Commander-specific memory ──────────────────────────────────────
echo ""
echo "[5/6] Creating Commander memory directory..."

mkdir -p "$HOME/.claude/projects/-Users-$(whoami)-Desktop-syncrescendence/memory"

# Write MBA-specific context
cat > "$HOME/.claude/projects/-Users-$(whoami)-Desktop-syncrescendence/memory/MEMORY.md" << 'MEMEOF'
# MBA Commander Context

## Machine
- **Hostname**: MacBook Air (Apple Silicon)
- **Role**: Kinetic cockpit (INT-P015) — synaptic, kinetic, micro-ops
- **Dual engine**: Ajna (CSO/OpenClaw) + Commander (COO/Claude Code)

## Differences from Mac mini Commander
- No Graphiti/Qdrant MCP (Docker services are on Mac mini only)
- No Chrome DevTools / Playwright (headless deployment)
- Lighter MCP footprint: Obsidian, Filesystem, Linear, ClickUp, Gemini
- mba-cockpit (2-pane) instead of 4x2 cockpit
- Ajna runs alongside as CSO via OpenClaw gateway (port 18789)

## Coordination
- Git sync every 5 minutes via launchd (com.syncrescendence.git-sync)
- -INBOX/commander/ on MBA is watched but Commander needs manual launch
- -INBOX/ajna/ is watched by launchd (auto-dispatch to Ajna)
- Push changes promptly — Mac mini Commander depends on git sync

## Key Commands
- `mba-cockpit` — launch 2-pane Ajna+Commander session
- `mba-cockpit --launch` — same but auto-starts agent CLIs
- `claude --dangerously-skip-permissions` — start Commander
- `openclaw tui --session main` — start Ajna
MEMEOF

echo "  Memory written to ~/.claude/projects/-Users-$(whoami)-Desktop-syncrescendence/memory/MEMORY.md"

# ── Final verification ────────────────────────────────────────────────────
echo ""
echo "[6/6] Verification..."

# Check MCP config was written
MCP_COUNT=$(python3 -c "
import json, os
c = json.load(open(os.path.expanduser('~/.claude.json')))
repo = os.path.expanduser('~/Desktop/syncrescendence')
servers = c.get('projects', {}).get(repo, {}).get('mcpServers', {})
print(len(servers))
" 2>/dev/null || echo "0")

echo "  MCP servers configured: $MCP_COUNT"

# Check alias
if grep -q 'alias mba-cockpit' "$HOME/.zshrc" 2>/dev/null; then
    echo "  mba-cockpit alias: OK"
else
    echo "  mba-cockpit alias: MISSING"
fi

# Check cockpit script
if [[ -x "$MBA_COCKPIT_SCRIPT" ]]; then
    echo "  mba-cockpit.sh: OK (executable)"
else
    echo "  mba-cockpit.sh: MISSING or not executable"
fi

# Check Claude Code
echo "  claude binary: $(which claude 2>/dev/null || echo 'NOT FOUND')"

echo ""
echo "=== MBA Commander Initialization Complete ==="
echo ""
echo "Next steps:"
echo "  1. Source your shell:  source ~/.zshrc"
echo "  2. Launch cockpit:    mba-cockpit --launch"
echo "  3. Or start manually: cd ~/Desktop/syncrescendence && claude"
echo ""
echo "Linear/ClickUp MCP will work if API keys are in $ENV_FILE."
echo "If keys are missing, add LINEAR_API_KEY and CLICKUP_API_KEY to $ENV_FILE."
