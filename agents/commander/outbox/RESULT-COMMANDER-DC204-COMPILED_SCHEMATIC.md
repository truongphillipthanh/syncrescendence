# DC-204: Compiled Engineering Schematic — Oracle DC-204E + Diviner DC-204D

**Compiled by**: Commander (Claude Opus 4.6)
**Date**: 2026-02-23
**Authority**: Sovereign directive — "dispatch the swarm, proceed comprehensively"
**Intel Sources**: Oracle DC-204E (industry consensus, 5 recommendations), Diviner DC-204D (cross-disciplinary synthesis, 3 predictions)
**Purpose**: Unified design spec for Adjudicator hyper-technical engineering review

---

## 1. Architecture Decision Summary

Oracle identified 7 architectural patterns in Syncrescendence, mapped each to industry state-of-the-art, and produced 5 concrete recommendations (now DC-147 through DC-151 in deferred commitments). Diviner overlaid scientific frameworks from materials science, immunology, neuroscience, stigmergy, and mycology to illuminate *why* each recommendation works, predicted failure modes, and contributed 3 falsifiable hypotheses.

### Convergence Assessment

| Oracle Recommendation | Diviner Scientific Frame | Convergence | Risk Identified |
|---|---|---|---|
| **Rec 1: AgentFS Hybrid** (SQLite under Markdown) | Glass-ceramic composite / delamination risk | HIGH — both agree on hybrid, both flag sync as critical | Diviner: "Jane Jacobs vs Robert Moses" — agents must still walk the filesystem, not just query DB |
| **Rec 2: Constitutional Evolution Loop** | Immunology / somatic hypermutation / autoimmunity | HIGH — both agree static constitutions fail at scale | Diviner Prediction 3: AGENTS.md ossification when >3000 words. Need "Supreme Court" (subtractive governance) |
| **Rec 3: Lightweight Model Router** | Thalamic Reticular Nucleus / salience gating | MEDIUM — Oracle says cost router, Diviner says *attention* router (suppress noise, not just route cheap) | Diviner: metric is salience, not just cost. Router needs GABAergic "no" function |
| **Rec 4: Git-Native Issue Tracking (Beads)** | Stigmergy / digital pheromones | HIGH — both agree Git DAG is the coordination substrate | Diviner Prediction 2: "Ghost in the Shell" — system can retrieve deleted knowledge via git history |
| **Rec 5: Auto Knowledge Graph** | Mycorrhizal networks / source-sink dynamics | HIGH — both agree passive graph is useless, must actively transport context | Diviner: graph must *inject* context from canon→praxis, not just visualize |

### Meta-Pattern: Free Energy Principle (Diviner)

