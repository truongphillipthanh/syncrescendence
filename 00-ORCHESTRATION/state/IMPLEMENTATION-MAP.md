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
  status: new

- id: IMPL-A-0002
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (2) + §8 Chorus/Medley"
  intent: Correct Chorus vs Medley terminology across ops docs.
  deliverable: COCKPIT.md update: Constellation operates in Medley mode; reserve Chorus for same-prompt parallel.
  dependencies: Identify all ‘Chorus’ references; adjust definitions.
  owner_lane: Psyche (spec) + Commander (edit)
  venue: repo
  status: new

- id: IMPL-A-0003
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Critical Fixes (3) + §5 Ring→sigma"
  intent: Finish Ring→sigma rename and ratify sigma/tau split.
  deliverable: Search+replace remaining ‘Ring’ refs in active docs; add explicit sigma/tau glossary + governance note.
  dependencies: Identify protected/historical files to avoid rewriting.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0004
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G1)"
  intent: Implement self-healing constitution pattern.
  deliverable: PostToolUse hook that detects failures/anti-patterns and proposes (or appends) CLAUDE.md updates under a governed section.
  dependencies: Hook framework; policy for auto-append vs PR.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0005
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G5)"
  intent: Adopt git worktree isolation as canonical parallelization mechanism.
  deliverable: Document + script for worktree creation per lane; integrate into Neo‑Blitzkrieg execution guidance.
  dependencies: Existing scripts; team conventions.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0006
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Community Patterns: Gap Analysis (G8)"
  intent: Enable token-efficient subagent delegation via skills.
  deliverable: Add `context: fork` (or equivalent) in skill specs + guidance on when to fork.
  dependencies: Skill system conventions.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0007
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Ralph Pattern (17) — ‘verify formal implementation’"
  intent: Ensure Ralph Pattern is actually implemented and discoverable.
  deliverable: Add a canonical ‘Ralph Pattern’ doc pointing to the exact scripts/hooks and example usage; add verification checklist.
  dependencies: Locate current implementation artifacts.
  owner_lane: Psyche (locate/spec) + Commander (implement)
  venue: repo
  status: new

- id: IMPL-A-0008
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "Pass 3 + ‘Required CANON-31150 Update’"
  intent: Bring CANON-31150 Platform Capability Catalog up to reality.
  deliverable: Rewrite CANON-31150 from 3 conflated entries → 7 distinct platform entries (separate CLI vs web; add OpenClaw, Codex; add Grok/Perplexity as separate external services).
  dependencies: COCKPIT.md role truth; Rosetta naming.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0009
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "Pass 7 ‘What This Creates’"
  intent: Fill missing avatar specs for execution substrate.
  deliverable: Create/populate AVATAR-OPENCLAW (Ajna/Psyche) and AVATAR-COMMANDER (Claude Code) per agreed schema.
  dependencies: Avatar template; COCKPIT mapping.
  owner_lane: Psyche + Commander
  venue: repo
  status: new

- id: IMPL-A-0010
  source_path: 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
  source_lines: "Pass 7 ‘What This Creates’ + Pass 10 Interaction Protocol"
  intent: Formalize the actual tool interaction/dispatch protocol.
  deliverable: DYN-TOOLCHAIN_INTERACTION_PROTOCOL.md capturing dispatch modes, return channels, and minimal file-based handoff conventions.
  dependencies: Existing dispatch scripts; twin protocol.
  owner_lane: Ajna (OpenClaw) + Commander
  venue: repo
  status: new

- id: IMPL-A-0011
  source_path: 02-ENGINE/REF-ROSETTA_STONE.md
  source_lines: "Immediate Actions → Architecture Adoptions (6)"
  intent: Hooks-based automation for deterministic failure handling.
  deliverable: Define + implement standard hook set (PreToolUse/PostToolUse/Stop/PreCompact) for common failure modes + receipts.
  dependencies: Hook support in primary executor tool.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0012
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "Phase 3: Backlog Reconciliation"
  intent: Make Linear the source of truth for tasks while keeping repo snapshot.
  deliverable: Design Linear workspace structure + spec sync: Linear ↔ DYN-BACKLOG.md + session-scoped todos.
  dependencies: Linear API/MCP decision.
  owner_lane: Psyche (design) + Commander (implementation)
  venue: linear+repo
  status: in_progress
  linear_id: SYN-16
  notes: "Linear workspace populated 2026-02-05: 13 projects, 26 issues, 17 labels. GraphQL API direct access. Sync mechanism pending."

- id: IMPL-A-0013
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "Phase 2: FDIS Foundation (#7-#9)"
  intent: Triangulate FDIS requirements and deployment surface.
  deliverable: FDIS requirements doc + minimal deployable node spec (hardware/software/network), with dependency mapping to CANON + Intent Compass.
  dependencies: Canon cross-reference; hardware inventory.
  owner_lane: Psyche
  venue: repo
  status: new

