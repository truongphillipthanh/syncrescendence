# 05-SIGMA: Operational Knowledge Corpus

**Version**: 2.0.0
**Updated**: 2026-02-01
**Source**: Research corpus metabolization, audited for token rent

---

## Purpose

σ₇ (Sigma-7) contains operational knowledge for AI-amplified workflows—how to configure, orchestrate, and integrate Claude Code with the broader AI ecosystem. Distinct from 01-CANON (constitutional knowledge about what to believe).

**Epistemic status**: Operational (faster update cadence than CANON)

---

## Structure

```
05-SIGMA/
├── mechanics/             # Deep-dive mechanisms (5 docs)
├── practice/              # Implementation patterns (6 docs)
├── EXEMPLA-*              # Wisdom layer: aphorisms, proverbs, cautionary tales
├── REF-*                  # Research reference docs
└── README.md              # This file
```

---

## Document Index

### Mechanics (Implemented Patterns)

| Document | Scope |
|----------|-------|
| `MECH-context_compaction_strategies.md` | 75% rule, manual vs auto, focus instructions |
| `MECH-hooks_lifecycle_automation.md` | PreToolUse guards, PostToolUse polish, governance |
| `MECH-mcp_server_patterns.md` | Server config, context tax mitigation, governance |
| `MECH-skill_system_architecture.md` | Progressive disclosure, SKILL.md format, subagent pairing |
| `MECH-task_orchestration.md` | Dependency management, parallel spawning, persistence |

### Practice (Operational Patterns)

| Document | Scope |
|----------|-------|
| `PRAC-cowork_desktop_integration.md` | Folder permissions, skills, connectors |
| `PRAC-ledger_management_patterns.md` | Zone-specific CSVs, consolidation |
| `PRAC-multi_account_coordination.md` | Isolation patterns, rate limit handling |
| `PRAC-oracle_to_executor_handoff.md` | Handoff template, timing, verification |
| `PRAC-ralph_pattern_execution.md` | Fresh context loops, static prompts |
| `PRAC-semantic_compression_workflow.md` | SN methodology, sutra crafting, quality verification |

### Exempla (Wisdom Layer)

| Document | Scope |
|----------|-------|
| `EXEMPLA-APHORISMS.md` | 17 operational aphorisms |
| `EXEMPLA-PROVERBS.md` | 28 operational proverbs |
| `EXEMPLA-TALE-ajna2-lobotomy.md` | Cautionary tale: context wipe anti-pattern |

### Reference

| Document | Scope |
|----------|-------|
| `REF-CLAUDE_CODE_OPERATIONS_MANUAL.md` | Distilled ops checklist (pending compression) |

---

## Audit Log

**v2.0.0 (2026-02-01)**: Deep audit — 43 files → 16 files (63% reduction)
- Deleted 7 MEMORY-* files (30-day TTL violated)
- Deleted 5 SYNTHESIS-* files (redundant with STACK_TELEOLOGY + CLAUDE.md)
- Deleted 7 empty templates (EXEMPLA-TEMPLATE-*, EXEMPLA-CASE/EXAMPLE-TEMPLATE)
- Deleted CONVERGENCE-METRICS.md (historical snapshot, git preserves)
- Deleted MECH-extended_thinking_triggers.md (outdated, covered in CLAUDE.md)
- Deleted PRAC-agentic_mastery_framework.md (generic, not implemented)
- Deleted EXEMPLA-AJNA-ARCHAEOLOGY.md (archaeology → NotebookLM offload candidate)
- Deleted REF-CLAUDE_CODE_UNIFIED_COALESCENCE.md (60KB → NotebookLM offload candidate)
- Moved 5 unimplemented patterns to 04-SOURCES/research/ (worktrees, headless, subagent, parallel, prompt engineering)
- Removed empty synthesis/ directory

**NotebookLM offload candidates** (recoverable from git):
- REF-CLAUDE_CODE_UNIFIED_COALESCENCE.md (60KB research synthesis)
- MEMORY-AJNA-THREAD-EXTRACTION.md (19KB archaeology)
- MEMORY-CHATGPT-ASSESSMENT-EXTRACTION.md (15KB archaeology)
- EXEMPLA-AJNA-ARCHAEOLOGY.md (11KB narrative)

---

*"Every token earns its rent."*
