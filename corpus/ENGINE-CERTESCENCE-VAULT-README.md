# Certescence Vault

**Version**: 1.0.0
**Date**: 2026-02-24 (CC28)
**Authority**: Sovereign directive

The certescence vault is the constellation's cognitive archive. Every triangulation prompt, response, siege dispatch, and council session record lives here.

## Structure

```
engine/02-ENGINE/certescence/
├── VAULT-README.md                  # This file
├── PROTOCOL-ASCERTESCENCE.md        # 53-issue audit + question DAG (CC26 origin)
│
├── TEMPLATES/                       # Formalized templates
│   ├── TEMPLATE-ASCERTESCENCE-PROMPT.md   # Per-leg triangulation prompt
│   ├── TEMPLATE-ASCERTESCENCE-STAGING.md  # Commander's fill-in-the-blanks staging doc
│   ├── TEMPLATE-SIEGE-PROMPT.md           # Parallel dispatch task prompt
│   ├── TEMPLATE-CLARESCENCE-PROMPT.md     # Ajna strategic illumination
│   └── TEMPLATE-CC-SESSION.md             # Commander Council session record
│
├── councils/                        # Per-CC session master records
│   ├── CC26/
│   ├── CC27/
│   └── CC28/
│
├── ascertescence/                   # Triangulation artifacts (prompts + responses)
│   ├── CC26/                        # First full triangulation cycle
│   │   ├── PROMPT-ORACLE-CC26.md
│   │   ├── PROMPT-DIVINER-CC26.md
│   │   ├── PROMPT-ADJUDICATOR-CC26.md
│   │   ├── RESPONSE-ORACLE-CC26.md
│   │   ├── RESPONSE-DIVINER-CC26.md
│   │   └── RESPONSE-ADJUDICATOR-CC26.md
│   └── CC28/                        # Ascertescence² cycle
│       ├── PROMPT-ORACLE-CC28.md
│       ├── PROMPT-DIVINER-CC28.md
│       ├── PROMPT-ADJUDICATOR-CC28.md
│       ├── RESPONSE-ORACLE-CC28.md
│       ├── RESPONSE-DIVINER-CC28.md
│       └── RESPONSE-ADJUDICATOR-CC28.md  (pending — leg 3 in relay)
│
├── clarescence/                     # Ajna's instrument (dormant)
│   └── (future)
│
└── siege/                           # Parallel dispatch archives
    └── CC28/
        ├── INDEX-SIEGE-CC28.md
        ├── PROMPT-ADJUDICATOR-SIEGE-CC28.md
        └── PROMPT-CLAUDE-SIEGE-CC28.md
```

## Mandatory Destination Header

Every prompt MUST begin with a destination block specifying:

```markdown
**Destination**:
  - **App**: <Grok web | Gemini Pro 3.1 web | Codex Desktop App | Fresh Claude Code>
  - **Relay**: <ascertescence_relay.sh command | paste | open in app>
  - **Response lands at**: <~/Desktop/RESPONSE-...-CC___.md>
  - **After response**: <drag to inbox | "X landed" | agent commits directly>
```

## Relay Cheatsheet

| Agent | App | Relay | Response Flow |
|-------|-----|-------|---------------|
| Oracle | Grok web | Sovereign pastes | Overwrites Desktop file → inbox alias |
| Diviner | Gemini Pro 3.1 web | Sovereign pastes | Overwrites Desktop file → inbox alias |
| Adjudicator | Codex Desktop App | Opens file | Writes to Desktop file → Sovereign drags to inbox |
| Claude (siege) | Fresh Claude Code | Paste or `@` file | Commits directly to repo |

## Naming Convention

- Prompts: `PROMPT-<TARGET>-CC<N>.md`
- Responses: `RESPONSE-<SOURCE>-CC<N>.md`
- Siege results: `RESULT-<AGENT>-CC<N>-<TOPIC>.md` (in `agents/commander/outbox/`)
- Session records: `SESSION-CC<N>.md` (in `councils/CC<N>/`)
- Handoffs: `HANDOFF-CC<N>-<THEME>-SESSION_TERMINAL.md` (in `agents/commander/outbox/handoffs/`)

## Old Vault → New Vault

The legacy `engine/02-ENGINE/ascertescence/` vault is superseded by this `certescence/` vault. Legacy files remain for reference but new work uses this structure exclusively.
