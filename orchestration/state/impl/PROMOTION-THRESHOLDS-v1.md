# Promotion Thresholds v1

**Date**: 2026-03-06
**Status**: compact constitutional addendum
**Purpose**: define the minimum lawful thresholds for promoting artifacts from `offices/` into `communications/` and from `communications/` into `executive/`

## 1. Core Rule

Artifact movement has two thresholds:

- `lineage threshold`: `offices/` -> `communications/`
- `steering threshold`: `communications/` -> `executive/`

No artifact should skip directly from `offices/` to `executive/`.

## 2. Offices -> Communications

Promote an office artifact into `communications/` when any of the following becomes true:

- another office, session, runtime surface, or external actor must read or act on it
- it is the authoritative packet, response, receipt, confirm, handoff, assessment, or dispatch record for a named exchange
- it must survive beyond local queue cleanup as durable lineage or audit evidence
- it is cited outside the originating office as proof of state, completion, failure, or transfer

Keep the artifact in `offices/` when it is still:

- scratch work
- queue residue
- local bookkeeping
- machine/runtime noise
- uncited local notes

## 3. Communications -> Executive

Promote a communications artifact into `executive/` only when sovereign steering is required.

Allowed executive classes:

- `briefing`
- `escalation`
- `summit`

Promotion is lawful only when the artifact:

- requests sovereign decision, ratification, reprioritization, or exception handling
- synthesizes cross-lane state for sovereign read-in
- requires synchronized comparative review across multiple lanes or ministries

Do not promote when the artifact is merely:

- informative
- evidentiary
- operationally resolvable under existing authority
- an ordinary prompt, response, receipt, confirm, dispatch record, or log

## 4. Dispatch Classification

`communications/dispatches/` exists for communication-event records, not for every outbound prompt.

A dispatch artifact belongs in `communications/dispatches/` when it records one or more of:

- the routed task or packet identifier
- sender and intended receiver
- route or surface used
- dispatch status
- authoritative send, receipt, or retry history

Prompts remain in `communications/prompts/`.
Responses remain in `communications/responses/`.
Chronological operational traces remain in `communications/logs/`.

## 5. Forbidden Direct Promotions

The following are unlawful by default:

- `offices/**` filed directly into `executive/**`
- raw office `TASK`, `RESULT`, `RECEIPT`, `CONFIRM`, `ALERT`, or `EXECLOG` artifacts filed directly into `executive/`
- use of `executive/` as a prestige archive for artifacts that do not carry steering burden

If executive attention is required, derive a lawful `briefing`, `escalation`, or `summit` artifact inside `communications/` first, then promote that derivative artifact.

## 6. Default Filing Table

| Artifact burden | Default home | Promote when |
| --- | --- | --- |
| office-local work | `offices/` | it crosses a lineage threshold |
| prompt / packet | `communications/prompts/` | it is a live routed communication |
| response | `communications/responses/` | it answers a prompt or packet |
| dispatch record | `communications/dispatches/` | it records routing, receipt, status, or retries |
| log | `communications/logs/` | it is primarily chronological observability |
| sovereign steering derivative | `executive/briefings/`, `executive/escalations/`, or `executive/summits/` | it crosses a steering threshold |

## 7. Enforcement Minimum

Validators should enforce at least:

- no direct `offices/` -> `executive/` filing
- no artifact under `executive/` unless classed as `briefing`, `escalation`, or `summit`
- no dispatch record filed as a response or log merely because a dispatch lane is missing
