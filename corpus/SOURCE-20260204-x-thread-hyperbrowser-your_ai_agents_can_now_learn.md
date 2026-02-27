# Hyperbrowser Thread: AI Agent Skill Learning

## Post 1: Core Announcement
**@hyperbrowser** · Feb 4

Your AI agents can now learn new skills from the web.
And update them automatically.

/learn stripe-payments

Searches the docs. Scrapes the pages. No more outdated skills.

Powered by Hyperbrowser, Setup Guide ↓

(Description: Video showing Claude Code v2.1.31 execution with terminal output demonstrating web search for "Stripe checkout integration guide", finding excellent official sources, scraping key documentation pages, and running multiple hyperbrowser scrape_webpage MCP calls with different URLs including stripe.com/payments and payments/accept endpoints. Console shows "Running..." status and "Wandering..." indicator. Permission bypass prompt visible at bottom with "shift+tab to cycle" instruction.)

---

## Post 2: API Key Setup
**@hyperbrowser** · Feb 4

Get your API keys

1. Hyperbrowser API Key → hyperbrowser.ai
2. Serper API Key

(Card: "Browser infra for AI Agents" - Hyperbrowser - Web Infra for AI Agents)

---

## Post 3: Claude Code MCP Configuration
**@hyperbrowser** · Feb 4

Add Hyperbrowser MCP to Claude Code

→ Open your project
→ Create .mcp.json in root
→ Paste config:
```json
{
  "mcpServers": {
    "hyperbrowser": {
      "command": "npx",
      "args": ["-y", "hyperbrowser-mcp"],
      "env": {
        "HYPERBROWSER_API_KEY": "YOUR_HYPERBROWSER_API_KEY",
        "SERPER_API_KEY": "YOUR_SERPER_API_KEY"
      }
    }
  }
}
```

---

## Post 4: Learning Command Installation
**@hyperbrowser** · Feb 4

Add the /learn command

→ mkdir .claude/commands
→ Drop in learn.md
→ Restart Claude Code

Get learn.md from: github.com/hyperbrowserai/.../examples/tree/main/skills

---

## Post 5: Usage Examples
**@hyperbrowser** · Feb 4

Use it

→ /learn hono
→ /learn drizzle-orm
→ /learn anything

Searches docs. Scrapes pages. Generates skill.

Your agent knows it now.

---

## Post 6: Learn More
**@hyperbrowser** · Feb 4

Learn more about Hyperbrowser:

(Card: "Browser infra for AI Agents" - Hyperbrowser - Web Infra for AI Agents)

---

**Thread Stats:**
- Main post: 55 replies, 217 reposts, 2,073 likes, 3,412 bookmarks, 778.4K views
- Post 2: 1 reply, 3 reposts, 42 likes, 71 bookmarks, 17.7K views
- Post 3: 2 replies, 0 reposts, 21 likes, 19 bookmarks, 14.7K views
- Post 4: 1 reply, 2 reposts, 20 likes, 28 bookmarks, 11.5K views
- Post 5: 1 reply, 0 reposts, 14 likes, 8 bookmarks, 10.6K views
- Post 6: 0 replies, 0 reposts, 13 likes, 16 bookmarks, 9.1K views