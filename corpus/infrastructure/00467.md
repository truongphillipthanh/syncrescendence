# CLARESCE-DIGEST-B: Feb 8 Deep Sessions + Feb 9 Early Execution
## Files: 5 | Lines: 1,760 | Date range: 2026-02-08 to 2026-02-09

---

## KEY DECISIONS (named decision atoms, architectural choices)

- **DEC-PSYCHE-001 (Field Kit, Not Mirror)**: MBA runs Layers 1-3 + lean Layer 5 only. Mac mini is always-on HQ; MBA is mobile thinking surface + remote dispatch terminal. Excludes voice, Doom Emacs dashboard, Cursor, full 4-pane cockpit.
- **DEC-PSYCHE-002 (Tailscale as Bridge)**: Tailscale SSH is the sole inter-machine transport. MagicDNS hostnames, zero-config auth, encrypted tunnel. Resolves cross-machine race condition concern from DEC-COCKPIT-006.
- **DEC-PSYCHE-003 (chezmoi for Dotfiles)**: Machine-specific templates (`machine = "hq" | "field"`) manage shared-but-differentiated configs. Bare git repo rejected (merge hell); manual copy rejected (drift guaranteed).
- **DEC-PSYCHE-004-005 (Separate Keys / Brewfile Subset)**: MBA gets own SSH keypair; ~40 formulae vs HQ's ~288. Tailscale handles inter-machine auth without shared keys.
- **DEC-PSYCHE-006 (No Local Constellation on MBA)**: MBA runs Claude Code locally, dispatches to mini constellation via Tailscale. M4 capable but always-on mac mini is correct host for always-on constellation.
- **DEC-PSYCHE-007 (OpenClaw Twins via Slack + Filesystem + Git)**: Ajna (mini) and Psyche (MBA) coordinate through three channels — no direct network IPC. Tailscale provides missing filesystem transport for -INBOX/outputs/.
- **DEC-PSYCHE-008 (Identical AeroSpace + Karabiner on Both)**: Muscle memory is non-negotiable. Window management and Hyper Key configs are identical across machines.
- **DEC-SOV-006 (launchd over cron)**: cron killed by power management on laptops. launchd is macOS-native with WatchPaths/KeepAlive/ProcessType.
- **DEC-SOV-008 (Protoss-primary Architecture)**: Specialized agents over generic swarms. Yegge's Gas Town = Zerg; Syncrescendence = Protoss with Zerg dispatch capability available for throughput situations.
- **DEC-SOV-009 (Self-Improvement as Standing Order)**: Commander REQUIRED to actively expand capabilities — not permission, obligation. Sovereign quote: "allowed, nay, required to self-improve." Constitutional, irreversible.
- **DEC-SOV-010 (MBA = Field Operations)**: MBA increasingly primary for intellectual work (no AC, uncomfortable chair, interruptions at HQ). Cascade must be differential, not identical.
- **DEC-SOV-011 (Narrative DNA as Design Vocabulary)**: StarCraft/Dune/Halo/anime provide design patterns, not decoration. Inscribed to persistent memory. Irreversible identity decision.
- **DEC-S6-001 (Qdrant MCP Priority over ClickUp)**: Memory search is foundational; diagnose before adding more MCPs. Fallback: Graphiti provides alternative graph-based memory if Qdrant unfixable.
- **DEC-S6-002 (claudecron Strategy)**: No official claudecron → build launchd-based scheduled dispatch that drops TASK files into agent inboxes. Unlocks INT-PARETO always-on heartbeat.
- **Git Concurrency — Zone Ownership (Recommended)**: Each agent owns file patterns. Commander owns orchestration/state/, canon/. Adjudicator owns test files, its inbox. Cartographer owns praxis/, survey reports. Shared mutable files use append-only semantics or per-agent staging files.

---

## CORE CONCEPTS INTRODUCED

