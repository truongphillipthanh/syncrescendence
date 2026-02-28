# CLARESCENCE: MCP Bridge Architecture — Full Surface Audit

**Date**: 2026-02-07
**Trigger**: Sovereign directive to "fully exploit" CLI bridge extensibility across all incumbent SaaS, AI platforms, browsers, and macOS native apps via MCP
**Prior Art**: CLARESCENCE-2026-02-05-incumbent-saas-teleology.md, DEC-20260206-144500-disposition-routing-charter.md, REF-STACK_TELEOLOGY.md

---

## Executive Finding

**Every incumbent surface in the Syncrescendence stack has a working MCP server.** The ecosystem matured faster than anticipated. 10 of 14 SaaS platforms have official first-party servers. Apple is adding native MCP support to Xcode 26.3. Google shipped official MCP for Chrome DevTools. Microsoft shipped official Playwright MCP for cross-browser automation.

MCP servers slot into the Disposition + Routing Charter as **Tier 0.5** — cheaper than native vendor integrations (Tier 1) because they're local, free, and require no vendor-side configuration. They do not replace the charter; they accelerate it.

---

## Surface Audit: Full Matrix

### Cloud Bridge (SaaS via MCP)

| Surface | Charter Role | MCP Server | Official? | Auth Method | R/W | Install |
|---------|-------------|------------|-----------|-------------|-----|---------|
| **Linear** | Repo-bound work bus (T1a) | `https://mcp.linear.app/mcp` | Official remote | OAuth | R+W | `claude mcp add --transport http linear https://mcp.linear.app/mcp` |
| **ClickUp** | Meta-work bus (T1b) | `https://mcp.clickup.com/mcp` | Official remote | OAuth | R+W | `claude mcp add --transport http clickup https://mcp.clickup.com/mcp` |
| **GitHub** | Execution artifact | `github/github-mcp-server` | Official (GitHub) | PAT | R+W | Docker or npx |
| **Slack** | Coordination bus | `@modelcontextprotocol/server-slack` | Anthropic ref (deprecated) | Bot Token | R+W | npx |
| **Discord** | Agent habitat | `mcp-discord` | Community | Bot Token | R+W | npx |
| **Notion** | Dashboard mirror | `https://mcp.notion.com/mcp` | Official remote | OAuth | R+W | `claude mcp add --transport http notion https://mcp.notion.com/mcp` |
| **Airtable** | Dashboard mirror | `airtable-mcp-server` | Community | PAT | R+W | npx |
| **Dropbox** | File storage | `https://mcp.dropbox.com/mcp` | Official remote | OAuth | R+W | `claude mcp add --transport http dropbox https://mcp.dropbox.com/mcp` |
| **Box** | File storage | `box-mcp-server` | Community + docs | JWT | R only | npx |
| **Google Drive** | Library/storage | `@modelcontextprotocol/server-gdrive` | Anthropic ref (deprecated) | OAuth | R | npx |
| **Figma** | Design surface | `https://mcp.figma.com/mcp` | Official remote | OAuth | R | `claude mcp add --transport http figma https://mcp.figma.com/mcp` |
| **Canva** | Design surface | `@canva/cli` | Official | OAuth | R+W | `npx -y @canva/cli@latest mcp` |
| **Make** | Data router | `@makehq/mcp-server` | Official | API Key | R+W | npx |
| **Outlook/M365** | Email/calendar | `@microsoft/m365agentstoolkit-mcp` | Official (Microsoft) | Azure AD | R+W | npx |

### AI Platform Bridge

| Surface | MCP Server | Official? | Mechanism | Notes |
|---------|------------|-----------|-----------|-------|
| **ChatGPT Desktop** | `chatgpt-mcp`, `mcp-server-chatgpt-app` | Community | osascript/UI automation | Send prompts, retrieve responses |
| **Claude Desktop** | N/A — Claude IS the MCP client | — | Native MCP host | The hub, not a spoke |
| **Perplexity** | `perplexityai/modelcontextprotocol` | Official | API | Sonar search, deep research |
| **Grok** | `Grok-MCP` | Community | xAI API | Text, vision, image gen |
| **Gemini** | Google managed MCP servers | Official (Google) | API | Maps, BigQuery, etc. |
| **NotebookLM** | `notebooklm-mcp` | Community | Undocumented API | FRAGILE — no official API |
| **Manus** | `manus-mcp` | Community | REST API | Task creation, webhooks |

### OS Bridge (macOS Native via MCP)

