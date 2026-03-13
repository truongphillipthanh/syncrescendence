# Five-Account Platform Execution Checklist

**Status**: active
**Class**: operator checklist
**Purpose**: provide the exact manual checklist for platform-account readiness and browser preflight across the five chain identities without mutating live platform state

## Operating Rule

- use this checklist only for preflight, not for account creation or platform mutation
- repo artifacts record readiness states and blockers, not secrets
- if any step becomes ambiguous, stop and mark the blocker instead of guessing

## State Legend

| State Class | Meaning | Allowed Values |
|---|---|---|
| email/keychain identity | local identity slot is available before browser work | `available`, `blocked`, `unconfirmed` |
| platform account existence | platform account/profile/channel has been externally observed or not | `observed_exists`, `observed_absent`, `unconfirmed` |
| platform session readiness | browser session is isolated and authenticated as the intended slot | `session_ready`, `session_blocked`, `session_contaminated`, `session_unconfirmed` |
| capture readiness | read-only evidence can be gathered with no live mutation | `capture_ready`, `capture_blocked`, `capture_requires_mutation`, `capture_unconfirmed` |

## Global Gates

- [ ] confirm the five chain identities exist in Keychain and will be referenced only as `CHAIN-01` through `CHAIN-05` in repo notes
- [ ] prepare one isolated browser profile, container, or equivalent context per chain slot
- [ ] freeze scope to read-only preflight only
- [ ] accept YouTube -> X -> Pinterest -> later surfaces as the platform order for each chain slot
- [ ] accept stop-on-ambiguity as mandatory

## Per-Platform Stop Conditions

Stop immediately if any of the following appears:

- account creation prompt
- onboarding wizard
- interest picker
- profile setup or channel setup
- board creation requirement
- forced follow or subscribe action
- ambiguous multi-login state
- wrong handle or wrong email in session

## Execution Order

For each chain slot:

1. confirm Keychain-backed identity availability
2. open the dedicated isolated browser context
3. check YouTube existence -> session readiness -> capture readiness
4. check X existence -> session readiness -> capture readiness
5. check Pinterest existence -> session readiness -> capture readiness
6. check any later surface only after the first three are classified
7. record blockers before moving to the next chain slot

## CHAIN-01

- [ ] intended identity confirmed from Keychain
- [ ] isolated browser context prepared
- [ ] no other chain identity present in active context

| Platform | Account Existence | Session Readiness | Capture Readiness | Stop Condition / Notes |
|---|---|---|---|---|
| YouTube |  |  |  |  |
| X |  |  |  |  |
| Pinterest |  |  |  |  |
| Later surface 01 |  |  |  |  |
| Later surface 02 |  |  |  |  |

## CHAIN-02

- [ ] intended identity confirmed from Keychain
- [ ] isolated browser context prepared
- [ ] no other chain identity present in active context

| Platform | Account Existence | Session Readiness | Capture Readiness | Stop Condition / Notes |
|---|---|---|---|---|
| YouTube |  |  |  |  |
| X |  |  |  |  |
| Pinterest |  |  |  |  |
| Later surface 01 |  |  |  |  |
| Later surface 02 |  |  |  |  |

## CHAIN-03

- [ ] intended identity confirmed from Keychain
- [ ] isolated browser context prepared
- [ ] no other chain identity present in active context

| Platform | Account Existence | Session Readiness | Capture Readiness | Stop Condition / Notes |
|---|---|---|---|---|
| YouTube |  |  |  |  |
| X |  |  |  |  |
| Pinterest |  |  |  |  |
| Later surface 01 |  |  |  |  |
| Later surface 02 |  |  |  |  |

## CHAIN-04

- [ ] intended identity confirmed from Keychain
- [ ] isolated browser context prepared
- [ ] no other chain identity present in active context

| Platform | Account Existence | Session Readiness | Capture Readiness | Stop Condition / Notes |
|---|---|---|---|---|
| YouTube |  |  |  |  |
| X |  |  |  |  |
| Pinterest |  |  |  |  |
| Later surface 01 |  |  |  |  |
| Later surface 02 |  |  |  |  |

## CHAIN-05

- [ ] intended identity confirmed from Keychain
- [ ] isolated browser context prepared
- [ ] no other chain identity present in active context

| Platform | Account Existence | Session Readiness | Capture Readiness | Stop Condition / Notes |
|---|---|---|---|---|
| YouTube |  |  |  |  |
| X |  |  |  |  |
| Pinterest |  |  |  |  |
| Later surface 01 |  |  |  |  |
| Later surface 02 |  |  |  |  |

## Completion Test

This checklist is complete only when every in-scope chain slot and platform row has:

- one account-existence classification
- one session-readiness classification
- one capture-readiness classification
- one precise blocker note whenever a ready state is not achieved

If a row would require account creation or social mutation to advance, completion means recording that blocker, not bypassing it.
