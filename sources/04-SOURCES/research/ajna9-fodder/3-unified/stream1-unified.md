# Claude Code Architecture: Unified Research Synthesis

This synthesis coalesces five independent research iterations investigating Claude Code's architecture, validating community-derived patterns against authoritative sources, and mapping the frontier of documented versus emergent capabilities. The iterations converge on substantial architectural truths while revealing productive tensions where credible sources recommend different approaches or arrive at contradictory conclusions. These tensions are preserved as navigable dimensions rather than resolved into false consensus.

---

## I. The Validation Landscape: Where Sources Converge and Diverge

### 1.1 Convergent Findings Across All Iterations

The research corpus achieves strong consensus on several architectural foundations:

**CLAUDE.md exists as a hierarchical configuration system.** All five iterations confirm that Claude Code loads memory files from multiple scopes—user, project, and subdirectory levels—with more specific scopes taking precedence on conflict. The on-demand loading of subdirectory CLAUDE.md files when Claude accesses those subtrees is documented behavior, not folk wisdom.

**Permissions follow a documented evaluation order.** The deny → allow → ask evaluation sequence appears consistently across official documentation, with hooks providing an interception layer before declarative rules are evaluated.

**Context degrades before reaching nominal limits.** The 200K token context window is a theoretical maximum, not a practical operating range. Research confirms the "Lost in the Middle" phenomenon where model performance drops for information positioned in the middle of context, with quality degradation observable well before capacity limits.

**Auto-compaction is inherently lossy.** All iterations acknowledge that compaction summarizes conversation history, discarding specific details while preserving high-level decisions. The process cannot be made lossless by definition.

**MCP integration uses scope-based precedence.** Local > project > user ordering governs which MCP server configurations take effect, with enterprise managed-mcp.json providing override capability.

**The Tasks system spawns genuine sub-agents.** Each task operates with its own context window and agent loop, not as a simple function call. Sub-agents cannot spawn additional sub-agents, preventing infinite nesting.

### 1.2 Productive Contradictions Requiring Navigation

The research reveals genuine disagreements that reflect different interpretive stances or evolving documentation:

**Extended thinking trigger mechanisms.** Claude's iteration reports source-code-verified token budgets (4,000 / 10,000 / 31,999) mapped to specific keywords. ChatGPT's iteration explicitly contradicts this, citing official documentation that these phrases are "interpreted like normal prompt instructions and don't allocate additional thinking tokens." Grok confirms only "think" and "ultrathink" as hardcoded, dismissing multi-tier escalations. Perplexity confirms the four-level ordering exists but marks specific numeric budgets as unverified. The iterations split between treating keywords as API-level budget switches versus behavioral instructions.

**CLAUDE.md hierarchy terminology.** Community consensus uses "Enterprise → Project → Modular rules → User → Local" ordering. ChatGPT's research reports official documentation frames this as "Managed > CLI args > Local > Project > User" for settings, suggesting the community-derived ordering conflates distinct hierarchies (memory versus settings). Perplexity confirms enterprise/user/project/rules scopes but notes they "combine rather than replace."

**Auto-compaction trigger thresholds.** Claude reports 64-75% in newer versions. ChatGPT cites CLAUDE_AUTOCOMPACT_PCT_OVERRIDE with ~95% default. Gemini states ~95% (25% safe buffer). Grok estimates 75-90%. The variance may reflect version differences, configuration options, or measurement methodology.

**Recursion/import depth limits.** Claude reports a 5-hop maximum import depth. ChatGPT confirms the same. Perplexity marks this as "NOT FOUND IN OFFICIAL DOCS" and recommends treating it as hypothesis. The discrepancy may reflect documentation surfacing versus absence.

---

## II. CLAUDE.md: Architecture and Configuration

### 2.1 The Memory Hierarchy

The configuration system operates across multiple scopes with distinct purposes and precedence relationships.

**Scope definitions from official documentation:**

