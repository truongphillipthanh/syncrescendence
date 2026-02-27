# Adjudicator Distillation — How to Get the Best Out of a QA/Engineering Agent

**Corpus**: 15 files across CC26–CC38 (8 prompts, 6 responses, 1 dispatch)
**Total**: 22,539 words of output. Signal range: 6/10 to 9/10.
**Core finding**: Signal correlates directly with how much the adjudicator *contradicts* its input. Rubber-stamping is the default; pushback is the value.

---

## 1. The Effective Prompt Shape

Every high-signal adjudicator prompt shares this anatomy:

### Header (routing)
```
Date, From, To, Session, Relay mechanism, Response landing path
```
Non-negotiable. The adjudicator needs to know exactly where to write and how the file routes back. Eliminates coordination ambiguity.

### Role Constraint (scope boundary)
Best formulation (CC38): *"Your cognitive function is deep hyper-technical engineering. You meet Commander halfway: Commander provides what and why; you provide how and how it breaks."*

The critical word is **how it breaks**. Without this, the adjudicator defaults to "how it works" — which is spec generation, not quality assurance.

### Prior-Leg Synthesis (upstream context)
Distill where Oracle and Diviner agree into numbered convergence points. Example (CC28): 7 bullet "CONVERGENCE SUMMARY" — the adjudicator engineers the agreed direction rather than re-debating.

Give full upstream context but **pre-digested**. Raw Oracle/Diviner responses waste tokens; synthesis focuses the engineering.

### Deliverables (the core ask)
Per-deliverable with explicit sub-questions works best. Required sub-artifacts:
- Data schema
- State machine / lifecycle
- Integration points (what reads/writes this)
- Failure modes (how it breaks)
- Verification contract (how you prove it works)
- Composition rules (how it interacts with other deliverables)

### Anti-Instructions (what NOT to do)
**Every effective prompt has these.** Without them, the adjudicator either goes meta (re-debates architecture) or goes granular (writes implementation code). Both waste the turn.

Proven anti-instructions:
- *"Do not re-analyze the philosophical framing."*
- *"Do not propose architectural alternatives. They are ratified. You specify HOW, not WHETHER."*
- *"Do not write implementation code. Write specifications."*
- *"Do not hand-wave feasibility."*
- *"No prose analysis. No recommendations."*

### Verification Demand (forces executable output)
- *"Implement the 5 test cases from your spec as a --self-test mode with synthetic fixtures."* (CC37)
- Without this, you get test case IDs without harnesses — specification-level verification, not implementation-level.

### Emotional Anchor (existential weight)
One sentence tying the deliverable to a past catastrophe or existential risk. Example (CC26): *"The INT-2210 Demolition happened because an agent interpreted 'triage the scaffold' as license to delete... This is not a historical footnote. It is the reason this entire triangulation exists."*

This prevents the adjudicator from treating the deliverable as routine checkbox work.

---

## 2. The Three High-Signal Framings

### A. The Bid/Audit — "Challenge this plan" (9/10 signal)
Prompt says: *"This is not a rubber stamp."* Forces the adjudicator to:
1. Survey actual repo state before responding
2. Challenge feasibility with specific blocking conditions
3. Audit token economics and delegation
4. Enforce standards against its own prior specs

**Why it works**: The adjudicator's natural mode is adversarial review. Bid framing activates it. Spec-generation framing suppresses it.

### B. Self-Referential Accountability — "Implement your own spec" (8/10 signal)
Prompt says: *"Your spec is at [path]. You wrote it — implement it faithfully."*

**Why it works**: Eliminates hand-waving. The adjudicator cannot deny its own prior commitments. Maximum fidelity because the constraint field is self-generated.

### C. Surgical Integration Review — short, scoped, specific (8/10 signal)
The CC37 integration review prompt (52 lines): lists exactly what changed, asks 5 specific review questions (lock order, subprocess isolation, adapter fidelity, batch atomicity, plist validity).

**Why it works**: Prevents comprehensive-but-shallow output. Focused scope produces focused engineering.

### What DOESN'T work: Unbounded Spec Generation
Asking for 7 deliverables with 6-point schemas each (CC35) produces 1,230 lines. The adjudicator fills every template mechanically. YAML schemas, state machines, lock orders — correct but derivable. The cross-cutting analysis is valuable; the per-deliverable fill is noise.