- **Field Kit**: MBA role concept — minimum viable cockpit (Layers 1-3 + lean Neovim) that lets Sovereign think anywhere and dispatch to always-on HQ. 70-minute setup target.
- **Brewfile.field**: ~40-formula MBA subset of HQ's ~288-formula Brewfile. 14% of HQ footprint. Canonical list defined in psyche-machine-elucidation.md.
- **chezmoi Template Pattern**: `machine = "hq" | "field"` + `has_voice`, `has_dashboard` flags. dot_zshrc.tmpl with `{{ if eq .machine "hq" }}` blocks. Enables one-repo dotfile management across divergent configs.
- **AjnaPsyche Archon**: Fused executive brain — two OpenClaw instances (Ajna/CSO on MBA, Psyche/CTO on Mac mini) coordinating via Slack + filesystem + git. Not direct IPC.
- **Three Loop Modes**: DISPATCH mode (current — watcher fires on inbox events), SESSION mode (target — persistent CLI in tmux pane), PROACTIVE mode (aspirational — agent scans IMPL map, self-dispatches). Phased ladder.
- **Zone Ownership (Concurrency Strategy)**: File-pattern-based write ownership per agent to prevent git merge conflicts in 4-concurrent-agent scenario. Append-only shared mutable files as complement.
- **Autonomy Gap (70% → ~85%)**: Remaining 30% was not installation — all Python deps already present. Gap was daemon wiring: Chroma server, webhook receiver, corpus health check. Three launchd services close majority of gap.
- **Deployment Playbook**: Formal name for what was TERMINAL-STACK-CONFIG.md. Martial convention (Ansible playbooks). Renamed DEC-SOV-007.
- **Cascade Architecture**: HQ-to-MBA differential (not identical) deployment pattern. Power-aware daemons on MBA (LowPriorityIO, reduced frequency). HQ for parallel orchestration; MBA for brain dumps + directives.
- **Sophistication Plateau Anti-Pattern**: IMPL map at 123 items at "new" status with zero execution = the recognized trap. "More architecture docs won't make the system run." Stop adding; start executing.
- **Restart Loop Root Cause**: corpus-health daemon alerts on uncommitted git changes → hooks write DYN files at session end → nobody commits after → daemon loops. Fix: commit state at session START, or teach corpus-health to tolerate hook-generated DYN files.
- **Stage 7-8 on Yegge's 8-Stage Developer-Agent Evolution**: System self-assessed at near-maximum developer-agent sophistication. 8 MCP servers, 5 plugins, 280+ brew, 17 launchd agents, 23+ skills.

---

## TENSIONS IDENTIFIED

- **Hooks only work for Commander**: The 7-phase clarescence cycle assumes hook infrastructure that only Claude Code supports. Codex CLI (Adjudicator) and Gemini CLI (Cartographer) have no lifecycle hooks. Resolution: watcher script performs post-task documentation for hook-less agents; 7-phase framing is aspirational for non-Commander agents.
- **Always-on vs Rate Limits**: 4 concurrent agents consuming Claude Max (~45 msgs/5hr for Opus) risks exhausting Sovereign's interactive quota. Proposed mitigation: 50% capacity reservation for Sovereign. Residual risk MEDIUM — proactive work is unpredictable in token consumption.
- **Proactive Awareness without Trigger**: Dispatch mode fires on inbox events; proactive mode has no defined trigger mechanism. Polling interval? fswatch scan? Persistent session? Radically different resource profiles. Deferred to Phase 3.
- **Infrastructure Exists but Activation Gap**: Canonical documents (COCKPIT.md, ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md) describe always-on behavior; reality is one-shot dispatch. The gap is activation (cockpit.sh not yet run), not architecture.
- **IMPL Backlog at 123 "new" items**: Most are Psyche-owned spec work or aspirational infrastructure with no execution capacity. Needs Sovereign triage. Commander cannot prune unilaterally.
- **Qdrant MCP not loading (Session 6)**: Configured in session 5 (uvx transport, local ONNX embeddings), absent from Claude Code's deferred tools list. Container healthy on port 6333. MCP process not starting. Possible uvx/stdio incompatibility with Claude Code.
- **Adjudicator "full-auto" risk**: Even with zone ownership, a misconfigured agent can damage its own zone. No arbitration when Cartographer survey and Adjudicator repair target same file simultaneously.

