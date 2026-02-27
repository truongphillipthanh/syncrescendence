# Oracle Setup Specifics — Every Concrete Recommendation Mined

**Source**: All 16 Oracle RESPONSE files (CC26–CC42)
**Purpose**: Raw material for the next Oracle prompt. Everything specific — no principles, only details.

---

## 1. Tool Configurations

### Optimal Full Config (CC35 Oracle thesis)
Commander (Claude Code) + Oracle (Grok web thesis) + Diviner (Gemini 3.1 CLI) + Adjudicator (Codex) + Cowork (scheduled exocortex heartbeat) + Perplexity Computer (delegated non-canon orchestration only)

### Per-Tool Details

**Claude Code (Commander)**
- Auto-generates 300-word "Session State Brief" on every constellation start (CC26)
- Status: Implemented (`session_state_brief.py`)

**Codex Desktop App (Adjudicator)**
- Desktop App for triangulation, NOT Codex CLI (CC30)
- Writes response directly, overwrites the relay file

**Gemini CLI (Diviner/Cartographer)**
- "Gemini 3.1 Pro CLI (ARC-AGI-2 77.1%, 3-tier compute, full-repo multimodal) obsoletes the old 'nerfed' constraint" (CC35)
- "Gemini 3.1 zero-shot 14-dim classification" for ontology scoring (CC40)
- Status: Available, not yet used for direct relay

**Grok (Oracle)**
- Under-utilized: "full-repo/X traversal for live mining" (CC40)
- Structured classification: "Pydantic 14-dim schema, git lineage in prompt, confidence scores" (CC42)
- Status: Used for thesis/X-mining but not structured classification

**OpenClaw (Ajna/Psyche)**
- "Activation only after first crystallization and Mac mini recovery" (CC35)
- "3/5 agents offline is recoverable today; full 5/5 possible once openclaw heartbeat restored on MBA" (CC40)

**Perplexity Computer**
- "19-model orchestration, autonomous month-long workflows, $200/mo cloud sandbox" (CC35)
- "Delegate non-canon workflows only; keep canon gates sovereign"

**Claude Cowork**
- "Scheduled tasks for exocortex heartbeat (daily atom scoring, weekly DAG health)" (CC35)
- `ascertescence_trigger.py` (Cowork-scheduled, fires on atom queue >50 or DAG <80%)

### MBA-Only Viable Constellation (CC40)
Without Mac mini: Grok (full repo/X access via web) + Claude on MBA + Gemini via web/CLI + Codex Desktop on MBA. Dispatch via auto_ingest_loop.sh + SCP sling to MBA-only; tmux resurrection optional.

---

## 2. Terminal Setup

**tmux**: `constellation` session as operational cockpit (ANESTHETIZED since CC27)

**launchd**:
- Sleep_Cycle: "Manual for first 3 runs, then launchd after scaffold_validate.sh passes" (CC33)
- CRITICAL: "launchd does NOT source ~/.zshrc. Env vars must be set in plist EnvironmentVariables" (SEARED)
- Health watchdog: runs every ~60s, writes to DYN-CONSTELLATION_HEALTH.md

**Shell hooks**:
- Session state brief must "persist to disk" — append to `agents/commander/memory/journal/$(date -u +%Y%m%d).md` and trigger `memsync_daemon.py` (CC28)

---

## 3. Memory Architecture

### Minimum Viable Stack (30-day horizon, CC30)
1. File-based repo memory (MEMORY.md per agent)
2. DYN-DEFERRED_COMMITMENTS
3. ARCH-INTENTION_COMPASS
4. Session handoff receipts
- "Freeze: Graphiti, tmux shared state until Mac mini online"

### Three-Layer Model (CC32)
- Layer 1: Knowledge Graph (long-term declarative)
- Layer 2: Daily Notes (episodic)
- Layer 3: Tacit Knowledge (procedural / MEMORY.md)
- Maps to: praxis (hippocampus buffer) → canon (neocortex)

### Consolidation Protocol (CC33)
- LTP if accessed >3 times or linked to canon_delta
- LTD if untouched >14 days (archive)
- Minimum praxis residence: 7 days before canon promotion eligibility
- First Sleep_Cycle run: 7 days after first crystallization

### 14 Components (CC28)
- Three working pre-CC27: git, partial journals, degraded Graphiti
- CC27 MVP: session_state_brief.py (Layer 0), cc_handoff.sh + git (Layer 1), autonomy ledger (trust state)
- "Graphiti valuable for relations but non-essential while Mac mini intermittent; deepen Layer 0+1 first"

---

## 4. Model Selection — Which Model for Which Task (CC40)

| Model | Best For | Under-Utilized Capability |
|-------|----------|---------------------------|
| Grok 4.20 | Thesis-first diagnosis, X mining | Full-repo traversal, structured 14-dim classification |
| Gemini 3.1 | Zero-shot classification, multimodal | 14-dim ontology scoring |
| Claude Opus 4.6 | Structured review loops, staging | — |
| Codex | Deterministic adapters, QA | — |

"Current setup asks models for prompts but not semantic projection or provenance graphs — capabilities that close the exact zero-vector and drift failures" (CC40)

