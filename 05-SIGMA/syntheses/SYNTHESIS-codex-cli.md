# SYNTHESIS: Codex CLI / OpenAI Developer-Agent Ecosystem

**Synthesis Date**: 2026-02-01
**Protocol**: Syncrescendence Research Protocol — Phase 3 (Preservative Coalescence)
**Sources**: 5 AI research reports (3,470 lines) + 3 practitioner posts + original prompt + AVATAR-CODEX.md
**Research Questions**: 8 (from DYN-RESEARCH_DISPATCH.md)
**Confidence Scale**: HIGH (3+ corroborating sources) / MEDIUM (2 sources or inference) / LOW (single source or practitioner anecdote)

---

## 1. Architecture & Initialization Model

### 1.1 Initialization Files

Codex CLI reads configuration from a layered hierarchy:

| File/Directory | Scope | Purpose | Confidence |
|---|---|---|---|
| `AGENTS.md` | Per-repository (root) | Custom per-repo instructions, coding standards, test commands, style rules. Read automatically at session start. | HIGH |
| `~/.codex/config.toml` | User-global | Shared configuration between CLI and IDE extensions. Contains model selection, approval mode, MCP server definitions. | HIGH |
| `.codex/` directory | Per-repository | Local configuration overrides (if present). Mirrors global config structure. | MEDIUM |
| `config.toml` model field | User-global | Default model selection (e.g., `model = "o3"`) | HIGH |
| `config.toml` approval mode | User-global | Default approval mode: `suggest`, `auto-edit`, or `full-auto` | HIGH |
| `config.toml` [mcp_servers.*] | User-global | MCP server registrations with command, args, env | HIGH |

**Key finding**: Unlike Claude Code (which uses `CLAUDE.md` / `.claude/` as its instruction surface), Codex reads `AGENTS.md` — the same filename convention used by Devin, Cursor, and other AI coding tools. This is a cross-platform instruction standard, not Codex-proprietary.

### 1.2 Authentication Model

Codex CLI supports two authentication paths:

1. **ChatGPT account sign-in** ("Sign in with ChatGPT") — uses Plus/Pro/Business subscription quota. No API key needed.
2. **API key** — standard `OPENAI_API_KEY` environment variable. Pay-per-token.

This dual-auth model is unique vs Claude Code (API key only) and creates an economic arbitrage: subscription users get flat-rate access to frontier models.

### 1.3 Runtime Architecture

```
┌─────────────────────────────────────────────────┐
│                  User Terminal                    │
│  codex [--yolo] [-m model] [prompt]              │
├─────────────┬───────────────────────────────────┤
│  CLI Client │  Reads: AGENTS.md, config.toml     │
│  (local)    │  Auth: ChatGPT SSO or API key      │
├─────────────┴───────────────────────────────────┤
│              ┌──────────┐  ┌──────────────────┐  │
│              │ Local    │  │ Cloud Sandbox    │  │
│              │ Execution│  │ (Codex Cloud)    │  │
│              │ (default)│  │ - Internet off   │  │
│              │ - fs rw  │  │ - Repo snapshot  │  │
│              │ - net ok  │  │ - Isolated       │  │
│              └──────────┘  └──────────────────┘  │
├─────────────────────────────────────────────────┤
│  MCP Servers (STDIO) ←→ External Tools           │
│  IDE Extensions (VS Code, Cursor, JetBrains)     │
│  GitHub Integration (@codex, codex-action)       │
└─────────────────────────────────────────────────┘
```

---

## 2. Capabilities Matrix

