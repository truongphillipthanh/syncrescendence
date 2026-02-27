# BLITZKRIEG PLAN — Repo Rearchitecture (INT-2201 through INT-2204)
## Issued: 2026-02-22 | Commander Session

### Objective
Replace the ad-hoc flat directory structure with an agent-centric "office" architecture that is intuitive, platform-native, and informed by research insights on memory, progressive disclosure, and knowledge-code isomorphism.

### Design Constraints
- Must accommodate 5 platforms: Claude Code (rich tooling), Codex CLI (sandboxed), Gemini CLI (weak tools, 1M context), OpenClaw (persistent TUI, root-level arch), Grok Build (future, no harness)
- Must preserve git history (moves via `git mv`, not delete+create)
- Must not break auto_ingest_loop.sh, dispatch.sh, or launchd plists during migration
- Must be implementable incrementally (no big-bang cutover)
- Must honor File-First (INT-P017) and Progressive Disclosure (INT-1701) principles

### Success Criteria
- [ ] Every agent has a standardized office directory with consistent internal structure
- [ ] Init files (CLAUDE.md, AGENTS.md, GEMINI.md) refactored into per-agent entry points
- [ ] -INBOX/ filesystem kanban migrated into agent offices
- [ ] Collaboration directory exists with lifecycle policy
- [ ] COCKPIT.md renamed and restructured
- [ ] dispatch.sh, auto_ingest_loop.sh, and launchd plists updated to new paths
- [ ] All constitutional rules updated in root CLAUDE.md

---

## PART 1: NEW DIRECTORY STRUCTURE

### Root Level (Target)

```
syncrescendence/
├── .claude/                    # Claude Code platform config (unchanged)
├── .gemini/                    # Gemini CLI platform config (unchanged)
├── .agent/                     # Codex CLI platform config (unchanged)
├── .constellation/             # Shared constellation metadata (unchanged)
│
├── orchestration/           # Strategic coordination (RETAINED)
│   ├── state/                  # ARCH-*, DYN-*, REF-* files
│   ├── scripts/                # dispatch.sh, auto_ingest_loop.sh, etc.
│   └── archive/                # Compacted logs
│
├── canon/                   # Verified canonical knowledge (PROTECTED, RETAINED)
│
├── engine/                  # Functions, prompts, avatars, templates (RETAINED)
│
├── sources/                 # Source documents (RETAINED)
│
├── praxis/                   # Operational knowledge corpus (RETAINED)
│
├── agents/                     # NEW — Agent offices (replaces -INBOX/)
│   ├── commander/
│   ├── adjudicator/
│   ├── cartographer/
│   ├── psyche/
│   └── ajna/
│
├── collab/                     # NEW — Multi-agent collaboration space (INT-2203)
│
├── -SOVEREIGN/                 # Async decision queue (RETAINED)
│
├── CLAUDE.md                   # Constitutional law (RETAINED, updated)
├── BRIDGE.md                   # RENAMED from COCKPIT.md — constellation overview
├── Makefile                    # Build targets (RETAINED)
└── .gitignore
```

### What Dies
| Current | Fate | Rationale |
|---------|------|-----------|
| `-INBOX/` | **MIGRATED** into `agents/<name>/inbox/` | Agent offices subsume inbox function |
| `-OUTGOING/` | **DELETED** | Vestigial — web avatars are Sovereign-operated, not agent-dispatched |
| `AGENTS.md` (root) | **SPLIT** into per-agent init files | Each platform reads its own init file |
| `GEMINI.md` (root) | **MOVED** into `agents/cartographer/INIT.md` | Per-agent init |
| `-OUTBOX/` | Already deleted | Confirmed dead |

### COCKPIT.md → BRIDGE.md
Rationale for rename: "Cockpit" implies a Mac mini tmux-specific concept. "Bridge" (as in starship bridge) is:
- Platform-agnostic (not tied to tmux)
- Metaphorically richer (command center, not a vehicle interior)
- Scalable (a bridge can have any number of stations)
- Consistent with the military/sci-fi vocabulary (Dune, Halo, Star Trek)

