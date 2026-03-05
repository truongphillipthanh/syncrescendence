# CC81 Phase 0 Gate Checklist

**Date**: 2026-03-04  
**Status**: active  
**Class**: pre-cutover gate

## Purpose

Define hard pass/fail gates before any ownership mutation begins.

## Gate Checks

| Gate ID | Check | Executor | Pass Condition | Evidence Artifact |
|---|---|---|---|---|
| `P0-G01` | Target account security hardening | human | MFA enabled and at least one recovery path validated for `syncrescendence@gmail.com` | screenshot pointer + confirmation note |
| `P0-G02` | Legacy break-glass viability | human | legacy account can still authenticate and reach owner surfaces | login verification note |
| `P0-G03` | Key integration inventory | commander | list of active automations/integrations tied to legacy identity exists | inventory artifact path |
| `P0-G04` | Token rotation freeze window | human | no unrelated token rotations during cutover window | approval note |
| `P0-G05` | Platform roster lock | commander | platform list and order are frozen for current wave | tracker state update |
| `P0-G06` | Psyche invocation capability | psyche/human | either paired and callable OR explicitly marked blocked with workaround | nodes status evidence |
| `P0-G07` | Manus execution path | commander | Manus API reachable and task dispatch/poll cycle successful | task id + status evidence |

## Gating Rule

All `P0-*` checks must pass before moving platform state from `not_started` to `snapshot_pending`.

## Failure Handling

If any gate fails:

1. Set `phase0_security_readiness` to `blocked`.
2. Record blocker owner and unblock action.
3. Prohibit owner mutation windows until gate is re-run and passes.