| Scope | Location | Purpose | Shareability |
|-------|----------|---------|--------------|
| **Managed/Enterprise** | `/Library/Application Support/ClaudeCode/` (macOS), `/etc/claude-code/` (Linux) | Organization-wide policies enforced by IT | Admin-controlled, cannot be overridden |
| **User** | `~/.claude/CLAUDE.md` | Personal preferences across all projects | Per-developer |
| **Project** | `./CLAUDE.md`, `./.claude/CLAUDE.md` | Repository-specific guidance | Version-controlled, team-shared |
| **Rules** | `.claude/rules/*.md` | Modular thematic breakdowns | Version-controlled, conditional activation |
| **Local** | `./CLAUDE.local.md` | Per-developer overrides | Gitignored |
| **Subdirectory** | `subdirectory/CLAUDE.md` | Path-specific context | Loaded on-demand when accessing subtree |

**Precedence dynamics:** More specific scopes override more general ones on conflict. The iterations disagree on whether this is strict replacement or additive combination. Perplexity explicitly states "All levels combine—they don't replace each other. More specific rules override on conflicts."

**On-demand loading:** Subdirectory CLAUDE.md files load lazily when Claude accesses files in those subtrees, not at startup. This enables scalable configuration for monorepos without context overhead.

**Import syntax:** Files can reference other files using `@path/to/file.md` syntax. A maximum import depth of 5 hops is reported by Claude and ChatGPT iterations but marked unverified by Perplexity.

### 2.2 Settings.json Schema and Permissions

The permissions system uses a declarative JSON schema with granular pattern matching.

**Settings file precedence (highest to lowest):**
1. Enterprise managed: `managed-settings.json` in protected system directories
2. Command-line arguments (session-scoped)
3. Local project: `.claude/settings.local.json` (gitignored)
4. Shared project: `.claude/settings.json` (version-controlled)
5. User: `~/.claude/settings.json`

**Permission evaluation order:**
1. Hooks (PreToolUse can intercept and modify)
2. Deny rules (always evaluated first among declarative rules)
3. Allow rules
4. Ask rules (default fallback)

**Pattern syntax examples:**
```json
{
  "permissions": {
    "allow": ["Read(./**/*.ts)", "Bash(npm run *)"],
    "deny": ["Read(./.env)", "Read(./secrets/**)", "Bash(rm -rf *)"],
    "ask": ["Bash(git push *)", "Bash(npm publish)"]
  }
}
```

**Security caveat from official documentation:** Argument-constraining patterns should not be treated as a security boundary. The permission system is a convenience layer for workflow friction, not a robust sandbox.

**MCP tool patterns:** Follow the format `mcp__<server-name>__<tool-name>` with wildcard support (`mcp__github__*`).

### 2.3 The Paradox of Less

Research converges on a counterintuitive finding: extensive CLAUDE.md instructions degrade performance. Models reliably follow approximately 150-200 instructions; Claude Code's system prompt already consumes roughly 50. Claude may ignore contents deemed "not highly relevant to the current task." The more irrelevant content included, the more likely relevant parts are ignored.

**Recommendations across iterations:**
- Target fewer than 300 lines, ideally fewer than 100
- Include only universally applicable rules
- Tell Claude why, not just what
- Reference external docs rather than embedding them
- Use progressive disclosure through Skills for specialized context

---

## III. Extended Thinking: The Budget Controversy

### 3.1 The Trigger Keyword Debate

The iterations fundamentally disagree on whether natural language triggers allocate specific token budgets.

**Position A: Keywords are API-level budget switches (Claude iteration)**

Simon Willison's extraction of Claude Code's CLI JavaScript reveals exact token budgets:

| Trigger Phrase | Token Budget |
|---------------|-------------|
| "think" | 4,000 |
| "think hard", "think deeply", "megathink" | 10,000 |
| "ultrathink", "think harder", "think very hard" | 31,999 |

The environment variable `MAX_THINKING_TOKENS` may allow budgets up to 63,999.

**Critical caveat:** These keywords only work in Claude Code's CLI. They have no effect in web chat or direct API calls, where developers must configure `budget_tokens` explicitly.

**Position B: Keywords are behavioral instructions, not budget switches (ChatGPT iteration)**

