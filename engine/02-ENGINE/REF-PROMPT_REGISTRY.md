---
id: prompt-registry
kind: registry
scope: repo
target: repo
owner: Vanguard
---

# Prompt Registry

Auto-generated index of all PROMPT-* files in engine/prompts/.

Last updated: 2026-01-18

## ChatGPT Prompts

| Filename | ID | Kind | Scope | Target | Triggers |
|----------|-----|------|-------|--------|----------|
| PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md | deviser-project-instructions | project_instructions | project | chatgpt | Blitzkrieg, Directive, Return packet, Execution log |
| PROMPT-CHATGPT-GLOBAL_MEMORY_REGISTRATION.md | chatgpt-global-memory-registration | memory_registration | global | chatgpt | - |
| PROMPT-CHATGPT-PROJECT_MEMORY_ANCHOR-SYNCRESCENDENCE.md | chatgpt-project-memory-anchor-syncrescendence | memory_registration | project | chatgpt | - |

## Canonical Prompts (engine/prompts/canonical/)

| Filename | ID | Kind | Scope | Target |
|----------|-----|------|-------|--------|
| PROMPT-CHATGPT-canonical.md | - | system_prompt | project | chatgpt |
| PROMPT-CLAUDE-canonical.md | - | system_prompt | project | claude |
| PROMPT-GEMINI-canonical.md | - | system_prompt | project | gemini |
| PROMPT-GROK-canonical.md | - | system_prompt | project | grok |
| PROMPT-IMEP-CHATGPT-AUDITOR.md | - | station_prompt (fmr. IMEP) | project | chatgpt |
| PROMPT-IMEP-CHATGPT-DEVISER.md | - | station_prompt (fmr. IMEP) | project | chatgpt |
| PROMPT-IMEP-CLAUDE-AUDITOR.md | - | station_prompt (fmr. IMEP) | project | claude |
| PROMPT-IMEP-CLAUDE-ENGINEER.md | - | station_prompt (fmr. IMEP) | project | claude |
| PROMPT-IMEP-GEMINI-ORACLE.md | - | station_prompt (fmr. IMEP) | project | gemini |

## Unified Prompts (engine/prompts/unified/)

| Filename | Purpose |
|----------|---------|
| ChatGPT-unified-prompt.md | Full unified prompt for ChatGPT |
| Claude-unified-prompt.md | Full unified prompt for Claude |
| Gemini-unified-prompt.md | Full unified prompt for Gemini |
| Grok-unified-prompt.md | Full unified prompt for Grok |
| *-gemknowledge-base.md | Knowledge base supplements |

## Notes

- Canonical prompts in `canonical/` may lack YAML frontmatter (legacy)
- Run `ops_lint.sh` to verify frontmatter compliance
- Update this registry when adding new prompts
