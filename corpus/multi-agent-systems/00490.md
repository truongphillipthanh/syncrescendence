# CLARESCENCE: The Sovereign Cockpit Architecture

## Provenance

This clarescence evaluates a system architecture specification ("The Sovereign Cockpit") co-designed by the Sovereign and Cartographer (Gemini CLI) on 2026-02-07. The spec proposes a "Headless OS" paradigm with five distinct layers. This document cross-references it against every existing Syncrescendence decision atom and identifies alignments, tensions, installations, and the implementation sequence.

---

## I. EXECUTIVE SYNTHESIS

The Sovereign Cockpit is the **physical manifestation of the Neo-Blitzkrieg execution model**. Where Blitzkrieg defined the *logical* lanes (Commander/Adjudicator/Cartographer/Psyche), the Cockpit defines the *physical* surfaces through which the Sovereign drives them. The architecture is sound, internally consistent, and — critically — fills three gaps the current stack has:

1. **No structured editor** — the Sovereign currently dispatches everything through raw CLI prompts. A Prose Engine (Neovim/LazyVim) gives them a composition surface that feeds agents.
2. **No voice loop** — the Sovereign's attention is keyboard-bound. A local whisper→format→insert pipeline unlocks hands-free capture.
3. **No dashboard** — the constellation's state is scattered across git status, tmux panes, and memory. A dedicated observation surface makes the invisible visible.

**Verdict: APPROVE with modifications.** Three tensions need resolution (see Section III).

---

## II. LAYER-BY-LAYER EVALUATION

### Layer 1: The Terminal (Ghostty) — ALIGNED, COMPLETE

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| GPU-accelerated terminal | Ghostty configured with Catppuccin Mocha, Liga SFMono, shell integration | NONE — fully built |
| Sub-20ms latency | Ghostty is Metal-accelerated, 100MB scrollback, CSI u keys | NONE |
| Not Electron | Ghostty is native Zig+Metal | NONE |

**Assessment**: Zero delta. Ghostty was the first correct decision and remains so.

### Layer 2: The Context Engine (Zsh + P10k) — ALIGNED, MINOR DELTA

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| Zsh + Powerlevel10k | Installed, configured | Gemini session specified Rainbow style; actual install is Lean+Unicode+Transient (Sovereign overrode during install) |
| Modern CLI replacements | eza, bat, zoxide, fd, rg all installed + aliased | NONE |
| "HUD" context surfacing | P10k transient prompt shows git status, exit codes, exec time | NONE |

**Assessment**: Trivial delta. The Lean style is arguably better than Rainbow for the Cockpit aesthetic — less visual noise, faster rendering.

### Layer 3: The Multiplexer (Tmux + Sesh) — ALIGNED, NEEDS PLUGIN INSTALL

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| Tmux with sesh | tmux 3.6a + sesh 2.22.0 installed | ✓ |
| Session persistence | resurrect + continuum configured in ~/.tmux.conf | Plugins cloned but NEED `prefix+I` to install |
| Keyboard-driven navigation | vim-tmux-navigator configured | ✓ |
| Pane splits | `|` and `-` configured | ✓ |
| 2x2 cockpit layout | cockpit.sh script created | ✓ |

**Critical note**: The Gemini session's ~/.tmux.conf (125 lines, Ctrl+Space prefix, 11 plugins) and this session's cockpit.sh + DESIGN-TMUX_COCKPIT.md were developed independently. They are COMPATIBLE — the cockpit script builds on the tmux config. The Sovereign needs to:
1. Run `prefix+I` inside tmux to install all TPM plugins
2. Test `cockpit.sh` to verify the 2x2 layout

