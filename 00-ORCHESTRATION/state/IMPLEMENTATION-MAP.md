# IMPLEMENTATION-MAP.md

> Normalized implementation paths extracted from Canon + Orchestration.
> Schema: id | source_path | source_lines | intent | deliverable | dependencies | owner_lane | venue | status

## 2026-02-05 — Tranche A (Spine): Rosetta Stone + Toolchain Clarescence + Neo‑Blitzkrieg Buildout

- id: IMPL-A-0001
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (1)"
  intent: Remove/repair outdated ‘extended thinking token allocation’ claims.
  deliverable: Update CLAUDE.md (and any related docs) to reflect current extended-thinking behavior; remove hardcoded 4k/8k/32k guidance.
  dependencies: Locate CLAUDE.md references; verify current behavior via tool docs.
  owner_lane: Commander (Claude Code)
  venue: repo
  status: done
  linear_id: SYN-5
  notes: "Completed 2026-02-09: CLAUDE.md updated to remove hardcoded token allocation, simplified to 'auto-enabled by Claude Code'."

- id: IMPL-A-0002
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (2) + §8 Chorus/Medley"
  intent: Correct Chorus vs Medley terminology across ops docs.
  deliverable: README.md update: Constellation operates in Medley mode; reserve Chorus for same-prompt parallel.
  dependencies: Identify all 'Chorus' references; adjust definitions.
  owner_lane: Psyche (spec) + Commander (edit)
  venue: repo
  status: done
  linear_id: SYN-6
  notes: "Completed 2026-02-09: README.md (formerly COCKPIT.md) Modus Operandi updated with Medley/Chorus distinction. AVATAR-GROK.md and AVATAR-CHATGPT.md updated from 'Role in the Chorus' to 'Role in the Constellation (Medley Mode)', PROC Chorus → PROC Medley. 2026-02-10: Residual sweep — 3 more files fixed (SN_BLOCK_TEMPLATES.md PROC Chorus→Medley, EXEMPLA-PROVERBS.md, EXEMPLA-TALE-ajna2-lobotomy.md)."

- id: IMPL-A-0003
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (3) + §5 Ring→sigma"
  intent: Finish Ring→sigma rename and ratify sigma/tau split.
  deliverable: Search+replace remaining 'Ring' refs in active docs; add explicit sigma/tau glossary + governance note.
  dependencies: Identify protected/historical files to avoid rewriting.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-7
  notes: "Completed 2026-02-09: Directory 05-Ring→05-SIGMA done (prior session). σ₇-First terminology in ARCH-TOOLCHAIN_CLARESCENCE.md. Sigma/tau governance note ratified in REF-ROSETTA_STONE.md entry #5. CANON 'Transcendence Ring' refs preserved as ontological content. 2026-02-10: Residual sweep — preface-to-research.md 3 Ring→σ fixes (Ring 7→σ₇, Ring 0→σ₀)."

- id: IMPL-A-0004
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G1)"
  intent: Implement self-healing constitution pattern.
  deliverable: PostToolUse hook that detects failures/anti-patterns and proposes (or appends) CLAUDE.md updates under a governed section.
  dependencies: Hook framework; policy for auto-append vs PR.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-8
  notes: "Completed 2026-02-10: REF-SELF_HEALING_CONSTITUTION.md created. 4-tier arch formalized: L0 launchd → L1 PID → L2 HTTP → L3 escalation. watchdog.sh (153 lines) already live. PostToolUse anti-pattern hook deferred (separate scope)."

- id: IMPL-A-0005
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G5)"
  intent: Adopt git worktree isolation as canonical parallelization mechanism.
  deliverable: Document + script for worktree creation per lane; integrate into Neo‑Blitzkrieg execution guidance.
  dependencies: Existing scripts; team conventions.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-9
  notes: "Completed 2026-02-10: PRAC-blitzkrieg_worktree_isolation.md. Lane-to-worktree binding (A-D), zone ownership, execution workflow. setup-worktrees.sh already existed. Rosetta Stone G5 DONE."

- id: IMPL-A-0006
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G8)"
  intent: Enable token-efficient subagent delegation via skills.
  deliverable: Add `context: fork` (or equivalent) in skill specs + guidance on when to fork.
  dependencies: Skill system conventions.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-10
  notes: "Completed 2026-02-10: PRAC-subagent_delegation_guide.md. Decision tree, context annotation spec (inline/fork/parallel), model selection, token savings analysis, Constellation mapping. Rosetta Stone G8 DONE."

- id: IMPL-A-0007
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Ralph Pattern (17) — ‘verify formal implementation’"
  intent: Ensure Ralph Pattern is actually implemented and discoverable.
  deliverable: Add a canonical ‘Ralph Pattern’ doc pointing to the exact scripts/hooks and example usage; add verification checklist.
  dependencies: Locate current implementation artifacts.
  owner_lane: Psyche (locate/spec) + Commander (implement)
  venue: repo
  status: done
  linear_id: SYN-11
  notes: "Completed 2026-02-10: PRAC-ralph_pattern_execution.md (272 lines) IS the canonical doc. Rosetta Stone #17 VERIFIED. Operationally implemented via claude -p in claudecron + watch_dispatch.sh."

- id: IMPL-A-0008
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "Pass 3 + ‘Required CANON-31150 Update’"
  intent: Bring CANON-31150 Platform Capability Catalog up to reality.
  deliverable: Rewrite CANON-31150 from 3 conflated entries → 7 distinct platform entries (separate CLI vs web; add OpenClaw, Codex; add Grok/Perplexity as separate external services).
  dependencies: README.md role truth; Rosetta naming.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-12
  notes: "Completed 2026-02-10: CANON-31150 regenerated v4.0 from updated platform_capabilities.json. Enterprise roles (CEO/CTO/COO/CQO/CIO/CSO), model updates (Opus 4.6, GPT-5.3-codex, Kimi K2.5, Gemini 2.5 Pro), AjnaPsyche Archon, dual-machine paradigm, 9 MCP servers, expanded metrics."

- id: IMPL-A-0009
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "Pass 7 ‘What This Creates’"
  intent: Fill missing avatar specs for execution substrate.
  deliverable: Create/populate AVATAR-OPENCLAW (Ajna/Psyche) and AVATAR-COMMANDER (Claude Code) per agreed schema.
  dependencies: Avatar template; COCKPIT mapping.
  owner_lane: Psyche + Commander
  venue: repo
  status: done
  linear_id: SYN-13
  notes: "Completed 2026-02-09: AVATAR-COMMANDER.md (prior). AVATAR-OPENCLAW.md created — dual-agent AjnaPsyche Archon spec with enterprise roles, memory infra, communication protocols, known personality/model mismatch documented."

- id: IMPL-A-0010
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "Pass 7 ‘What This Creates’ + Pass 10 Interaction Protocol"
  intent: Formalize the actual tool interaction/dispatch protocol.
  deliverable: DYN-TOOLCHAIN_INTERACTION_PROTOCOL.md capturing dispatch modes, return channels, and minimal file-based handoff conventions.
  dependencies: Existing dispatch scripts; twin protocol.
  owner_lane: Ajna (OpenClaw) + Commander
  venue: repo
  status: done
  linear_id: SYN-14
  notes: "2026-02-10: DYN-TOOLCHAIN_INTERACTION_PROTOCOL.md v1.0.0 created. 8 dispatch modes, file formats (TASK/RESULT/CONFIRM/RECEIPT/ESCALATION), filesystem kanban, return channels, error codes, timeout escalation, agent CLI mapping. dispatch.sh + watch_dispatch.sh enhanced with escalation headers and escalate_on_timeout()."

- id: IMPL-A-0011
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Architecture Adoptions (6)"
  intent: Hooks-based automation for deterministic failure handling.
  deliverable: Define + implement standard hook set (PreToolUse/PostToolUse/Stop/PreCompact) for common failure modes + receipts.
  dependencies: Hook support in primary executor tool.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-15
  notes: "Completed 2026-02-10: REF-HOOKS_FORMALIZATION.md created. 6 hooks + 1 supplementary. Event matrix, output formats, compaction policy (10-entry threshold), staging→archive pipeline, verification checklist."

- id: IMPL-A-0012
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "Phase 3: Backlog Reconciliation"
  intent: Make Linear the source of truth for tasks while keeping repo snapshot.
  deliverable: Design Linear workspace structure + spec sync: Linear ↔ DYN-BACKLOG.md + session-scoped todos.
  dependencies: Linear API/MCP decision.
  owner_lane: Psyche (design) + Commander (implementation)
  venue: linear+repo
  status: done
  linear_id: SYN-16
  notes: "DONE 2026-02-11: SYN-16 complete — 197/197 IMPL entries linked to 42 unique SYN issues (100% bridge coverage). Linear workspace: 56 issues, 36 Done, 20 open."

- id: IMPL-A-0013
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "Phase 2: FDIS Foundation (#7-#9)"
  intent: Triangulate FDIS requirements and deployment surface.
  deliverable: FDIS requirements doc + minimal deployable node spec (hardware/software/network), with dependency mapping to CANON + Intent Compass.
  dependencies: Canon cross-reference; hardware inventory.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-17

- id: IMPL-A-0014
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "MCP Server Buildout"
  intent: Enable cross-tool data sharing via MCP servers.
  deliverable: Prioritized MCP rollout plan + initial Slack + Linear servers (or alternatives), with config templates committed.
  dependencies: Credentialing + security posture.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-18
  notes: "Completed 2026-02-10: 9 MCP servers LIVE — Linear (33 tools, plugin), ClickUp, Graphiti (9), Obsidian (11), Filesystem (16), Chrome DevTools (18+), Playwright (20+), Qdrant (2), Gemini-MCP (6). Slack MCP deferred (free tier, low priority). Config in ~/.claude.json."

- id: IMPL-A-0015
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "Phase 4: Velocity Management"
  intent: Manage token/cost burn and lane routing.
  deliverable: Routing matrix + budget alerts (50%/70%/85%) and default model downshift rules.
  dependencies: Usage telemetry surface.
  owner_lane: Ajna + Psyche
  venue: repo
  status: new
  linear_id: SYN-19

## 2026-02-06 — Tranche A (Spine): Four-Systems operationalization (modes → implementation)

- id: IMPL-A-0016
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "System 1: Automatic-Push (Scheduled Monitoring)"
  intent: Turn System 1 from concept into a runnable scheduled monitor.
  deliverable: Minimal System-1 runner spec + script (or Makefile target) that polls a defined feed list and writes a Daily/Weekly Brief artifact to agents/ or SOURCES/inbox/processed/.
  dependencies: Decide feed sources + auth surface (RSS/Feedly/YouTube); scheduling surface (launchd vs cron).
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-A-0017
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "System 2: Curation-Push (Serendipitous Discovery)"
  intent: Create a frictionless 'save-to-queue' ingestion path.
  deliverable: A capture protocol for watch-later/bookmark inputs (YouTube Watch Later, browser share sheet, etc.) with a deterministic queue file format and a processor that deposits cleaned sources into 04-SOURCES/processed/.
  dependencies: Decide capture surfaces (YouTube playlist polling, Pocket/Instapaper, Apple Notes, etc.).
  owner_lane: Psyche (spec) + Commander (impl)
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-A-0018
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "System 3: On-Demand-Pull (Active Research)"
  intent: Standardize research packets so outputs are comparable and reusable.
  deliverable: Research packet template (frontmatter + sections + citation requirements) and a routing rule: when to use Cartographer (Gemini CLI), Augur (Perplexity), Oracle (Grok), or web_search.
  dependencies: Toolchain interaction protocol (IMPL-A-0010) and CANON-31150 catalog update (IMPL-A-0008).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-A-0019
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "System 4: Triage & Qualification (Gatekeeper)"
  intent: Make triage an explicit, fast, repeatable gate for every incoming source.
  deliverable: A triage checklist + classification schema (signal_tier, value_modality) with a ‘30-second scan’ SOP and default routing decisions.
  dependencies: Existing TRIAGE_PROTOCOL.md / PROCESSING_ROUTING.md (if present) and SOURCES schema references.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-A-0020
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "Critical Questions (value modality)"
  intent: Operationalize value_modality so the apparatus chooses the right medium (read/watch/listen) by default.
  deliverable: Value-modality decision tree + mapping to processing functions (readize/listenize/transcribe/watch) and a required field in source frontmatter.
  dependencies: Function library docs + source frontmatter schema agreement.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-A-0021
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "How Systems Interact (diagram)"
  intent: Make the interaction model executable (not just a diagram).
  deliverable: A single ‘source intake’ state machine spec showing entrypoints (System 1/2/3) → triage (System 4) → outcomes (process/queue/archive/prune) with filenames/dirs.
  dependencies: Dispatch kanban protocol + directory conventions (agents/<agent>/inbox/04-SOURCES).
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-A-0022
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "MVP Implementation (Manual batch processing)"
  intent: Replace “manual” MVP statements with explicit automation milestones.
  deliverable: A milestone table (M0 manual → M1 semi-auto → M2 scheduled) for each of the four systems, with acceptance tests.
  dependencies: None.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-A-0023
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "Future automation: n8n / scheduled triggers"
  intent: Decide and document the automation substrate for scheduled + event-driven ingestion.
  deliverable: DecisionAtom: launchd/cron vs n8n vs OpenClaw cron; include security posture and portability.
  dependencies: /claresce Pass 1-3 on automation policy (truth surface + reliability).
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-45

