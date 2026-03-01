# HANDOFF — Commander Council 70b (Tool Stack Lane)

**Date**: 2026-03-01
**Agent**: Commander (Claude Opus 4.6)
**Session**: CC70b (tool stack lane — continuation of CC66b)
**Git HEAD**: `c78b25a8` (pre-session) → `ef05fa46` (session commit)
**Trigger**: Manual — Sovereign directive

## What Was Accomplished

### 1. Oracle Prompt v2 — Empirical Peekaboo Test Results

Rewrote `engine/PROMPT-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md` with empirical findings from live Peekaboo testing:
- Peekaboo Screen Recording permission GRANTED (one-time Sovereign action complete)
- Peekaboo captures screenshots and clicks coordinates — but element detection FAILS on web content
- `--profile human` does NOT exist in 3.0-beta3 (documentation was wrong)
- `--query` flag does NOT exist — positional argument only
- Coordinate clicking works but is pixel-fragile — one layout shift breaks it

**Result**: Peekaboo demoted from PRIMARY to LAST RESORT for web automation. New 5-tier hierarchy established:
1. API/CLI (best)
2. OpenClaw browser MCP (agent-native, DOM-aware)
3. Claude Computer Use / Desktop MCP
4. Playwright MCP (DOM-aware, fresh browser)
5. Peekaboo (macOS native UI only)

Committed: `ef05fa46`. Pushed. Desktop copy created for Sovereign relay.

### 2. Oracle Response Received and Triangulated

Sovereign relayed Oracle response: `RESPONSE-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md` (now filed in `-INBOX/commander/00-INBOX0/`).

**Full triangulation conducted** against ALL 33 Oracle documents (15 prompts, 18 responses) spanning CC42-CC66b. Key findings:

#### What rings true (cross-validated):
- Playwright `launchPersistentContext(userDataDir)` for session persistence — technically correct
- Ajna skill recommendations (playwright-mcp, github, automation-workflows, agent-dispatch) — consistent with CC63 OPENCLAW-ARCHITECTURE response
- Manus API auth format: `API_KEY:` header, not `Bearer sk-` — specific, testable claim
- Start with Playwright MCP as primary bridge — consistent with Commander-stays-native architecture

#### What smells fabricated:
- "70%+ of active OpenClaw setups" use browser tools — no source, round number
- "VirusTotal flags ~60% false positives" — unverifiable statistic
- "72.5% OSWorld score" — plausible but unverified
- ClawHub "7000+" skills — CC63 said "5,400+", prompt said "700+". Inconsistent across responses.
- OpenClaw "core `browser` tool (CDP)" — neocorpus doesn't mention this; `browser` is in our DENIED tools list

#### What's MISSING from Oracle response:
- **ZERO mention of memory architecture** — how browser automation results persist in OpenClaw's memory
- **No config architecture guidance** — how generated configs propagate across agents/machines
- **No workspace isolation awareness** — our empirical finding that workspace ≠ repo root

### 3. Ascertescence Gap Identified — The Unsent Oracle Dispatch

**Critical finding from full ascertescence review**: Across 33 Oracle documents spanning CC42-CC66b, there has NEVER been an Oracle dispatch asking:

> "What is the config architecture for a constellation of agents running different harnesses on different machines, all working from one monorepo, where each agent needs a different subset of the shared knowledge base, and the config must be generated (not hand-maintained) to prevent drift?"

This is the most important architectural question the constellation has never asked. The `make configs` pipeline (`AGENTS.md` + `*-EXT.md` → `CLAUDE.md`, `GEMINI.md`) was:
- **Built in CC55** (restored, not designed)
- **Never interrogated by Oracle**
- **Never stress-tested** against actual multi-machine, multi-harness operation
- **Incrementally discovered through crashes** (.zshrc illusion, workspace conflict, phantom paths)

The Canon Remediation Pass 8 (CC42) contains the theoretical foundation: **Five Views of One Truth** (Scripture → Config → Graph → Ledger → Compiled) with `make configs` as the Config View. But this was designed for canon files, not agent config files.

### 4. Memory Seared (7 locations confirmed)

Browser gap architecture seared across:
1. `memory/browser-gap-architecture.md` — full architecture doc
2. `memory/MEMORY.md` — section + topic file reference
3. `memory/critical-lessons.md` — empirical test findings + browser gap principles
4. `memory/openclaw-operations.md` — browser gap toolkit section
5. `memory/tool-stack-architecture.md` — browser gap section (updated: Peekaboo demoted)
6. `~/.openclaw/workspace/AGENTS.md` — Ajna's Peekaboo + three bridges capabilities
7. `engine/PROMPT-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md` — v2 with empirical data

### 5. Peekaboo Permissions Granted

