# SIEGE CC28 — Adjudicator Engineering Tasks

**Agent**: Adjudicator (Codex Desktop App)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## TASK 1: Config Migration Script (Strangler-Fig)

Oracle CC28 confirmed: config.sh and config.py exist but only scaffold_validate.sh uses them. 146 files remain hardcoded.

**Build**: `orchestration/00-ORCHESTRATION/scripts/config_migrate.sh`

Requirements:
1. Read the inventory from `-INBOX/commander/00-INBOX0/RESULT-CODEX-CONFIG-CENTRALIZATION.md`
2. For each Bash script in `orchestration/00-ORCHESTRATION/scripts/`: inject `source "$(dirname "${BASH_SOURCE[0]}")/config.sh"` and replace hardcoded paths with config vars
3. For each Python script in `orchestration/00-ORCHESTRATION/scripts/`: inject `from config import *` and replace hardcoded paths
4. Skip markdown files (prose references migrate later)
5. **DRY-RUN by default** — `--dry-run` shows diff, `--apply` writes changes
6. Run `scaffold_validate.sh` as post-migration gate
7. Output a summary of files migrated vs skipped

**Verify**: Run with `--dry-run`, confirm output is sane, then run with `--apply` on scripts/ only. Commit with `feat: config migration — strangler-fig phase 1 (scripts)`.

## TASK 2: Persist Session Brief to Disk

Oracle CC28 recommended: session_state_brief.py output is ephemeral (context only). It should persist.

**Modify**: `orchestration/00-ORCHESTRATION/scripts/session_state_brief.py`

Requirements:
1. After generating the brief, append it as a structured entry to `agents/commander/memory/journal/YYYY-MM-DD.jsonl` (UTC date)
2. Entry format: `{"timestamp": "ISO8601", "type": "session_brief", "content": "<brief text>"}`
3. Create the journal file if it doesn't exist
4. Do NOT change the existing stdout behavior — the hook still needs terminal output

**Verify**: Run the script, confirm journal file is created with valid JSONL entry.

## TASK 3: Integration-First Gate

Oracle's meta-finding: Means-Ends Inversion. Antidote is an Integration-First Gate.

**Modify**: `orchestration/00-ORCHESTRATION/scripts/session_state_brief.py`

Add a new section to the brief output: `## Integration Metric` that reports:
- Count of atoms promoted this session (grep git log for "promote" or "integrate" in today's commits)
- Count of files migrated to config.sh/config.py this session
- A simple pass/fail: "Integration-First Gate: PASS" if at least 1 integration artifact was committed, "WARN" otherwise

This surfaces the anti-pattern directly in every session brief.

---

## CONSTRAINTS
- Commit each task separately with semantic prefix
- Do not modify AGENTS.md or CLAUDE.md
- Do not create new top-level directories
- Run verification before claiming done