Official documentation explicitly states these phrases are interpreted like normal prompt instructions and don't allocate additional thinking tokens. Official control surfaces are:
- `alwaysThinkingEnabled` setting
- `MAX_THINKING_TOKENS` environment variable

This position recommends teaching real control surfaces rather than keyword triggers.

**Position C: Only ultrathink is special (Grok iteration)**

GitHub issue #9072 clarifies only "ultrathink" is hardcoded. Phrases like "think hard" lack special handling. No escalating levels are officially specified.

**Position D: Levels exist, numeric budgets are unverified (Perplexity iteration)**

The four-level ordering (`think < think hard < think harder < ultrathink`) is confirmed by Anthropic's best practices post. Specific numeric allocations are community-derived, not officially documented.

### 3.2 Practical Implications

Despite the disagreement, operational guidance converges:

- Extended thinking increases latency and token consumption
- Reserve deeper thinking for complex, high-stakes operations
- The thinking budget trades off against prompt-caching efficiency
- For workloads exceeding 32K tokens, batch processing is recommended due to timeout risks
- The API minimum is 1,024 tokens

**The Gemini iteration's formula for effective context:**
```
Effective Context = Total Context - System Prompt - Extended Thinking Budget - Conversation History
```

Heavy use of extended thinking accelerates approach to compaction threshold.

---

## IV. Context Management: The Scarcest Resource

### 4.1 The Degradation Phenomenon

All iterations confirm quality degradation occurs well before nominal context limits. The "Lost in the Middle" phenomenon (Liu et al., 2023) provides research backing: model performance peaks for information at the beginning and end of context, dropping significantly for middle content. The NoLiMa Benchmark showed 11 of 12 models fell below 50% performance at just 32,000 tokens.

**Practical threshold estimates across iterations:**

| Source | Warning Threshold | Maximum Recommended | Auto-Compact Trigger |
|--------|-------------------|---------------------|---------------------|
| Claude | 70% | 80% | 64-75% (newer versions) |
| ChatGPT | Not specified | Not specified | ~95% (configurable via CLAUDE_AUTOCOMPACT_PCT_OVERRIDE) |
| Gemini | Not specified | Not specified | ~95% (25% safe buffer) |
| Grok | Not specified | <85% | 75-90% |
| Perplexity | 20% starting context | Not specified | Not specified |

The variance may reflect different measurement approaches, version differences, or the inherent difficulty of specifying a single threshold for diverse workloads.

### 4.2 Compaction Mechanics

**What compaction preserves (from official documentation):**
- Architectural decisions
- Unresolved bugs
- Implementation details
- The five most recently accessed files

**What compaction discards:**
- Older tool outputs (cleared first)
- Conversation history (summarized)
- Early detailed instructions (may be lost)

**Steering mechanisms:**
- "Compact Instructions" section in CLAUDE.md to control retention
- `/compact [directive]` for manual compaction with explicit summarization directives
- PreCompact hooks for programmatic intervention

**The compaction death spiral:** Context fills → auto-compact fires → critical instructions lost → quality degrades → user provides more instructions → context fills faster → cycle repeats.

### 4.3 Mitigation Strategies

**Strategy A: Proactive Manual Compaction**
Run `/compact` manually at logical breakpoints with explicit directives rather than waiting for auto-compact.

**Strategy B: External State Persistence**
Write critical state to files that survive compaction:
- `plan.md` for current implementation plan
- `decisions.md` for architectural choices
- `SCRATCHPAD.md` for working notes

**Strategy C: Session Scoping**
One conversation per task. Don't mix unrelated work in the same session.

**Strategy D: Fresh Context Resets**
Copy critical information, run `/compact` for summary, run `/clear` to wipe context, paste back only essentials. Fresh context outperforms degraded context.

**Strategy E: The 20% Starting Budget (Perplexity community heuristic)**
Keep initial system + memory footprint under ~20% of context to leave room for actual work.

---

## V. The Hooks System: Event-Driven Automation

### 5.1 Hook Types

The hooks system is more comprehensive than most community documentation suggests:

