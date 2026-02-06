# TASK-20260205-always_on_smoke_validation_v2

**From**: dispatch
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-05 16:29:26
**Fingerprint**: d0968c2
**Priority**: P1
**Status**: COMPLETE
**Claimed-By**: commander-M1-Mac-mini
**Claimed-At**: 2026-02-06T00:30:00Z
**Completed-At**: 2026-02-06T01:03:00Z
**Exit-Code**: 0
**Timeout**: 30

---

## Objective

Adjust plan based on Sovereign note: Claude Code is currently using Anthropic API (billing/credits) but we want it to use Claude Max OAuth/subscription on the Mac mini if possible.

Objective (on M1 Mac mini, user home):

A) Commander / Claude Code auth path
1) Determine current auth mode:
   - Inspect environment for ANTHROPIC_API_KEY and any claude-code auth files.
   - Run: claude --version; claude config list (if available) or equivalent.
   - Attempt to sign in / link to Claude Max subscription (OAuth) if supported by Claude Code CLI.
2) If Claude Code cannot use Claude Max subscription (CLI requires API key), document that as a hard constraint with citations (CLI help output).
3) If OAuth/subscription is possible, execute the login flow and re-test:
   - claude -p "respond with exactly: PONG_COMMANDER" 

B) Cartographer / Gemini watcher proof (must pass)
4) Dispatch a SENSOR_SMOKE task to cartographer and verify auto-complete + durable receipt.

C) Adjudicator / Codex auth
5) Fix Codex auth non-interactively if possible:
   - Prefer setting OPENAI_API_KEY in LaunchAgent EnvironmentVariables for com.syncrescendence.watch-adjudicator on the mini.
   - If interactive login is required, document exact steps + why.
   - Verify with a simple adjudicator task.

D) Ajna / OpenClaw install
6) Confirm whether openclaw is installed on mini:
   - command -v openclaw; openclaw --version
   - If missing: install via the correct mechanism for this environment (brew/npm) and verify gateway status.

E) Deliverables (proof, not just narrative)
7) Produce receipts in -OUTGOING:
   - RESULT-commander-20260205-always_on_smoke_validation_v2.md
   - RESULT-cartographer-20260205-sensor_smoke.md (if not auto-generated, include watcher logs showing execution)
   - RESULT-adjudicator-20260205-executor_smoke.md (or explicit auth blocker)
   - RESULT-ajna-20260205-openclaw_install_check.md

Also include:
- launchctl print for watch-commander/adjudicator/cartographer/ajna
- tail -120 of /tmp/syncrescendence-watch-{commander,adjudicator,cartographer,ajna}.err and .log

Success criteria:
- Cartographer auto-exec proves end-to-end.
- Commander either (a) works via OAuth/subscription, or (b) we conclusively prove Claude Code CLI cannot use Max subscription and must use API credits.
- Adjudicator is authenticated (API key or login).
- Ajna has openclaw installed and can run a trivial openclaw agent turn.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTGOING/RESULT-commander-20260205-always_on_smoke_validation_v2.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: always_on_smoke_validation_v2 complete" && git push`