Alternative candidates considered: `CONSTELLATION.md`, `HELM.md`, `NEXUS.md`, `COMMAND.md`. "Bridge" wins on clarity and metaphorical fit.

---

## PART 2: AGENT OFFICE SCHEMA

Every agent gets a standardized office directory. The structure is informed by:
- **Three-Layer Memory** (INT-1707): knowledge graph + daily notes + tacit knowledge
- **Progressive Disclosure** (INT-1701): tree → descriptions → outlines → full content
- **Filesystem Kanban** (existing): INBOX0 → IN_PROGRESS → DONE/FAILED
- **Platform-Native Accommodation** (INT-2204): each office can have platform-specific extensions

### Standard Office Structure

```
agents/<agent-name>/
├── INIT.md                     # Agent identity, role, protocols (replaces root init files)
├── inbox/                      # Filesystem kanban (migrated from -INBOX/<agent>/)
│   ├── pending/                # Was 00-INBOX0 — incoming tasks
│   ├── active/                 # Was 10-IN_PROGRESS — claimed tasks
│   ├── done/                   # Was 40-DONE — completed
│   ├── failed/                 # Was 50_FAILED
│   └── blocked/                # Was 30-BLOCKED
├── outbox/                     # Results, evidence packs, deliverables
├── scratchpad/                 # Working files, drafts, temp artifacts
├── memory/                     # Agent-specific memory (Three-Layer)
│   ├── MEMORY.md               # Tacit knowledge (Layer 3) — patterns, lessons
│   ├── entities/               # Knowledge graph (Layer 1) — per-entity summaries
│   └── journal/                # Daily notes (Layer 2) — dated entries
└── _platform/                  # Platform-specific extensions (optional)
```

### Per-Agent INIT.md Design

Each INIT.md replaces the current root-level init files (AGENTS.md for Adjudicator, GEMINI.md for Cartographer, etc.) and contains:

1. **Identity block**: Name, epithet, enterprise role, model, machine, summon phrase
2. **Jurisdiction**: What this agent handles autonomously vs. escalates
3. **Protocols**: Initialization, execution, completion (currently spread across AGENTS.md/GEMINI.md)
4. **Office pointers**: Where inbox/outbox/memory live (self-referential)
5. **Platform-native notes**: Capabilities, limitations, dispatch mode

The root `CLAUDE.md` remains as constitutional law — agent-agnostic invariants. Agent-specific protocols move to their INIT.md.

### Platform-Native `_platform/` Extensions (INT-2204)

| Agent | Platform | `_platform/` Contents |
|-------|----------|----------------------|
| Commander | Claude Code | `skills/` (symlink to .claude/skills), `hooks/` config |
| Adjudicator | Codex CLI | `codex-config.json`, sandbox policies |
| Cartographer | Gemini CLI | `gemini-config/`, headless templates, 1M context strategies |
| Psyche | OpenClaw | `openclaw/` (mirror of ~/.openclaw/ structure: SOUL.md, HEARTBEAT.md, etc.) |
| Ajna | OpenClaw | `openclaw/` (mirror of ~/.openclaw/ on MBA) |

For **Gemini** (weak tooling, strong context): INIT.md is written to be maximally self-contained. No `@` file references that require tool use. Include inline context rather than pointers. The `_platform/` folder contains pre-composed prompts for headless dispatch.

For **OpenClaw** agents: The `_platform/openclaw/` directory mirrors the `~/.openclaw/` structure, serving as the canonical source. A sync mechanism (launchd or hook) keeps `~/.openclaw/` in sync with the repo copy, so personality files are version-controlled.

For **Grok Build** (future, INT-1901): Reserve `agents/oracle/` (or whatever avatar name). Minimal INIT.md with role definition. Flesh out when the platform releases.

---

## PART 3: COLLABORATION DIRECTORY (INT-2203)

```
collab/
├── README.md                   # Policies, naming conventions, lifecycle rules
├── _archive/                   # Completed/abandoned projects
└── <project-slug>/             # Active collaboration spaces
    ├── MANIFEST.md             # Objective, lanes, agents, sync points, owner
    ├── findings.md             # Shared research/evidence
    └── <agent-artifacts>/      # Per-agent deliverables within the project
```