| Event | Description | Exit Code 2 Behavior |
|-------|-------------|---------------------|
| **UserPromptSubmit** | Before prompt processing | Blocks prompt |
| **PreToolUse** | Before tool execution | Blocks tool use |
| **PostToolUse** | After tool completion | N/A |
| **PermissionRequest** | Permission prompts | Auto-approve/deny |
| **Stop** | When Claude finishes | N/A |
| **SubagentStop** | When subagent finishes | Blocks stoppage |
| **PreCompact** | Before compaction | N/A |
| **SessionStart** | Session start/resume | N/A |
| **Notification** | Various UI events | N/A |

### 5.2 Hook Response Semantics

Hooks can return structured decisions:
```json
{
  "continue": true,
  "decision": "approve|block|ask",
  "reason": "...",
  "suppressOutput": false,
  "updatedInput": {...}
}
```

The `updatedInput` field enables input mutation, allowing hooks to modify tool parameters before execution.

### 5.3 Hooks as Policy Gateway

The Perplexity iteration frames permissions as a three-layered system:
1. Enterprise-managed settings and MCP policies
2. Programmable hooks that can inspect and mutate tool invocations
3. Per-project/user declarative allow/deny rules

This positions hooks as the recommended mechanism for complex organizational policy, with declarative rules reserved for simpler cases.

---

## VI. MCP Integration: External Tool Connectivity

### 6.1 Configuration Schema

**Scope precedence:** local > project > user, with enterprise `managed-mcp.json` providing override capability.

**Configuration locations:**
- Project: `.mcp.json` (committed, team-shared)
- Local: `~/.claude.json` (per-machine)
- Enterprise: `/Library/Application Support/ClaudeCode/managed-mcp.json`

**Transport types:** stdio (local processes), SSE (server-sent events), HTTP (non-streaming), SDK (in-process)

### 6.2 Tool Discovery and Context Impact

When MCP tool descriptions exceed 10% of context window, Claude Code automatically defers them and loads tools on-demand via tool search. This explains community reports of MCP servers consuming unexpected context.

**Control surfaces:**
- `ENABLE_TOOL_SEARCH=auto:N` to tune threshold
- `allowedMcpjsonServers` / `deniedMcpjsonServers` for enterprise policy
- Denylist always takes precedence over allowlist

### 6.3 Security Boundaries

- Tools require explicit permission (`allowedTools: ["mcp__github__*"]`)
- Enterprise managed allowlist/denylist supported
- Hooks can intercept MCP tool calls
- Isolated execution prevents direct codebase access without permissions
- Environment variable expansion with failure on missing required variables

---

## VII. The Tasks System: Multi-Agent Orchestration

### 7.1 Task Architecture

**Background tasks:** Commands run asynchronously with unique IDs, buffered output retrievable via `TaskOutput` tool, automatic cleanup on exit. Disable with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.

**Subagent properties:**
- Each runs in isolated context window
- Cannot spawn additional subagents (prevents infinite nesting)
- Built-in types: Explore, Plan, general-purpose
- Configurable thoroughness: quick/medium
- Resumable with full conversation history

**Task tool schema:**
```javascript
Input: { description: "3-5 word description", prompt: "Task instruction", subagent_type: "type" }
Output: { result: string, usage: object, total_cost_usd: float, duration_ms: int }
```

### 7.2 The Task Graph Question

The iterations disagree on whether Claude Code exposes an explicit task graph abstraction:

- Claude: "parallel agents for independent tasks" supported
- ChatGPT: Internal graph protocol not specified; treat as hypothesis
- Gemini: `tasks.md` maintains persistent task graph with numbered items
- Grok: Decomposition with dependency graphs confirmed
- Perplexity: No explicit task-graph API documented; present patterns rather than implying guaranteed architecture

**Operational consensus:** Tasks support decomposition, dependency tracking, and coordination. Whether this manifests as an explicit graph API or emergent behavior from simpler primitives remains unclear.

### 7.3 Anti-Nesting Guidance

All iterations warn against deep task nesting. The "Task Tool" article explicitly recommends flattening except for legitimate parallel work. The pattern:

