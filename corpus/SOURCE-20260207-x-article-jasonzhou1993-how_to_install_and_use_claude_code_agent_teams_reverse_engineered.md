# How to install and use Claude Code Agent Teams (Reverse-engineered)

(Description: Pixel art style header with large orange text reading "AGENT TEAMS" accompanied by three pixelated robot/character icons on the right side)

Claude Code just shipped a **massive upgrade** to its agent system: **Agent Teams**.

This isn't a small iteration on the old task + sub-agent model. It's a fundamentally different execution model that allows **3–5 independent Claude Code instances** to collaborate on the same project, share context, exchange messages, and coordinate through a shared task system.

I spent time digging into the logs, tracing model calls, and inspecting the filesystem changes behind the scenes. After a lot of back-and-forth investigation, I finally feel like I understand how Agent Teams **actually** work - and more importantly, **when they're worth using over traditional sub-agents**.

This post walks through:

- How to install and enable Agent Teams
- How Agent Teams differ from sub-agents
- The internal tools and lifecycle (Team Create, Task Create, messaging, shutdown)
- How agents communicate with each other
- A real debugging use case where Agent Teams clearly outperform sub-agents

## How to install and enable Agent Teams

Before anything else, make sure you're on the right version.

### 1. Update Claude Code to latest version

### 2. Enable the Experimental Flag

Agent Teams are still behind a feature flag. Run below to open settings.json
```
code ~/.claude/settings.json
```

and in global setting file, add:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Save the file and restart your terminal.

### 3. Start a New Claude Code Session

Once enabled, They can be activated when your prompt explicitly instructs Claude Code to **create an agent team**.

For example:

> "I'm designing a CLI tool that helps developers track TODO comments across their codebase. Create an agent team to explore this from different angles: one teammate on UX, one on technical architecture, one playing devil's advocate."

When Claude Code detects that intent, it will begin creating team members automatically.

## The Best Way to Use Agent Teams (Live, Multi-Session View)

(Description: Screenshot of iTerm2 terminal displaying multiple panes showing code investigation results with a debugging table containing columns for "Finding", "CLI Assessment", "Agent Assessment", "Next Changes" and rows showing various findings like "Codebase", "Issues Test", etc., with detailed debugging information visible across multiple synchronized agent sessions)

Agent Teams shine when you can **see every agent working in parallel**.

The best setup I've found:

- **tmux**, or
- **iTerm2 on macOS**

### iTerm2 Setup

1. Install iTerm2
2. Go to **Settings → General → Magic**
3. Enable **Python API**
4. Restart iTerm2

Then launch Claude Code with tmux mode:
```
claude --teammate-mode tmux
```

This opens:

- One pane for the **team lead**
- Separate panes for each **agent teammate**

You can click into any pane, watch what the agent is doing live, and even send direct messages to individual agents.

## Sub-Agents vs Agent Teams: What Actually Changed?

(Description: Diagram comparing Sub-agent vs Agent Teams architecture. Left side shows "Sub-agent" with a simple "Task" box connected to a small robot icon. Right side shows "Agent Teams" with hierarchical structure: TeamCreate at top, TaskCreate dropdown with task list icon, Task M boxes connecting to three robot icons labeled TaskUpdate, with "Send message" boxes at the bottom, showing the more complex coordination structure)

Before Agent Teams, Claude Code had a simple model:

### Old Model: Sub-Agents / Task tool

- Main agent calls task tool
- A sub-agent spins up
- Sub-agent works in isolation
- Session terminates
- Only a summary is returned to the main agent

### New Model: Agent Teams

Agent Teams introduce:

- Shared task lists
- Message & communication between agents
- Explicit lifecycle control (startup, shutdown)

This is enabled by **new internal tools**.

Let's break them down.

### Tool 1: TeamCreation

Everything starts with the **TeamCreate** tool. When invoked: A new team folder is created under: `.claude/teams/`

At this point, The team exists, **No agents are assigned yet**

Think of this as scaffolding.
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["team_name"],
  "additionalProperties": false,
  "properties": {
    "team_name": {
      "type": "string",
      "description": "Name for the new team to create."
    },
    "description": {
      "type": "string",
      "description": "Team description/purpose."
    },
    "agent_type": {
      "type": "string",
      "description": "Type/role of the team lead (e.g., \\"researcher\\", \\"test-runner\\"). Used for team file and inter-agent coordination."
    }
  }
}
```

### Tool 2: TaskCreate

This tool is different from the Task tool which will spin up agent sessions, this tool this specifically creating new todo

Each task lives as a JSON file under: `.claude/tasks/team-id`

Tracks: Task ID, Description, Status (pending, in_progress, complete, deleted), Owner, Dependencies (blocks, blocked_by)

Tasks can be delegated top-down by **team-lead** (which is the main agent), or **Self-claim** (as agent team can use taskList or getTask, updateTask tool to do so)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["subject", "description"],
  "additionalProperties": false,
  "properties": {
    "subject": {
      "type": "string",
      "description": "A brief title for the task"
    },
    "description": {
      "type": "string",
      "description": "A detailed description of what needs to be done"
    },
    "activeForm": {
      "type": "string",
      "description": "Present continuous form shown in spinner when in_progress (e.g., \\"Running tests\\")"
    },
    "metadata": {
      "type": "object",
      "additionalProperties": {},
      "description": "Arbitrary metadata to attach to the task"
    }
  }
}
```

