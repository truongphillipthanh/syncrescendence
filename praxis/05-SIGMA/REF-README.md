# praxis: Operational Knowledge Corpus

**Version**: 2.1.0
**Updated**: 2026-02-23
**Source**: Research corpus metabolization, audited for token rent

---

## Purpose

σ₇ (Sigma-7) contains operational knowledge for AI-amplified workflows—how to configure, orchestrate, and integrate Claude Code with the broader AI ecosystem. Distinct from canon (constitutional knowledge about what to believe).

**Epistemic status**: Operational (faster update cadence than CANON)

---

## Structure

```
praxis/05-SIGMA/
├── mechanics/             # Deep-dive mechanisms (12 docs)
├── practice/              # Implementation patterns (13 docs)
├── syntheses/             # Platform syntheses (8 docs)
├── EXEMPLA-*              # Wisdom layer: aphorisms, proverbs, cautionary tales (4 docs)
├── REF-*                  # Research reference docs (2 docs, including this file)
```

---

## Document Index

### Mechanics (12 docs)

| Document | Scope |
|----------|-------|
| `MECH-context_compaction_strategies.md` | 75% rule, manual vs auto, focus instructions |
| `MECH-extended_thinking_triggers.md` | Extended thinking activation patterns |
| `MECH-git_worktree_coordination.md` | Worktree creation, zone isolation, multi-agent patterns |
| `MECH-headless_mode_automation.md` | Headless CLI execution patterns |
| `MECH-hooks_lifecycle_automation.md` | PreToolUse guards, PostToolUse polish, governance |
| `MECH-mcp_server_patterns.md` | Server config, context tax mitigation, governance |
| `MECH-prompt_engineering_patterns.md` | Prompt design patterns and techniques |
| `MECH-skill_system_architecture.md` | Progressive disclosure, SKILL.md format, subagent pairing |
| `MECH-source_anneal_pipeline.md` | Source ingestion, dedup, enrichment pipeline (STALE — blueprint) |
| `MECH-subagent_delegation.md` | Subagent spawning and delegation patterns |
| `MECH-task_orchestration.md` | Dependency management, parallel spawning, persistence |
| `MECH-youtube_ingestion_pipeline.md` | YouTube transcript ingestion workflow |

### Practice (13 docs)

| Document | Scope |
|----------|-------|
| `PRAC-auteur_content_strategy.md` | Content creation strategy |
| `PRAC-blitzkrieg_worktree_isolation.md` | Rapid parallel worktree execution |
| `PRAC-cowork_desktop_integration.md` | Folder permissions, skills, connectors |
| `PRAC-ledger_management_patterns.md` | Zone-specific CSVs, consolidation |
| `PRAC-multi_account_coordination.md` | Isolation patterns, rate limit handling (STALE) |
| `PRAC-multi_methodology_framework.md` | Multi-methodology PM framework (STALE) |
| `PRAC-ontology_queries.md` | Obsidian Dataview queries for CANON (STALE) |
| `PRAC-operational_wisdom_compendium.md` | Compacted operational wisdom |
| `PRAC-oracle_to_executor_handoff.md` | Handoff template, timing, verification |
| `PRAC-parallel_claude_orchestration.md` | Multi-instance Claude orchestration |
| `PRAC-ralph_pattern_execution.md` | Fresh context loops, static prompts |
| `PRAC-semantic_compression_workflow.md` | SN methodology, sutra crafting, quality verification |
| `PRAC-subagent_delegation_guide.md` | Subagent delegation guide |

### Syntheses (8 docs)

| Document | Scope |
|----------|-------|
| `SYNTHESIS-agents_mcp_foundations.md` | Agent and MCP ecosystem foundations |
| `SYNTHESIS-claude_code_architecture.md` | Claude Code architectural analysis |
| `SYNTHESIS-codex-cli.md` | Codex CLI / OpenAI ecosystem (STALE) |
| `SYNTHESIS-cross_platform_patterns.md` | Cross-platform integration patterns |
| `SYNTHESIS-gemini-cli.md` | Gemini CLI / Google AI ecosystem (STALE) |
| `SYNTHESIS-openclaw-v2.md` | OpenClaw v2 synthesis |
| `SYNTHESIS-openclaw.md` | OpenClaw synthesis |
| `SYNTHESIS-platform_topology_jan2026.md` | Platform technical specs snapshot (STALE) |

### Exempla (Wisdom Layer)

| Document | Scope |
|----------|-------|
| `EXEMPLA-APHORISMS.md` | Operational aphorisms |
| `EXEMPLA-PROVERBS.md` | Operational proverbs |
| `EXEMPLA-README.md` | Exempla index |
| `EXEMPLA-TALE-ajna2-lobotomy.md` | Cautionary tale: context wipe anti-pattern |

### Reference

| Document | Scope |
|----------|-------|
| `REF-CLAUDE_CODE_OPERATIONS_MANUAL.md` | Distilled ops checklist (pending compression) |
| `REF-README.md` | This file |

---

## Audit Log

**v2.1.0 (2026-02-23)**: Staleness audit — updated file counts (12 mechanics, 13 practice, 8 syntheses, 4 exempla, 2 ref = 39 total). Added staleness banners to 7 files. Updated structure to reflect actual directory layout including syntheses/.

**v2.0.0 (2026-02-01)**: Deep audit — 43 files → 16 files (63% reduction)
- Deleted 7 MEMORY-* files (30-day TTL violated)
- Deleted 5 SYNTHESIS-* files (redundant with STACK_TELEOLOGY + CLAUDE.md)
- Deleted 7 empty templates (EXEMPLA-TEMPLATE-*, EXEMPLA-CASE/EXAMPLE-TEMPLATE)
- Deleted CONVERGENCE-METRICS.md (historical snapshot, git preserves)
- Deleted MECH-extended_thinking_triggers.md (outdated, covered in CLAUDE.md)
- Deleted PRAC-agentic_mastery_framework.md (generic, not implemented)
- Deleted EXEMPLA-AJNA-ARCHAEOLOGY.md (archaeology → NotebookLM offload candidate)
- Deleted REF-CLAUDE_CODE_UNIFIED_COALESCENCE.md (60KB → NotebookLM offload candidate)
- Moved 5 unimplemented patterns to sources/research/ (worktrees, headless, subagent, parallel, prompt engineering)
- Removed empty synthesis/ directory

**NotebookLM offload candidates** (recoverable from git):
- REF-CLAUDE_CODE_UNIFIED_COALESCENCE.md (60KB research synthesis)
- MEMORY-AJNA-THREAD-EXTRACTION.md (19KB archaeology)
- MEMORY-CHATGPT-ASSESSMENT-EXTRACTION.md (15KB archaeology)
- EXEMPLA-AJNA-ARCHAEOLOGY.md (11KB narrative)

---

*"Every token earns its rent."*
