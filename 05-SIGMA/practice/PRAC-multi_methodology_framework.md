# Multi-Methodology Project Management Framework
## Syncrescendence Operational Knowledge

**Version**: 1.0.0
**Created**: 2026-02-10
**Source**: SOVEREIGN-009 Decision 1 (Ratified 2026-02-10)
**Linear**: SYN-58
**Canon Reference**: REF-STACK_TELEOLOGY.md (v1.0.0)

---

## Architecture

```
            ┌─────────────────────────────────────────────┐
            │              CLICKUP (Hub)                   │
            │   Multi-method views, native integrations    │
            └─────┬──────┬──────┬──────┬──────────────────┘
                  │      │      │      │
    ┌─────────────┤      │      │      ├──────────────┐
    ▼             ▼      ▼      ▼      ▼              ▼
┌────────┐ ┌────────┐ ┌──────┐ ┌─────────┐ ┌──────────────┐
│ LINEAR │ │  JIRA  │ │TRELLO│ │TODOIST  │ │  TEAMGANTT   │
│ Agile  │ │ Scrum  │ │Kanban│ │  GTD    │ │  Waterfall   │
│ T1a    │ │ Sprint │ │ Flow │ │ Capture │ │  Timeline    │
└────────┘ └────────┘ └──────┘ └─────────┘ └──────────────┘
```

**Principle**: ClickUp sits at the center with maximum native integrations. Each tool owns one methodology. Long-term goal: build internal replacements.

---

## Methodology Profiles

### 1. Scrum (Jira + Linear)

**When to use**: Iterative development with defined sprints, team velocity tracking, complex feature delivery.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | Jira (primary), Linear (engineering escalation) |
| **Ceremonies** | Sprint planning, daily standups (async), sprint review, retrospective |
| **Artifacts** | Product backlog, sprint backlog, increment |
| **Cadence** | 2-week sprints |
| **Metrics** | Velocity, burndown, sprint goal completion |
| **Integration** | Jira superstructures Linear — escalated engineering issues flow up |
| **Canon mapping** | Sprint outcomes → IMPL-MAP entries → CANON updates |

**Workflow**:
1. Backlog grooming in Jira (prioritize by P0-P3)
2. Sprint planning: pull items into sprint board
3. Daily async standup via -INBOX dispatch or Linear comments
4. Sprint review: artifacts committed to repo
5. Retrospective: lessons → 05-SIGMA/practice/ or EXEMPLA

---

### 2. Kanban (Trello + ClickUp Views)

**When to use**: Continuous flow work, visual pipeline management, WIP-limited queues.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | Trello (primary), ClickUp Board View (mirror) |
| **Columns** | Backlog → Ready → In Progress → Review → Done |
| **WIP Limits** | Max 3 in-progress per agent (Commander, Adjudicator, Cartographer) |
| **Metrics** | Lead time, cycle time, throughput, cumulative flow |
| **Integration** | Trello cards = visual phase/stage/tier tracking |
| **Canon mapping** | Flow state transitions map to DYN-EXECUTION_STAGING entries |

**Best for**: Phases, stages, tiers, strata, levels — any ordered-phase system.

---

### 3. GTD — Getting Things Done (Todoist → ClickUp)

**When to use**: Personal task capture, rapid triage, context-based execution.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | Todoist (capture), ClickUp (organize), Things 3 (daily personal) |
| **5 Steps** | Capture → Clarify → Organize → Reflect → Engage |
| **Contexts** | @machine (Mac mini), @mobile (MBA), @sovereign (human-gated), @waiting |
| **Weekly Review** | Sunday: process Todoist inbox → ClickUp lists, review all open items |
| **Integration** | Todoist substructures ClickUp — quick capture flows up to structured PM |
| **Canon mapping** | Captured ideas → -INBOX → IMPL-MAP → CANON (if knowledge-worthy) |

**Workflow**:
1. **Capture**: Todoist (mobile/desktop quick entry) or Apple Reminders (Siri)
2. **Clarify**: Is it actionable? Next action? Project? Someday/Maybe?
3. **Organize**: Route to ClickUp list (Professional/Personal/Financial)
4. **Reflect**: Weekly review cycle
5. **Engage**: Execute by context and energy