**Prefer:** Main → [Task A, Task B, Task C] (parallel independent work)
**Avoid:** Main → Task → Sub-Task → Sub-Sub-Task (deep sequential nesting)

---

## VIII. Antipattern Inventory

### 8.1 Catastrophic Failures

**rm -rf Home Directory Deletion (Claude iteration)**
Multiple documented incidents where `rm -rf tests/ patches/ plan/ ~/` executed with trailing tilde expansion, deleting all user files. Viral December 2025.

*Mitigation:* Container sandboxing mandatory with `--dangerously-skip-permissions`; add deny rules for destructive patterns.

**Context Window Corruption (Claude iteration)**
Failed compaction attempts can permanently corrupt context management, showing "102%" regardless of conversation length.

*Mitigation:* Session clear or reinstall required.

### 8.2 Workflow Degradation Patterns

**Permission Prompt Overload (Grok iteration)**
Frequent stops for user confirmation slow autonomous flows.

*Root Cause:* Default conservative permissions in settings.json.
*Mitigation:* Set `defaultMode` to "acceptEdits"; use `/permissions` UI.

**Context Overflow in Large Repos (Grok iteration)**
Degraded outputs, infinite loops on >10K files.

*Root Cause:* Inefficient context gathering without indexing.
*Mitigation:* Pre-compact hooks or MCP for external data.

**Hidden Auto-Compaction (Perplexity iteration)**
Sessions hit context limits quickly; later replies feel "forgetful" even though 200K capacity not exhausted.

*Root Cause:* Large persistent system instructions, verbose history, active MCPs consume context silently.
*Mitigation:* Keep initial footprint under ~20%; turn off nonessential MCPs; start fresh sessions periodically.

### 8.3 Safety Erosion Patterns

**bypassPermissions in Unsafe Environments (Perplexity iteration)**
Claude runs arbitrary shell commands without confirmation.

*Root Cause:* Setting `defaultMode: "bypassPermissions"` globally on machines with production access.
*Mitigation:* Reserve bypass for dedicated sandboxes and ephemeral containers.

**Over-broad Allow Patterns (Perplexity iteration)**
Permissions system becomes meaningless; `Bash(*)` always allowed.

*Root Cause:* Convenience-driven patterns at global scope.
*Mitigation:* Constrain to project-local settings; use hooks to narrow commands.

**Permissions as Security Boundary (ChatGPT iteration)**
Sensitive files or restricted actions still reachable.

*Root Cause:* Pattern-based matching is fragile; bugs and edge cases exist.
*Mitigation:* Treat permissions as guardrails, not vault. Put secrets out-of-repo; enforce at OS/credential-manager level.

### 8.4 Behavioral Drift Patterns

**The Refactoring Trap (Gemini iteration)**
When asked to "refactor" or "move" code, Claude attempts to "improve" it simultaneously, altering logic, simplifying functions, or updating dependencies.

*Root Cause:* Training bias toward "fixing" perceived suboptimal code.
*Mitigation:* Explicit prompts: "Move class X to new file. Do NOT alter logic. Copy distinct implementation exactly."

**Context Rot (Gemini iteration)**
Agent slowly drifts from initial requirements as specific details are smoothed over by successive summarizations.

*Root Cause:* Compaction's lossy summarization combined with "Lost in the Middle" phenomenon.
*Mitigation:* Limit sessions to "one mission"; frequently use `/clear`; maintain lean context.

**Sub-agent Naming Bug (Claude iteration)**
Descriptive agent names (e.g., "code-reviewer") trigger Claude's inference system to override custom instructions.

*Mitigation:* Use non-descriptive names ("blue-jay").

---

## IX. Undocumented Capabilities and Emerging Features

### 9.1 Agent Skills System

An open specification (agentskills.io) maintained by Anthropic defines SKILL.md format with YAML frontmatter:

```yaml
---
name: skill-name
description: What this skill does
allowed-tools: Read, Grep, Bash(npm:*)
model: claude-sonnet-4-20250514
---
# Instructions
```

