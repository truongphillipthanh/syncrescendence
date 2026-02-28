# Agent Teams in Claude Code

I've been running Claude Code's Agent Teams for real work. It's experimental, but already useful if you understand how agents coordinate and how file edits are controlled.

These are the patterns that helped me improve throughput and avoid edit collisions.

(Description: Architectural diagram showing a User Prompt flowing to a Team Lead, which connects to three Reviewer agents (A, B, C) within a CLAUDE.md context box. The Team Lead coordinates with a "Shared Tasks & Messages" box on the right.)

## Install

Just add `"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"` to your settings.json

(Description: Code snippet showing a settings.json configuration with the agent teams flag enabled alongside other settings like enableAllProjectMcpServers and enableMcpJsonServers.)

That's it, no extra dependencies.

## How to use them

### 1. Describe the task and ask for a team

You don't configure teams manually. Just describe what you need:

> I need to remove all debug console.log statements from docs/js/. Create an agent team, split by file ownership so nobody edits the same file.

Claude creates the team, splits the work into tasks, spawns teammates, and coordinates everything.

### 2. Watch teammates appear in the statusline

(Description: Terminal statusline showing a "Channeling..." message with token count, indicating active agent team execution with instructions to use keyboard shortcuts for navigation.)

### 3. Watch them work in parallel

Each teammate reads files, makes edits, and reports progress. In the console you can see all three working simultaneously on different files:

(Description: Terminal output showing parallel execution of cleanup tasks across multiple files, with color-coded module indicators (data-core, ui-events, features) and file edit progress messages.)

### 4. Tasks complete one by one

The shared task list tracks everything. You can check progress anytime:

(Description: Terminal task completion view showing three teams with their completion status, including feature cleanup (10 console.log removed), data-core cleanup (all files cleaned), and ui-events completion, with a final "Brewing..." state showing completed file checkmarks.)

## How Agent Teams really behave

A few things become obvious quickly:

- Each teammate runs in its **own context window**
- There's **no shared conversation history**
- All teammates automatically load **CLAUDE.md**
- Communication happens via messages + a shared task list

So coordination doesn't come from conversation, it comes from **structure**. That's where **CLAUDE.md** matters.

## The 3 rules

### 1- Describe your module boundaries so the lead can split work

When you ask for an agent team, Claude Code reads your CLAUDE.md to decide how to divide files across teammates. The clearer your module boundaries, the smarter the split.

In CLAUDE.md (shared project context):
```markdown
## Independent Modules
| Module | Directory | Notes |
|---------|-------------|-----|
| API | api/ | Each file is independent |
| CLI | src/ | Core logic |
| Website | docs/js/ | Static content |

**Shared files (coordinate before editing):**
- package.json
- tsconfig.json
```

In my test, I told Claude Code: "there are console.log across files in docs/js/, create a team and split by file ownership." Claude Code read the project structure, assigned explicit file lists to each teammate, and produced zero conflicts across 9 files. It made that split because it understood which files were independent.

### 2. Keep project context short and operational

Every teammate loads your CLAUDE.md on startup, but none of them inherit the lead's conversation. If your CLAUDE.md is vague, each teammate wastes tokens re-exploring the codebase independently.
```markdown
## Quick Context
- **Stack**: Node.js CLI + Static site + Vercel Serverless
- **Entry point**: src/index.js
- **Tests**: Jest (`npm test`)
- **Database**: Neon
```

In our team, no teammate asked the lead what the project was about or where files lived. They all got that from CLAUDE.md. Three teammates loading context simultaneously means three times the token cost if that context requires exploration instead of a quick read.

### 3. Define what "verified" means for your project

Claude Code includes verification steps in each task when it knows what passing looks like. If your CLAUDE.md lists how to check that things work, teammates use those signals to confirm their own work:
```markdown
## Verification
- `npm test`
- `npm run lint`
- `npm run build`
```

In our cleanup, teammates self-verified using grep because the task was about removing console.log. Claude Code chose the right check for the task. But having project-wide gates in CLAUDE.md gives the lead a vocabulary for "done" that it can adapt per task automatically.

In practice, each teammate self-reported exactly what they did:
```markdown
data-core: "Removed 27 console.log across 3 files. Kept all 12 console.error and 2 console.warn in component-page.js. Verified zero console.log remaining in my assigned files."
```

No lead intervention was needed. Clear rules in, clear reports out.

## Extra: a note on plan mode

One thing I learned by using it in teams, plan mode is evaluated **on every turn**, not just once.

(Description: Flow diagram showing plan-request approval-approved-new turn cycle, with a secondary loop branching back to re-plan and request approval again, illustrating the iterative planning mode.)

In practice, this makes it great for:

- design-only roles
- initial task shaping

For execution, spawning a new teammate in default mode keeps work flowing. An agent's mode stays fixed for its entire lifetime.

## Takeaway

Agent Teams work best when:

- agents own clear surfaces
- communication is structured, not conversational
- CLAUDE.md is treated as shared runtime context

It's experimental, but once you align with how teams actually execute and communicate, it starts to feel less like "multiple agents" and more like a coordinated system running in parallel.

---

**Posted:** 8:19 AM · Feb 7, 2026  
**Views:** 111.8K  
**Engagement:** 11 replies, 37 reposts, 343 likes, 667 bookmarks