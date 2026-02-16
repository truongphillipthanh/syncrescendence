---
url: https://x.com/manthanguptaa/status/2015780646770323543
author: Manthan Gupta (@manthanguptaa)
captured_date: 2026-01-26
---

# How Clawdbot Remembers Everything

Clawdbot is an open-source personal AI assistant (MIT licensed) created by [Peter Steinberger](https://x.com/steipete) that has quickly gained traction with over 32,600 stars on [GitHub](https://github.com/clawdbot/clawdbot) at the time of writing this blog. Unlike ChatGPT or Claude, which run in the cloud, Clawdbot runs locally on your machine and integrates with chat platforms you already use, like Discord, WhatsApp, Telegram, and more.

What sets Clawdbot apart is its ability to handle real-world tasks autonomously: managing emails, scheduling calendar events, handling flight check-ins, and running background jobs on a schedule. But what caught my attention was its **persistent memory system**, which maintains 24/7 context retention, remembering conversations and building upon previous interactions indefinitely.

If you've read my previous posts on [ChatGPT memory](https://manthanguptaa.in/posts/chatgpt_memory) and [Claude memory](https://manthanguptaa.in/posts/claude_memory), you know I am fascinated by how different AI products approach memory. Clawdbot takes a fundamentally different approach: instead of cloud-based, company controlled memory, it keeps everything local, giving users full ownership of their context and skills.

Let's dive into how it works.

## How Context is Built

Before diving into memory, let's understand what the model sees on each request:
```
[0] System Prompt (static + conditional instructions)
 Project Context (bootstrap files: AGENTS.md, SOUL.md, etc.)
 Conversation History (messages, tool calls, compaction summaries)
 Current Message
```

The system prompt defines the agent's capabilities and available tools. What's relevant for memory is Project Context, which includes user-editable Markdown files injected into every request:

| File | Purpose |
|------|---------|
| `AGENTS.md` | Agent instructions, including memory guidelines |
| `SOUL.md` | Personality and tone |
| `USER.md` | Information about the user |
| `TOOLS.md` | Usage guidance for external tools |

These files live in the agent's workspace alongside memory files, making the entire agent configuration transparent and editable.

## Context vs Memory

Understanding the distinction between **context** and **memory** is fundamental to understanding Clawdbot.

**Context** is everything the model sees for a single request:
```
Context = System Prompt + Conversation History + Tool Results + Attachments
```

Context is:
- **Ephemeral** - exists only for this request
- **Bounded** - limited by the model's context window (e.g., 200K tokens)
- **Expensive** - every token counts toward API costs and speed

**Memory** is what's stored on disk:
```
Memory = MEMORY.md + memory/*.md + Session Transcripts
```

Memory is:
- **Persistent** - survives restarts, days, months
- **Unbounded** - can grow indefinitely
- **Cheap** - no API cost to store
- **Searchable** - indexed for semantic retrieval

## The Memory Tools

The agent accesses memory through two specialized tools:

### 1. memory_search

**Purpose:** Find relevant memories across all files
```json
{
  "name": "memory_search",
  "description": "Mandatory recall step: semantically search MEMORY.md + memory/*.md before answering questions about prior work, decisions, dates, people, preferences, or todos",
  "parameters": {
    "query": "What did we decide about the API?",
    "maxResults": 6,
    "minScore": 0.35
  }
}
```

**Returns:**
```json
{
  "results": [
    {
      "path": "memory/2026-01-20.md",
      "startLine": 45,
      "endLine": 52,
      "score": 0.87,
      "snippet": "## API Discussion\\nDecided to use REST over GraphQL for simplicity...",
      "source": "memory"
    }
  ],
  "provider": "openai",
  "model": "text-embedding-3-small"
}
```

### 2. memory_get

**Purpose:** Read specific content after finding it
```json
{
  "name": "memory_get",
  "description": "Read specific lines from a memory file after memory_search",
  "parameters": {
    "path": "memory/2026-01-20.md",
    "from": 45,
    "lines": 15
  }
}
```

**Returns:**
```json
{
  "path": "memory/2026-01-20.md",
  "text": "## API Discussion\\n\\nMet with the team to discuss API architecture.\\n\\n### Decision\\nWe chose REST over GraphQL for the following reasons:\\n1. Simpler to implement\\n2. Better caching\\n3. Team familiarity\\n\\n### Endpoints\\n- GET /users\\n- POST /auth/login\\n- GET /projects/:id"
}
```

## Writing to Memory

There is no dedicated `memory_write` tool. The agent writes to memory using the standard `write` and `edit` tools which it uses for any file. Since memory is just Markdown, you can manually edit these files too (they will be re-indexed automatically).

The decision of **where** to write is prompt-driven via `AGENTS.md`:

(Description: A screenshot showing agent instructions specifying where to write memories based on significance and context type)

Automatic writes also occur during pre-compaction flush and session end (covered in later sections).

## Memory Storage

Clawdbot's memory system is built on the principle that "Memory is plain Markdown in the agent workspace."

### Two-Layer Memory System

Memory lives in the agent's workspace (default: `~/clawd/`):
```
~/clawd/
├── MEMORY.md - Layer 2: Long-term curated knowledge
└── memory/
    ├── 2026-01-26.md - Layer 1: Today's notes
    ├── 2026-01-25.md - Yesterday's notes
    ├── 2026-01-24.md - ...and so on
    └── ...
```

#### Layer 1: Daily Logs (memory/YYYY-MM-DD.md)

These are append-only **daily notes** that the agent writes here throughout the day. The agent writes this when the agent wants to remember something or when explicitly told to remember something.
```
# 2026-01-26

## 10:30 AM - API Discussion
Discussed REST vs GraphQL with user. Decision: use REST for simplicity. Key endpoints: /users, /auth, /projects.

## 2:15 PM - Deployment
Deployed v2.3.0 to production. No issues.

## 4:00 PM - User Preference
User mentioned they prefer TypeScript over JavaScript.
```

#### Layer 2: Long-term Memory (MEMORY.md)

This is **curated, persistent knowledge**. Agent writes to this when significant events, thoughts, decisions, opinions, and lessons are learned.
```
# Long-term Memory

## User Preferences
- Prefers TypeScript over JavaScript
- Likes concise explanations
- Working on project "Acme Dashboard"

## Important Decisions
- 2026-01-15: Chose PostgreSQL for database
- 2026-01-20: Adopted REST over GraphQL
- 2026-01-26: Using Tailwind CSS for styling

## Key Contacts
- Alice (alice@acme.com) - Design lead
- Bob (bob@acme.com) - Backend engineer
```

## How the Agent Knows to Read Memory

The `AGENTS.md` file (which is automatically loaded) contains instructions:
```
## Every Session

Before doing anything else:

1. Read SOUL.md - this is who you are
2. Read USER.md - this is who you are helping
3. Read memory/YYYY-MM-DD.md (today and yesterday) for recent context
4. If in MAIN SESSION (direct chat with your human), also read MEMORY.md

Don't ask permission, just do it.
```

## How Memory Gets Indexed

When you save a memory file, here's what happens behind the scenes:

(Description: A flowchart showing the memory indexing pipeline with 5 stages: File Saved → File Watcher Detects Change → Chunking (splitting into ~400 token chunks with 80 token overlap) → Embedding (converting chunks to vectors via embedding provider) → Storage (persisting to SQLite with vector and FTS5 indexes))

**sqlite-vec** is a SQLite extension that enables vector similarity search directly in SQLite, no external vector database required.

**FTS5** is SQLite's built-in full-text search engine that powers the BM25 keyword matching. Together, they allow Clawdbot to run hybrid search (semantic + keyword) from a single lightweight database file.

## How Memory is Searched

When you search memory, Clawdbot runs two search strategies in parallel. Vector search (semantic) finds content that means the same thing and BM25 search (keyword) finds content with exact tokens.

The results are combined with weighted scoring:
```
finalScore = (0.7 * vectorScore) + (0.3 * textScore)
```

Why 70/30? Semantic similarity is the primary signal for memory recall, but BM25 keyword matching catches exact terms that vectors might miss (names, IDs, dates). Results below a `minScore` threshold (default 0.35) are filtered out. All these values are configurable.

This ensures you get good results whether you are searching for concepts ("that database thing") or specifics ("POSTGRES_URL").

## Multi-Agent Memory

Clawdbot supports multiple agents, each with **complete memory isolation**: