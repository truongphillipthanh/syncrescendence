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

## References
- Full constellation mapping: `COCKPIT.md`
- CLI enlistment guide: `02-ENGINE/REF-CLI_ENLISTMENT.md`
- DEF variables: `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md`
- Neo-Blitzkrieg buildout: `00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md`