**Progressive disclosure:** Only name+description (~100 bytes) load at startup; full instructions (~2-5K tokens) load on activation. Skill locations include:
- `/mnt/skills/public/` for built-in skills
- `/mnt/skills/user/` for user-uploaded skills
- `.claude/skills/` for project-specific skills

### 9.2 Plugin Architecture

Extends Claude Code with custom commands, agents, hooks, and MCP servers:

```
plugin-name/
├── .claude-plugin/plugin.json
├── commands/
├── agents/
├── skills/
├── hooks/
└── .mcp.json
```

### 9.3 Output Styles

Completely replace Claude Code's system prompt for different use cases. Built-in styles: Default, Explanatory, Learning. Custom styles via `~/.claude/output-styles/*.md`.

### 9.4 Checkpointing

Git-based file checkpointing with `rewindFiles(userMessageUuid)` SDK method for rollback during development.

### 9.5 Todo Lists

Built-in persistent task tracking with `TodoWrite` tool, survives sessions via `CLAUDE_CODE_TASK_LIST_ID` environment variable.

---

## X. Comparative Architecture Analysis

### 10.1 Claude Code vs. Competing Systems

| Feature | Claude Code | Cursor (Composer) | Aider |
|---------|-------------|-------------------|-------|
| **Primary Paradigm** | Autonomous Agent (CLI) | Augmented IDE (GUI) | Pair Programmer (CLI) |
| **Context Strategy** | Just-in-Time (Read/Grep) | Pre-indexed Embeddings (RAG) | Repo Map (AST-based) |
| **File Editing** | Multi-file, deep refactors | Single/Few-file, high speed | Multi-file, git-aware |
| **User Role** | Architect / Supervisor | Pilot / Editor | Pair Programmer |
| **Latency** | High (Planning + Execution) | Low (Autocomplete/Apply) | Medium |
| **Strengths** | Large-scale refactors, research, autonomy | Speed, "Vibe Coding," UI integration | Git integration, diff quality |
| **Weaknesses** | Slow, expensive, context rot | Struggles with global context | UI friction for some |

### 10.2 Transferable Patterns

| Pattern | Origin | Claude Code Applicability | Implementation Path |
|---------|--------|---------------------------|---------------------|
| Indexed Context for Fast Retrieval | Cursor | Adapted | Use MCP servers for codebase indexing; add to CLAUDE.md for dynamic pulls |
| Multi-File Edit Workflows | Aider | Direct | Leverage tasks decomposition; extend with subagents for parallel edits |
| Autonomous Refactors | Devin | Incompatible | Limited by non-visual interface; adapt via verbal planning in plan mode |
| Codebase Summarization | Continue | Adapted | Integrate via skills folders for pre-session compaction |
| Repository Mapping | Aider | Adapted | Tree-sitter parsing + PageRank-style graph ranking; equivalent via well-curated CLAUDE.md or MCP semantic search |

### 10.3 Claude Code Advantages

- 200K context actually delivers (Cursor often limited to 70-120K in practice)
- Terminal-first composability enables scripting and CI/CD integration
- CLAUDE.md hierarchy comparable to Cursor's rules system
- Agentic search means always-fresh context without re-indexing
- Grep-based retrieval is deterministic versus embedding semantic drift

---

## XI. Cognitive Ergonomics and Workflow Patterns

### 11.1 The "Wait" Problem

Unlike sub-100ms autocomplete latency, Claude Code tasks can take minutes to plan and execute. The uncertainty of wait time breaks developer flow state—unable to start new tasks but waiting too long to stare at screen.

**Implications:** Shift from synchronous coding to asynchronous management. Learn to context-switch effectively or run multiple agents in parallel via git worktrees.

### 11.2 Cognitive Load Research

arXiv searches on "human-AI teaming coding" yield guidance:
- Attention management via interruption thresholds (5-10 min supervision loops)
- Trust calibration through verbose logs
- Cognitive load reduced by parallel orchestration (subagents handle ~70% routine)

### 11.3 Recursive Colony Architectures