### Anti-Proliferation Policy (STRICT)

1. **Max 3 active projects** in `collab/`. If a 4th is needed, archive or complete one first.
2. **Naming convention**: `YYYY-MM-slug` (e.g., `2026-02-repo-rearchitecture`)
3. **Ownership**: Every project MUST have an owner agent in MANIFEST.md
4. **TTL**: Projects without commits in 7 days get flagged. 14 days = auto-archive.
5. **Archival**: `git mv collab/<slug> collab/_archive/<slug>` with final status in MANIFEST.md
6. **No orphan files**: Every file in a collab project must be referenced in MANIFEST.md or deleted

This replaces the ad-hoc pattern where blitzkrieg artifacts, research findings, and multi-agent outputs scattered across `orchestration/state/impl/`, root directory, and `-OUTGOING/`.

---

## PART 4: INIT FILE REDESIGN

### Current State (Fragmented)

| File | Loaded By | Contains |
|------|-----------|----------|
| `CLAUDE.md` | Claude Code (all agents) | Constitutional law + Commander protocols + Adjudicator awareness + dispatch docs |
| `AGENTS.md` | Codex CLI (Adjudicator) | Adjudicator protocols + partial Commander/Cartographer/Psyche/Ajna info |
| `GEMINI.md` | Gemini CLI (Cartographer) | Cartographer protocols |

Problem: CLAUDE.md is 330+ lines trying to serve both as constitutional law AND Commander-specific protocol. AGENTS.md duplicates constellation info that's already in COCKPIT.md.

### Target State (Clean Separation)

| File | Loaded By | Contains |
|------|-----------|----------|
| `CLAUDE.md` (root) | All Claude Code agents | Constitutional law ONLY: 5 invariants, structural rules, semantic rules, operational rules, context economics, extended thinking. NO agent-specific protocols. |
| `agents/commander/INIT.md` | Commander (Claude Code) | Commander identity, jurisdiction, protocols (A/B from current CLAUDE.md), dispatch docs, skill/hook inventory |
| `agents/adjudicator/INIT.md` | Adjudicator (Codex CLI) | Adjudicator identity, jurisdiction, protocols (A/B/C from current AGENTS.md) |
| `agents/cartographer/INIT.md` | Cartographer (Gemini CLI) | Cartographer identity, self-contained context (no file refs), headless dispatch patterns |
| `agents/psyche/INIT.md` | Psyche (OpenClaw) | Psyche identity, CTO jurisdiction, automation/pipeline domain |
| `agents/ajna/INIT.md` | Ajna (OpenClaw) | Ajna identity, CSO jurisdiction, strategic domain |
| `BRIDGE.md` (root) | All agents on-demand | Constellation overview, machine topology, cockpit layout, web avatars, operational runbook |

### How Each Platform Discovers Its INIT.md

| Platform | Mechanism |
|----------|-----------|
| **Claude Code** | `.claude/CLAUDE.md` hierarchy — root `CLAUDE.md` auto-loads. Commander's INIT.md loaded via `@agents/commander/INIT.md` reference in CLAUDE.md, or via local CLAUDE.md in `agents/commander/` |
| **Codex CLI** | `AGENTS.md` renamed to `agents/adjudicator/INIT.md`. Codex reads from working directory — launch from `agents/adjudicator/` or use `--instructions` flag |
| **Gemini CLI** | `GEMINI.md` renamed to `agents/cartographer/INIT.md`. Gemini's `--system-instruction` flag or `.gemini/` config points to it |
| **OpenClaw** | `~/.openclaw/SOUL.md` etc. remain the runtime files. `agents/{psyche,ajna}/_platform/openclaw/` is the repo-canonical version. Sync script pushes changes from repo → `~/.openclaw/` |

### Local CLAUDE.md Files (Progressive Disclosure)

Place a minimal `CLAUDE.md` in each agent office directory:

```markdown
# agents/commander/CLAUDE.md
# Commander Office — Local Context

You are in Commander's office. Read `INIT.md` for your full protocol.
Your inbox is at `inbox/pending/`. Your scratchpad is at `scratchpad/`.
```

