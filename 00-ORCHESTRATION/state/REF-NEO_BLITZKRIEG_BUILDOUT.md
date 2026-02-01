# NEO-BLITZKRIEG BUILDOUT PLAN
## Manhattan Project for Constellation Operationalization

**Version**: 1.0.0
**Created**: 2026-02-01
**Authority**: Oracle 13 / Sovereign directive
**Status**: ACTIVE

---

## What Is Neo-Blitzkrieg?

Neo-Blitzkrieg is the synthesis of five automation layers into a unified execution engine:

```
SOVEREIGN INPUT
     │
     ▼
┌─────────────────────────────────┐
│  INTENT COMPASS (UserPromptSubmit)│  ← Captures intention signals
│  intent_compass.sh               │     on every input
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  AJNA PEDIGREE (Stop)            │  ← Captures decision lineage
│  ajna_pedigree.sh                │     at session end
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  DIRECTIVE + EXECUTION LOG       │  ← Codified production
│  create_directive.sh             │     + auto-compaction
│  create_execution_log.sh         │     into wisdom
│  compact_wisdom.sh               │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  DISPATCH SYSTEM                 │  ← Autonomous twin triggering
│  dispatch_to_psyche.sh           │     + CLI tool enlistment
│  watch_dispatch.sh               │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  BLITZKRIEG LANES                │  ← Parallel execution
│  Lane A: Commander (Claude Max)  │     across CLI tools
│  Lane B: Adjudicator (Codex)     │
│  Lane C: Cartographer (Gemini)   │
│  Lane D: Psyche (autonomous QA)  │
└─────────────────────────────────┘
```

The original Blitzkrieg was manual: Sovereign crafts directives, dispatches to lanes, collects results. Neo-Blitzkrieg automates the connective tissue so the Sovereign's raw input flows through the system with minimal relay overhead.

---

## Operational Infrastructure (Built)

| Layer | Script | Hook Event | Output |
|-------|--------|------------|--------|
| Intent Compass | `intent_compass.sh` | UserPromptSubmit | `DYN-INTENTIONS_QUEUE.md` |
| Ajna Pedigree | `ajna_pedigree.sh` | Stop | `DYN-PEDIGREE_LOG.md` |
| Session Log | `session_log.sh` | Stop | `DYN-SESSION_LOG.md` |
| Execution Log | `create_execution_log.sh` | Stop | `DYN-EXECUTION_STAGING.md` |
| Pre-Compaction | `pre_compaction.sh` | PreCompact | stdout warning |
| Directive Gen | `create_directive.sh` | Manual | `DYN-DIRECTIVE_STAGING.md` |
| Wisdom Compaction | `compact_wisdom.sh` | Manual (threshold=10) | Appends to compendiums |
| Twin Dispatch | `dispatch_to_psyche.sh` | Manual | `DISPATCH-PSYCHE-*.md` |
| Dispatch Watcher | `watch_dispatch.sh` | Background process | Triggers processing |

All scripts in `00-ORCHESTRATION/scripts/`. All hooks configured in `.claude/settings.json`.

---

## What Still Needs Building

### Phase 1: Consolidation (Current Sprint)

| # | Item | Priority | Effort | Status |
|---|------|----------|--------|--------|
| 1 | CANON lean-out (3 merge pairs approved) | P1 | Medium | APPROVED, not started |
| 2 | Build `sn_expand.py` for ${DEF} variable resolution | P1 | Medium | Not started |
| 3 | Codex CLI AGENTS.md configuration | P2 | Low | Not started |
| 4 | Gemini CLI API key setup on Account 2 | P2 | Low | Not started |
| 5 | Install `fswatch` on both machines | P2 | Low | Not started |
| 6 | Branch merge: `refactor/restructure-v3` → main | P1 | Low | APPROVED |

### Phase 2: FDIS Foundation

**FDIS** = Field Deployable Intelligence System. The culmination of Syncrescendence: a portable, self-contained intelligence infrastructure that can be deployed in any environment.

| # | Item | Priority | Dependency | Notes |
|---|------|----------|------------|-------|
| 7 | Triangulate FDIS requirements from CANON + Compass + Backlog | P1 | Phase 1 | Cross-reference intentions, decisions, and canonical architecture |
| 8 | Define FDIS deployment surface (hardware, software, network) | P1 | #7 | What does a "field node" look like in Modal 1? |
| 9 | Palantir integration prototype | P2 | #7 | Foundry/AIP as the analytical backbone |
| 10 | Linear onboarding | P2 | DYN-Backlog reconciliation | Project management modernization |

### Phase 3: Backlog Reconciliation

The DYN-Backlog needs to reconcile three tracking systems:

```
CURRENT STATE:
  DYN-BACKLOG.md ←── Manual markdown (30+ items, partially stale)
  Claude Code tasks ←── In-session task list (ephemeral per session)
  ARCH-INTENTION_COMPASS.md ←── Rolling intention tracker

TARGET STATE:
  Linear (cloud PM) ←── Source of truth for project/task tracking
  DYN-BACKLOG.md ←── Snapshot/cache synced from Linear
  Claude Code tasks ←── Session-scoped execution derived from Linear
  ARCH-INTENTION_COMPASS.md ←── Feeds into Linear via Intent Compass → triage
```

| # | Item | Priority | Notes |
|---|------|----------|-------|
| 11 | Audit DYN-BACKLOG.md against current state | P1 | Many items resolved by restructure |
| 12 | Design Linear workspace structure | P2 | Teams = Constellation roles? Projects = PROJ-XXX? |
| 13 | Build Linear ↔ DYN-BACKLOG sync (MCP or API) | P3 | Requires Linear MCP server or custom script |
| 14 | Claude Code TodoWrite → Linear integration | P3 | Research: can hooks push to Linear API? |

### Phase 4: Velocity Management

Claude Max ($100/mo) provides ~5x usage but depletes faster due to primary execution load.

| Strategy | Implementation | Priority |
|----------|---------------|----------|
| Offload to Adjudicator | Route mechanical tasks (tests, formatting) to Codex CLI on Account 2 | P1 |
| Offload to Cartographer | Route corpus surveys to Gemini CLI on Account 2 | P1 |
| Model downshift | Use Sonnet for routine work, Opus for architecture/decisions | P2 |
| Psyche QA delegation | Dispatch QA tasks to Psyche instead of Commander self-checking | P2 |
| Session budgeting | Track token usage per session, alert at 50% daily budget | P3 |

---

## Palantir Culmination Path

The Sovereign's long-term vision positions Palantir (Foundry/AIP) as the analytical culmination:

```
Modal 1 (Current — Abstraction):
  Syncrescendence corpus → Semantic Notation → Knowledge graph

Modal 2 (2027-2030 — Simulation):
  Knowledge graph → Palantir Foundry ontology → Visual analysis
  FDIS field nodes → Palantir AIP integration → Decision support

Modal 3+ (2031+ — Embodiment):
  Palantir + physical sensors → Distributed intelligence → Field operations
```

**Current actionable**: Study Palantir Foundry's ontology system. Map it against our SN ontology (DEF variables, ROSETTA STONE terms, CANON structure). Identify impedance mismatches early.

---

## MCP Server Buildout

MCPs (Model Context Protocol servers) enable cross-tool data sharing:

| MCP Server | Purpose | Priority | Status |
|------------|---------|----------|--------|
| Filesystem | Local file access for all CLIs | P0 | Configured (gemini-settings.json) |
| GitHub | PR, issues, code review | P1 | Configured (template) |
| Fetch | Web content retrieval | P2 | Configured (template) |
| Slack | Psyche ↔ Ajna communication | P2 | Not started |
| Linear | Task sync | P3 | Not started |
| Google Drive | Gemini Web live sync | P3 | Not started |

---

## Neo-Blitzkrieg Execution Flow (Target State)

```
1. SOVEREIGN types prompt
   │
   ├── [HOOK] Intent Compass scans → captures intention signals
   │
2. COMMANDER (Claude Max) processes
   │
   ├── [IF parallel needed] Spawns Blitzkrieg lanes
   │   ├── Lane A: Commander continues primary work
   │   ├── Lane B: dispatch_to_psyche.sh → Psyche QA
   │   ├── Lane C: gemini CLI survey (if corpus-wide)
   │   └── Lane D: codex CLI implement (if mechanical code)
   │
   ├── [HOOK on commit] Execution log entry auto-generated
   │
3. SESSION ENDS
   │
   ├── [HOOK] Session log → DYN-SESSION_LOG.md
   ├── [HOOK] Ajna Pedigree → DYN-PEDIGREE_LOG.md
   ├── [HOOK] Execution log → DYN-EXECUTION_STAGING.md
   │
4. [THRESHOLD] 10 entries accumulated
   │
   └── compact_wisdom.sh → ARCH-DIRECTIVE_COMPENDIUM.md + ARCH-EXECUTION_HISTORY.md
```

---

## Timeline (No Estimates, Just Sequence)

```
NOW:          Consolidation (branch merge, CANON lean-out, sn_expand.py)
NEXT:         CLI tool activation (Codex + Gemini on Account 2)
THEN:         Linear onboarding + backlog reconciliation
AFTER THAT:   FDIS triangulation + Palantir mapping
ONGOING:      Velocity management + wisdom compaction
```

---

## Cross-References

| Reference | Path |
|-----------|------|
| Original Blitzkrieg | `00-ORCHESTRATION/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md` |
| CLI Enlistment | `02-ENGINE/REF-CLI_ENLISTMENT.md` |
| Twin Coordination | `00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md` |
| Intention Compass | `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` |
| DEF Variables | `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` |
| Account Structure | `COCKPIT.md` (Three Accounts section) |
| Constellation Teleology | `01-CANON/CANON-25200` (includes merged teleology) |
