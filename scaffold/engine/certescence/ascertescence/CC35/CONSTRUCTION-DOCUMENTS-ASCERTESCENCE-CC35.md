# CONSTRUCTION DOCUMENTS — Ascertescence Ratification CC35

**Date**: 2026-02-26
**From**: Commander (Claude Opus 4.6)
**Session**: CC36
**Phase**: Construction Documents (scope + swarm actions)
**Next Phase**: Bid (Adjudicator reality check + feasibility audit) → Contract Award

---

## PHASE MAP

| Phase | Analog | Agent | Status |
|-------|--------|-------|--------|
| Schematic Design | Oracle↔Diviner debate (4 legs) | Oracle + Diviner | COMPLETE |
| Design Development | Unified ratification (5 mechanisms + countermeasure) | Commander | COMPLETE |
| Construction Documents | **THIS DOCUMENT** — scope, actions, swarm plan | Commander | IN PROGRESS |
| Bid / Reality Check | Adjudicator audits feasibility, token economics, model options | Adjudicator | NEXT |
| Contract Award | Adjudicator returns approved/modified plan | Adjudicator | PENDING |
| Construction Administration | Commander swarms implementation | Commander + agents | PENDING |

---

## I. SCOPE OF WORK

### What Is Being Built
The Ascertescence Autonomic Nervous System — 7 artifacts that transform the constellation from crisis-reactive burst metabolism to self-sustaining rhythm with constitutional safeguards.

