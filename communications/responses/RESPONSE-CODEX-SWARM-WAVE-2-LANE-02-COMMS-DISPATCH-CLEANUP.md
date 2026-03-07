# Response

**Response ID**: `RSP-20260306-comms-dispatch-cleanup`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-2-lane-02-comms-dispatch-cleanup`
**Result state**: `complete`
**Receipt artifacts**:
- `communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-02-COMMS-DISPATCH-CLEANUP.md`

## Returned Content

Derived from:

- [COMMUNICATIONS-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/COMMUNICATIONS-LAW-v1.md)
- [communications/dispatches/README.md](/Users/system/syncrescendence/communications/dispatches/README.md)
- [communications/README.md](/Users/system/syncrescendence/communications/README.md)
- [README.md](/Users/system/syncrescendence/README.md)
- [AGENTS.md](/Users/system/syncrescendence/AGENTS.md)
- [WORK-LOOP.md](/Users/system/syncrescendence/WORK-LOOP.md)

The minimal live-facing documentation cleanup is:

1. update the communications index so the lane map itself is no longer incomplete
2. update the root README so root-level routing does not describe `communications/` as a six-lane surface
3. update `AGENTS.md` so constitutional lane-role summaries do not omit dispatches
4. update `WORK-LOOP.md` so the metabolic rule matches the now-physical communications topology

Not recommended in this packet:

- editing [COMMUNICATIONS-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/COMMUNICATIONS-LAW-v1.md), because it already includes `communications/dispatches/`
- broad office-by-office README cleanup, because that is normalization follow-on work rather than the minimum live-facing fix

## 1. Exact Docs That Should Mention Dispatches Now

- [communications/README.md](/Users/system/syncrescendence/communications/README.md)
- [README.md](/Users/system/syncrescendence/README.md)
- [AGENTS.md](/Users/system/syncrescendence/AGENTS.md)
- [WORK-LOOP.md](/Users/system/syncrescendence/WORK-LOOP.md)

## 2. Patch-Ready Wording

### A. `communications/README.md`

Replace:

```md
Use it for:
- dispatch packets and prompts
- returned responses
- handoffs
- logs
- retros
- assessments
```

With:

```md
Use it for:
- prompts and packets
- responses
- dispatch records
- handoffs
- logs
- retros
- assessments
```

Add `dispatches` to the sub-lane list:

```md
## Sub-lanes

- [prompts](/Users/system/syncrescendence/communications/prompts)
- [responses](/Users/system/syncrescendence/communications/responses)
- [dispatches](/Users/system/syncrescendence/communications/dispatches)
- [handoffs](/Users/system/syncrescendence/communications/handoffs)
- [logs](/Users/system/syncrescendence/communications/logs)
- [retros](/Users/system/syncrescendence/communications/retros)
- [assessments](/Users/system/syncrescendence/communications/assessments)
```

Recommended one-sentence clarification to append near the rule or authority section:

```md
`dispatches/` is the durable routing and receipt lane for communications whose send, receipt, retry, or failure state must survive as lineage.
```

### B. `README.md`

Replace:

```md
- [communications](/Users/system/syncrescendence/communications): prompts, responses, handoffs, logs, assessments
```

With:

```md
- [communications](/Users/system/syncrescendence/communications): prompts, responses, dispatches, handoffs, logs, retros, assessments
```

### C. `AGENTS.md`

Replace invariant 3:

```md
3. **One Artifact, One Class** — prompts, responses, handoffs, playbooks, operators, executive artifacts, program artifacts, and assessments must stay in their lanes.
```

With:

```md
3. **One Artifact, One Class** — prompts, responses, dispatches, handoffs, playbooks, operators, executive artifacts, program artifacts, and assessments must stay in their lanes.
```

Replace the lane-role summary:

```md
- `communications/`: prompts, responses, handoffs, logs, retros, assessments
```

With:

```md
- `communications/`: prompts, responses, dispatches, handoffs, logs, retros, assessments
```

### D. `WORK-LOOP.md`

Replace:

```md
- prompts, responses, and handoffs belong in communications lineage
```

With:

```md
- prompts, responses, dispatches, and handoffs belong in communications lineage
```

Recommended optional clarification immediately after:

```md
- dispatch artifacts are for durable routing and receipt state, not for every prompt by default
```

## 3. Terminology Clarifications

- `prompts` are the request bodies or packets that ask for work.
- `responses` are the returned answer bodies tied to prompts or packets.
- `dispatches` are event records about routing, send state, receipt, retry, failure, or route changes for a named communication.
- `logs` are chronological traces and observability records; they are not the authoritative home for dispatch metadata once that metadata has lineage value.

Boundary rule:

- prompt != dispatch
- response != dispatch
- log != dispatch
- one communication may lawfully have all four artifacts when both content and routing history matter

## 4. Top Failure Modes If The Layer Stays Semantically Incomplete

- prompt bodies continue absorbing dispatch metadata, which blurs content vs route lineage
- dispatch events keep getting filed as logs, making authoritative receipt state harder to audit
- root and constitutional summaries teach an outdated lane model, so new artifacts are misrouted by default
- validators and migration work inherit contradictory semantics between the law doc and the live-facing indexes
- office-local receipts and outbox residue are more likely to be promoted inconsistently because the federal destination remains underdescribed

## 5. Status

- `complete`: required docs identified, wording drafted, terminology clarified, and failure modes listed