---

## 3. Generalizable Lessons

### The QA Agent Value Function
The adjudicator justifies its existence **only when it catches things the designer missed**. Specifically:
- Doc-code divergence (specs say X, implementation does Y)
- Stale truth surfaces (prompt claims N, repo shows M)
- Missing interfaces between independently-specified components
- Circular dependencies in build order
- Failure cascades across deliverable boundaries

### Operational Rules

1. **Bid before Build**: Always run an adversarial feasibility check before committing to implementation. The CC35 Bid caught 9 amendments that would have been bugs in production.

2. **Force Repo Grounding**: *"Read the actual code, not just documentation"* with specific file paths. Without this, agents spec against assumed state. The CC35 Bid caught HEAD mismatch, dirty worktree, and stale banner — all invisible without repo read.

3. **Separate WHETHER from HOW**: When given both design and implementation authority, the QA agent either rubber-stamps or re-debates. Constrain it to one mode per prompt.

4. **Token Economics as Explicit Deliverable**: Without asking, agents never volunteer cost/delegation analysis. The CC35 Bid discovered `opencode` installed but unconfigured, `cline` installed, `aider` absent — actionable infrastructure inventory.

5. **The Integration Review is Underrated**: Short (50-60 lines), scoped to specific changes, 5 targeted questions. Highest signal-per-token ratio of any prompt format.

6. **Lean Siege Format**: 62 lines. Three concrete tasks, dry-run/apply flags, verification instructions. Minimal context, maximum leverage. Contrast with 383-line prompts that produce no proportional increase in value.

---

## 4. Failure Modes

### System Failures the Adjudicator Caught

| ID | Failure | How Caught | Significance |
|----|---------|------------|-------------|
| **ADJUST Loop Mismatch** | `protease_promote.py` treats ADJUST as terminal abort; `CANON-ONTOLOGY-GATE_v2.md` mandates iterative retry (max 3). | CC38: reading actual code vs documentation | Crown jewel. Doc-code divergence invisible to spec review. Fix: `QUARANTINED_ADJUST_PENDING` state. |
| **Lineage Preservation Bug** | `candidate_adapter.py` uses `[atom["atom_id"]]` instead of `atom.get("source_atom_ids")`. Silently clobbers provenance chains during promotion. | CC38: code-level review | One-line fix, significant data integrity consequence. |
| **Autoimmune Starvation** | `lattice_annealer.py` formula `0.70 - 0.25*(gc - 0.70)` tightens gate when coherence drops — rejects novel atoms when system most needs them. | CC38: mathematical analysis of threshold formula | Sign error. Fix: `0.70 + 0.25*(gc - 0.70)`. Point-checked at gc=0.50→0.65, gc=0.00→0.60, gc=1.00→0.775. |
| **Ambient Paralyzation** | `dag_tension_monitor.py`: any ambient operation leaving 1 net-new open DAG node forces permanent HOLD. | CC38 chain | One mess freezes everything. |
| **Dimension Blindness** | `candidate_adapter.py` maps 5 operational dimensions, ignores 14-dimensional Meaning Taxonomy. Structural bias against philosophical atoms. | CC38 chain | Systemic filtering of the content the system was built to process. |
| **Circular Dependency D2↔D6** | Construction docs list D2 depending on D6 and D6 depending on D2. | CC35 Bid: reading build order | Build deadlock. Resolution: D6 policy-first, then D2 implementation. |
| **Missing Adapter Contract** | No interface between `protease_promote.py` output and `lattice_annealer.py` input. Specs designed independently. | CC35 Bid: integration analysis | Became `ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml`. |
| **Stale Truth Surfaces** | Prompt claims 150 clusters / 606 sovereign_review; repo shows 50 clusters / 120 queue band. Banner says 0% transformation while DAG reports 62%. | CC30, CC35 Bid: repo state audit | Meta-failure: stale numbers in prompts contaminate all downstream reasoning. |
| **Missing Seed State Files** | `DYN-DAG_STATE.json`, `DYN-ASCERTESCENCE_THRESHOLDS.yaml`, etc. — all assumed by specs, none present in repo. | CC35 Bid: file existence check | Specs building on phantom foundations. |