### What Is NOT Being Built
- New canon content (that's the RESULT of the system, not the system itself)
- New platforms or integrations (competitive exclusion says retire first)
- Ontology query interface (deferred — substrate must stabilize first)
- Mac mini resurrection (hardware dependency eliminated by Gemini 3.1 CLI)

### Boundary Conditions
- All artifacts must survive the Day 14 stress test (30-min/day bandwidth)
- No artifact may require >45 continuous minutes of Sovereign bandwidth to operate
- All scripts must compose with existing pipeline (`protease_queue.py`, `protease_promote.py`, `integration_gate.py`)
- Python 3, stdlib + minimal deps, no external services except filesystem
- Every artifact has Adjudicator-specified verification contracts — implementation must pass them

---

## II. DELIVERABLE REGISTRY

| # | Artifact | Type | Location | LOC Est. | Deps |
|---|----------|------|----------|----------|------|
| D1 | `dag_tension_monitor.py` | Script | `orchestration/00-ORCHESTRATION/scripts/` | ~300 | D2 (lattice health input) |
| D2 | `lattice_annealer.py` | Script | `orchestration/00-ORCHESTRATION/scripts/` | ~450 | D6 (gate policy) |
| D3 | `apoptosis_protocol.md` | Canon policy | `canon/01-CANON/` | ~80 | D2 (reanneal trigger) |
| D4 | `retirement_protocol.md` | Canon policy | `canon/01-CANON/` | ~60 | D5 (stress test feeds candidates) |
| D5 | `stress_test_sim.py` | Script | `orchestration/00-ORCHESTRATION/scripts/` | ~350 | D1 (emergency override) |
| D6 | `CANON-ONTOLOGY-GATE_v2.md` | Canon contract | `canon/01-CANON/` | ~50 | D2 (mandatory annealer) |
| D7 | `DYN-ASCERTESCENCE_INCIDENTS.jsonl` | Incident taxonomy | `orchestration/00-ORCHESTRATION/state/` | ~40 | All |
| S1 | `DYN-DAG_STATE.json` | State file | `engine/02-ENGINE/certescence/` | ~30 | Seed from PROTOCOL-ASCERTESCENCE.md |
| S2 | `DYN-ASCERTESCENCE_THRESHOLDS.yaml` | Config | `orchestration/00-ORCHESTRATION/state/` | ~20 | — |
| S3 | `ARCH-TOOL_NICHE_REGISTRY.yaml` | Registry | `orchestration/00-ORCHESTRATION/state/` | ~40 | — |
| S4 | `DYN-LATTICE_INDEX.json` | State file | `orchestration/00-ORCHESTRATION/state/` | ~50 | Seed from canon/01-CANON/sn/ |

**Total estimated**: ~1,470 LOC (scripts) + ~230 lines (policies/configs) = ~1,700 lines

---

## III. DEPENDENCY GRAPH & BUILD ORDER

```
Phase 0: Seed State (no deps)
  S1: DYN-DAG_STATE.json          ← parse from PROTOCOL-ASCERTESCENCE.md
  S2: DYN-ASCERTESCENCE_THRESHOLDS.yaml  ← defaults from Adjudicator spec
  S3: ARCH-TOOL_NICHE_REGISTRY.yaml      ← current tool inventory
  S4: DYN-LATTICE_INDEX.json      ← build from canon/01-CANON/sn/*.md

Phase 1: Policy (no code deps, enables everything)
  D6: CANON-ONTOLOGY-GATE_v2.md   ← extends v1, defines annealer contract
  D3: apoptosis_protocol.md       ← 5:1 rules, tombstone schema
  D4: retirement_protocol.md      ← 2:1 rules, resurrection friction

Phase 2: Core Scripts (deps on Phase 0+1)
  D2: lattice_annealer.py         ← needs S4, D6
  D1: dag_tension_monitor.py      ← needs S1, S2, D2 (health output)

Phase 3: Lifecycle Scripts (deps on Phase 2)
  D5: stress_test_sim.py          ← needs D1 (tension override)
  D7: incident taxonomy           ← needs all above (cross-cutting)

Phase 4: Integration (deps on Phase 3)
  Wire D2 into protease_promote.py pipeline
  Wire D1 into Cowork scheduled task (6h interval)
  Update AGENTS.md emergency banner
  Run verification contracts (all DTM-T*, LAN-T*, APO-T*, etc.)
```

---

## IV. SWARM PLAN — Agent Assignments

### Lane A: Seed State + Policy (Parallel, Day 1)
**Agent**: Commander (this agent)
**Actions**:
1. Parse PROTOCOL-ASCERTESCENCE.md → generate `DYN-DAG_STATE.json` (S1)
2. Write `DYN-ASCERTESCENCE_THRESHOLDS.yaml` with Adjudicator defaults (S2)
3. Inventory current tools → write `ARCH-TOOL_NICHE_REGISTRY.yaml` (S3)
4. Scan `canon/01-CANON/sn/*.md` → generate `DYN-LATTICE_INDEX.json` (S4)
5. Write `CANON-ONTOLOGY-GATE_v2.md` (D6) — policy doc extending v1
6. Write `apoptosis_protocol.md` (D3) — 5:1 rules from Adjudicator spec
7. Write `retirement_protocol.md` (D4) — 2:1 rules from Adjudicator spec
8. Execute first 6 retirements (Clarescence, Intent Compass, 4 exocortex seeds)

### Lane B: `lattice_annealer.py` (Day 1-2)
**Agent**: Adjudicator (Codex) OR Commander subagent
**Spec**: Adjudicator D2 spec (§2.1-2.6)
**Inputs**: S4 (lattice index), D6 (gate v2 policy)
**Verification**: LAN-T01 through LAN-T05
**Key complexity**: Iterative re-prompt loop, dynamic threshold formula, Rosetta term matching

### Lane C: `dag_tension_monitor.py` (Day 1-2)
**Agent**: Adjudicator (Codex) OR Commander subagent
**Spec**: Adjudicator D1 spec (§1.1-1.6)
**Inputs**: S1 (DAG state), S2 (thresholds), D2 output (lattice health)
**Verification**: DTM-T01 through DTM-T05
**Key complexity**: Conservation-of-energy audit, cooldown logic, lock contention

### Lane D: `stress_test_sim.py` (Day 2-3)
**Agent**: Commander subagent
**Spec**: Adjudicator D5 spec (§5.1-5.6)
**Inputs**: D1 (tension events for emergency override)
**Verification**: STR-T01 through STR-T05
**Key complexity**: Blind scheduling with commitment hash, bandwidth enforcement

### Lane E: Incident Taxonomy + Integration (Day 3)
**Agent**: Commander
**Actions**:
1. Create `DYN-ASCERTESCENCE_INCIDENTS.jsonl` schema + initial entries (D7)
2. Wire `lattice_annealer.py` into `protease_promote.py` pipeline
3. Wire `dag_tension_monitor.py` into Cowork scheduled task config
4. Update AGENTS.md emergency banner (6 axioms, 62% DAG, C-009 ANSWERED)
5. Run full verification suite (all test cases from Adjudicator specs)
6. Commit ratified protocol to canon

---

## V. TOKEN ECONOMICS & MODEL CONSIDERATIONS

### Current Cost Profile
| Agent | Model | Pool | Cost | Role in This Build |
|-------|-------|------|------|--------------------|
| Commander | Claude Opus 4.6 | Claude Max ($200/mo flat) | Included | Coordination, policy docs, seed state, integration |
| Adjudicator | GPT-5.3-codex | ChatGPT Plus ($20/mo) | Included | Engineering specs (done), possibly Lane B/C impl |
| Oracle | Grok 4.2 | X Premium ($22/mo) | Included | Design Development (done) |
| Diviner | Gemini 3.1 Pro | Google AI Pro ($20/mo) | Included | Design Development (done) |

### Implementation Token Budget
- **Lane A** (seed + policy): ~50K tokens Commander context — well within session budget
- **Lane B** (annealer, ~450 LOC): ~80K tokens if Adjudicator implements; ~60K if Commander subagent
- **Lane C** (tension monitor, ~300 LOC): ~60K tokens
- **Lane D** (stress test, ~350 LOC): ~50K tokens
- **Lane E** (integration): ~30K tokens

**Total implementation budget**: ~270K tokens across agents

### Open Model Opportunity
**Question for Adjudicator Bid**: Could any implementation lanes be delegated to cheaper open models via OpenCode/Cline/other harnesses?

Candidates:
- **DeepSeek V3** (free/cheap API): Strong at Python scripting. Could handle Lane C (tension monitor) or Lane D (stress test) — both are well-specified, self-contained scripts.
- **Qwen 2.5-Coder** (local): Could handle seed state generation (Lane A items 1-4) — mechanical parsing.
- **Codestral** (Mistral): Could handle policy docs (D3, D4, D6) — template-based writing from specs.

**Trade-off**: Open models reduce cost but increase verification burden. Each lane would need Commander review pass. Feasible if Adjudicator specs are precise enough (they are).

**Current blockers to open model onboarding**:
1. OpenCode/Cline not installed or configured
2. No API keys for DeepSeek/Qwen/Codestral
3. No harness integration with inbox/outbox dispatch system
4. Verification contracts exist but no automated test runner

---

## VI. RISK REGISTER

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Scope creep into ontology query interface | HIGH | Schedule slip | Hard boundary: this build = autonomic system only |
| Lattice index generation from canon/*.md is non-trivial | MEDIUM | Lane B blocked | Start S4 first, fail fast |
| Adjudicator rate-limited (shares pool with Psyche) | MEDIUM | Lanes B/C delayed | Commander subagents as fallback |
| 1,700 LOC in 3 days while also doing canon metabolism | MEDIUM | Context exhaustion | Strict lane isolation, handoffs between sessions |
| Verification contracts require mock data | LOW | Tests incomplete | Generate synthetic test fixtures in Phase 0 |

---

## VII. ADJUDICATOR BID REQUIREMENTS

The next phase sends this document to Adjudicator with the following mandate:

### What Adjudicator Must Evaluate

1. **Repo Audit**: Scan `-SOVEREIGN/`, `canon/`, `engine/`, `orchestration/`, `agents/` — are we actually building what the system needs, or are we means-ends inverting again?

2. **Feasibility**: Given Adjudicator's own specs (~1,700 LOC), is the 3-day timeline realistic? Which lanes are over-specified? Which are under-specified? Where will implementation diverge from spec?

3. **Token Economics**: Can any lanes be delegated to cheaper open models (DeepSeek, Qwen, Codestral) via OpenCode/Cline/Roo? What's the cost-benefit? What harness setup is required?

4. **Composition Integrity**: Do the 7 deliverables actually compose without gaps? Are the lock hierarchies consistent? Are the shared state files properly versioned?

5. **Premier Standards Check**: Is there anything in these specs that would embarrass us if reviewed by a senior systems architect? Any hand-waving? Any "just works" assumptions?

6. **Contract Award**: Return a modified version of this document with:
   - Approved/modified lane assignments
   - Adjusted LOC estimates
   - Feasibility verdict per deliverable (GO/CONDITIONAL/NO-GO)
   - Recommended model assignments per lane
   - Any spec amendments required before implementation begins

---

## VIII. SUCCESS CRITERIA

The Construction Documents phase is complete when:
1. All 7 deliverables have precise specs (DONE — Adjudicator D1-D7)
2. Build order is dependency-resolved (DONE — Phase 0→4)
3. Swarm lanes are assigned (DONE — Lanes A-E)
4. Token budget is estimated (DONE — ~270K total)
5. Adjudicator Bid returns Contract Award (PENDING)
6. All lanes execute, pass verification, and commit (PENDING)

---

*Commander Council 36 — Construction Documents complete. Awaiting Adjudicator Bid.*