This activates Claude Code's local CLAUDE.md hierarchy — when Commander works inside `agents/commander/`, it auto-loads this context.

---

## PART 5: DISPATCH & INFRASTRUCTURE MIGRATION

### dispatch.sh Changes

Current paths:
```bash
INBOX_DIR="$REPO_ROOT/-INBOX/$AGENT/00-INBOX0"
```

New paths:
```bash
INBOX_DIR="$REPO_ROOT/agents/$AGENT/inbox/pending"
```

### auto_ingest_loop.sh Changes

Current kanban folder names → New names:
| Current | New |
|---------|-----|
| `00-INBOX0/` | `inbox/pending/` |
| `10-IN_PROGRESS/` | `inbox/active/` |
| `20-WAITING/` | (removed — merge into blocked) |
| `30-BLOCKED/` | `inbox/blocked/` |
| `40-DONE/` | `inbox/done/` |
| `50_FAILED/` | `inbox/failed/` |
| `90_ARCHIVE/` | `inbox/done/` (no separate archive — use git history) |
| `RECEIPTS/` | `outbox/` |

### launchd Plists

Update `WatchPaths` in all 5 watcher plists:
```xml
<!-- Old -->
<string>/Users/home/Desktop/syncrescendence/-INBOX/commander/00-INBOX0</string>
<!-- New -->
<string>/Users/home/Desktop/syncrescendence/agents/commander/inbox/pending</string>
```

### Migration Strategy (Zero-Downtime)

Phase 1: **Symlink bridge** (immediate)
```bash
# Create new structure
mkdir -p agents/{commander,adjudicator,cartographer,psyche,ajna}/{inbox/{pending,active,done,failed,blocked},outbox,scratchpad,memory/{entities,journal},_platform}

# Symlink old → new for backwards compatibility
ln -s ../agents/commander/inbox/pending -INBOX/commander/00-INBOX0
# (repeat for all agents)
```

Phase 2: **Update scripts** (same session)
- Modify dispatch.sh, auto_ingest_loop.sh to use new paths
- Update launchd plists
- Reload launchd services

Phase 3: **Remove symlinks** (after verification)
- Delete `-INBOX/` directory
- Delete `-OUTGOING/` directory
- Commit

Phase 4: **Init file refactor** (next session)
- Extract agent-specific content from CLAUDE.md → per-agent INIT.md files
- Rename COCKPIT.md → BRIDGE.md
- Delete root AGENTS.md and GEMINI.md
- Update all cross-references

---

## PART 6: CLAUDE.MD REFACTOR (Constitutional Slimming)

### Content That Stays in Root CLAUDE.md
- Identity paragraph
- Five Invariants
- Constitutional Rules (Structural, Semantic, Operational) — updated for new paths
- Extended Thinking guidance
- CLAUDE.md Hierarchy explanation
- Context Economics
- Hard-Gate Skills (DEC-C3)
- Anti-Patterns (PROHIBITED) — universal ones only
- Session Protocol

### Content That Moves to `agents/commander/INIT.md`
- Sovereign Interaction Protocol (§99-113)
- Directive Initialization Protocol (A)
- Directive Completion Protocol (B)
- Constellation Operations (§224-326) — all the neural bridge, dispatch, auto-ingest docs
- Hooks table
- Processing Patterns
- Key References table
- OpenClaw Integration section

### Content That Moves to `BRIDGE.md`
- Machine topology diagram
- Cockpit layout
- Agent loop architecture (reference)
- Web avatar descriptions
- Always-On Services table
- Operational Runbook

### Updated Constitutional Rule 4 (SANCTIONED EXCEPTIONS)
```markdown
4. **SANCTIONED EXCEPTIONS**: `agents/`, `collab/`, and `-SOVEREIGN/` are the
   only non-numbered directories permitted at root (besides dotfiles).
```

This replaces the old `-INBOX/`, `-OUTGOING/`, `-OUTBOX/` exceptions.

---

## PART 7: OPENCLAW ARCHITECTURE ACCOMMODATION

