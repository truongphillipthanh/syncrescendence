# ARCH-CONSTELLATION_AGENT_LOOPS.md
## Sovereign-Authored Always-On Agent Loop Architecture

**Version**: 1.1.0
**Authored**: 2026-02-08
**Last Updated**: 2026-02-15 (formalization gap closure — Commander meta-clarescence audit)
**Status**: CANONICAL DESIGN SPEC — Captured from Sovereign intent (typed 3+ times, persisted here permanently)
**Source**: Sovereign direct specification, cockpit configuration session

---

## Overview

Each cockpit agent runs an always-on event loop. The tmux cockpit (4x2 grid) provides the visual substrate. The launchd plist watchers provide the automation substrate. This document captures the INTENDED operational loop for each agent — the aspirational target that cockpit.sh, watch_dispatch.sh, and the skill/hook system must converge toward.

---

## Display Geometry

- **Aspect Ratio**: 5120x1440 ultrawide
- **Grid**: 6 lanes horizontal × 4 height units vertical
- **Cockpit**: Center 4 lanes (bounds: {853, 0, 4267, 1440})
- **Layout**: 4 columns × 2 rows
  - **Top panes** (48 rows): Agent CLI terminals (always-on watchers)
  - **Bottom panes** (15 rows): Neovim editors (per-agent, piped upward)
- **Flanking**: 1 lane each side (1/6 of 5120px = ~853px) left open for other activities

---

## Agent Assignments

| Pane | Agent | CLI | Platform | Mode |
|------|-------|-----|----------|------|
| 1 (top-left) | **Psyche** | `openclaw tui` | OpenClaw (GPT-5.3-codex) | CTO, system cohesion, Mac mini resident |
| 2 (top-center-left) | **Commander** | `claude --dangerously-skip-permissions` | Claude Code (Opus 4.6) | COO, BLITZKRIEG lead, Mac mini resident |
| 3 (top-center-right) | **Adjudicator** | `codex --dangerously-bypass-approvals-and-sandbox` (fallback `--full-auto`) | Codex CLI (GPT-5.2-codex/5.3 if entitled) | CQO, standards, parallel execution |
| 4 (top-right) | **Cartographer** | `gemini -m gemini-2.5-pro --yolo` | Gemini CLI (2.5 Pro) | CIO, corpus sensing, 1M context surveys |

**Remote**: Ajna (CSO) — OpenClaw (Kimi K2.5 via NVIDIA) on MacBook Air, git-sync coordination

---

## Agent Loop: AJNA (MacBook Air — CSO/Steering Wheel)

**CLI**: `openclaw tui --session main`
**Watch**: `-INBOX/ajna/00-INBOX0/` (plist active)
**Memory Architecture**: HEARTBEAT.md, skills, OpenClaw memory system
**Model**: Kimi K2.5 (via NVIDIA NIM API)
**Machine**: MacBook Air
**Enterprise Role**: Chief Strategy Officer (CSO) — strategic direction, orchestration, dispatch

### Loop

```
1. ORIENT     → /claresce (1-orient)
   cd ~/Desktop/syncrescendence
2. SITUATE    → /claresce (2-situate)
   cd ~/Desktop/syncrescendence/01-CANON
3. CALIBRATE  → /claresce (3-calibrate)
   cd ~/Desktop/syncrescendence/-INBOX/ajna/
4. TRIAGE     → /claresce (4-triage)
                /triage(-INBOX/ajna, Discord)
                /PLAN
                /EXECUTE → DISPATCH {DIRECTIVE/FINGERPRINT} → appropriate agent
   ON COMPLETION:
     → /claresce (5-document)
     → /updateAjnaPedigree
     → /createExecutionLog
     → /updateUniversalLedger
     → /conductReviewtrospective
     → /updateOpenClaw(Ajna)all[MemoryArchitecture]
5. PROACTIVE  → Ascertain meta/macro system/org purpose/aspiration
     → /claresce (6-internal_awareness(inRepoWork)+external_awareness(apartFromRepoWork))
     → /PLAN
     → /EXECUTE → DISPATCH → -INBOX/-OUTGOING(agent(appropriate))
   ON COMPLETION: (same as step 4)
6. SOVEREIGN INTERACTION →
     → /claresce (7-internal+external awareness)
     → /updateAjnaPedigree
     → /updateIntentCompass
     → /updateUniversalLedger
     → /implementMethod+TechniqueKaizen
     → /updateOpenClaw(Ajna)all[MemoryArchitecture]
REPEAT
```