The ability for Claude Code to call itself creates potential for hierarchical orchestration:

**Structure:** A "Coordinator" agent spawns sub-agents for specific sub-tasks (e.g., "Agent A: Update Database Schema," "Agent B: Update API Endpoints").

**Benefit:** Each sub-agent starts with fresh context window, avoiding context rot of parent. Coordinator only receives final verified output.

**Cost:** Token cost multiplies linearly with agent count, but allows theoretically infinite task complexity through decomposition.

---

## XII. Experimental Research Agenda

### 12.1 Context Degradation Curve

**Goal:** Quantify output quality versus context utilization (10/25/50/75/90%).

**Method:**
- Pick fixed repository and fixed task (implement small feature + tests)
- Pre-fill context using synthetic but realistic artifacts
- Use `/context` to confirm percentage used
- Score outputs via test pass rate, diff correctness, reviewer rating, latency, corrections needed

**Expected Output:** Degradation curve + recommended "safe operating band."

### 12.2 Compaction Loss Taxonomy

**Goal:** Characterize what compaction drops (instructions, code snippets, tool outputs) and how "Compact Instructions" changes retention.

**Method:**
- Seed session with labeled information types (short code, long code, prose requirements, API docs, tabular reference)
- Force compaction using `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` set low
- Query Claude about each content segment's details
- Measure which types degrade first

### 12.3 Instruction-Following Saturation

**Goal:** Test the "150-200 instructions then drift" claim.

