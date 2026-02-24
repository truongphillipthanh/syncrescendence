# ARCH — Task Tier Architecture
## Five-Tier Model with Dual Project Management

Version: 1.0.0
Updated: 2026-02-05
**Version**: 1.0.0
**Created**: 2026-02-05
**Authority**: Commander (Claude Code Opus)
**Purpose**: Formalize the relationship between strategic intentions, project management tools, implementation tracking, and session-level execution across the Syncrescendence Constellation.

---

## THE FIVE TIERS

### T0: Strategic Intentions
**Tool**: `ARCH-INTENTION_COMPASS.md` (repo)
**Scope**: Vision vectors, meta-patterns, anti-patterns, civilizational-scale direction
**Cadence**: Per-Council session / monthly review
**Owner**: Sovereign
**Capture Mechanism**: `intent_compass.sh` hook (fires on every user prompt)

Intentions are the highest-resolution articulation of Sovereign will. They are not tasks — they are vectors. They decompose into T1 projects.

### T1a: Corpus/Repo Projects (Linear)
**Tool**: Linear
**Scope**: Work done **TO** the repository and corpus
**Cadence**: Weekly review
**Owner**: Sovereign + Commander

Everything that modifies, extends, or maintains the Syncrescendence repo:
- Canon development, Ontology work, Architecture decisions
- CLI tool orchestration configs (Claude Code, Codex CLI, Gemini CLI, OpenClaw)
- Engine functions, Avatar specs, SN system
- Multi-agent dispatch coordination
- Infrastructure automation (hooks, scripts, watchers)
- Source processing and research integration

**Workspace**: Syncrescendence
**Teams**:
| Team | Scope |
|------|-------|
| Canon | Canon development, Ontology, Schema, Chain work |
| Engine | Functions, Avatars, IIC, Processing Pipeline |
| Orchestration | Automation, Dispatch, Constellation, CLI configs |
| Infrastructure | Hooks, Scripts, MCP, Integrations |

**Issue Hierarchy**:
| Level | Maps To | Example |
|-------|---------|---------|
| Project | PROJ-XXX | PROJ-006 (Ontology) |
| Epic | Major phase | PROJ-006 Phase 1 (Content) |
| Issue | IMPL-A-XXXX | IMPL-A-0008 (CANON-31150 rewrite) |
| Sub-issue | Session task | "Apply frontmatter to CANON-30xxx files" |

**Labels**: `P0`/`P1`/`P2`/`P3`, `chain:intelligence`/`chain:information`/`chain:insight`/`chain:expertise`/`chain:knowledge`/`chain:wisdom`, `cli:claude-code`/`cli:codex`/`cli:gemini`/`cli:openclaw`

**Sync**: DYN-BACKLOG.md remains the repo snapshot per Invariant #5 (Repo Sovereignty). Linear is source of truth for project status; the repo snapshot is updated at session checkpoints.

### T1b: Life/External Projects (ClickUp)
**Tool**: ClickUp
**Scope**: Work done **NOT ON** the repository
**Cadence**: Weekly review
**Owner**: Sovereign

Everything outside the repo's domain:
- Professional development (interviews, education, certifications)
- Personal/home tasks
- External research not yet routed to repo
- Administrative tasks, errands, appointments
- Financial tracking, account management

**Workspace**: Sovereign Operations
**Spaces**:
| Space | Scope |
|-------|-------|
| Professional | Interviews (IEETC), Education (Chaffey), Career development |
| Personal | Home maintenance, Admin, Health |
| Financial | Budget, Subscriptions ($160/mo constellation), Investments |

**Migration**: SOVEREIGN PERSONAL QUEUE items from DYN-BACKLOG.md migrate to ClickUp. The DYN-BACKLOG.md section remains as frozen reference per Invariant #5.

### T2: Implementation Items
**Tool**: `IMPLEMENTATION-MAP.md` + `DYN-BACKLOG.md` (repo)
**Scope**: Sprint-level concrete tasks with dependencies, owners, and venues
**Cadence**: Per-session checkpoint
**Owner**: Commander

Implementation items are the operational bridge between projects (T1) and execution (T3). Each has:
- Source path and lines (traceability to Canon or Architecture)
- Intent (why this exists)
- Deliverable (what it produces)
- Dependencies (what must be true first)
- Owner lane (which agent executes)
- Venue (repo, linear, external)
- Status (new → in_progress → done)

### T3: Session Operations
**Tool**: Claude Code first-party Tasks (`TaskCreate`/`TaskUpdate`/`TaskList`) + `agents/`/inbox dispatch
**Scope**: Atomic execution units within a single Commander session
**Cadence**: Real-time
**Owner**: Commander + dispatched agents

At session start, T2 items decompose into T3 tasks:
- `TaskCreate` for each session target
- `TaskUpdate` as work progresses
- `agents/{agent}/inbox/` dispatch for multi-agent work
- On session end: bubble completion status up to T2