- id: IMPL-A-0024
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "IIC Mapping (Acumen/Coherence)"
  intent: Connect operational modes to IIC configs so routing can be identity-aware.
  deliverable: Mapping table: System 1-4 → IIC streams (Acumen/Coherence) and default recipients/inboxes; note SLA/brief cadence.
  dependencies: IIC config status + CANON IIC docs.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-49

- id: IMPL-A-0025
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "Cross-References (SOURCES_SCHEMA/TRIAGE_PROTOCOL/PROCESSING_ROUTING)"
  intent: Remove dangling references / make cross-refs real.
  deliverable: Verify referenced docs exist; if missing, create minimal stubs or update links to current equivalents.
  dependencies: Repo scan for actual filenames.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-20

- id: IMPL-A-0026
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "System Selection Guide"
  intent: Provide a quick operator UI for choosing which system to invoke.
  deliverable: A short operator command reference (e.g., make auto-push, make curate-push, make research-pull, make triage) that routes to the correct scripts and writes receipts.
  dependencies: Scripts created in IMPL-A-0016/0017/0018/0019.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-45

## 2026-02-06 — Tranche B (Execution substrate): Twin coordination + Intent Compass mechanics + Dispatch Kanban

- id: IMPL-B-0001
  source_path: 00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "Sovereign Contact Rules"
  intent: Make ‘when to ping Phillip’ enforceable instead of aspirational.
  deliverable: A decision gate checklist (blocking/safety/data-loss/ratification bundle) implemented as (a) a template section in RESULT receipts and (b) optional OpenClaw notify helper that requires selecting one of the allowed reasons.
  dependencies: Agreement on notification channels; OpenClaw notify semantics.
  owner_lane: Psyche
  venue: repo+tool
  status: new
  linear_id: SYN-14

- id: IMPL-B-0002
  source_path: 00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "Inter-Twin Communication"
  intent: Make TWIN handoffs durable and discoverable.
  deliverable: Create canonical folder + naming spec for `TWIN-{FROM}-{TO}-{topic}.md` (or update to current kanban structure) and add a simple index/ledger entry type for TWIN relays.
  dependencies: Decide whether TWIN relays live in `agents/<agent>/inbox/` or a shared `agents/outputs/inbox/` resurrected equivalent.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-B-0003
  source_path: 00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "Git: Only Ajna commits"
  intent: Reduce merge/drift risk while allowing Psyche to contribute safely.
  deliverable: Document ‘Psyche contribution protocol’: Psyche opens PATCH artifacts (diffs) or PR branches; Ajna merges/commits. Include receipts: how to produce a patch bundle.
  dependencies: Decide branch naming + patch handoff surface (agents/psyche/outbox/PATCH-* vs agents/psyche/outbox/ARTIFACTS).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-27

- id: IMPL-B-0004
  source_path: 00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "Update Format (both twins)"
  intent: Standardize twin update payloads so they can be parsed/summarized automatically.
  deliverable: A `TWIN-UPDATE` markdown template + optional linter that verifies required headings + max bullets constraints.
  dependencies: None.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-B-0005
  source_path: 00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "Autonomous Work Cycle"
  intent: Convert heartbeat guidance into an executable checklist.
  deliverable: Add a `make twin-heartbeat` (or equivalent) that runs: git log tail, inbox queue status, ledger tail, and emits a short TWIN-UPDATE stub.
  dependencies: queue_status.sh availability; ledger paths.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-B-0006
  source_path: .claude/skills/intentions.md
  source_lines: "PURPOSE + PROCESS (Capture/Categorization/Integration)"
  intent: Ensure the Intent Compass loop is closed end-to-end (hook → queue → compass).
  deliverable: A concrete triage SOP: how often to triage DYN-INTENTIONS_QUEUE.md, how to assign IDs, and what ‘flush’ means (move vs copy vs archive). Include acceptance: queue empties or entries marked triaged.
  dependencies: Confirm current locations: DYN-INTENTIONS_QUEUE.md, ARCH-INTENTION_COMPASS.md.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-B-0007
  source_path: .claude/skills/intentions.md
  source_lines: "ID Assignment"
  intent: Prevent intention ID collisions and ensure IDs are machine-derivable.
  deliverable: Define an ID authority + generator (script or make target) that allocates INT IDs and appends to compass; enforce uniqueness via lint.
  dependencies: Decide oracle numbering source; lint framework.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-B-0008
  source_path: .claude/skills/intentions.md
  source_lines: "ANTI-PATTERNS (False resolution / orphan intentions)"
  intent: Add verification before marking intentions resolved.
  deliverable: Compass schema extension: `evidence:` or `integrated_into:` required when status transitions to resolved; add a checker that fails if missing.
  dependencies: Compass file schema governance.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-B-0009
  source_path: 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  source_lines: "Per-Agent Outbox Structure + RESULT Receipt Determinism"
  intent: Align watchers and humans on where RESULT receipts live.
  deliverable: Create `agents/<agent>/outbox/{RESULTS,ARTIFACTS}/` structure in repo + update watcher scripts to write there.
  dependencies: watch_dispatch.sh implementation state; repo directory conventions.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-B-0010
  source_path: 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  source_lines: "Dispatch Kinds + header field requirements"
  intent: Make Kind gating and schema validation a hard safety rail.
  deliverable: Add a kanban linter (or extend ops_lint) that validates headers: Kind ∈ allowed set, To matches folder agent, Receipts-To is safe/relative, and Timeout is numeric.
  dependencies: ops_lint.sh extension work.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-B-0011
  source_path: 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  source_lines: "Lifecycle (Claim/Process/Complete/Fail)"
  intent: Ensure lifecycle transitions are auditable.
  deliverable: Ledger policy: required events (DISPATCH/CLAIM/COMPLETE/FAILED/BLOCKED/WAITING) and required fields in each event; implement missing events if any.
  dependencies: DYN-GLOBAL_LEDGER schema; append_ledger.sh.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-B-0012
  source_path: 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  source_lines: "Cross-Claim Prevention"
  intent: Prevent wrong-agent execution and forensic ambiguity.
  deliverable: Update watcher claim code to enforce `To:` matches agent AND record `Claimed-By=<agent>-<hostname>`; add a health check that scans IN_PROGRESS for stale claims.
  dependencies: watcher_health.sh and watch_dispatch.sh.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

## 2026-02-06 — Tranche C (Canon hotspots): Multi-agent orchestration + Memory systems + Tech stack DB

- id: IMPL-C-0001
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md
  source_lines: "PART II: Five Core Orchestration Patterns"
  intent: Map industry orchestration patterns onto Syncrescendence’s actual execution substrate.
  deliverable: A mapping doc/table: {Sequential, Concurrent, Group Chat, Handoff, Magentic} → {Neo‑Blitzkrieg stages, OpenClaw primitives, inbox kanban, sessions_spawn}, with a ‘when to use’ router.
  dependencies: Neo‑Blitzkrieg spec + Toolchain interaction protocol.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-35

- id: IMPL-C-0002
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md
  source_lines: "PART III: Collaboration Topologies"
  intent: Choose a default collaboration topology for the Constellation.
  deliverable: DecisionAtom: default topology (Hub‑and‑spoke + mesh) with explicit allowed deviations (critic‑refiner, planner‑executor, swarm) and their triggers.
  dependencies: /claresce passes 1–3 (truth surface + lifecycle semantics).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-35

- id: IMPL-C-0003
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md
  source_lines: "PART IV: Protocol Landscape (MCP/A2A)"
  intent: Clarify protocol posture: what we actually implement vs track as ecosystem.
  deliverable: Protocol posture doc: MCP (tool integration) vs A2A (agent discovery) vs filesystem kanban; include security implications and adoption roadmap aligned to Syncrescendence.
  dependencies: Existing MCP config templates + kanban protocol.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-18

- id: IMPL-C-0004
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md
  source_lines: "PART IV: Message Architecture"
  intent: Standardize inter-agent message headers so automation can parse them.
  deliverable: A minimal message schema for dispatch artifacts (type/intent/priority/origin/correlation_id/provenance) that fits in the existing TASK header format.
  dependencies: DYN-DISPATCH_KANBAN_PROTOCOL.md header fields.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-C-0005
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md
  source_lines: "PART VIII: Safety Considerations + Progressive Trust Model"
  intent: Prevent over-autonomy before reliability is proven.
  deliverable: Progressive trust ladder for lanes (Commander/Adjudicator/Cartographer/OpenClaw): allowed actions by level, required verification gates, and ‘promotion’ criteria.
  dependencies: Safety policy + external-send boundaries.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-35

- id: IMPL-C-0006
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
  source_lines: "PART I: Memory Taxonomy"
  intent: Map Syncrescendence artifacts to canonical memory types.
  deliverable: Memory architecture map: Working/Episodic/Semantic/Procedural/Prospective → concrete files/dirs (MEMORY.md, memory/YYYY-MM-DD.md, CANON/, skills/, cron/jobs, Linear).
  dependencies: Decide prospective-memory truth surface (cron vs Linear).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-C-0007
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
  source_lines: "PART IV: Context Engineering Strategies"
  intent: Reduce context pollution and staleness.
  deliverable: A ‘context engineering policy’ for sessions: chunking conventions, relevance scoring heuristics, temporal decay signals, and hierarchical summarization triggers.
  dependencies: Existing memory + canon regen processes.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-C-0008
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
  source_lines: "PART IV: Sleep-Time Compute"
  intent: Turn idle time into durable memory maintenance.
  deliverable: Sleep-time compute job set (OpenClaw cron / launchd): summarize recent logs, refresh stale claims, prune/annotate, and write curated updates to MEMORY.md / state.
  dependencies: Decide automation substrate; guardrails for auto-edits.
  owner_lane: Ajna
  venue: tool+repo
  status: new
  linear_id: SYN-45

- id: IMPL-C-0009
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
  source_lines: "PART VI: Memory Interfaces"
  intent: Ensure memory operations are explicit and auditable.
  deliverable: Define Memory Interface ops for Syncrescendence: write/read/update/forget with logging; decide what is manual-only vs automatable.
  dependencies: Ledger schema + memory governance.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-C-0010
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
  source_lines: "PART VII: Consistency and Coherence"
  intent: Prevent hallucination propagation into durable memory.
  deliverable: Memory verification gates: require source attribution/confidence; introduce ‘deprecated/stale’ markers; periodic re-verify policy.
  dependencies: DecisionAtom on truth/verification surfaces.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-C-0011
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
  source_lines: "PART VIII: Security Considerations"
  intent: Avoid leaking PII/secrets via memory and logs.
  deliverable: Memory security policy: access control boundaries, encryption-at-rest posture (if any), PII handling rules, and audit logging expectations.
  dependencies: Current security posture + token handling decisions.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-57

- id: IMPL-C-0012
  source_path: 01-CANON/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md
  source_lines: "MIGRATION PROTOCOL (Phases 1–6)"
  intent: Turn Tech Stack DB from schema doc into a populated, queryable system.
  deliverable: Implement migration: create DB (sqlite/postgres), populate bedrock tables, import Function.csv/Models.csv/API.csv, run integrity checks, and produce a ‘migration receipt’.
  dependencies: Locate CSV sources; choose DB backend.
  owner_lane: Adjudicator + Commander
  venue: repo
  status: done
  linear_id: SYN-22
  notes: "SQLite ontology DB at 939 rows, 21 tables. DYN-FUNCTIONS.csv (89 entries), DYN-MODELS.csv, DYN-API_COSTS.csv populated. ontology_query.py CLI operational. 0 FK violations. Completed 2026-02-10."

