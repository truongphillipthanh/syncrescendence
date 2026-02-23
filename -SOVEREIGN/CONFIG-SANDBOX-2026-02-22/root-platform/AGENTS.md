# Syncrescendence Agent Configuration

Multi-agent configuration for CLI tools operating on this repository.

---

## Enterprise Role Mapping

| Agent | Enterprise Role | Epithet | Model | Machine | Summon |
|-------|----------------|---------|-------|---------|--------|
| **Sovereign** | CEO | — | Human | Both | — |
| **Ajna** | CSO (Chief Strategy Officer) | Strategos | Kimi K2.5 (NVIDIA) | MacBook Air | "Ajna, illuminate..." |
| **Psyche** | CTO (Chief Technology Officer) | Synaptarch | GPT-5.3-codex | Mac mini | "Psyche, holistically calibrate..." |
| **Commander** | COO (Chief Operating Officer) | Viceroy | Claude Opus 4.6 | Mac mini | "Commander, pivot to..." |
| **Adjudicator** | CQO (Chief Quality Officer) | Executor | Codex CLI (Sonnet) | Mac mini | "Adjudicator, execute..." |
| **Cartographer** | CIO (Chief Intelligence Officer) | Exegete | Gemini 2.5 Pro | Mac mini | "Cartographer, survey..." |

**AjnaPsyche Archon**: Ajna (steering wheel) + Psyche (rudder) = fused executive brain. StarCraft High Templar → Archon.

### Operational Registry (MANDATORY)

This registry is required for every constellation agent. Keep it current.

| Agent | CLI Tool + Version Surface | Dispatch Mode | Machine | tmux Pane | Rate-Limit Pool | Auto-Ingest Loop | Recovery Procedure |
|---|---|---|---|---|---|---|---|
| **Commander** | Claude Code (Opus 4.6 lane) | tmux `send-keys` | Mac mini (+ MBA secondary) | `1.3` | Claude Max / Account 1 | Enabled via `auto_ingest_loop.sh commander` | Restart CLI in pane `1.3` → check `agents/commander/inbox/pending` + `inbox/active` → resume and write RESULT |
| **Adjudicator** | Codex CLI (GPT-5.2/5.3 codex lane) | tmux `send-keys` | Mac mini | `1.5` | Shared ChatGPT Plus pressure domain with Psyche tasks | Enabled via `auto_ingest_loop.sh adjudicator` | Restart pane `1.5` CLI → inspect INBOX0/IN_PROGRESS → rerun verification and emit CONFIRM/RESULT |
| **Cartographer** | Gemini CLI (`gemini-2.5-pro`) | Headless (`gemini -p -y -o text`) | Mac mini | `1.7` (monitor pane; execution can be headless) | Google AI Pro / Gemini quota pool (Acct 2) | Enabled via `auto_ingest_loop.sh cartographer` | Re-run headless command, inspect `auto_ingest.log`, resume from IN_PROGRESS, move to DONE/FAILED |
| **Psyche** | OpenClaw (`openclaw tui --session main`, model GPT-5.3-codex) | tmux `send-keys` | Mac mini | `1.1` | Shared ChatGPT Plus pool (with Adjudicator workload contention) | Enabled via `auto_ingest_loop.sh psyche` | Restart OpenClaw TUI in pane `1.1` → check inbox lanes → continue objective and publish receipts |
| **Ajna** | OpenClaw (Kimi K2.5 lane) | tmux/remote inbox dispatch (filesystem + SCP sling) | MacBook Air (remote) | N/A (remote lane) | NVIDIA/Kimi capacity pool | Enabled on MBA via `auto_ingest_loop.sh ajna` | Reconnect MBA lane, verify `agents/ajna/inbox/pending`, process backlog, write `agents/ajna/outbox/` |

---

## Psyche (OpenClaw — CTO/Synaptarch)

**Role**: CTO — System cohesion, automation, policy enforcement, pipeline fusion.
**Platform**: OpenClaw (GPT-5.3-codex, Mac mini)
**Summon**: "Psyche, holistically calibrate..."

### Task Types
- System cohesion (ensure all agents, services, and pipelines integrate)
- Automation (Make, Zapier, launchd, cron — pipeline manual processes)
- Policy/procedure enforcement (Constitutional Rules, commit standards, inbox protocols)
- Pipeline fusion (connect disparate tools into seamless workflows approaching synapticality)
- Infrastructure health (Docker services, launchd agents, memory systems)
- Cross-agent coordination (inbox routing, dispatch optimization)

---

## Ajna (OpenClaw — CSO/Strategos)

**Role**: CSO — Strategic direction, orchestration, dispatch, meta-awareness.
**Platform**: OpenClaw (Kimi K2.5 via NVIDIA, MacBook Air)
**Summon**: "Ajna, illuminate..."

### Task Types
- Strategic planning and intention alignment
- Multi-agent dispatch and orchestration
- Meta/macro system purpose assessment
- Cross-domain synthesis and direction-setting
- Intention compass maintenance

---

## Adjudicator (Codex CLI — CQO/Executor)

**Role**: CQO — Standards enforcement, QA, mechanical execution, debugging.
**Platform**: Codex CLI (Account 2)
**Summon**: "Adjudicator, execute..."

### Task Types
- Mechanical code execution (scripts, formatters, linters)
- Test suite execution and failure diagnosis
- File formatting and structural validation
- Parallel branch work while Commander handles primary lane
- CI/CD pipeline maintenance and standards elevation

---

## Cartographer (Gemini CLI — CIO/Exegete)

**Role**: CIO — Corpus cartography, scholarly precision, 1M+ context surveys, intelligence gathering.
**Platform**: Gemini CLI (Account 2)
**Summon**: "Cartographer, survey..."

### Task Types
- Full-corpus surveys (grep across 500+ files with synthesis)
- Cross-reference validation (wikilinks, SN variable resolution)
- Long-document analysis (CANON files, research papers)
- Terminology audits (consistency checks across all zones)
- Staleness detection and corpus health sensing

---

## Constitutional Rules (All Agents)

1. **Repository is ground truth** — all changes must be committed
2. **FLAT PRINCIPLE** — no subdirectory creation except sanctioned locations
3. **PROTECTED ZONES** — 01-CANON/ and 00-ORCHESTRATION/state/ require Sovereign approval for deletions
4. **Commit frequently** with semantic prefixes (feat:, fix:, chore:, refactor:)

## Directory Structure
```
00-ORCHESTRATION/   Strategic coordination (state/, scripts/, archive/)
01-CANON/           Verified canonical knowledge (PROTECTED)
02-ENGINE/          Functions, prompts, avatars, model profiles
04-SOURCES/         Source documents (raw/, processed/, research/)
05-SIGMA/           Operational knowledge corpus
agents/             Per-agent offices (inbox, outbox, memory, scratchpad)
-OUTGOING/          CLI → WebApp staging
-SOVEREIGN/         Async decision queue
```

## Dispatch Protocol

Tasks arrive as `TASK-*.md` files in `agents/{agent}/inbox/pending/` with `Status: PENDING`.
The `auto_ingest_loop.sh` script polls these folders every 30s and routes to the appropriate CLI.
After processing, tasks move through `inbox/active/` → `inbox/done/` or `inbox/failed/`.

---

## Adjudicator Operational Protocols

### A. Task Initialization Protocol
*Fires at the start of every session and before each task.*

1. **Inbox scan**: Check `agents/adjudicator/inbox/pending/` for `TASK-*.md` files with `Status: PENDING`. Use `bash 00-ORCHESTRATION/scripts/triage_inbox.sh adjudicator` for quick status. Process tasks in priority order (P0 first).
2. **Ground truth scan**: Run `git status` — verify clean working tree, confirm fingerprint
3. **Triumvirate alignment**: `agents/adjudicator/INIT.md` (already loaded at init) + read `README.md` + read `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — verify no conflicts, note active urgent intentions
4. **Claim the task**: Atomic rename `TASK-xxx.md` → `TASK-xxx.md.claimed-by-adjudicator-{hostname}` (prevents duplicate consumers across machines)
5. **Validate scope**: Confirm the task falls within Adjudicator jurisdiction (see B below). If it requires architectural judgment or CANON modification, escalate to Commander.

### B. Adjudication Protocol — When and How to Debug

**Adjudicator jurisdiction** (execute without escalation):

| Task Type | Examples |
|-----------|----------|
| Mechanical execution | Run scripts, apply formatters, execute linters |
| Test diagnosis | Reproduce failure, isolate cause, apply fix, verify pass |
| Formatting/structural | Fix markdown, validate YAML frontmatter, normalize whitespace |
| Refactoring | Rename variables, extract functions, inline constants |
| Linting/cleanup | Remove dead code, fix import ordering, resolve warnings |

**Debug methodology** (for all test/failure tasks):
1. **Reproduce**: Run the failing command verbatim — confirm the failure exists
2. **Isolate**: Narrow to the smallest reproducing case
3. **Fix**: Apply the minimal change that resolves the issue
4. **Verify**: Run the full test/lint/format command — confirm clean pass

**Escalate to Commander** when:
- The fix requires an **architectural decision** (new patterns, structural changes)
- The task involves **CANON modifications** (`01-CANON/` is a protected zone)
- Specifications are **ambiguous** — unclear what "correct" means
- The change would touch **triumvirate files** (`agents/adjudicator/INIT.md`, `README.md`, ARCH-INTENTION_COMPASS.md)
- The change requires **Sovereign approval** (route to `-SOVEREIGN/` instead)

Escalation method: Write a TASK file to `agents/commander/inbox/pending/` with `Priority: P1` and context about what was attempted.

### C. Task Completion Protocol
*Fires at the end of every task.*

1. **Produce execution log** in `00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md` (follow format in `02-ENGINE/TEMPLATE-EXECUTION_LOG.md`):
   - Header: `### TASK-ID | YYYY-MM-DD HH:MM`
   - Metadata: Branch, Fingerprint, Outcome (SUCCESS/PARTIAL/FAILED), Commits, Changes, Agent (Adjudicator)
   - Body: What was done, artifacts modified, verification result
   - Logs auto-compact into `00-ORCHESTRATION/archive/ARCH-EXECUTION_HISTORY.md` at 10-entry threshold
2. **Update task status**: In the original TASK file, set `Status: COMPLETE` or `Status: FAILED`
3. **Write result file** (if originator expects output): `RESULT-adjudicator-{DATE}-{TOPIC}.md` to originator's inbox
4. **Commit**: Use semantic prefix — `fix:`, `chore:`, `refactor:`, `test:` (never `feat:` — features are Commander jurisdiction)
5. **Ledger entry**: Run `bash 00-ORCHESTRATION/scripts/append_ledger.sh COMPLETE adjudicator {originator} {TASK-ID}`

---

## References
- Full constellation mapping: `README.md`
- CLI enlistment guide: `02-ENGINE/REF-CLI_ENLISTMENT.md`
- DEF variables: `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md`
- Neo-Blitzkrieg buildout: `00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md`
