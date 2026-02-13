---
id: REF-CLARESCENCE_RUNBOOK
kind: REF
scope: system
target: syncrescendence
status: canonical
version: 2.0.0
updated: 2026-02-10
---

# /claresce — Clarescence Runbook v2.0.0

> **Clarescence** is the value-guided progressive refinement meta-operation (Rosetta #169).
> It is the culmination of every operational insight, hard-won lesson, and accumulated wisdom
> from the development of Syncrescendence — distilled into a repeatable, rigorous procedure
> that any agent in the Constellation can execute to converge on the best path forward.

Clarescence is not merely analysis. It is the act of making something *clear that was not* —
of taking a decision space clouded by drift, coupling, ambiguity, or stale assumptions and
**comprehensively** illuminating it until only one path remains defensible. Every pass is
designed to eliminate a category of blindness. Every output is an artifact committed to the
repository, because claims without receipts are not claims at all.

---

## Core Principles

These principles are not aspirational. They are load-bearing walls learned through operational
failure and recovery across 20+ sessions of multi-agent coordination:

1. **Orient before acting** — No pass produces output until the operator has oriented to the
   current state of the repository, the active intentions, and the strategic destination.
   Misorientation is the root cause of most wasted work.

2. **Situate every decision** — Every decision exists in a web of dependencies, tier couplings,
   and agent responsibilities. A decision made in isolation is a decision made blind. Situate
   the decision in its full operational context before evaluating it.

3. **Calibrate against ground truth** — The repository is ground truth. When a platform state
   conflicts with what the repo says, the repo wins. When a memory conflicts with what `git log`
   says, `git log` wins. Calibrate every claim against verifiable artifacts.

4. **Verify meticulously** — Never claim convergence without running verification. No completion
   without committed artifacts. No "I checked" without grep output. This is Invariant #3
   (Receipts / Closure Gate) applied to the decision process itself.

5. **Reason rigorously** — Every convergent path must have a falsifier: a concrete condition
   that, if true, would invalidate the recommendation. Analysis without falsifiers is advocacy,
   not reasoning.

6. **Execute, don't elaborate** — The anti-pattern that has cost more cycles than any other:
   producing beautiful analysis that never becomes action. Every clarescence must terminate in
   either a DecisionAtom (binding choice) or a staged backlog entry (deferred choice). Infinite
   refinement is a failure mode.

---

## When to Invoke

Invoke **/claresce** whenever you encounter a decision that:

- Changes a **truth surface** (what is canonical)
- Changes **lifecycle semantics** (what "done" / "claimed" / "blocked" means)
- Affects **automation** (watchers, hooks, cron, launchd agents)
- Affects **sovereignty or portability** (lock-in risk, vendor coupling)
- Adds or changes **interfaces** across agents, tools, or platforms
- Resolves a **SOVEREIGN decision** that gates downstream work
- Involves **tier coupling** (T0↔T1a, T1a↔T2, T2↔T3 linkage changes)
- Creates **irreversible state** (schema migrations, key rotations, API contracts)

### Fidelity Levels

| Level | Passes | When | Duration |
|-------|--------|------|----------|
| **Tactical** | 1–3 | Local decisions, low blast radius, easily reversible | 5–15 min |
| **Operational** | 1–7 | Cross-domain decisions, moderate coupling, staged rollback | 15–45 min |
| **Strategic** | 1–10 | Substrate-affecting, irreversible coupling, architectural | 45–120 min |

Default to **Tactical** unless the decision touches the substrate (σ-7) or creates coupling
that survives session boundaries.

---

## Phase 0: Orient and Situate

Before running any passes, the operator must orient to the current state and situate the
decision in its operational context. This is not optional.

### 0a. Orient

1. **Read the Triumvirate**: CLAUDE.md (loaded), COCKPIT.md, ARCH-INTENTION_COMPASS.md
2. **Check ground truth**: `git status`, `git log --oneline -5`
3. **Scan inbox**: `-INBOX/commander/00-INBOX0/` for pending tasks or completion signals
4. **Note active urgencies**: What intentions are marked P0? What SOVEREIGN decisions are pending?

### 0b. Situate

1. **Identify the decision's tier**: Is this T0 (strategic), T1a (operational-repo), T1b (operational-external), T2 (sprint), or T3 (session)?
2. **Map dependencies**: What does this decision block? What blocks this decision?
3. **Identify affected agents**: Which Constellation members are impacted?
4. **Check for prior clarescence**: Search `00-ORCHESTRATION/state/impl/clarescence/` — has this been claresced before? If so, what changed?

### 0c. Gather Inputs (Minimum Viable Packet)

- **Topic**: What decision or path is being claresced
- **Current state**: Relevant files, observed drift, conflicts
- **Options**: Available paths (if not self-evident from analysis)
- **Constraints**: Time, energy, cost, token budget, policies

---

## The 10-Pass Procedure

For each pass, write **1–5 bullets max** (digestible). Only expand where the pass reveals
conflict or drift. Brevity is a virtue; thoroughness is in the *coverage*, not the word count.

### Pass 1: Triumvirate Calibration

Calibrate the decision against the three coordinates of strategic alignment:

- **Destination**: Where are we headed? Does this decision move toward or away from the
  active intentions (INT-* vectors)? Check ARCH-INTENTION_COMPASS.md.
- **Current state**: What is the verified ground truth? Not what we *think* the state is —
  what `git status`, `grep`, and file reads actually confirm.
- **Fit-to-destination verdict**: Does this decision close the gap between current state
  and destination, or does it create a new gap?

*This is the equivalent of Commander's Intent + OODA Orient. If Pass 1 fails — if the
decision doesn't fit the destination — stop. Reframe the problem before continuing.*

### Pass 2: Lens Sweep (18+)

Run the decision through the operational lens battery. Score each lens pass/fail:

1. Sovereignty (does it preserve optionality?)
2. Portability (can we leave if needed?)
3. Durability (will this survive session boundaries?)
4. Reversibility (can we undo this?)
5. Atomicity (is it a single coherent change?)
6. Verifiability (can we prove it worked?)
7. Delegability (can another agent execute this?)
8. Composability (does it combine cleanly with other work?)
9. Observability (can we tell if it breaks?)
10. Token economy (is the context cost justified?)
11. Energy sustainability (can the Sovereign sustain this?)
12. Coupling risk (does it create hidden dependencies?)
13. Semantic clarity (is the terminology unambiguous?)
14. Canon alignment (does CANON support or contradict?)
15. Tier coherence (does it strengthen or weaken tier coupling?)
16. Agent compatibility (does it work with current Constellation capabilities?)
17. Automation potential (can this be automated once proven?)
18. Narrative fit (does it align with the project's identity and DNA?)

**Target**: >=12/18 passing. If <10/18, the decision needs reframing.

### Pass 3: CANON Coherence

- What do the canonical documents (01-CANON/) say about this domain?
- Where does observed reality diverge from what CANON claims?
- Is the drift in the decision, in CANON, or in both?
- **Action**: If CANON is stale, flag for update. If the decision contradicts CANON,
  justify the contradiction or change the decision.

### Pass 4: Omni-Qualities

Evaluate impact on the four systemic qualities:

- **Omniscience**: Does this improve or degrade the system's ability to *know* its own state?
- **Omnipresence**: Does this improve or degrade the system's reach across platforms/machines?
- **Omnipotence**: Does this improve or degrade the system's ability to *act* autonomously?
- **Omnibenevolence**: Does this improve or degrade the system's alignment with Sovereign values?

### Pass 5: Five Faces

Evaluate alignment with the five ontological faces:

- **Sensing** (σ₀–σ₁): Does this improve the system's ability to perceive?
- **Meaning** (σ₂–σ₃): Does this improve the system's ability to interpret?
- **Intention** (σ₄): Does this align with declared intentions?
- **Embodiment** (σ₅–σ₆): Does this manifest concretely in running systems?
- **Harmony** (σ₇): Does this integrate cleanly with the whole?

### Pass 6: Rosetta Precision

- Are all terms used in this decision defined in REF-ROSETTA_STONE.md?
- Do the terms mean what we think they mean, or has semantic drift occurred?
- **Action**: If any term is ambiguous, resolve it here. Propose Rosetta updates if needed.

### Pass 7: Backlog Coherence

- What does this decision **unblock** in IMPLEMENTATION-MAP.md?
- What new tasks does it **create**?
- What existing tasks does it **invalidate or modify**?
- What is the net impact on T1a↔T2 coupling health?
- **Priority assessment**: Where does the unblocked work sit in the priority stack?

### Pass 8: nth-Order Effects

- **First order**: What changes directly?
- **Second order**: What changes because of those changes?
- **Third order**: What new dependencies or failure modes appear?
- **Compounding**: Does this compound positively with other recent decisions, or does it
  create interference patterns?

### Pass 9: Energy State

- Is it sustainable to implement this now, given current Sovereign energy and agent availability?
- What is the token cost of implementation?
- What is the opportunity cost (what *doesn't* get done if we do this)?
- **If unsustainable**: Stage it. Create a backlog entry with clear activation criteria.

### Pass 10: Authenticity Gate

The final gate. This is not analytical — it is existential:

- Does this preserve sovereignty and optionality?
- Does this align with what the Sovereign *actually values*, not what the system *says* they value?
- Would the Sovereign at peak clarity — fully rested, fully informed, fully present — approve this?
- **If no**: Stop. The analysis has drifted from values into optimization theater.

---

## Epistemic Rigor

Every clarescence must include explicit epistemic markers. Analysis without confidence
levels is advocacy disguised as reasoning.

### Confidence Levels

| Level | Meaning | Basis |
|-------|---------|-------|
| **High (>85%)** | Strong evidence, multiple confirming signals | Grep-verified, git-confirmed, cross-referenced |
| **Medium (60–85%)** | Reasonable inference, some uncertainty | Pattern-based, partially verified |
| **Low (<60%)** | Speculative, limited data | Single-source, unverified assumption |

### Falsifier Methodology

For every convergent path, state the **falsifier**: a concrete, testable condition that,
if true, would invalidate the recommendation. A recommendation without a falsifier is
an opinion, not a conclusion.

Format:
```
Falsifier: If [condition], then [this recommendation is wrong] because [reason].
Test: [How to check if the falsifier is true]
```

---

## Anti-Patterns (Learned Through Failure)

These anti-patterns have been identified across 20+ operational sessions. Each has cost
real cycles and real progress:

| Anti-Pattern | Symptom | Correction |
|---|---|---|
| **Elaboration over execution** | Beautiful analysis, no artifacts committed | Every pass must produce either a decision or a staged task |
| **Aspiration masquerading as state** | "The system can do X" when no agent has done X | Verify claims with `grep`, `git log`, actual tool invocation |
| **Tier coupling blindness** | Decisions made in one tier without checking impact on others | Pass 7 (Backlog Coherence) is mandatory, not optional |
| **Semantic drift tolerance** | Using terms loosely, creating confusion across agents | Pass 6 (Rosetta Precision) catches this; fix terms before proceeding |
| **Infinite refinement** | Running passes 1–10 repeatedly without converging | Set a pass limit at invocation. If passes 1–3 don't converge, escalate to Sovereign |
| **Verification theater** | "I verified" without showing the verification output | Show the grep, show the git status, show the file read |
| **Solo analysis of shared decisions** | Clarescing a multi-agent decision without consulting affected agents | Check agent availability; dispatch to affected agents for input if operational |

---

## Constitutional Constraints (Non-Negotiable)

Every clarescence operates within the Five Invariants. These cannot be suspended,
overridden, or traded away — even if the analysis suggests otherwise:

1. **Objective Lock** — No work begins until the objective is explicitly confirmed.
2. **Translation Layer** — All outputs must be intelligible without retransmission.
3. **Receipts** — No completion claim without committed artifacts.
4. **Continuation/Deletability** — Any conversation must be deletable without losing state.
5. **Repo Sovereignty** — The repository is ground truth; platforms are cache.

---

## Output Artifacts

### 1. Clarescence Record

Write one record per claresced decision to:
`00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-YYYY-MM-DD-<slug>.md`

### 2. DecisionAtom (if a binding decision is made)

Produce a DecisionAtom with:
- Decision statement (one sentence, unambiguous)
- Canonical truth surface (what becomes ground truth and where it lives)
- Reversibility + rollback path
- Falsifier
- Confidence level

### 3. Backlog and Ledger Updates

- Add/adjust implementation tasks in `IMPLEMENTATION-MAP.md` and/or `IMPLEMENTATION-BACKLOG.md`
- Append to `DYN-GLOBAL_LEDGER.md` with event `DECISION`
- Update T1a (Linear) if the decision affects tracked issues

---

## Standard Output Format

```
CLARESCENCE: <topic>
Date: YYYY-MM-DD
Fidelity: tactical | operational | strategic
Passes run: 1-3 | 1-7 | 1-10
Convergent Path: <single best path, one sentence>
Rationale (digest): <3-7 bullets>
Dependencies created/updated: <IMPL-IDs, SYN-IDs>
Falsifier: <what would make this wrong>
Confidence: low | medium | high (with percentage)
Energy cost: <estimated tokens/time to implement>
```

---

## Clarescence Record Template

```markdown
# CLARESCENCE: <topic>

**Date**: YYYY-MM-DD
**Fidelity**: tactical | operational | strategic
**Passes run**: 1-3 | 1-7 | 1-10
**Owner**: <Sovereign | Psyche | Ajna | Commander | Adjudicator | Cartographer>

---

## Convergent Path

<one paragraph — the single recommendation>

## Digest Rationale

- <bullet 1>
- <bullet 2>
- ...

## Falsifier

<what would make this wrong>
<how to test it>

## Confidence

<low | medium | high> (<percentage>) — <basis for confidence level>

## Dependencies / Tasks Touched

- <IMPL-ID or SYN-ID>: <impact>

---

## Pass Notes

### Phase 0 — Orient & Situate
- Oriented to:
- Situated in tier:
- Prior clarescence:

### Pass 1 — Triumvirate Calibration
- Destination:
- Current state:
- Fit verdict:

### Pass 2 — Lens Sweep
- Passes: <list>
- Fails: <list>
- Score: /18

### Pass 3 — CANON Coherence
- Canon says:
- Drift:
- Action:

### Pass 4 — Omni-Qualities

### Pass 5 — Five Faces

### Pass 6 — Rosetta Precision

### Pass 7 — Backlog Coherence
- Unblocks:
- Creates:
- Net T1a↔T2 impact:

### Pass 8 — nth-Order Effects

### Pass 9 — Energy State

### Pass 10 — Authenticity Gate
```

---

## Substrate Triggers (Auto-Claresce)

These categories require automatic clarescence when encountered during any operation:

- **Schema changes**: Any modification to SQLite tables, Qdrant collections, or Neo4j graph structure
- **Tier boundary changes**: Any modification to how T0↔T1a↔T1b↔T2↔T3 communicate
- **Agent capability changes**: Any change to what an agent can or cannot do
- **Automation changes**: Any change to launchd agents, hooks, cron tasks, or watchdog behavior
- **Key rotation or credential changes**: Any security-sensitive state change
- **Canon modifications**: Any change to 01-CANON/ content (protected zone)
- **Irreversible coupling**: Any decision that cannot be undone without significant rework

---

## Evolution History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-04 | Initial draft — 10-pass procedure, basic templates |
| 2.0.0 | 2026-02-10 | Canonical release — Phase 0 (orient/situate), 3-tier fidelity, 18-lens battery, epistemic rigor (falsifiers + confidence), anti-patterns from CLARESCE^3 v1+v2, constitutional constraints, substrate triggers, operational wisdom integration |
