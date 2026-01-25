# OpenAI Codex Ecosystem: Canonical Reference

**Version**: 1.0.0
**Synthesized**: 2026-01-25
**Sources**: codex/ directory (9 files, 49K words) + research synthesis
**Compression**: 49K → 5.8K words (88% reduction)

---

## Executive Frame

OpenAI's ecosystem centers on an **API-first paradigm** where intelligence is accessed through structured function calling schemas rather than direct tool execution. The January 2026 landscape shows radical transformation: GPT-5.2 replaced GPT-4, Operator merged into ChatGPT agent mode, Assistants API announced deprecation (August 2026), and the Responses API emerged as the recommended entry point for agentic workflows.

The strategic pivot toward agents manifests in Codex (cloud coding agent), Atlas (browser automation), and a unified Agents SDK. Unlike Claude Code's terminal-first philosophy, OpenAI emphasizes cloud-native parallel execution with sandbox isolation. The ecosystem serves enterprise needs through tiered access (Free/Go/Plus/Pro/Business/Enterprise) while maintaining API parity for developers seeking programmatic control.

For Ψ Constellation integration, OpenAI provides unique capabilities (video generation, real-time web search, parallel PR review) that complement Claude's superior reasoning and code generation.

---

## TERM Blocks: Core Concepts