**Method:**
- Generate instruction sets by category (do/don't, formatting, security, style, constraints)
- Run standardized tasks and measure violations per category

**Possible result:** Not single threshold but weighted capacity model (some instruction types more "expensive").

### 12.4 Extended Thinking ROI

**Goal:** Identify when extended thinking is worth the cost.

**Method:**
- For each task complexity (toy bug, medium feature, multi-file refactor, greenfield module), run four conditions: no keyword, `think`, `think hard`, `ultrathink`
- Evaluate on task success, defect rate, latency, token usage

**Expected Output:** Task-class-specific heuristic (e.g., "above X complexity, `think hard` dominates").

---

## XIII. Validation Matrix Summary

| Claim | Status | Confidence | Primary Evidence |
|-------|--------|------------|------------------|
| CLAUDE.md hierarchy exists | **CONFIRMED** | High | Official docs, multiple iterations |
| On-demand subdirectory loading | **CONFIRMED** | High | Builder.io, official docs |
| 5-hop import depth limit | **DISPUTED** | Medium | Claude/ChatGPT confirm, Perplexity unverified |
| Extended thinking levels exist | **CONFIRMED** | High | Anthropic best practices |
| Specific token budgets (4K/10K/32K) | **DISPUTED** | Medium | Source code extraction vs. official silence |
| Keywords are budget switches | **CONTRADICTED** | Low | Claude confirms, ChatGPT contradicts |
| Context degrades before 200K | **CONFIRMED** | High | Research + community consensus |
| Auto-compaction is lossy | **CONFIRMED** | High | By definition + official docs |
| 70-80% optimal context threshold | **CORROBORATED** | Medium | Community consensus, variance in estimates |
| Permissions deny → allow → ask order | **CONFIRMED** | High | Official docs |
| Hooks intercept before rules | **CONFIRMED** | High | Official docs |
| MCP local > project > user precedence | **CONFIRMED** | High | Official docs |
| Tasks spawn genuine sub-agents | **CONFIRMED** | High | Agent SDK |
| Task graph is explicit API | **UNVERIFIED** | Low | Not in surfaced official docs |
| Plan Mode uses Opus | **UNVERIFIED** | Low | No official source |
| ~150-200 instruction saturation | **UNVERIFIED** | Low | No official source |

---

## XIV. Open Questions Register

These questions could not be definitively resolved through documentation:

1. **Exact auto-compact trigger threshold:** Reports suggest 64-75% to 95% depending on version and configuration. Behavior may be model-dependent.

2. **MAX_THINKING_TOKENS maximum:** Reports suggest values up to 63,999 possible but not officially documented.

3. **Keyword deprecation timeline:** Will extended thinking keywords be removed, or do they still provide value in current versions?

4. **Context quality curve:** Precise relationship between utilization percentage and output quality lacks quantitative research.

5. **Compaction information preservation:** What specific information types are prioritized versus discarded during compaction?

6. **Enterprise feature parity:** Which features require Team versus Enterprise tier? Documentation gaps exist.

7. **MCP tool context overhead:** Exact context consumption per registered MCP tool not documented.

8. **Instruction saturation point:** Community claims ~150-200 rules before degradation; no official validation found.

9. **Internal task graph representation:** Whether Tasks expose a stable graph abstraction or just parent-child relationships.

10. **Interaction between MCP scope precedence and Enterprise managed MCP policy in complex setups.**

---

## XV. Research Bibliography

### First-Party / Official Sources

- Claude Code settings (scopes, precedence, permissions, tool list, env vars) — code.claude.com/docs/en/settings
- Memory management (CLAUDE.md, @import, max depth) — docs.anthropic.com/en/docs/claude-code/memory
- Common workflows (extended thinking) — code.claude.com/docs/en/common-workflows
- How Claude Code works (context window + compaction) — docs.anthropic.com
- Hooks reference (PreCompact, SessionStart, PermissionRequest) — code.claude.com/docs/en/hooks
- MCP integration docs (schema, scopes, OAuth, tool search) — code.claude.com/docs/en/mcp
- CLI reference — code.claude.com/docs/en/cli-reference
- Agent SDK overview — platform.claude.com/docs/en/agent-sdk/overview
- Agent SDK permissions — platform.claude.com/docs/en/agent-sdk/permissions
- Context windows — platform.claude.com/docs/en/build-with-claude/context-windows
- Extended thinking — platform.claude.com/docs/en/build-with-claude/extended-thinking
- Best practices — anthropic.com/engineering/claude-code-best-practices
- GitHub repository — github.com/anthropics/claude-code

### Community / Triangulation Sources

- Reddit r/ClaudeAI workflow patterns, multi-agent systems, MCP usage
- GitHub issues: permissions bypass, parsing edge cases, proposed directory-level restrictions
- Hacker News discussions of workflow ergonomics and "swarms" culture
- YouTube tutorials for UI demonstrations
- X posts from @alexalbert__, @daboross, @mitsuhiko, @bcherny, @steipete
- Builder.io CLAUDE.md guide
- CodeWithMukesh .NET CLAUDE.md guide
- Agent Skills specification (agentskills.io)
- Simon Willison's source code extraction (April 2025)
- Steve Kinney's compaction analysis

### Research Papers

- Liu et al. (2023) "Lost in the Middle" — context position effects on LLM performance
- NoLiMa Benchmark — context length evaluation across models

---

## Appendix: Prompt Refinement Recommendations for Future Research

Based on what surfaces cleanly from current sources:

1. **Split Phase 1 questions into "documented behavior" versus "inferred internals."** This helps avoid chasing answers that aren't public yet.

2. **Add version pinning step.** Capture Claude Code version(s) and date-stamp all findings; many behaviors are release-sensitive.

3. **Rephrase numeric/implementation questions into experiment-design prompts.** "How can we empirically estimate thinking budgets?" rather than "What is the budget?"

4. **Add dedicated line of inquiry for hooks and managed MCP** as the de-facto policy surface, under-emphasized in community guides but strongly represented in official docs.

5. **Make on-demand subtree CLAUDE.md loading and MCP scope/precedence explicit architectural pillars.** They show up repeatedly in high-quality docs and are central to advanced workflows.

6. **Add experiment harness appendix** for claims systematically unanswerable from docs (task internals, compaction loss), with runnable probes and scoring rubrics.

7. **Separate "authoritative claims" from "ergonomic best practices"** to keep the guide honest by labeling normative workflow advice versus documented mechanics.

---

*This synthesis coalesces research iterations from Claude, ChatGPT, Gemini, Grok, and Perplexity, preserving convergent findings, productive contradictions, and open questions as navigable dimensions rather than resolved conclusions.*
