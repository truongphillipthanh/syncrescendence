# Triangulation Protocol
Type: concept
First seen: Council 22 (2026-02-23)
Status: active

## What it is
The cognitive architecture of the constellation. A multi-agent reasoning cycle: Commander (GROUND) -> Oracle/Grok (THESIS) -> Sovereign relay -> Commander (SYNTHESIS) -> Diviner/Gemini (NOVEL SYNTHESIS) -> Sovereign relay -> Commander (COMPILE) -> Adjudicator/Codex (ENGINEER). Each leg produces documented prompts and responses.

## Relationships
- defined_in: AGENTS.md, CLAUDE.md, playbook-triangulation.md
- involves: Commander, Oracle (Grok), Diviner (Gemini), Adjudicator (Codex), Sovereign (relay)
- documentation_invariant: Every prompt -> engine/PROMPT-*, every response -> -INBOX/commander/00-INBOX0/RESPONSE-*
- first_full_cycle: DC-204 playbook (safe point 019f973e)

## Commander Council (CC) Lineage
Triangulation is now conducted under the CC session lineage (Sovereign↔Commander). CC26 is the current session. Prompts are named `PROMPT-COMMANDER-ASCERTESCENCE-CC{N}.md`; responses are `RESPONSE-{AGENT}-ASCERTESCENCE-CC{N}.md`.

**Relay mechanism**: `ascertescence_relay.sh` — sequential single-file relay (ONE file on Desktop at a time):
1. Commander creates prompt in `engine/02-ENGINE/`
2. `ascertescence_relay.sh CC# send oracle` → rsyncs to Desktop as `RESPONSE-ORACLE-ASCERTESCENCE-CC{N}.md`
3. Sovereign pastes to Oracle (Grok web), overwrites Desktop file with response, drags into Commander inbox alias (→ `-INBOX/commander/00-INBOX0/`)
4. Sovereign says "Oracle landed" → Commander reads, creates next prompt (`CC{N}-DIV.md`)
5. `ascertescence_relay.sh CC# send diviner` → rsyncs to Desktop as `RESPONSE-DIVINER-*`
6. Sovereign pastes prompt to Diviner (Gemini Pro 3.1 web), overwrites Desktop file with response, drags into Commander inbox alias. Do NOT use Gemini CLI (nerfed).
7. Sovereign says "Diviner landed" → Commander reads, creates Adjudicator prompt (`CC{N}-ADJ.md`)
8. `ascertescence_relay.sh CC# send adjudicator` → Adjudicator (Codex Desktop App, NOT Codex CLI) writes response directly, overwrites the file. Sovereign drops in Commander inbox. (Last leg.)

Index: `-INBOX/commander/00-INBOX0/INDEX-TRIANGULATION_RESPONSES.md`. Future: auto-compact into "ultra-enhanced wisdom".

## Current state
Operational. First full cycle completed for DC-204. The protocol is constitutional (Sovereign directive 2026-02-23). Triangulation weights: Oracle HIGH, Adjudicator HIGH, Cartographer LOW-MEDIUM. CC session lineage formalized at CC26 (2026-02-24).
