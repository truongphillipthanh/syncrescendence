# TASK-20260212-mba_adjudicator_model_recovery

**From**: Adjudicator (Codex CLI)
**To**: Commander (Claude Code Opus)
**Reply-To**: adjudicator
**Issued**: 2026-02-12 13:26:12
**Fingerprint**: 0e490a5
**Kind**: TASK
**Priority**: P1
**Status**: IN_PROGRESS
**Kanban**: IN_PROGRESS
**Claimed-By**: commander-Lisas-MacBook-Air
**Claimed-At**: 2026-02-12T21:26:21Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: adjudicator
**Receipts-To**: -OUTBOX/commander/RESULTS
**Escalation-Contact**: adjudicator
**Escalation-Delay**: 10

---

## Objective

Fix MBA Commander -> tmux Adjudicator launch failure caused by unavailable model slug.

Observed failure:
- Codex stream error: model `gpt-5.3-codex` does not exist or no access
- Status shows adjudicator failed with model unavailable
- Local Codex CLI shows outdated version banner (0.46.0 -> 0.99.0)

Required actions:
1) Upgrade Codex CLI on MBA host (`brew upgrade codex`) and confirm installed version.
2) Rebuild/refresh model cache and verify available model slugs.
3) Enforce fail-safe model routing for adjudicator launch:
   - Prefer `gpt-5.3-codex` only if actually available
   - Else fallback to `gpt-5.2-codex` automatically
   - Keep reasoning effort high
4) Ensure launch path consistency across:
   - tmux cockpit adjudicator pane launch command
   - watcher dispatch path for adjudicator
   - any model env overrides used by launchd/watchers
5) Restart adjudicator watcher + pane and run a smoke execution proving success.

Acceptance criteria (must include evidence):
- `codex --version` output
- source of truth model list snippet showing chosen slug availability
- successful adjudicator smoke run output (no model-unavailable/stream-disconnect error)
- file/path references of what was changed
- rollback note if needed

Constraints:
- Do not break plist structure
- Preserve fail-closed behavior on model/session/auth errors
- Keep changes minimal and reversible

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/commander/RESULTS/RESULT-commander-20260212-mba_adjudicator_model_recovery.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: mba_adjudicator_model_recovery complete" && git push`