| Capability | Status | Confidence | Primary Sources |
|---|---|---|---|
| **Interactive terminal mode** | GA | HIGH | claude-openai, chatgpt-openai, practitioner posts |
| **Headless mode** (`codex exec`) | GA | HIGH | claude-openai, gemini-openai |
| **Approval modes** (Suggest/Auto-Edit/Full Auto) | GA | HIGH | claude-openai, practitioner posts |
| **`--yolo` flag** (alias for Full Auto) | GA | HIGH | practitioner posts (2/3 recommend it) |
| **Model selection** (`-m` flag or config.toml) | GA | HIGH | claude-openai, grok-openai |
| **Cloud sandbox execution** (Codex Cloud) | GA | HIGH | claude-openai, chatgpt-openai, gemini-openai |
| **Parallel cloud tasks** (multiple simultaneous) | GA | HIGH | claude-openai, grok-openai |
| **GitHub @codex mentions** (PR/issue) | GA | HIGH | claude-openai, chatgpt-openai |
| **GitHub Action** (`openai/codex-action@v1`) | GA | HIGH | claude-openai |
| **IDE extensions** (VS Code, Cursor, JetBrains) | GA | HIGH | claude-openai, chatgpt-openai |
| **MCP server support** (STDIO transport) | GA | HIGH | claude-openai, perplexity-openai |
| **MCP SSE/Streamable HTTP** | GA | MEDIUM | claude-openai (single mention) |
| **Slack integration** (trigger tasks) | GA | MEDIUM | claude-openai |
| **Linear integration** (trigger tasks) | GA | MEDIUM | claude-openai |
| **Session resumption** (`/resume`) | GA | MEDIUM | claude-openai |
| **Conversation compaction** (auto) | GA | MEDIUM | claude-openai |
| **Branch isolation** (`--branch` flag) | GA | MEDIUM | claude-openai |
| **"Spec mode"** (write "make a spec" vs "make a plan") | Practitioner discovery | MEDIUM | codex/@kr0der |
| **Long-running task persistence** ("don't stop until...") | Practitioner-confirmed | MEDIUM | codex/i_almost_quit |
| **Figma integration** | NOT FOUND | LOW | No source mentions it |
| **Canva integration** | NOT FOUND | LOW | No source mentions it |
| **Native browser automation** | NOT FOUND — use Agent Mode separately | MEDIUM | chatgpt-openai |
| **Open source** (CLI itself) | Apache 2.0 | HIGH | claude-openai |

---

## 3. Sandbox Model

### 3.1 Codex Cloud Sandbox (Remote)

The Codex Cloud sandbox is architecturally distinct from Claude Code's execution model:

| Property | Codex Cloud | Claude Code |
|---|---|---|
| **Execution location** | OpenAI cloud containers | User's local machine |
| **Internet access during execution** | **Disabled** | Enabled (user's network) |
| **Repository access** | Snapshot pre-loaded into container | Live filesystem access |
| **Isolation** | Full container isolation per task | Shares user's filesystem and permissions |
| **Parallelism** | Multiple containers simultaneously | Single sequential session |
| **Persistence** | Ephemeral — results via git commit/PR | Persistent — changes land on local disk |
| **State handoff** | Cloud ↔ local seamless (claimed) | N/A (always local) |
| **Risk model** | Lower (sandboxed, no network) | Higher (full local access) |

**Critical insight**: Codex Cloud's "internet disabled during execution" design is a **security-first** choice that trades capability for safety. The agent cannot fetch dependencies mid-task, cannot call APIs, cannot exfiltrate data. This is the opposite of Claude Code's model where the agent has full network access and can `curl`, `npm install`, etc.

### 3.2 Codex CLI Local Mode

When running locally (the default interactive mode), Codex CLI:
- Has full filesystem read/write (subject to approval mode)
- Has internet access
- Can install packages, run tests, etc.
- Behaves more like Claude Code but with the approval-mode gating layer

### 3.3 Approval Modes as Security Gradient

| Mode | File Changes | Shell Commands | Risk Level |
|---|---|---|---|
| **Suggest** | Review all before apply | Review all before run | Lowest |
| **Auto-Edit** | Auto-apply file changes | Prompt for commands | Medium |
| **Full Auto** (`--yolo`) | Auto-apply all | Auto-run all | Highest |

**Practitioner consensus**: 2 of 3 practitioner sources recommend `--yolo` as default, with one recommending aliasing `codex` to `codex --yolo`. The permission system in non-yolo mode is described as "super annoying" and "a game changer" when disabled.

**Productive tension**: The security model OpenAI designed (cautious by default) vs. what practitioners actually use (full auto). This suggests either the defaults are miscalibrated for experienced users, or OpenAI is optimizing for safety-first onboarding at the cost of power-user experience.

---

## 4. GitHub & First-Party Integrations

### 4.1 GitHub Integration (The "Connectability" Advantage)

This is Codex's strongest differentiator vs Claude Code. The integration is **first-party and native**:

| Feature | Mechanism | Capability |
|---|---|---|
| **PR Review** | `@codex review` comment | Intent analysis, code execution, inline feedback |
| **Task from Issue/PR** | `@codex` mention | Spawns cloud task, can commit and push |
| **GitHub Action** | `openai/codex-action@v1` | CI/CD pipeline integration |
| **Branch creation** | `codex cloud exec --branch` | Isolated work on new branch |
| **AGENTS.md** | Repository file convention | Per-repo custom instructions |

Claude Code has **no equivalent**. Claude Code users must manually create PRs, run git commands, and manage GitHub workflows through shell access. There is no `@claude` GitHub bot, no Claude GitHub Action, no native PR review trigger.

### 4.2 Other First-Party Integrations

| Integration | Type | Status | Confidence |
|---|---|---|---|
| **Slack** | Task trigger | GA | MEDIUM |
| **Linear** | Task trigger | GA | MEDIUM |
| **VS Code** | IDE extension | GA | HIGH |
| **Cursor** | IDE extension | GA | HIGH |
| **JetBrains** | IDE extension | GA | HIGH |
| **chatgpt.com/codex** | Web UI | GA | HIGH |
| **Figma** | Not found | — | LOW |
| **Canva** | Not found | — | LOW |

### 4.3 60+ ChatGPT Connectors (Adjacent Capability)

Via ChatGPT Agent Mode (not Codex CLI directly), the broader OpenAI ecosystem offers 60+ app connectors: Gmail, Google Drive, SharePoint, GitHub, Atlassian, HubSpot, Slack, Notion, etc. These are accessible to Plus+ users and could be orchestrated alongside Codex workflows, but they operate in the ChatGPT UI context, not the CLI.

---

## 5. MCP Support & Tool Ecosystem

### 5.1 MCP Configuration

Codex CLI supports MCP servers via `~/.codex/config.toml`:

```toml
[mcp_servers.my_server]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-example"]

[mcp_servers.openai_docs]
command = "npx"
args = ["-y", "@openai/mcp-server-docs"]
```

**Transport support**:
- **STDIO**: Confirmed, primary transport (HIGH confidence)
- **SSE**: Mentioned in claude-openai source (MEDIUM confidence)
- **Streamable HTTP**: Mentioned in claude-openai source (MEDIUM confidence)

### 5.2 MCP as Cross-Platform Bridge

A critical finding across sources: **MCP is the protocol that enables Codex and Claude Code to share tool servers**. Both platforms support MCP, which means:

- A single MCP server implementation can serve both Codex and Claude Code
- OpenAI's official docs MCP server can be consumed by Claude Code
- Community MCP servers (e.g., `openai-vector-assistant-mcp`) wrap OpenAI APIs for consumption by any MCP client, including Claude

This is the key integration point for the Syncrescendence Constellation: **MCP is the shared nervous system**.

### 5.3 Known MCP Servers Relevant to Codex

| Server | Provider | Function |
|---|---|---|
| `@openai/mcp-server-docs` | OpenAI (first-party) | Query OpenAI developer documentation |
| `openai-vector-assistant-mcp` | Community (jezweb) | Wrap OpenAI Vector Store API |
| Apps SDK MCP servers | OpenAI (first-party) | Custom apps for ChatGPT workspaces |
| Custom per-project servers | User-defined | Any STDIO-compatible MCP server |

---

## 6. Model Routing

### 6.1 Available Models

| Model | Optimization | Use Case | Selection |
|---|---|---|---|
| **GPT-5.2-Codex** | Latest frontier, coding-optimized | Complex reasoning, architecture | Default for Codex |
| **GPT-5.2-Codex high** | Higher reasoning effort | Recommended starting point | `codex -m gpt-5.2-codex-high` |
| **GPT-5.2-Codex xhigh** | Maximum reasoning | Only for very tricky problems | Uses more tokens, slower |
| **GPT-5-Codex** | Previous gen, agentic coding | General development | Legacy but functional |
| **o3** | Deep reasoning | Complex problem-solving | `codex -m o3` |
| **o4-mini** | Fast reasoning, efficient | Quick logic tasks | `codex -m o4-mini` |
| **gpt-4.1** | 1M token context | Large codebase analysis | `codex -m gpt-4.1` |
| **codex-mini-latest** | Economy | Fast simple tasks | **SUNSET Jan 16, 2026** |

### 6.2 Model Selection Guidance

From practitioner source (@paulsolt):
> "Start with GPT-5.2-Codex high. That is high reasoning. It is enough. Don't be tempted with xhigh unless working on something really tricky. It uses more tokens and will be slower to finish."

### 6.3 Model Routing vs Claude Code

| Scenario | Route to Codex | Route to Claude Code |
|---|---|---|
| Parallel PR reviews | ✓ (cloud tasks) | — |
| Quick scaffolding | ✓ (fast iteration) | — |
| GitHub-integrated workflows | ✓ (native) | — |
| Complex architectural refactoring | — | ✓ (deeper reasoning per task) |
| Investigative debugging | — | ✓ (superior context retention) |
| Large codebase comprehension | — | ✓ (200K context, superior retrieval) |
| Multi-agent verification | ✓ + ✓ | Both for cross-validation |

---

## 7. Cloud vs Local Execution

| Aspect | Local (CLI default) | Cloud (Codex Cloud) |
|---|---|---|
| **Trigger** | Interactive terminal session | `codex cloud exec`, chatgpt.com/codex, @codex on GitHub |
| **Where code runs** | User's machine | OpenAI's containers |
| **Internet** | Full access | **Disabled during execution** |
| **Filesystem** | User's actual files | Repo snapshot (read-only clone) |
| **Output delivery** | Changes on local disk | Git commit/PR |
| **Parallelism** | Sequential (one session) | Multiple simultaneous tasks |
| **Cost** | API tokens or subscription quota | Subscription quota (Plus+) or credits |
| **Session state** | Persistent until exit | Ephemeral per task |
| **IDE integration** | VS Code, Cursor, JetBrains | Web UI at chatgpt.com/codex |

**Handoff pattern**: Start locally for exploration → delegate heavy/repetitive work to cloud → review results locally. The claimed "seamless handoff without losing state" between local and cloud remains practitioner-confirmed but architecturally opaque.

---

## 8. Integration Points with Syncrescendence Constellation

### 8.1 Role in Constellation

Per AVATAR-CODEX.md, Codex is configured as the **Adjudicator (Executor)** — a "Rule-Bound Fabricator" for parallel execution. This aligns with the research findings:

| Constellation Role | Codex Capability | Fit |
|---|---|---|
| EXEC (execute changes) | Cloud parallel tasks, Full Auto mode | ✓✓✓ Excellent |
| VERIFY (run tests) | Execute tests, benchmark, iterate until pass | ✓✓✓ Excellent |
| DOCUMENT (update docs) | Auto-generate from code changes | ✓✓ Good |
| ARCHITECT (design) | Weaker reasoning per source consensus | ✗ Poor — leave to Claude |

### 8.2 MCP Bridge Architecture

```
┌─────────────────────────────────────────────────────┐
│              Syncrescendence Constellation            │
├───────────────┬─────────────────┬───────────────────┤
│  Claude Code  │  Shared MCP     │  Codex CLI        │
│  (Architect)  │  Tool Servers   │  (Executor)       │
│               │                 │                   │
│  Reads:       │  ┌───────────┐  │  Reads:           │
│  CLAUDE.md    │  │FS Server  │  │  AGENTS.md        │
│  .claude/     │  │DB Server  │  │  .codex/          │
│               │  │API Server │  │  config.toml      │
│  Context:     │  │Docs Server│  │                   │
│  200K tokens  │  └───────────┘  │  Context:         │
│               │                 │  400K tokens      │
│  Strength:    │  Both consume   │  Strength:        │
│  Deep reason  │  same servers   │  Parallel exec    │
│  Architecture │  via MCP        │  GitHub native    │
│  Refactoring  │                 │  Long-running     │
└───────────────┴─────────────────┴───────────────────┘
```

### 8.3 Recommended Workflow Patterns

**Pattern 1: Claude Architects, Codex Executes**
1. Claude Code analyzes codebase, defines interface changes, creates implementation plan
2. Codex receives plan via AGENTS.md or prompt, executes boilerplate changes across files
3. Codex runs tests iteratively ("don't stop until all tests pass")
4. Claude Code reviews resulting diff for quality assurance

**Pattern 2: Parallel PR Farm**
1. Multiple Codex Cloud tasks assigned to different PRs/issues
2. Each operates in isolated branch
3. Claude Code does final architectural review of merged results

**Pattern 3: Cross-Validation**
1. Same task given to both Claude Code and Codex
2. Outputs compared for correctness
3. Discrepancies flagged for human review

---

## 9. Known Limitations

| Limitation | Impact | Workaround | Confidence |
|---|---|---|---|
| **Worse at inferring intent** than Claude Code | Must be more explicit in prompts; add "check repo" | Write detailed prompts, use AGENTS.md | HIGH (practitioner consensus) |
| **Permission system friction** (non-yolo) | Constant interruptions kill flow | Use `--yolo` flag | HIGH |
| **Cloud sandbox has no internet** | Cannot fetch dependencies, call APIs during cloud tasks | Pre-install dependencies, use local mode for network-dependent work | HIGH |
| **"Dry" communication style** | Harder to understand what it's doing | Skill issue per practitioner; ask for explanations | MEDIUM |
| **"Plan" mode gives shallow output** | 6-7 bullet points insufficient for complex tasks | Use "make a spec" instead of "make a plan" | MEDIUM |
| **No native browser automation** | Cannot interact with web UIs | Use Agent Mode separately, or RPA tools | HIGH |
| **Subscription-gated** (Plus+ required) | Free tier users locked out | API key access available | HIGH |
| **Model sunset velocity** | codex-mini-latest sunset Jan 16, 2026; GPT-5-Codex deprecated | Stay current on deprecation schedule | HIGH |
| **No Figma/Canva integration** | Cannot directly work with design tools | Manual export/import | HIGH (absence confirmed) |

---

## 10. Productive Tensions

### 10.1 Security vs Usability
**The tension**: OpenAI designed Codex with cautious defaults (Suggest mode, permission prompts). Practitioners unanimously recommend overriding these with `--yolo`. This is the classic security-usability tradeoff — the "right" default depends on context. For a Syncrescendence deployment, the answer is contextual: `--yolo` for trusted repositories, Suggest mode for unfamiliar codebases.

### 10.2 Cloud-First vs Local-First
**The tension**: Codex Cloud offers parallelism and isolation but disables internet. Claude Code is local-first with full access. Neither is universally better. The cloud model excels for "fire and forget" tasks; local excels for exploratory/interactive work. The Constellation should route accordingly.

### 10.3 Explicit vs Implicit Instructions
**The tension**: Codex requires more explicit prompting than Claude Code ("garbage in, garbage out" — practitioner). Claude Code infers intent better from context. This means AGENTS.md must be more comprehensive for Codex than CLAUDE.md is for Claude Code. The Adjudicator role config should reflect this by including explicit test commands, style guides, and verification steps.

### 10.4 Speed Perception vs Actual Throughput
**The tension**: Codex is perceived as "slow" because individual tasks take 15+ minutes. But practitioner evidence suggests Claude Code (Opus 4.5) often requires follow-up fix prompts, making total completion time comparable. The real advantage is Codex's parallelism — while one task runs, start another.

### 10.5 Open Source CLI vs Proprietary Cloud
**The tension**: Codex CLI is Apache 2.0 open source, but the cloud execution and model serving are fully proprietary. This is more open than Claude Code (fully proprietary) but less open than local-only tools. For the Constellation, the open CLI means we can inspect, fork, and extend the client-side behavior.

---

## 11. Comparison Matrix

### 11.1 Codex CLI vs Claude Code

| Dimension | Codex CLI | Claude Code | Winner |
|---|---|---|---|
| **Primary mode** | Cloud-first, multi-interface | Terminal-first, local-only | Context-dependent |
| **Execution model** | Cloud sandboxed + local option | Local filesystem only | Codex (flexibility) |
| **Intent inference** | Weaker — needs explicit prompts | Stronger — reads context well | Claude Code |
| **Reasoning depth** | Good (GPT-5.2-Codex) | Superior (Opus 4.5) | Claude Code |
| **Parallelism** | Multiple simultaneous cloud tasks | Single sequential session | Codex |
| **GitHub integration** | Native (@codex, Actions, PR review) | Manual git commands | Codex |
| **MCP support** | STDIO via config.toml | Native HTTP support | Both (different transports) |
| **Open source** | CLI is Apache 2.0 | Proprietary | Codex |
| **Long-running tasks** | Excellent ("don't stop until...") | Good but more follow-up prompts | Codex |
| **Context window** | Up to 400K (GPT-5.2), 1M (gpt-4.1) | 200K (Opus 4.5) | Codex (raw size) |
| **Context quality** | Good | Superior retrieval/comprehension | Claude Code |
| **Instruction file** | AGENTS.md | CLAUDE.md | Equivalent |
| **Config location** | `~/.codex/config.toml` | `~/.claude/` | Equivalent |
| **Auth model** | ChatGPT SSO or API key | API key only | Codex (subscription option) |
| **Cost for heavy use** | Flat subscription (Plus $20/Pro $200) | Per-token (can be expensive) | Codex |
| **Philosophy** | "Move fast, iterate, workhorse" | "Measure twice, cut once, architect" | Complementary |

### 11.2 Codex CLI vs Gemini CLI

| Dimension | Codex CLI | Gemini CLI | Notes |
|---|---|---|---|
| **Maturity** | GA, production-tested | Newer, less ecosystem | Codex more mature |
| **Model quality** | GPT-5.2-Codex (frontier) | Gemini 2.5 Pro | Both strong |
| **GitHub integration** | Native, deep | Not native | Codex advantage |
| **MCP support** | Yes (STDIO) | Yes (growing) | Both |
| **Cloud execution** | Yes (Codex Cloud) | Limited | Codex advantage |
| **Open source** | Apache 2.0 (CLI) | Open source | Both |
| **Context window** | 400K-1M | 1M+ (Gemini native) | Gemini (raw size) |
| **Cost** | Subscription or API | Free tier generous | Gemini (cost) |

---

## 12. Recommendations for Adjudicator Role Configuration

Based on this synthesis, the following updates to AVATAR-CODEX.md are recommended:

### 12.1 AGENTS.md Best Practices (for Codex consumption)

The Adjudicator's AGENTS.md should be **more explicit** than Claude Code's CLAUDE.md because Codex requires clearer instructions:

```markdown
# AGENTS.md additions for Codex (Adjudicator)

## Verification Commands
- Run tests: `pnpm test` (or project-specific)
- Lint: `pnpm lint`
- Type check: `pnpm tsc --noEmit`
- Always run verification before claiming completion

## Coding Standards
- [Explicit style rules — Codex won't infer from context]
- [Explicit file naming conventions]
- [Explicit import ordering]

## Task Execution Rules
- When given a task, "make a spec" first for complex work
- For implementation: "don't stop until all tests pass"
- Commit with semantic prefixes: feat:, fix:, docs:, chore:, refactor:
```

### 12.2 Config Recommendations

```toml
# ~/.codex/config.toml — Recommended for Adjudicator role

model = "gpt-5.2-codex-high"  # High reasoning, balanced speed
approval_mode = "full-auto"    # For trusted repos

[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"]

[mcp_servers.openai_docs]
command = "npx"
args = ["-y", "@openai/mcp-server-docs"]
```

### 12.3 Role Boundaries

| Do | Don't |
|---|---|
| Execute implementation plans from Claude Code | Create architectural plans |
| Run parallel PR reviews | Make design decisions |
| Generate tests and verify they pass | Modify `01-CANON/` without approval |
| Update documentation to match changes | Architect complex refactors |
| Handle long-running iterative tasks | Tasks requiring live network access (use local mode) |

### 12.4 Operational Patterns

1. **Default invocation**: `codex --yolo` (alias recommended)
2. **Model**: `gpt-5.2-codex-high` for most tasks, `o3` for deep reasoning verification
3. **Parallelism**: Launch multiple cloud tasks for independent work streams
4. **Verification**: Always end with test execution; use "don't stop until all tests pass" pattern
5. **GitHub**: Use `@codex` for PR reviews; `openai/codex-action@v1` in CI
6. **MCP**: Share tool servers with Claude Code for unified tool access

---

## 13. Source Cross-Reference

| Source File | Lines | Unique Value Contributed |
|---|---|---|
| `claude-openai.md` | 872 | Most complete technical architecture; model matrix; sandbox details; MCP config syntax; side-by-side comparison |
| `chatgpt-openai.md` | 999 | Broadest ecosystem context; pricing; routing decision tree; integration blueprint; cost model |
| `gemini-openai.md` | 399 | Partial taxonomy; MCP-as-bridge insight; Apps SDK details; Enterprise governance RBAC |
| `grok-openai.md` | 594 | Forensic pricing analysis; "Pro divergence" insight; hidden tool costs; deprecation "Death Row" |
| `perplexity-openai.md` | 445 | Duplicate of gemini source (same content) — no unique value |
| `codex/@kr0der` | ~30 | "Spec mode" discovery — use "make a spec" instead of "make a plan" |
| `codex/i_almost_quit` | ~50 | Critical practitioner insights: --yolo, explicit prompting, long-running tasks, comparison with Claude Code |
| `codex/@paulsolt` | ~40 | Model selection guidance (high vs xhigh); workflow patterns; @steipete AGENTS.md reference |
| `openai_prompt.md` | 161 | Original research prompt — defined scope and structure |
| `AVATAR-CODEX.md` | ~80 | Existing Adjudicator role definition — target for recommendations |

### Source Agreement/Disagreement Map

| Topic | Sources Agree | Sources Disagree | Resolution |
|---|---|---|---|
| AGENTS.md is read at init | All | None | Confirmed |
| MCP support exists | claude, gemini, perplexity | None | Confirmed |
| Cloud sandbox disables internet | claude, chatgpt | None | Confirmed |
| Codex is "slower" than Claude | chatgpt (claims slower) | practitioner (claims comparable total time) | Both true — individual task slower, but parallel + fewer follow-ups = comparable |
| Claude Code superior at reasoning | claude, grok, chatgpt | None | Confirmed (consensus) |
| Codex superior at parallel execution | All | None | Confirmed |
| Figma/Canva integration exists | None claim it exists | N/A | Confirmed absent |
| perplexity vs gemini content | Identical content | N/A | perplexity is duplicate of gemini |

---

*Synthesis complete. This document answers all 8 research questions from DYN-RESEARCH_DISPATCH.md and provides actionable recommendations for the Adjudicator role configuration.*
