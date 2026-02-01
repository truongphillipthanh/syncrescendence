Claude Code is best thought of as an extensible, CLI‑first agent runtime that can drive your whole environment (files, shell, MCP tools, desktop, web) under explicit human supervision, with persistent project scaffolding (CLAUDE.md, settings, skills) that makes it behave like a specialized knowledge worker rather than a generic chatbot.[1][2] Used well, its value is less “better autocomplete” and more “coordinated execution engine” sitting between your orchestration layer (your Oracles) and a heterogeneous tool surface.

Below is a synthesis aimed at architectural understanding and multi‑agent orchestration, not feature inventory.

***

## Part 1: Capability architecture

**Mental model vs IDE tools**

- Claude Code is **CLI‑first, editor‑agnostic**, designed to run in terminals, CI, remote servers, and now also via a web/desktop “code” surface; Cursor/Windsurf are IDEs that embed AI into a GUI editor loop.[3][1]
- Cursor focuses on inline, single‑file edits and embeddings indices inside the editor; Claude Code focuses on multi‑file, multi‑tool workflows where the model issues file, shell, MCP, and (via Desktop) GUI actions as tools.[3][1]

**Tooling surface (execution engine)**

At a high level, Claude Code exposes the model to four main tool classes:

- **Filesystem tools**: read, diff, write, create, delete, search, and multi‑file edit across an arbitrary repo or workspace, with explicit permissions and visible plans in Plan Mode.[2][4]
- **Shell/Bash tools**: execute commands (build, test, run scripts, CLI‑driven automation) with granular permissions; hooks and preconfigured permissions can pre‑allow or veto commands.[5][6]
- **MCP tools**: Model Context Protocol servers expose external systems (GitHub, Slack, Google Drive, BigQuery, etc.) as structured tools; Claude Code reads `.mcp.json`/`~/.claude.json` to discover servers.[7][4]
- **Desktop/web control (via Desktop/GUI use)**: when connected through Claude Desktop and web “computer use” APIs, Claude can operate browsers and GUIs (clicking, typing, following flows), effectively expanding the tool surface to any GUI‑driven system.[8][9]

This means your “execution engine” is not just a code editor: it is an agent that can:

- Traverse and refactor large repos.  
- Run tests, deploy scripts, analytics queries, or scraping pipelines.  
- Call MCP servers to talk to SaaS systems (Slack, GitHub, ticketing, storage).  
- Drive GUI flows when no API exists.[7][8]

**Context management and degradation**

- Claude Code uses **on‑demand file reads** and transcript history rather than a prebuilt embeddings index; it stays within the model’s ~200K context window by deciding what to read and when.[1][2]
- **Compaction** (`/compact`) summarizes prior turns and tool traces into a smaller latent state; hooks, CLAUDE.md, and files on disk become the “stable memory,” while the chat log gets compressed.[4][2]
- Practitioners report that performance degrades **before** the hard context limit — long transcripts lead to slower, more error‑prone reasoning, so compaction and good externalization (CLAUDE.md, docs, logs) are key.[8][10]

**Surfaces: CLI, Desktop, web code**

- **CLI**: `claude` is the primary runtime; it owns session transcripts, hooks, MCP configs, and slash commands, and can be scripted or run headless for automation.[7][2]
- **Desktop app**: embeds Claude chat + Claude Code, adds OS‑level integration (file browser, “use my computer,” notifications) and easier GitHub/Drive integrations.[9][11]
- **Web code interface** (`claude.ai/code` / “Code” projects): a browser‑based view that mirrors the Claude Code mental model—file tree, tools, Plan Mode—but runs in Anthropic’s environment.[9][11]

The same conceptual stack appears in all three, but the CLI has the deepest hooks, MCP, and scripting affordances; Desktop/web are better for GUI/knowledge‑work centric tasks and managed integrations.[7][9]

**Skills, plugins, MCP, subagents**

