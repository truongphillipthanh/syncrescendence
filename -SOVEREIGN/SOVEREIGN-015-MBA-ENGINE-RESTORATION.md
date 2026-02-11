# SOVEREIGN-015: MBA Engine Restoration — Status & Escalations

**Date**: 2026-02-11
**From**: Commander (COO)
**Priority**: P0-CRITICAL (contains multiple escalation items)
**Status**: AWAITING SOVEREIGN TRIAGE

---

## Summary

Commander initiated on MacBook Air and ran a comprehensive clarescence of the "second engine." The MBA is 95% operational — gateway plist was missing (now fixed), identity was wrong (now fixed), inbox has been triaged.

**However, inbox triage revealed systemic failures that require Sovereign decisions.**

---

## COMPLETED (No Sovereign Action Needed)

| Fix | Status |
|-----|--------|
| OpenClaw gateway launchd plist created | DONE — survives reboots now |
| Gateway identity changed from Psyche → Ajna | DONE — `IDENTITY.md` updated, gateway restarted |
| `.claude/skills/claresce.md` restored from git | DONE |
| Commander inbox cleared (9 items → 0) | DONE — triaged to 40-DONE and 50_FAILED |

---

## ESCALATION 1 — Adjudicator Systemic Failure (P0)

**What**: Adjudicator (Codex CLI, Mac mini) cannot execute tasks. Model `gpt-5.3-codex` returns "does not exist" errors. Linear/Notion MCP auth tokens are invalid (OAuth errors).

**Impact**: Both dispatched tasks failed completely:
- `TASK-20260211-ecosystem_health` — zero deliverables
- `TASK-20260211-KINETIC_LAYER_DATA` — zero of 5 artifacts produced (ACTION_TYPES, APP_ACTIONS, AGENT_BINDINGS, MODEL_CAPABILITIES, WORKFLOW_TEMPLATES)

**PROJ-006b Phase B (Kinetic Layer)** is blocked on this. The 200+ rows of structured kinetic data Adjudicator was supposed to produce don't exist.

**Decision Needed**: Fix Adjudicator's model access on Mac mini, or reassign kinetic data work to Commander/Cartographer.

---

## ESCALATION 2 — INT-1201 Revenue Generation FAILED (P0)

**What**: The corpus insight sensing report flags INT-1201 (Revenue Generation) as FAILED status with no recovery path and no commits addressing it.

**Decision Needed**: Reset, reframe, or explicitly park this intention.

---

## ESCALATION 3 — SYN-24 Mastery IIC Email Setup (P0-Critical, 5 days stale)

**What**: This P0-Critical issue has been Sovereign-gated for 5 days with no movement. It requires manual configuration that only the Sovereign can perform.

**Decision Needed**: Execute, delegate, or explicitly deprioritize.

---

## ESCALATION 4 — Global Ledger Pipeline Broken

**What**: `append_ledger.sh` is not capturing commits. Only 6 entries in the ledger despite 73 commits in the last 24 hours. DYN-GLOBAL_LEDGER.md is stale.

**Decision Needed**: Low urgency but degrades observability. Commander can investigate and fix if authorized.

---

## MBA Health Scorecard (Post-Restoration)

| Component | Status |
|-----------|--------|
| Homebrew + deps | GREEN |
| OpenClaw 2026.2.9 | GREEN |
| Gateway (launchd-managed) | GREEN |
| Gateway identity = Ajna | GREEN |
| NVIDIA API (Kimi K2.5) | GREEN |
| Git sync | GREEN |
| 6 agent watchers | GREEN |
| 16 universal skills | GREEN |
| 11 OpenClaw skills | GREEN |
| Inbox (Commander) | GREEN (cleared) |
| Repo state | YELLOW (uncommitted DYN files) |
| Adjudicator (Mac mini) | RED (model access failure) |

**Verdict**: MBA second engine is ONLINE and AUTONOMOUS. The Mac mini has the systemic issues.