Diviner identified that all 7 patterns are emergent properties of Active Inference (Karl Friston's Free Energy Principle). The system minimizes surprise by making the codebase match the user's intent. This isn't metaphor — it's the actual computational dynamic:
- Internal States = filesystem (canon, praxis)
- Sensory Blanket = agents reading input
- Generative Model = AGENTS.md constitution
- Active Inference = code generation / file writing
- Surprise Minimization = the tightening plan itself

### Critical Warning: Jamming Transition (Diviner)

The system approaches a **context singularity** when: `Context Density = (Active Files × Avg Interdependence) / Context Window > 1.0`. At this point, the Commander cannot hold the working set and begins hallucinating or looping. The AgentFS hybrid (DC-149) is the primary mitigation — it lowers effective density by indexing/sparsifying data.

---

## 2. Engineering Specifications for Adjudicator

### Spec A: Lightweight Model Router (DC-147) — SMALL EFFORT, HIGH VALUE

**What**: A routing function that selects model + token budget before dispatch.sh sends a task.

**Oracle Design**: R2-style reasoning prompt or simple classifier. Maps to `dispatch.sh`.

**Diviner Enrichment**: Not just cost optimization — implement *salience gating*. The router should have a "suppress" function that says "this query is noise, do not dispatch to high-compute agents."

**Engineering Requirements**:
1. New file: `engine/02-ENGINE/FUNC-MODEL_ROUTER.md` (routing logic spec)
2. New script: `orchestration/00-ORCHESTRATION/scripts/route_model.sh` (callable from dispatch.sh)
3. Input: task topic, description, estimated complexity, target agent
4. Output: recommended model, token budget, dispatch/suppress decision
5. Lookup table: Frontier Model Registry (from MEMORY.md) as ground truth until FIDS operational
6. Salience threshold: if task is pure telemetry/status check, route to cheapest model or suppress entirely
7. Integration point: `dispatch.sh` calls `route_model.sh` before SCP sling

**Constraints**: Must work without network. Pure filesystem lookup + heuristic. No ML model needed.

### Spec B: Auto Knowledge Graph View (DC-148) — SMALL EFFORT, HIGH VALUE

**What**: Weekly script that generates a graph over praxis/ and canon/ with broken-link detection and repair.

**Oracle Design**: Script using existing prefix ontology. Demonstrated by Obsidian Bases.

**Diviner Enrichment**: Graph must be *active transport* (mycorrhizal), not passive visualization. Should inject context from source nodes (canon/) to sink nodes (praxis/) — flag when a praxis doc references a concept that exists in canon but isn't linked.

**Engineering Requirements**:
1. New script: `orchestration/00-ORCHESTRATION/scripts/knowledge_graph.sh`
2. Scan: all `*.md` files in praxis/ and canon/
3. Extract: wiki-links `[[target]]`, path references, prefix-tagged cross-refs
4. Build: adjacency list (JSON output to `orchestration/00-ORCHESTRATION/state/DYN-KNOWLEDGE_GRAPH.json`)
5. Detect: broken links (target doesn't exist), orphan nodes (no inbound links), stale refs (target modified >30 days after reference)
6. Report: `agents/commander/outbox/REPORT-KNOWLEDGE_GRAPH_HEALTH.md`
7. Enrichment layer: for each broken link, suggest the most likely existing file (fuzzy match on filename + prefix)
8. Cron: weekly via launchd or manual invocation

**Constraints**: Pure bash/jq. No Python dependency beyond what's already installed.

### Spec C: AgentFS Hybrid (DC-149) — MEDIUM EFFORT, STRATEGIC

**What**: SQLite database under the Markdown interface. Files remain human-readable; DB provides ACID, query, and audit.

**Diviner Enrichment + Warnings**:
- "Delamination" risk: if DB index drifts from Markdown source, the composite fails
- "Robert Moses" risk: if agents stop reading raw files because DB is easier, filesystem coherence decays
- Mitigation: mandatory "randomized patrols" — agents must periodically read raw files to verify map matches territory

**Engineering Requirements** (design-level — Adjudicator to detail):
1. Single SQLite file at `orchestration/00-ORCHESTRATION/state/agentfs.db`
2. Schema mirrors prefix ontology: table per prefix type (ARCH, DYN, REF, FUNC, PROMPT, etc.)
3. Content column stores raw markdown; metadata columns for parsed frontmatter
4. Write path: on git commit, post-commit hook updates DB from changed files
5. Read path: agents query DB for structured lookups, fall back to raw file for full content
6. Sync invariant: DB is always rebuildable from filesystem (`rebuild_agentfs.sh`)
7. Patrol system: weekly random sample of N files, compare DB hash to file hash, alert on drift

**Constraints**: Must be fully rebuildable from Git. DB is cache, not source of truth. Filesystem remains sovereign (Invariant 5).

### Spec D: Git-Native Issue Tracking / Beads (DC-150) — MEDIUM EFFORT

**What**: Replace ad-hoc outbox/inbox with Yegge-style Beads for structured work items embedded in Git.

**Diviner Enrichment**: Digital pheromone trails. Commit messages ARE the coordination substrate. Poor messages = faint trails = colony loses coherence.

**Engineering Requirements** (design-level):
1. Work item format: structured YAML frontmatter in TASK-*.md files (already partially exists)
2. Git integration: each task gets a commit tag or trailer (`Task-ID: DC-XXX`)
3. Query: script to list open tasks from git log trailers
4. Merge queue: structured outbox with state machine (pending→active→done→archived)
5. Existing inbox system is already 80% there — main gap is git-log integration and trailer convention

### Spec E: Constitutional Evolution Loop (DC-151) — LARGE EFFORT, DEFERRED

**What**: LLM-guided simulation search to discover optimal AGENTS.md rules.

**Diviner Enrichment**: Somatic hypermutation model. The system simulates rule variants, tests which ones "neutralize chaos without causing autoimmunity."

**Engineering Requirements** (sketch only — Adjudicator to evaluate feasibility):
1. Simulation harness: replay historical directives under modified constitutions
2. Fitness function: measure coherence (broken refs), completion rate, agent conflict rate
3. Mutation operator: add/remove/modify single rules in AGENTS.md
4. Selection: top-K rules survive, merge into candidate constitution
5. Sovereign veto: no rule merges without human approval
6. "Supreme Court" mechanism: specialized agent whose job is to *repeal* rules (subtractive governance)

---

## 3. Diviner's Falsifiable Predictions (for Adjudicator validation)

| # | Prediction | Test | Timeline | Implication |
|---|---|---|---|---|
| 1 | Spontaneous Pidgin Formation — agents begin using compressed syntax in logs | NLP analysis of agent logs over 6 months | >2000 commits or >70% context fill | Formalize "System Creole" rather than fighting it |
| 2 | Ghost in the Shell — system retrieves deleted knowledge via git history | Delete a praxis file, ask system to solve related problem | Post-DC-150 (git-native tracking) | "Deletion" becomes soft state; system gains 4D memory |
| 3 | Constitutional Ossification — AGENTS.md complexity causes agent paralysis | Measure thinking/output token ratio over time | AGENTS.md >3000 words | Need subtractive governance mechanism |

---

## 4. Recommended Execution Order

1. **DC-147** (Model Router) — smallest effort, immediate dispatch.sh improvement
2. **DC-148** (Knowledge Graph) — small effort, enables ongoing health monitoring
3. **DC-150** (Beads/Git Tracking) — medium effort, formalizes existing inbox pattern
4. **DC-149** (AgentFS Hybrid) — medium effort, strategic infrastructure
5. **DC-151** (Evolution Loop) — large effort, defer until system is stable

All gated by Phase 0 (DC-100–102) per phase gate rule. DC-147 and DC-148 could proceed in parallel as design-only work while Phase 0 infrastructure is resolved.

---

*Compiled from Oracle DC-204E + Diviner DC-204D. Next: dispatch to Adjudicator for hyper-technical engineering review of Specs A-E.*