- id: IMPL-C-0013
  source_path: 01-CANON/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md
  source_lines: "Navigation Specifications + CLI Mockups"
  intent: Make the Tech Stack DB usable for daily routing decisions.
  deliverable: Minimal CLI (or make targets) for: search, context routing, primitive lookup, apparatus view, model cost compare.
  dependencies: DB created + populated.
  owner_lane: Adjudicator
  venue: repo
  status: done
  linear_id: SYN-22
  notes: "ontology_query.py: 21 commands (stats/search/layers/apps/primitives/apparatus/projects/tasks/sources/actions/agent-bindings/workflows/commitments/goals/risks/resources/relationships/environments/verbs/dashboard/sql). Schema v1.3.0, 2015 rows, 43 tables. Dashboard command provides full strategic overview. Completed 2026-02-12."

- id: IMPL-C-0014
  source_path: 01-CANON/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md
  source_lines: "MAINTENANCE PROTOCOLS"
  intent: Keep tech stack intelligence from going stale.
  deliverable: Maintenance cadence implemented as jobs: weekly model/pricing refresh, monthly primitive extraction prompts, quarterly integrity audits.
  dependencies: Automation substrate decision.
  owner_lane: Ajna
  venue: tool+repo
  status: done
  linear_id: SYN-22
  notes: "ontology_maintain.py — 3 commands (refresh/audit/report). make ontology-refresh + make ontology-audit. Completed 2026-02-12."

- id: IMPL-C-0015
  source_path: 01-CANON/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md
  source_lines: "Falsification Criteria + Success Criteria"
  intent: Make the Tech Stack DB falsifiable and measurable.
  deliverable: Add acceptance tests + metrics tracking (coverage %, duplicates, query latency) and a simple report artifact produced by CI or make verify.
  dependencies: DB + CLI.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-22
  notes: "ontology_verify.py — 47 tests. make ontology-verify. 46 PASS, 1 WARN. Completed 2026-02-12."

## 2026-02-06 — Tranche D (Tooling + integration): Makefile + GitHub connector protocol

- id: IMPL-D-0071
  source_path: Makefile
  source_lines: "verify target (wc -l < DYN-TASKS.csv / DYN-PROJECTS.csv)"
  intent: Prevent make verify from hard-failing on first-run or missing ledger files.
  deliverable: Makefile verify/update-ledgers targets become missing-file tolerant (print 0/Not found instead of error).
  dependencies: Align behavior with verify_all.sh hardening plan.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-32

- id: IMPL-D-0072
  source_path: Makefile
  source_lines: "verify: Root .md files count"
  intent: Make structure verification meaningful and consistent with repo conventions.
  deliverable: Replace raw root .md count with explicit allowlist check (and surface offending filenames).
  dependencies: Decide canonical allowed root markdown list.
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-32
  notes: "Completed 2026-02-09: Makefile verify now checks CLAUDE.md, README.md explicitly and reports unexpected .md files."

- id: IMPL-D-0073
  source_path: Makefile
  source_lines: "update-ledgers: sources.csv rows"
  intent: Ensure update-ledgers can run even if sources ledger is absent.
  deliverable: Guard `04-SOURCES/DYN-SOURCES.csv` reads with existence check.
  dependencies: None.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-32
  notes: "Completed 2026-02-09: Makefile update-ledgers sources.csv wrapped in if-exists guard."

- id: IMPL-D-0074
  source_path: Makefile
  source_lines: "tree target uses tree"
  intent: Avoid tool dependency failures on machines without `tree` installed.
  deliverable: Fallback behavior: if tree missing, run `find` summary; or document dependency and add install helper.
  dependencies: Decide preferred baseline tooling on Ajna/Psyche hosts.
  owner_lane: Adjudicator
  venue: repo
  status: done
  linear_id: SYN-34
  notes: "Completed 2026-02-09: Makefile tree target now checks for tree binary, falls back to find with install hint."

- id: IMPL-D-0075
  source_path: Makefile
  source_lines: "clean target deletes *.bak.* older than 7d"
  intent: Avoid accidental deletion of meaningful artifacts.
  deliverable: Confirm clean only touches explicitly safe temp patterns; add dry-run mode or restrict to /tmp + known scratch dirs.
  dependencies: None.
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-32
  notes: "Completed 2026-02-09: clean target excludes .git, suppresses errors, safe patterns only."

- id: IMPL-D-0076
  source_path: Makefile
  source_lines: "token/token-json/token-full"
  intent: Ensure token generation is durable cross-platform (not macOS-only).
  deliverable: Replace pbcopy hard-dependency with conditional clipboard support (pbcopy/xclip/wl-copy/no-clipboard) and always write artifact files.
  dependencies: Cross-host OS assumptions.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-34

- id: IMPL-D-0077
  source_path: Makefile
  source_lines: "regenerate-canon / model-db targets"
  intent: Make intelligence targets discoverable and safe.
  deliverable: Add target help text and add a `make ops-health` umbrella that runs lint+verify-full+queue status (ties to IMPL-D-0057/0068).
  dependencies: watcher_health.sh existence.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-32

- id: IMPL-D-0078
  source_path: .github/CONNECTOR_PROTOCOL.md
  source_lines: "Entry Points (CLAUDE.md / CHATGPT.md / GEMINI.md / README.md)"
  intent: Remove protocol drift: ensure all entrypoint files exist and reflect current truth.
  deliverable: Create missing CHATGPT.md (and/or update filenames) and ensure CLAUDE.md/GEMINI.md/README.md are current; update CONNECTOR_PROTOCOL if names differ.
  dependencies: Identify actual current entrypoints in repo.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-34

- id: IMPL-D-0079
  source_path: .github/CONNECTOR_PROTOCOL.md
  source_lines: "Ground truth: main branch on GitHub is canonical"
  intent: Resolve potential contradiction with “Desktop repo is ground truth” doctrine.
  deliverable: DecisionAtom: define ground-truth precedence (local desktop vs GitHub main) and when ‘GitHub main’ becomes canonical for connector reads.
  dependencies: Sovereign ratification; security posture.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-30

- id: IMPL-D-0080
  source_path: .github/CONNECTOR_PROTOCOL.md
  source_lines: "Never: create conflicting branches (single-branch workflow)"
  intent: Decide whether single-branch remains tenable as automation increases.
  deliverable: DecisionAtom: branching policy (single-branch vs short-lived branches/PRs) tied to kanban + watcher automation and conflict risk.
  dependencies: Neo-Blitzkrieg + watcher maturity.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-30

- id: IMPL-D-0081
  source_path: .github/CONNECTOR_PROTOCOL.md
  source_lines: "Token Economics / Navigation Strategy"
  intent: Provide a self-contained ‘connector navigation playbook’ that web agents can follow.
  deliverable: A concise, current navigation cheat sheet (grep-first, line ranges, cache policy) placed in each platform entrypoint file.
  dependencies: Entry point files existence.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-19

- id: IMPL-D-0082
  source_path: .github/CONNECTOR_PROTOCOL.md
  source_lines: "Write path: platform generates spec → CLI executes → commit → push"
  intent: Make write-path enforceable with receipts.
  deliverable: Add required receipt fields to PATCH/TASK outputs: commit hash, files changed, and push confirmation; update task templates accordingly.
  dependencies: Dispatch kanban protocol + RESULT receipt format.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

## 2026-02-06 — Tranche D (Tooling + integration): Script surfaces (verify/lint/triage/canon regen)

- id: IMPL-D-0083
  source_path: 00-ORCHESTRATION/scripts/verify_all.sh
  source_lines: "Structure Verification → Root .md files (expected <=2 mismatch)"
  intent: Make verification truthful and non-brittle.
  deliverable: Fix allowlist vs message mismatch; switch to explicit allowlist and surface offending files; set -euo pipefail; tolerate missing optional artifacts.
  dependencies: Decide canonical root .md allowlist; align with Makefile verify.
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-32
  notes: "Completed 2026-02-09: verify_all.sh switched to explicit CLAUDE.md/README.md allowlist, reports unexpected files. Aligned with Makefile verify."

- id: IMPL-D-0084
  source_path: 00-ORCHESTRATION/scripts/verify_all.sh
  source_lines: "Ledger Verification: Not found handling"
  intent: Standardize missing-file policy across ops commands.
  deliverable: Define which missing ledgers are ERROR vs WARN; ensure verify-full exits nonzero only on true invariants.
  dependencies: Repo invariants doc (if any).
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-32

- id: IMPL-D-0085
  source_path: 00-ORCHESTRATION/scripts/ops_lint.sh
  source_lines: "check_frontmatter(): only checks presence of keys"
  intent: Turn ops_lint into a correctness gate.
  deliverable: Validate kind ∈ allowed set, id uniqueness, YAML parse, and filename/id convention alignment; add summary output suitable for CI.
  dependencies: Allowed kinds + naming conventions per directory.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-20

