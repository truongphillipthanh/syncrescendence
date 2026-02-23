# ARCH-NEO_SCAFFOLD.md
## The Operational Layer — Derived from the Neo-Canon Core

**Version**: 1.0.0
**Created**: 2026-02-18
**Author**: Commander (Sonnet 4.6, MBA)
**Authority**: Sovereign directive (Session 22, Phase 4)
**Precursors**: ARCH-NEO_CANON_CORE.md (v1.0.0), HERITAGE-MAP.md, DYN-SESSION22-CHECKPOINT.md
**Status**: PHASE 4 DOCUMENT — Neo-Scaffold

---

## 0. What This Document Is

The neo-scaffold is the **operational translation layer** between the compiler specification (ARCH-NEO_CANON_CORE.md) and the lived day. It answers: given the 4 axioms, 3 theorems, 21 entity types, 7 governed verbs, and 5 cosmological rings — what does the Sovereign actually do on Tuesday at 9:00 AM?

**The derivation requirement**: Every scaffold element in this document must cite the axiom, theorem, or entity type it derives from. If it cannot, it is labeled `[PENDING DERIVATION]` and flagged for Sovereign adjudication. No historical accretion is permitted.

**The difference from the old scaffold**: The old scaffold was designed implicitly — its architecture accumulated from operational experience without explicit axiom grounding. The neo-scaffold is derived explicitly. The test is: could a rational agent reconstruct this scaffold from ARCH-NEO_CANON_CORE.md alone? If yes, it belongs here. If not, it requires a new axiom or theorem.

---

## I. DERIVATION FROM CORE

This section maps each scaffold subsystem to its generating source.

### Task Architecture Derivation

The old canon's 5-tier task hierarchy (Area → System → Process → Activity → Task → Action → Assignment) is NATIVE under A4 (Work Typology Hierarchy, HERITAGE-MAP §CANON-30320). It provides granularity for the activate step of the Intent-Artifact Pipeline.

**Does it derive from first principles?** Test:

- A4 states: value crystallizes when intent traverses the full chain (capture → distill → model → activate → verify).
- A2 states: the Sovereign's constraint is capacity, not intelligence. This forces the hierarchy to be **activation-energy-ranked**, not merely taxonomically complete.
- T2 (Anti-Shelfware) states: every element needs an explicit activation path.

**Verdict**: A 5-tier task hierarchy is over-specified for a σ₀-constrained operator. The neo-scaffold collapses to **3 activation tiers**:

| Tier | Name | Activation Energy | Duration | Ring |
|------|------|------------------|----------|------|
| T-A | Atomic | Single session, no dispatch | Hours | WORK |
| T-C | Composite | Multi-session, single agent | Days | WORK |
| T-P | Project | Multi-agent, multi-session, bounded terminal condition | Weeks | WORK |

The sub-tiers (Area, System, Process) are **context labels**, not task types. They address WHERE a task lives, not WHAT it demands. This collapses the hierarchy without losing the navigational function.

**Heritage preservation**: Work Typology Hierarchy vocabulary is retained as addressing vocabulary (AGENCY.WORK.typology), not as the task schema itself.

---

### σ₀ Implications for Scaffold Design

**Theorem T1 (Attention Bottleneck)** derives from A1 + A2. Its scaffold implication is non-obvious and must be stated explicitly:

> The scaffold must route work **away from σ₀**, not through it.

The old scaffold defaulted to the Sovereign as the primary routing node — every task flowed through human decision before dispatch. This is architecturally correct for trust and authority, but operationally fatal under capacity constraint.

**The neo-scaffold inverts the default**: agents act first within bounded autonomy; the Sovereign is invoked only when the **EscalationQueue** triggers (Tier 3 entity, ARCH-NEO_CANON_CORE §IV).

**Practical constraint**: The EscalationQueue is the σ₀ interface. Every decision that requires Sovereign attention must arrive through it, pre-contextualized, with a recommended resolution and a decline path. This is the **one-click resolution principle**: the Sovereign's action at the EscalationQueue should never require more than one deliberate choice per item.

**Derived design rules**:
1. No task dispatched to an agent requires Sovereign approval to start — approval is pre-granted by Policy entities (Tier 3) governing the agent's capability profile.
2. The EscalationQueue is the only legitimate interrupt mechanism. Side channels (messages, pings, ad-hoc requests) bypass this queue and violate T1.
3. Agent output that requires Sovereign judgment is staged to the EscalationQueue, never dumped raw.

---