- **Skills**: reusable, named workflows defined in `~/.claude/skills` or `.claude/skills`; they can specify prompts, default tools, models, and even attach custom agents; hot‑reloaded in recent versions.[8][5]
- **Slash commands**: lightweight commands in `.claude/commands/` that wrap shell/Python/other scripts and present them as `/command` from within a session.[5][4]
- **MCP servers**: external “plugins” exposing tools/resources/prompts (e.g., Slack, GitHub, Google Drive); configured in `~/.claude.json` or `.mcp.json` with per‑scope control.[7][4]
- **Subagents**: Claude Code can spawn short‑lived subagents for specific tasks (notably in skills and complex plans) that operate in isolated contexts and return artifacts back to the main agent.[8][2]

The extensibility gradient is: slash commands for simple shell glue; hooks for lifecycle automation; skills for reusable, higher‑level workflows; MCP for integrating entire systems as tools; and subagents for internal parallelism.

***

## Part 2: Configuration deep dive

**CLAUDE.md hierarchy**

Anthropic treats `CLAUDE.md` as the primary mechanism for encoding persistent norms and project knowledge.[4][10]

- **User/global**: `~/.claude/CLAUDE.md` — your default working style, safety rules, language preferences, general instructions across projects.[4]
- **Project**: `CLAUDE.md` at repo root or `.claude/CLAUDE.md` — project‑specific policies (architecture, coding conventions, deployment rules, “never touch prod,” etc.).[4][10]
- **Local/variant**: `.claude/CLAUDE.local.md` and other overlays (like branch‑local) can tweak behavior without touching shared files.[4]
- **Subdirectory**: nested `CLAUDE.md` files in subfolders refine instructions for that area (e.g., “docs/ CLAUDE.md” for documentation standards).[4]

Claude merges these hierarchically; Boris’s team uses this as a **learning artifact**: every time Claude makes a mistake, they update the shared CLAUDE.md so it is not repeated.[10] This is essentially externalized, versioned “institutional memory.”

**What persists across sessions**

- **CLAUDE.md and config files**: all scope‑appropriate CLAUDE.md, `settings.json`, `managed‑settings.json`, MCP configs, skills, hooks, and commands persist on disk and apply to new sessions automatically.[4][7]
- **Named sessions and transcripts**: the CLI can save and resume named sessions; `/resume` and `--continue` pick up prior context, while `/teleport` can move a session between CLI and web.[8][2]
- **Skills**: stored under `~/.claude/skills` or `.claude/skills`, hot‑reloaded so changes become available without restarting.[8][5]

In contrast, the web app’s “memory” feature stores user preferences and long‑term facts at the account level but is logically separate; Claude Code primarily relies on local files and project configs as memory.[9][2]

**settings.json and hooks**

The configuration surface is split by scope and file type:

- **Settings**:  
  - User: `~/.claude/settings.json`  
  - Project: `.claude/settings.json`  
  - Local overrides: `.claude/settings.local.json`  
  - Managed: `managed‑settings.json` / `managed‑mcp.json` for centrally controlled org setups.[4][7]

Key configurable dimensions include:

- Permission defaults and wildcards (e.g., allow `Bash(*-h*)` without prompts).[8][5]
- Default model (Opus/Sonnet, “ultrathink” thinking tokens), temperature, language.[8][2]
- Hooks configuration: PreToolUse / PostToolUse definitions and matchers.[5][6]
- File suggestions, auto‑open behavior, Plan Mode defaults, and headless behavior.

**Hooks**

Hooks are shell commands or scripts that run at lifecycle points:

- **PreToolUse**: runs before a tool (FileEdit, Bash, MCP) executes; can inspect the payload and allow, modify, or block the call.[5][6]
- **PostToolUse**: runs after a tool executes; common patterns include formatting, running tests, logging, sending notifications, or updating external trackers.[5][8]

Hooks can:

- Check transcript path and detect Plan Mode, enabling different behaviors during planning vs execution.[6][5]
- Override permissions (e.g., auto‑grant for known safe commands) or enforce policy (e.g., block `rm -rf /`).[6][5]
- Be attached not only globally but also directly to agents/skills via frontmatter in newer versions.[8]

