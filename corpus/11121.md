# TASK-20260205-revive_ajna_auth

**From**: dispatch
**To**: Ajna (OpenClaw Opus 4.5)
**Issued**: 2026-02-05 15:23:10
**Fingerprint**: 1db3a82
**Priority**: P1
**Status**: FAILED
**Claimed-By**: ajna-M1-Mac-mini
**Claimed-At**: 2026-02-05T23:25:31Z
**Completed-At**: 2026-02-05T23:25:32Z
**Exit-Code**: 127
**Timeout**: 30

---

## Objective

Goal: revive Ajna by switching away from Anthropic Max. Configure OpenClaw on the Mac mini to use OpenAI via OAuth (openai-codex) for agent runtime, keep OpenAI API key for embeddings if needed. Steps: (1) run: openclaw doctor --non-interactive; (2) openclaw configure (or openclaw auth/login for openai-codex oauth if available); ensure auth.profiles includes openai-codex:default mode oauth; (3) set agents.defaults.model.primary=openai-codex/gpt-5.2 (or other desired) and restart gateway; (4) verify with: openclaw gateway status; (5) run a test agent turn: openclaw agent --agent main --message 'Ajna is back' --timeout 60; (6) rearm watchers: bash orchestration/scripts/rearm_watchers.sh --mini; (7) report back with exact outputs + any blockers.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTGOING/RESULT-ajna-20260205-revive_ajna_auth.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: revive_ajna_auth complete" && git push`