```
TERM CodexArchitecture:
sutra: "Cloud-native coding agent with parallel sandbox execution—move fast, iterate"
gloss:
    Codex operates as OpenAI's answer to Claude Code but with fundamentally different
    philosophy. Cloud-first execution enables parallel tasks in isolated containers
    while CLI interface provides local interactive mode. The model (GPT-5.2-Codex)
    optimizes for production code generation and team collaboration.
spec:
    type: TERM
    paradigm: cloud-first (vs Claude Code's terminal-first)
    execution_modes: [cloud_sandbox, cli_interactive, cli_headless, ide_extension]
    parallel_capability: true (multiple cloud tasks simultaneous)
    github_native: true (@codex mentions, PR reviews, Actions)
    approval_modes: [suggest, auto_edit, full_auto]
    config_location: ~/.codex/config.toml
    mcp_support: STDIO via config
    open_source: CLI is Apache 2.0
end

TERM ResponsesAPI:
sutra: "Recommended entry point—built-in tools replace manual orchestration"
gloss:
    Responses API supersedes both Chat Completions and deprecated Assistants API,
    providing native support for web_search, file_search, computer_use, and
    code_interpreter tools. Remote MCP server support enables external integrations.
    This represents OpenAI's shift from "bring your own tools" to "use our tools."
spec:
    type: TERM
    status: GA (recommended)
    replaces: [assistants_api, chat_completions_for_agents]
    built_in_tools: [web_search, file_search, computer_use, code_interpreter]
    mcp_support: remote servers via HTTP/SSE
    key_advantage: reduced orchestration complexity
end

TERM AssistantsAPIDeprecation:
sutra: "Threads with tool delegation—sunsetting August 2026"
gloss:
    Assistants API provided persistent conversation state, file search, code
    interpreter, and function calling. The thread abstraction enabled stateful
    agents but required significant orchestration overhead. Migration to Responses
    API is mandatory before August 2026 sunset.
spec:
    type: TERM
    status: DEPRECATED
    sunset_date: 2026-08-26
    replacement: responses_api
    capabilities: [threads, file_search, code_interpreter, functions]
    migration_path: platform.openai.com/docs/assistants-migration
end

TERM AgentModeIntegration:
sutra: "Operator merged into ChatGPT—browser automation without standalone app"
gloss:
    Operator launched January 2025 as standalone browser agent, then integrated
    into ChatGPT as "agent mode" July 2025. Visual browser (GUI automation),
    text browser (reasoning-based), terminal, and task scheduling unified under
    single interface. Watch mode enforces supervision on sensitive sites.
spec:
    type: TERM
    launch: 2025-01-23 (Operator) → 2025-07-17 (integrated)
    capabilities: [visual_browser, text_browser, terminal, connectors_60plus, scheduling]
    safety: [watch_mode, 100pct_financial_confirmation, blocklist]
    limits: Plus ~40/mo, Pro ~400/mo, Business pooled
    api: CUA (computer-use-preview) for Tier 3-5 developers
end

TERM FunctionCallingParadigm:
sutra: "Declare capabilities, receive structured calls—API-native tool interface"
gloss:
    OpenAI's tool interface centers on JSON schemas defining function signatures.
    Models determine when to call tools and return structured requests; execution
    happens externally. This contrasts with Claude Code's direct tool execution.
    Structured outputs guarantee schema compliance for reliable parsing.
spec:
    type: TERM
    interface: json_schema definitions
    execution: external (model requests, developer executes)
    structured_outputs: guaranteed schema compliance
    mcp_adoption: 2025-03 (same protocol as Anthropic)
    advantage: composable, testable, version-controllable
end

TERM HiddenSpecMode:
sutra: "Say 'spec' not 'plan'—unlocks structured output with acceptance criteria"
gloss:
    Practitioner-discovered feature: prompting Codex with "make a spec" instead of
    "make a plan" triggers dramatically more structured output. Plan yields 6-7
    bullets; spec yields sections (Goal, Backend, UI/UX, Acceptance, Open Questions).
    The Acceptance section proves critical for long-running task validation.
spec:
    type: TERM
    trigger_word: "spec" (vs "plan")
    output_sections: [goal, backend, ui_ux, acceptance_criteria, open_questions]
    use_case: tasks >15 min runtime where plan review critical
    source: practitioner discovery (@kr0der)
end

TERM AgentsSDK:
sutra: "Lightweight multi-agent orchestration—Swarm graduated to production"
gloss:
    Agents SDK (Python: openai-agents, TypeScript: @openai/agents) provides
    production-ready multi-agent orchestration evolved from experimental Swarm.
    Supports agents, handoffs, guardrails, sessions, and built-in tools with
    native MCP integration for external capabilities.
spec:
    type: TERM
    packages: [openai-agents-python v0.5+, @openai/agents typescript]
    capabilities: [agents, handoffs, guardrails, sessions, built_in_tools, mcp]
    predecessor: swarm (experimental)
    status: GA
end

TERM MediaStack:
sutra: "Sora video + GPT-Image—pure additive capabilities Claude lacks"
gloss:
    OpenAI's media generation provides capabilities absent from Claude: Sora 2
    generates 4-25 second videos with synchronized audio; GPT-Image 1.5 handles
    generation and editing. These represent pure additive value for Constellation
    workflows requiring video or advanced image manipulation.
spec:
    type: TERM
    video: sora-2, sora-2-pro (4-25 sec, 480p-1080p, audio sync)
    image: gpt-image-1.5, gpt-image-1, gpt-image-1-mini
    deprecated_image: DALL-E 2/3 (May 2026)
    access: Plus limited, Pro priority, API pay-per-unit
    watermark: visible + C2PA metadata
    restrictions: no EU/UK (Sora), real people blocked
end

TERM DeepResearch:
sutra: "Multi-step autonomous research agent—30-minute comprehensive reports"
gloss:
    Deep Research executes multi-step autonomous research with web search,
    source synthesis, and structured report generation. Produces comprehensive
    analysis that would take humans hours in approximately 30 minutes. Unique
    capability for market research, literature review, competitive analysis.
spec:
    type: TERM
    capability: autonomous multi-step web research
    output: comprehensive reports with citations
    duration: 15-30 minutes typical
    limits: Free 5 light/mo, Plus 10+15/mo, Pro extended
    fallback: lightweight version after quota
end
```

---

## Service Matrix: Tiers and Capabilities