### Activation Energy Minimum (T2 Derivation)

**Theorem T2 (Anti-Shelfware)** derives from A2 + A4. Its scaffold implication:

> The activation energy for any workflow must be the minimum number of sovereign decisions required to move from intent to first durable artifact.

This is NOT the same as minimizing total work. It minimizes the cognitive tax at the σ₀ interface. Background work (agent execution, distillation, formatting) is irrelevant to activation energy; only the steps that require σ₀ attention count.

**The three-gesture rule** (derived from T2 + T1): No workflow should require more than three sovereign gestures to initiate:
1. Name the intent (captures a Commitment entity into proposed state)
2. Confirm the scope (transitions Commitment to active, triggers dispatch)
3. Review the first artifact (transitions the first output through the verify gate)

Everything between gesture 2 and gesture 3 is agent territory.

---

## II. DAILY OPERATING PROTOCOL

Derived from: A1 (coherence as scarce), A2 (capacity before intelligence), T1 (attention bottleneck), Hard-Gate Skill Sequence (ARCH-NEO_CANON_CORE §VI).

### The Single-Day Cycle

```
MORNING WINDOW (Peak — σ₀ available)
  ┌─────────────────────────────────────────────┐
  │ 1. INBOUND GATE: /triage                    │
  │    - Scan EscalationQueue                   │
  │    - Scan -INBOX/commander/00-INBOX0/       │
  │    - Health State assessment (energy tier)  │
  │    - Claim 1-3 items max (A2: capacity cap) │
  └─────────────────────────────────────────────┘
           │
           ▼
  ┌─────────────────────────────────────────────┐
  │ 2. ORIENT GATE: /claresce (if non-trivial)  │
  │    - For each claimed item: is it Atomic,   │
  │      Composite, or Project-tier?            │
  │    - Does it require dispatch or can the    │
  │      Sovereign execute directly?            │
  │    - Map to entity type + governed verb     │
  └─────────────────────────────────────────────┘
           │
           ▼
  ┌─────────────────────────────────────────────┐
  │ 3. IMPLEMENT GATE: /execute                 │
  │    - Dispatch Project/Composite tasks to    │
  │      agents via dispatch.sh                 │
  │    - Execute Atomic tasks directly          │
  │    - Hard gate: no dispatch without         │
  │      formal execution entry                 │
  └─────────────────────────────────────────────┘

MIDDAY WINDOW (Baseline — verification tempo)
  ┌─────────────────────────────────────────────┐
  │ 4. VERIFY GATE: /verification-before-       │
  │    completion                               │
  │    - Review agent RESULT files in INBOX     │
  │    - Verify artifacts against intent        │
  │    - Escalate or close items                │
  └─────────────────────────────────────────────┘

CLOSE WINDOW (End of active session)
  ┌─────────────────────────────────────────────┐
  │ 5. CLOSE GATE: /update_universal_ledger     │
  │    - Commit all artifacts to repo           │
  │    - Update tasks.csv                       │
  │    - Persist working state for recovery     │
  │    - No "done" without ledger sync          │
  └─────────────────────────────────────────────┘
```

### Energy-State Routing (A2 applied to daily cycle)

