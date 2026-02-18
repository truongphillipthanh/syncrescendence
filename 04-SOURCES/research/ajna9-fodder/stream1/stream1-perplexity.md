Here’s an initial research scaffold for your program, focusing on directly answerable Phase 1 questions and a minimal but actionable slice of Phases 2–4. I’ll stay terse but precise so you can slot this into your larger corpus.

***

## 1. Phase 1 – First‑Party Validation Snapshot

### 1.1 CLAUDE.md specification & hierarchy

**Key architectural claims you care about: hierarchy, on‑demand subdirectory loading, recursion limits.**

1)  
CLAIM: `CLAUDE.md` hierarchy is Enterprise → Project → Modular rules → User → Local, with more specific levels overriding more general ones.  
SOURCE: Builder.io guide, HumanLayer blog, CodeWithMukesh, plus Agent SDK docs for CLAUDE.md discovery. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)
VERDICT: EXTENDED  
EVIDENCE:  
- Agent SDK: project vs user CLAUDE.md and how they are loaded when `settingSources` is configured. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)
- CodeWithMukesh: explicit hierarchy including Enterprise Policy, Project Memory (`CLAUDE.md` at repo root), Project Rules (`.claude/rules/`), and User Memory (`~/.claude/CLAUDE.md`). [codewithmukesh](https://codewithmukesh.com/blog/claude-md-mastery-dotnet/)
- Builder.io: root CLAUDE.md plus `.claude/` variants and mention of subdirectory CLAUDE.mds. [builder](https://www.builder.io/blog/claude-md-guide)
IMPLICATION: The guide should (a) explicitly separate “memory scopes” (Enterprise policy, User, Project, Rules) from “file layout”, and (b) state that precedence is “more specific overrides on conflict” rather than a single replacement chain. [codewithmukesh](https://codewithmukesh.com/blog/claude-md-mastery-dotnet/)

2)  
CLAIM: Subdirectory `CLAUDE.md` files load on demand only when Claude is working in that subtree.  
SOURCE: Builder.io CLAUDE.md guide. [builder](https://www.builder.io/blog/claude-md-guide)
VERDICT: CONFIRMED  
EVIDENCE: Builder.io: “When Claude reads files in a subdirectory, it automatically picks up any `CLAUDE.md` in that subtree… These aren’t loaded at launch. They’re only included when Claude is actively working in that part of the codebase.” [builder](https://www.builder.io/blog/claude-md-guide)
IMPLICATION: This pattern is explicitly documented and should be upgraded from “folk wisdom” to “documented behavior” in the guide, with a clear recommendation to use subtree‑specific CLAUDE.md for risky or specialized areas (e.g. infra, security‑critical code). [builder](https://www.builder.io/blog/claude-md-guide)

3)  
CLAIM: Recursion/import depth exists for modular rule files and can be exceeded.  
SOURCE: NOT FOUND IN OFFICIAL DOCS (in the material surfaced so far).  
VERDICT: UNVERIFIED  
EVIDENCE: Agent/CLAUDE.md docs describe locations and scopes but don’t specify a recursion or import depth limit, nor do they describe a failure mode when depth is exceeded. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)
IMPLICATION: Treat any “max depth” numbers in the current guide as speculative and re‑label as hypotheses requiring empirical testing. Add an open question to the guide’s “Research Agenda” section to measure import depth via controlled experiments.  

4)  
CLAIM: Enterprise‑level CLAUDE.md / policy memory sits above project, rules, and user scopes.  
SOURCE: CodeWithMukesh .NET CLAUDE.md guide; other enterprise‑oriented blog content. [codewithmukesh](https://codewithmukesh.com/blog/claude-md-mastery-dotnet/)
VERDICT: CONFIRMED (at least at concept level)  
EVIDENCE: CodeWithMukesh: “Enterprise Policy — Organization‑level rules (if using Claude for Teams)” and “Key insight: All levels combine — they don’t replace each other. More specific rules override on conflicts.” [codewithmukesh](https://codewithmukesh.com/blog/claude-md-mastery-dotnet/)
IMPLICATION: The guide should explicitly mention an Enterprise policy layer and clarify that this is typically controlled by admins, not developers, and may enforce non‑negotiable constraints.  

***

### 1.2 Extended thinking budget (“think” / “ultrathink”)

5)  
CLAIM: `think` / `think hard` / `think harder` / `ultrathink` are magic words with increasing thinking budgets; “ultrathink” is the highest tier.  
SOURCE: Anthropic “Claude Code: Best practices for agentic coding”; Anthropic extended‑thinking announcement; HN discussion quoting the doc. [news.ycombinator](https://news.ycombinator.com/item?id=43739997)
VERDICT: CONFIRMED  
EVIDENCE: Anthropic best‑practices post: phrases are “mapped directly to increasing levels of thinking budget… `\"think\" < \"think hard\" < \"think harder\" < \"ultrathink\"`.” Anthropic extended‑thinking news post describes extended thinking as an official feature across products. HN thread cites the same wording and notes that ultrathink is explicitly called out in public Anthropic docs. [anthropic](https://www.anthropic.com/news/visible-extended-thinking)
IMPLICATION: Treat these triggers as first‑class API/UX features, not hacks. The guide should recommend explicit, intentional use (e.g. “Use `think` for everyday planning; reserve `ultrathink` for complex, high‑stakes operations due to cost”).  

6)  
CLAIM: Specific token allocations: `think` ~4K, `ultrathink` ~32K, with hard‑coded budgets.  
SOURCE: NOT FOUND IN OFFICIAL DOCS; community reports (HN, blogs) infer numbers. [wenaidev](https://www.wenaidev.com/blog/en/claude-code-ultrathink-secret-prompt)
VERDICT: UNVERIFIED  
EVIDENCE: HN comment: Claude Code “detects the exact string `ultrathink` and sets the thinking token budget to 31999,” but this is not backed by first‑party documentation. Wenaidev blog repeats the level ordering but not official numeric budgets. [wenaidev](https://www.wenaidev.com/blog/en/claude-code-ultrathink-secret-prompt)
IMPLICATION: Strip or soften any numeric budget claims in the guide; keep only the monotonic ordering and qualitative trade‑off (more budget = more cost and latency). Mark “exact token budgets per thinking level” as an experimental question for Phase 3.  

7)  
CLAIM: There are additional, undocumented trigger phrases beyond the four main levels.  
SOURCE: NOT FOUND IN OFFICIAL DOCS (in surfaced materials).  
VERDICT: UNVERIFIED  
EVIDENCE: Anthropic explicitly names exactly four phrases; no official mention of more. [anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
IMPLICATION: Treat any other claimed secret triggers as speculative. Place them in a “folk patterns” appendix separated from verified architecture.  

***

### 1.3 Context window behavior & compaction

8)  
CLAIM: Claude Code uses a 200K token context window (with larger tiers for Enterprise), and the system is “context‑aware.”  
SOURCE: Context windows API docs for Claude 4.5 models. [platform.claude](https://platform.claude.com/docs/en/build-with-claude/context-windows)
VERDICT: CONFIRMED  
EVIDENCE: Docs describe a `<budget:token_budget>200000</budget:token_budget>` header and note that Enterprise context can be 500K or 1M. [platform.claude](https://platform.claude.com/docs/en/build-with-claude/context-windows)
IMPLICATION: The guide can confidently anchor its context‑strategy discussion around a 200K standard, while explicitly calling out 500K/1M tiers for Enterprise and the fact that the model is **aware** of remaining budget.  

9)  
CLAIM: Quality degrades “well before” 200K and auto‑compaction is lossy, particularly with big system instructions and long sessions.  
SOURCE: NOT DIRECTLY SPECIFIED IN OFFICIAL DOCS; community strategy posts and practitioners’ observations. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1p05r7p/my_claude_code_context_window_strategy_200k_is/)
VERDICT: EXTENDED (by community, not first‑party)  
EVIDENCE: A Reddit context‑strategy post recommends keeping starting usage below 20% of the context window and explicitly disabling convenience features to avoid hidden auto‑compaction and summarization; the author argues that these background summaries can distort user intent. Official context docs emphasize effective use of the budget but do not quantify a “safe” utilization percentage or describe compaction algorithms in detail. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1p05r7p/my_claude_code_context_window_strategy_200k_is/)
IMPLICATION: Your guide should:  
- Clearly mark “20% starting context” and similar heuristics as community‑derived.  
- Separate “model context awareness” (official) from “auto‑compaction strategy” (inferred).  
- Add an experimental Phase 3 task to empirically measure degradation at different utilization levels.  

10)  
CLAIM: Auto‑compaction is “lossy” vs. “lossless,” and particular content types are more prone to being dropped.  
SOURCE: NOT FOUND IN OFFICIAL DOCS. [platform.claude](https://platform.claude.com/docs/en/build-with-claude/context-windows)
VERDICT: UNVERIFIED  
EVIDENCE: Official docs focus on budget awareness, not compaction internals. [platform.claude](https://platform.claude.com/docs/en/build-with-claude/context-windows)
IMPLICATION: Any detailed claims about the compaction algorithm (e.g. “narrative instructions are preserved but code is compressed”) should be removed or reframed as hypotheses to test via systematic probing.  

***

### 1.4 Permissions system (`settings.json`, allow/deny, hooks)

11)  
CLAIM: Permissions use allow/deny lists with glob‑style patterns, and `defaultMode` can be set to bypass or ask.  
SOURCE: Agent SDK permissions docs; community schema references; user guides. [gist.github](https://gist.github.com/xdannyrobertsx/0a395c59b1ef09508e52522289bd5bf6)
VERDICT: EXTENDED  
EVIDENCE: Agent SDK permissions docs describe a rule‑checking order: hooks, then `deny` rules, then `allow` rules in `settings.json`. Zhaolong Zhong’s settings guide shows `$schema` pointing at `https://json.schemastore.org/claude-code-settings.json` and demonstrates `permissions` with `allow`, `deny`, and `defaultMode: "bypassPermissions"`. A published schema gist describes config for `settings.json` including permission options, though this is community‑hosted. [zhaolongzhong](https://www.zhaolongzhong.com/blog/claude-code-tips)
IMPLICATION: Your guide should:  
- Explicitly document evaluation order: hooks → deny → allow → default mode. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/permissions)
- Promote `$schema` usage to get editor validation and discover the full permission surface. [zhaolongzhong](https://www.zhaolongzhong.com/blog/claude-code-tips)

12)  
CLAIM: There are permission hooks (PreToolUse, PermissionRequest, etc.) with richer decision semantics and optional input mutation.  
SOURCE: Claude Code Hooks reference; Agent SDK permissions doc. [code.claude](https://code.claude.com/docs/en/hooks)
VERDICT: CONFIRMED  
EVIDENCE: Hooks reference describes `PreToolUse`, `PostToolUse`, and `PermissionRequest`, along with fields like `permissionDecision` (`allow` / `deny` / `ask`), `permissionDecisionReason`, and `updatedInput` to modify tool parameters. It also distinguishes `continue`/`block` decisions for stopping behavior. Permissions docs state that hooks run before rules and can short‑circuit. [code.claude](https://code.claude.com/docs/en/hooks)
IMPLICATION: The guide’s current “settings.json‑only” view of permissions is incomplete; it should be reframed as a three‑layered system: enterprise‑managed settings, hooks, then per‑project/user declarative rules.  

13)  
CLAIM: You can implement custom permission logic via hooks that consult external configuration (regex, etc.).  
SOURCE: Korny’s hook blog post. [blog.korny](https://blog.korny.info/2025/10/10/better-claude-code-permissions)
VERDICT: EXTENDED  
EVIDENCE: The post describes a `PreToolUse` hook that receives structured tool‑use data, applies regex‑based allow/deny rules, and returns decisions; it notes that deny rules take precedence, aligning with official ordering. [blog.korny](https://blog.korny.info/2025/10/10/better-claude-code-permissions)
IMPLICATION: This validates the “permission hooks as programmable policy gateway” pattern. Your guide should show this as the recommended way to express complex org policy, with declarative allow/deny reserved for simpler cases.  

***

### 1.5 Tasks system & multi‑agent orchestration

14)  
CLAIM: The Tasks system spawns sub‑agents with their own context, tools, and autonomous loops; they can run in the background and report results back.  
SOURCE: Agent SDK overview; Product/UX oriented guides; dedicated “Task tool” articles. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/overview)
VERDICT: CONFIRMED  
EVIDENCE: Agent SDK: “Build AI agents… The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code.” ProductTalk: “Claude can spawn sub‑agents… If you see Claude use the Task command, that’s Claude spinning up a general‑purpose agent to help it do something.” The “Task Tool” article describes sub‑agents with their own context and tool sets, running autonomously and returning results. [dev](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2)
IMPLICATION: The guide is directionally correct: Tasks are genuine sub‑agents, not just long‑running functions. It should clarify that each Task has its own agent loop and context slice, which matters for context budgeting and decomposition.  

15)  
CLAIM: The task system internally maintains a task graph, tracks dependencies, and supports complex scheduling (beyond simple parent–child).  
SOURCE: NOT EXPLICITLY DOCUMENTED in first‑party sources uncovered so far. [producttalk](https://www.producttalk.org/how-to-use-claude-code-features/)
VERDICT: UNVERIFIED  
EVIDENCE: Public materials describe Tasks conceptually (spawn, background, completion) but do not expose an explicit task‑graph API or internal representation. [dev](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2)
IMPLICATION: Present any “task graph with explicit dependency edges” as inferred behavior, not guaranteed architecture. In the guide, emphasize *patterns* (“fan‑out/fan‑in via Tasks”) rather than implying a documented internal graph model.  

16)  
CLAIM: Nesting Tasks deeply is supported but harmful; flattened task structures are preferred.  
SOURCE: Task Tool article. [dev](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2)
VERDICT: EXTENDED  
EVIDENCE: The article explicitly warns against deep nesting (`Main → Task → Sub‑Task → Sub‑Sub‑Task`) and recommends flattening except for legitimate parallel work. [dev](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2)
IMPLICATION: This validates your “don’t over‑nest agents” anti‑pattern. You can cite this as semi‑authoritative guidance and fold it into your dialectic on orchestration complexity vs. observability.  

***

### 1.6 MCP integration & configuration

17)  
CLAIM: MCP servers have a clear scope precedence: local > project > user; Enterprise can override with `managed-mcp.json`.  
SOURCE: Claude Code MCP docs. [code.claude](https://code.claude.com/docs/en/mcp)
VERDICT: CONFIRMED  
EVIDENCE: MCP docs: “Scope hierarchy and precedence… local‑scoped servers first, followed by project‑scoped… and finally user‑scoped.” The same doc describes `managed-mcp.json` for exclusive control, plus allowlist/denylist policy via `allowedMcpServers` / `deniedMcpServers`. [code.claude](https://code.claude.com/docs/en/mcp)
IMPLICATION: The guide should present MCP configuration using this explicit precedence and show how it parallels (but is separate from) CLAUDE.md memory hierarchy.  

18)  
CLAIM: You can restrict MCP servers by server name, command, or URL pattern with wildcards.  
SOURCE: MCP configuration docs. [code.claude](https://code.claude.com/docs/en/mcp)
VERDICT: CONFIRMED  
EVIDENCE: Docs specify `serverName`, `serverCommand`, or `serverUrl` as mutually exclusive selectors, with wildcard support for URLs. [code.claude](https://code.claude.com/docs/en/mcp)
IMPLICATION: Document these selectors and emphasize that security policy is typically expressed at this level, not just via per‑tool permissions.  

19)  
CLAIM: MCP discovery uses a CLI wizard (`claude mcp add`) and JSON files, with environment variable expansion.  
SOURCE: MCP docs and implementation guides. [scottspence](https://scottspence.com/posts/configuring-mcp-tools-in-claude-code)
VERDICT: EXTENDED  
EVIDENCE: MCP docs show JSON configs with environment variable expansion like `${API_BASE_URL:-https://api.example.com}` and note that missing required variables cause parsing failure. Clockwise and other guides describe use of the CLI wizard and JSON files for configuration. [getclockwise](https://www.getclockwise.com/blog/claude-code-mcp-tools-integration)
IMPLICATION: Your guide should link MCP discovery explicitly to JSON config plus CLI flows, and call out failure modes when env vars are missing (important for CI and multi‑machine setups).  

20)  
CLAIM: MCP has a separate “installation scope” concept (local/project/user) that impacts shareability and security.  
SOURCE: Clockwise integration guide. [getclockwise](https://www.getclockwise.com/blog/claude-code-mcp-tools-integration)
VERDICT: EXTENDED  
EVIDENCE: The guide explains “installation scopes” with local servers tied to a single project and stored in user‑specific settings, versus more shared scopes. [getclockwise](https://www.getclockwise.com/blog/claude-code-mcp-tools-integration)
IMPLICATION: Clarify in the guide that scope influences not only precedence, but also collaboration properties (e.g. local MCP servers are invisible to teammates unless replicated).  

***

## 2. Phase 2 – Early Antipattern & Community Pattern Signals

Here are a few high‑yield community‑validated antipatterns you can fold into your systematic matrix. These are not exhaustive, but they map well to your existing sections.

### 2.1 Context & memory antipatterns

ANTIPATTERN: Hidden auto‑compaction via “helpful” history and always‑on MCPs  
SYMPTOM: Sessions hit context limits quickly, later replies feel “forgetful” or misaligned even though 200K capacity is not exhausted.  
ROOT CAUSE: Large persistent system instructions, verbose history, and active MCPs consume context; compaction/summarization silently rewrites history.  
FREQUENCY: Common in longer sessions and multi‑MCP setups (multiple independent reports). [reddit](https://www.reddit.com/r/ClaudeAI/comments/1p05r7p/my_claude_code_context_window_strategy_200k_is/)
MITIGATION:  
- Keep initial system + memory footprint under ~20% of context.  
- Turn off nonessential MCPs; selectively enable via `@` when needed.  
- Periodically start fresh sessions and paste in curated history instead of relying on automatic summarization. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1p05r7p/my_claude_code_context_window_strategy_200k_is/)
GUIDE STATUS: Probably DOCUMENTED qualitatively in your current guide; can be sharpened with “20% starting budget” and “MCP hygiene” as explicit heuristics.  

### 2.2 Permissions antipatterns

ANTIPATTERN: `bypassPermissions` in unsafe environments  
SYMPTOM: Claude runs arbitrary shell commands or edits sensitive files without confirmation.  
ROOT CAUSE: Setting `defaultMode: "bypassPermissions"` globally in `settings.json` on machines that have production access. [zhaolongzhong](https://www.zhaolongzhong.com/blog/claude-code-tips)
FREQUENCY: Occasionally reported; highlighted in tips posts as a footgun. [zhaolongzhong](https://www.zhaolongzhong.com/blog/claude-code-tips)
MITIGATION:  
- Reserve `bypassPermissions` for dedicated sandboxes and ephemeral dev containers.  
- Use hooks and allow/deny rules instead of bypass for convenience.  
GUIDE STATUS: Likely INCOMPLETE – add a strong warning wherever you mention bypass permissions.  

ANTIPATTERN: Over‑broad allow patterns in permissions or hooks  
SYMPTOM: Permissions system becomes effectively meaningless; tools like `Bash(*)` are always allowed across projects.  
ROOT CAUSE: Convenience‑driven patterns (`Read(*)`, `Write(*)`, `Bash(*)`) placed at global scope. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1l24a93/claude_code_settingsjson/)
FREQUENCY: Common among early adopters sharing config snippets. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1l24a93/claude_code_settingsjson/)
MITIGATION: Constrain to project‑local settings, and use hooks to narrow commands (e.g. only allow `mermaid-cli` or `pytest`). [blog.korny](https://blog.korny.info/2025/10/10/better-claude-code-permissions)
GUIDE STATUS: MISSING – your guide should add a “Principle of Least Privilege for Tools” section.  

### 2.3 Tasks & orchestration antipatterns

ANTIPATTERN: Deeply nested task trees  
SYMPTOM: Hard‑to‑debug agent behavior, circular task flows, and “lost” work in sub‑tasks.  
ROOT CAUSE: Using Tasks recursively for every micro‑step instead of doing substantial work in a single agent. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1n4yjtj/claude_code_task_completion_system_multiagent/)
FREQUENCY: Recurrent in multi‑agent enthusiasm posts, then later corrected in “lessons learned.” [reddit](https://www.reddit.com/r/ClaudeAI/comments/1n4yjtj/claude_code_task_completion_system_multiagent/)
MITIGATION:  
- Prefer flat task structures with well‑specified responsibilities.  
- Use at most one level of parallel sub‑agents for independent work.  
GUIDE STATUS: DOCUMENTED (likely) but can be upgraded with explicit diagrams and a “flatten unless you need true parallelism” rule of thumb. [dev](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2)

***

## 3. Phase 3 – Concrete Experiment Designs (Minimal Set)

You can embed these as “research recipes” in a dedicated section of the guide.

### 3.1 Context degradation curve

Experiment sketch:  
- Choose a deterministic coding task (e.g. implement a small feature with clear acceptance tests).  
- Construct synthetic histories at 10%, 25%, 50%, 75%, 90% of the 200K context (combine CLAUDE.md content, conversation, and code excerpts).  
- Run the identical user request from a fresh agent each time and compare: test pass rate, defect count, and plan quality.  

Tie‑in: This directly tests the “20% starting context” heuristic and could upgrade it from anecdotal to empirically grounded. [platform.claude](https://platform.claude.com/docs/en/build-with-claude/context-windows)

### 3.2 Compaction information‑loss characterization

Experiment sketch:  
- Populate a session with varied content types (short code, long code, prose requirements, API docs, tabular reference).  
- Drive the session past the compaction threshold, then query Claude about each content segment’s details.  
- Measure which types degrade first (e.g. minor comments vs. API edge‑cases).  

Tie‑in: Helps validate or refute claims that certain content should live in CLAUDE.md vs. transient chat because of compaction behavior. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)

### 3.3 Extended thinking ROI

Experiment sketch:  
- For each of several task complexities (toy bug, medium feature, multi‑file refactor, greenfield module), run four conditions: no keyword, `think`, `think hard`, `ultrathink`.  
- Evaluate on task success, defect rate, latency, and token usage.  

Tie‑in: Converts “use ultrathink sparingly” into a task‑class–specific heuristic (e.g. “above X complexity, `think hard` dominates.”) [anthropic](https://www.anthropic.com/news/visible-extended-thinking)

***

## 4. Synthesis & Guide‑Update Skeleton

Below is a compact structure you can extend when you incorporate more sources.

### 4.1 Validation matrix (excerpt)

| Claim cluster                         | Status       | Notes |
|--------------------------------------|-------------|-------|
| `think`→`ultrathink` levels exist    | Confirmed   | Official Anthropic docs; no numeric budgets. [anthropic](https://www.anthropic.com/engineering/claude-code-best-practices) |
| Numeric token budgets per level      | Unverified  | HN/blog numbers only; must treat as hypotheses. [news.ycombinator](https://news.ycombinator.com/item?id=43739997) |
| CLAUDE.md hierarchy & subdirectories | Confirmed   | Enterprise/user/project/rules + on‑demand subtree CLAUDE.md. [codewithmukesh](https://codewithmukesh.com/blog/claude-md-mastery-dotnet/) |
| Auto‑compaction is lossy             | Unverified  | Strong community evidence but no official description. [reddit](https://www.reddit.com/r/ClaudeAI/comments/1p05r7p/my_claude_code_context_window_strategy_200k_is/) |
| Task system as sub‑agent spawner     | Confirmed   | Agent SDK + docs/blogs. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/overview) |
| Explicit internal task graph         | Unverified  | Not described in surfaced docs. [dev](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2) |
| Permissions: hooks → deny → allow    | Confirmed   | Agent SDK permissions docs. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/permissions) |
| MCP scopes & precedence              | Confirmed   | Local > project > user; managed configs override. [code.claude](https://code.claude.com/docs/en/mcp) |

***

### 4.2 Enhancement recommendation examples

1)  
SECTION: Extended Thinking & Plan Mode  
CHANGE_TYPE: MODIFY  
RATIONALE: Align with Anthropic wording and remove unverified numeric budgets.  
PROPOSED_CONTENT: “Claude Code supports four extended thinking levels triggered by the phrases `think`, `think hard`, `think harder`, and `ultrathink`. Each level gives Claude more thinking budget, increasing latency and token use in exchange for deeper reasoning. Reserve `ultrathink` for the most complex and high‑stakes tasks.” [anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
CONFIDENCE: HIGH  
EVIDENCE_STRENGTH: 3+ independent official/community sources. [news.ycombinator](https://news.ycombinator.com/item?id=43739997)

2)  
SECTION: CLAUDE.md Memory Architecture  
CHANGE_TYPE: ADD  
RATIONALE: Reflect officially documented subtree behavior and enterprise policy layer.  
PROPOSED_CONTENT: “Claude loads CLAUDE.md instructions from multiple scopes: Enterprise policies, user‑level `~/.claude/CLAUDE.md`, project‑root `CLAUDE.md`, rules in `.claude/rules/`, and subtree‑specific CLAUDE.md files. Subdirectory CLAUDE.md files are loaded on demand only when Claude is working in that part of the tree, allowing you to localize instructions for sensitive or specialized areas.” [codewithmukesh](https://codewithmukesh.com/blog/claude-md-mastery-dotnet/)
CONFIDENCE: HIGH  
EVIDENCE_STRENGTH: 2+ independent sources with consistent descriptions. [builder](https://www.builder.io/blog/claude-md-guide)

3)  
SECTION: Permissions & Safety  
CHANGE_TYPE: RESTRUCTURE  
RATIONALE: Incorporate hooks and managed MCP settings as first‑class control layers.  
PROPOSED_CONTENT: “Think of permissions as a three‑layer system: (1) Enterprise‑managed settings and MCP policies, (2) programmable hooks (`PreToolUse`, `PermissionRequest`, `PostToolUse`) that can inspect and mutate tool invocations, and (3) per‑project/user declarative `allow`/`deny` rules in `settings.json`, evaluated in the order: hooks → deny → allow → default mode.” [platform.claude](https://platform.claude.com/docs/en/agent-sdk/permissions)
CONFIDENCE: HIGH  
EVIDENCE_STRENGTH: 3 official sources. [code.claude](https://code.claude.com/docs/en/hooks)

***

## 5. Open Questions Register (High‑Value)

- Exact token budgets per extended‑thinking level and whether they vary by model or plan mode. [news.ycombinator](https://news.ycombinator.com/item?id=43739997)
- Maximum CLAUDE.md modular import depth and failure behavior when exceeded. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)
- Detailed auto‑compaction algorithm (ordering, importance weighting, and loss profile across content types). [reddit](https://www.reddit.com/r/ClaudeAI/comments/1p05r7p/my_claude_code_context_window_strategy_200k_is/)
- Internal representation of the task system (whether it exposes a stable “task graph” abstraction or just parent–child relationships). [platform.claude](https://platform.claude.com/docs/en/agent-sdk/overview)
- Interaction between MCP scope precedence and Enterprise managed MCP policy in complex setups (e.g. conflicting definitions across scopes). [getclockwise](https://www.getclockwise.com/blog/claude-code-mcp-tools-integration)

***

## 6. Appendix – Prompt Refinement Recommendations

Based on what surfaces cleanly from current sources:

- Split your Phase 1 questions into “documented behavior” (e.g. CLAUDE.md scopes, MCP precedence, extended thinking triggers) versus “inferred internals” (compaction algorithm, task graph). This helps avoid chasing answers that simply aren’t public yet. [anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
- Rephrase numeric or implementation‑detail questions into experiment‑design prompts for Phase 3 (e.g. “How can we empirically estimate thinking budgets?” rather than “What is the budget?”).  
- Add a dedicated line of inquiry for hooks and managed MCP as the de‑facto policy surface, which is under‑emphasized in most community guides but strongly represented in official docs. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/permissions)
- Make “on‑demand subtree CLAUDE.md loading” and “MCP scope/precedence” explicit architectural pillars in your prompt; they show up repeatedly in high‑quality docs and are central to advanced workflows. [code.claude](https://code.claude.com/docs/en/mcp)

If you’d like, next step I can focus purely on building out a full Phase‑2 antipattern inventory (Reddit, GitHub issues, HN, X, YouTube) in your exact matrix formats.