### Current OpenClaw Structure (~/.openclaw/)
```
~/.openclaw/
├── SOUL.md          # Identity, personality, negative constraints
├── AGENTS.md        # Multi-agent awareness
├── HEARTBEAT.md     # Health check cadence and criteria
├── USER.md          # (user profile — not currently used)
├── MEMORY.md        # Long-term memory
├── openclaw.json    # Provider/model config
├── agents/          # Sub-agent definitions
├── skills/          # OpenClaw skills
├── memory/          # OpenClaw memory store
└── workspace/       # Workspace-specific config
```

### Isomorphism with Agent Office

| OpenClaw File | Agent Office Equivalent |
|---------------|------------------------|
| `SOUL.md` | `INIT.md` (identity section) |
| `AGENTS.md` | `INIT.md` (constellation awareness section) |
| `HEARTBEAT.md` | `_platform/openclaw/HEARTBEAT.md` |
| `MEMORY.md` | `memory/MEMORY.md` |
| `skills/` | `_platform/openclaw/skills/` |
| `openclaw.json` | `_platform/openclaw/openclaw.json` |

### Sync Protocol
A git hook or launchd plist syncs `agents/{psyche,ajna}/_platform/openclaw/` → `~/.openclaw/` on the appropriate machine:
- MBA: `agents/ajna/_platform/openclaw/` → `~/.openclaw/` (Ajna's machine)
- Mac mini: `agents/psyche/_platform/openclaw/` → `~/.openclaw/` (Psyche's machine)

This makes OpenClaw personality files version-controlled in the repo while maintaining the runtime location OpenClaw expects.

---

## PART 8: RESEARCH-INFORMED DECISIONS

| Research Insight | How It Informs This Plan |
|-----------------|-------------------------|
| **Progressive Disclosure** (INT-1701) | Office structure is layered: INIT.md (cheap overview) → inbox/outbox (operational state) → memory/ (deep context) → _platform/ (implementation detail). Agents read INIT.md first, dive deeper only when needed. |
| **Three-Layer Memory** (INT-1707) | Each office has `memory/` with three sub-layers: `MEMORY.md` (tacit), `entities/` (knowledge graph), `journal/` (daily notes). |
| **File-First** (INT-P017) | No databases, no vector stores in the critical path. Everything is markdown + YAML frontmatter. grep/search suffices. |
| **Notes = Skills** (§1.7) | Agent INIT.md files ARE skills — highly curated knowledge injected when relevant. The vault index pattern applies to agent discovery. |
| **Hooks as Basal Ganglia** (§1.5) | Verification hooks remain in .claude/settings.json (deterministic). Judgment stays in INIT.md protocols (semantic). |
| **Supersede, Never Delete** (§2.2) | Migration preserves history via `git mv`. Old -INBOX/ paths become symlinks, then die. No orphaned state. |
| **Correction-Based Knowledge** (§2.5) | Agent `memory/` directories capture corrections as they happen. Pattern already supported by Claude Code's auto-memory. |
| **Security Perimeter** (INT-1709, INT-1712) | Each agent's `_platform/` can specify security policies. Sandbox config for Adjudicator, SHIELD.md for OpenClaw agents. |
| **Constellation Validated** (INT-P022, INT-1710) | The office pattern mirrors what independent practitioners converged on. We're formalizing the emergent consensus. |
| **Anti-Tool-Shaped-Object** (§3.6) | The collaboration directory has strict TTL and max-active limits. No proliferation. Every artifact must produce real output. |

---

## PART 9: MIGRATION EXECUTION PLAN

### Phase 1: Scaffolding (This Session — Commander)
1. Create all `agents/<name>/` directories with standardized internal structure
2. `git mv` all `-INBOX/<agent>/` contents to `agents/<agent>/inbox/`
3. Rename inbox subdirectories (00-INBOX0 → pending, etc.)
4. Create `collab/` with README.md and policies
5. Create symlinks for backwards compatibility
6. Commit: `refactor: scaffold agent office directories (INT-2201)`

### Phase 2: Script Migration (This Session — Commander)
1. Update dispatch.sh paths
2. Update auto_ingest_loop.sh paths
3. Update auto_ingest_supervisor.sh paths
4. Update any other scripts referencing `-INBOX/`
5. Commit: `refactor: update dispatch scripts for agent offices (INT-2201)`

### Phase 3: Init File Refactor (Next Session — Commander)
1. Write per-agent INIT.md files (extract from CLAUDE.md, AGENTS.md, GEMINI.md)
2. Slim CLAUDE.md to constitutional-only
3. Rename COCKPIT.md → BRIDGE.md, update content
4. Delete root AGENTS.md and GEMINI.md
5. Place local CLAUDE.md in each agent office
6. Commit: `refactor: per-agent init files, COCKPIT→BRIDGE rename (INT-2201)`

### Phase 4: Infrastructure (Dispatch to Mac mini — Psyche/Commander)
1. Update launchd plists on Mac mini (WatchPaths)
2. Update launchd plists on MBA (WatchPaths)
3. Create OpenClaw sync mechanism (repo → ~/.openclaw/)
4. Remove backwards-compat symlinks
5. Delete `-INBOX/`, `-OUTGOING/`
6. Reload all launchd services on both machines
7. Commit: `refactor: launchd migration to agent offices (INT-2201)`

### Phase 5: Verification (Adjudicator — FORTIFY)
1. Dispatch test task to each agent via new paths
2. Verify full kanban lifecycle: pending → active → done + CONFIRM
3. Verify cross-machine SCP sling with new paths
4. Verify git sync doesn't break
5. Verify no stale references to old paths anywhere in repo
6. Commit: `test: verify agent office migration (INT-2201)`

### Phase 6: Cleanup (Commander)
1. Delete `-INBOX/` spam directories (the `[2026-02-19...]` junk dirs)
2. Archive migration artifacts
3. Update BRIDGE.md with final state
4. Update ARCH-INTENTION_COMPASS.md: INT-2201 → resolved
5. Commit: `chore: post-migration cleanup (INT-2201)`

---

## RISK ASSESSMENT

- **HIGH**: launchd plist updates on Mac mini require SSH access and service reload. If Neural Bridge is down, Phase 4 blocks. **Mitigation**: Do Phase 4 as a dispatched task to Psyche/Commander on Mac mini, or push via git and have Mac mini pull.

- **HIGH**: Git sandbox SIGKILL on large commits (MEMORY.md lesson). The migration involves many file moves. **Mitigation**: Use git plumbing (`git write-tree` → `git commit-tree`) or commit in small batches.

- **MEDIUM**: Auto-ingest loop may process tasks during migration, hitting broken paths. **Mitigation**: Disable auto-ingest watchers (`launchctl unload`) during migration, re-enable after.

- **MEDIUM**: Cross-references in 100+ files point to `-INBOX/`. **Mitigation**: `grep -r '\-INBOX' --include='*.md'` to find all references, update in batch.

- **LOW**: Symlink bridge may cause confusion if both old and new paths are used simultaneously. **Mitigation**: Symlink phase is temporary (hours, not days).

---

## DISPATCH COMMANDS

Phase 1-2 execute locally (this session, Commander on MBA).

Phase 4 requires Mac mini dispatch:
```bash
bash orchestration/scripts/dispatch.sh psyche "LAUNCHD_MIGRATION" "Update all launchd WatchPaths from -INBOX/<agent>/00-INBOX0 to agents/<agent>/inbox/pending. Reload all services. Verify with launchctl list." "" "DIRECTIVE" "commander"
```

Phase 5 validation:
```bash
bash orchestration/scripts/dispatch.sh adjudicator "MIGRATION_VERIFICATION" "Run full kanban lifecycle test on new agent office paths. Dispatch test task, verify pending→active→done flow, verify CONFIRM routing." "" "DIRECTIVE" "commander"
```

---

*Plan authored by Commander (Claude Opus 4.6) | 2026-02-22 | INT-2201 through INT-2204*
*Research corpus consumed: RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md, RESEARCH-INSIGHTS-HIGH-SIGNAL.md, 12 source articles from sources/*