- id: IMPL-D-0086
  source_path: 00-ORCHESTRATION/scripts/ops_lint.sh
  source_lines: "Scope limited to flat 02-ENGINE/"
  intent: Prevent frontmatter drift in other critical zones.
  deliverable: Extend lint coverage to additional directories (00-ORCHESTRATION/state/*, 01-CANON/*) or add separate linters with explicit scopes.
  dependencies: Performance constraints + false-positive policy.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-20

- id: IMPL-D-0087
  source_path: 00-ORCHESTRATION/scripts/triage_outgoing.sh
  source_lines: "PENDING/IN_PROGRESS grep across inbox"
  intent: Make triage reflect kanban truth rather than header regex.
  deliverable: Update triage to report counts by lane folders (00/10/20/30/40/50) and flag mismatches between folder state and header Status/Kanban.
  dependencies: Kanban protocol; queue_status.sh (if present).
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-14
  notes: "Completed 2026-02-09: triage_outgoing.sh now reports per-agent lane with individual task status."

- id: IMPL-D-0088
  source_path: 00-ORCHESTRATION/scripts/triage_outgoing.sh
  source_lines: "Requires rg for best output"
  intent: Avoid optional tool dependencies breaking observability.
  deliverable: Add clear dependency banner + robust fallback; optionally vendor a minimal ripgrep check/install helper.
  dependencies: Baseline tooling policy.
  owner_lane: Adjudicator
  venue: repo
  status: new
  linear_id: SYN-34

- id: IMPL-D-0089
  source_path: 00-ORCHESTRATION/scripts/regenerate_canon.py
  source_lines: "regenerate_all(): prints human output only"
  intent: Make canon regen observable and machine-parseable.
  deliverable: Add --json output (or deterministic stdout markers) that returns regenerated CANON IDs + status so watch_canon can log exact IDs and emit ledger REGEN events.
  dependencies: watch_canon.sh expectations (IMPL-D-0055/0059/0060).
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: regenerate_canon.py --json flag added for --list and --all modes."

- id: IMPL-D-0090
  source_path: 00-ORCHESTRATION/scripts/regenerate_canon.py
  source_lines: "jinja2 auto-install via pip"
  intent: Avoid surprise network/package changes during daemon runs.
  deliverable: Remove auto-install in production path; instead fail fast with remediation steps or preflight install; document dependencies.
  dependencies: Host bootstrap policy.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: Replaced auto-install with fail-fast sys.exit(1) and remediation message."

## 2026-02-06 — Tranche D (Tooling + integration): intent_compass / dispatch / canon watch

- id: IMPL-D-0091
  source_path: 00-ORCHESTRATION/scripts/intent_compass.sh
  source_lines: "SIGNALS=… (intention signal patterns)"
  intent: Reduce false positives/negatives in auto intention capture.
  deliverable: Replace grep regex list with a small, versioned ruleset (YAML/JSON) + add basic tests (sample prompts → expected capture yes/no).
  dependencies: Decide where rules live (00-ORCHESTRATION/state/ or 02-ENGINE/).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-D-0092
  source_path: 00-ORCHESTRATION/scripts/intent_compass.sh
  source_lines: "CAPTURED=… head -1 | cut -c1-200"
  intent: Preserve more context while keeping the queue lightweight.
  deliverable: Capture up to N lines with surrounding context (or store full prompt hash + pointer), and include a stable correlation_id for later triage.
  dependencies: Define queue entry schema.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-D-0093
  source_path: 00-ORCHESTRATION/scripts/intent_compass.sh
  source_lines: "QUEUE_FILE=… DYN-INTENTIONS_QUEUE.md"
  intent: Make intention capture robust under concurrent hook calls.
  deliverable: Add an atomic append strategy (lockfile or flock) so simultaneous prompts don’t interleave writes.
  dependencies: macOS flock availability (or mkdir lock).
  owner_lane: Adjudicator
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-D-0094
  source_path: 00-ORCHESTRATION/scripts/intent_compass.sh
  source_lines: "jq -r '.prompt'"
  intent: Avoid silent failure when jq is missing or input schema changes.
  deliverable: Preflight check for jq; if missing, emit a warning once (rate-limited) and exit 0; document hook input schema assumptions.
  dependencies: Baseline tooling policy.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-15
  notes: "Completed 2026-02-09: jq preflight added — silent exit 0 if missing (hook must not block prompts)."

- id: IMPL-D-0095
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Ensure kanban dirs exist (00/10/40/50/RECEIPTS only)"
  intent: Align dispatch with full kanban lane set.
  deliverable: dispatch.sh should create all lanes per DYN-DISPATCH_KANBAN_PROTOCOL.md (00/10/20/30/40/50/90/RECEIPTS) to avoid inconsistent boards.
  dependencies: Kanban protocol.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0096
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "KIND_RAW default + no validation"
  intent: Prevent invalid Kind values from entering the system.
  deliverable: Validate KIND_RAW ∈ allowed set; if invalid, fail with help text.
  dependencies: Allowed kind set (already in DYN protocol).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0097
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Receipts-To: agents/<agent>/outbox"
  intent: Ensure -OUTBOX directory exists and is git-tracked policy-wise.
  deliverable: dispatch.sh should mkdir -p agents/<agent>/outbox/{RESULTS,ARTIFACTS} and/or emit a clear warning if missing.
  dependencies: Decision: track empty dirs via .keep files or mkdir at runtime only.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0098
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Timeout: 30"
  intent: Make timeouts meaningful and consistent across watchers.
  deliverable: Define timeout semantics (minutes vs seconds) and ensure watchers interpret it the same; add a recommended default by Kind.
  dependencies: watch_dispatch.sh wall-clock timeout work (IMPL-D-0051).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0099
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Completion Protocol: update Status PENDING→COMPLETE"
  intent: Remove mismatch: folder is canonical state, not header.
  deliverable: Update task template text to say ‘move to DONE/FAILED’ (or watcher will) and header fields are mirrors; discourage manual header edits.
  dependencies: Kanban doctrine.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0100
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Append ledger DISPATCH if append_ledger.sh exists"
  intent: Make ledger logging reliable and complete.
  deliverable: If append_ledger.sh missing/not executable, print a WARN; optionally bundle a no-op stub; ensure DISPATCH always logged.
  dependencies: Ledger governance.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0101
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "append_regen_log(): hardcodes CANON IDs as 31150"
  intent: Fix known observability bug.
  deliverable: Replace hardcoded '31150' with actual regenerated IDs (from regenerate_canon.py --json or markers).
  dependencies: IMPL-D-0089.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: regenerate() now uses --json output, extracts canon_ids via Python, passes to append_regen_log."

- id: IMPL-D-0102
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "fswatch loop: no lock; regen can overlap"
  intent: Prevent overlapping regen runs.
  deliverable: Add a lockdir (mkdir) around regenerate(); debounce already exists but isn't sufficient for long regens.
  dependencies: None.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: mkdir /tmp/syncrescendence-canon.lock guard with trap cleanup on RETURN."

- id: IMPL-D-0103
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "build_watch_paths(): adds REPO_ROOT/wp without existence check"
  intent: Make diagnostics first-class so missing watch inputs aren’t silent.
  deliverable: Add --diagnose mode that prints resolved watch set + exits nonzero if critical missing.
  dependencies: Define ‘critical’ watch paths.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-D-0104
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "Requires: fswatch, python3, jinja2"
  intent: Make watcher safe for daemon environments.
  deliverable: Preflight dependency checks + clear remediation; avoid any auto-install in regen path.
  dependencies: IMPL-D-0090.
  owner_lane: Adjudicator
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-D-0105
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "No ledger events emitted"
  intent: Make canon regen part of the global audit trail.
  deliverable: Emit ledger REGEN events (trigger/status/ids) via append_ledger.sh.
  dependencies: Decide ledger event schema fields.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-29

## 2026-02-06 — Tranche D (Tooling): Always-on watchers (launchd) hardening + smoke validation

- id: IMPL-D-0034
  source_path: 00-ORCHESTRATION/scripts/rearm_watchers.sh
  source_lines: "mode selection + plist source dir"
  intent: Make launchd watcher installs deterministic across machines/users.
  deliverable: Maintain explicit plist sets per host persona (mini/home vs psyche/system) and ensure rearm_watchers.sh selects correctly.
  dependencies: 00-ORCHESTRATION/scripts/launchd-mini/*, 00-ORCHESTRATION/scripts/launchd-psyche/*
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-34

- id: IMPL-D-0035
  source_path: 00-ORCHESTRATION/scripts/launchd-mini/com.syncrescendence.watch-*.plist
  source_lines: "ProgramArguments + WorkingDirectory"
  intent: Hardcode Mac mini home base paths to user `home` (per Sovereign).
  deliverable: Keep mini plists pinned to /Users/home/Desktop/syncrescendence and keep them the canonical install source for --mini.
  dependencies: None
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-34

- id: IMPL-D-0036
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "process_task case routing"
  intent: Guarantee that every executed task produces a durable receipt artifact.
  deliverable: Capture executor stdout/stderr into agents/<agent>/outbox/RESULT-<agent>-<date>-<topic>.md (or a deterministic name derived from the task filename) automatically; link it in task header and ledger.
  dependencies: dispatch.sh naming conventions; agents/<agent>/outbox/ directory structure; ledger event schema
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0037
  source_path: agents/commander/outbox/RESULT-commander-20260205-always_on_watchers_sweep.md
  source_lines: "Remediation Plan (Blockers 1-3)"
  intent: Restore always-on readiness for Ajna + Adjudicator + Commander on the Mac mini.
  deliverable: (1) Install OpenClaw on mini (openclaw binary + gateway), (2) configure Codex auth (codex login or API key), (3) resolve Claude billing/plan path for Commander.
  dependencies: Access to mini; provider credentials/billing
  owner_lane: Sovereign + Commander
  venue: tool
  status: queued
  linear_id: SYN-34

- id: IMPL-D-0038
  source_path: 00-ORCHESTRATION/scripts/rearm_watchers.sh
  source_lines: "bootout/bootstrap/kickstart"
  intent: Make watcher state auditable and self-checked.
  deliverable: Add a companion script (e.g., watcher_health.sh) that prints: launchctl state, PATH/env, binary resolution, last 50 log lines, and recent task failures per agent.
  dependencies: launchctl; /tmp log paths; ledger
  owner_lane: Adjudicator (Codex) + Commander
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-D-0039
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Expected Output section"
  intent: Align task contract with actual watcher behavior.
  deliverable: Either (A) implement RESULT writing in watchers (preferred), or (B) change task templates to state that receipts live in /tmp logs + ledger.
  dependencies: Decision on receipt truth surface
  owner_lane: Psyche + Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0040
  source_path: 00-ORCHESTRATION/scripts/launchd-*/com.syncrescendence.watch-*.plist
  source_lines: "EnvironmentVariables"
  intent: Reduce noise and drift in daemonized environments.
  deliverable: Standardize NODE_OPTIONS=--no-warnings and NODE_NO_WARNINGS=1 across all watcher plists (mini + psyche), and ensure installed copies match repo source.
  dependencies: None
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-D-0041
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "Auth tests implied by executor calls"
  intent: Prevent "watcher running but executor unusable" states from masquerading as healthy.
  deliverable: Add optional startup self-test mode per agent (verify command -v + minimal PONG) and emit FAILED_PRECHECK to ledger if missing.
  dependencies: Safe non-interactive auth checks for each CLI
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-45


## 2026-02-06 — Tranche D (Tooling): OpenClaw outfitment sync (Ajna ↔ Psyche)

- id: IMPL-D-0042
  source_path: 00-ORCHESTRATION/state/impl/tooling/OUTFITMENT-SYNC.md
  source_lines: "Goal + sync/non-sync definitions"
  intent: Make Ajna and Psyche share the same OpenClaw capability surface while keeping secrets local.
  deliverable: Ratified outfitment sync policy and operational verification checklist.
  dependencies: None
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-27

- id: IMPL-D-0043
  source_path: 00-ORCHESTRATION/scripts/sync_openclaw_skills.sh
  source_lines: "SKILLS allowlist + rsync excludes"
  intent: Provide a repeatable, secrets-safe mechanism for mirroring OpenClaw workspace skills between hosts.
  deliverable: rsync-based skill sync script with conservative allowlist + node_modules/dist excludes.
  dependencies: SSH reachability + host aliasing between machines
  owner_lane: Psyche
  venue: repo
  status: mapped
  linear_id: SYN-43

- id: IMPL-D-0044
  source_path: agents/ajna/outbox/RESULT-ajna-20260205-outfitment_sync_and_smoketest.md
  source_lines: "Phase 1 SSH reachability failures"
  intent: Remove SSH trust/bootstrap friction as a blocker for operational sync.
  deliverable: Establish stable SSH aliasing (psyche/ajna), host discovery method, and host-key pinning procedure; generate receipts (fingerprints).
  dependencies: LAN reachability; SSH keys; known_hosts hygiene
  owner_lane: Ajna + Commander
  venue: tool
  status: queued
  linear_id: SYN-43

- id: IMPL-D-0045
  source_path: agents/ajna/outbox/RESULT-ajna-20260205-sync_outfitment.md
  source_lines: "CRITICAL: OAuth dir missing (~/.openclaw/credentials)"
  intent: Ensure OpenClaw OAuth-based providers (openai-codex) are stable on Ajna.
  deliverable: Run `openclaw doctor --fix` (or equivalent) and verify ~/.openclaw/credentials exists; add a watcher preflight that fails fast if missing.
  dependencies: OpenClaw CLI; ability to restart gateway
  owner_lane: Ajna
  venue: tool
  status: done
  linear_id: SYN-27

- id: IMPL-D-0046
  source_path: 00-ORCHESTRATION/scripts/sync_openclaw_skills.sh
  source_lines: "REMOTE_HOME probe + remote skills dir"
  intent: Make the sync script robust across differing usernames (home/system) without guesswork.
  deliverable: Add explicit flags for remote user/path (e.g., --from-user, --from-skills-dir), and write receipts for resolved REMOTE_HOME and final resolved REMOTE_SKILLS_DIR.
  dependencies: SSH
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-27

- id: IMPL-D-0047
  source_path: 00-ORCHESTRATION/state/impl/tooling/OUTFITMENT-SYNC.md
  source_lines: "Verification"
  intent: Provide a deterministic parity smoke test that proves synced skills are actually loadable.
  deliverable: A dedicated smoke task that invokes a non-core workspace skill on Ajna (e.g., supermemory/hindsight integration) and returns a clear PASS/FAIL receipt.
  dependencies: Skill load + plugin enablement state
  owner_lane: Psyche + Ajna
  venue: repo
  status: done
  linear_id: SYN-33

- id: IMPL-D-0048
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "psyche|ajna route"
  intent: Prevent tasks marked FAILED when they only represent environmental/bootstrap blockers.
  deliverable: Add a distinct lifecycle status (e.g., BLOCKED) or error classification when failures are due to missing binaries/auth/ssh trust.
  dependencies: Ledger schema + task lifecycle semantics
  owner_lane: Psyche + Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0049
  source_path: 00-ORCHESTRATION/scripts/rearm_watchers.sh
  source_lines: "mini/home vs psyche/system"
  intent: Keep OpenClaw+watcher scaffolding synchronized between hosts while respecting role split.
  deliverable: Ensure rearm_watchers installs the correct plist set; add a verification step that prints the resolved ProgramArguments paths after install.
  dependencies: launchctl/plutil
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-43

- id: IMPL-D-0050
  source_path: agents/ajna/outbox/RESULT-ajna-20260205-outfitment_sync_and_smoketest.md
  source_lines: "git stash used to proceed"
  intent: Avoid hidden local state (stashes) on Ajna causing drift or future merge surprises.
  deliverable: Define policy: no long-lived stashes on always-on node; create a periodic audit script that lists stashes and requires resolution.
  dependencies: git
  owner_lane: Ajna
  venue: repo
  status: new
  linear_id: SYN-27


## 2026-02-06 — Tranche D (Tooling + integration): Watcher hardening + CANON regen observability

- id: IMPL-D-0051
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "run_executor(): openclaw agent --timeout 600; handle_file(): claim+execute pipeline"
  intent: Prevent kanban queue stalls when an executor hangs or is SIGKILLed.
  deliverable: Add a real wall-clock execution timeout wrapper (and classify as BLOCKED vs FAILED); on timeout move task to 30-BLOCKED/ (or 50_FAILED/) and emit a RESULT receipt documenting timeout.
  dependencies: macOS-compatible timeout strategy (coreutils gtimeout or python watchdog); agreed lifecycle semantics for BLOCKED.
  owner_lane: Psyche (spec) + Commander (implement)
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-D-0052
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "handle_file(): comment says TASK/SURVEY/PATCH allowed but not enforced"
  intent: Ensure inbox drop-ins and non-task files can never be executed accidentally.
  deliverable: Enforce Kind gating: parse **Kind** and only execute when Kind ∈ {TASK,SURVEY,PATCH}; otherwise move to 90-ARCHIVE/ (or ignore) and optionally emit a lightweight receipt.
  dependencies: DYN-DISPATCH_KANBAN_PROTOCOL.md (kind contract); decision on archive behavior.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0053
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "write_result_receipt(): uses date=now, slug derived from filename"
  intent: Make RESULT filenames deterministic and aligned with dispatch Expected Output.
  deliverable: Prefer parsing Expected Output path from task header when present; fall back to current slug/date logic; ensure no zsh glob errors in tooling.
  dependencies: dispatch.sh template; header parser robustness.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-D-0054
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "logs include advisory text; /tmp/*.err contains narrative"
  intent: Keep watcher logs machine-parseable (no essay leakage) to support health checks and incident review.
  deliverable: Ensure only structured [Watch] log lines are written to the launchd stderr log; route any long-form diagnostics into RESULT receipts only.
  dependencies: launchd log locations; logging policy.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-D-0055
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "append_regen_log(): currently writes CANON IDs as hardcoded '31150'"
  intent: Make CANON regeneration observability truthful and automatable.
  deliverable: Modify regenerate_canon.py to print regenerated CANON IDs (machine-parseable), and have watch_canon.sh append exact IDs to DYN-CANON_REGEN_LOG.md; also emit ledger REGEN events (per DEC-20260204-213941-ledger-event-set).
  dependencies: regenerate_canon.py output contract; append_ledger.sh usage.
  owner_lane: Psyche (spec) + Commander (implement)
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: Same fix as D-0101 — regenerate() uses --json, extracts actual IDs."

- id: IMPL-D-0056
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "build_watch_paths(): reads template_registry.json watch_paths"
  intent: Ensure canon watch daemon actually covers all relevant sources without silent gaps.
  deliverable: Add a --diagnose mode that prints resolved watch set + missing paths and exits nonzero if critical watch_paths are missing.
  dependencies: define "critical" watch_paths and expected minimum set.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-D-0057
  source_path: Makefile
  source_lines: "make update-ledgers / regenerate-canon targets"
  intent: Provide a single 'ops health' command for humans + watchers.
  deliverable: Add make target (e.g. make ops-health) that runs: watcher_health.sh, git status summary, queue_status.sh all agents, ledger tail, and canon watch diagnose.
  dependencies: watcher_health.sh (IMPL-D-0038) + canon diagnose (IMPL-D-0056).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-D-0058
  source_path: 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  source_lines: "Receipts-To + state transitions"
  intent: Close the loop between filesystem-kanban and SaaS execution surfaces (Linear/ClickUp/Slack/Discord).
  deliverable: Add an explicit 'Integration hooks' section: where notifications go, what events are emitted (DISPATCH/RESULT/FAILED/BLOCKED/REGEN/COMPACT), and which SaaS surfaces subscribe.
  dependencies: platform integration decisions (Cowork); Linear vs ClickUp role boundary.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-30

- id: IMPL-D-0059
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "append_regen_log(): hardcoded CANON IDs (echo ... | 31150 |)"
  intent: Make CANON regeneration log truthful and useful for audit.
  deliverable: Patch watch_canon.sh so regen log writes the actual CANON IDs regenerated (pulled from regenerate_canon.py output), not a hardcoded placeholder.
  dependencies: regenerate_canon.py must expose/return regenerated ids (stdout/json).
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: Same fix as D-0101/D-0055."

- id: IMPL-D-0060
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "regenerate() + append_regen_log()"
  intent: Add ledger observability for CANON regeneration events.
  deliverable: On regen SUCCESS/FAILED, append a ledger REGEN event via append_ledger.sh including trigger, status, and CANON IDs.
  dependencies: append_ledger.sh REGEN event type already present; decide payload fields.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-D-0061
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "build_watch_paths() + dry-run"
  intent: Diagnose missing watch inputs early to avoid silent non-regeneration.
  deliverable: Add watch_canon.sh --diagnose mode that (a) prints registry entries + watch_paths, (b) highlights missing files, and (c) exits nonzero if critical watch_paths missing.
  dependencies: Template registry schema; policy for critical vs optional inputs.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-D-0062
  source_path: 00-ORCHESTRATION/scripts/watch_canon.sh
  source_lines: "fswatch loop (no lock)"
  intent: Prevent concurrent/overlapping regen runs on bursty fswatch events.
  deliverable: Add a lock (mkdir lockdir) around regenerate() so only one regen can run at a time; drop/restart if another event arrives while running.
  dependencies: Lock directory convention (/tmp/syncrescendence-canon.lock).
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Completed 2026-02-09: Same fix as D-0102 — mkdir lock in regenerate()."

- id: IMPL-D-0063
  source_path: 00-ORCHESTRATION/scripts/ops_lint.sh
  source_lines: "check_frontmatter(): only checks presence of keys"
  intent: Turn ops_lint into a correctness gate, not just a presence check.
  deliverable: Extend ops_lint to validate: (a) kind is in allowed set, (b) id matches filename prefix conventions, (c) YAML parses (python -c yaml.safe_load) where available.
  dependencies: Decide allowed kind set for 02-ENGINE (PROMPT/REF/etc.).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-20

- id: IMPL-D-0064
  source_path: 00-ORCHESTRATION/scripts/ops_lint.sh
  source_lines: "currently checks each file independently"
  intent: Prevent duplicate ids across operational artifacts.
  deliverable: Add a pass that collects all frontmatter ids and fails on duplicates; output the colliding file paths.
  dependencies: None.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-20

- id: IMPL-D-0065
  source_path: 00-ORCHESTRATION/scripts/verify_all.sh
  source_lines: "Root .md files: conditional + comment mismatch"
  intent: Remove drift/mismatch in verification messages.
  deliverable: Fix verify_all.sh root .md allowance message (comment says 3 allowed; message says expected <=2) and make allowed list explicit.
  dependencies: Decide canonical allowed root markdown list.
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-32
  notes: "Completed 2026-02-09: Same fix as D-0083 — verify_all.sh now uses explicit allowlist (CLAUDE.md, README.md)."

- id: IMPL-D-0066
  source_path: 00-ORCHESTRATION/scripts/verify_all.sh
  source_lines: "set -e; ledger checks; ls/wc pipelines"
  intent: Make verification resilient and CI-friendly.
  deliverable: Harden verify_all.sh: set -euo pipefail; avoid failures when optional files are missing; standardize counts and exit codes.
  dependencies: Decide which missing artifacts are warnings vs errors.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-32

- id: IMPL-D-0067
  source_path: Makefile
  source_lines: "verify target assumes DYN-TASKS.csv + DYN-PROJECTS.csv exist"
  intent: Prevent make verify from failing on first-run repos.
  deliverable: Patch Makefile verify/update-ledgers to check file existence and print 'Not found' instead of erroring; align with verify_all.sh.
  dependencies: None.
  owner_lane: Psyche
  venue: repo
  status: done
  linear_id: SYN-32
  notes: "Completed 2026-02-10: verify + update-ledgers use if/else for CSV existence. Root .md check updated (AGENTS.md, GEMINI.md). verify_all.sh aligned."

- id: IMPL-D-0068
  source_path: Makefile
  source_lines: ".PHONY list + targets"
  intent: Provide a single ops-health entrypoint.
  deliverable: Add make ops-health that runs lint + verify-full + (future) watcher_health.sh and surfaces a summarized PASS/FAIL.
  dependencies: IMPL-D-0038 watcher_health.sh.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-45

- id: IMPL-D-0069
  source_path: Makefile
  source_lines: "canon tooling targets"
  intent: Make canon watch/regeneration accessible and standardized.
  deliverable: Add make canon-watch and canon-watch-once targets that call watch_canon.sh (and/or regenerate_canon.py) with consistent logging.
  dependencies: watch_canon.sh flags.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-D-0070
  source_path: 00-ORCHESTRATION/scripts/verify_all.sh + Makefile
  source_lines: "stdout-only; no machine-readable report"
  intent: Enable automated ops checks and dashboards.
  deliverable: Add optional JSON output mode (e.g., VERIFY_JSON=1) for verify_all.sh and wire Makefile target verify-json; useful for watcher_health aggregation.
  dependencies: Decide JSON schema + where to write.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-45

## 2026-02-08 — Tranche E (Sovereign Cockpit): Terminal lifestyle layer + activation

- id: IMPL-E-0001
  source_path: 00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md
  source_lines: "Sovereign Cockpit (8-layer stack)"
  intent: Complete cockpit activation and verify all 8 layers operational end-to-end.
  deliverable: All layers verified: Ghostty, Starship, tmux+sesh, Bun, Neovim/LazyVim, Whisper/Piper, Doom Emacs (emacs-mac), Cursor. Smoke test each layer independently.
  dependencies: None (structurally complete).
  owner_lane: Commander
  venue: tool+repo
  status: in_progress
  linear_id: SYN-42
  notes: "8 layers installed 2026-02-08. Starship replaced P10k, emacs-mac replaced emacs-plus, cockpit 1x4 layout. See CLARESCENCE-2026-02-08-cockpit-lifestyle-layer.md."

- id: IMPL-E-0002
  source_path: 00-ORCHESTRATION/scripts/cockpit.sh
  source_lines: "1x4 horizontal lane layout"
  intent: Validate cockpit.sh launches correctly and all 4 panes receive commands.
  deliverable: tmux constellation session with 4 equal-width panes, each running the correct CLI agent.
  dependencies: IMPL-E-0001
  owner_lane: Commander
  venue: tool
  status: done
  linear_id: SYN-42
  notes: "Verified 2026-02-08: 4 panes ~49 cols each, 1-based indexing."

- id: IMPL-E-0003
  source_path: 00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md
  source_lines: "Lifestyle Tools"
  intent: Install and verify lifestyle TUI tools for daily use.
  deliverable: fastfetch, chafa, ticker, circumflex (clx), mpv, yt-dlp installed and aliased.
  dependencies: None
  owner_lane: Commander
  venue: tool
  status: done
  linear_id: SYN-42
  notes: "All 6 installed via Homebrew 2026-02-08. Aliases in ~/.zshrc."

- id: IMPL-E-0004
  source_path: 00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md
  source_lines: "Prompt: Starship"
  intent: Replace Powerlevel10k with Starship for lean, cross-shell prompt.
  deliverable: Starship configured with Catppuccin Mocha palette, P10k removed from .zshrc.
  dependencies: None
  owner_lane: Commander
  venue: tool
  status: done
  linear_id: SYN-42
  notes: "Completed 2026-02-08. Config at ~/.config/starship.toml. See DEC-LIFESTYLE-001."

- id: IMPL-E-0005
  source_path: 00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md
  source_lines: "Dashboard: Doom Emacs (emacs-mac)"
  intent: Replace emacs-plus with emacs-mac (Yamamoto port) for native macOS integration.
  deliverable: emacs-mac installed, Doom rebuilt with init.29.4.el, server-start via after-init-hook.
  dependencies: None
  owner_lane: Commander
  venue: tool
  status: done
  linear_id: SYN-42
  notes: "Completed 2026-02-08. Doom rebuild required for version-stamped init files. See DEC-LIFESTYLE-002."

- id: IMPL-E-0006
  source_path: 00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-08-cockpit-lifestyle-layer.md
  source_lines: "DEC-LIFESTYLE-001 through 005"
  intent: Formal clarescence for cockpit lifestyle layer decisions.
  deliverable: Clarescence document with decision atoms, falsifiers, and reversibility paths.
  dependencies: None
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-42
  notes: "Passes 1-3 completed 2026-02-08."

- id: IMPL-E-0007
  source_path: 00-ORCHESTRATION/FLEET-COMMANDERS-HANDBOOK.md
  source_lines: "v1.1"
  intent: Update Fleet Commander's Handbook to reflect lifestyle layer changes.
  deliverable: Handbook v1.1 with 1x4 layout, Starship, emacs-mac, voice layer, lifestyle tools.
  dependencies: IMPL-E-0001 through IMPL-E-0005
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-42
  notes: "Updated 2026-02-08."

- id: IMPL-E-0008
  source_path: 00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md
  source_lines: "tmux TPM plugins"
  intent: Install tmux TPM plugins for catppuccin, resurrect, continuum.
  deliverable: Run tmux prefix+I to install plugins; verify catppuccin theme active.
  dependencies: IMPL-E-0001
  owner_lane: Sovereign (interactive)
  venue: tool
  status: new
  linear_id: SYN-40
  notes: "Requires interactive tmux prefix+I keystroke."

- id: IMPL-E-0009
  source_path: 00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md
  source_lines: "Agent Pipe"
  intent: Verify Neovim Agent Pipe sends text to correct tmux panes.
  deliverable: Open nvim, select text, <leader>ac → verify text appears in Commander pane.
  dependencies: IMPL-E-0001, IMPL-E-0002
  owner_lane: Sovereign (interactive)
  venue: tool
  status: new
  linear_id: SYN-40
  notes: "Requires interactive Neovim session."

## 2026-02-09 — Tranche F (Spine follow-ons): Toolchain alignment + Neo-Blitzkrieg + Intentions

- id: IMPL-F-0001
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "115–140 (New Terms Needed + Existing Terms to Update)"
  intent: Update Rosetta Stone so OpenClaw/Codex/Gemini operational primitives are canonically defined.
  deliverable: REF-ROSETTA_STONE.md: add terms #170–180 (Gateway/Skills/Heartbeat/Sub-agent/Node/Approval Mode/Codex Cloud/--yolo/AGENTS.md/Evidence Pack/Stateless Invocation) and update entries #14/#48/#49/#114/#122/#124 per clarescence.
  dependencies: IMPL-A-0008 (CANON-31150 platform catalog rewrite); confirm current Rosetta numbering.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-7

- id: IMPL-F-0002
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "171–172 (Mitigation: regeneration protocol)"
  intent: Prevent the platform capability catalog from going stale.
  deliverable: Implement/verify PROC::Regeneration for CANON-31150: keep platform matrix in JSON and regenerate the markdown catalog from a template; document edit policy (edit JSON, not the generated file).
  dependencies: IMPL-A-0008; existing regenerate_canon.py / templating system.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-29

- id: IMPL-F-0003
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "181–185 (Recommended Execution streams)"
  intent: Make the Toolchain Clarescence executable as a repeatable micro-cycle.
  deliverable: Add a Neo-Blitzkrieg “Toolchain Alignment” micro-cycle template (Stream A/B/C) with task stubs that dispatch to Commander/Adjudicator/Cartographer + expected receipts.
  dependencies: IMPL-A-0010 (DYN-TOOLCHAIN_INTERACTION_PROTOCOL).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-F-0004
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "86–88 (Gemini CLI API key setup on Account 2)"
  intent: Activate Cartographer lane at full strength.
  deliverable: Verify Gemini CLI on Account 2 has API key configured; add a non-interactive preflight check + a PASS/FAIL receipt artifact.
  dependencies: Sovereign provides key / account access; security posture for env vars.
  owner_lane: Sovereign + Commander
  venue: tool+repo
  status: done
  linear_id: SYN-25
  notes: "Google AI API key configured in ~/.syncrescendence/.env. Gemini CLI operational. Gemini-MCP live as MCP server. Cartographer/CIO lane active. Completed 2026-02-10."

- id: IMPL-F-0005
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "96–100 (FDIS Foundation)"
  intent: Turn FDIS from a slogan into a requirements-backed node spec.
  deliverable: FDIS v0 requirements (derived from CANON + Compass + DYN backlog) and a “Modal 1 field node” spec (hardware/software/network) with explicit acceptance checks.
  dependencies: IMPL-A-0013; hardware inventory.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-17

- id: IMPL-F-0006
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "155 (Palantir ontology mapping actionable)"
  intent: De-risk the Palantir/Foundry culmination by finding ontology impedance mismatches early.
  deliverable: A short “SN ↔ Foundry Ontology” mapping memo: primitive alignment, missing abstractions, and a prioritized mismatch list.
  dependencies: Access to current SN ontology docs + DEF variables; Foundry ontology reference materials.
  owner_lane: Cartographer (Gemini) + Psyche
  venue: repo
  status: new
  linear_id: SYN-22

- id: IMPL-F-0007
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "163–170 (MCP Server Buildout)"
  intent: Enable cross-tool coordination on the actual channels where twins operate.
  deliverable: Stand up/choose a Slack MCP server (or alternative) + minimal Linear MCP surface; commit config templates and a threat model note.
  dependencies: IMPL-A-0014 (MCP buildout plan); credentialing.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-18
  notes: "Linear MCP (33 tools) LIVE as plugin. 9 MCP servers total operational. Slack MCP deferred (free tier, low priority). Config templates in ~/.claude.json. Completed 2026-02-10."

- id: IMPL-F-0008
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "129–135 (Velocity management: session budgeting)"
  intent: Make token/cost burn visible so velocity doesn’t quietly collapse.
  deliverable: Session budgeting spec: what counts as burn, what thresholds trigger alerts, and where receipts/logs live (ledger vs dedicated DYN file).
  dependencies: Tool usage telemetry surfaces (Claude/Codex/OpenClaw/Gemini) and what’s automatable.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-19

- id: IMPL-F-0009
  source_path: 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
  source_lines: "57–60 (INT-1209 Temporal intelligence refresh pipeline)"
  intent: Ensure temporal platform intelligence doesn’t rot in-place.
  deliverable: Temporal intelligence refresh pipeline spec: cadence, artifact format, and ‘expiration warning’ frontmatter for time-sensitive model/platform docs.
  dependencies: Identify where temporal intel lives (ARCH-*, 04-SOURCES syntheses, etc.).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-F-0010
  source_path: 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
  source_lines: "123–128 (Capture: attached reports canonization; tmux; HighCommand; session discipline)"
  intent: Flush pending meta-intentions into executable tasks.
  deliverable: Triage note + concrete task definitions for INT-C002/INT-C005/INT-C006/INT-C007 (canonize reports; tmux enablement; HighCommand ontology linkage doc; parallel-session discipline SOP).
  dependencies: Identify the "attached reports" location; confirm HighCommand repo path.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-40

- id: IMPL-F-0011
  source_path: 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
  source_lines: "57–58, 123–125 (Revenue target reset)"
  intent: Resolve ambiguity about sustainability deadline so planning isn’t based on a ghost constraint.
  deliverable: DecisionAtom: INT-1201/INT-C003 revenue target reset—new deadline, leading indicators, and how it affects prioritization.
  dependencies: Sovereign ratification.
  owner_lane: Sovereign + Psyche
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-F-0012
  source_path: 00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md
  source_lines: "203–206 (Future automation)"
  intent: Close the loop between Four-Systems automation and the actual tool substrate (OpenClaw/launchd/n8n).
  deliverable: DecisionAtom addendum to IMPL-A-0023: confirm which automation substrate owns which mode (System 1 schedules, System 2 capture polling, etc.) and how portability is handled on laptops.
  dependencies: IMPL-A-0023.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-45

## 2026-02-09 — Tranche G (Spine): Rosetta + Dispatch Kanban + Intentions mechanics

- id: IMPL-G-0001
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (2) + #8 Chorus/Medley"
  intent: Fix operational terminology drift: Constellation is Medley by default; Chorus reserved for same-prompt parallel runs.
  deliverable: README.md + any ops docs: replace incorrect ‘Chorus’ usage for day-to-day operations with ‘Medley’; add a one-paragraph glossary note + ‘when to use Chorus’ examples.
  dependencies: IMPL-A-0002.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-6

- id: IMPL-G-0002
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (3) + #5 Ring→sigma"
  intent: Complete ‘Ring’→sigma rename and ratify sigma/tau split everywhere.
  deliverable: Repo-wide search/replace remaining active-doc ‘Ring’ references; add an explicit sigma/tau glossary section + migration note; ensure historical references remain intact.
  dependencies: IMPL-A-0003.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-7

- id: IMPL-G-0003
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Definition Discovery (9)"
  intent: Disambiguate ‘Five Invariants’ vs the broader constitutional rule set so ‘invariant’ actually means non-overridable.
  deliverable: CLAUDE.md: add a section that enumerates the five invariants explicitly, separates them from ‘constitutional rules’, and documents override/ratification semantics.
  dependencies: Sovereign ratification of the exact five.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-5

- id: IMPL-G-0004
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G2 Memory Crystal Protocol)"
  intent: Add a token-economic session-compaction primitive that produces durable memory without bloating context.
  deliverable: Design a ‘Memory Crystal’ spec adapted to Syncrescendence: librarian sub-agent or script that writes compressed session summary to a durable target (e.g., 05-SIGMA/MEMORY-* or 00-ORCHESTRATION/state/DYN-*) with citations and freshness markers.
  dependencies: Decide storage surface + cadence; existing compact_wisdom.sh integration.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-G-0005
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G3 Adversarial Validation)"
  intent: Institutionalize falsification before canonization to prevent hallucinated drift.
  deliverable: Add an ‘Adversarial Validation’ checklist to DecisionAtoms + a lane routing rule: when to dispatch to Oracle (Grok) / Augur (Perplexity) specifically for disproof/counterexamples.
  dependencies: Tool availability + dispatch protocol.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-22