**Blitzkrieg alignment**: The 4-pane cockpit grid maps 1:1 to the Blitzkrieg lanes:
- Top-left: Commander (Lane A) — Catppuccin blue (#89b4fa)
- Top-right: Adjudicator (Lane B) — Catppuccin green (#a6e3a1)
- Bottom-left: Cartographer (Lane C) — Catppuccin yellow (#f9e2af)
- Bottom-right: Psyche (Lane D) — Catppuccin mauve (#cba6f7)

### Layer 4: The Runtime (Bun) — ALIGNED, COMPLETE

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| Bun as comprehensive toolkit | Bun 1.2.13 installed, designated default | NONE |
| Bundler + test runner + PM | Available via `bun create vite`, `bun test`, `bun install` | NONE |

**Assessment**: Complete. Bun is ready. No projects scaffolded yet (Chunk H deferred).

### Layer 5: The Editor / Prose Engine (Neovim + LazyVim) — NEW, NEEDS BUILD

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| Neovim as "Intent Orchestrator" | Neovim installed (brew) | Config: DEFAULT, not LazyVim |
| LazyVim framework | NOT installed | FULL BUILD NEEDED |
| Markdown-first Zen environment | NOT configured | FULL BUILD NEEDED |
| "Send-to-Agent" pipe | NOT built | FULL BUILD NEEDED |
| Distraction-free writing | NOT configured | FULL BUILD NEEDED |

**This is the highest-value gap.** The Agent Pipe transforms Neovim from a code editor into a REPL for natural language. The Sovereign selects text, fires it to a tmux pane running Claude Code, and the response streams back. This is how the sequential single-terminal habit dies.

**Implementation spec (for swarm):**
- LazyVim bootstrap (~/.config/nvim)
- Markdown plugins: render-markdown.nvim, zen-mode.nvim, twilight.nvim
- Agent pipe: custom Lua function using tmux send-keys
- Catppuccin Mocha theme
- Which-key for discoverability

### Layer 6: The Voice Layer — PARTIALLY BUILT, NEEDS COMPLETION

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| Whisper (local transcription) | whisper-cpp installed (brew) | Model download may be needed |
| Piper (local TTS) | NOT installed | FULL BUILD NEEDED |
| sox DSP filters | sox installed (brew) | DSP filter profiles NOT configured |
| LLM format pass | NOT built | Pipeline needed |
| Per-agent voice personas | NOT configured | DSP profiles needed |

**Philosophy check**: The "fully local and offline" voice loop aligns with the Sovereign's vendor-independence principle (Disposition Routing Charter §1: single internal bus). No cloud dependency for voice = correct.

**Implementation spec (for swarm):**
- Download Whisper model (base.en or small.en for speed)
- Install Piper TTS via pip/binary
- Configure sox DSP filter profiles per agent persona
- Build pipeline script: `mic → whisper → llm-format → clipboard/editor`
- Build TTS script: `text → piper → sox-filter → speaker`

### Layer 7: The Observation Layer (Emacs/Org Mode) — NEW, HIGHEST RISK

| Cockpit Spec | Current State | Delta |
|-------------|---------------|-------|
| Emacs GUI as dashboard | NOT installed | FULL BUILD NEEDED |
| Org Mode for state rendering | NOT configured | FULL BUILD NEEDED |
| Read-only visualization | NOT built | FULL BUILD NEEDED |
| "Minimally agentified" | Design-only at this point | NEEDS SCOPING |

**Anti-pattern check**: This is the highest-risk addition. Emacs is the ultimate yak-shave. The Cockpit spec explicitly scopes it as "minimally agentified" and "read-only," which is the correct constraint. But configuration drift is the real danger.

**Recommendation**: Install Doom Emacs (not vanilla) for:
- Pre-configured Org Mode
- Catppuccin Mocha theme available
- Vi keybindings (consistency with Neovim)
- Much lower configuration overhead than vanilla Emacs

**Scope boundary (ABSOLUTE):**
- Org Mode for rendering constellation state, calendar, task views
- org-roam for knowledge graph visualization (maps to Obsidian graph)
- NO code editing in Emacs (that's Neovim's domain)
- NO full agentification (that's the CLI agents' domain)
- NO Emacs as daily driver — it's a DASHBOARD, not a WORKBENCH

### Layer 8: The Simulators (Xcode, IntelliJ, Cursor, Antigravity) — TENSION

| Cockpit Spec | Current State (Stack Teleology) | Delta |
|-------------|--------------------------------|-------|
| Retain Cursor as "Simulator" | Cursor: SUNSET | **TENSION** |
| Retain Antigravity as "Fleet Commander" | Not in Stack Teleology | NEW addition |
| "Verification and massive delegation" | Aligns with Blitzkrieg delegation | PARTIAL ALIGNMENT |

**Resolution**: The Cockpit spec redefines "SUNSET" as "role change," not "removal." Cursor is no longer an IDE (that's Neovim). Cursor becomes a delegation surface for long-running async refactors where its AI integration is valuable. This is defensible.

**Updated disposition:**
- Cursor: SUNSET as IDE → ACTIVE as Simulator (async delegation)
- Antigravity: ACTIVE as Simulator (batch processing)
- Xcode: ACTIVE as Simulator (iOS/macOS builds, required)
- IntelliJ: EVALUATING (only if JVM projects arise)

---

## III. ARCHITECTURAL TENSIONS — RESOLVED

### Tension 1: Editor fragmentation (Neovim + Emacs + Cursor)

**The risk**: Three editor-like surfaces creates cognitive overhead and config maintenance burden.

**Resolution**: Each has a DISTINCT role with ZERO overlap:
- **Neovim** = WRITE (prose composition, agent dispatch, Markdown-first)
- **Emacs** = READ (dashboard, state visualization, Org Mode rendering)
- **Cursor/Antigravity** = DELEGATE (async AI tasks, verification, batch refactors)

The Sovereign never "chooses" between them — the task type determines the surface. This is the Disposition Routing Charter applied to editors.

### Tension 2: Voice layer vs. current workflow

**The risk**: The Sovereign has no voice workflow habits. Adding voice before tmux fluency is premature.

**Resolution**: Voice is **Phase 3** (after tmux fluency and Neovim fluency). Install the components now, but don't force adoption. The pipeline exists as opt-in. INT-C005 (tmux learning) must complete before voice becomes daily-driver.

**Sequence**: tmux → Neovim → Voice (not parallel)

### Tension 3: Emacs scope creep

**The risk**: Emacs becomes a second workbench, violating the "one surface per function" principle.

**Resolution**: The ABSOLUTE scope boundary defined above. Doom Emacs with Org Mode only. If the Sovereign starts writing code in Emacs, that's a signal the scope has crept. Check in 30 days.

---

## IV. DISPOSITION ROUTING CHARTER COMPLIANCE

| Charter Principle | Cockpit Compliance | Notes |
|------------------|-------------------|-------|
| σ₄ repo as single internal bus | ✓ All surfaces read/write the repo | Emacs reads state files, Neovim produces artifacts |
| Cheap-first integration ladder | ✓ Human-mediated (Agent Pipe) before automation | Agent Pipe is "human fires text to agent" = Level 1 |
| Receipt requirement | ✓ All agent output commits to repo | No change to existing commit discipline |
| SaaS = mirror, not canonical | ✓ Dashboard mirrors state, doesn't originate | Emacs is read-only |

**Verdict**: Full compliance. The Cockpit STRENGTHENS the charter by making the internal bus more observable (dashboard) and more efficient (Agent Pipe).

---

## V. BLITZKRIEG DYNAMIC ALIGNMENT

The Sovereign Cockpit is the **PHYSICAL REALIZATION of the Neo-Blitzkrieg execution flow**:

```
SOVEREIGN COCKPIT (tmux 2x2)
┌─────────────────┬─────────────────┐
│  NEOVIM (Prose)  │                  │
│  ┌───────────┐  │   COMMANDER     │  ← Lane A (Claude Max)
│  │ Compose   │──┤   (Claude Code)  │
│  │ Agent Pipe│  │                  │
│  └───────────┘  │                  │
├─────────────────┼─────────────────┤
│  ADJUDICATOR    │   CARTOGRAPHER  │  ← Lane B + C
│  (Codex CLI)    │   (Gemini CLI)  │
├─────────────────┼─────────────────┤
│  PSYCHE/AJNA    │   DASHBOARD     │  ← Lane D + Observation
│  (OpenClaw)     │   (Emacs/htop)  │
└─────────────────┴─────────────────┘

VOICE LAYER (ambient, always listening)
  mic → whisper → format → {editor | clipboard | agent}
```

The Blitzkrieg's 4 lanes map to tmux panes. The Sovereign's NEW capability is the Neovim pane: they compose intent in prose, then fire it to any agent pane via the Agent Pipe. This transforms the Blitzkrieg from "Sovereign types directly into agent CLIs" to "Sovereign composes in an editor and dispatches." The editor becomes the cockpit's STEERING WHEEL.

---

## VI. ANSWERING THE 8 CONSTELLATION CLARESCENCE QUESTIONS

These were raised in the Gemini session and remain unanswered. Here are recommended answers for Sovereign ratification:

### Q1: Concurrent task handling on Ajna
**Recommendation**: ONE-AT-A-TIME with queue. OpenClaw processes tasks sequentially via its Gateway. Add a simple FIFO queue to `watch_dispatch.sh` — tasks claimed in creation order. Backpressure = additional tasks wait in INBOX0.

### Q2: Psyche topology
**Confirmed**: Psyche runs on MacBook Air. Cross-machine dispatch uses the filesystem (Dropbox/iCloud sync or Tailscale SCP). For reliability, prefer Tailscale (already installed on both machines via App Store) over filesystem sync to avoid race conditions (see Q8).

### Q3: Web platform integration
**Recommendation**: Web agents (Manus, Perplexity Deep Research) remain MANUAL workflows dispatched by the Sovereign. They are NOT part of the filesystem-kanban dispatch system. Rationale: web platforms don't have filesystem access and would require custom API bridges (Level 4 on the cheap-first ladder). Not worth it yet.

### Q4: Cost-aware model routing
**Recommendation**: DEFERRED. The current model assignments (Opus for Commander, o3 for Adjudicator, Gemini 2.5 Pro for Cartographer) are correct defaults. Cost-aware routing adds complexity without clear ROI at current scale. Revisit when token budgets become a constraint.

### Q5: Sovereign escalation rules
**Recommendation**: Implement 3-tier escalation:
1. **PROCEED** — agent can proceed autonomously: file operations, formatting, tests, linting
2. **NOTIFY** — agent proceeds but writes to `-SOVEREIGN/` queue: architectural decisions, dependency changes, deletions in PROTECTED zones
3. **BLOCK** — agent must wait for Sovereign: any operation touching `canon/`, account credentials, external API calls, git push

### Q6: Intention Compass ↔ Ledger sync
**Recommendation**: MANUAL reconciliation on a weekly cadence. Automate only if the manual process reveals consistent pain. The Intent Compass captures signals; the Ledger captures execution. They converge at the WEEKLY REVIEW, not at the automation layer.

### Q7: State compaction policy
**Already addressed**: `compact_wisdom.sh` fires at threshold=10 entries. This is correct. Add a cron job or launchd plist to check threshold weekly. DYN-EXECUTION_STAGING.md → ARCH-EXECUTION_HISTORY.md archival is the designed path.

### Q8: Cross-machine race conditions
**Recommendation**: Use Tailscale for Psyche dispatch (direct SCP, not filesystem sync). For shared paths, implement flock-style file locking on TASK file claim:
```bash
# In watch_dispatch.sh
flock -n "$TASK_FILE.lock" mv "$TASK_FILE" "$PROCESSING_DIR/" || echo "Already claimed"
```
This prevents both machines from claiming the same task.

---

## VII. IMPLEMENTATION SEQUENCE

Priority ordered by value and dependency:

| Phase | Layer | What | Effort | Dependency |
|-------|-------|------|--------|------------|
| **0** | Tmux | Run `prefix+I` to install plugins, test cockpit.sh | 5 min | Sovereign interactive |
| **1** | Editor | LazyVim + Prose Engine + Agent Pipe | Medium | Neovim installed ✓ |
| **2** | Voice | Piper TTS + Whisper pipeline + sox DSP | Medium | whisper-cpp ✓, sox ✓ |
| **3** | Dashboard | Doom Emacs + Org Mode + state rendering | Large | None |
| **4** | Integration | Agent Pipe ↔ tmux ↔ cockpit.sh glue | Small | Phase 1 + tmux |
| **5** | Personas | DSP voice profiles per constellation agent | Small | Phase 2 |

**The swarm is handling Phases 1-3 now.**

---

## VIII. NEW ARTIFACTS CREATED

| Artifact | Purpose |
|----------|---------|
| This document | Architectural evaluation + Q&A resolution |
| LazyVim config (`~/.config/nvim/`) | Prose Engine (swarm) |
| Piper + pipeline scripts | Voice Layer (swarm) |
| Doom Emacs config | Dashboard Layer (swarm) |
| Agent Pipe plugin | Editor→Agent bridge (swarm) |

---

## IX. DECISION ATOMS (for Sovereign ratification)

1. **DEC-COCKPIT-001**: Neovim/LazyVim is the Prose Engine. Emacs is the Dashboard. Cursor is a Simulator. No overlap.
2. **DEC-COCKPIT-002**: Voice Layer is Phase 3 (after tmux + Neovim fluency). Install now, adopt later.
3. **DEC-COCKPIT-003**: Emacs scope is ABSOLUTE: Org Mode dashboard, read-only. No code editing.
4. **DEC-COCKPIT-004**: 8 constellation questions answered per Section VI. Sovereign ratification required.
5. **DEC-COCKPIT-005**: Cursor disposition changes from SUNSET to ACTIVE-SIMULATOR.
6. **DEC-COCKPIT-006**: Tailscale is the cross-machine transport for Psyche dispatch. Not filesystem sync.

---

*"The Cockpit is not a terminal — it's an instrument panel. Every surface shows one thing. Every action has one path. The Sovereign does not context-switch; the Sovereign FLIES."*
