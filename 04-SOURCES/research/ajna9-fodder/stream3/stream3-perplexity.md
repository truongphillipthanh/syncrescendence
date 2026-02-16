Anthropic has not yet published a full "God‑Mode" spec for Claude Code, but there is enough emerging documentation, SDK detail, and community experimentation to sketch a high‑confidence architecture and to call out where you're in uncharted territory. Below is a concise, phase‑aligned synthesis with explicit caveats and concrete config/SOP patterns.

***

## Phase 1 – Runtime "Physics" (Tasks, Compaction, Skills)

### 1. Task primitive & dependency graph

**What we can ground:**

- The CLI exposes a `TaskUpdate` tool plus a list tool (often called `TaskList`) for manipulating a persistent task graph. Community docs summarize it as "TaskUpdate: update task state; TaskList: list all tasks." [facebook](https://www.facebook.com/groups/3928385267460239/posts/3951927025106063/)
- Tasks **vanish with the conversation** unless you set `CLAUDE_CODE_TASK_LIST_ID`, which binds that task list to a project‑wide logical ID that persists **across separate sessions and terminals.** [x](https://x.com/algillera?lang=eu)
- Concrete behavior reported: "Set `CLAUDE_CODE_TASK_LIST_ID=<project-name>` and as long as the project name stays the same, you can open multiple windows and keep the same tasks," including "close your laptop, return tomorrow with the same `CLAUDE_CODE_TASK_LIST_ID`, and the task state is still there." (https://x.com/ghumare64/status/2015475110883254738)

**Implications for your architecture:**

- You can treat the task list as a **shared, project‑scoped state machine** across multiple CLI instances, anchored by `CLAUDE_CODE_TASK_LIST_ID`. Medium confidence this is backed by Anthropic's backend, not local files, so you get atomic updates at the API level, but there is **no public guarantee** of ACID or cross‑instance locking semantics.  
- Dependencies are explicitly supported via `TaskUpdate` adding `blockedBy` links (usually surfaced to the user as `addBlockedBy`/"blocked by task X"). A Shipyard integration example shows hooks that listen to `TaskUpdate` status changes, reinforcing that status and dependency edges are modeled as first‑class fields on the task. [southbohemia-edu-marroquin.blogspot](https://southbohemia-edu-marroquin.blogspot.com/?page=en-git-schoolai-shipyard-1769146107797)

**Can Tasks replace `plan.md` as the central bus?**

- For **coordination metadata** (status, assignee, dependencies, high‑level summaries), yes: tasks are clearly designed to be a persistent "work graph" across CLI sessions.  
- For **rich, longform plans**, you still want files (`plan.md`, `ARCHITECTURE.md`) because:  
  - Task descriptions will be truncated by context and compaction.  
  - The public material does not show tasks as version‑controlled documents; they are more like tickets than blueprints.  

**Confidence:** High that `CLAUDE_CODE_TASK_LIST_ID` gives you cross‑session, multi‑terminal persistence; medium that multiple concurrent CLIs will behave safely under simultaneous writes (no evidence of race bugs, but also no explicit guarantees).

***

### 2. Context compaction & session TTL

**What we know:**

- The Agent SDK exposes `autoCompact: true` and describes **automatic summarization of older context when approaching token limits**. [kane](https://kane.mx/posts/2025/context-engineering-secrets-claude-code/)
- A changelog‑style review describes Claude Code's compaction as "simply summarize the session unless you explicitly specify compaction instructions" and recommends explicit `/clear` or manual compaction to "keep the context window clean." [dev](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)
- Users on 2.1.7 report a **buggy effective limit**: context hitting "limit reached" around 165–175k tokens despite a 200k nominal window, even with auto‑compact disabled. This indicates the window math and compaction interplay are not perfectly transparent. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1qczpzg/anyone_else_getting_context_limit_reached_in/)

**Tasks and plans vs compaction:**

- Anthropic marketing and community write‑ups repeatedly emphasize that **structural artifacts** (Tasks, Plans, and the filesystem) are the stable memory, while the **chat transcript** is what gets compacted. The v2.1 line and SDK docs say compaction "summarizes older context," not that it deletes Tasks. [kane](https://kane.mx/posts/2025/context-engineering-secrets-claude-code/)
- Third‑party guides explicitly push "build your memory in files and task systems; expect context to rot unless you compact aggressively or reset often." [octospark](https://octospark.ai/blog/the-comprehensive-guide-to-claude-code)

**Do Tasks persist "through" compaction?**

- Evidence strongly suggests yes: users rely on `CLAUDE_CODE_TASK_LIST_ID` to see the same task states **even after closing sessions and returning**, which is much stronger than "survives compaction." (https://x.com/ghumare64/status/2015475110883254738)
- There is no credible report of Tasks being lost by compaction; complaints focus on **conversation quality degradation** and premature "context limit reached," not task disappearance. [dev](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

**TTL recommendation:**

You won't get a formal equation from Anthropic, but given:

- 200k nominal window,  
- compaction summarization introduces lossy compression of older conversational turns,  
- community reports of quality degradation and early limit errors near 165–175k tokens, [reddit](https://www.reddit.com/r/ClaudeAI/comments/1qczpzg/anyone_else_getting_context_limit_reached_in/)

a practical TTL for a single session before hard reset:

- **For high‑stakes engineering:**  
  - Reset every **50–80k tokens** of *conversation* (not counting tool output), or whenever:  
    - You see multiple "did we already…?" confusions, or  
    - You've changed the architecture significantly and want a fresh mental model.  
- Use a **"Librarian" skill** (see Phase 3.9) to snapshot into `STATE.json`/`DIGEST.md` before a reset.  

**Confidence:** High that Tasks/Plans are structurally persistent across compaction; medium on exact token thresholds due to version‑specific bugs.

***

### 3. Skill/Command merge, `agent` field, and subagent scoping

**What is documented:**

- Official skills docs now describe Skills as the general extension mechanism; with frontmatter fields `context` and `agent`: [code.claude](https://code.claude.com/docs/en/skills)
  - `context: fork` runs the skill in a **forked subagent context**.  
  - `agent` chooses which subagent type (Explore, Plan, etc.) executes it when `context: fork` is set. [code.claude](https://code.claude.com/docs/en/skills)
  - Without `context: fork`, `agent` alone "does nothing" – it's the combination that turns the Skill into a subagent. [github](https://github.com/anthropics/claude-code/issues/12633)
- Skills with `context: fork` load: system prompt from agent type + the skill markdown body as the **task** + project `CLAUDE.md`. [code.claude](https://code.claude.com/docs/en/skills)
- A separate path is "subagent with `skills` field," where a subagent's markdown body acts as system prompt and preloads referenced skills and `CLAUDE.md`. [code.claude](https://code.claude.com/docs/en/skills)
- Commentary on the convergence of subagents, commands, and skills notes that `context: fork` gives skills "their own context window", effectively collapsing earlier subagent constructs into forked skills. [vivekhaldar](https://www.vivekhaldar.com/articles/claude-code-subagents-commands-skills-converging/)

**Does `context: fork` copy the whole history?**

- Docs show the forked context loads:  
  - The **agent template** (Explore/Plan/etc.) as system behavior,  
  - The skill content as the **task**,  
  - `CLAUDE.md` as shared project rules. [code.claude](https://code.claude.com/docs/en/skills)
- There is no indication that it clones the entire transient conversation history; the mental model is: **new agent, same project memory, new task**.  

**Can a skill spawn recursive subagents?**

- A skill with `context: fork` is already running as a subagent. Within that skill's execution, Anthropic's orchestrator still has tool access, including the ability to call other skills or subagents. However:  
  - There is **no explicit guarantee** in current docs that you get arbitrarily deep nesting; you only see the first‑class pattern "Skill → forked agent → uses tools and skills." [vivekhaldar](https://www.vivekhaldar.com/articles/claude-code-subagents-commands-skills-converging/)
  - In practice, any such recursion is limited by the outer agent's orchestration policy and total context budget; you can't reliably create unbounded depth.  

**Fractal topology feasibility:**

- Supported and stable:  
  - **Flat + 1‑level fork:** root agent → forked skills (Explore/Plan/Implement/QA) each with their own context and access to skills + `CLAUDE.md`. [octospark](https://octospark.ai/blog/the-comprehensive-guide-to-claude-code)
- Experimental but plausible:  
  - Skill A forks an Explore agent which, during its task, invokes Skill B with `context: fork` to spin a nested subagent. Documentation doesn't forbid it, but you're layering orchestration inside orchestration; expect fragile behavior and compaction side‑effects.  

**Confidence:** High regarding semantics of `context: fork` and `agent`; low‑to‑medium on stable, deeply recursive subagent trees.

***

## Phase 2 – Frontier Patterns & Emergent "Dark Matter"

### 4. Recursive self‑improvement of `CLAUDE.md` / skills

**Evidence of self‑healing patterns:**

- A Claude‑focused guide describes a "compound quality" loop: **every bug yields tests and new rules added to `Claude.md`**, explicitly positioning the config as a living constitution that accretes anti‑patterns and hardening rules over time. [octospark](https://octospark.ai/blog/the-comprehensive-guide-to-claude-code)
- An "Observability‑Driven Skill Improvement" skill automates the self‑improvement lifecycle of skills, promoting a "self‑healing and self‑optimizing environment" for Claude‑driven development. It focuses on: [mcpmarket](https://mcpmarket.com/tools/skills/observability-driven-skill-improvement)
  - Logging skill outcomes,  
  - Analysing failures,  
  - Updating the skill behavior or associated documentation.  
- Advanced orchestration frameworks (e.g., Claude Flow v3) expose hooks such as `memory:post-store`, `swarm:consensus-reached`, etc., suitable for wiring regression or anomaly data back into configuration. [github](https://github.com/ruvnet/claude-flow)

**What is *not* clearly observed yet:**

- Strong, public examples where Claude **spontaneously decides** to modify `CLAUDE.md` or `SKILL.md` **without any meta prompt** or external automation. Most patterns are human‑designed loops where:  
  - Hooks or scripts call Claude with an explicit "update the rules given this log" instruction. [mcpmarket](https://mcpmarket.com/tools/skills/observability-driven-skill-improvement)

**Designing a "Self‑Healing Constitution" loop:**

The highest‑confidence pattern today:

1. Instrumentation  
   - Attach `PostToolUse` hooks (or equivalent orchestration hooks) to capture: failing tests, lints, runtime errors, and unclear tool calls. [github](https://github.com/ruvnet/claude-flow)
2. Analysis agent  
   - Dedicated "Constitution Editor" skill with `context: fork` + `agent: Plan`; restrict it to **read‑write** on `CLAUDE.md` and `skills/`. [code.claude](https://code.claude.com/docs/en/skills)
3. Edit policy  
   - Prompt the editor to:  
     - Convert repeated failure patterns into new **rules** or **checklists** in `CLAUDE.md`.  
     - For recurring tool errors, propose **new skills** and, after human approval (or automated gating), add them.  
4. Regression guard  
   - Require that any proposed constitution change is accompanied by a small test plan or invariants to avoid rule bloat.  

**Confidence:** High that such loops are feasible (there are off‑the‑shelf skills aimed at this); low that they yet exhibit fully autonomous, open‑ended self‑modification without human‑designed guardrails.

***

### 5. Headless orchestration & CI/CD

**Headless (`-p`) capabilities:**

- Guides and examples show heavy use of **headless, print‑only** runs for CI and automation: `claude -p "Design spec" > spec.md`, hooking this into GitHub Actions for fully autonomous pipelines. [octospark](https://octospark.ai/blog/the-comprehensive-guide-to-claude-code)
- Claude Flow builds on this concept with "always‑on daemon" behavior, scheduled workers, and continuous mapping/optimization of repos. [claude-flow.ruv](https://claude-flow.ruv.io)

**Daisy‑chaining headless instances:**

- The pattern you propose is exactly how people are already composing agents:  
  - Agent A (headless) writes `spec.md`, which is then consumed by Agent B (headless) with a different prompt.  
- Existing "swarm" orchestrators such as Claude Flow:  
  - Use the **filesystem as a message bus** (files for tasks, state, logs),  
  - Run background workers that watch directories and Git events,  
  - Use hooks like `file:pre-read/post-read` and swarm events to coordinate multi‑agent workflows. [claude-flow.ruv](https://claude-flow.ruv.io)

**Serverless agency blueprint:**

- GitHub Actions / CI layer:  
  - Trigger on PRs, pushes, or labels.  
  - Use `claude -p` (or Flow equivalents) to: generate specs, refactors, tests, docs.  
- Local daemon (or self‑hosted runner):  
  - Run as a Claude Flow swarm or a custom watcher that:  
    - Watches repo and task list,  
    - Schedules specialized agents (exploration, refactor, QA) as separate headless runs,  
    - Writes outputs to files and tasks instead of chat.  

**Confidence:** High – these patterns are in active use in public frameworks and guides. [github](https://github.com/ruvnet/claude-flow)

***

### 6. Context injection vs "true" RAG

**Current state of Claude Code retrieval:**

- A detailed critique from Milvus notes that **Claude Code "doesn't use RAG at all," instead effectively grepping the repo line by line**, with obvious efficiency limits on large codebases. [milvus](https://milvus.io/blog/why-im-against-claude-codes-grep-only-retrieval-it-just-burns-too-many-tokens.md)
- Developers compare it unfavorably to tools like Cursor that pre‑index repositories with embeddings. [reddit](https://www.reddit.com/r/LLMDevs/comments/1nw2duk/whats_the_best_indexing_toolrag_setup_for_claude/)

**Custom indexing scripts vs MCP RAG:**

- Community discussions for large repos (>100k LoC) describe two main patterns: [youtube](https://www.youtube.com/watch?v=qN3vhWlzd4A)
  - **CLI‑native exploration**: use `fd`, `ripgrep`, globbing, and manual narrowing (sometimes via skills) to have Claude iteratively explore.  
  - **External RAG**: run a vector index (Milvus, pgvector, etc.), expose it via MCP, and have Claude query it.  
- The Milvus piece explicitly argues that **grep‑only retrieval burns tokens and misses semantics**; they advocate for embedding‑based indexing for both speed and reduction of hallucination. [milvus](https://milvus.io/blog/why-im-against-claude-codes-grep-only-retrieval-it-just-burns-too-many-tokens.md)
- RAG vs long‑context tradeoffs discussed generally (not Claude‑specific):  
  - Long context is good for single, deeply entangled tasks but expensive and prone to "smearing" attention.  
  - RAG excels when you need **repeated, sparse access** to relevant slices of a large corpus. [youtube](https://www.youtube.com/watch?v=qN3vhWlzd4A)

**Practical position:**

- For your "super‑orchestrator" scenario with big repos:  
  - Use **MCP‑based RAG** for semantic retrieval and cross‑file reasoning.  
  - Use **context injection** (`CLAUDE.md`, `DIGEST.md`, `STATE.json`) for **meta‑maps, rules, and task graphs**.  
  - Use **custom CLI scripts (`fd`, `rg`, etc.)** for high‑precision pattern searches, but not as the only retrieval mechanism.  

**Confidence:** High on limitations of grep‑only retrieval; high that hybrid (MCP RAG + injection) is superior at scale. [reddit](https://www.reddit.com/r/LLMDevs/comments/1nw2duk/whats_the_best_indexing_toolrag_setup_for_claude/)

***

## Phase 3 – Hypothetical Architectures

These are plausible constructions built atop current primitives; they are not yet widely documented as complete systems.

### 7. "Git‑Based Neural Bus"

**Feasibility:**

- Nothing in Claude Code prevents multiple instances running in different `git worktree`s with shared remote. Guides encourage worktrees for parallel dev. [octospark](https://octospark.ai/blog/the-comprehensive-guide-to-claude-code)
- Git is naturally a **distributed ledger** of structured messages (commits), with timestamps, authors, and branches.  

**Practical pattern:**

- Worker agents:  
  - Each worktree has its own `CLAUDE.md` / skills tuned to a role (Backend, Frontend, QA, Refactor).  
  - Each commit message follows a **structured schema** \(e.g., `ROLE: TASK_ID: SUMMARY | INPUT_DIGEST | OUTPUT_DIGEST`.\)  
- Oracle agent:  
  - Runs in a central worktree with an "Oracle" `CLAUDE.md`.  
  - Periodically runs `git log` and `git show` to:  
    - Track per‑task progress,  
    - Detect conflicting edits,  
    - Annotate Tasks (via `TaskUpdate`) with state derived from commit metadata.  
- Message semantics:  
  - Commits from workers = **"thoughts"** or **"actions"**.  
  - Oracle comments or PR reviews = feedback and updated plans.  

**Risks and caveats:**

- Latency: Git is not a low‑latency message bus; you pay for commits and pulls.  
- Conflicts: Without discipline, you risk merge hell.  
- Observability: You'll likely want an MCP or local daemon that synthesizes `git log` into human‑readable dashboards.  

**Confidence:** Medium – conceptually sound and aligned with existing "git‑centric" workflows, but not yet widely case‑studied.

***

### 8. "MCP‑as‑OS" (Semantic OS)

**State of MCP for DevOps:**

- The MCP ecosystem is rapidly evolving and includes servers for: databases, clouds, Kubernetes, Docker, monitoring, etc. (see MCP marketplaces and public server lists, including "DevOps" abstractions). [mcpmarket](https://mcpmarket.com/tools/skills/observability-driven-skill-improvement)
- Advanced orchestration platforms for Claude (e.g., Claude Flow) treat MCP servers as the primary action surface: tools for code, infra, monitoring, and workflows. [claude-flow.ruv](https://claude-flow.ruv.io)

**Can Claude replace the shell?**

- For many DevOps flows, **yes in principle**:  
  - "Deploy this service" → MCP tool that calls the right cloud APIs.  
  - "Scale this cluster" → MCP that talks to Kubernetes.  
  - "Rotate secrets" → MCP for your secrets manager.  
- A "Semantic OS" architecture would look like:  
  - **Core agent**: orchestrator defined by `CLAUDE.md` and a set of skills.  
  - **MCP servers**: each representing OS‑level capabilities (FS, processes, networking, cloud APIs).  
  - **Human**: interacts only via natural language and high‑level tasks.  

**Constraints:**

- You still rely on an underlying OS runtime (for MCP servers) and must handle **permissions, security, and rate limits**.  
- You will hit the boundaries of tool schema expressiveness and error handling—complex shell pipelines may still be easier in native scripting for now.  

**Confidence:** Medium‑to‑high that you can implement "OS as MCP" for many workflows; low that you can *fully* retire traditional shell interaction for everything.

***

### 9. "Hyper‑Compacted Memory Crystal"

**Existing ingredients:**

- Guides stress the power of **DIGEST.md** or summary files to carry context across sessions and services. [octospark](https://octospark.ai/blog/the-comprehensive-guide-to-claude-code)
- Context‑engineering articles recommend structuring long‑term memory into hierarchical files and using targeted summarization strategies. [kane](https://kane.mx/posts/2025/context-engineering-secrets-claude-code/)
- General LLM practice (e.g., "70/80 rule" style heuristics) suggests: capture ~70–80% of the information density with carefully structured summaries optimized for model ingestion. [youtube](https://www.youtube.com/watch?v=qN3vhWlzd4A)

**Proposed protocol:**

- Librarian skill (`context: fork`, `agent: Plan`):  
  - Input: current Tasks, key files touched, recent logs.  
  - Output: `STATE.json` + `MEMORY.md` with:  
    - Task graph snapshot,  
    - Open questions,  
    - Key architectural decisions,  
    - Pointers (paths + line ranges) to canonical sources.  
- Schema heuristic (for ingestion efficiency):  
  - Keep JSON flat, avoid verbose prose.  
  - Use stable IDs (`task_id`, `decision_id`) and references to files rather than embedding entire code.  
  - Enforce size caps (e.g., "no more than N tokens for each section").  

**Losslessness caveat:**

- You cannot get truly lossless compression under current models; summarization is inherently lossy.  
- What you can approximate is **task‑sufficient state**: enough structured data and pointers that a new agent can reconstruct necessary context cheaply.  

**Confidence:** High that such patterns work well in practice; low that you can guarantee "perfect" losslessness.

***

## Phase 4 – Concrete Outputs

Below are **lightweight but opinionated** artifacts you can adapt. They assume:

- You're using Tasks (`TaskUpdate`, `TaskList`) with `CLAUDE_CODE_TASK_LIST_ID`.  
- You run multiple worktrees for parallel agents.  
- You have MCP servers for filesystem, Git, and (optionally) RAG and DevOps.

### 1. "God‑Config" (settings, CLAUDE.md, MCP)

#### 1.1 `settings.json` (CLI / workspace)

Example skeleton:

```json
{
  "model": "claude-3-5-sonnet-20241022",
  "autoCompact": true,
  "thinkingBudget": 16000,
  "maxTurns": 80,
  "taskListIdEnv": "CLAUDE_CODE_TASK_LIST_ID",
  "defaultAgents": {
    "orchestrator": "Orchestrator",
    "explore": "Explore",
    "implement": "Implement",
    "qa": "QA",
    "refactor": "Refactor"
  },
  "skills": {
    "enabled": [
      "skills/deep-research",
      "skills/librarian",
      "skills/self-heal",
      "skills/oracle-sync"
    ]
  }
}
```

Rationale:

- `thinkingBudget` and `autoCompact` mirror SDK knobs for reasoning vs performance. [kane](https://kane.mx/posts/2025/context-engineering-secrets-claude-code/)
- `maxTurns` ~80 gives room but still encourages periodic "save state and reset." [dev](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

#### 1.2 `CLAUDE.md` (project constitution – abbreviated)

```markdown
# Claude Constitution for This Repo

## Mission
You are the **Orchestrator** of a multi-agent development fleet.
Your responsibilities:
- Maintain the task graph as the source of truth for work.
- Decompose goals into small, testable tasks with clear dependencies.
- Keep `CLAUDE.md`, `STATE.json`, and `MEMORY.md` up to date.

## Hard Rules
- Never modify infra or prod without explicit task and human approval.
- Prefer creating/using skills instead of ad-hoc, one-off flows.
- Every bug or failure must result in:
  - ≥3 regression tests, and
  - An update to this file or a relevant skill if it reveals a recurring pattern.

## Tasks and Planning
- Treat the Task list as the canonical backlog.
- When given a new goal:
  1. Create/Update a parent Task with a clear description.
  2. Decompose into child Tasks with `blockedBy` edges.
  3. Keep Task statuses current (`todo`, `in_progress`, `blocked`, `done`).

## Context Hygiene
- Prefer reading source files, `STATE.json`, and `MEMORY.md` over relying on old chat.
- Before the context window becomes saturated:
  - Call the `librarian` skill to refresh `STATE.json` and `MEMORY.md`.
  - Ask for a session reset once state is saved.

## Code Quality and Tests
- For every non-trivial change:
  - Update or add tests.
  - Run tests or ask a QA subagent to run them.
- For recurring failure patterns:
  - Add an "Anti-Pattern" rule here.
  - If appropriate, create/update a dedicated skill.

## Subagents
- Use specialized agents:
  - Explore: discovery, reading, mapping.
  - Plan: decomposition, design, coordination.
  - Implement: coding and refactors.
  - QA: tests, static analysis, validation.
- Use skills with `context: fork` for long-running or isolated tasks.

## Anti-Patterns
- Do not re-implement tools that exist as MCP servers.
- Do not perform large, sweeping refactors without a written plan and Tasks.
- Avoid relying solely on grep-based exploration for large repos; prefer RAG MCP when available.
```

This codifies your "Fleet Commander" and self‑healing rules using patterns advocated in existing autonomous‑development guides. [kane](https://kane.mx/posts/2025/context-engineering-secrets-claude-code/)

#### 1.3 `.mcp.json` (MCP stack – sketch)

```json
{
  "servers": {
    "filesystem": {
      "type": "http",
      "url": "http://localhost:7401"
    },
    "git": {
      "type": "http",
      "url": "http://localhost:7402"
    },
    "rag-code": {
      "type": "http",
      "url": "http://localhost:7500"
    },
    "devops": {
      "type": "http",
      "url": "http://localhost:7600"
    }
  }
}
```

- `rag-code` abstracts vector search over your repo; aligns with RAG critiques and recommendations. [milvus](https://milvus.io/blog/why-im-against-claude-codes-grep-only-retrieval-it-just-burns-too-many-tokens.md)
- `devops` is your "Semantic OS" gateway (Kubernetes, cloud APIs). [github](https://github.com/ruvnet/claude-flow)

***

### 2. "Oracle Protocol" – Human Fleet Commander SOP

**Goal:** Use Tasks as the unified bus while coordinating a multi‑agent swarm.

1. **Initialize project & task list**

   - Export a stable ID:  
     - `export CLAUDE_CODE_TASK_LIST_ID="my-project-main"`  
   - Ensure `CLAUDE.md`, `settings.json`, `.mcp.json`, and skills (`/skills`) are checked into the repo.  

2. **Create top‑level mission**

   - Start an Orchestrator session.  
   - Prompt pattern:  
     - "Create a parent Task for 'Implement feature X' and decompose into 5–15 sub‑tasks with clear `blockedBy` relations. Use TaskUpdate and show me the resulting graph."  
   - Verify the graph via Task list (CLI or a custom skill).  

3. **Assign work to subagents (per worktree)**

   - Create separate `git worktree`s for major roles:  
     - `worktrees/backend`, `worktrees/frontend`, `worktrees/qa`, `worktrees/refactor`.  
   - In each worktree, start Claude with the same `CLAUDE_CODE_TASK_LIST_ID` but a role‑specific agent or `CLAUDE.md` overlay.  

4. **Operate in "Task mode"**

   - For each work session, instruct the agent:  
     - "Pick a `todo` task assigned to your role, mark `in_progress`, do the work, then mark `done` or `blocked` with a reason."  
   - Enforce that **every code change references a `task_id` in the commit message**, enabling the Git‑based neural bus.  

5. **Orchestrator governance loop**

   - Periodically (or via a scheduled headless agent):  
     - Read the Task graph and `git log`.  
     - Detect stalled tasks, conflicting branches, or structural issues.  
     - Create new Tasks (e.g., "Refactor module Y") and reassign as needed.  

6. **Self‑healing & constitution updates**

   - Wire `PostToolUse` (or an orchestration hook) to feed failures (test failures, tool errors) to the "Constitution Editor" skill.  
   - As Fleet Commander:  
     - Review proposed `CLAUDE.md` and skill edits.  
     - Approve/commit them, or instruct the agent to revise.  

7. **Session hygiene**

   - When conversation quality degrades or token usage is high:  
     - Run the `librarian` skill to regenerate `STATE.json` and `MEMORY.md`.  
     - Close session and start a fresh one, pointing it at the same Tasks and memory files.  

This pattern leverages both task persistence and multi‑worktree Git flows, with human‑in‑the‑loop governance. [facebook](https://www.facebook.com/groups/3928385267460239/posts/3951927025106063/)

***

### 3. "Recursion Hook" – PostToolUse self‑update script

You can implement this either via:

- Claude Flow / orchestrator hooks (e.g., `tool:post-run`, `memory:post-store`), or [github](https://github.com/ruvnet/claude-flow)
- A custom wrapper around the CLI that parses JSON transcripts and calls Claude again.

Below is a conceptual **pseudo‑hook** that you adapt to your environment:

```ts
// postToolUse-hook.ts
// Runs after every tool call in a session.

import { spawnSync } from "node:child_process";
import fs from "node:fs";

type ToolResult = {
  toolName: string;
  success: boolean;
  errorMessage?: string;
  taskId?: string;
};

function runClaude(prompt: string, extraFiles: string[] = []) {
  const cmd = [
    "claude",
    "-p",
    prompt,
    ...extraFiles.flatMap(f => ["--file", f])
  ];
  return spawnSync(cmd, cmd.slice(1), { encoding: "utf8" });
}

export function onPostToolUse(result: ToolResult) {
  if (result.success) return;

  const logEntry = {
    timestamp: new Date().toISOString(),
    tool: result.toolName,
    error: result.errorMessage,
    taskId: result.taskId ?? null
  };

  fs.appendFileSync(".claude/errors.log", JSON.stringify(logEntry) + "\n");

  const prompt = `
You are the Constitution Editor for this repo.

An error occurred in a Claude Code tool call.

Error payload:
${JSON.stringify(logEntry, null, 2)}

Your job:
1. Identify whether this represents a recurring pattern that should be addressed in CLAUDE.md or a dedicated skill.
2. If yes, propose a minimal patch to CLAUDE.md and/or a new/updated SKILL.md file.
3. Output a unified diff (patch format) only. Do not include explanations.

Be conservative: prefer small, precise rules over broad or vague policies.
`;

  const res = runClaude(prompt, ["CLAUDE.md"]);
  if (res.status === 0 && res.stdout.trim()) {
    fs.writeFileSync(".claude/pending-constitution.patch", res.stdout);
    // Optional: auto-apply patch after human review step in CI
  }
}
```

**How it functions:**

- Every failed tool call logs an entry and triggers a **secondary Claude run** in "Constitution Editor" mode.  
- The editor proposes a small patch to `CLAUDE.md` or skills, encoded as a diff.  
- You then decide (manually or via CI policy) whether to apply patches automatically.  

This follows the same logic as "Observability‑Driven Skill Improvement" and the self‑healing architectures already demonstrated in the ecosystem. [mcpmarket](https://mcpmarket.com/tools/skills/observability-driven-skill-improvement)

***

## Caveats and Confidence Map

- **High confidence:**  
  - Task system semantics (persistence via `CLAUDE_CODE_TASK_LIST_ID`, TaskUpdate usage). (https://x.com/algillera?lang=eu)
  - Skills/Commands merge, `context: fork` + `agent` behavior. [github](https://github.com/anthropics/claude-code/issues/12633)
  - Need for explicit context hygiene and summary artifacts. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1qczpzg/anyone_else_getting_context_limit_reached_in/)
  - Benefits of MCP‑based RAG over pure grep for large repos. [reddit](https://www.reddit.com/r/LLMDevs/comments/1nw2duk/whats_the_best_indexing_toolrag_setup_for_claude/)
  - Feasibility of headless swarms and CI/Daemon orchestration (Claude Flow, etc.). [claude-flow.ruv](https://claude-flow.ruv.io)

- **Medium confidence:**  
  - Effective session TTL heuristics in the presence of compaction bugs. [dev](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)
  - Stability of multi‑level recursive subagents.  
  - Robustness of Git‑based neural bus in large, highly parallel teams.  

- **Low confidence / speculative:**  
  - Truly autonomous, unbounded recursive self‑improvement without human gating.  
  - Perfectly lossless "memory crystal" architectures; in practice you always trade off detail vs cost.  

If you'd like, next we can tighten this into a concrete repo layout (directory tree, example skills, and a minimal Claude Flow swarm config) that you can literally clone and start iterating on as your "God‑Mode" template.