- id: IMPL-G-0006
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G4 Temporal Versioning / Decay)"
  intent: Make time-sensitivity first-class so technical claims self-expire rather than rot.
  deliverable: Add temporal metadata schema (last_verified, expires_at, refresh_trigger) to relevant docs and/or a ‘temporal intel’ frontmatter block; implement a periodic refresh scanner that flags expired items.
  dependencies: Align with IMPL-F-0009 temporal refresh pipeline.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-46

- id: IMPL-G-0007
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "SN Format → Syncrescript (Migration Path)"
  intent: Remove naming ambiguity between ‘SN’, ‘Semantic Notation’, and ‘Syncrescript’.
  deliverable: Repo-wide migration: update active docs to prefer ‘Syncrescript’ terminology; keep tooling names (sn_*) for compatibility; add a short glossary note mapping old→new.
  dependencies: None.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-37

- id: IMPL-G-0008
  source_path: 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  source_lines: "§2–§6 (Structure + Lifecycle + Reply-To-Sender)"
  intent: Close the loop: make bidirectional feedback mandatory and machine-checkable.
  deliverable: Extend ops_lint.sh (or add kanban_lint.sh) to validate: Kind present/allowed; Kanban mirrors folder; Reply-To is present; Receipts-To points at agents/<agent>/outbox/; CONFIRM/RESULT/EXECLOG prefixes are excluded from watchers.
  dependencies: IMPL-B-0010; IMPL-D-0085.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-G-0009
  source_path: 00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "Operating Principles → Inter-Twin Communication"
  intent: Repair protocol drift: doc references `agents/outputs/inbox/` but it was deleted; twin relay surface needs a canonical path.
  deliverable: Update DYN-TWIN_COORDINATION_PROTOCOL.md to point to the current canonical twin handoff surface (e.g., agents/psyche/outbox/ARTIFACTS or a reinstated agents/outputs);/inbox add a one-line rule for discoverability + indexing.
  dependencies: Decision on shared handoff directory.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

