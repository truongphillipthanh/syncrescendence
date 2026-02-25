# PORTAL: Chat Agent Context Injection
**Version**: 1.0.0
**Created**: 2026-02-24
**Purpose**: Single self-contained context document for chat-based agents (Gemini/Diviner, Grok/Oracle) who cannot crawl the repo.
**Authority**: Commander Council 28

---

## 1. System Description

Syncrescendence is a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. A single human Sovereign coordinates five AI agents (the Constellation) through a git-first, file-backed coordination system. The repo IS ground truth — web apps are cache. All durable knowledge lives in files, not threads.

**Five Invariants (Constitutional Law — non-negotiable):**
1. **Objective Lock** — No work without explicit Sovereign confirmation. Ambiguity = clarify, not interpret.
2. **Translation Layer** — All output intelligible without retransmission.
3. **Receipts** — No completion claim without committed artifacts.
4. **Continuation/Deletability** — Any conversation deletable without losing state.
5. **Repo Sovereignty** — Repository wins over platform state. Always.

---

## 2. Phase Status

| Phase | Status | Summary |
|-------|--------|---------|
| **0: Infrastructure** | DONE | Docker, Neo4j 5.26.0, Graphiti 0.22.0, Qdrant healthy. SSH bridge verified. |
| **1: Memory** | DONE | memsync daemon, JSONL journals, e2e write path verified. P1 hardening (DC-114/115) ready to deploy. |
| **2: Deep Audit** | DONE | 825 files indexed, 14,311 atoms extracted from 1,152 sources, coherence synthesis complete, 9 pipeline components built. |
| **3: Surface Org** | DONE | scaffold_validate PASS (0 violations), 26 naming conventions, headers standardized. DC-122 (rename) awaits Sovereign. |
| **4: Automations** | IN PROGRESS | Cockpit startup + ledger refresh DONE. DC-131/132/133 (Graphiti triples, backfill, query tools) blocked by Mac mini offline. |
| **5: Hardening** | IN PROGRESS | Security audit DONE (2 CRITICAL, 4 HIGH). Memory compaction DONE. API key rotation + cross-machine sync OPEN. |

**Current position**: All MacBook Air-executable items DONE. Remaining blockers: Mac mini offline, Sovereign decisions, deferred items.

---

## 3. Top 10 Active Intentions

| ID | Priority | Summary |
|----|----------|---------|
| INT-1202 | P0 | Maximize construction velocity during capability window |
| INT-1612 | P0 | Begin ALL automations (cockpit activation underway) |
| INT-2301 | P0 | Docker + Neo4j + Graphiti online (DONE, maintain) |
| INT-1709 | P0 | Security is existential — 200+ exposed instances, supply chain attacks |
| INT-2202 | P1 | MBA single-cockpit consolidation — one control plane |
| INT-2408 | P1 | Exocortex integration — slot SaaS tools into constellation |
| INT-2401 | P1 | OpenClaw architecture harmonization (bridge INIT.md and SOUL.md) |
| INT-2402 | P1 | CLI agent heterogeneity strategy — graceful degradation across 5+ harnesses |
| INT-1616 | P1 | LifeOS/PKM/Zettelkasten architectural convergence |
| INT-2412 | P1 | Recanonization pass after corpus extraction completes |

---

## 4. Key Script Invocations

```bash
# Dispatch a task to an agent
bash orchestration/scripts/dispatch.sh <agent> "TOPIC" "DESC" "" "TASK" "<from-agent>"

# Cluster extracted atoms (triage sovereign_review vs archive)
python3 orchestration/00-ORCHESTRATION/scripts/atom_cluster.py \
  --atoms-dir agents/commander/outbox/ --output clusters.json

# Validate scaffold integrity (must pass before structural changes)
bash orchestration/00-ORCHESTRATION/scripts/scaffold_validate.sh

# Ascertescence relay (triangulation prompt staging)
bash orchestration/00-ORCHESTRATION/scripts/ascertescence_relay.sh CC<N> send <oracle|diviner|adjudicator>

# Cockpit startup health check
bash orchestration/00-ORCHESTRATION/scripts/cockpit_startup.sh --quick
```

---

## 5. Memory Status

**Architecture**: Sovereign Temporal Hybrid (STH) — three-layer, triangulation-confirmed.

| Layer | What | Status |
|-------|------|--------|
| **L0: Git** | Markdown files (MEMORY.md, entities/, journal/) — absolute ground truth | OPERATIONAL |
| **L1: Working Memory** | Context window — ephemeral, per-session | OPERATIONAL |
| **L2: Session Memory** | Per-agent `agents/<name>/memory/` with JSONL journals | OPERATIONAL |
| **L3: Graph** | Graphiti on Neo4j — derived projection, rebuildable from git | OPERATIONAL (Mac mini) |

Write path: Agent journal JSONL -> memsync daemon -> Graphiti `/messages` -> entity materialization.
Read path: Graphiti `/search` -> cache/ -> file fallback if graph down.
11/14 memory components built. Gaps: Graphiti `/triples` endpoint, backfill, query tools in agent harnesses.

---

## 6. SN Quick-Ref Glossary

Semantic Notation (SN) provides ~80% token reduction. Key symbols:

| Symbol | Meaning | | Symbol | Meaning |
|--------|---------|---|--------|---------|
| `Psi` | Syncrescendence | | `Kappa` | CANON (constitutional doc) |
| `Omicron` | OPERATIONAL | | `Sigma` | SOURCE (raw material) |
| `Delta` | DIRECTIVE | | `Lambda` | LOG (execution record) |
| `::` | expands to / defined as | | `>>` | transforms into / flows to |
| `\|` | constrained by | | `=>` | implies / produces |
| `MUST` | required invariant | | `MUST_NOT` | forbidden |
| T0-T7 | Tiers: cosmos > core > lattice > chain > planetary > lunar > satellite > asteroid |

**Chains**: I (Intelligence), i (Information), .:. (Insight), E (Expertise), K (Knowledge), W (Wisdom)
**Virtues**: alpha (Acumen), chi (Coherence), epsilon (Efficacy), mu (Mastery), tau (Transcendence)
**Block types**: TERM (ontology), NORM (constraints), PROC (procedures), PASS (transforms), ARTIFACT (outputs), TEST (validation)

---

## 7. Depth Links

All files accessible via GitHub at:

```
https://github.com/truongphillipthanh/syncrescendence/blob/main/<path>
```

Key paths:
- `AGENTS.md` — Constitutional law (all agents inherit this)
- `orchestration/00-ORCHESTRATION/state/DYN-DEFERRED_COMMITMENTS.md` — Phase tracker
- `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — All intentions
- `orchestration/00-ORCHESTRATION/state/ARCH-MEMORY_ARCHITECTURE.md` — Memory design
- `engine/02-ENGINE/` — 147 implementation files (prompts, functions, templates)
- `canon/` — Verified canonical knowledge (PROTECTED)
- `praxis/05-SIGMA/` — Operational wisdom (mechanics, practice, syntheses)
- `agents/` — Agent offices (commander, adjudicator, cartographer, psyche, ajna)
- `engine/REF-ROSETTA_STONE.md` — Terminology reconciliation
- `orchestration/00-ORCHESTRATION/scripts/sn_symbols.yaml` — Full SN glossary

---

*This portal is regenerated per Commander Council session. Do not treat cached versions as current.*