---

## THEMES

- **Reconnaissance → Execution Transition**: Session 5 explicitly declared the 3rd clarescence "the LAST reconnaissance pass." All subsequent sessions mandated as execution. Anti-pattern named: elaboration plateau. The shift from architecture to activation is the dominant narrative of the Feb 9 sessions.
- **Differential Deployment**: Nothing should be mirrored verbatim. MBA vs HQ, Protoss vs Zerg, chezmoi templates vs bare copy — the principle of fit-to-context runs through every architecture choice in this batch.
- **Infrastructure-First Velocity**: The autonomy gap at 70% was not about missing installs — everything was already installed. The blockers were daemon wiring and activation. Recognition that "having tools" ≠ "tools running."
- **Constitutional Escalation of Autonomy**: DEC-SOV-009 (self-improvement as standing order) converts what was permission into obligation. This is a one-way door — an identity commitment, not a policy.
- **Concurrency as the Critical Gate**: Git merge conflicts from 4 concurrent committers is identified as the single bottleneck blocking full always-on operation. Zone ownership is the pragmatic resolution, but it requires codification before any persistent-session activation is safe.

---

## PER-FILE HIGH-VALUE EXTRACTS

### psyche-machine-elucidation (2026-02-08, 645 lines)
- Full layer-by-layer Field Kit specification: what's IN (Layers 1-3, lean Neovim, Tailscale, AeroSpace, chezmoi) and what's OUT (Voice, Doom Emacs, Cursor, local constellation). Rationale per exclusion.
- Canonical Brewfile.field (~40 formulae) defined in full — reference list for MBA setup.
- Tailscale alias set for MBA .zshrc (`hq`, `hq-cockpit`, `hq-dashboard`, `hq-dispatch`, `hq-status`, `hq-agents`).
- chezmoi template structure fully specified: dot_zshrc.tmpl with `{{ if eq .machine "hq" }}` / `{{ if eq .machine "field" }}` blocks; chezmoidata.yaml with `has_voice`, `has_dashboard` flags.
- 8 named Decision Atoms (DEC-PSYCHE-001 through DEC-PSYCHE-008) — most compact concentration of architectural decisions in this batch.
- 8-phase execution checklist: Phase 0 (Foundation/15min) through Phase 8 (Verification/5min), 70-min total.

### constellation-modus-operandi (2026-02-08, 624 lines)
- Full 10-pass clarescence on 4-agent always-on cockpit. Identifies the gap: infrastructure is STRUCTURALLY COMPLETE, activation is pending. cockpit.sh has not been run.
- Canonical dependency graph: SOVEREIGN → Ajna → {Commander, Adjudicator, Cartographer} → REPOSITORY. Commander is hub; if rate-limited, system stalls. Psyche not yet connected (blocked on Tailscale).
- Critical insight: hooks/skills only work for Commander. Codex/Gemini CLIs need watcher-level post-task documentation.
- Neo-Blitzkrieg v1.0 → Always-On Cockpit v2.0 evolution table: trigger model shifts from event-driven to loop-driven.
- Risk matrix: 7 risks rated. Git conflicts (HIGH), Rate limits (HIGH), Runaway agent (HIGH) are the three critical risks.
- Zone ownership recommendation: Commander owns state/+canon, Adjudicator owns test files, Cartographer owns praxis/. Append-only semantics for shared mutable files.
- Phased implementation: Phase 0 (30min, today) → Phase 1 Concurrency Safety (this week) → Phase 2 Persistent Sessions (next week) → Phase 3 Proactive Operations (week 3+).

