# MCP Authentication Setup Guide

> Generated: 2026-02-07
> Context: Configuring MCP servers that require OAuth browser flows or manual API token creation for Claude Code integration.

---

## Section 1: OAuth MCP Servers (Remote — Browser Auth Required)

These 5 MCP servers are already configured in `~/.claude.json` as remote (`url`-based) servers. Each requires a one-time OAuth browser authentication flow. No npm install is needed — Claude Code connects to the hosted service directly.

### General OAuth Flow

1. Start a new Claude Code session (or restart the current one so it picks up `~/.claude.json` changes).
2. Invoke a tool from the target service (e.g., "list my Linear issues").
3. Claude Code detects the remote MCP server needs auth and opens a browser tab to the service's OAuth consent screen.
4. Approve the requested permissions in the browser.
5. The browser redirects back; Claude Code captures the token.
6. Auth persists across sessions (stored in Claude Code's OAuth token cache at `~/.claude/`).

If auth expires or is revoked, repeating steps 2-5 will re-authenticate.

---

### 1. Linear MCP

| Field | Value |
|-------|-------|
| **URL** | `https://mcp.linear.app/mcp` |
| **OAuth trigger** | Claude Code opens a browser tab to Linear's OAuth consent screen |
| **Permissions to grant** | Read/write access to your Linear workspace (issues, projects, teams, comments) |
| **How to verify** | Ask Claude Code: "List my Linear issues" or "Show SYN team issues" |

**Alternative (stdio, no OAuth):**
The community `linear-mcp-server` package can run locally using your existing API key (`lin_api_...`), avoiding the OAuth flow. Trade-off: may have fewer features than the official remote server.

```json
"linear-local": {
  "command": "npx",
  "args": ["-y", "linear-mcp-server"],
  "env": { "LINEAR_API_KEY": "<your-linear-api-key>" }
}
```

---

### 2. ClickUp MCP

| Field | Value |
|-------|-------|
| **URL** | `https://mcp.clickup.com/mcp` |
| **OAuth trigger** | Browser OAuth to ClickUp |
| **Permissions to grant** | Read/write access to your ClickUp workspace (tasks, lists, spaces) |
| **How to verify** | Ask Claude Code: "List my ClickUp tasks" or "Show tasks in the Professional space" |

**Alternative (stdio, no OAuth):**
The community `@taazkareem/clickup-mcp-server` runs locally with your existing API key.

```json
"clickup-local": {
  "command": "npx",
  "args": ["-y", "@anthropic/clickup-mcp-server"],
  "env": { "CLICKUP_API_KEY": "<your-clickup-api-key>" }
}
```

> Note: Verify the exact community package name at install time; the `@taazkareem/clickup-mcp-server` package is the most referenced community option.

---

### 3. Notion MCP

| Field | Value |
|-------|-------|
| **URL** | `https://mcp.notion.com/mcp` |
| **OAuth trigger** | Browser OAuth to Notion |
| **Permissions to grant** | Access to workspace pages, databases, and blocks |
| **How to verify** | Ask Claude Code: "Search my Notion pages" or "List Notion databases" |

No widely-used stdio alternative exists — the official remote server is the recommended path.

---

### 4. Dropbox MCP

| Field | Value |
|-------|-------|
| **URL** | `https://mcp.dropbox.com/mcp` |
| **OAuth trigger** | Browser OAuth to Dropbox |
| **Permissions to grant** | File and folder read/write access |
| **How to verify** | Ask Claude Code: "List files in my Dropbox root" or "Search Dropbox for <filename>" |

No widely-used stdio alternative exists — use the official remote server.

---

### 5. Figma MCP

| Field | Value |
|-------|-------|
| **URL** | `https://mcp.figma.com/mcp` |
| **OAuth trigger** | Browser OAuth to Figma |
| **Permissions to grant** | Read access to Figma files, projects, and design data |
| **How to verify** | Ask Claude Code: "Describe my recent Figma files" or "Get details for Figma file <URL>" |

No widely-used stdio alternative exists — use the official remote server.

---

## Section 2: Tier C MCP Servers (Manual Install + Token Creation)

These servers run locally (stdio transport) and require both npm package installation and manually-created API tokens. Add each config block to the `mcpServers` object in `~/.claude.json`.

---

### 1. GitHub MCP

**Create token:**
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **"Generate new token"** -> **Fine-grained token** (recommended) or Classic token
3. Set expiration (90 days recommended, or no expiration for personal use)
4. **Repository access**: All repositories (or select specific ones)
5. **Permissions** (fine-grained): Contents (read/write), Issues (read/write), Pull requests (read/write), Metadata (read)
6. For classic tokens, select scopes: `repo` (full), `read:org`, `read:user`, `read:project`
7. Click **Generate token** and copy immediately

**Package:** [`@modelcontextprotocol/server-github`](https://www.npmjs.com/package/@modelcontextprotocol/server-github)

**Add to `~/.claude.json`:**
```json
"github": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-github-token>"
  }
}
```

**Verify:** Ask Claude Code "List my GitHub repos" or "Show open issues in <repo>"

---

### 2. Slack MCP

**Create Slack App and Bot Token:**
1. Go to [api.slack.com/apps](https://api.slack.com/apps) -> **Create New App** -> **From scratch**
2. Name the app (e.g., "Claude MCP") and select your workspace
3. Navigate to **OAuth & Permissions** in the sidebar
4. Under **Bot Token Scopes**, add:
   - `channels:read` — list public channels
   - `channels:history` — read channel messages
   - `chat:write` — send messages
   - `users:read` — list users
   - `files:read` — access shared files
   - `groups:read` — list private channels (optional)
   - `reactions:read` — read reactions (optional)
5. Click **Install to Workspace** at the top of the OAuth page
6. Approve the permissions
7. Copy the **Bot User OAuth Token** (starts with `xoxb-...`)
8. Find your **Workspace/Team ID**: it's the `T`-prefixed value in your Slack URL (e.g., `T01234567`)

**Package:** [`@modelcontextprotocol/server-slack`](https://www.npmjs.com/package/@modelcontextprotocol/server-slack)

**Add to `~/.claude.json`:**
```json
"slack": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-slack"],
  "env": {
    "SLACK_BOT_TOKEN": "xoxb-your-bot-token-here",
    "SLACK_TEAM_ID": "T01234567"
  }
}
```

**Optional:** Add `"SLACK_CHANNEL_IDS": "C01234567,C76543210"` to `env` to restrict which channels the bot can access.

**Verify:** Ask Claude Code "List Slack channels" or "Read recent messages in #general"

---

### 3. Discord MCP

**Create Discord Bot:**
1. Go to [discord.com/developers/applications](https://discord.com/developers/applications) -> **New Application**
2. Name it (e.g., "Claude MCP Bot")
3. Navigate to the **Bot** tab in the sidebar
4. Click **Reset Token** -> copy the bot token immediately (shown only once)
5. Under **Privileged Gateway Intents**, enable:
   - **Message Content Intent** (required to read message content)
6. Navigate to **OAuth2** -> **URL Generator**:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Read Message History`, `View Channels`
7. Copy the generated URL, open it in a browser, and invite the bot to your server

**Package:** [`discord-mcp`](https://www.npmjs.com/package/discord-mcp) (community package by GustyCube — most actively maintained)

**Add to `~/.claude.json`:**
```json
"discord": {
  "command": "npx",
  "args": ["-y", "discord-mcp"],
  "env": {
    "DISCORD_TOKEN": "<your-bot-token>"
  }
}
```

**Verify:** Ask Claude Code "List my Discord servers" or "Read messages in #general on <server name>"

---

### 4. Airtable MCP

**Create token:**
1. Go to [airtable.com/create/tokens](https://airtable.com/create/tokens)
2. Click **Create new token**
3. Name it (e.g., "Claude MCP")
4. **Scopes**:
   - `data.records:read` — read records
   - `data.records:write` — create/update records
   - `schema.bases:read` — read base schemas
   - `data.recordComments:read` — read comments (optional)
5. **Access**: Select specific bases or all bases
6. Click **Create token** and copy immediately

**Package:** [`airtable-mcp-server`](https://www.npmjs.com/package/airtable-mcp-server) (official MCP implementation — note: no `@modelcontextprotocol/` prefix)

**Add to `~/.claude.json`:**
```json
"airtable": {
  "command": "npx",
  "args": ["-y", "airtable-mcp-server"],
  "env": {
    "AIRTABLE_API_KEY": "<your-airtable-token>"
  }
}
```

**Verify:** Ask Claude Code "List my Airtable bases" or "Show records in <base name>"

---

### 5. Brave Search MCP

**Create API key:**
1. Go to [brave.com/search/api](https://brave.com/search/api)
2. Click **Get API Key** (or sign in if you have an account)
3. The **Free tier** provides 2,000 queries/month (sufficient for personal use)
4. Copy your API key from the dashboard

**Package:** [`@modelcontextprotocol/server-brave-search`](https://www.npmjs.com/package/@modelcontextprotocol/server-brave-search)

> Note: Brave also publishes an official package at `@brave/brave-search-mcp-server` with additional features (image/video/news search). Either works; the `@modelcontextprotocol` version is more widely tested with Claude Code.

**Add to `~/.claude.json`:**
```json
"brave-search": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-brave-search"],
  "env": {
    "BRAVE_API_KEY": "<your-brave-api-key>"
  }
}
```

**Verify:** Ask Claude Code "Search Brave for latest MCP server updates" or "Search the web for <query>"

---

## Quick Reference: All Tier C Config Blocks

Copy this combined block into the `mcpServers` section of `~/.claude.json`:

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "<token>" }
  },
  "slack": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "xoxb-...",
      "SLACK_TEAM_ID": "T..."
    }
  },
  "discord": {
    "command": "npx",
    "args": ["-y", "discord-mcp"],
    "env": { "DISCORD_TOKEN": "<token>" }
  },
  "airtable": {
    "command": "npx",
    "args": ["-y", "airtable-mcp-server"],
    "env": { "AIRTABLE_API_KEY": "<token>" }
  },
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": { "BRAVE_API_KEY": "<key>" }
  }
}
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| OAuth flow doesn't open browser | Ensure you're running Claude Code in a terminal with browser access (not headless SSH) |
| OAuth token expired | Re-trigger by calling any tool from that service; Claude Code will re-auth |
| `npx` hangs on first run | First invocation downloads the package; allow 30-60s. Check network connectivity |
| "GITHUB_PERSONAL_ACCESS_TOKEN not set" | Ensure the env var is in `~/.claude.json`, not in shell env (Claude Code reads from config) |
| Slack bot can't see channels | The bot must be invited to channels with `/invite @BotName`, or use `SLACK_CHANNEL_IDS` |
| Discord bot has no messages | Enable **Message Content Intent** in the bot's developer portal settings |
| Permission denied errors | Check that tokens have the required scopes listed above |
| Server crashes on startup | Run `npx -y <package-name>` directly in terminal to see error output |

---

## Token Security

- Never commit tokens to git. The `~/.claude.json` file is in your home directory, outside any repo.
- Use fine-grained tokens with minimal scopes where possible (especially GitHub).
- Set token expiration dates and rotate periodically.
- If a token is compromised, revoke it immediately at the service's settings page.