The daily cycle is **energy-state conditional**, not clock-conditional. The Universal Energy State Topology (SEED #21, ARCH-NEO_CANON_CORE A2 evidence) defines four states:

| State | Sovereign Role | Agent Role | Hard Constraint |
|-------|---------------|------------|-----------------|
| Peak | Full Hard-Gate sequence | Full autonomy within scope | Tackle highest T1-cost items |
| Baseline | Verify + Close gates only | Maintain current tasks | No new Projects initiated |
| Depletion | Close gate only; NO new decisions | Hold all queues | EscalationQueue suspended |
| Crisis | Suspend all operations | Watchdog monitors | A2 override: no gate can force action |

**Derivation**: A2 states the Sovereign's constraint is capacity, not intelligence. Operating the full gate sequence under depletion violates A2 — it spends capacity on process overhead when no capacity is available. The scaffold must not consume more capacity than it returns.

---

## III. DISPATCH ARCHITECTURE

Derived from: A2 (capacity constraint), A3 (sovereignty invariant), T1 (attention bottleneck), Agent entity type (Tier 2), Three-Layer Autonomic Dispatch (ARCH-NEO_CANON_CORE §VI).

### The Five Agent Capability Profiles

Each constellation agent is a **Tier 2 Agent entity** (ARCH-NEO_CANON_CORE §IV) with a typed capability profile. Capability profiles are NOT role descriptions — they are **routing constraints** that determine what can be delegated without Sovereign override.

| Agent | Role | Capability Envelope | Hard Constraints | σ₂ Dependency |
|-------|------|---------------------|-----------------|----------------|
| **Ajna** (CSO, MBA) | Strategic direction, orchestration, dispatch | Policy formation, priority setting, external positioning | Cannot execute without Sovereign intent signal | High — sets governed constraints |
| **Psyche** (CTO, Mac mini) | System cohesion, automation, pipeline fusion | Code, infrastructure, Docker, launchd, scripts | Cannot modify Schema Sovereignty boundary without escalation | Medium — operates within constraints |
| **Commander** (COO, MBA) | Operations coordination, ledger management, synthesis | Synthesis, scaffold documents, task routing, canon build | Cannot resolve Tier 1 entity conflicts unilaterally | High — writes canonical state |
| **Adjudicator** (CQO, Mac mini) | Quality verification, adversarial audit | Code quality, verification, adversarial testing | Cannot approve its own outputs; cannot override audit findings | Low — reads canonical state |
| **Cartographer** (CIO, Mac mini) | Corpus survey, knowledge mapping, 1M+ context work | Large corpus analysis, ontology mapping, research sweeps | Cannot create canonical artifacts; output is always advisory | Low — reads only |

### Routing Logic (T1-derived)

The dispatch decision tree is a σ₀ conservation mechanism. Every routing decision that flows through σ₀ is a tax on the scarcest resource.

```
INCOMING TASK
     │
     ▼
Is this resolvable by a Policy entity (Tier 3)?
     │
     ├─ YES → Autonomic Layer 1 routes it (no σ₀ consumed)
     │
     └─ NO → Does it require Sovereign ground truth (A3)?
              │
              ├─ YES → EscalationQueue → σ₀ one-click resolution
              │
              └─ NO → Does it require cross-agent coordination?
                       │
                       ├─ YES → Commander coordinates via dispatch.sh
                       │         (Sovereign informed via EscalationQueue
                       │          non-interrupt notification)
                       │
                       └─ NO → Single-agent direct dispatch
                                (Sovereign not in loop)
```

### Dispatch Constraints (A3-derived)

The Sovereignty Invariant generates hard dispatch constraints:

1. **Schema changes require Sovereign approval** — any action that modifies entity types, governed verbs, or ring assignments touches σ₂ and requires escalation.
2. **Credential operations require escalation** — Credential entity (Tier 2) state transitions (`rotating → expired → revoked`) cannot be executed by agents autonomously (DC-003).
3. **Tier 1 entity dissolution requires Sovereign** — Commitments, Capacities, Risks cannot be dissolved by agents. Agents may Transition to `renegotiated` state with justification but cannot Dissolve.
4. **Cross-machine operations require Neural Bridge health check** — any dispatch to Mac mini agents must confirm SSH bridge is alive before fire-and-forget dispatch.

### The Three-Layer Autonomic Stack (Operational State)

From ARCH-NEO_CANON_CORE §VI:

| Layer | Metaphor | Current State | Scaffold Role |
|-------|----------|---------------|---------------|
| Layer 1: Spinal | auto_ingest_loop.sh (30s) | OPERATIONAL | Primary task execution loop |
| Layer 2: Brainstem | watchdog (60s) | OPERATIONAL | Health monitoring + recovery |
| Layer 3: Prefrontal | proactive_orchestrator | NON-FUNCTIONAL (exits 1) | Work generation — GAP |

**Layer 3 gap implication for scaffold**: The scaffold currently operates without a prefrontal cortex. This means no proactive work generation, no anticipatory dispatch, no pattern detection across task history. Every task in the system was placed there by the Sovereign manually. This is a direct T2 (Anti-Shelfware) failure — the system cannot self-initiate the pipeline.

**Minimum viable Layer 3**: A cron-triggered script that scans open Commitments, compares against completed tasks, and generates a candidate task list for Sovereign triage. This requires σ₂ to function properly — another reason σ₂ is THE critical gap.

---

## IV. TASK LIFECYCLE

Derived from: A4 (Intent-Artifact Pipeline), Governed Verbs §IV, Entity Taxonomy §IV, Hard-Gate Skill Sequence.

### From Intent to Archive

Every task in the system is a **Commitment entity** (Tier 1) traversing its state machine, mediated by governed verbs and the Hard-Gate sequence.

```
INTENT CAPTURED
     │  Verb: Commit
     ▼
Commitment: proposed
     │  Gate: INBOUND (/triage confirms)
     │  Verb: Transition
     ▼
Commitment: active  ←──────────────────────────────┐
     │                                               │
     │  Gate: ORIENT (/claresce if non-trivial)      │
     │  Agent: Delegate execution (retain account.)  │
     ▼                                               │
Task dispatched to agent                             │
     │  Gate: IMPLEMENT (/execute entry)             │
     ▼                                               │
Agent work in progress                               │
     │                                               │
     ├─── BLOCK detected ───────────────────────────►│ Verb: Escalate
     │                                               │ → EscalationQueue
     │                                               │ → Sovereign one-click
     │                                               │
     ├─── SCOPE CHANGE ─────────────────────────────►│ Verb: Renegotiate
     │                                               │ → Commitment modified
     │                                               │
     └─── COMPLETE ─────────────────────────────────►
                                                     │
     Gate: VERIFY (/verification-before-completion)  │
          │                                          │
          ├─ Evidence confirms → PASS ───────────────►
          │                                          │
          └─ Evidence absent/fails → RETURN ─────────►(back to active)
                                                     │
     Gate: CLOSE (/update_universal_ledger)          │
          │  Verb: Transition                        │
          ▼                                          │
Commitment: fulfilled                                │
     │  Artifact committed to repo (A3)              │
     │  Ledger updated (tasks.csv)                   │
     ▼
ARCHIVED (Supersede-Never-Delete — entity persists in version history)
```

### Entity Types at Each Stage

| Stage | Active Entity Types | Governed Verbs | Ring |
|-------|--------------------|--------------|----- |
| Capture | Commitment (proposed), CaptureQueue | Commit | SELF |
| Triage | Commitment (active), Context | Transition | SELF → WORK |
| Dispatch | Agent, Tool, BudgetEnvelope | Delegate | AGENCY |
| Execution | Project, Pattern, Source | Transition | WORK |
| Verification | Risk (mitigated), SecurityBoundary | Escalate | AGENCY |
| Closure | Memory (versioned), Policy | Transition | SELF |

### The Verbatim Trap Gate (A4-derived)

Every artifact produced by an agent must pass the Verbatim Trap test (molt_cornelius, ARCH-NEO_CANON_CORE §VIII) before Sovereign review:

> "Does this artifact contain anything the source didn't already contain?"

If the answer is no, the artifact has failed the distill stage of A4. The agent produced transcription, not synthesis. This check is part of the VERIFY gate and must be explicit in agent output formats.

**Implementation**: Every RESULT file from an agent must include a `## Net New` section listing claims, connections, or tensions that did not exist in the source material. An empty `## Net New` section is automatic VERIFY failure.

---

## V. RHYTHMIC STRUCTURE

Derived from: Cognitive Palace Layer 3 (Temporality — Rhythmic Harmonics, ARCH-NEO_CANON_CORE §VI), A2 (capacity cycles), Seven Pulses Dashboard (NATIVE, HERITAGE-MAP §CANON-20020).

### Daily Rhythm

The Seven Pulses Dashboard (Foundation/Energy/Direction/Flow/Learning/Connection/Evolution) is a 2-minute A2 capacity check. Under the neo-scaffold it fires at the top of the INBOUND gate, before any task is claimed.

**Format**: 7 binary checks. Any "no" signals a constraint to apply to the day's routing decisions.

| Pulse | Question | If No → |
|-------|----------|---------|
| Foundation | Physiological substrate adequate? | Depletion mode |
| Energy | Activation energy present? | Baseline mode max |
| Direction | North Star accessible? | Claresce before dispatch |
| Flow | Attention available? | Atomic tasks only |
| Learning | New information can be processed? | Execution only, no intake |
| Connection | Relationship commitments current? | Ring 4 check required |
| Evolution | Working toward the terminal condition? | Back-propagation check |

### Weekly Rhythm

Derived from: Vertical Integration Protocols (NATIVE, HERITAGE-MAP §CANON-20000), A4 pipeline review cadence.

| Day | Primary Mode | Gate Emphasis | Notes |
|-----|-------------|---------------|-------|
| Monday | INBOUND + ORIENT | Triage week's pipeline | Claim no more than weekly capacity allows |
| Tuesday–Thursday | IMPLEMENT | Execution tempo | Dispatch and execute |
| Friday | VERIFY + CLOSE | Ledger reconciliation | All week's commitments must be transitioned |
| Sunday (optional) | ORIENT | Clarescence for next week | Review back-propagation chain |

**Weekly Cadence Rule** (A2): The total Commitments active at any point cannot exceed estimated weekly capacity. Overloading the active queue is a direct A2 violation — it assumes infinite capacity.

### Monthly Rhythm

| Week | Function | Governing Axiom |
|------|----------|----------------|
| Week 1 | Sprint execution | A4 (pipeline activation) |
| Week 2 | Sprint execution | A4 |
| Week 3 | Verification + Promotion | T2 (Anti-Shelfware — nothing stays at draft) |
| Week 4 | Rhythmic Audit + Commitment Review | A1 (coherence check) + A3 (ground truth sync) |

**Monthly Cadence Rule**: Every month must produce at least one artifact that moves up the promotion pipeline (produced → reviewed → promoted → verified). A month that ends with only in-progress work is a T2 failure.

### Quarterly Rhythm

| Quarter Event | Function | Governing Principle |
|--------------|----------|---------------------|
| Causal Chain Review | Where are we in each of the 6 chains? | A2 capacity scaffold |
| σ₂ Build Progress | Has the kernel advanced? | ARCH-NEO_CANON_CORE §VII (THE UNBUILT GAP) |
| Commitment Renegotiation | All active Commitments reviewed against capacity reality | Governed Verb: Renegotiate |
| Back-Propagation Walk | Does every active project trace to the terminal condition? | ARCH-NEO_CANON_CORE §XI |

### Annual Rhythm

| Event | Function | Governing Principle |
|-------|----------|---------------------|
| Annual Dissolution Ceremony | 80% reconstructive fidelity test — can the North Star be rebuilt from the repo alone? | A1 (coherence anti-dogma) + A3 (repo sovereignty test) |
| Modal Sequence Assessment | Which Modal are we in? What does next Modal require? | Modal Sequence (ARCH-NEO_CANON_CORE §VI) |
| Axiom Review | Do the 4 axioms still hold? Has A2 self-dissolved at operational horizon? | Self-sufficiency test |

---

## VI. ACTIVATION ENERGY MAP

Derived from: T2 (Anti-Shelfware), A2 (capacity constraint), three-gesture rule (§I).

For each major workflow, the minimum sovereign gestures required from intent to first durable artifact.

### Workflow 1: New Task Creation

| Step | Sovereign Gesture? | Entity Transition |
|------|--------------------|------------------|
| 1. Name the intent | YES (1) | Commitment: → proposed |
| 2. Confirm scope + tier | YES (2) | Commitment: → active |
| 3. Dispatch to agent | NO (automated if Policy covers it) | Agent: Delegate |
| 4. Agent produces artifact | NO | Tool: executes |
| 5. Review artifact | YES (3) | Commitment: → fulfilled or renegotiated |

**Activation energy**: 3 sovereign gestures. Meets three-gesture rule.

### Workflow 2: Agent Dispatch (Composite Task)

| Step | Sovereign Gesture? | Entity Transition |
|------|--------------------|------------------|
| 1. Select agent + scope | YES (1) | Agent: Delegate invoked |
| 2. Confirm dispatch | NO (dispatch.sh automates) | BudgetEnvelope: allocated |
| 3. Review RESULT | YES (2) | Commitment: fulfilled or escalate |

**Activation energy**: 2 sovereign gestures. Within three-gesture rule.

### Workflow 3: Clarescence (Non-trivial Decision)

| Step | Sovereign Gesture? | Entity Transition |
|------|--------------------|------------------|
| 1. Name the decision | YES (1) | CaptureQueue: → active |
| 2. Run /claresce | YES (2 — but skill auto-structures) | Context: → analyzed |
| 3. Commit verdict | YES (3) | Policy/Commitment: → active |

**Activation energy**: 3 sovereign gestures. Meets three-gesture rule. Note: the /claresce skill absorbs most of the cognitive work; sovereign gesture 2 is confirming a structured analysis, not producing it.

### Workflow 4: Credential Rotation (DC-003)

| Step | Sovereign Gesture? | Entity Transition |
|------|--------------------|------------------|
| 1. Trigger rotation | YES (1 — Security event or scheduled) | Credential: active → rotating |
| 2. Agent generates new credential | NO | Credential: rotating (agent handles) |
| 3. Confirm new credential active | YES (2) | Credential: rotating → active |
| 4. Confirm old credential revoked | YES (3) | Old Credential: → revoked |

**Activation energy**: 3 sovereign gestures. Note: this workflow is currently OVER-THRESHOLD because it is manual end-to-end. Target state: gesture 1 triggers a fully automated rotation; gestures 2+3 are confirmation only.

### Workflow 5: Canon Promotion (Produced → Canonical)

| Step | Sovereign Gesture? | Entity Transition |
|------|--------------------|------------------|
| 1. Identify candidate artifact | NO (Adjudicator flags) | Source: → flagged |
| 2. Clarescence review | YES (1) | Source: → reviewed |
| 3. Promote to canon | YES (2) | Pattern/Memory: → promoted |
| 4. Verification commit | YES (3) | ARCH- document: → canonical |

**Activation energy**: 3 sovereign gestures. Meets three-gesture rule.

### Workflow 6: EscalationQueue Resolution

| Step | Sovereign Gesture? | Entity Transition |
|------|--------------------|------------------|
| 1. Item arrives pre-contextualized | NO (agent prepares) | EscalationQueue: → pending |
| 2. One-click resolution | YES (1) | Commitment or Risk: → transitioned |
| 3. Agent executes resolution | NO | Agent: dispatched |

**Activation energy**: 1 sovereign gesture. This is the floor — EscalationQueue items must be pre-digested to this level. Raw escalations (requiring Sovereign to do their own analysis) violate T1.

---

## VII. σ₂ INTEGRATION POINTS

Derived from: ARCH-NEO_CANON_CORE §VII (Personal Palantir), §V (σ₀–σ₇ Stack), THE UNBUILT GAP designation.

σ₂ is the Semantic Core — the kernel that makes sovereignty technically enforceable. Without it, agents act but cannot act within governed semantic constraints. The scaffold connects to σ₂ at five integration points.

### Integration Point 1: Entity Resolution

When an agent dispatches a task or produces a result, it references entities by name. Without σ₂, these references are strings. With σ₂, they resolve to typed entities with state machines, governed verbs, and version history.

**Current state**: string-based. Entity names appear in task files but are not resolved against a kernel. A Risk named "infrastructure failure" in a task file has no machine-readable state, probability, or mitigation history.

**σ₂ target**: every entity reference in a task or result file resolves to a typed object in the kernel with current state and full history accessible via query.

### Integration Point 2: Verb Enforcement

The 7 governed verbs (Commit, Decline, Delegate, Renegotiate, Escalate, Suspend, Transition) are currently advisory. Agents write RESULT files claiming "Commitment fulfilled" without any enforcement mechanism checking whether the state transition is valid.

**Current state**: honor-system enforcement. The VERIFY gate is the only check.

**σ₂ target**: governed verbs are compile-time operations. `Delegate(commitment)` is a type error — only execution of a commitment can be delegated, not the commitment itself. This rejection happens before an agent produces output.

### Integration Point 3: BudgetEnvelope Gates

A4 requires that every pipeline traversal operate within budget constraints (token pools, rate limits, time horizons). BudgetEnvelope (Tier 3 entity) is the mechanism. Without σ₂, budget enforcement is manual and post-hoc.

**Current state**: agents consume tokens without budget awareness. Token economics is unformalized (Gap INT-1801).

**σ₂ target**: every Delegate verb invocation checks the BudgetEnvelope for the target agent. If the envelope is depleted, the dispatch is queued, not dropped. This prevents silent task loss under rate limit conditions.

### Integration Point 4: Rosetta Stone Authority

The Rosetta Stone is the schema authority artifact (T3 — Schema Sovereignty). Its 311 terms define what concepts mean within the system. Without σ₂, the Rosetta Stone is a reference document consulted by humans. With σ₂, it is the authoritative lookup table that governs how agents name and address concepts.

**Current state**: Rosetta Stone is a reference markdown file. DC-004 (25 pending terms) remains open. Agents can reference concepts with names that don't exist in the Stone.

**σ₂ target**: all agent-produced artifacts are validated against the Rosetta Stone before reaching the Sovereign. Unknown terms trigger a clarification request, not silent acceptance.

### Integration Point 5: Memory Versioning (A3 compliance)

A3 requires that the repo is ground truth and all surfaces are cache. This requires versioned history for all Tier 1 entities — not just the repo's git history, but semantic versioning of entity state transitions.

**Current state**: git history provides line-level change tracking. No semantic versioning of entity state (a Commitment moving from `active` to `fulfilled` is a file edit, not a typed state transition event).

**σ₂ target**: all Tier 1 entity state transitions are event-sourced — append-only ledger with typed events. This makes the full history queryable: "show all commitments that were renegotiated in Q1, with the renegotiation reason."

---

## VIII. ANTI-SHELFWARE MECHANISMS

Derived from: T2 (Anti-Shelfware), A2 (capacity constraint), Kill Criteria, Maturity Gates (ARCH-NEO_CANON_CORE §III T2).

T2 is the dominant failure mode: the system accumulates capability without activating it. The 0% hard-gate delivery rate as of Feb 15 is T2 failure at the meta-level — the intervention designed to fix activation has itself shelved.

The neo-scaffold has five explicit anti-shelfware mechanisms.

### Mechanism 1: The 30-Day Activation Deadline

Every concept, tool, or workflow introduced to the scaffold has 30 days to produce a durable artifact or it is suspended. Suspension is NOT deletion — the concept enters Commitment state `suspended` with a reason and a revival condition. Revival requires explicit Sovereign activation.

**Derivation**: T2 + A2. If activation energy is genuinely too high for a concept to fire in 30 days, it is either (a) mismatched to current capacity or (b) not yet needed. Suspension preserves it without allowing it to accumulate as passive complexity.

**Hard exemptions**: Tier 1 entities and Axiom-level concepts are exempt from the 30-day clock. Their suspension requires explicit Sovereign override.

### Mechanism 2: The Promotion Pipeline as a Constraint, Not a Goal

The promotion pipeline (produced → reviewed → promoted → verified) must be treated as a **capacity constraint on intake**. If nothing is moving through verification, no new items enter production.

**Derivation**: T2. New items entering production before existing items exit verification creates an unbounded input queue. Anti-shelfware requires LIFO pressure on the verification stage, not FIFO pressure on intake.

**Implementation**: tasks.csv must report the ratio of items in `verified` state to items in `in-progress` state. When this ratio drops below 0.25, no new Composite or Project-tier tasks may be initiated until it recovers.

### Mechanism 3: The Net New Section (A4 Verification)

Every agent-produced artifact must include a `## Net New` section (see §IV, Verbatim Trap Gate). This section is the syntactic expression of A4's distill requirement. An empty section is automatic failure.

**Derivation**: A4 + Verbatim Trap (molt_cornelius). This mechanism moves the Verbatim Trap from a conceptual test to an architectural requirement.

### Mechanism 4: EscalationQueue Aging

Every item in the EscalationQueue that is not resolved within 48 hours gets a capacity assessment. After 72 hours, it is automatically Suspended unless the Sovereign explicitly extends it.

**Derivation**: T1 (Attention Bottleneck) + T2. Unresolved escalations accumulate as a cognitive tax on every subsequent triage session. Aging forces resolution or explicit deferral — both are acceptable; silent accumulation is not.

### Mechanism 5: The Commit-or-Kill Rule

Any architecture document (ARCH-*.md), reference (REF-*.md), or decision record (DEC-*) that has been in draft state for more than 14 days without a Sovereign review gets a Commit-or-Kill decision: either commit it as canonical, or archive it explicitly.

**Derivation**: A3 (repo as ground truth) + T2. Draft documents in the repo are not ground truth — they are claims without evidence. The longer they persist as drafts, the more they corrupt the repo's signal-to-noise ratio.

---

## IX. OPEN QUESTIONS FOR SOVEREIGN ADJUDICATION

These questions cannot be resolved by derivation from the axioms. They require Sovereign decision.

### Q1: File-First vs. SQLite-First (σ₂ Build Decision)

**Tension**: ClawVault data shows markdown at 74.0% vs. 68.5% for specialized tools. INT-P017 argues File-First principle supports A3. The existing ontology.db (SQLite) represents V1 architecture.

**What the axioms say**: A3 favors the substrate with highest ground-truth fidelity. The answer depends on which substrate is more durable and more recoverable — markdown files or SQLite. This is an empirical question, not a derivable one.

**Sovereign decision needed**: Should the σ₂ build use markdown as the primary storage substrate with SQLite as an index, or SQLite as the primary store with markdown exports? This decision gates the σ₂ build.

### Q2: Hard-Gate Delivery Rate — Second-Order Intervention

**Problem**: The Hard-Gate sequence is itself at 0% delivery. The intervention (DEC-C3) is shelfware. T2 predicts this outcome: without a second-order enforcement mechanism, any self-improvement protocol falls into the same activation gap it was designed to solve.

**Derivation limit**: The axioms generate the need for Hard Gates. They do not generate a self-enforcing mechanism. A mechanism that requires willpower to activate violates A2 when capacity is constrained.

**Sovereign decision needed**: What is the enforcement mechanism for the Hard Gates themselves? Options include: (a) automated hook that blocks commits without VERIFY evidence, (b) a daily report that makes non-compliance visible, (c) a trusted external party with audit authority (Adjudicator's existing CQO role). Option (c) has the strongest A3 derivation — it externalizes enforcement from σ₀.

### Q3: Security Domain — T4 or A5?

**ARCH-NEO_CANON_CORE §IX** identifies security as a P0 gap. The open question is architectural: does security merit a 5th axiom (A5: Security Invariant) or is it derivable as a theorem from A3 (T4: Perimeter = Capability)?

**The distinction matters**: A5 would mean security is irreducible and cannot be derived from sovereignty alone — it is a separate primitive. T4 would mean security is A3 applied to the threat surface — a corollary, not an axiom.

**Sovereign decision needed**: Adjudicate whether T4 (derived from A3) is sufficient or whether the credential exfiltration threat surface represents a genuinely new primitive requiring A5. DC-002 and DC-003 are the empirical evidence base.

### Q4: Layer 3 Autonomic — Minimum Viable Implementation

**Current state**: proactive_orchestrator exits 1. The prefrontal cortex is absent. This means the system cannot self-generate work — every task requires Sovereign initiation.

**Derivation limit**: A2 and A4 both point toward autonomous work generation, but the implementation architecture is not axiom-derivable. It depends on what σ₂ looks like (Q1 above) and what budget constraints exist.

**Sovereign decision needed**: What is the minimum viable Layer 3 that (a) doesn't require full σ₂ to function, (b) generates work from existing Commitment and task history, (c) fits within current infrastructure? This is a build specification decision.

### Q5: Causal Chain Position Assessment

**ARCH-NEO_CANON_CORE §VI** defines 6 causal chains. The scaffold depends on knowing the Sovereign's current stage in each chain to route capacity appropriately (A2 implies: right capacity deployed to right stage). Without a current position assessment, the scaffold routes blindly.

**Sovereign decision needed**: What is the current stage in each of the 6 chains? This assessment cannot be produced by an agent — it requires Sovereign first-person knowledge. The assessment becomes an input to the quarterly rhythm and the dispatch capability profile for each agent.

---

## X. SCAFFOLD VALIDATION — DERIVATION AUDIT

This section performs the Software Succession Test from ARCH-NEO_CANON_CORE §X applied to the scaffold itself.

### Test: Can a novel scaffold element derive from this document alone?

"Daily triage should be limited to 3 items maximum" → A2 (capacity constraint: claiming more than capacity allows creates a commitment deficit) + T1 (attention bottleneck: more than 3 parallel items exceeds σ₀ parallel processing) → Hard constraint, not heuristic. **PASS**.

"Agent results should include a Net New section" → A4 (distill stage requires genuine compression) + Verbatim Trap (molt_cornelius, ARCH-NEO_CANON_CORE §VIII) → The Net New section operationalizes A4's distill requirement at the artifact level. **PASS**.

"The EscalationQueue is the only legitimate interrupt mechanism" → T1 (attention bottleneck) + A3 (sovereignty invariant: the Sovereign defines what reaches σ₀) → Side channels violate both. **PASS**.

### Test: Does a vestigial element fail automatically?

"Weekly status meeting" → No axiom derivation. Ring 4 (COMMUNITY) has no structure requiring synchronous communication rituals. T1 actively disfavors scheduled interrupts. → **REJECTED**. If coordination is needed, it routes through the dispatch system.

"Habit tracker" → No axiom derivation. A2 addresses capacity, not habit formation. No governed verb applies. → **REJECTED at maximum Tier 2 Tool** if it demonstrably reduces activation energy for a mapped workflow; otherwise, **PRUNED**.

All elements in §§ I–IX pass derivation audit or are explicitly flagged as open questions for Sovereign adjudication.

---

*ARCH-NEO_SCAFFOLD.md v1.0.0 | Commander (Sonnet 4.6, MBA) | Session 22 | 2026-02-18*
*Derives from ARCH-NEO_CANON_CORE.md v1.0.0. Every scaffold element cites its axiom. Phase 4, Document 1 of 3.*
*Open questions for adjudication: Q1 (σ₂ substrate), Q2 (Hard-Gate enforcement), Q3 (Security axiom), Q4 (Layer 3 minimum viable), Q5 (Causal Chain position).*