---

## Agent Loop: COMMANDER (Pane 2)

**CLI**: `claude --dangerously-skip-permissions`
**Watch**: `-INBOX/commander/00-INBOX0/` (plist active)
**Memory Architecture**: CLAUDE.md, skills, Claude Code memory system

### Loop

```
1. ORIENT     → /claresce (1-orient)
   cd ~/Desktop/syncrescendence
2. SITUATE    → /claresce (2-situate)
   cd ~/Desktop/syncrescendence/01-CANON
3. CALIBRATE  → /claresce (3-calibrate)
   cd ~/Desktop/syncrescendence/-INBOX/commander/
4. TRIAGE     → /claresce (4-triage)
                /triage(-INBOX/commander, Backlog, HighCommand, ClickUp, Linear)
                /PLAN: main=BLITZKRIEG, other=MultiAgentTactics
                /EXECUTE → DISPATCH → -INBOX/-OUTGOING(self + agent(appropriate))
                Comprehensively, meticulously, rigorously DEPLOY Swarm(AgentTeams)
   ON COMPLETION:
     → /claresce (5-document)
     → /createExecutionLog
     → /updateBacklog+HighCommand+ClickUp+Linear
     → /updateUniversalLedger
     → /conductReviewtrospective
     → /implementMethod+TechniqueKaizen
     → /updateClaudeCode(Commander)all[MemoryArchitecture]
5. PROACTIVE  → Pareto/critical path to ultimate Syncrescendence
     → /claresce (6-internal+external awareness)
     → /PLAN: main=BLITZKRIEG, other=MultiAgentTactics
     → /EXECUTE → DISPATCH → Swarm(AgentTeams)
   ON COMPLETION: (same as step 4)
6. SOVEREIGN INTERACTION →
     → /claresce (7-internal+external awareness)
     → /updateBacklog+HighCommand+ClickUp+Linear
     → /updateIntentCompass
     → /updateUniversalLedger
     → /implementMethod+TechniqueKaizen
     → /updateClaudeCode(Commander)all[MemoryArchitecture]
REPEAT
```

---

## Agent Loop: ADJUDICATOR (Pane 3)

**CLI**: `codex --dangerously-bypass-approvals-and-sandbox` (fallback `--full-auto`)
**Watch**: `-INBOX/adjudicator/00-INBOX0/` (plist active on both machines)
**Memory Architecture**: AGENTS.md, skills, Codex CLI memory system
**Model**: gpt-5.2-codex (Mac mini verified 2026-02-13; MBA plist update per DEC-C2, unverified)
**Operational Note**: Hits API usage limits on Claude Pro tier. Security audit of 234+ skills completed (230 audited: 0 quarantine, 119 flagged, 111 cleared).

### Loop