**Slash commands vs Skills**

- **Slash commands** (`.claude/commands/`):  
  - Thin wrappers around scripts or one‑off actions, invoked via `/name`.  
  - Good for “call this script with current project context or arguments,” e.g., `/sync-notion`, `/open-pr`.[5]

- **Skills** (`~/.claude/skills` or `.claude/skills`):  
  - Richer constructs specifying prompt, tools, hooks, model, and custom agent configuration.  
  - Invoked like modes or named agents; can run subagents, chain tools, and define defaults for Plan Mode behavior.[8][5]

The distinction: slash commands are “do this one thing”; skills are “be this role and run this workflow.”

**Custom subagents**

- Skills and configuration can define **custom agents** that act as subroles with their own prompts, tool restrictions, and sometimes dedicated hooks.[8][2]
- These subagents are spawned as needed (e.g., “doc writer,” “test synthesizer,” “summarizer”) and work in isolated contexts, passing artifacts back to the main agent.[8][10]

Architecturally, this is close to what you are building: a “fleet” of constrained roles coordinated at a higher level.

**Compaction and session continuity**

- `/compact` summarizes older transcript segments, keeping recent context and externalized artifacts (files, CLAUDE.md, logs) as the durable record.[2][4]
- Plan Mode + compaction best practices emerging from practitioners:  
  - Use Plan Mode to front‑load intent;  
  - Execute;  
  - Use `/compact` once a phase is complete, relying on CLAUDE.md and written docs as memory.[12][10]
- `/resume`, named sessions, and `--continue` allow you to treat sessions as long‑lived workers; `/teleport` moves that worker between surfaces (e.g., CLI to web) without losing context.[8][2]

***

## Part 3: Workflow patterns

**“Fleet of workers” rather than one giant brain**

- Boris explicitly treats each session as a **separate worker** with its own context; he runs multiple agents in parallel rather than trying to cram everything into one massive session.[10][13]
- Zvi’s write‑up similarly emphasizes short‑lived agents and subagents that pass artifacts rather than a monolithic agent that must “remember everything.”[8][14]

Generalizable principle: **specialize and isolate** agents by role; pass documents, not raw transcript state.

**Plan Mode → execution**

- Practitioners (and official guidance) stress Plan Mode as the default starting point: ensure Claude produces an explicit, checkable plan before edits, shell commands, or MCP calls.[12][2]
- Boris uses Plan Mode to converge on a high‑quality plan, then switches into auto‑accept mode to let Claude execute in one shot, minimizing micro‑supervision.[10]

Generalizable principle: treat planning as a **separate phase** with its own quality bar; once the plan is stable, commit to it and evaluate at the phase boundaries.

**CLAUDE.md as learning mechanism**

- Teams maintain shared CLAUDE.md files where any misbehavior or mistake is encoded as a new rule or clarification; this turns episodic failures into persistent, versioned memory.[10][2]
- For non‑coding work, this pattern extends naturally: add sections for domain concepts, decision criteria, tone guidelines, and “never do X” constraints for each knowledge domain.[10][4]

Generalizable principle: externalize “lessons learned” into structured, version‑controlled context rather than relying on a model’s ephemeral memory.

**Handling friction points**

- **Permission fatigue**: users pre‑allow specific tools/commands via settings and hooks; some use hooks to persist per‑directory permissions and reuse them across Plan Mode and execution.[6][5]
- **Context bloat**: heavy use of `/compact`, CLAUDE.md, and written docs; practitioners treat the transcript as disposable once the knowledge is extracted into durable artifacts.[8][10]
- **Verification failures**: PostToolUse hooks to run tests, linters, or validations; some GitHub workflows run Claude under CI with automated checks before humans see changes.[5][15]

What differentiates productive workflows from PKM‑for‑PKM’s‑sake:

- Artifacts are **used** by the system (CLAUDE.md, commands, hooks) rather than just hoarded.  
- There is a clear **pipeline** (spec → plan → execution → verification → documentation), with automations anchored to these stages.[10][2]

**Plan Mode → execution handoff**

- Effective users treat Plan Mode output as a **contract**: once agreed, they instruct Claude to execute without re‑negotiating each step.[12][10]
- Hooks and skills often encode post‑plan behavior: e.g., after a “refactor” plan is accepted, automatically run tests and log results to a dashboard.[5][8]

This suggests a pattern for your Oracles: produce plans in a high‑context, strategic session; hand those plans off as “contracts” to Claude Code–backed executors that operate largely autonomously within those constraints.

***

## Part 4: Integration landscape

**Claude Code vs Cursor**

| Aspect | Claude Code | Cursor |
| --- | --- | --- |
| Interface | CLI‑first, terminal, editor‑agnostic | GUI IDE (VS Code fork) integrated editor | 
| Context strategy | On‑the‑fly file reads, no embeddings index | Embeddings over codebase, inline context | 
| Scope of action | Filesystem, shell, MCP, desktop via Desktop | Mostly code edits and IDE‑adjacent tasks | 
| Models | Anthropic only | Multiple providers including Claude | 
| Mental model | “AI can use your computer like a developer”[1] | “Your editor has AI built in”[3] |

- Use **Claude Code** when you want an agent to orchestrate tools, repos, and systems — as in your multi‑agent architecture.[1][2]
- Use **Cursor** when you want high‑speed, inline coding assistance inside a GUI editor loop.[3][1]

**MCP servers**

- Commonly used MCP servers include GitHub, Slack, Google Drive, and other SaaS integrations, configured via `claude mcp add` and stored in `~/.claude.json` or project `.mcp.json`.[7][4]
- MCP supports `list_changed` notifications so tools/resources can update dynamically without reconnecting, enabling robust long‑running workflows.[8][7]

These MCP integrations are what make Claude Code a general knowledge‑work engine: the same planning and execution patterns apply whether the tool is a repo, a doc store, or a chat system.

**Hooks and automation**

- Hooks (PreToolUse / PostToolUse) are the main automation surface: they can enforce policy, add observability, and glue Claude’s actions into your existing automation infrastructure (CI, notifications, logging).[5][8]
- MinChoi and others highlight using hooks for: pre‑allowing safe commands, auto‑running tests, logging plans and results, and bridging between human and AI workflows.[8][12]

**GitHub Actions and @Claude/@.claude**

- Claude Code can be wired into GitHub Actions so that tagging `@Claude` on a PR triggers an automated response: run checks, patch code, and report back with a checklist.[15][9]
- This pattern effectively turns PR comments into “mini Oracles” that instruct a Claude Code instance running in CI to modify the repo and propose changes.

**Desktop vs CLI**

- Desktop adds OS integration: easier file selection, GUI “computer use,” and streamlined GitHub/Drive connections; it is ideal when the task involves GUIs or non‑terminal users.[9][8]
- CLI is more composable, scriptable, and friendly to multi‑instance, headless, or remote setups — closer to what you will want for multi‑agent orchestration.[7][2]

***

## Part 5: Orchestration principles

**Multi‑instance orchestration patterns**

- Power users run multiple Claude Code sessions in parallel via terminal tabs, tmux panes, web sessions, and Desktop windows; each session is assigned a role or zone (e.g., “docs,” “data,” “infra”).[10][8]
- Hand‑offs are document‑centric: one session writes artifacts (plans, specs, code, summaries) that others consume via files or MCP resources, not via shared transcript.[8][5]

`&` and `--teleport`:

- The `&` prefix is used in some contexts to mark instructions for web or other surfaces when coordinating between CLI and web code.[8]
- `/teleport` and related flags let you move a session context from CLI to web (`claude.ai/code`) so an agent can continue its work in a different surface, useful when a task needs GUI tools or account‑scoped integrations.[8][2]