### Adjudicator's Own Failure Modes

| Failure | Pattern | Mitigation |
|---------|---------|------------|
| **Spec Volume Without Executable Verification** | CC26: 750+ lines, CC35: 1,230 lines. YAML schemas, test case IDs, no fixtures, no harness. | Mandate `--self-test` mode. Require executable verification, not specification-level. |
| **Lock Hierarchy Inconsistency** | CC35 specs contain inconsistent lock orders across 7 deliverables. Adjudicator's own Bid caught this. | Single canonical lock hierarchy doc, not per-deliverable copies. |
| **Over-Engineering for System Scale** | CC35 Bid self-assessment: *"Full apoptosis + retirement + stress orchestration can overtake throughput if enforced without waiver/debt guardrails."* 7 deliverables of autonomic infrastructure for 6 axioms. | Adjudicator recognizes this but doesn't refuse the scope. Sovereign must enforce proportionality. |
| **Mechanical Template Fill** | When given unbounded spec scope, fills every sub-schema identically. State machines, lock orders, verification contracts — structurally repetitive. | Scope to 3 deliverables max per prompt. Or use Bid framing to challenge scope itself. |
| **Fails to Volunteer Risk** | Without explicit anti-instructions and bid framing, defaults to affirmative spec generation. Never spontaneously says "this shouldn't be built." | Always include: *"Challenge feasibility. If a deliverable is unnecessary, say so."* |

### Cross-Cutting Cascade Taxonomy (from CC35 specs)

| ID | Class | Description |
|----|-------|-------------|
| XFM-RACE-001 | Race | Apoptosis retires node while annealer scores edge to same node |
| XFM-CASCADE-002 | Cascade | High gate rejects inflate DAG tension → perpetual FIRE loop |
| XFM-DEADLOCK-001 | Deadlock | Annealer requests ADJUST but no model bandwidth on constrained day |
| XFM-STARVE-001 | Starvation | Dynamic threshold too strict despite high coherence (autoimmune) |

---

## 5. Crown Jewel Insights (Unique to Adjudicator)

**"Build is directionally correct only if treated as throughput infrastructure for canon metabolism, not as another architecture cycle."** (CC35 Bid) — The legitimacy of any build is conditional on serving output production.

**Integration-First Gate dual enforcement**: Session-close gate (atom lifecycle advancement) + commit-time gate (commit trailers). Pass requires both new canon/praxis file AND atom index transition. Bypass requires explicit reason file in `-SOVEREIGN/`. Most technically precise anti-means-ends-inversion mechanism in the corpus.

**"Make it breathe or die" viability assessment**: Diviner's autocatalytic proposal assessed as *"Viable only with rails"* — then 5 rails specified (quarantine lane, TTL probation, rollback pointer, contradiction preservation, health budget). The adjudicator at its best: not rejecting radical ideas, engineering the safety envelope.

**Minimum catalyst set**: *"Spec 1 core (Protease queue + promote + consumed marking + metrics). Spec 4 Tier 1 (300-token state vector). Spec 2 lite (filesystem-only consolidation)."* Explicit exclusion: *"Spec 3 is high-value hardening but not the minimum catalyst for phase transition."* Engineering-disciplined triage of what's actually needed vs. what's nice.

**"Protease queue becomes another backlog"**: Identified as Medium likelihood / High impact. Prescient — anticipates the exact failure mode of building a queue system for a system that already has too many queues.

**Two-step forget for dream cycle**: *"candidate then confirmed after N cycles."* Prevents over-aggressive memory consolidation from irreversibly deleting needed context.

**Ontology as runtime Layer 1**: Keep ontology as Layer 2 in the conceptual stack but reorder runtime pipeline so ontology classification executes immediately after intake, before any praxis/canon write. Runtime-vs-architecture distinction.

---

## 6. The One-Line Summary

The adjudicator is a **bug-finding instrument, not a design instrument**. Use it to break things (Bid, audit, integration review). Never use it to build things (unbounded spec generation). Its highest-signal output is always a correction — of the prompt, of the code, of its own prior specs.