### Tool 3: Task tool

The agents are still activated by Task tool, which is the same as sub agent, however it got some upgrades;

It got new params **`name`**, and **`team_name`**, when those 2 params are past, it will use agent team instead of simple sub agent subprocess
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["description", "prompt", "subagent_type"],
  "additionalProperties": false,
  "properties": {
    "description": {
      "type": "string",
      "description": "A short (3-5 word) description of the task"
    },
    "prompt": {
      "type": "string",
      "description": "The task for the agent to perform"
    },
    "subagent_type": {
      "type": "string",
      "description": "The type of specialized agent to use"
    },
    "name": {
      "type": "string",
      "description": "Name for the spawned agent - used as their identity for messaging"
    },
    "team_name": {
      "type": "string",
      "description": "Team name to join. This is what makes it a teammate vs a sub-agent."
    },
    "model": {
      "type": "string",
      "enum": ["claude", "grok", "haiku"],
      "description": "Optional model override"
    },
    "mode": {
      "type": "string",
      "enum": ["superscripts", "bypassPermissions", "default", "delegate", "dontAsk", "plan"],
      "description": "Permission mode for the teammate"
    },
    "run_in_background": {
      "type": "boolean",
      "description": "Set true to run in background (typical for teammates)"
    },
    "max_turns": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "Maximum agentic turns before stopping"
    },
    "resume": {
      "type": "string",
      "description": "Agent ID to resume a previous teammate"
    }
  }
}
```

The key distinction: adding name + team_name makes it a **teammate**. Without those, it's a standalone **sub-agent**.

### Tool 4: taskUpdate

Each agent is expected to call taskUpdate tool to claim task, update status
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["taskId"],
  "additionalProperties": false,
  "properties": {
    "taskId": {
      "type": "string",
      "description": "The ID of the task to update"
    },
    "status": {
      "anyOf": [
        {
          "type": "string",
          "enum": ["pending", "in_progress", "complete"]
        },
        {
          "type": "string",
          "const": "deleted"
        }
      ],
      "description": "New status for the task"
    },
    "subject": {
      "type": "string",
      "description": "New subject for the task"
    },
    "description": {
      "type": "string",
      "description": "New description for the task"
    },
    "activeForm": {
      "type": "string",
      "description": "Present continuous form shown in spinner when in_progress"
    },
    "owner": {
      "type": "string",
      "description": "New owner for the task"
    },
    "metadata": {
      "type": "object",
      "additionalProperties": {},
      "description": "Metadata keys to merge into the task. Set a key to null to delete it."
    },
    "addBlocks": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Task IDs that this task blocks"
    },
    "addBlockedBy": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Task IDs that block this task"
    }
  }
}
```

### Tool 5: sendMessage

Agent Teams introduce a **Send Message** tool.

It supports:

- **Direct messages** (agent → agent)
- **Broadcast messages** (agent → all teammates)

Under the hood:

- Messages are written to `.claude/teams/<team_id>/inbox/`
- Each agent has its own inbox
- Messages are injected as **new user messages** into the agent's conversation history, e.g. `<teammate-message teammate_id="team-lead">...</teammate-message>`

--------

Meanwhile team-lead agent can send **`shutdown_request`** to team mate agent, where team-mate agent send **`shutdown_response`** to confirm, which likely use postToolCall hook to auto terminate the agent session
```json
{
  "type": "object",
  "required": ["recipient"],
  "additionalProperties": false,
  "properties": {
    "type": {
      "type": "string",
      "enum": ["message", "broadcast", "shutdown_request", "shutdown_response", "plan_approval_response"],
      "description": "Message type"
    },
    "recipient": {
      "type": "string",
      "description": "Agent name of the recipient (Required for message, !shutdown_request, plan_approval_response)"
    },
    "content": {
      "type": "string",
      "description": "Message text, reason, or feedback"
    },
    "summary": {
      "type": "string",
      "description": "A 5-10 word summary, shown as preview in the UI (required for message, broadcast)"
    },
    "approve": {
      "type": "boolean",
      "description": "Whether to approve the request (required for shutdown_response, plan_approval_response)"
    },
    "request_id": {
      "type": "string",
      "description": "Request ID to respond to (required for shutdown_response, plan_approval_response)"
    }
  }
}
```

## When Agent Teams Are Actually Better Than Sub-Agents

It's hard to tell whether anthropic will sunset sub-agent and just use agent teams, but this new structure open up loads of imagination as it offers a more sophisticated communication channel & context sharing

One example I liked from their official doc is for deep debug:

> Users report the app exits after one message instead of staying connected. Spawn 5 agent teammates to investigate different hypotheses. Have them talk to each other to try to disprove each other's theories, like a scientific debate. Update the findings doc with whatever consensus emerges.

I used this for @SuperDesignDev and it works great; But the trade-off is a lot more token consumption and speed; So i dont think agent team directly replace sub agents, yet;

I can imagine this agent team + some sort of ralph loop can put together structure for extremely long running agentic tasks completion;

Keen to see what use cases you guys come up with, comment below!

---

If you enjoy this and want to dive deeper, you can join @aibuilderclub_ where we share latest learnings on AI coding + agent building weekly.

**Engagement:** 6 replies, 49 reposts, 377 likes, 774 bookmarks, 44.4K views
**Posted:** 2:47 AM · Feb 7, 2026