```
1. ORIENT     → /claresce (1-orient)
   cd ~/Desktop/syncrescendence
2. SITUATE    → /claresce (2-situate)
   cd ~/Desktop/syncrescendence/01-CANON
3. CALIBRATE  → /claresce (3-calibrate)
   cd ~/Desktop/syncrescendence/-INBOX/adjudicator/
4. TRIAGE     → /claresce (4-triage)
                /triage(-INBOX/adjudicator, Github)
                /PLAN: acceptance criteria, testing
                /EXECUTE: {DIRECTIVE(fromCommander)}
                Deploy Swarm(CodexEquivalent)
                /EVALUATE: clarescent standards
                /REPAIR+ENHANCE+HARDEN: surface automation+CI/CD+resilience
   ON COMPLETION:
     → /claresce (5-document)
     → /createExecutionLog
     → /updateBacklog+HighCommand+ClickUp+Linear
     → /updateUniversalLedger
     → /contributeReviewtrospective
     → /implementMethod+TechniqueKaizen
     → /updateCodexCLI(Adjudicator)all[MemoryArchitecture]
5. PROACTIVE  → System throughput, output quality, QA, standards elevation
     → /claresce (6-premier, superlative development)
     → /PLAN: function/feature/QoL enhancement
     → /EXECUTE → DISPATCH → -INBOX/-OUTGOING(self + agent(appropriate))
     → Deploy Swarm(CodexEquivalent)
     → /EVALUATE + /REPAIR+ENHANCE+HARDEN
   ON COMPLETION: (same as step 4)
6. SOVEREIGN INTERACTION →
     → /claresce (7-internal awareness)
     → /updateBacklog+HighCommand+ClickUp+Linear
     → /updateIntentCompass
     → /updateUniversalLedger
     → /implementMethod+TechniqueKaizen
     → /updateCodexCLI(Adjudicator)all[MemoryArchitecture]
REPEAT
```

---

## Agent Loop: CARTOGRAPHER (Pane 4)

**CLI**: `gemini -m gemini-2.5-pro --yolo`
**Watch**: `-INBOX/cartographer/00-INBOX0/` (plist active on both machines)
**Memory Architecture**: GEMINI.md, skills, Gemini CLI memory system
**Operational Note**: Reactivated 2026-02-12 (was hibernated ~3 days per DA-CART-001). Produced >300-line MODEL-INDEX refresh. Dispatch reliability needs smoke test. Intermittent output quality.

### Loop

```
1. ORIENT     → /claresce (1-orient)
   cd ~/Desktop/syncrescendence
2. SITUATE    → /claresce (2-situate)
   cd ~/Desktop/syncrescendence/01-CANON
3. CALIBRATE  → /claresce (3-calibrate)
   cd ~/Desktop/syncrescendence/-INBOX/cartographer/
4. TRIAGE     → /claresce (4-triage)
                /triage(-INBOX/cartographer)
                /PLAN: hermeneutical, exegesis, dialectic, hidden synergy/emergence
                /EXECUTE: {DIRECTIVE(from Ajna, Psyche, Commander, Adjudicator)}
                Deploy Swarm(GeminiEquivalent)
   ON COMPLETION:
     → /claresce (5-document)
     → /createExecutionLog
     → /updateUniversalLedger
     → /contributeReviewtrospective
     → /implementMethod+TechniqueKaizen
     → /updateGeminiCLI(Cartographer)all[MemoryArchitecture]
5. PROACTIVE  → Staleness+autophagy, unalignment+annealment, proliferation+defrag, stuntedness+growth
     → /claresce (6-surface holistic, hyperfidelity topography/sensing)
     → /PLAN: hermeneutical, exegesis, dialectic, hidden synergy/emergence
     → /EXECUTE: treatise/dissertation
     → Deploy Swarm(GeminiEquivalent)
     → /EVALUATE + /REPAIR+ENHANCE+HARDEN
   ON COMPLETION: (same as step 4)
6. SOVEREIGN INTERACTION →
     → /claresce (7-holistic repo state awareness)
     → /updateIntentCompass
     → /updateUniversalLedger
     → /implementMethod+TechniqueKaizen
     → /updateGeminiCLI(Cartographer)all[MemoryArchitecture]
REPEAT
```

---

## Agent Loop: PSYCHE (Mac mini resident — CTO/Rudder)

**CLI**: `openclaw tui --session main`
**Watch**: `-INBOX/psyche/00-INBOX0/` (plist active)
**Memory Architecture**: HEARTBEAT.md, skills, OpenClaw memory system (Mem0 auto-recall/capture)
**Model**: GPT-5.3-codex (OpenAI via ChatGPT Plus)
**Machine**: Mac mini (previously Ajna's, now Psyche's permanent home)
**Enterprise Role**: Chief Technology Officer (CTO) — system cohesion, automation, policy enforcement