| Capability | Free | Plus ($20) | Pro ($200) | Business ($25/seat) | Enterprise | API |
|------------|------|------------|------------|---------------------|------------|-----|
| **GPT-5.2 Instant** | 10/5hr | 160/3hr* | Unlimited | Unlimited | Pool | Pay-per-token |
| **GPT-5.2 Thinking** | No | 3K/week | Unlimited | 3K/week | Pool | Pay-per-token |
| **Codex Cloud** | No | Yes | Priority | Yes | Yes | Via key |
| **Agent Mode** | No | ~40/mo | ~400/mo | ~40/mo | Pool | CUA API (Tier 3-5) |
| **Deep Research** | 5 light | 10+15/mo | Extended | 10+15/mo | Pool | Limited |
| **Sora Video** | No | 1K credits | 10K + relaxed | Consumer | No | $0.10-0.50/sec |
| **Image Gen** | 2-3/day | 50/3hr | Unlimited | 100/3hr | Unlimited | $0.01-0.17/img |
| **Connectors** | No | Yes | Yes | 60+ apps | Custom | MCP |
| **File Uploads** | 3/day | 80/3hr | 80/3hr | 80/3hr | 80/3hr | 2M tokens/file |
| **SSO/SCIM** | No | No | No | SAML/OIDC | Full | Yes |
| **Data Training** | Opt-out | Opt-out | Opt-out | No (default) | No (default) | No (default) |

*Plus GPT-5.2 limit noted as "temporary increase—will revert"

---

## Competitive Positioning: Codex vs Claude Code

```
COMP CodexVsClaudeCode:
sutra: "Cloud-parallel vs terminal-focused—complementary not competitive"
gloss:
    Codex and Claude Code optimize for different workflows. Codex excels at
    parallel cloud execution (10 PRs simultaneously), GitHub-native integration
    (@codex mentions), and "move fast" iteration. Claude Code excels at deep
    reasoning, investigative debugging, and architecture work requiring careful
    deliberation.
spec:
    type: COMP

    codex_strengths:
      - parallel_cloud_tasks: true
      - github_native: deep (@codex, Actions, PR review)
      - execution_speed: fast iteration
      - sandbox_isolation: per-task containers
      - open_source_cli: Apache 2.0

    claude_strengths:
      - reasoning_depth: "measure twice, cut once"
      - investigative: debugging, architecture
      - local_by_default: direct file access
      - context_persistence: session continuity
      - code_quality: superior generation

    routing_rules:
      quick_scaffolding: codex
      parallel_pr_review: codex
      github_workflows: codex
      complex_refactoring: claude_code
      investigative_debugging: claude_code
      architecture_decisions: claude_code

    combination_pattern: multi-agent verification, cross-validation
end
```

---

## Deprecation Timeline

| Item | Deprecation | Shutdown | Replacement | Action |
|------|-------------|----------|-------------|--------|
| Assistants API | 2025-08-26 | 2026-08-26 | Responses API | Migrate to built-in tools |
| Realtime API Beta | — | 2026-02-27 | Realtime GA | Upgrade endpoints |
| DALL-E 2/3 | 2025-11-14 | 2026-05-12 | GPT-Image 1.5 | Update model calls |
| chatgpt-4o-latest | 2025-11-18 | 2026-02-17 | Dated snapshots | Pin versions |
| Operator (standalone) | 2025-07-17 | 2025-08-31 | ChatGPT agent mode | Use integrated |

---

## Integration Patterns for Ψ Constellation

```
PROC OpenAIRouting:
sutra: "Route unique capabilities to OpenAI, reasoning to Claude"
spec:
    type: PROC

    decision_tree:
      video_generation: → openai_sora
      realtime_web_search: → openai_search
      autonomous_research: → openai_deep_research
      github_pr_review: → openai_codex
      browser_automation: → openai_agent_mode
      multi_app_workflow: → openai_connectors
      complex_reasoning: → claude (primary) + o3_pro (verification)
      creative_writing: → claude
      large_codebase: → claude + gpt41 (context)
      default_coding: → claude_code (local) + codex (parallel)

    handoff_patterns:
      ui: explicit user invocation or capability detection
      api: claude orchestrates, calls openai endpoints
      mcp: shared servers serve both providers
end

PROC SharedMCPPattern:
sutra: "Single tool implementation serves both orchestrators"
spec:
    type: PROC

    protocol: MCP (adopted by OpenAI March 2025)
    transports: [stdio, sse, streamable_http]

    pattern: |
      # MCP server works with both Claude and OpenAI
      from mcp import FastMCP
      server = FastMCP("shared-tools")

      @server.tool()
      def query_database(query: str) -> str:
          return execute_query(query)

    benefits:
      - single_implementation: one codebase
      - provider_agnostic: switch without rewrite
      - composable: mix tools from either ecosystem
end
```

