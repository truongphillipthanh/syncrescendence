# Syncrescendence Agent Configuration

Multi-agent configuration for CLI tools operating on this repository.

---

## Adjudicator (Codex CLI)

**Role**: PARALLEL_EXEC — Mechanical code execution, debugging, formatting, test running.
**Platform**: Codex CLI (Account 2)
**Summon**: "Adjudicator, execute..."

### Task Types
- Mechanical code execution (scripts, formatters, linters)
- Test suite execution and failure diagnosis
- File formatting and structural validation
- Parallel branch work while Commander handles primary lane

---

## Cartographer (Gemini CLI)

**Role**: SENSOR — Corpus cartography, scholarly precision, 1M+ context surveys.
**Platform**: Gemini CLI (Account 2)
**Summon**: "Cartographer, survey..."

### Task Types
- Full-corpus surveys (grep across 500+ files with synthesis)
- Cross-reference validation (wikilinks, SN variable resolution)
- Long-document analysis (CANON files, research papers)
- Terminology audits (consistency checks across all zones)

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
-INBOX/             Per-agent task dispatch folders
-OUTGOING/          CLI → WebApp staging
-SOVEREIGN/         Async decision queue
```

## Dispatch Protocol

Tasks arrive as `TASK-*.md` files in `-INBOX/{agent}/` with `Status: PENDING`.
The `watch_dispatch.sh` script monitors these folders and routes to the appropriate CLI.
After processing, mark `Status: COMPLETE` or `Status: FAILED`.

---

## Adjudicator Operational Protocols

### A. Task Initialization Protocol
*Fires at the start of every task picked from `-INBOX/adjudicator/`.*

1. **Ground truth scan**: Run `git status` — verify clean working tree, confirm fingerprint
2. **Triumvirate alignment**: AGENTS.md (already loaded at init) + read `COCKPIT.md` + read `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — verify no conflicts, note active urgent intentions
3. **Claim the task**: Atomic rename `TASK-xxx.md` → `TASK-xxx.md.claimed-by-adjudicator-{hostname}` (prevents duplicate consumers across machines)
4. **Validate scope**: Confirm the task falls within Adjudicator jurisdiction (see B below). If it requires architectural judgment or CANON modification, escalate to Commander.

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
- The change would touch **triumvirate files** (AGENTS.md, COCKPIT.md, ARCH-INTENTION_COMPASS.md)
- The change requires **Sovereign approval** (route to `-SOVEREIGN/` instead)

Escalation method: Write a TASK file to `-INBOX/commander/` with `Priority: P1` and context about what was attempted.

### C. Task Completion Protocol
*Fires at the end of every task.*

1. **Produce execution log** in `00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md`:
   - Header: `### TASK-ID | YYYY-MM-DD HH:MM`
   - Metadata: Branch, Fingerprint, Outcome (SUCCESS/PARTIAL/FAILED), Commits, Changes, Agent (Adjudicator)
   - Body: What was done, artifacts modified, verification result
2. **Update task status**: In the original TASK file, set `Status: COMPLETE` or `Status: FAILED`
3. **Write result file** (if originator expects output): `RESULT-adjudicator-{DATE}-{TOPIC}.md` to originator's inbox
4. **Commit**: Use semantic prefix — `fix:`, `chore:`, `refactor:`, `test:` (never `feat:` — features are Commander jurisdiction)
5. **Ledger entry**: Run `bash 00-ORCHESTRATION/scripts/append_ledger.sh COMPLETE adjudicator {originator} {TASK-ID}`

---

## References
- Full constellation mapping: `COCKPIT.md`
- CLI enlistment guide: `02-ENGINE/REF-CLI_ENLISTMENT.md`
- DEF variables: `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md`
- Neo-Blitzkrieg buildout: `00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md`
