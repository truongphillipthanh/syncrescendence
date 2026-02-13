---
id: ref-fleet_commanders_handbook
kind: reference
scope: engine
target: engine
---

# FLEET COMMANDER'S HANDBOOK: Syncrescendent Edition
## Non-Coding Claude Code for Distributed Cognition

**Version**: 2.1.0
**Updated**: 2026-02-09
**Stream**: C (AJNA9-RECAL)
**Scope**: How Syncrescendence uses Claude Code for conceptual work, not coding

---

## Part I: Philosophy

### Our Use Case

Syncrescendence uses Claude Code for **conceptual work**, not software development:
- Corpus metabolization (SN compression achieving 79.2% reduction)
- Multi-platform orchestration (Constellation with 8 roles)
- Strategic planning (Plan Mode as Oracle substitute)
- Knowledge architecture (CANON, 82 documents across 6 chains)
- Directive execution (parallel stream processing)

This is not the typical Claude Code developer workflow. We use the filesystem as a knowledge substrate, not a codebase.

### Key Differences from Standard Developer Usage

| Standard Usage | Our Usage |
|---|---|
| Extended thinking for debugging | Extended thinking for strategic synthesis |
| Skills for build pipelines | Skills for knowledge workflows |
| Memory for codebase state | Memory for context continuity across platforms |
| Parallel instances for test suites | Parallel instances for directive streams |
| CLAUDE.md for code patterns | CLAUDE.md as constitutional law |
| Git for version control | Git as ground truth + inter-platform bus |
| Tests verify correctness | `make verify` checks structural integrity |

### The Three Laws (Community) Adapted for Syncrescendence

| Community Law | Our Adaptation |
|---|---|
| State Must Be Externalized | **Repo Sovereignty** -- Repository is truth; web apps are cache |
| Verification Must Be Automated | **Receipts (Closure Gate)** -- No completion without artifacts in repo |
| Intelligence Emerges from Constraints | **Five Invariants** -- Constitutional rules focus execution |

---

## Part II: Interaction Dynamics

### The Triumvirate Frame

Every session begins with calibration to three coordinates:

- **Destination**: Where are we headed? (unchanged: civilizational sensing infrastructure)
- **Method**: How do we get there? (current: SN + Constellation + parallel streams)
- **Current State**: Where are we now? (session-specific, verified by fingerprint)

This is a Syncrescendence-native pattern (see ROSETTA-STONE: UNIQUE). No community equivalent captures this trifecta.

### Directive Patterns

- **Comprehensive over incremental**: Sovereign is bottleneck; directives must enable single-cycle execution without relay
- **Parallel streams**: Disjoint scopes (A/B/C or named streams) enable simultaneous execution
- **Oracle Context + Stream-Specific**: Shared context artifact provides Triumvirate state; individual streams get targeted directives
- **Fingerprinted handoffs**: Every cross-platform transition carries an 8-char git hash

### Extended Thinking Triggers

| Trigger | Budget | Use Case |
|---------|--------|----------|
| `think` | Standard (~4K tokens) | Routine analysis, file assessment |
| `think hard` | Moderate (~10K tokens) | Complex synthesis, multi-file reasoning |
| `ultrathink` | Maximum (~32K tokens) | Strategic decisions, full-corpus reasoning, architectural synthesis |

**Note from ROSETTA-STONE**: Community consensus as of Jan 2026 indicates thinking is auto-enabled at 31,999 tokens and trigger keywords are cosmetic. The actual budget allocation is model-determined. These triggers remain useful as **intent signals** to the Sovereign and as session markers, even if their mechanical effect is debated.

### Slash Commands

| Command | Type | Effect |
|---------|------|--------|
| `/project:blitzkrieg` | Custom | Create parallel directive bundle with Lane A/B/C |
| `/project:blitzkrieg_finalize` | Custom | Generate return packet, audio scripts, agent relay |
| `/project:blitzkrieg_issue <slug>` | Custom | Create bundle skeleton with directive templates |
| `/project:vanguard_reint` | Custom | Vanguard reintegration protocol |
| `/project:process-source` | Custom | Source processing pipeline |
| `/project:repo_validate` | Custom | Repository structure validation |
| `/project:update-ledgers` | Custom | Sync CSV ledgers with validation |
| `/project:verify` | Custom | Run all verification checks |