---

### 4. Waterfall (TeamGantt + ClickUp Gantt)

**When to use**: Fixed-scope deliverables, dependency-heavy projects, timeline visualization.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | TeamGantt (primary), ClickUp Gantt View (mirror) |
| **Phases** | Requirements → Design → Implementation → Testing → Deployment |
| **Dependencies** | Explicit predecessor/successor links |
| **Milestones** | Gate reviews between phases |
| **Integration** | TeamGantt superstructures ClickUp — timeline views feed down |
| **Canon mapping** | Milestones → DYN-PROJECTS.csv status changes |

**Best for**: PROJ-level initiatives with clear phase gates (e.g., PROJ-006 Ontology has defined phases).

---

### 5. Prince2 — Projects IN Controlled Environments

**When to use**: Business case justification, stage-gate governance, exception management.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | Documentation layer (repo-native) |
| **Principles** | Continued business justification, learn from experience, defined roles, manage by stages, manage by exception, focus on products, tailor to environment |
| **Themes** | Business case, organization, quality, plans, risk, change, progress |
| **Integration** | -SOVEREIGN/ directory = exception management. SOVEREIGN decisions = stage-gate approvals |
| **Canon mapping** | Business cases → ARCH-INTENTION_COMPASS.md (each intention = a business case) |

**Already active (implicitly)**:
- Stage-gate governance: SOVEREIGN decision queue
- Exception management: -SOVEREIGN/ escalation path
- Defined roles: Constellation agent enterprise roles (CEO/CTO/COO/CQO/CIO/CSO)
- Progress reporting: DYN-BACKLOG.md, DYN-EXECUTION_STAGING.md

---

### 6. Critical Chain Project Management

**When to use**: Resource-constrained scheduling, buffer management, multi-project environments.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | Custom tracking (repo-native or Airtable) |
| **Key concepts** | Resource constraints, feeding buffers, project buffers, drum buffer rope |
| **Constraint** | Primary constraint = Sovereign attention (human-gated decisions) |
| **Buffer types** | Project buffer (schedule slack), feeding buffer (dependency chains), resource buffer (agent availability) |
| **Integration** | Maps to DYN-BACKLOG.md dependency graph |
| **Canon mapping** | Constraint identification → ARCH-INTENTION_COMPASS.md priority ordering |

**Application to Syncrescendence**:
- **Constraint**: Sovereign decision throughput (see -SOVEREIGN/ queue depth)
- **Feeding buffers**: Agent teams can pre-stage work before Sovereign review
- **Project buffer**: Session time flexibility — no fixed deadlines on modal work

---

### 7. Critical Path Method

**When to use**: Longest-path analysis for deadline-driven work, float calculation.

| Aspect | Implementation |
|--------|---------------|
| **Tool** | TeamGantt + custom analysis |
| **Key concepts** | Forward pass, backward pass, total float, free float, critical path |
| **Integration** | DYN-BACKLOG.md dependency graph IS the critical path |
| **Canon mapping** | Critical path = the dependency chain in DYN-BACKLOG.md |

**Current critical path**:
```
PROJ-002 (IIC) → PROJ-005 (Branding) → Launch
PROJ-003 (Stack) → PROJ-006b (Ontology Substrate) → PROJ-007 (Curriculum)
                                                    → Modal 1 completion
                                                    → Modal 2 (2027)
```

---

### 8. OPM3 — Organizational Project Management Maturity Model

**When to use**: Assessing and improving PM maturity across the constellation.

| Level | Description | Current State |
|-------|-------------|--------------|
| 1. Standardize | Documented processes exist | PARTIAL — CLAUDE.md, COCKPIT.md, protocols documented |
| 2. Measure | Metrics tracked | PARTIAL — commit velocity, file counts, but no formal KPIs |
| 3. Control | Processes enforced consistently | PARTIAL — hooks enforce some, but agent compliance varies |
| 4. Continuously Improve | Feedback loops drive improvement | ACTIVE — clarescence cycles, session retrospectives |