- id: IMPL-A-0014
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "MCP Server Buildout"
  intent: Enable cross-tool data sharing via MCP servers.
  deliverable: Prioritized MCP rollout plan + initial Slack + Linear servers (or alternatives), with config templates committed.
  dependencies: Credentialing + security posture.
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-A-0015
  source_path: 00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md
  source_lines: "Phase 4: Velocity Management"
  intent: Manage token/cost burn and lane routing.
  deliverable: Routing matrix + budget alerts (50%/70%/85%) and default model downshift rules.
  dependencies: Usage telemetry surface.
  owner_lane: Ajna + Psyche
  venue: repo
  status: new

## 2026-02-06 — Tranche D (Tooling): Always-on watchers (launchd) hardening + smoke validation

- id: IMPL-D-0034
  source_path: 00-ORCHESTRATION/scripts/rearm_watchers.sh
  source_lines: "mode selection + plist source dir"
  intent: Make launchd watcher installs deterministic across machines/users.
  deliverable: Maintain explicit plist sets per host persona (mini/home vs psyche/system) and ensure rearm_watchers.sh selects correctly.
  dependencies: 00-ORCHESTRATION/scripts/launchd-mini/*, 00-ORCHESTRATION/scripts/launchd-psyche/*
  owner_lane: Psyche
  venue: repo
  status: mapped

- id: IMPL-D-0035
  source_path: 00-ORCHESTRATION/scripts/launchd-mini/com.syncrescendence.watch-*.plist
  source_lines: "ProgramArguments + WorkingDirectory"
  intent: Hardcode Mac mini home base paths to user `home` (per Sovereign).
  deliverable: Keep mini plists pinned to /Users/home/Desktop/syncrescendence and keep them the canonical install source for --mini.
  dependencies: None
  owner_lane: Psyche
  venue: repo
  status: mapped

- id: IMPL-D-0036
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "process_task case routing"
  intent: Guarantee that every executed task produces a durable receipt artifact.
  deliverable: Capture executor stdout/stderr into -OUTGOING/RESULT-<agent>-<date>-<topic>.md (or a deterministic name derived from the task filename) automatically; link it in task header and ledger.
  dependencies: dispatch.sh naming conventions; -OUTGOING/ directory structure; ledger event schema
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-D-0037
  source_path: -OUTGOING/RESULT-commander-20260205-always_on_watchers_sweep.md
  source_lines: "Remediation Plan (Blockers 1-3)"
  intent: Restore always-on readiness for Ajna + Adjudicator + Commander on the Mac mini.
  deliverable: (1) Install OpenClaw on mini (openclaw binary + gateway), (2) configure Codex auth (codex login or API key), (3) resolve Claude billing/plan path for Commander.
  dependencies: Access to mini; provider credentials/billing
  owner_lane: Sovereign + Commander
  venue: tool
  status: queued

- id: IMPL-D-0038
  source_path: 00-ORCHESTRATION/scripts/rearm_watchers.sh
  source_lines: "bootout/bootstrap/kickstart"
  intent: Make watcher state auditable and self-checked.
  deliverable: Add a companion script (e.g., watcher_health.sh) that prints: launchctl state, PATH/env, binary resolution, last 50 log lines, and recent task failures per agent.
  dependencies: launchctl; /tmp log paths; ledger
  owner_lane: Adjudicator (Codex) + Commander
  venue: repo
  status: new

- id: IMPL-D-0039
  source_path: 00-ORCHESTRATION/scripts/dispatch.sh
  source_lines: "Expected Output section"
  intent: Align task contract with actual watcher behavior.
  deliverable: Either (A) implement RESULT writing in watchers (preferred), or (B) change task templates to state that receipts live in /tmp logs + ledger.
  dependencies: Decision on receipt truth surface
  owner_lane: Psyche + Commander
  venue: repo
  status: new

- id: IMPL-D-0040
  source_path: 00-ORCHESTRATION/scripts/launchd-*/com.syncrescendence.watch-*.plist
  source_lines: "EnvironmentVariables"
  intent: Reduce noise and drift in daemonized environments.
  deliverable: Standardize NODE_OPTIONS=--no-warnings and NODE_NO_WARNINGS=1 across all watcher plists (mini + psyche), and ensure installed copies match repo source.
  dependencies: None
  owner_lane: Commander
  venue: repo
  status: new

- id: IMPL-D-0041
  source_path: 00-ORCHESTRATION/scripts/watch_dispatch.sh
  source_lines: "Auth tests implied by executor calls"
  intent: Prevent "watcher running but executor unusable" states from masquerading as healthy.
  deliverable: Add optional startup self-test mode per agent (verify command -v + minimal PONG) and emit FAILED_PRECHECK to ledger if missing.
  dependencies: Safe non-interactive auth checks for each CLI
  owner_lane: Commander
  venue: repo
  status: new