### Specific Adapter Upgrade (CC42)
"Edit candidate_adapter.py lines 87-112 to replace pure keyword freq with Grok structured call (Pydantic 14-dim schema, git lineage in prompt, confidence scores); fallback keywords only for zero-match; write JSON directly to DYN-LATTICE_INDEX.json."

---

## 5. Multi-Agent Orchestration

**Dispatch**: auto_ingest_loop.sh polls inbox every 30s. Lifecycle: pending → active → done/failed. watch_dispatch.sh deprecated (race conditions).

**Relay**: Sequential single-file relay. ONE file on Desktop at a time. Commander creates prompt → relay script rsyncs to Desktop → Sovereign pastes to web agent → drags response into Commander inbox alias.

**Sovereign relay reduction** (CC40, not implemented):
- GitHub Actions + agent PRs
- Cloud relay via Claude Cowork/Perplexity Computer
- launchd-wrapped auto-ingest with notifications

**v2 hybrid direct Oracle↔Diviner dialogue** when alignment >0.85 (CC35, not implemented)

**Rate limit pooling**: Psyche + Adjudicator share ChatGPT Plus capacity pool. No simultaneous heavy jobs.

---

## 6. Infrastructure

**SSH config**: MBA→mini via `mini` alias, Mac mini→MBA via `macbook-air` alias. ICMP ping BLOCKED — use SSH for health checks.

**Cross-machine env vars**:
- MBA: `SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER=mini`, `AJNA=local`
- Mac mini: `SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA=macbook-air`, all others `local`

---

## 7. Pipeline Execution (CC30)

```bash
protease_queue.py --max-atoms 5
protease_promote.py --repo-root /path --axiom-file <file> --target praxis
protease_promote.py --repo-root /path --axiom-file <file> --target canon
integration_gate.py --repo-root /path --session-id <id>
auto_ingest_loop.sh
atom_cluster.py --mode=full
```

---

## 8. Automation (Not Implemented)

**CI-style validator** (CC40): "(1) diffs schema claims vs actual file count, (2) runs session_state_brief after every DAG write, (3) agent-audits README metrics"

**Feedcraft pipeline** (CC28): "feed (RSS/X/arXiv) → atom extraction → 6D cluster scoring → irrigation rule → usage feedback loop"

---

## 9. Named Practitioners from X/Twitter

| Practitioner | Pattern | Relevance |
|-------------|---------|-----------|
| **MotionViz** | skills.md workflow | "founder's taste defines the capability surface daily" |
| **Claudius Maximus** | Three-layer memory | "KG entities never deleted, daily log, weekly curated — human reviews and marks superseded" |
| **Heinrich** | Obsidian+Claude parallel agents | "agents extract claims but vault owner still decides MOC splits" |
| **Velinus** | Sage Protocol | "agent-owned skill libraries under protocol incentives — human taste as governance" |
| **Bryan Jenks** | Obsidian/Zettelkasten | 3-stage pipeline: fleeting → atomic → MOCs |
| **Tiago Forte** | BASB/PARA | "weekly review Friday 45 min, daily 5-min capture close, AI brief morning" |
| **Andy Matuschak** | Evergreen notes | "collection without distillation as primary failure mode" |
| **Replit 2025** | Trust recovery after DB deletion | "sandbox + planning-only (2 wk), monitored L2 (4 wk), gradual expansion" |
| **Swarm DJ / OpenFang** | Agent OS | "starts with 5-item human-gated batch exactly" for cold-start |
| **Stripe** | Minion pattern | "hybrid deterministic code + LLM for ambiguous nodes" |

---

## 10. Session Brief Specs (CC26)

Contents: "current priorities, open decisions, last 3 agent actions, graph health, one-sentence 'what changed since last'"

Design rationale: "respects AuDHD context-switching costs (external, visual, <15 min) and collapses orientation overhead from 50% to <10% immediately."

"When memory layer reaches 95% recall on audit, the brief auto-shortens to zero."

"Add Friday 20-minute weekly review only after three consecutive successful days."

---

## 11. Throughput Benchmarks

- Realistic throughput with AI: 300-500 atoms triaged per human hour; 30-50 meaningfully crystallized (CC26)
- "When human review backlog exceeds 500 atoms, the system is abandoned" (CC26)
- "Over 40% orientation time signals collapse" (CC26)
- "14,025 → 6 promotions is within normal range for high-fidelity early-stage curation (<5% until semantic gates mature)" (CC40)
- "2 promotions cost <200k tokens total" (CC42)
- Weekly throughput delta: canon_delta >= 1 per session (CC30)
- 3-atom batches for constrained bandwidth, scale to 5 post-proof (CC32/CC33)

---

## 12. What Oracle Consistently Prescribes (Cross-Session Pattern)

1. **Hybrid keyword+LLM ontology scoring** replacing pure keyword heuristics
2. **Sovereign taste as non-removable apex selector** with daily 5-atom veto queues
3. **4-connection minimum** as operational spine (ontology gate, config propagation, repo state, triangulation quality)
4. **MBA-only constellation viability** without Mac mini
5. **Cowork/Perplexity for ambient automation** while keeping canon gates sovereign
6. **Session state brief + git handoff** as the minimum memory that actually works for AuDHD context
