# TASK-20260216-zero_offline_adversarial_audit

**Kind**: TASK
**From-Agent**: commander
**Reply-To**: commander
**CC**: commander
**Priority**: P0
**Status**: PENDING

## Objective

ADVERSARIAL ZERO-OFFLINE AUDIT. Your mission: attempt to find every possible way the Syncrescendence constellation could go offline, and for each
attack vector, verify that a defense exists or create one.

Read these files first:
- CLAUDE.md (root)
- AGENTS.md (root)
- GEMINI.md (root)
- COCKPIT.md (root)
- orchestration/scripts/auto_ingest_loop.sh
- orchestration/scripts/constellation_watchdog.sh
- orchestration/launchd/com.syncrescendence.watchdog.plist
- orchestration/scripts/cockpit.sh
- orchestration/scripts/dispatch.sh

Then produce a RESULT file covering:

### A. Attack Surface Enumeration
List every way the constellation could go offline:
- Rate limit exhaustion (per model: Gemini, ChatGPT Plus, Anthropic, NVIDIA/Kimi)
- tmux session death (crash, reboot, OOM)
- Network partition (Tailscale down, SSH broken, DNS failure)
- Git conflicts (merge conflicts, push protection, divergent histories)
- Stale lockfiles blocking auto-ingest
- Agent context exhaustion (100% tokens, no compaction)
- Credential expiry (API keys, OAuth tokens, SSH keys)
- Disk full on either machine
- launchd daemon failure (watchdog stops cycling)
- Process zombies (headless gemini never exits)
- Config drift (CLAUDE.md on MBA vs Mac mini diverge)

### B. Defense Gap Analysis
For each attack vector: does a defense exist in the current codebase? Rate: DEFENDED / PARTIAL / UNDEFENDED.

### C. Proposed Hardening Patches
For every UNDEFENDED or PARTIAL vector, write the EXACT code or config change needed. Include file path, line numbers, and the change.

### D. Agent Surface Audit
Check EVERY agent-facing config file for missing operational knowledge:
- Does CLAUDE.md document the auto-ingest system?
- Does CLAUDE.md document the watchdog?
- Does CLAUDE.md document dispatch.sh and the INBOX protocol?
- Does AGENTS.md list all agent CLIs with their dispatch modes (tmux vs headless)?
- Does GEMINI.md mention headless mode (-p flag)?
- Does any config mention the SYNCRESCENDENCE_REMOTE_AGENT_HOST vars?
- Does any config document rate limit recovery procedures?
- Does any config document what to do when context is exhausted?

For EVERY gap, write the exact text that must be added and where.

Write result to: -OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260216-zero_offline_adversarial_audit.md