**Limits of parallelization**

- Zvi and others note that over‑parallelization introduces coordination overhead; the bottleneck becomes human attention to integrate outputs and manage conflicts.[8][14]
- A practical pattern is 3–7 concurrent “workers,” each owning a domain or phase, with explicit synchronization points where a higher‑level Oracle reviews and re‑splits work.[10][8]

Generalizable principle: **parallelize by artifact boundaries** (documents, PRs, reports, KB entries), not by micro‑tasks; keep each agent’s mandate coherent and bounded.

**Plan Mode and decomposition**

- Plan Mode embodies a general strategy: let the model explicitly decompose tasks, then review and adjust decomposition before any irreversible actions.[12][2]
- For multi‑agent systems, this suggests a two‑tier design:  
  - Oracles produce high‑level decompositions and objectives.  
  - Claude Code instances refine those into executable plans using Plan Mode, then execute.

**Subagent pattern**

- Claude Code’s use of subagents (short‑lived, specialized workers for a subtask) mirrors a general multi‑agent pattern: create ephemeral role‑specific workers that hand back artifacts and then terminate.[8][2]
- This supports recursive self‑improvement: logs and artifacts from subagents become training data for future CLAUDE.md updates and skills.[8][10]

***

## Part 6: Anti‑patterns and failure modes

**Known struggles**

- Highly adversarial domains (security, trading, complex distributed systems) where small errors are catastrophic; even Zvi describes “flying too close to the sun” when letting Claude Code build complex systems end‑to‑end without tight constraints.[8][14]
- Long, unconstrained sessions with no compaction and no artifact externalization, leading to degraded reasoning and subtle inconsistencies.[8][2]

**Security and `--dangerously-skip-permissions`**

- `--dangerously-skip-permissions` disables interactive permission prompts for tools; users and Anthropic engineers consistently warn that this substantially increases risk, especially with Bash and destructive file operations.[8][6]
- Best practice is to combine: narrow tool scopes, hooks that enforce policies, and explicit pre‑allowed commands, rather than global skip‑permissions.[6][5]

**Looping and recovery**

- When Claude Code “loops” (e.g., repeatedly trying failing commands or edits), practitioners:  
  - Interrupt and request a **post‑mortem + new plan**, turning failure into an explicit lesson.  
  - Add constraints or corrections to CLAUDE.md and rerun from a clean session.  
  - Use hooks to detect repeated failing commands and halt with a diagnostic.[5][2]

Anti‑pattern: continuing in a broken session with growing context bloat; healthier to externalize artifacts, compact, or restart with improved scaffolding.

**PKM overengineering**

- Workflows that obsess over organizing CLAUDE.md and configs without tying them to hooks, skills, or actual automated behaviors rarely pay off.[10][8]
- Productive setups are **behavior‑driven**: every configuration element (CLAUDE.md rule, hook, command) exists because it prevents a real class of errors or automates a recurring action.[10][5]

***

## Part 7: Evolution trajectory

**Recent trends and features**

- Recent releases emphasize **recursive self‑improvement**: automatic skill hot‑reload, support for MCP `list_changed`, attaching hooks to agents/skills, wildcard permissions, and `/teleport` between surfaces.[8][7]
- Anthropic’s best‑practices posts and Desktop improvements point to Claude Code being positioned as a general **agentic platform**, not just a coding assistant.[2][9]

**Model usage and cost**

- Opus 4.5 is favored by power users for complex, multi‑tool workflows (especially with “ultrathink” tokens for deeper reasoning), while Sonnet 4.5 is used for cheaper, high‑volume tasks.[8][2]
- Practitioners like Boris explicitly optimize for **cost per reliable change**, not cost per token; that usually justifies Opus for critical planning and refactors, and Sonnet for routine transformations.[10][8]

**Headless and automation**