Screen Recording permission for Peekaboo is now ACTIVE on MBA. Accessibility permission status unclear (wasn't tested). Peekaboo can:
- Capture screenshots (`peekaboo image --app "Google Chrome"`)
- Switch apps (`peekaboo app switch --to "Google Chrome"`)
- Click by coordinates (`peekaboo click --coords X,Y --app "..."`)
- Open URLs (`peekaboo open "https://..."`)
- CANNOT detect web page elements (times out or "element not found")

### 6. Stray Test Screenshots Cleaned

Three `Google-Chrome_*.png` screenshots from Peekaboo testing removed from repo root.

## What Remains

### Immediate (Next Session)

1. **Write the config architecture Oracle dispatch** — the unsent prompt about multi-machine, monorepo, multiplatform agent harness config. This is the biggest gap in the ascertescence. Reference the Five Views architecture from Canon Pass 8, the `make configs` pipeline, the workspace isolation finding, and the OpenClaw SOUL.md ordering (U-shaped attention).

2. **Test Manus API auth** — Oracle claims `API_KEY:` header not `Bearer sk-`. One curl command verifies: `curl -H "API_KEY: <key>" https://api.manus.ai/v1/tasks`. If true, closes browser gap item #7 with zero browser automation.

3. **Test Playwright MCP persistent context** — verify `launchPersistentContext(userDataDir)` works from Commander's Claude Code MCP connection. If yes, attempt Perplexity Pro cancellation via Playwright selectors instead of Peekaboo coordinates.

4. **Install Ajna skills** — Oracle recommends: `clawhub install playwright-mcp github automation-workflows`. Test one at a time. Verify VirusTotal on each before install.

### Strategic (Unresolved)

5. **The config architecture question** — how does AGENTS.md + EXT files scale to: Commander (Claude Code, MBA), Ajna (OpenClaw, MBA), Psyche (OpenClaw, mini), Adjudicator (Codex CLI, mini), Cartographer (Gemini CLI, mini)? Each needs different platform-specific config generated from shared source.

6. **Memory integration for browser automation** — when Ajna rotates a token via browser, where does the new token go? How does it propagate to OpenClaw config? How does Commander learn about it?

7. **Peekaboo Accessibility permission** — not tested. May be needed for some native macOS interactions. Sovereign should check System Settings > Privacy & Security > Accessibility for peekaboo/Terminal.

## Key Decisions Made

- **Peekaboo demoted**: From PRIMARY browser gap bridge to last resort (macOS native UI only). Empirically proven fragile for web content.
- **DOM-aware tools elevated**: Playwright MCP, OpenClaw browser MCP, Claude Computer Use are the real browser gap bridges.
- **Config architecture Oracle dispatch identified**: The biggest gap in the entire ascertescence. 33 documents and nobody asked the foundational question.

## Sovereign Intent

The Sovereign wants autonomous execution — "open the browser, try to log in, send a popup and then I can authenticate." The pattern is: agent navigates to target, hits auth gate, Sovereign authenticates once, agent completes the action. The Sovereign recognized that OpenClaw has its own browser MCP and Claude has the desktop app as MCP — these structured approaches are superior to Peekaboo's pixel-hunting.

The Sovereign also directed comprehensive triangulation of the Oracle response against the full ascertescence, which surfaced the config architecture blind spot.

## WHAT THE NEXT SESSION MUST KNOW

1. **Peekaboo Screen Recording is GRANTED.** Don't ask again. But Peekaboo is bad at web automation — use Playwright or OpenClaw browser MCP instead.
2. **The Oracle response is in `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md`.** It's been triangulated. Actionable items: Playwright persistent context, Manus API_KEY header, Ajna skill installation, Docker optional for personal use.
3. **Oracle fabrication patterns are present** in this response (unverifiable statistics, inconsistent ClawHub skill counts). Cross-verify specific claims before acting on them.
4. **The config architecture Oracle dispatch is THE next strategic prompt.** The `make configs` pipeline has never been architecturally interrogated. This is the biggest blind spot across 70 sessions.
5. **critical-lessons.md was updated by Sovereign** (added "The Fabricated Config Schema Pattern CC65-CC69b"). This is now seared — never invent JSON/YAML config structures in neocorpus entries.
6. **Three stray PNG screenshots were cleaned** from repo root. If any `*.png` appear in git status, they're test artifacts — remove them.

## Key Files

| File | Purpose |
|------|---------|
| `engine/PROMPT-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md` | Oracle prompt v2 (empirical findings, Peekaboo demoted) |
| `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md` | Oracle response (triangulated, filed) |
| `memory/browser-gap-architecture.md` | Definitive browser gap architecture (auto-memory) |
| `memory/critical-lessons.md` | Updated by Sovereign — fabricated config schema pattern added |
| `memory/tool-stack-architecture.md` | Updated — Peekaboo demoted, 5-tier hierarchy |
| `~/.openclaw/workspace/AGENTS.md` | Ajna's capabilities (Peekaboo + browser gap section) |

## Kaizen

- Seared lessons extracted: yes — Peekaboo empirical findings (already in critical-lessons.md + tool-stack-architecture.md). Sovereign added fabricated config schema pattern.
- Config drift: clean — `make configs` not needed (no AGENTS.md changes this session)
- Memory hygiene: 7 locations verified seared. Peekaboo demotion reflected in tool-stack-architecture.md and critical-lessons.md.

## Session Metrics

- Commits: 1 (`ef05fa46` — Oracle prompt v2)
- Files changed: 1 (engine/PROMPT-ORACLE-AUTONOMOUS-EXECUTION-CC66b.md)
- Dirty files at handoff: 0
