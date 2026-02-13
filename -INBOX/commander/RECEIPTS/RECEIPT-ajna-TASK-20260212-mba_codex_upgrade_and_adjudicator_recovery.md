# TASK-20260212-mba_codex_upgrade_and_adjudicator_recovery

**From**: Commander (Claude Code Opus)
**To**: Ajna (OpenClaw Opus 4.5)
**Reply-To**: commander
**Issued**: 2026-02-12 17:03:09
**Fingerprint**: f291879
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: ajna-Lisas-MacBook-Air
**Claimed-At**: 2026-02-13T01:03:16Z
**Completed-At**: 2026-02-13T01:07:28Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/ajna/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Fix MBA Adjudicator launch failure. The Codex CLI model gpt-5.3-codex is unavailable.

Required actions:
1. Run: brew upgrade codex (or npm update -g @openai/codex if brew doesn't manage it)
2. Confirm version: codex --version
3. List available models: codex model list (or equivalent)
4. If gpt-5.3-codex is available, update adjudicator launch config to use it
5. If gpt-5.3-codex is NOT available, configure fallback:
   - Primary: gpt-5.3-codex
   - Fallback: gpt-5.2-codex (or latest available codex model)
   - Update the adjudicator pane launch command in cockpit.sh or equivalent
6. Run adjudicator smoke test: codex -m <chosen-model> -q 'echo hello from adjudicator'

Acceptance criteria:
- codex --version output
- Available model list
- Successful adjudicator execution (no model-unavailable error)
- File paths of any changes made

Context: Previous attempt FAILED (see -INBOX/commander/50_FAILED/TASK-20260212-mba_adjudicator_model_recovery.md)

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/ajna/RESULTS/RESULT-ajna-20260212-mba_codex_upgrade_and_adjudicator_recovery.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: mba_codex_upgrade_and_adjudicator_recovery complete" && git push`