---

## SYNC PROTOCOL

```
T0 (Intention Compass — repo)
 │ ← Sovereign captures intentions (hook: intent_compass.sh)
 │ → Repo-facing intentions → T1a (Linear)
 │ → Life-facing intentions → T1b (ClickUp)
 │
T1a (Linear — repo/corpus)              T1b (ClickUp — life/external)
 │ ← Source of truth for repo projects   │ ← Source of truth for non-repo tasks
 │ → Decompose into T2 implementation    │ → Standalone (no T2 decomposition)
 │ ↔ DYN-BACKLOG.md = repo snapshot      │ → SOVEREIGN PERSONAL QUEUE = repo snapshot
 │
T2 (Implementation Map — repo)
 │ ← Concrete deliverables with dependencies, owners, venues
 │ → Items decompose into T3 session tasks at session start
 │
T3 (Claude Code Tasks + INBOX dispatch)
 │ ← TaskCreate at session start from T2 items
 │ → TaskUpdate on completion → bubbles up to T2 status
 │ → agents//inbox dispatch for multi-agent work
```

### Upward Propagation Rules

| Event | T3 Action | T2 Action | T1 Action |
|-------|-----------|-----------|-----------|
| Task completed | `TaskUpdate` completed | Update IMPL status | Update Linear issue |
| Task blocked | Note blocker | Add dependency | Flag in Linear |
| New work discovered | `TaskCreate` | Add to IMPLEMENTATION-MAP | Create Linear issue if multi-session |
| Session ends | All T3 resolved or noted | Checkpoint IMPLEMENTATION-MAP | DYN-BACKLOG.md snapshot updated |

### Downward Decomposition Rules

| Event | T0 Action | T1 Action | T2 Action |
|-------|-----------|-----------|-----------|
| New intention captured | Add to Compass | Create Linear project if substantial | — |
| Sprint planning | Review active intentions | Prioritize Linear issues | Create IMPL items |
| Session start | Read Compass for context | Check Linear for priorities | Decompose into T3 tasks |

---

## CLI ORCHESTRATION CONFIG LAYER

Linear serves as the meta-layer above orchestration configs for ALL CLI tools:

| CLI Tool | Agent | Config Location | Repo Mirror |
|----------|-------|----------------|-------------|
| Claude Code | Commander | `CLAUDE.md` + `.claude/` | Native (lives in repo) |
| Codex CLI | Adjudicator | `AGENTS.md` + codex config | `engine/AVATAR-CODEX.md` |
| Gemini CLI | Cartographer | `GEMINI.md` + gemini config | `engine/AVATAR-GEMINI-CLI.md` |
| OpenClaw | Ajna/Psyche | System-level (root access) | `engine/REF-OPENCLAW_CONFIG_MIRROR.md` |

### Config Parity Principle

All CLI tools should have equivalent orchestration capability:
1. **Constitutional rules** — Each tool needs its equivalent of CLAUDE.md's Five Invariants
2. **Directory awareness** — Each tool must understand the repo structure
3. **Dispatch awareness** — Each tool must know how to check its inbox and produce results
4. **Commit discipline** — Each tool must follow semantic commit conventions
5. **Verification** — Each tool must verify before claiming completion

### OpenClaw Special Handling

OpenClaw configs live outside the repo at system level. The repo holds a mirror document (`engine/REF-OPENCLAW_CONFIG_MIRROR.md`) that captures canonical configuration. Protocol:
1. Any OpenClaw config change → update the system config
2. Update the mirror document → commit to repo
3. Repo mirror is ground truth for "how is OpenClaw configured?"

---

## TELEOLOGICAL RATIONALE

### Why Linear for Repo Work?
- Engineering-first aesthetic matches Syncrescendence's technical nature
- MCP server support enables Claude Code ↔ Linear bidirectional operations
- Issue hierarchy (Project → Epic → Issue → Sub-issue) maps cleanly to PROJ → Phase → IMPL → Task
- CLI integration possible via `linear` CLI tool
- API-first design enables future automation

### Why ClickUp for Life Work?
- Broader task management features beyond engineering
- Better suited for varied task types (appointments, errands, education)
- Visual flexibility (multiple view types)
- Separates professional/personal from technical work
- Prevents repo bloat from non-technical tasks

### Why Keep Repo Snapshots?
- Invariant #5: Repository is ground truth
- Any conversation must be deletable without losing state (Invariant #4)
- Agents need repo-accessible context (can't query Linear/ClickUp without MCP)
- Offline resilience — repo works without internet
- Audit trail — git history preserves all state transitions

---

## VERSION HISTORY

**v1.0.0** (2026-02-05): Genesis
- Five-tier model formalized (T0/T1a/T1b/T2/T3)
- Linear/ClickUp teleological separation defined
- CLI config parity principle established
- Sync protocol documented
- Authority: Commander (Claude Code Opus)