---

## Unique Capabilities Matrix (Pure Additive)

| Capability | Description | Workflow Example |
|------------|-------------|------------------|
| **Sora Video** | Text/image-to-video, 25s, synced audio | Marketing: product explainer from text brief |
| **ChatGPT Search** | Integrated real-time web with sources | Research: current events with inline citations |
| **Deep Research** | Multi-step autonomous agent | Analysis: comprehensive market research in 30min |
| **Codex Parallelization** | Multiple isolated sandbox tasks | DevOps: review 10 PRs simultaneously |
| **GitHub @codex** | Native PR/issue integration | Automation: code review on every PR |
| **Agent Mode** | Full browser automation | Operations: book appointments autonomously |
| **60+ Connectors** | Native app integrations | Productivity: pull context from Slack+Drive+GitHub |
| **Voice Screenshare** | Visual context in voice chat | Support: show screen while voice chatting |
| **GPT Store** | Custom GPT marketplace | Discovery: specialized tools for workflows |
| **AGENTS.md** | Per-repo agent configuration | Standards: consistent agent behavior across team |

---

## Cost Model: When to Route to OpenAI

```
ECON OpenAIValueThresholds:
sutra: "Plus for occasional, Pro for heavy, API for integration"
spec:
    type: ECON

    plus_20_breaks_even_when:
      - >15K GPT-5.2 output tokens/month
      - OR >120 images/month
      - OR regular deep_research/agent_mode/voice

    pro_200_breaks_even_when:
      - heavy video (>500 sec Sora/month)
      - heavy o3-pro reasoning
      - unlimited voice needed
      - deep research power user (>50/month)

    recommended_configuration:
      individual_developer: claude_pro + openai_plus (~$40/mo)
      power_researcher: claude_pro + openai_pro (~$220/mo)
      small_team_5: claude_team + openai_business (~$200-300/mo)
      api_automation: claude_api + openai_api (variable)

    upgrade_triggers:
      to_pro: need video/unlimited reasoning
      to_business: need SSO/shared projects
      downgrade_from_pro: not using video/unlimited
end
```

---

## Anti-Patterns and Practitioner Insights

```
WARN CodexAntiPatterns:
sutra: "Discovered failure modes from practitioner experience"
spec:
    type: WARN

    patterns:
      plan_not_spec:
        problem: "make a plan" yields 6-7 bullets
        solution: "make a spec" yields structured sections with acceptance criteria
        source: @kr0der practitioner discovery

      ignoring_cloud_limits:
        problem: internet disabled during cloud execution
        solution: pre-fetch dependencies, use local for web-dependent tasks

      approval_mode_mismatch:
        problem: full_auto on untested repos
        solution: start suggest, graduate to auto_edit, reserve full_auto for trusted

      missing_agents_md:
        problem: inconsistent behavior across repos
        solution: define AGENTS.md with per-repo instructions

      parallel_confusion:
        problem: losing track of multiple cloud tasks
        solution: name tasks, use project organization, check cloud dashboard
end
```

---

## Verification Checklist

- [x] API paradigm documented (function calling, Responses API)
- [x] Deprecation timeline complete (Assistants API, DALL-E)
- [x] Tier gating comprehensive (Free through Enterprise)
- [x] Competitive positioning fair (Codex vs Claude Code)
- [x] Integration patterns concrete (routing tree, MCP sharing)
- [x] Unique capabilities enumerated (Sora, Deep Research, etc.)
- [x] Cost model actionable (break-even thresholds)
- [x] Practitioner insights preserved (spec mode, anti-patterns)

---

*"API-native agents with function schemas—OpenAI declares, you execute. The Constellation routes unique capabilities while Claude orchestrates the whole."*

**END SYNTHESIS**
