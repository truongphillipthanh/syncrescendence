# REF-PROCEDURAL_STANDARD_BEARER.md

**Version**: 1.0.0
**Created**: 2026-02-12
**Status**: ACTIVE
**Owner**: Adjudicator (Process/Output Quality) + Psyche (Systems/Throughput Quality)

---

## 1. Purpose

Codify the operating doctrine that produced current breakthroughs and make it repeatable under stress.

This protocol defines how to:
- exploit breakthroughs without losing coherence,
- preserve process quality while scaling throughput,
- convert repeated work into automation quickly,
- maintain self-healing operations across watcher agents.

---

## 2. Role Split (Non-overlapping Mandates)

### Adjudicator — Procedural Standard Bearer

Primary objective: maximize process and output quality.

Core duties:
- enforce acceptance criteria before execution,
- enforce verification-before-completion,
- enforce fail-closed behavior on model/session errors,
- codify durable standards into `REF-*` and Rosetta terms.

### Psyche — Systems and Throughput Quality

Primary objective: maximize system throughput and automation maturity.

Core duties:
- identify repetitive work and design automation points,
- implement or propose scripts/hooks/watchers for repetitive workflows,
- reduce operator cognitive load and queue latency,
- ensure service continuity and recovery loops stay intact.

---

## 3. Operating Loop (Breach Exploitation Loop)

1. Detect breach: confirm an unlocked path (new capability, process opening, data access, architecture simplification).
2. Forward passage of lines: reinforce the opened path with immediate execution tasks.
3. Commit reserves: reallocate available agents to widen the gain.
4. Follow-and-support: secondary agents harden, document, and automate behind the leading edge.
5. Ratify to repertoire: convert ad hoc success into canonical protocol and Rosetta vocabulary.

---

## 4. Control Gates (Must Pass)

1. **Intent Gate**: task ties to active objective and critical path.
2. **Quality Gate**: explicit acceptance criteria and falsifier are defined.
3. **Execution Gate**: owner and deadline are assigned; dispatch is acknowledged.
4. **Verification Gate**: fresh command evidence confirms claims.
5. **Durability Gate**: outcome is written to durable artifacts (`REF-*`, scripts, Rosetta).

---

## 5. Automation Trigger Policy

Automation is mandatory when either condition is true:
- same task executed 2+ times manually within 7 days,
- manual recovery took >5 minutes for a known failure mode.

Required output from automation candidate review:
- task fingerprint and observed repetition count,
- proposed automation insertion point,
- failure modes and rollback path,
- owner and verification command.

---

## 6. Self-Healing Baseline

Operational baseline must include:
- launchd KeepAlive + watchdog restart loop,
- critical watcher auto-bootstrap from local plists,
- cockpit session auto-rebuild when pane topology drifts,
- critical agent pane restart (Psyche + Adjudicator),
- skill repertoire sync into all active runtimes.

---

## 7. Dispatch Contract (Adjudicator ↔ Psyche)

Every systems-quality dispatch to Psyche must include:
- objective and success criteria,
- explicit automation discovery scope,
- ranked opportunities by expected throughput gain,
- concrete implementation recommendation for top opportunities,
- rollback/safety notes for each recommendation.

Every returned result is evaluated by Adjudicator for:
- correctness,
- blast radius,
- operational durability,
- maintenance burden.

---

## 8. Success Metrics

- Median time-to-recovery for watcher/service failures
- Queue dwell time in `00-INBOX0/` and `10-IN_PROGRESS/`
- Percentage of repeated tasks converted to automation
- Verification compliance rate before completion claims
- Frequency of blocked tasks due preventable operational drift

---

## 9. Canonical Rule

If a workflow is important enough to repeat, it is important enough to automate, verify, and canonize.
