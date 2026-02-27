# Certescence Vault — Architecture

**Version**: 1.0.0
**Date**: 2026-02-24 (CC28)
**Authority**: Sovereign directive

## Three Vaults

The constellation's cognitive operations produce three categories of artifact, each with its own vault:

| Vault | Instrument | Agent | Purpose |
|-------|-----------|-------|---------|
| `ascertescence/` | Ascertescence | Commander | Triangulation: question generation → Oracle → Diviner → Adjudicator relay |
| `clarescence/` | Clarescence | Ajna | Holistic/meta/macro strategic illumination (currently dormant) |
| `siege/` | Siege | Any | Parallel dispatch: fan-out tasks to concurrent agents with structured results |

## Directory Structure

```
engine/02-ENGINE/certescence/
├── VAULT-README.md          # This file
├── TEMPLATES/               # Formalized templates (one per artifact type)
│   ├── TEMPLATE-ASCERTESCENCE-PROMPT.md
│   ├── TEMPLATE-SIEGE-PROMPT.md
│   └── TEMPLATE-CLARESCENCE-PROMPT.md
├── ascertescence/
│   ├── CC26/                # Per-cycle directories
│   │   ├── PROMPT-ORACLE-CC26.md
│   │   ├── PROMPT-DIVINER-CC26.md
│   │   ├── PROMPT-ADJUDICATOR-CC26.md
│   │   ├── RESPONSE-ORACLE-CC26.md
│   │   ├── RESPONSE-DIVINER-CC26.md
│   │   └── RESPONSE-ADJUDICATOR-CC26.md
│   └── CC28/
│       ├── PROMPT-ORACLE-CC28.md
│       ├── PROMPT-DIVINER-CC28.md
│       ├── PROMPT-ADJUDICATOR-CC28.md
│       ├── RESPONSE-ORACLE-CC28.md
│       ├── RESPONSE-DIVINER-CC28.md
│       └── RESPONSE-ADJUDICATOR-CC28.md  (pending)
├── clarescence/
│   └── (future — Ajna dormant)
└── siege/
    └── CC28/
        ├── INDEX-SIEGE-CC28.md
        ├── PROMPT-ADJUDICATOR-SIEGE-CC28.md
        ├── PROMPT-CLAUDE-SIEGE-CC28.md
        ├── RESULT-CLAUDE-CC28-ATOM_TRIAGE.md       (symlink or copy from outbox)
        ├── RESULT-CLAUDE-CC28-INTENTION_PRUNING.md  (symlink or copy from outbox)
        └── RESULT-CODEX-CC28-CONFIG_MIGRATION.md    (commit reference)
```

## Naming Convention

### Prompts
`PROMPT-<TARGET_AGENT>-<OPERATION>-CC<N>.md`
- Target agent: ORACLE, DIVINER, ADJUDICATOR, CLAUDE, COMMANDER
- Operation: ascertescence leg implied by agent; siege explicit

### Responses
`RESPONSE-<SOURCE_AGENT>-<OPERATION>-CC<N>.md`
- Source agent: who produced it

### Results (siege)
`RESULT-<AGENT>-CC<N>-<TOPIC>.md`

## Destination Header (MANDATORY on all prompts)

Every prompt file MUST begin with a destination block:

```markdown
# <TITLE>

**Destination**: <where the Sovereign relays this>
  - **App**: <Grok web | Gemini Pro 3.1 web | Codex Desktop App | Fresh Claude Code session>
  - **Relay**: <paste full prompt | open file in app | ascertescence_relay.sh command>
  - **Response lands at**: <Desktop filename for overwrite | direct commit>
  - **After response**: <drag to inbox alias | Sovereign says "X landed" | agent commits directly>
```

## Relay Cheatsheet

| Agent | App | Relay Method | Response Flow |
|-------|-----|-------------|---------------|
| Oracle (Grok) | Grok web chat | Sovereign pastes prompt | Sovereign overwrites Desktop file → drags to inbox alias |
| Diviner (Gemini) | Gemini Pro 3.1 web | Sovereign pastes prompt | Sovereign overwrites Desktop file → drags to inbox alias |
| Adjudicator (Codex) | Codex Desktop App | Open file in app | Codex writes directly to Desktop file → Sovereign drags to inbox |
| Claude (siege) | Fresh Claude Code session | Paste siege prompt or `@` file | Claude commits directly to repo |
