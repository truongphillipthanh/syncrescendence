# HANDOFF — Commander Council 65 (Tool Stack Lane)

**Date**: 2026-03-01
**Agent**: Commander (Claude Opus 4.6)
**Session**: CC65 (tool stack workstream — parallel to CRUSH workstream)
**Git HEAD**: `ad87ebbd`
**Trigger**: Manual (Sovereign directive — tool stack decisions locked)

---

## What Was Accomplished

### 1. Oracle Intelligence — 4 DISPATCHES, ALL INGESTED

Four Oracle dispatches in a single Grok thread (stateful follow-ups):

| # | Topic | Key Finding |
|---|-------|-------------|
| 1 | Full Strategy Stress Test (7 questions) | 87% aligned. Ontology MVP = Postgres+pg_vector. Cut Perplexity. $330 total-spend framing. |
| 2 | Subscription Triage (5 candidates) | xAI ONBOARD, Perplexity CUT, Cursor/Windsurf DEFER, Manus DEPLOY |
| 3 | OpenClaw Architecture (5 questions) | Dispatch-FROM dominant. Sonnet only viable orchestrator. Token overhead 1.8-3.2x. Minimal viable config. |
| 4 | Commander Capabilities (6 actions) | 4/6 automatable via Playwright MCP + APIs. Manus has REST API. |

Commander overrode Oracle on: Account 3 (conditional not committed), Mac mini (revive not kill), 30-day sprint (unrealistic for single Sovereign).

### 2. Tool Stack FINAL — LOCKED

`engine/CC65-TOOL-STACK-FINAL.md` — THE authority document superseding CC62/CC63.

**The Pedigree Architecture** (confirmed as original design):
- Ajna dispatches FROM OpenClaw (Sonnet/Haiku) downward to constellation
- C-suite labels are cognitive function type signatures, not org chart
- Ajna and Psyche are latent intent — CRUSH reveals their task profiles
- Fortress dispatch protocol: compress on send, expand on receive

**Subscription Stack (March 2026)**:
- Committed: $196.50/mo (was $210, minus Perplexity $20, plus VPS $5 + domain $1.50)
- Credits: +$160/mo (xAI $150 + GCP $10)
- Contingent: Account 3 ($20) only if Max rate limit test fails
- Deferred: Cursor, Windsurf, ElevenLabs

### 3. OpenClaw — ALIVE, WIRED, BUT CONFIG CORRUPTED

**Discovery**: OpenClaw was already running. Gateway LaunchAgent active, Ajna on Kimi K2.5, Slack/Discord wired, MCP adapter with Obsidian.

**Fortress dispatch validated**: Commander → Ajna (Kimi) produced a SITREP. Protocol works.

**Sonnet swap FAILED**: Config said Sonnet, Kimi kept loading. Agent-level models.json overrides global config. Doctor migrations make it worse.

**Sovereign directive**: Clean rebuild. Nuke ~/.openclaw/, reinstall, reconfigure from neocorpus knowledge.

### 4. Infrastructure Wired
- OpenClaw updated to 2026.2.26
- Playwright MCP installed in Claude Code
- Fresh Anthropic setup-token obtained and saved to memory
- All channel tokens (Slack, Discord, NVIDIA, Google) saved to memory
- Config backups saved to repo (`agents/commander/outbox/openclaw-*-backup-cc65.json`)

### 5. Memory Updated (5 files)
- `tool-stack-architecture.md` — CC65 FINAL
- `account-consolidation.md` — CC65 budget
- `openclaw-operations.md` — NEW: OpenClaw operations reference
- `infrastructure.md` — Anthropic token, channel tokens, rebuild instructions
- `MEMORY.md` — openclaw-operations.md reference

### Commits (tool stack lane)
- `163c21a9` — feat: Oracle follow-up — subscription triage
- `26af2d07` — feat: Oracle follow-up — OpenClaw architecture + inbox filings
- `3ce4508d` — feat: CC65 tool stack FINAL
- `f1b0ab28` — feat: Oracle follow-up — end-to-end autonomous execution audit
- `ad87ebbd` — chore: backup OpenClaw config before clean rebuild

---

## What Remains

### TIER 0 — OpenClaw Clean Rebuild (NEXT SESSION, FIRST THING)

**Before rebuilding, MINE the neocorpus:**

Read these 20 entries in `neocorpus/openclaw/` — they contain crystallized knowledge from 46+ source files:
- `openclaw-setup-and-operations.md` — setup procedures, first-week playbook
- `openclaw-model-configuration.md` — model routing, provider config, cost doctrine
- `syncrescendence-openclaw-infrastructure.md` — OUR specific constellation config
- `openclaw-memory-architecture.md` — memory system (13 files, 263 chunks currently)
- `openclaw-multi-agent-fleet-operations.md` — fleet patterns, dispatch
- `openclaw-security-hardening.md` — security baseline
- `openclaw-skills-platform-economics.md` — skills registry (44 eligible)
- All others for completeness