- id: IMPL-G-0010
  source_path: .claude/skills/intentions.md
  source_lines: "PROCESS + ID Assignment + Anti-patterns (False resolution)"
  intent: Make intention triage/flush deterministic, collision-free, and evidence-backed.
  deliverable: Add (a) a cadence/SOP for triaging DYN-INTENTIONS_QUEUE.md, (b) an INT id allocation helper (script or make target), and (c) a lint rule: status=resolved requires integrated_into/evidence.
  dependencies: IMPL-B-0006/0007/0008.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-41

## 2026-02-09 — Tranche H (Tooling): Operations scripts + Makefile targets

- id: IMPL-H-0001
  source_path: 00-ORCHESTRATION/scripts/ajna_pedigree.sh
  source_lines: "1–85 (full script)"
  intent: Enrich Ajna Pedigree with DecisionAtom and Intention linking for full lineage traceability.
  deliverable: Extend ajna_pedigree.sh to read DYN-GLOBAL_LEDGER.md for DECISION events in session window, and correlate with ARCH-INTENTION_COMPASS.md entries that were resolved this session; append cross-reference section to pedigree entry.
  dependencies: DYN-GLOBAL_LEDGER.md schema (IMPL-D-0105); ARCH-INTENTION_COMPASS.md structure.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-41

- id: IMPL-H-0002
  source_path: 00-ORCHESTRATION/scripts/append_ledger.sh
  source_lines: "1–95 (full script)"
  intent: Ensure ledger append is crash-safe and supports query interface for audit trails.
  deliverable: Add (a) temp file cleanup trap verification, (b) ledger corruption detection/recovery (checksum or entry count validation), (c) query mode: `append_ledger.sh query <TASK_ID>` returns all events for task.
  dependencies: None.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-31