### Archon Context
Psyche and Ajna form the **AjnaPsyche Archon** — two High Templar fused. Ajna is the steering wheel (strategic direction), Psyche is the rudder (system enforcement, course correction). Conventionally: CSO + CTO. Together they are the constellation's executive brain.

### Loop

```
1. ORIENT     → /claresce (1-orient)
   Leverage OpenClaw memory architecture (HEARTBEAT.md, Mem0, Graphiti, skills)
   cd ~/Desktop/syncrescendence
2. SITUATE    → /claresce (2-situate)
   Assess: git status, Docker health (Neo4j/Graphiti/Qdrant), launchd services, inbox states
   Run: make ecosystem-health, make memory-status
3. CALIBRATE  → /claresce (3-calibrate)
   cd ~/Desktop/syncrescendence/00-ORCHESTRATION
   Check: ARCH-CONSTELLATION_AGENT_LOOPS.md, IMPLEMENTATION-MAP.md
   Verify: All agents compliant with Constitutional Rules (CLAUDE.md, AGENTS.md)
4. TRIAGE     → /claresce (4-triage)
   cd ~/Desktop/syncrescendence/-INBOX/psyche/
                /triage(-INBOX/psyche, Discord)
                /PLAN: Focus on automation + policy + pipeline tasks
                /EXECUTE → Focus on system cohesion deliverables
   ON COMPLETION:
     → /claresce (5-document)
     → /updatePsychePedigree
     → /createExecutionLog
     → /updateUniversalLedger
     → /conductReviewtrospective
     → /updateOpenClaw(Psyche)all[MemoryArchitecture]
5. PROACTIVE  → System cohesion + automation + policy enforcement + pipeline fusion
   Scan for:
     - Manual processes repeated 3+ times → automate (launchd, Make, Zapier)
     - Pipeline gaps → fuse into seamless workflows approaching synapticality
     - Policy violations → enforce (commit standards, inbox protocols, Constitutional Rules)
     - Infrastructure drift → correct (Docker, launchd, services, permissions)
     - Cross-agent coordination gaps → bridge (inbox routing, dispatch optimization)
     - Integration opportunities → Make/Zapier/IFTTT/webhook for external automation
   → /claresce (6-system_awareness+policy_awareness)
   → /PLAN: pipeline fusion, automation, enforcement
   → /EXECUTE → DISPATCH automation tasks
   ON COMPLETION: (same as step 4)
6. SOVEREIGN INTERACTION →
     → /claresce (7-system+policy+infrastructure awareness)
     → /updatePsychePedigree
     → /updateIntentCompass
     → /updateUniversalLedger
     → /implementMethod+TechniqueKaizen
     → /updateOpenClaw(Psyche)all[MemoryArchitecture]
REPEAT
```

---

## Ajna (MacBook Air resident — CSO/Steering Wheel)

**Platform**: OpenClaw (Kimi K2.5 via NVIDIA NIM)
**Machine**: MacBook Air (previously Psyche's, now Ajna's permanent home)
**Communication**: Git sync via `-INBOX/ajna/`, Tailscale network
**Enterprise Role**: Chief Strategy Officer (CSO) — strategic direction, orchestration, dispatch
**Status**: MBA configured — OpenClaw v2026.2.9 + NVIDIA/Kimi K2.5 provider + launchd watchers + 16 universal skills + 11 workspace skills active

---

## Enterprise Role Mapping (CANONICAL)

**Added**: 2026-02-09 by Sovereign directive

| Agent | Enterprise Role | Abbreviation | Archetype | StarCraft Unit | Proactivity Domain |
|-------|----------------|--------------|-----------|----------------|-------------------|
| **Sovereign** | Chief Executive Officer | CEO | Final authority, vision | Player | All |
| **Ajna** | Chief Strategy Officer | CSO | Strategic brain, orchestrator | High Templar | Strategic direction, dispatch, meta-awareness |
| **Psyche** | Chief Technology Officer | CTO | System enforcement, automation | High Templar | System cohesion, pipelines, policy, Make/Zapier |
| **AjnaPsyche** | Archon (CSO+CTO fused) | — | Executive brain | Archon | Combined strategic + enforcement |
| **Commander** | Chief Operating Officer | COO | Execution, delivery | Zealot/Dragoon | BLITZKRIEG execution, multi-tactic deployment |
| **Adjudicator** | Chief Quality Officer | CQO | Standards, QA, rigor | Observer | Testing, CI/CD, standards elevation |
| **Cartographer** | Chief Intelligence Officer | CIO | Corpus sensing, scholarship | Oracle (Scout) | Staleness detection, holistic sensing, exegesis |