**Then rebuild:**
1. `npm uninstall -g openclaw && rm -rf ~/.openclaw/`
2. `npm install -g openclaw@latest`
3. `openclaw setup` (fresh wizard)
4. Configure from neocorpus knowledge:
   - Model: `anthropic/claude-sonnet-4-5` as primary FROM THE START
   - Auth: fresh token from memory `infrastructure.md`
   - Workspace: `/Users/system/syncrescendence`
   - Channels: Slack + Discord tokens from memory `infrastructure.md`
   - Memory: enable, source from repo
   - Skills: minimal (agent-dispatch, team-orchestration only)
5. Test: Ajna dispatch, confirm Sonnet, confirm concurrent with Claude Code

### TIER 1 — Sovereign Manual Actions
| # | Action | Status |
|---|--------|--------|
| 1 | Cancel Perplexity Pro | PENDING |
| 2 | Enroll xAI data sharing | PENDING |
| 3 | Register syncrescendence.com | PENDING |
| 4 | Claim GCP credits | PENDING |
| 5 | Manus API key format | PENDING — sk- key rejected, needs JWT? Check docs |

### TIER 2 — Post-Rebuild
| Task | Depends On |
|------|-----------|
| Rate limit test (concurrent Ajna + Commander) | OpenClaw rebuild |
| Account 3 decision | Rate limit test |
| Mac mini revival | OpenClaw stable on MBA first |
| Kimi daemon (OpenCode on mini) | Mini revival |
| Manus VPS deployment | Correct API auth |

---

## Key Decisions Made

1. **Pedigree confirmed.** Ajna→Commander is the original design. Three sessions of alternatives exhausted; all worse.
2. **Fortress protocol scales by model tier.** Sonnet: minimal. Haiku: rigid template. Kimi: full fortress.
3. **OpenClaw for free-token models primarily.** Claude stays on native harnesses where tokens count. OpenClaw orchestrates but doesn't grind tool loops on subscription auth.
4. **Haiku via OpenClaw (Pro subscription) = full Anthropic roster per dispatch.** Model selected per-task, not per-agent. This is the unlock that makes Pro Account 3 worth considering — but ONLY if Max sharing fails.
5. **Clean rebuild over incremental repair.** Seared lesson from this session.

## Sovereign Intent

Stop circling the tool stack. The architecture is confirmed. Execute the rebuild, execute the sprint, let CRUSH reveal what the constellation actually needs.

## WHAT THE NEXT SESSION MUST KNOW

1. **Mine neocorpus/openclaw/ FIRST.** 20 entries. Read them. The rebuild should be informed by crystallized knowledge, not by repeating old mistakes.
2. **The config is corrupted.** Don't try to fix it. Nuke and rebuild. Agent-level models.json silently overrides global config — this is the specific bug.
3. **Fresh Anthropic token in memory `infrastructure.md`.** All channel tokens there too.
4. **Kimi-with-fortress WORKS.** If Sonnet swap fails again, Kimi is the fallback. The protocol is validated.
5. **Tool stack is CLOSED.** `engine/CC65-TOOL-STACK-FINAL.md` is authority. Don't re-open. April retool at month end.
6. **Manus API: `api.manus.im/v1/tasks`**, key is `sk-G7...Jh03k` but rejects as "malformed token." Needs JWT format or different auth header. Check Manus documentation.

## Key Files

| File | Purpose |
|------|---------|
| `engine/CC65-TOOL-STACK-FINAL.md` | THE authority — architecture, subs, sprint |
| `neocorpus/openclaw/` (20 entries) | MINE BEFORE REBUILDING |
| `agents/commander/outbox/openclaw-*-backup-cc65.json` | Config backups (auth is local-only) |
| `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-*.md` | 3 Oracle responses |
| Memory: `infrastructure.md` | All tokens and keys |
| Memory: `openclaw-operations.md` | OpenClaw commands reference |
| Memory: `tool-stack-architecture.md` | CC65 FINAL architecture |

## Kaizen

- Seared lessons: "OpenClaw doctor migrations corrupt state — clean rebuild beats incremental repair" + "agent-level models.json overrides global config silently" + "check before assuming anesthesia — OpenClaw was alive"
- Config drift: CLAUDE.md updated externally (Sovereign added neocorpus/ to Flat Principle)
- Memory hygiene: 5 files updated/created, all current

## Session Metrics
- Commits: 5 (tool stack lane)
- Oracle dispatches: 4 (same Grok thread, stateful)
- Files created: 1 strategy doc, 3 config backups, 3 Oracle responses filed, 4 Oracle prompts
- Memory files: 5 updated/created
- OpenClaw: Sonnet swap FAILED, clean rebuild queued
- Dirty files at handoff: 0