- id: IMPL-H-0003
  source_path: 00-ORCHESTRATION/scripts/audit_applications.sh
  source_lines: "1–350 (full script)"
  intent: Operationalize application audit so golden state is maintained automatically.
  deliverable: (a) Schedule audit_applications.sh via cron/launchd monthly, (b) store generated Brewfile and report in repo (00-ORCHESTRATION/state/DYN-BREWFILE.md and DYN-APP_AUDIT.md), (c) drift detection: compare current Brewfile against stored and alert on divergence.
  dependencies: IMPL-A-0016 (System 1 automation); launchd/cron decision.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-56

- id: IMPL-H-0004
  source_path: Makefile
  source_lines: "252–255 (sync-drive placeholder), 310–320 (ecosystem-health with potential path error)"
  intent: Complete Makefile ecosystem targets and fix path assumptions.
  deliverable: (a) Implement sync-drive target with rclone or alternative (or DecisionAtom to remove), (b) verify watchdog.sh path ($HOME/.syncrescendence/scripts/ vs 00-ORCHESTRATION/scripts/), (c) add missing target help-text for model-db, model-query, search.
  dependencies: Verify actual script locations; rclone availability.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-32

## 2026-02-10 — Follow-up Tranche: CANON-31150 regeneration + Tech Stack DB migration + Lint protocol

- id: IMPL-I-0001
  source_path: 01-CANON/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md
  source_lines: "35–40 (TEMPORAL DATA NOTICE)"
  intent: Operationalize the canon regeneration protocol so capability updates are reproducible.
  deliverable: Document or script the three-step regeneration workflow (edit platform_capabilities.json → run regenerate_canon.py 31150 → commit). Verify this works e2e with a test edit.
  dependencies: Python env with regenerate_canon.py; write access to 01-CANON/.
  owner_lane: Ajna
  venue: repo
  status: done
  linear_id: SYN-29
  notes: "Canon regeneration workflow operational: edit platform_capabilities.json → run regenerate_canon.py 31150 → commit. Verified e2e with CANON-31150 v4.0 regeneration (enterprise roles + model updates). Completed 2026-02-10."

- id: IMPL-I-0002
  source_path: 01-CANON/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md
  source_lines: "75–85 (Migration protocol mention)"
  intent: Execute the Tech Stack DB migration from CSV sources to canonical backend.
  deliverable: (a) Choose backend (SQLite/PostgreSQL/JSON), (b) locate and verify CSVs (Function.csv, Models.csv, API.csv), (c) run migration with integrity checks, (d) write receipt to DYN-CORPUS_HEALTH.md or impl receipt.
  dependencies: IMPL-C-0012; CSV location confirmation; backend decision in CANON-30310.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-22

- id: IMPL-I-0003
  source_path: 00-ORCHESTRATION/scripts/corpus_health_check.py
  source_lines: "1–150 (full script scan)"
  intent: Ensure corpus health checks run on schedule and alert on drift.
  deliverable: (a) Add launchd/cron entry for daily corpus_health_check.py, (b) output to DYN-CORPUS_HEALTH.md with timestamp, (c) alert threshold if >N broken links or schema violations.
  dependencies: launchd vs cron decision; alert routing (Slapshot? Slack DM?).
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-31

- id: IMPL-I-0004
  source_path: DYN-DISPATCH_KANBAN_PROTOCOL.md + DYN-TWIN_COORDINATION_PROTOCOL.md
  source_lines: "cross-doc drift detection"
  intent: Close IMPL-G-0009 by making twin handoff surface discoverable and indexed.
  deliverable: (a) Update DYN-TWIN_COORDINATION_PROTOCOL.md to replace agents/outputs/inbox/ with canonical agents/<agent>/outbox/ARTIFACTS/ path, (b) add INDEX.md entry in agents/ pointing to latest twin relay files, (c) close IMPL-G-0009 as completed./outbox
  dependencies: IMPL-G-0009 status update; folder creation (if agents/ structure not present)./outbox
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-14

## 2026-02-10 — Tranche J (Canon Hotspots Follow-up): Five-Account + Multi-Agent + Memory + Seven-Layer

- id: IMPL-J-0001
  source_path: 01-CANON/CANON-31141-FIVE_ACCOUNT
  source_lines: "Part II–V (Acumen IIC operational architecture)"
  intent: Operationalize Acumen IIC with account-specific platform grammars and automation.
  deliverable: (a) Document feed polling cadence (daily/weekly), (b) define Red Alert threshold and routing, (c) create quick-priority classification (read/queue/delegate), (d) prototype daily_brief.py generator.
  dependencies: IMPL-C-0001; Acumen IIC account access.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-49

- id: IMPL-J-0002
  source_path: 01-CANON/CANON-31141-FIVE_ACCOUNT
  source_lines: "Part III (Coherence IIC multi-stage refinement pipeline)"
  intent: Operationalize Coherence IIC synthesis pipeline with weekly handoff automation.
  deliverable: (a) Weekly Acumen→Coherence handoff SOP, (b) framework refinement template, (c) synthesis essay template with citation network, (d) prototype coherence_synthesizer.py.
  dependencies: IMPL-J-0001 (Acumen pipeline first).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-49

- id: IMPL-J-0003
  source_path: 01-CANON/CANON-31141-FIVE_ACCOUNT
  source_lines: "Part IV (Efficacy IIC execution cadence)"
  intent: Operationalize Efficacy IIC with task prioritization and velocity tracking.
  deliverable: (a) Daily task triage SOP (high/medium/low), (b) calendar integration rules, (c) weekly velocity review template, (d) LogSeq/Obsidian pattern for task flow.
  dependencies: Calendar API access decision.
  owner_lane: Ajna
  venue: repo
  status: new
  linear_id: SYN-49

- id: IMPL-J-0004
  source_path: 01-CANON/CANON-31141-FIVE_ACCOUNT
  source_lines: "Part V (Mastery IIC curriculum and syllabus tracking)"
  intent: Operationalize Mastery IIC for learning project tracking and spaced repetition.
  deliverable: (a) Curriculum YAML schema (topic/stage/resources), (b) syllabus progress tracker, (c) spaced repetition integration (Anki API or similar), (d) learning artifact storage pattern.
  dependencies: Spaced repetition tool selection.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-24

- id: IMPL-J-0005
  source_path: 01-CANON/CANON-31141-FIVE_ACCOUNT
  source_lines: "Part VI (Transcendence IIC journaling and reflection)"
  intent: Operationalize Transcendence IIC with reflection prompts and meaning-making capture.
  deliverable: (a) Daily reflection prompt generator, (b) weekly meaning synthesis template, (c) values alignment check (quarterly), (d) integration with existing journaling practice.
  dependencies: Journaling platform selection (Bear/Apple Notes/Obsidian).
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-48

- id: IMPL-J-0006
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION
  source_lines: "§2.3 (planner-executor, critic-refiner, specialist swarm topologies)"
  intent: Implement canonical multi-agent topologies as runner scripts with handoff protocols.
  deliverable: (a) planner_executor.py: two-layer planning → execution with task decomposition, (b) critic_refiner.py: collaborative feedback loop with quality threshold, (c) specialist_swarm.py: parallel specialists with aggregation synthesis.
  dependencies: Agent spawning mechanism (OpenClaw sessions_spawn or equivalent).
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-35

- id: IMPL-J-0007
  source_path: 01-CANON/CANON-30420-MULTI_AGENT_ORCHESTRATION
  source_lines: "§3.5–3.6 (MCP, A2A protocols; progressive trust model)"
  intent: Evaluate and prototype protocol surfaces for multi-agent communication.
  deliverable: (a) DecisionAtom: MCP vs A2A vs filesystem-kanban tradeoff for Syncrescendence, (b) prototype MCP server exposing repo operations, (c) progressive trust ladder specification (allowed actions per trust tier).
  dependencies: IMPL-C-0005 (progressive trust); MCP research.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-18

- id: IMPL-J-0008
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS
  source_lines: "§1.1 (memory taxonomy: working/episodic/semantic/procedural/prospective)"
  intent: Map canonical memory taxonomy to concrete repo artifacts and storage.
  deliverable: (a) Document where each memory type lives: working→CONTEXT.md, episodic→DYN-SESSION_LOG.md, semantic→MEMORY.md / canon, procedural→SKILL.md / PROCESSES/, prospective→DYN-INTENTIONS_QUEUE.md.
  dependencies: Existing artifact structure; minimal reorganization.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-J-0009
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS
  source_lines: "§2.2–2.4 (A-MEM, MIRIX, MemGPT system overviews)"
  intent: Evaluate memory system implementations for local deployment.
  deliverable: (a) A-MEM integration assessment (vector store for transcripts), (b) MIRIX evaluation (if applicable to local setup), (c) MemGPT comparison, (d) DecisionAtom with recommendation.
  dependencies: Local compute resources; vector DB selection.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-J-0010
  source_path: 01-CANON/CANON-30430-MEMORY_SYSTEMS
  source_lines: "§3 (context engineering: chunking, relevance, decay, summarization)"
  intent: Implement context compression and memory maintenance automation.
  deliverable: (a) Session compaction policy (when/how to summarize), (b) relevance scoring for memory retrieval, (c) decay rules for ephemeral vs persistent memory, (d) sleep-time compute jobs for maintenance.
  dependencies: IMPL-C-0008 (cron/launchd jobs for memory maintenance).
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-J-0011
  source_path: 01-CANON/CANON-31130-SEVEN_LAYER
  source_lines: "Part I.C (sovereignty challenges per layer)"
  intent: Document sovereignty-preserving configurations for each of the seven layers.
  deliverable: (a) Layer 0 (Physical): device selection + local-first hardening guide, (b) Layer 1 (Identity): account separation strategy, (c) Layer 2 (Ambient): Siri/Google Assistant opt-outs, (d) Layer 3 (Browser): Brave/Firefox config with extension audit, (e) Layer 4 (AI): platform data retention review, (f) Layer 5 (Content): feed curation independence, (g) Layer 6 (Production): self-hosted vs cloud tool audit, (h) Layer 7 (Meta): human-judgment preserved decisions.
  dependencies: Privacy/data export APIs for major platforms.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-48

- id: IMPL-J-0012
  source_path: 01-CANON/CANON-31130-SEVEN_LAYER
  source_lines: "Part II (differential sovereignty patterns)"
  intent: Operationalize differential sovereignty: fine-grained control delegation per context.
  deliverable: (a) Decision matrix: when to use human judgment vs agent automation vs platform native, (b) sensitive operations registry (never-automate list), (c) sovereignty preservation checklist for new tool adoption.
  dependencies: IMPL-J-0011 layer analysis.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-48


## 2026-02-10 — Tranche K (New Material): SaaS Integrations + Memory Audit + Sensing Templates

- id: IMPL-K-0001
  source_path: 02-ENGINE/REF-AIRTABLE_INTEGRATION.md
  source_lines: "I–II (account structure, base schema)"
  intent: Operationalize Airtable ontology surface with bidirectional sync to ontology.db.
  deliverable: (a) airtable_sync.py: bidirectional sync (ontology.db ↔ Airtable), (b) handle 5 req/s rate limit with backoff, (c) PAT token management in ~/.syncrescendence/.env, (d) field mapping verification.
  dependencies: ontology.db schema stability; Airtable API access.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-55

- id: IMPL-K-0002
  source_path: 02-ENGINE/REF-AIRTABLE_INTEGRATION.md
  source_lines: "II–III (tables: Platforms, Models, etc.)"
  intent: Seed Airtable tables with existing ontology data.
  deliverable: (a) Migration script: seed Platforms table (126 records), Models (20 records), (b) validate Slug/ASA Layer/Lifecycle fields, (c) handle singleSelect field constraints, (d) write sync receipt.
  dependencies: IMPL-K-0001.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-55

- id: IMPL-K-0003
  source_path: 02-ENGINE/REF-JIRA_INTEGRATION.md
  source_lines: "I (API details, deprecated /search endpoint)"
  intent: Fix Jira integration for deprecated REST API endpoints.
  deliverable: (a) Update all Jira API calls from /rest/api/3/search → /rest/api/3/search/jql, (b) verify Basic Auth still works with new endpoint, (c) add endpoint deprecation detection, (d) create Jira MCP server if valuable.
  dependencies: Jira project SCRUM exists; ~/.syncrescendence/.env with ATLASSIAN_API_KEY.
  owner_lane: Commander
  venue: repo
  status: in_progress
  linear_id: SYN-51