| Surface | MCP Server | Official? | Mechanism | Notes |
|---------|------------|-----------|-----------|-------|
| **Apple Shortcuts** | `artemnovichkov/shortcuts` | Community | shortcuts CLI | Also usable without MCP |
| **Keyboard Maestro** | `anthropics/keyboard-maestro-mcp` | Anthropic-affiliated | osascript/KM API | 51+ tools |
| **Apple Reminders** | `apple-reminders-mcp` (3+ options) | Community | AppleScript/EventKit | Full CRUD |
| **Apple Notes** | `mcp-apple-notes` (3+ options) | Community | AppleScript/iCloud | CRUD + semantic search |
| **Apple Native (umbrella)** | `supermemoryai/apple-mcp` | Community | AppleScript | Messages, Contacts, Notes, Mail, Calendar, Maps |

### Browser Bridge

| Surface | MCP Server | Official? | Mechanism | Notes |
|---------|------------|-----------|-----------|-------|
| **Chrome** | `chrome-devtools-mcp` | Official (Google) | Chrome DevTools Protocol | Debug, inspect, control |
| **Brave** | `@brave/brave-search-mcp-server` | Official (Brave) | Search API | 2K queries/mo free |
| **Any browser** | `microsoft/playwright-mcp` | Official (Microsoft) | Playwright | Gold standard, cross-browser |
| **Browser Use** | `browser-use` | Community | AI automation | Vision + accessibility tree |

### Development Bridge

| Surface | MCP Server | Official? | Notes |
|---------|------------|-----------|-------|
| **Xcode** | Native in Xcode 26.3 + `XcodeBuildMCP` | Official (Apple) + community | iOS/macOS build, test, simulator |
| **Apple Dev Docs** | `apple-developer-documentation` | Community | Search Apple docs via MCP |

### Filesystem Bridge

| Surface | MCP Server | Official? | Notes |
|---------|------------|-----------|-------|
| **Obsidian vault** | `@mauricio.wolff/mcp-obsidian` | Community (best) | Direct filesystem, frontmatter-aware, no plugin needed |
| **General filesystem** | `@modelcontextprotocol/server-filesystem` | Anthropic official | Sandboxed file R/W |

---

## Charter Alignment

Per DEC-20260206-144500-disposition-routing-charter.md, the integration ladder is:

1. **Tier 0**: Human-mediated
2. **Tier 0.5**: MCP servers (NEW — free, local, no vendor dependency)
3. **Tier 1**: Native vendor integrations (Linear↔GitHub, etc.)
4. **Tier 2**: Make/Zapier
5. **Tier 3**: Custom API scripts

MCP servers satisfy all three charter principles:
- **Single internal bus (σ₄)**: MCP doesn't move ground truth — Claude reads/writes through it while repo stays canonical
- **Cheap-first**: Zero marginal cost, no subscription, no vendor approval
- **Receipt requirement**: All MCP operations are logged in Claude Code session history

---

## MCP Tool Search (Context Optimization)

Claude Code has built-in MCP Tool Search (`ENABLE_TOOL_SEARCH`). When configured MCP servers expose too many tools (>10% of context window), Claude defers loading them and searches on-demand via regex/BM25. This is critical — with 30+ MCP servers, tool descriptions alone could consume 20K+ tokens.

**Configuration**: Already defaults to `auto` — no action needed. It will self-activate as we add servers.

---

## Installation Tiers

### Tier A: Install Now (remote hosted, OAuth via browser — one-time auth)
Linear, ClickUp, Notion, Dropbox, Figma

### Tier B: Install Now (npx, uses existing credentials)
Obsidian (filesystem-based), Filesystem, Brave Search, Playwright, Chrome DevTools

### Tier C: Install After Auth Setup
GitHub (needs PAT), Slack (needs bot token), Discord (needs bot token), Airtable (needs PAT)

### Tier D: Install When Needed
Make, Canva, Outlook/M365, Box, Google Drive, ChatGPT bridge, Perplexity, Xcode, Apple Native, Keyboard Maestro, Shortcuts, NotebookLM, Manus

---

## Registries for Future Discovery

| Registry | URL | Scale |
|----------|-----|-------|
| mcp.so | mcp.so | 17,500+ servers |
| Smithery | smithery.ai | 7,300+ servers |
| PulseMCP | pulsemcp.com/servers | 8,050+ servers |
| Official MCP Registry | registry.modelcontextprotocol.io | Curated |
| GitHub MCP Registry | github.com (blog/announcement) | Curated |
| mcp-get | mcp-get.com | npm-style |

---

## Open Decisions for Sovereign

1. **Linear MCP**: Use official remote (OAuth) or community `linear-mcp-server` (existing API key)?
2. **ClickUp MCP**: Use official remote (OAuth) or community `@taazkareem/clickup-mcp-server` (existing API key)?
3. **Slack**: Create a Slack bot for the MCP server, or defer?
4. **Discord**: Create a Discord bot, or defer?
5. **Google Drive auth**: Set up OAuth Desktop App credentials?
6. **NotebookLM**: Accept fragility of undocumented API, or wait for official?
7. **Code editor**: Zed vs Nova vs BBEdit vs CotEditor — backlog item, non-urgent
