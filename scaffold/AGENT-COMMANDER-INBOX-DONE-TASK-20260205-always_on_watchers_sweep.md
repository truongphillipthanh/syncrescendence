# TASK-20260205-always_on_watchers_sweep

**From**: dispatch
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-05 16:08:40
**Fingerprint**: 1db3a82
**Priority**: P1
**Status**: COMPLETE
**Claimed-By**: commander-M1-Mac-mini
**Claimed-At**: 2026-02-06T00:08:45Z
**Completed-At**: 2026-02-06T00:20:00Z
**Exit-Code**: 0
**Timeout**: 30

---

## Objective

Comprehensive sweep + repair plan for always-on CLI executors (Commander/Adjudicator/Cartographer) + Ajna on the M1 Mac mini.

Objective:
1) Verify binaries exist on mini (non-interactive PATH):
   - command -v openclaw claude codex gemini fswatch
   - openclaw --version; node -v
2) Verify auth state for each executor in headless context:
   - claude: confirm non-interactive run works (e.g. 'claude -p "ping"')
   - codex: confirm non-interactive run works (e.g. 'codex "ping"' or minimal)
   - gemini: confirm 'gemini "ping"' works
   - openclaw: confirm 'openclaw gateway status' works
   If any require interactive login, document exactly what prompt appears.
3) Verify launchd installation location & unify:
   - We want repo-managed plists installed under ~/Library/LaunchAgents (NOT /Users/system/Library/LaunchAgents) unless you have a reason.
   - On mini run: ls -la ~/Library/LaunchAgents/com.syncrescendence.watch-*.plist ; ls -la /Users/system/Library/LaunchAgents/com.syncrescendence.watch-*.plist
4) Verify plists environment is sufficient for headless execution:
   - Ensure EnvironmentVariables.PATH includes /opt/homebrew/bin and any required paths.
   - Ensure NODE_OPTIONS=--no-warnings (optional but reduces noise) for all watchers.
5) Re-arm watchers on mini using repo script:
   - cd ~/Desktop/syncrescendence && bash orchestration/scripts/rearm_watchers.sh --mini
6) Validate watchers are actually running and can execute:
   - launchctl print gui/503/com.syncrescendence.watch-ajna
   - ...watch-commander, ...watch-adjudicator, ...watch-cartographer
   - tail -200 /tmp/syncrescendence-watch-*.err and .log
7) Smoke-test end-to-end by dropping 4 tiny tasks (PENDING) into each inbox and confirming COMPLETE and RESULT file written to -OUTGOING:
   - -INBOX/ajna/ -> openclaw agent turn
   - -INBOX/commander/ -> claude
   - -INBOX/adjudicator/ -> codex
   - -INBOX/cartographer/ -> gemini

Deliverable:
- Write a single report: -OUTGOING/RESULT-commander-20260205-always_on_watchers_sweep.md containing:
  - a checklist table with PASS/FAIL per requirement
  - exact CLI outputs for version/path/auth checks
  - any required config diffs (plists or scripts)
  - final 'always-on ready' verdict

Important constraint:
- Recent failures on mini returned Exit-Code 127 (command not found). Prioritize eliminating that class of failure: PATH + install + auth.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTGOING/RESULT-commander-20260205-always_on_watchers_sweep.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: always_on_watchers_sweep complete" && git push`