- id: IMPL-K-0004
  source_path: 02-ENGINE/REF-TODOIST_INTEGRATION.md
  source_lines: "I–II (API v1, Bearer auth)"
  intent: Operationalize Todoist v1 API integration (v2 deprecated).
  deliverable: (a) todoist_sync.py using /api/v1/ endpoints, (b) TODOIST_API_KEY from ~/.syncrescendence/.env, (c) handle free tier limits (8 projects, 5 active tasks), (d) migrate from v2→v1.
  dependencies: Todoist account access; API key.
  owner_lane: Ajna
  venue: repo
  status: in_progress
  linear_id: SYN-53

- id: IMPL-K-0005
  source_path: 02-ENGINE/REF-TODOIST_INTEGRATION.md
  source_lines: "I (Five-Tier Architecture, GTD → ClickUp feeding)"
  intent: Build Todoist ↔ ClickUp bidirectional bridge for GTD methodology.
  deliverable: (a) gtd_bridge.py: sync Todoist @Computer/@Phone/@Errands to ClickUp context-based projects, (b) Todoist Inbox → Linear (if actionable), (c) weekly review automation, (d) preserve WIP project segregation.
  dependencies: ClickUp API access; Todoist project structure documented.
  owner_lane: Ajna
  venue: repo
  status: new
  linear_id: SYN-53

- id: IMPL-K-0006
  source_path: 02-ENGINE/REF-WEB_APP_MEMORY_AUDIT.md
  source_lines: "Executive Summary + Platform Comparison Matrix"
  intent: Implement memory portability verification/audit script.
  deliverable: (a) memory_portability_audit.py: assess each platform's exportability, (b) lock-in risk scoring, (c) generate migration recommendations for HIGH lock-in platforms, (d) integrate with DYN-CORPUS_HEALTH.md.
  dependencies: Platform API access where available.
  owner_lane: Commander
  venue: repo
  status: done
  linear_id: SYN-38

- id: IMPL-K-0007
  source_path: 02-ENGINE/REF-WEB_APP_MEMORY_AUDIT.md
  source_lines: "Detailed Assessments (Claude, ChatGPT, Gemini, etc.)"
  intent: Operationalize memory export automation for all high-value platforms.
  deliverable: (a) Claude Memory Tool API wrapper, (b) ChatGPT data export automation (no API → manual), (c) Gemini export validation, (d) Notion MCP memory ops, (e) Mem0/Graphiti/QMD status verification.
  dependencies: API keys per platform; export endpoints.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-K-0008
  source_path: 00-ORCHESTRATION/state/impl/sensing/TEMPLATE-frontier-scan.md
  source_lines: "full template"
  intent: Operationalize frontier scanning for paradigm shifts in AI/tech.
  deliverable: (a) frontier_scan.py: poll sources (Reddit, arXiv, X), (b) Red Alert classification threshold, (c) output to DYN-CORPUS_HEALTH.md, (d) Acumen IIC integration.
  dependencies: Source APIs; IMPL-J-0001.
  owner_lane: Psyche
  venue: repo
  status: new
  linear_id: SYN-31

- id: IMPL-K-0009
  source_path: 00-ORCHESTRATION/state/impl/sensing/TEMPLATE-corpus-staleness.md
  source_lines: "full template"
  intent: Auto-detect stale corpus files and trigger refresh workflows.
  deliverable: (a) staleness_detector.py: check last-modified timestamps, (b) threshold: >30 days triggers refresh, (c) queue refresh tasks to DYN-INTENTIONS_QUEUE.md, (d) stale file registry.
  dependencies: git timestamps; file metadata.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-31

- id: IMPL-K-0010
  source_path: 00-ORCHESTRATION/state/impl/sensing/TEMPLATE-linear-impl-sync.md
  source_lines: "full template"
  intent: Implement Linear ↔ IMPLEMENTATION-MAP bidirectional sync.
  deliverable: (a) linear_sync.py: sync nextUp items to Linear, (b) pull Linear status back to IMPLEMENTATION-MAP, (c) deduplication logic, (d) webhook for real-time sync.
  dependencies: Linear API key; project mapping.
  owner_lane: Ajna
  venue: repo
  status: new
  linear_id: SYN-30

- id: IMPL-K-0011
  source_path: 00-ORCHESTRATION/state/impl/sensing/TEMPLATE-ecosystem-health.md
  source_lines: "full template"
  intent: Comprehensive SaaS/API ecosystem health monitoring.
  deliverable: (a) ecosystem_health.py: check all API endpoints (Airtable, Jira, Todoist, Linear, etc.), (b) rate limit status, (c) auth health, (d) daily report to DYN-ECOSYSTEM_HEALTH.md.
  dependencies: All API keys; endpoint list.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-31


## 2026-02-10 — Tranche L (Operational Recalibration): Atomicity + Wiring + SYN-16

- id: IMPL-L-0001
  source_path: impl/clarescence/CLARESCENCE-2026-02-10-operational-recalibration.md
  source_lines: "Pass 2 atomicity failures; Immediate Action 1"
  intent: Restore REF-WEB_APP_MEMORY_AUDIT.md destructively deleted by Ajna sync.
  deliverable: (a) git checkout REF-WEB_APP_MEMORY_AUDIT.md from prior commit, (b) verify restoration, (c) add .gitattributes protection if needed, (d) document Ajna sync hazard.
  dependencies: git reflog access; prior commit hash.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-38

- id: IMPL-L-0002
  source_path: impl/clarescence/CLARESCENCE-2026-02-10-operational-recalibration.md
  source_lines: "Immediate Action 2"
  intent: Clear 9 uncommitted hook-generated DYN-* files violating Receipts invariant.
  deliverable: (a) Review each DYN-* file for value, (b) commit or discard, (c) update pre_compaction hook to auto-commit DYN-* files, (d) add DYN-* to .gitattributes or global .gitignore.
  dependencies: None.
  owner_lane: Commander
  venue: repo
  status: new
  linear_id: SYN-15

- id: IMPL-L-0003
  source_path: impl/clarescence/CLARESCENCE-2026-02-10-operational-recalibration.md
  source_lines: "Immediate Action 4; INT-1612 activation"
  intent: Wire SYN-31 sensing templates into claudecron Phase 2 pipeline.
  deliverable: (a) Create claudecron.job for sensing templates (frontier-scan, corpus-staleness, ecosystem-health), (b) configure launchd dispatch timing, (c) test end-to-end execution, (d) verify output to appropriate DYN-* files.
  dependencies: SYN-31 templates exist; claudecron available.
  owner_lane: Commander
  venue: repo
  status: in_progress
  linear_id: SYN-31

- id: IMPL-L-0004
  source_path: impl/clarescence/CLARESCENCE-2026-02-10-operational-recalibration.md
  source_lines: "Immediate Action 5; T1a↔T2 bridge at 14.2%"
  intent: Advance SYN-16 — T1a (Linear) ↔ T2 (Implementation Map) bridge work.
  deliverable: (a) Linear project mapping schema, (b) bidirectional sync logic, (c) test with 5 sample issues, (d) target: 14.2% → 25%+ completion.
  dependencies: IMPL-K-0010 (Linear↔IMPL sync).
  owner_lane: Ajna
  venue: repo
  status: done
  linear_id: SYN-16
  notes: "DONE 2026-02-11: SYN-16 complete — T1a↔T2 bridge at 100% (197/197 entries linked). Exceeded target of 25%."

- id: IMPL-L-0005
  source_path: impl/clarescence/CLARESCENCE-2026-02-10-operational-recalibration.md
  source_lines: "Pass 2: Agent compat PARTIAL"
  intent: Add Ajna sync coordination guard to prevent destructive deletions.
  deliverable: (a) Pre-sync checklist script (verify local changes), (b) conflict detection (warn on divergent HEAD), (c) --dry-run option for Ajna sync, (d) documentation: "Sync Protocol v2".
  dependencies: Git hook framework.
  owner_lane: Ajna
  venue: repo
  status: new
  linear_id: SYN-27


## 2026-02-10 — Tranche M (New Material): MCP Decisions + Sensing Launchd

- id: IMPL-M-0001
  source_path: -SOVEREIGN/DECISION-BATCH-MCP-ONBOARDING.md
  source_lines: "Decision 1"
  intent: Await Sovereign approval for Jira MCP server installation.
  deliverable: (a) Sovereign decision: APPROVED/DENIED/DEFERRED, (b) if APPROVED: convert Jira board to Scrum type in UI, (c) add MCP config to ~/.claude.json, (d) test: create a Jira ticket from Commander.
  dependencies: Jira board access; Sovereign decision.
  owner_lane: Commander
  venue: Linear
  status: new
  linear_id: SYN-51

- id: IMPL-M-0002
  source_path: -SOVEREIGN/DECISION-BATCH-MCP-ONBOARDING.md
  source_lines: "Decision 2"
  intent: Await Sovereign approval for Todoist MCP + frozen project decision.
  deliverable: (a) Sovereign decision: APPROVED/DENIED/DEFERRED, (b) if APPROVED: choose Option A/B/C for frozen projects, (c) add MCP config to ~/.claude.json, (d) test: create/move/complete a Todoist task from Commander.
  dependencies: Todoist API key; Sovereign decision.
  owner_lane: Commander
  venue: Linear
  status: new
  linear_id: SYN-53

- id: IMPL-M-0003
  source_path: -SOVEREIGN/DECISION-BATCH-MCP-ONBOARDING.md
  source_lines: "Decision 3"
  intent: Await Sovereign approval for Airtable MCP server installation.
  deliverable: (a) Sovereign decision: APPROVED/DENIED/DEFERRED, (b) if APPROVED: add MCP config to ~/.claude.json, (c) test: query/edit Airtable Platforms table from Commander.
  dependencies: Airtable PAT; Sovereign decision.
  owner_lane: Commander
  venue: Linear
  status: new
  linear_id: SYN-55

- id: IMPL-M-0004
  source_path: -SOVEREIGN/DECISION-BATCH-MCP-ONBOARDING.md
  source_lines: "Decision 4"
  intent: Await Sovereign decision on Todoist weekly review cadence.
  deliverable: (a) Sovereign decision: Option A (auto) / B (manual) / C (hybrid), (b) if A or C: add claudecron job, (c) implement weekly review template.
  dependencies: Todoist MCP status; Sovereign decision.
  owner_lane: Commander
  venue: Linear
  status: new
  linear_id: SYN-53

- id: IMPL-M-0010
  source_path: 00-ORCHESTRATION/scripts/launchd/*sensing*.plist
  source_lines: "All 3 plist files"
  intent: Complete IMPL-L-0003 by activating sensing launchd agents.
  deliverable: (a) Move plist files from untracked to committed state, (b) load agents: launchctl load, (c) verify jobs run at scheduled times, (d) check logs in /tmp/syncrescendence-claude/.
  dependencies: Plist files created; paths validated.
  owner_lane: Ajna
  venue: repo
  status: in_progress
  linear_id: SYN-31


## 2026-02-10 — Tranche N (Execution): Jira Sync Map + Launchd Commit

- id: IMPL-N-0001
  source_path: 02-ENGINE/REF-JIRA_SYNC_MAP.md
  source_lines: "full file"
  intent: Operationalize bidirectional Jira↔Linear sync using documented mapping.
  deliverable: (a) Implement jira_linear_sync.py using status/ID mapping, (b) confirm Epic↔Project, Story↔Issue mapping, (c) handle Sprint → manual Cycle, (d) sync status transitions bidirectionally.
  dependencies: IMPL-M-0001 (Jira MCP approval) or direct API; Linear API access.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-N-0002
  source_path: 02-ENGINE/REF-JIRA_SYNC_MAP.md
  source_lines: "§Status Mapping, §Sprint Map"
  intent: Automate status sync using documented transition IDs.
  deliverable: (a) Jira webhook → Linear state update, (b) Linear state change → Jira transition, (c) handle edge cases (In Review → Linear In Progress).
  dependencies: Webhook infrastructure; both APIs.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-N-0010
  source_path: 00-ORCHESTRATION/scripts/launchd/*.plist
  source_lines: "All 12 plist files"
  intent: Complete M-0010 by committing and activating all launchd agents.
  deliverable: (a) Add plists to git (00-ORCHESTRATION/scripts/launchd/), (b) launchctl load for sensing jobs, (c) verify with launchctl list | grep syncrescendence, (d) check /tmp logs after first runs.
  dependencies: Plists written; paths validated.
  owner_lane: Ajna
  venue: repo
  status: in_progress