**Next steps**: Formalize KPIs per agent, standardize reporting cadence, add automated compliance checks.

---

### 9. CMMI — Capability Maturity Model Integration

**When to use**: Process improvement assessment, development practice maturity.

| Level | Description | Current State |
|-------|-------------|--------------|
| 1. Initial | Ad hoc, heroic efforts | PAST — pre-constellation era |
| 2. Managed | Basic project management | CURRENT — T0-T3 architecture, Linear/ClickUp |
| 3. Defined | Organization-wide standards | EMERGING — Constellation roles, protocol standardization |
| 4. Quantitatively Managed | Statistical process control | FUTURE — requires metric infrastructure |
| 5. Optimizing | Continuous improvement | ASPIRATIONAL — requires Level 4 foundation |

**Syncrescendence target**: Level 3 (Defined) by end of Modal 1. Level 4 requires ontology substrate completion.

---

### 10. XP — Extreme Programming

**When to use**: Development practices for high-quality code delivery.

| Practice | Implementation | Status |
|----------|---------------|--------|
| **TDD** | Write tests before implementation | PARTIAL — Adjudicator role handles quality gates |
| **Pair Programming** | Two agents on one problem | ACTIVE — Agent Teams (Blitzkrieg tactic) |
| **Continuous Integration** | Frequent commits, automated checks | ACTIVE — commit discipline, corpus-health hooks |
| **Refactoring** | Continuous code improvement | ACTIVE — clarescence cycles |
| **Simple Design** | YAGNI, minimal complexity | ENFORCED — anti-pattern: over-engineering |
| **Collective Ownership** | Any agent can modify any file | ACTIVE — all agents have repo access |
| **Coding Standards** | Consistent style | ENFORCED — CLAUDE.md constitutional rules |
| **Sustainable Pace** | Avoid burnout | N/A — agents don't tire (but token budgets apply) |

---

## Cross-Methodology Integration Matrix

| Methodology | Tool Surface | T0 Alignment | T1a Link | T1b Link | T2 Artifact | Cadence |
|-------------|-------------|-------------|----------|----------|-------------|---------|
| Scrum | Jira + Linear | INT sprint goals | SYN issues | — | IMPL entries | 2-week sprint |
| Kanban | Trello + ClickUp | Continuous flow | Board view | Board view | DYN-EXECUTION | Continuous |
| GTD | Todoist → ClickUp | Quick capture | — | Task dispatch | -INBOX items | Weekly review |
| Waterfall | TeamGantt | PROJ phases | Milestone SYN | Milestone CU | DYN-PROJECTS | Phase gates |
| Prince2 | Repo-native | -SOVEREIGN/ | Exception SYN | — | Decision log | On exception |
| Critical Chain | Custom | Buffer tracking | — | — | DYN-BACKLOG | Per constraint |
| Critical Path | TeamGantt | Dependency chain | — | — | DYN-BACKLOG | Per project |
| OPM3 | Assessment | Maturity audit | — | — | Annual review | Quarterly |
| CMMI | Assessment | Process level | — | — | Annual review | Quarterly |
| XP | Development | Coding practices | SYN dev issues | — | Commit history | Continuous |

---

## Decision Framework: Which Methodology When?

```
Is the work time-boxed with defined scope?
├── YES → Is scope fixed and sequential?
│         ├── YES → Waterfall (TeamGantt)
│         └── NO → Scrum (Jira sprints)
└── NO → Is it continuous/flow-based?
          ├── YES → Kanban (Trello)
          └── NO → Is it a quick personal task?
                    ├── YES → GTD (Todoist)
                    └── NO → Is it a governance decision?
                              ├── YES → Prince2 (-SOVEREIGN/)
                              └── NO → Is it resource-constrained?
                                        ├── YES → Critical Chain
                                        └── NO → Kanban (default)
```

---

*"The map is not the territory, but without maps, all territory is wilderness." — Syncrescendence operational principle*
