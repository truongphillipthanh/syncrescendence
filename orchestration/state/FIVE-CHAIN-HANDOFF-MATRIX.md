# Five-Chain Handoff Matrix

**Date**: 2026-03-13
**Status**: staged control artifact
**Purpose**: record the default lawful inbound artifact classes, stopping points, and escalation boundaries across Acumen, Coherence, Efficacy, Mastery, and Transcendence

## Status Vocabulary

- `default inbound`: artifact classes a chain should consume without extra exception handling
- `bounded inbound`: source-near material allowed only after explicit Acumen-linked escalation
- `stopping point`: the artifact class where that chain should normally stop
- `forbidden default`: inbound or runtime patterns this matrix disallows by default

## Matrix

| Chain | Authority posture | Default inbound artifact classes | Bounded inbound exceptions | Default stopping points | Default downstream handoff | Forbidden default |
| --- | --- | --- | --- | --- | --- | --- |
| Acumen | governed intake and triage authority | captured manifests after import; registry candidates; polled raw candidate rows; verification bridge state downstream of triage | none beyond its own governed intake surfaces | triage decision; `Dawn Brief`; verification dossier; repo-side assessment; primary-source queue admission or hold | Coherence via `VERIFIED-SIGNAL-BRIEF-*`, repo-side assessment, queue readout, or bounded queue item; operator awareness via `Dawn Brief` | surrendering intake authority to later chains or treating imported manifests as self-executing downstream queues |
| Coherence | derivative synthesis authority | `VERIFIED-SIGNAL-BRIEF-*`; repo-side assessment artifacts; `PRIMARY-SOURCE-QUEUE-READOUT-*`; convergent promoted clusters | bounded primary-source queue items or dossiers with explicit reason codes from Acumen assessment surfaces | synthesis memo; framework dossier; comparison lattice; model update artifact | Efficacy for execution shaping; Mastery for pedagogy; Transcendence for meta-integration | raw intake streams; independent polling or triage; runtime raw-intake directories |
| Efficacy | derivative operational authority | Coherence synthesis memos; framework dossiers; `VERIFIED-SIGNAL-BRIEF-*` with direct operational implications; repo-side assessments with tactical consequence | bounded primary-source tasks routed for execution planning | task packet; protocol update; execution plan; backlog item; demonstration-domain plan | Mastery for teachable procedure; Transcendence for yield and failure-pattern review | reopening source-truth adjudication from scratch; independent raw candidate intake; runtime raw-intake directories |
| Mastery | derivative curriculum authority | Coherence synthesis memos; framework dossiers; Efficacy-tested procedures; verified exemplars; bounded teaching queues | bounded primary-source teaching tasks when derivative artifacts cannot support explanation integrity | lesson module; curriculum unit; drill set; teaching note; explanatory sequence | Transcendence for strategic pedagogy and meta-pattern review | ambient raw feed consumption; hidden verification intake; runtime raw-intake directories |
| Transcendence | downstream meta-governance authority | cross-chain telemetry; Coherence synthesis dossiers; Efficacy outcomes and retros; Mastery curricula and teaching outcomes | rare high-value primary-source escalations explicitly marked for meta-review | meta-pattern report; strategic review; doctrine-pressure signal; phase-transition readout | Acumen only through priority or governance feedback, not by bypassing intake law | standing raw intake lane; chain-local feed polling; runtime raw-intake directories |

## Default Route

The default route remains:

`captured manifest -> Acumen intake and triage -> derivative downstream artifacts -> Coherence / Efficacy / Mastery / Transcendence specialization`

Later chains should consume derivative artifacts, not raw intake streams.

## Runtime Boundary

This matrix does not authorize raw-intake runtime directories for later chains.

Disallowed default surfaces:

- `runtime/coherence/intake/`
- `runtime/efficacy/intake/`
- `runtime/mastery/intake/`
- `runtime/transcendence/intake/`

## Escalation Rule

When derivative artifacts are insufficient, Acumen or an Acumen-linked repo-side assessment may escalate a bounded source-near artifact to a later chain.
That escalation must name the reason the derivative layer was insufficient.
It does not convert the receiving chain into a standing intake authority.