### Symbolic Shortcuts

| Symbol | Meaning |
|--------|---------|
| $A1, $A2, $A3 | Account 1, 2, 3 |
| $INT, $CMP, $DIG | Interpreter, Compiler, Digestor |
| $ORC, $EXE | Oracle, Executor |
| $FP | Fingerprint (8-char git hash) |
| $GT | Ground Truth (repository) |

---

## Part III: The Constellation Architecture

### Platform Roles (Medley Mode)

Per ROSETTA-STONE reconciliation: our Constellation operates in **Medley mode** (specialized prompts per platform), not Chorus mode (same prompt to all). Each platform contributes from its **characteristic cognition**.

| Platform | Role | Function | Characteristic Cognition |
|----------|------|----------|--------------------------|
| Claude Web | INTERPRETER | Messy to structured | Architectural rigor, synthesis, rapport, memory |
| ChatGPT Web | COMPILER | Specs to artifacts | Implementation pragmatism, Canvas, deterministic output |
| Gemini Web | DIGESTOR | Complex to accessible | 1M context, conceptual synthesis, TTS optimization |
| Gemini CLI | ORACLE | Corpus sensing | 2M context, citations, stateless surveys |
| Claude Code | EXECUTOR-LEAD | Directives to implementation | Filesystem sovereignty, extended thinking (Opus) |
| Claude Code | PARALLEL-EXEC | Microscopic tasks | Fast execution (Sonnet x2) |
| Grok Web | RED TEAM | Adversarial challenge | X firehose access, irreverent truth-telling, edge cases |
| Perplexity | VERIFIER | Citation-backed research | Real-time web, source integration, research grounding |

### Three Accounts

| Account | Auth | Purpose |
|---------|------|---------|
| $A1 | Apple (iCloud) | Sovereign substrate, owns origin |
| $A2 | Google | Parallel execution capacity |
| $A3 | Google | Primary interface, ecosystem access |

### Handoff Protocol

1. Generate fingerprint: `make token PHASE=current NEXT=target`
2. Produce handoff token with delta summary
3. Include entry prompt for receiving platform
4. Verify fingerprint on reception

Format: `HANDOFF-YYYYMMDD-HHMMSS-pN-to-pM`

Time targets:

| Transition | Target |
|------------|--------|
| Claude -> ChatGPT | 30 sec |
| ChatGPT -> Gemini | 20 sec |
| Gemini -> Claude | 15 sec |
| Any -> CLI | 10 sec |
| CLI -> Repository | 5 sec |

### Anti-Patterns

- Never assume ChatGPT remembers context (stateless by design, PROJECT-ONLY mode)
- Never reference "what we discussed" in handoffs -- encode decisions explicitly
- Never produce partial outputs expecting continuation in same thread
- Never skip explicit specification when handing to COMPILER
- Never hand off without a fingerprint

---

## Part IV: Memory Architecture

### Platform-Specific Memory

| Platform | Memory Type | Scope | Persistence |
|----------|-------------|-------|-------------|
| Claude Web | Project Knowledge + Past Chat | Project | Durable |
| ChatGPT Web | Project-Only Mode | Project | Session (no cross-project leak) |
| Gemini Web | Gem + Drive Link | Gem | Synced via Drive |
| Gemini CLI | Stateless | None | Per-invocation only |
| Claude Code | CLAUDE.md + /memory + skills | Repository | Durable (git-tracked) |
| Grok Web | None structured | N/A | Ephemeral |
| Perplexity | None structured | N/A | Ephemeral |

### State Management