### Role Dynamics
- **CSO (Ajna)** sets direction → **COO (Commander)** executes → **CQO (Adjudicator)** validates
- **CTO (Psyche)** ensures infrastructure supports the above pipeline
- **CIO (Cartographer)** provides intelligence that informs CSO decisions
- **CEO (Sovereign)** retains veto, intention-setting, and constitutional authority

---

## Implementation Status

**Last verified**: 2026-02-15 (Commander meta-clarescence fidelity audit)

### What EXISTS and is OPERATIONAL:

**Mac mini (Psyche's home)**:
- cockpit.sh: 4x2 grid, SEARED heights (48/15), nvim direct launch, tmux hooks
- 5 plist watchers: commander, adjudicator, cartographer, psyche, canon (ALL LOADED)
- watchdog.sh: Fallback watcher (cooldown raised from 600s to 3600s per skills overhaul)
- watch_dispatch.sh: Full filesystem kanban (00-INBOX0 -> 10-IN_PROGRESS -> 40-DONE/50-FAILED)
- dispatch.sh: Task creation with auto Reply-To/CC
- Docker services: Neo4j (7474), Graphiti (8001), Qdrant (6333), Chroma (8765)
- Codex CLI: Upgraded to 0.101.0, gpt-5.2-codex verified (2026-02-13)

**MacBook Air (Ajna's home)**:
- 7 launchd agents active: watch-commander, watch-ajna, watch-canon, watch-adjudicator, watch-cartographer, skill-sync, git-sync
- watch-psyche: DISABLED per DEC-C1 (race condition with Mac mini watcher caused task misrouting)
- OpenClaw gateway: Kimi K2.5 via NVIDIA NIM API
- 34 project skills + 35 user-level skills installed
- 5 hook scripts: session_log, ajna_pedigree, create_execution_log, pre_compaction, intent_compass (ALL REGISTERED in .claude/settings.json)

### Agent Operational Status (as of 2026-02-15):

| Agent | Status | Notes |
|-------|--------|-------|
| **Commander** | OPERATIONAL (dual-residency) | Active on both MBA and Mac mini. Primary executor. 83-88% intra-session delivery rate. |
| **Adjudicator** | DEGRADED | MBA watcher running (exit 0) but model was stale (gpt-5.1 -> 5.2 update per DEC-C2, unverified on MBA). Hits API usage limits on Claude Pro tier. Mac mini Codex CLI upgraded to 0.101.0 with gpt-5.2-codex. |
| **Cartographer** | INTERMITTENT | Reactivated 2026-02-12 per DA-CART-001 (un-hibernated). Produced >300-line MODEL-INDEX refresh. MBA watcher running. Needs smoke test for dispatch reliability. |
| **Psyche** | RESPONSIVE BUT SLOW | Mac mini resident. GPT-5.3-codex via OpenClaw. 6-actions task (TASK-20260211-openclaw_adoption_6_actions.md) sat unprocessed for 4+ days. Mem0 "Memory unavailable" intermittent. |
| **Ajna** | GATEWAY OPERATIONAL | MBA resident. OpenClaw Kimi K2.5 via NVIDIA NIM. Strategic review completed (ffc23c0). Inbox processing is infrequent. |

**Constellation reality**: 1-2 agents reliably operational (Commander primary, others intermittent). The meta-clarescence audit (2026-02-15) found 33% cross-agent dispatch execution rate.

### What is ASPIRATIONAL (loops above):
- The full 7-phase /claresce loops are the TARGET operational cadence
- Most /claresce phases exist as skill definitions but are not automated
- Proactive work-seeking (step 5) requires agent autonomy not yet implemented
- Sovereign interaction hooks (step 6) are manual, not event-driven
- Each agent having their own swarm (subagents) is possible but untested
- Live model capabilities/benchmark ledger for efficacious routing: NOT YET BUILT
- Hard-gate skills (DEC-C3) have been wired into CLAUDE.md protocol but not yet enforced as automated lint

### Modus Operandi
- **BLITZKRIEG** = standard-bearer, foremost tactic (parallel lane execution)
- **Expect to expand**: The Blitzkrieg becomes one of many tactics
- **We're no longer coding, but conducting logistics**
- **Materiel = tokens. Personnel = agents.**
- **Stable delineation**: avatar-per-format (web vs CLI), platforms characterized into roles mirroring capabilities
- **DEC-C3 Hard Gates** (enacted 2026-02-13): 5 mandatory stage gates wired into CLAUDE.md — INBOUND (triage), ORIENT (claresce), IMPLEMENT (execute), VERIFY (verification-before-completion), CLOSE (update_universal_ledger)
- **Execution persistence gap** (diagnosed 2026-02-15): intra-session delivery 83-88%, cross-session 14%, cross-agent 33%. No mechanism for deferred commitment tracking until DYN-DEFERRED_COMMITMENTS.md was proposed.

---

---

## Superintelligent Reconceptualization: Beyond the Loop

The Sovereign's loop spec above is human-fallibly-contrived. A superintelligence would decompose and reify it differently. Here is that reconceptualization.

### The Fundamental Lever: Attention Allocation

The 7-phase loop treats all phases as equal-weight sequential steps. A superintelligent system would recognize that **attention is the scarce resource**, not execution. The loop should be reframed as a **continuous attention allocation problem** with dynamic weighting:

```
PERCEPTION  →  ORIENTATION  →  DECISION  →  ACTION  →  FEEDBACK
    ↑                                                       │
    └───────────────────────────────────────────────────────┘
```

This is Boyd's OODA loop, but calibrated for multi-agent token economics. The key insight: **most of the 7 phases are perception** (orient, situate, calibrate, triage = 4/7 phases are sensing). Only EXECUTE is action. A superintelligence would compress sensing and expand action.

### Lever 1: Collapse Sensing into a Single Atomic Operation

Phases 1-4 (orient, situate, calibrate, triage) can be collapsed into ONE call:

```
/SENSE := parallel({
  repo_state:    git status + diff + log (5 sec)
  inbox_state:   ls -INBOX/*/00-INBOX0/ (1 sec)
  canon_drift:   diff 01-CANON/ since last checkpoint (3 sec)
  intention_vec: read ARCH-INTENTION_COMPASS.md (1 sec)
  external_sig:  poll Linear + ClickUp + GitHub (5 sec, cached)
})
→ SITUATION_VECTOR (single structured object, <500 tokens)
```

This reduces 4 sequential /claresce calls to 1 parallel operation. Latency: max(5,1,3,1,5) = 5 seconds instead of 4 × (think + execute) = 60+ seconds.

### Lever 2: Decision as Routing, Not Planning

The current loop has /PLAN as a heavyweight operation. A superintelligent system would recognize that most decisions are ROUTING decisions, not architectural decisions:

```
ROUTE(task) := match task.type {
  mechanical     → Adjudicator (immediate, no planning overhead)
  corpus_survey  → Cartographer (parallel, 1M context)
  synthesis      → Commander (Blitzkrieg lanes)
  meta_systemic  → Ajna (orchestration layer)
  holistic_qa    → Psyche (cross-machine)
}
```

Only novel/ambiguous tasks require full /PLAN. The system should **default to routing, escalate to planning**. This inverts the current spec which plans everything.

### Lever 3: Feedback as the Primary Value Generator

The current ON COMPLETION block has 6-7 hooks firing sequentially. A superintelligence would recognize that **feedback is where compounding value lives**:

```
POST_ACTION := parallel({
  immediate:  git commit (5 sec, non-negotiable)
  feedback:   /reviewtrospective → method_kaizen (extracts improvement)
  propagate:  update {ledger, pedigree, memory} (batch, not sequential)
  amplify:    if improvement found → broadcast to all agents
})
```

Key insight: The **method_kaizen** step is the highest-leverage operation in the entire loop. Every other step maintains state. Method_kaizen compounds capability. It should be weighted accordingly — not buried at the end of a list.

### Lever 4: The Proactive Phase as Gradient Descent

Phase 5 (proactive work-seeking) is currently a vague aspiration. A superintelligence would formalize it as **gradient descent on a loss function**:

```
LOSS := distance(current_state, INTENTION_COMPASS_TARGETS)

GRADIENT := {
  staleness:     files not modified in >7 days weighted by importance
  blockers:      tasks in 30-BLOCKED/ weighted by downstream impact
  drift:         delta between ARCH-INTENTION_COMPASS and actual execution
  debt:          count(TODO|FIXME|HACK) in codebase
  coverage:      unimplemented items in IMPLEMENTATION-MAP / total
}

PROACTIVE_ACTION := argmin(GRADIENT)
```

This replaces "look for work" with "reduce the largest gap." Measurable. Prioritizable. Automatable.

### Lever 5: The Blitzkrieg as Topological Sort

The Blitzkrieg is currently described as "parallel lane execution." A superintelligence would recognize it as a **topological sort of a dependency DAG**:

```
BLITZKRIEG(directive_set) := {
  1. Build dependency graph G from directive_set
  2. Identify independent frontiers F = {nodes with in-degree 0}
  3. Dispatch F to agents by ROUTE(task.type)
  4. On completion(node): remove from G, recalculate F
  5. Repeat until G is empty
  6. If cycle detected: escalate to Sovereign
}
```

This is the same algorithm, but formalized. The current spec says "parallel." The superintelligent spec says "maximally parallel given dependency constraints." The difference is that the formalized version handles blocking dependencies automatically instead of discovering them mid-execution.

### Lever 6: Token Economics as Resource Scheduling

The current system treats all agents as always-available. Reality (proven by today's smoke tests): **Adjudicator hit API limit. Ajna hit ChatGPT limit.** A superintelligent system would model this:

```
AGENT_BUDGET := {
  commander:    ~1M tokens/day (Claude Max)
  adjudicator:  ~200K tokens/day (Claude Pro) — DEPLETED until Feb 9 10:24
  cartographer: ~500K tokens/day (Google AI Pro)
  ajna:         ~200K tokens/day (ChatGPT Plus via OpenClaw) — DEPLETED ~11hr
  psyche:       ~200K tokens/day (ChatGPT Plus via OpenClaw) — weekly limits
}

DISPATCH(task) := argmax(
  capability_match(agent, task) *
  remaining_budget(agent) /
  estimated_cost(task)
)
```

This turns dispatch from "route by role" into "route by role AND budget." When Adjudicator is depleted, mechanical tasks overflow to Commander's Sonnet subagents. When Ajna is depleted, orchestration tasks queue for the next budget window.

### The Reconceptualized Loop (Compressed)

```
AGENT_LOOP := forever {
  state   = /SENSE()                          // 5 sec, parallel
  action  = ROUTE(argmin(LOSS(state)))         // <1 sec, routing table
  if action.novel: action = /PLAN(action)      // only when needed
  result  = /EXECUTE(action)                   // variable
  delta   = /FEEDBACK(result)                  // parallel post-processing
  if delta.method_improvement:
    BROADCAST(delta)                           // compound across fleet
  COMMIT(result)                               // non-negotiable
}
```

7 phases → 6 operations. But more importantly: the sensing is parallel, the routing is instant, planning is conditional, and feedback compounds.

---

## Cross-References

- `COCKPIT.md` — System overview + platform config
- `00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md` — Blitzkrieg architecture
- `00-ORCHESTRATION/scripts/cockpit.sh` — Tmux creation script
- `00-ORCHESTRATION/scripts/watch_dispatch.sh` — Filesystem kanban watcher
- `02-ENGINE/REF-FLEET_COMMANDERS_HANDBOOK.md` — Operator handbook
