# Siege Index — CC28

**Date**: 2026-02-24
**Session**: CC28 Ascertescence²

## Siege Prompts

| Prompt | Agent | Tasks |
|--------|-------|-------|
| `PROMPT-ADJUDICATOR-SIEGE-CC28.md` | Codex Desktop App | Config migration, persist brief, integration-first gate |
| `PROMPT-CLAUDE-SIEGE-CC28.md` | Fresh Claude Code | Atom clustering, intention pruning, portal draft |

## Siege Results

### Claude Code Siege
| Commit | Deliverable | Summary |
|--------|-------------|---------|
| `5a3a97e4` | `agents/commander/outbox/RESULT-CLAUDE-CC28-ATOM_TRIAGE.md` | 14,025 atoms → 150 clusters → 606 sovereign_review. Cross-referenced against ARCH-INTENTION_COMPASS.md. |
| `6ca5a74a` | `agents/commander/outbox/RESULT-CLAUDE-CC28-INTENTION_PRUNING_DRAFT.md` | 97 intentions → 35 ACTIVE, 62 removable (DONE/STALE/MERGED). Sovereign approval required. |
| `d7ffb96f` | `orchestration/00-ORCHESTRATION/PORTAL-CHAT-AGENTS.md` | Chat agent portal for Diviner relay. Auto-generation stub TBD. |

### Codex Siege
| Commit | Deliverable | Summary |
|--------|-------------|---------|
| `bd693791` | `orchestration/00-ORCHESTRATION/scripts/config_migrate.sh` + 103 scripts migrated | Strangler-fig phase 1: all scripts now source config.sh/config.py. Markdown files deferred. |
| `d2485514` | `session_state_brief.py` (modified) | Brief output now appends structured JSONL to `agents/commander/memory/journal/YYYY-MM-DD.jsonl` |
| `57755271` | `session_state_brief.py` (modified) | Integration-First Gate: reports atoms promoted + files migrated + pass/warn status per session |

## Siege Prompt Archive

Prompts are in `engine/02-ENGINE/ascertescence/prompts/`:
- `PROMPT-ADJUDICATOR-SIEGE-CC28.md`
- `PROMPT-CLAUDE-SIEGE-CC28.md`