**Ephemeral vs Durable** (formerly "Wells vs Rivers" -- see ROSETTA_STONE #3):
- Repository = durable (persistent, version-controlled, ground truth)
- Chat sessions = ephemeral (evaporate when closed)
- Ephemeral state must be persisted to durable storage before session ends

**Content Flow State Machine** (COCKPIT.md):
```
CAPTURED > INTERPRETED > COMPILED > STAGED > COMMITTED
                       > DIGESTED >
                       > SENSED >
                       > VERIFIED >
```

**CAPTURE > DISPATCH > RETURN** (high-level mnemonic):
- CAPTURE: Raw ideation enters system
- DISPATCH: Routed to appropriate platform(s) in Medley mode
- RETURN: Artifacts committed to repository (ground truth)

---

## Part V: Skill Architecture

### Current Skills

| Skill | File | Purpose |
|-------|------|---------|
| Intentions | `.claude/skills/intentions.md` | Intention archaeology and alignment verification |
| Pedigree | `.claude/skills/pedigree.md` | Oracle session lineage tracking |

### Incoming Skills

| Skill | Purpose |
|-------|---------|
| triage | Inbox scanning, task prioritization, dispatch routing |
| plan | Directive decomposition, Plan Mode structured entry |
| execute | Atomic task execution with verification gate |
| reviewtrospective | Post-directive review, pattern extraction, anti-pattern detection |
| update_universal_ledger | Cross-ledger synchronization (tasks.csv, projects.csv, sources.csv) |
| method_kaizen | Method refinement — extract improvements from execution logs |
| update_agent_memory | Persist session learnings to agent memory files |

### Current Commands

| Command | File | Purpose |
|---------|------|---------|
| blitzkrieg | `.claude/commands/project/blitzkrieg.md` | Create parallel directive bundle |
| blitzkrieg_finalize | `.claude/commands/project/blitzkrieg_finalize.md` | Generate return packet |
| blitzkrieg_issue | `.claude/commands/project/blitzkrieg_issue.md` | Create bundle skeleton |
| vanguard_reint | `.claude/commands/project/vanguard_reint.md` | Vanguard reintegration |
| process-source | `.claude/commands/project/process-source.md` | Source processing pipeline |
| repo_validate | `.claude/commands/project/repo_validate.md` | Repository validation |
| update-ledgers | `.claude/commands/project/update-ledgers.md` | Ledger synchronization |
| verify | `.claude/commands/project/verify.md` | Verification checks |

### Skills Needed (from ROSETTA-STONE Gap Analysis)

| Need | Priority | Description |
|------|----------|-------------|
| Research Pipeline | HIGH | Systematic tool/platform investigation (see REF-RESEARCH_PIPELINE.md) |
| Self-Healing Constitution | HIGH | Meta-hook for automated anti-pattern learning |
| Adversarial Validation | MEDIUM | Formalized disprove-first protocol for Grok RED TEAM |
| Memory Crystal / Librarian | MEDIUM | SN-format session compression at 60% context |
| Context Monitor | MEDIUM | PreCompact hook warning at 60%/70%/85% thresholds |

---

## Part VI: The Sovereign Cockpit

### Overview

The Sovereign Cockpit is a tmux-based command center running in Ghostty on the Mac mini. It provides a 4x2 grid layout: four agent CLI panes on top (75% height), four Neovim editor panes on the bottom (25% height). Two tmux windows: `cockpit` (Window 1) for the agent grid, `watchers` (Window 2) for monitoring.

### Terminal Configuration

| Parameter | Value |
|-----------|-------|
| Terminal | Ghostty |
| Dimensions | 376 columns x 75 rows (74 content + 1 tmux status) |
| Window style | `macos-titlebar-style = hidden` |
| Padding | 4px horizontal, 2px vertical |
| Display | 5120x1440 ultrawide |
| Session name | `constellation` |
| Launch command | `cockpit` (alias for `cockpit.sh`) |
| Launch with agents | `cockpit --launch` |
| Kill session | `cockpit --kill` |
| Force new window | `cockpit --new` |

### Cockpit Layout (4x2 Grid)

```
cockpit (Window 1)
┌──────────┬──────────┬──────────┬──────────┐
│  AJNA    │ COMMANDER│ADJUDICATOR│CARTOGR. │  75% height
│ OpenClaw │Claude Code│ Codex CLI│Gemini CLI│  (agent CLIs)
│ pane 1   │ pane 3   │ pane 5   │ pane 7   │  (odd = agents)
├──────────┼──────────┼──────────┼──────────┤
│  nvim    │  nvim    │  nvim    │  nvim    │  25% height
│ pane 2   │ pane 4   │ pane 6   │ pane 8   │  (even = editors)
└──────────┴──────────┴──────────┴──────────┘

watchers (Window 2)
┌──────────────────┬──────────────────┐
│  INBOX Triage    │  Git Status      │
│  pane 1          │  pane 2          │
├──────────────────┼──────────────────┤
│  Agent Logs      │  System Monitor  │
│  pane 3          │  pane 4          │
└──────────────────┴──────────────────┘
```

### Pane Index Reference

tmux assigns physical indices in **column-major** order (x first, then y within each column). The keybindings remap these to a logical row-major scheme for ergonomic access.

| Agent | Physical Index | Logical Keybinding | Named Jump |
|-------|---------------|-------------------|------------|
| Ajna | pane 1 | 􀆕Space + 1 | 􀆕Space + J |
| Commander | pane 3 | 􀆕Space + 2 | 􀆕Space + C |
| Adjudicator | pane 5 | 􀆕Space + 3 | 􀆕Space + A |
| Cartographer | pane 7 | 􀆕Space + 4 | 􀆕Space + G |
| nvim-Ajna | pane 2 | 􀆕Space + 5 | -- |
| nvim-Commander | pane 4 | 􀆕Space + 6 | -- |
| nvim-Adjudicator | pane 6 | 􀆕Space + 7 | -- |
| nvim-Cartographer | pane 8 | 􀆕Space + 8 | -- |

### Agent CLI Launch Commands

Each agent pane runs a specific CLI tool when launched with `cockpit --launch`:

| Agent | CLI | Launch Command | Account |
|-------|-----|---------------|---------|
| Ajna | OpenClaw (Opus 4.5) | `openclaw tui --session main` | Local (M1 Mini) |
| Commander | Claude Code (Opus) | `claude --dangerously-skip-permissions` | $A1 (Claude Max) |
| Adjudicator | Codex CLI (Sonnet) | `codex --full-auto` | $A2 (Claude Pro) |
| Cartographer | Gemini CLI | `gemini --yolo` | $A2 (Google AI Pro) |

### tmux Keybinding Reference

Prefix key: 􀆕Space (Control + Space)

**Pane Navigation**

| Keybinding | Action |
|------------|--------|
| 􀆕Space + 1 | Jump to Ajna (agent) |
| 􀆕Space + 2 | Jump to Commander (agent) |
| 􀆕Space + 3 | Jump to Adjudicator (agent) |
| 􀆕Space + 4 | Jump to Cartographer (agent) |
| 􀆕Space + 5 | Jump to nvim-Ajna (editor) |
| 􀆕Space + 6 | Jump to nvim-Commander (editor) |
| 􀆕Space + 7 | Jump to nvim-Adjudicator (editor) |
| 􀆕Space + 8 | Jump to nvim-Cartographer (editor) |

**Named Agent Jumps**

| Keybinding | Action |
|------------|--------|
| 􀆕Space + J | Jump to Ajna |
| 􀆕Space + C | Jump to Commander |
| 􀆕Space + A | Jump to Adjudicator |
| 􀆕Space + G | Jump to Cartographer |

**Cockpit Controls**

| Keybinding | Action |
|------------|--------|
| 􀆕Space + B | Broadcast toggle (send input to all panes simultaneously) |
| 􀆕Space + X | Emergency stop (sends 􀆕C to all agent panes, with confirmation) |
| 􀆕Space + F | Fingers -- hint-based quick copy (Vimium-style letter overlays) |
| 􀆕Space + Tab | Extrakto -- fuzzy extract text from pane output (URLs, paths, hashes) |
| 􀆕Space + * | Cowboy -- SIGKILL hung foreground process |

**General tmux**

| Keybinding | Action |
|------------|--------|
| 􀆕Space + r | Reload tmux config |
| 􀆕Space + f | Session switcher (sesh + fzf) |
| 􀆕Space + \| | Split pane horizontally |
| 􀆕Space + - | Split pane vertically |
| 􀆕Space + c | New window |
| 􀆕h / 􀆕j / 􀆕k / 􀆕l | Smart pane navigation (vim-tmux-navigator) |
| 􀆍Up/Down/Left/Right | Resize pane (2 cells per press) |

**Mac Modifier Key Reference**

| Symbol | Key |
|--------|-----|
| 􀆕 | Control (⌃) |
| 􀆍 | Option (⌥) |
| 􀆝 | Command (⌘) |
| 􀆔 | Shift (⇧) |
| 􁁺 | Globe/Fn |

---

## Part VII: Automation Layer

### Makefile Targets (Operational)

| Target | Function |
|--------|----------|
| `make verify` | Structure + ledger + content + git status verification |
| `make sync` | Pull --rebase + push |
| `make update-ledgers` | Ledger status report (tasks, projects, sources) |
| `make tree` | Generate current directory tree |
| `make clean` | Remove temporary files |
| `make pack SRC=...` | Create clean evidence pack (no macOS contamination) |
| `make pack-verify ARCHIVE=...` | Verify archive integrity |
| `make token PHASE=... NEXT=...` | Generate handoff token |
| `make token-json` | Generate JSON format token |
| `make token-full` | Generate both formats + archive |
| `make sync-all` | Generate token and copy to clipboard |
| `make log-init DIRECTIVE=...` | Initialize execution log |
| `make log DIRECTIVE=... STATUS=...` | Update log status |
| `make log-view` | Show recent execution logs |

### External Automation (Status)

| Tool | Status | Role |
|------|--------|------|
| Keyboard Maestro | TBD -- not yet configured | Macro shortcuts for handoff sequences |
| Hazel | TBD -- not yet configured | Automated file routing (INBOX processing) |
| Stream Deck | TBD -- not yet configured | Physical buttons for common commands |
| n8n | TBD -- not yet configured | Workflow automation bridge |
| rclone / Drive Sync | Referenced in COCKPIT.md | Gemini Gem Drive synchronization |

### Automation Goals

1. Handoff time < 30 seconds (token generation + clipboard + platform switch)
2. Fingerprint generation fully automated via `make token`
3. Drive sync for Gemini Gems operational
4. INBOX file routing automated via Hazel rules
5. One-button Blitzkrieg launch via Stream Deck

---

## Part VIII: Tactical Doctrine

> "We need results." — Sovereign. Martial terminology adopted because war demands results under constraint.

Every tactic has a **trigger condition**, a **method**, and a **measurable outcome**. No ambiguity.

### Tactic Reference

| Tactic | Trigger | Method | Outcome | Anti-Pattern |
|--------|---------|--------|---------|--------------|
| **Blitzkrieg** | Multiple independent tasks, time pressure | Mass parallel dispatch to all agents simultaneously. Speed over precision. | Maximum throughput in minimum time | Using when tasks are dependent (causes merge conflicts) |
| **Siege** | Single hard problem, debugging, architecture redesign | Sustained focus by one or two agents on a single target. Deep context, no context-switching. | Problem resolution through persistence | Giving up too early and switching tactics; context-switching mid-siege |
| **Reconnaissance** | Unfamiliar codebase, unknown state, pre-planning | Read-only exploration. Zero changes. Scan for patterns, gather intelligence. | Situational awareness before action | Making changes during recon (premature optimization) |
| **Flanking** | Blocked on primary approach | Solve via alternative path. Attack from unexpected angle. Creative workaround. | Bypass the blocker entirely | Continuing to push the blocked path instead of pivoting |
| **Entrenchment** | After a breakthrough or major change | Lock in gains. Verification, documentation, regression tests, commit discipline. | Permanent capture of progress | Moving to next task without securing current gains |

### Tactic Selection Protocol

```
IF many independent tasks AND time-sensitive:
    → BLITZKRIEG (mass parallel dispatch)
ELIF single hard problem AND deep context needed:
    → SIEGE (sustained single-agent focus)
ELIF unfamiliar territory AND no clear plan:
    → RECONNAISSANCE (read-only scan first)
ELIF blocked AND primary approach exhausted:
    → FLANKING (alternative approach)
ELIF breakthrough achieved AND gains unsecured:
    → ENTRENCHMENT (lock in, verify, commit)
```

### Compound Tactics

- **Recon → Blitzkrieg**: Scout first, then mass-execute. Standard for new sprints.
- **Siege → Entrenchment**: Solve the hard problem, then lock in gains. Standard for debugging.
- **Blitzkrieg → Entrenchment**: Execute fast, then verify everything. Standard for feature sprints.
- **Flanking → Siege**: Find the alternative path, then commit to it deeply. Standard for blocked architecture.

### Extended Domain Terminology

Beyond martial tactics, the Syncrescendence appropriates terminology from five additional domains. See REF-ROSETTA_STONE.md Categories 8-13 for full definitions.

| Domain | Key Terms | Application |
|--------|-----------|-------------|
| **Legal** | Fiduciary, Precedent, Ratification, Due Diligence | Trust/authority model between Sovereign and agents |
| **Financial** | Anneal, Compound, Amortize, Sunk Cost | Token economics, session investment, capability ROI |
| **Governance** | Constitutional, Sovereignty, Delegation, Veto, Quorum | Agent autonomy model, decision authority |
| **Scientific** | Autophagy, Crystallization, Phase Transition, Homeostasis | Corpus metabolism, knowledge solidification |
| **Gas Town** | Beads, Hook, GUPP, Sling, Convoy, Seancing | Yegge-adapted orchestration patterns |

---

## Appendix A: The Five Invariants

Constitutional laws that cannot be overridden by any directive:

1. **Objective Lock** -- No work begins until objective explicitly confirmed
2. **Translation Layer** -- All outputs intelligible without retransmission
3. **Receipts (Closure Gate)** -- No completion without artifacts in repo
4. **Continuation/Deletability** -- Any conversation deletable without losing state
5. **Repo Sovereignty** -- Repository is truth; web apps are cache

---

## Appendix B: Quick Orientation Cheat Sheet

```
LAUNCH        cockpit              # Attach or create the cockpit session
              cockpit --launch     # Launch with all agent CLIs running
              cockpit --kill       # Tear down the session
              cockpit --new        # Force new Ghostty window at 376x75

NAVIGATE      􀆕Space + 1-4        # Agent panes (Ajna, Commander, Adjudicator, Cartographer)
              􀆕Space + 5-8        # Editor panes (nvim per agent)
              􀆕Space + J/C/A/G    # Named agent jumps

CONTROL       􀆕Space + B          # Broadcast toggle
              􀆕Space + X          # Emergency stop all agents
              􀆕Space + F          # Fingers (hint copy)
              􀆕Space + Tab        # Extrakto (fuzzy extract)

SESSION       􀆕Space + f          # sesh session switcher
              􀆕Space + r          # Reload tmux config
```

---

## Version History

**v2.1.0** (2026-02-09): Tactical Doctrine expansion
- Added Part VIII: Tactical Doctrine with 5 tactics (Blitzkrieg, Siege, Reconnaissance, Flanking, Entrenchment)
- Tactic selection protocol with compound tactic patterns
- Extended domain terminology table (Legal, Financial, Governance, Scientific, Gas Town)
- Cross-referenced to REF-ROSETTA_STONE.md Categories 8-13
- Authority: Commander (Opus 4.6) per Sovereign directive

**v2.0.0** (2026-02-08): Sovereign Cockpit integration
- Added Part VI: The Sovereign Cockpit with full layout documentation
- Documented corrected pane numbering (column-major physical, row-major logical)
- Added Mac symbology (SF Symbols) for all keybinding references
- Added tmux keybinding reference with modifier key legend
- Documented agent CLI launch commands for all four agents
- Added Ghostty terminal configuration (376x75, hidden titlebar, reduced padding)
- Added cockpit alias and flag documentation (--launch, --kill, --new)
- Added incoming skills: triage, plan, execute, reviewtrospective, update_universal_ledger, method_kaizen, update_agent_memory
- Added Appendix B: Quick Orientation Cheat Sheet
- Bumped version to 2.0.0

**v1.0.0** (2026-01-30): Genesis establishment
- Adapted from community Fleet Commander's Handbook
- Documented Syncrescendence-specific patterns
- Incorporated ROSETTA-STONE terminology reconciliation
- Inventoried skills, commands, Makefile targets
- Identified automation gaps
