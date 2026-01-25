# 07-SIGMA7: Operational Knowledge Corpus

**Version**: 1.0.0
**Generated**: 2026-01-25
**Source**: Research corpus metabolization (223K → 22.7K words)
**Compression**: 90%

---

## Purpose

σ₇ (Sigma-7) contains operational knowledge for AI-amplified workflows—how to configure, orchestrate, and integrate Claude Code with the broader AI ecosystem. This is distinct from 01-CANON (constitutional knowledge about what to believe).

**Epistemic status**: Operational (faster update cadence than CANON)

---

## Structure

```
07-SIGMA7/
├── 00-SYNTHESIS/          # Canonical references (5 docs, 9.2K words)
│   ├── SYNTHESIS-claude_code_architecture.md
│   ├── SYNTHESIS-codex_openai_ecosystem.md
│   ├── SYNTHESIS-gemini_google_ecosystem.md
│   ├── SYNTHESIS-cross_platform_patterns.md
│   └── SYNTHESIS-agents_mcp_foundations.md
│
├── 01-MECHANICS/          # Deep-dive mechanisms (10 docs, 8.6K words)
│   ├── MECH-skill_system_architecture.md
│   ├── MECH-task_orchestration.md
│   ├── MECH-context_compaction_strategies.md
│   ├── MECH-hooks_lifecycle_automation.md
│   ├── MECH-headless_mode_automation.md
│   ├── MECH-mcp_server_patterns.md
│   ├── MECH-subagent_delegation.md
│   ├── MECH-git_worktree_coordination.md
│   ├── MECH-extended_thinking_triggers.md
│   └── MECH-prompt_engineering_patterns.md
│
└── 02-PRACTICE/           # Implementation patterns (7 docs, 4.8K words)
    ├── PRAC-parallel_claude_orchestration.md
    ├── PRAC-ralph_pattern_execution.md
    ├── PRAC-semantic_compression_workflow.md
    ├── PRAC-oracle_to_executor_handoff.md
    ├── PRAC-ledger_management_patterns.md
    ├── PRAC-multi_account_coordination.md
    └── PRAC-cowork_desktop_integration.md
```

---

## Document Index

### 00-SYNTHESIS (Canonical References)

| Document | Words | Scope |
|----------|-------|-------|
| `SYNTHESIS-claude_code_architecture.md` | 1,934 | Agentic loop, context management, CLAUDE.md, skills, tasks, hooks, Plan Mode |
| `SYNTHESIS-codex_openai_ecosystem.md` | 1,916 | OpenAI API architecture, Codex, Responses API, agent mode, deprecations |
| `SYNTHESIS-gemini_google_ecosystem.md` | 1,988 | 1M context advantage, NotebookLM, dual-agent patterns, Labs portfolio |
| `SYNTHESIS-cross_platform_patterns.md` | 1,596 | Chorus Architecture, Oracle-Executor, platform characteristic cognition |
| `SYNTHESIS-agents_mcp_foundations.md` | 1,817 | Agent paradigm, MCP architecture, orchestration patterns |

### 01-MECHANICS (Deep Dives)

| Document | Words | Scope |
|----------|-------|-------|
| `MECH-skill_system_architecture.md` | 947 | Progressive disclosure, SKILL.md format, subagent pairing |
| `MECH-task_orchestration.md` | 1,061 | Dependency management, parallel spawning, persistence |
| `MECH-context_compaction_strategies.md` | 913 | 75% rule, manual vs auto, focus instructions |
| `MECH-hooks_lifecycle_automation.md` | 1,002 | PreToolUse guards, PostToolUse polish, governance |
| `MECH-headless_mode_automation.md` | 795 | -p flag, output formats, CI/CD integration |
| `MECH-mcp_server_patterns.md` | 802 | Server config, context tax mitigation, governance |
| `MECH-subagent_delegation.md` | 806 | Task tool, isolation, custom agents |
| `MECH-git_worktree_coordination.md` | 760 | Worktree setup, zone ownership, merge strategy |
| `MECH-extended_thinking_triggers.md` | 609 | When to enable, token allocation, cost/benefit |
| `MECH-prompt_engineering_patterns.md` | 950 | Seven rules, clarity first, XML scaffolds |

### 02-PRACTICE (Implementation Patterns)

| Document | Words | Scope |
|----------|-------|-------|
| `PRAC-parallel_claude_orchestration.md` | 791 | Multi-instance patterns, worktrees, teleport |
| `PRAC-ralph_pattern_execution.md` | 905 | Fresh context loops, static prompts, one-shot tasks |
| `PRAC-semantic_compression_workflow.md` | 753 | SN methodology, sutra crafting, quality verification |
| `PRAC-oracle_to_executor_handoff.md` | 568 | Handoff template, timing, verification |
| `PRAC-ledger_management_patterns.md` | 499 | Zone-specific CSVs, consolidation |
| `PRAC-multi_account_coordination.md` | 595 | Isolation patterns, rate limit handling |
| `PRAC-cowork_desktop_integration.md` | 721 | Folder permissions, skills, connectors |

---

## Key Insights Preserved

### From Claude Code Research (Stream A)
- Context degradation before capacity (75% rule)
- Plan Mode as external working memory
- Ralph fresh context principle
- Skills progressive disclosure
- Task dependency enforcement
- Hooks as deterministic control points
- Worktree isolation for parallel agents
- Teleport session mobility

### From Ecosystems Research (Stream B)
- OpenAI API-first vs Claude CLI-first paradigms
- Gemini 1M context advantage for detection
- Dual-agent pattern: Gemini detects → Claude executes
- Assistants API deprecation (August 2026)
- Responses API as recommended entry point
- NotebookLM audio/video synthesis
- Platform competitive positioning

### From Cross-Cutting Research (Stream C)
- Context tax (7 MCP servers = 50% of 200K context)
- Tool Search/Launchpad for progressive disclosure
- Git worktree isolation as gold standard
- Zone-specific ledgers eliminate conflicts
- Oracle-Executor handoff documents survive session death
- Three agent components (perception, decision, action)
- Supervisor bottleneck in centralized patterns

---

## Usage Patterns

### For Claude Code Configuration
```markdown
# Reference in CLAUDE.md
@07-SIGMA7/00-SYNTHESIS/SYNTHESIS-claude_code_architecture.md
```

### For Specific Mechanisms
```markdown
# Load skill architecture when building skills
@07-SIGMA7/01-MECHANICS/MECH-skill_system_architecture.md
```

### For Workflow Execution
```markdown
# Reference handoff pattern before session end
@07-SIGMA7/02-PRACTICE/PRAC-oracle_to_executor_handoff.md
```

---

## Cross-References

- `[[01-CANON]]` — Constitutional knowledge (what to believe)
- `[[00-ORCHESTRATION]]` — Directives and execution logs
- `[[CLAUDE.md]]` — Project instructions referencing σ₇

---

## Metrics

| Metric | Value |
|--------|-------|
| Source corpus | 223,007 words |
| Output corpus | 22,728 words |
| **Compression** | **90%** |
| Documents | 22 |
| Streams executed | 3 (parallel) |

---

*"Operational knowledge metabolized from the earliest ethnography of human-AI joint cognition."*