- Headless mode (`-p` and related flags) is increasingly used for CI, scheduled tasks, and noninteractive automations, essentially turning Claude Code into a daemonized worker that can be triggered by events (GitHub comments, cron jobs, webhooks).[15][7]
- Combined with MCP and hooks, this makes Claude Code a convergence point between LLM agents and traditional automation (Actions, cron, pipelines).

**Competitive positioning**

- Compared to IDE‑centric tools like Cursor, Claude Code is clearly evolving toward a **general orchestration layer** for knowledge work that happens to be excellent at coding, rather than a coding tool that incidentally touches other workflows.[1][2]
- Zvi and others explicitly frame it as an “agent orchestrator” that many organizations are using to prototype agent architectures far faster than dedicated internal efforts.[8][14]

For your multi‑Oracle architecture, this all points to a stable pattern: use Claude Code as the standardized “executor role” that understands CLAUDE.md norms, tools, and MCP landscape, while your higher‑level Oracles focus on cross‑project strategy, decomposition, and knowledge modeling.

Sources
[1] Claude Code vs Cursor: A Power-User's Playbook - Arize AI https://arize.com/blog/claude-code-vs-cursor-a-power-users-playbook/
[2] Claude Code: Best practices for agentic coding - Anthropic https://www.anthropic.com/engineering/claude-code-best-practices
[3] Claude Code vs Cursor: Deep Comparison for Dev Teams [2025] https://www.qodo.ai/blog/claude-code-vs-cursor/
[4] Claude Code settings - Claude Code Docs https://code.claude.com/docs/en/settings
[5] How I use Claude Code (+ my best tips) - Builder.io https://www.builder.io/blog/claude-code
[6] Hooks in plan mode ? : r/ClaudeAI - Reddit https://www.reddit.com/r/ClaudeAI/comments/1n447qu/hooks_in_plan_mode/
[7] Configuring Claude Code MCP Tools for Better Integration - Clockwise https://www.getclockwise.com/blog/claude-code-mcp-tools-integration
[8] Claude Codes - by Zvi Mowshowitz https://thezvi.substack.com/p/claude-codes
[9] Using the GitHub Integration - Claude Help Center https://support.claude.com/en/articles/10167454-using-the-github-integration
[10] How Boris Cherny, Builder of Claude Code, Uses It - DEV Community https://dev.to/with_attitude/how-boris-cherny-builder-of-claude-code-uses-it-and-why-that-should-change-how-you-think-about-173g
[11] Claude Code vs Cursor: Which is Best for Your Dev Workflow? https://www.cbtnuggets.com/blog/technology/devops/claude-code-vs-cursor
[12] Claude Code's Hidden Superpower: Plan Mode for Smart Developers https://www.youtube.com/watch?v=QlWyrYuEC84
[13] Claude Code creator Boris shares his setup with 13 detailed steps ... https://www.reddit.com/r/ClaudeAI/comments/1q2c0ne/claude_code_creator_boris_shares_his_setup_with/
[14] AI #150: While Claude Codes | Don't Worry About the Vase https://thezvi.wordpress.com/2026/01/08/ai-150-while-claude-codes/
[15] How to Use Claude Code with GitHub Actions - Apidog https://apidog.com/blog/claude-code-github-actions/
[16] allow hooks in MCP servers · Issue #6981 · anthropics/claude-code https://github.com/anthropics/claude-code/issues/6981
[17] Adding Github integration to Claude : r/ClaudeAI - Reddit https://www.reddit.com/r/ClaudeAI/comments/1l47qf3/adding_github_integration_to_claude/
[18] For those struggling with MCPs, Hooks, Command Configs - Reddit https://www.reddit.com/r/ClaudeCode/comments/1m7my73/for_those_struggling_with_mcps_hooks_command/
[19] “Claude Codes” by Zvi - LessWrong (30+ Karma) - Apple Podcasts https://podcasts.apple.com/ve/podcast/claude-codes-by-zvi/id1698192712?i=1000744503624
[20] Comments - Claude Codes - by Zvi Mowshowitz https://thezvi.substack.com/p/claude-codes/comments
