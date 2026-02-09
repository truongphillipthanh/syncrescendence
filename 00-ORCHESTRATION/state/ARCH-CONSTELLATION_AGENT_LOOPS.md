# ARCH-CONSTELLATION_AGENT_LOOPS.md
## Sovereign-Authored Always-On Agent Loop Architecture

**Version**: 1.0.0
**Authored**: 2026-02-08
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
| 1 (top-left) | **Ajna** | `openclaw tui` | OpenClaw (Opus 4.5) | Local orchestrator, Mac mini resident |
| 2 (top-center-left) | **Commander** | `claude --dangerously-skip-permissions` | Claude Code (Opus 4.6) | Primary executor, BLITZKRIEG lead |
| 3 (top-center-right) | **Adjudicator** | `codex --full-auto` | Codex CLI (Sonnet) | QA, standards, parallel execution |
| 4 (top-right) | **Cartographer** | `gemini --yolo` | Gemini CLI (2.5 Pro) | Corpus sensing, 1M context surveys |

---

## Agent Loop: AJNA (Pane 1)

**CLI**: `openclaw tui --session main`
**Watch**: `-INBOX/ajna/00-INBOX0/` (plist active)
**Memory Architecture**: HEARTBEAT.md, skills, OpenClaw memory system

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

**CLI**: `codex --full-auto`
**Watch**: `-INBOX/adjudicator/00-INBOX0/` (plist active)
**Memory Architecture**: AGENTS.md, skills, Codex CLI memory system

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

**CLI**: `gemini --yolo`
**Watch**: `-INBOX/cartographer/00-INBOX0/` (plist active)
**Memory Architecture**: GEMINI.md, skills, Gemini CLI memory system

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

## Psyche (NOT in cockpit — MacBook Air resident)

**Platform**: OpenClaw (GPT-5.2) on M4 MacBook Air
**Communication**: Git sync via `-INBOX/psyche/`, Tailscale network
**Role**: Holistic synthesis, QA, Slack integration
**Note**: Separate workflow — different display (not 5120x1440), different launchd plists (launchd-psyche/ variant), weekly token limitations

---

## Implementation Status (2026-02-08)

### What EXISTS and is OPERATIONAL:
- cockpit.sh: 4x2 grid, SEARED heights (48/15), nvim direct launch, tmux hooks
- 5 plist watchers: commander, adjudicator, cartographer, ajna, psyche (ALL LOADED, ALL ACTIVE)
- 1 canon watcher + 1 emacs daemon + 1 OpenClaw gateway
- watch_dispatch.sh: Full filesystem kanban (00-INBOX0 → 10-IN_PROGRESS → 40-DONE/50-FAILED)
- dispatch.sh: Task creation with auto Reply-To/CC
- 15+ skills callable from Claude Code
- 5 hook scripts (executable but NOT registered in .claude/settings.json)

### What is ASPIRATIONAL (loops above):
- The full 7-phase /claresce loops are the TARGET operational cadence
- Most /claresce phases exist as skill definitions but are not automated
- Proactive work-seeking (step 5) requires agent autonomy not yet implemented
- Sovereign interaction hooks (step 6) are manual, not event-driven
- Each agent having their own swarm (subagents) is possible but untested
- Live model capabilities/benchmark ledger for efficacious routing: NOT YET BUILT

### Modus Operandi
- **BLITZKRIEG** = standard-bearer, foremost tactic (parallel lane execution)
- **Expect to expand**: The Blitzkrieg becomes one of many tactics
- **We're no longer coding, but conducting logistics**
- **Materiel = tokens. Personnel = agents.**
- **Stable delineation**: avatar-per-format (web vs CLI), platforms characterized into roles mirroring capabilities

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