### session5-execution-priorities (2026-02-09, 136 lines)
- Root cause analysis of corpus-health restart loop: hooks write DYN files at session end → corpus-health alerts → watchdog kicks corpus-health → loop. Fix: commit at session START or tolerate hook DYN files.
- System status snapshot: Docker (neo4j/graphiti/qdrant ALL UP), launchd (10 UP / 2 cycling), Linear MCP installed but not yet exercised, autonomy at ~95% (remaining: job queue, chat bot bridge, clipboard monitor).
- Anti-pattern named explicitly: IMPL backlog at 123 "new" items = sophistication plateau. "STOP adding items. START executing."
- Intentions queue at 168 lines without flush — violates IMPL-B-0006 triage SOP.
- P1 execution targets for session: Qdrant MCP, Graphiti MCP, Linear MCP live test, corpus-health tolerance fix.

### session6-mcp-activation-execution (2026-02-09, 192 lines)
- System snapshot: 53+ MCP tools now live (Linear 33, Graphiti 9, Obsidian 11). First session with native MCP access. Cockpit reloaded, Pane 1 = Psyche confirmed.
- All 6 services GREEN (Chroma/8765, Webhook/8888, Qdrant/6333, Neo4j/7474, Graphiti/8001, OpenClaw/18789).
- Qdrant MCP not loading despite session 5 config — only unresolved technical blocker in batch.
- P1 roadmap: ClickUp MCP (T1b native access) → claudecron (unlocks SYN-31 Live Ledger) → Blitzkrieg Agent Teams skill → MBA physical setup.
- Two decision atoms: Qdrant diagnosis before ClickUp (DEC-S6-001), launchd-based claudecron if no official solution exists (DEC-S6-002).
- IntentionLinks: INT-1501 (maximize autonomy), INT-1503 (fiduciary level), INT-1202 (capitalize on heavy machinery).

### autonomy-narrative-cascade (2026-02-09, 163 lines)
- Sovereign trigger verbatim: "Yes please maximize claude code autonomy, close that final 30%... codify within yourself that you're allowed, nay, required to self-improve." This is the authorization event for DEC-SOV-009.
- Self-positions at Yegge Stage 7-8 of 8. Contextualized against Yegge's Gas Town analysis (Zerg = Gas Town; Syncrescendence = Protoss).
- 32 new Rosetta Stone terms added (v2.3.0): 5 UNIQUE martial terms (no community equivalent for agent orchestration tactics), 26 ADAPTED from legal/financial/governance/scientific domains, 1 ALIGNED (Constitutional AI).
- Three new launchd services to close autonomy gap: Chroma server (semantic search), webhook receiver (external event integration), corpus health check (staleness prevention). All Python deps pre-installed — gap was wiring only.
- Cascade architecture: HQ optimized for parallel agent orchestration; MBA for brain dumps + directives. Power-aware daemons on MBA (LowPriorityIO, reduced frequency).
- 2nd-3rd-4th order effects documented: Chroma + webhook = external semantic-informed dispatch (2nd); self-improvement mandate + corpus health = self-fixing infrastructure gaps (3rd); MBA cascade = two-machine redundancy (4th).

---

## WHAT THIS BATCH CONTRIBUTES TO THE WHOLE

These five sessions represent the pivot point from architecture-building to operational activation — the moment the system recognized it had been over-designing and under-executing. The psyche-machine and modus-operandi claresce documents (Feb 8) completed the dual-machine architecture design: Field Kit + HQ separation, Tailscale bridge, chezmoi dotfile management, zone ownership concurrency strategy, and the full 10-pass analysis of what the always-on cockpit requires to be safe. The three Feb 9 sessions then enacted the pivot: Session 5 named the sophistication plateau anti-pattern and mandated execution over reconnaissance; Session 6 confirmed 53+ MCP tools were now live and identified the P1 sprint targets (ClickUp MCP, claudecron, Blitzkrieg skill, MBA physical setup); the autonomy-cascade session inscribed the self-improvement obligation constitutionally and documented the autonomy gap as a wiring problem (not an installation problem), closing with 6 decision atoms that define Commander's operational identity going forward.
