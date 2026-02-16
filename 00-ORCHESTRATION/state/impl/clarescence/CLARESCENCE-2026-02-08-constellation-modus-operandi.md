# CLARESCENCE: 4-Agent Always-On Cockpit Architecture (Constellation Modus Operandi)

**Topic**: Aspirational agent architecture -- 4-agent always-on cockpit where each agent runs a continuous clarescence-driven operational loop
**Fidelity**: Full (Passes 1-10)
**Passes Run**: 1-10
**Date**: 2026-02-08
**Authority**: Commander / Sovereign directive
**Source Documents**: `COCKPIT.md`, `ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md`, `ARCH-INTENTION_COMPASS.md`, `REF-NEO_BLITZKRIEG_BUILDOUT.md`, `REF-FLEET_COMMANDERS_HANDBOOK.md`, `watch_dispatch.sh`, `dispatch.sh`, launchd plist inventory

---

## Pass 1: Triumvirate Calibration

### Destination / Why Now

The Sovereign's stated intention (INT-1202: "capitalize on these heavy machinery to construct as much of Syncrescendence") demands maximum concurrent utilization of all available CLI agents. The 4-agent always-on cockpit is the operational embodiment of INT-P006 ("multi-agent 90.2% outperforms single-agent") and INT-1203 ("design/architect for 3 Claude + 1 Gemini + 1 ChatGPT paid"). The architecture transforms the cockpit from a manually-invoked workspace into a self-sustaining nervous system that works between Sovereign interactions.

The timing is structurally correct: the 8-layer Sovereign Cockpit is STRUCTURALLY COMPLETE (PROJ-003 at 85%), launchd watchers are ACTIVE for all 6 agents (commander, adjudicator, cartographer, psyche, ajna, canon), `dispatch.sh` and `watch_dispatch.sh` are production-ready with bidirectional feedback, and ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md has already codified the target-state behavior.

### Current State / What's Broken

The gap is between the *infrastructure* (which exists) and the *operational loop* (which does not yet run autonomously). Specifically:

1. **Watchers are passive**: The launchd plists run `watch_dispatch.sh` for each agent, but agents only execute when a TASK file lands in their inbox. There is no self-initiating work-seeking behavior.
2. **No persistent agent sessions**: The architecture describes always-on CLI sessions (Ajna in pane 1, Commander in pane 3, etc.), but the watchers spawn one-shot CLI invocations per task, not persistent sessions.
3. **Clarescence cycle is documented but not automated**: The 7-phase cycle exists in ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md as prose, not as executable logic.
4. **Proactive awareness is entirely aspirational**: Phase 6 of the cycle (staleness detection, autophagy, drift monitoring) has no implementation.
5. **Cockpit script (`cockpit.sh`) activation pending**: The 19-minute activation referenced in REINIT-COMMANDER-2026-02-08.md has not been executed.

### Fit-to-Destination Verdict

The architecture is **structurally sound and directionally correct**. The design is the natural evolution of the Neo-Blitzkrieg pattern into a persistent-loop model. The gap is not architectural -- it is operational. The distance from current state to always-on is a series of activation steps, not a redesign.

---

## Pass 2: 18+ Lenses Scorecard

| # | Lens | Pass/Fail | Notes |
|---|------|-----------|-------|
| 1 | Bitter Lesson | PASS | Relies on scaling compute (4 concurrent LLM agents), not hand-crafting rules |
| 2 | Repo Sovereignty | PASS | All agent state flows through git; filesystem-kanban is git-trackable |
| 3 | Deletability | PASS | Agents are stateless except repo; any session can be killed without state loss |
| 4 | Translation Layer | WARN | TASK/CONFIRM/RESULT protocol is clear, but proactive work-seeking has no defined output format |
| 5 | Receipts | PASS | `watch_dispatch.sh` writes RESULT-*, CONFIRM-*, EXECLOG-* deterministically |
| 6 | Context Economics | WARN | 4 concurrent agents will compete for context on the same repo; no token budget coordination |
| 7 | Flat Principle | PASS | Inbox structure is flat per agent with prefix-based kanban (00-INBOX0, 10-IN_PROGRESS, 40-DONE) |
| 8 | Atomic Updates | PASS | `mv` for atomic claim; `set_fields` for atomic header mutation |
| 9 | Verification | WARN | No automated verification that agents don't conflict on shared files |
| 10 | Commit Discipline | FAIL | 4 agents committing concurrently will create merge conflicts; no coordination protocol |
| 11 | Five Invariants | PASS | Architecture respects all five constitutional laws |
| 12 | Semantic Prefixes | PASS | Each agent commits with semantic prefixes per protocol |
| 13 | Delegation Assessment | PASS | Explicit role specialization: Commander=architect, Adjudicator=mechanical, Cartographer=survey |
| 14 | Energy State | WARN | Always-on means always-consuming; Claude Max/Pro rate limits will be hit |
| 15 | Medley Mode | PASS | Each agent operates from characteristic cognition, not homogenized prompts |
| 16 | Pedigree Protocol | PASS | INT-P007 honored; each agent maintains its own lineage |
| 17 | Temporal Intelligence | WARN | No cadence for refreshing agent configs as models/APIs change |
| 18 | Globe Before Trees | PASS | Architecture is holistic before granular |

**Score: 13/18 PASS, 5/18 WARN, 0/18 FAIL** (adjusted: 1 FAIL on lens 10)

The warnings cluster around concurrency safety and resource management -- the novel risks introduced by "always-on" that do not exist in the current dispatch-and-respond model.

---

## Pass 3: CANON Coherence

### What Canonical Docs Say

- **COCKPIT.md** defines the 4x2 grid layout, agent roles, and the state machine (CAPTURED > INTERPRETED > COMPILED > STAGED > COMMITTED).
- **ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md** defines the 7-phase clarescence cycle per agent with explicit boot sequences, hook inventories, and keybinding references.
- **CLAUDE.md** defines Commander's constitutional rules and hooks (5 active hooks, 8 active skills).
- **REF-NEO_BLITZKRIEG_BUILDOUT.md** defines the flow from Sovereign input through dispatch lanes.
- **REF-FLEET_COMMANDERS_HANDBOOK.md** defines the Medley-mode constellation philosophy.

### Where Reality Diverges

| Canonical Claim | Reality |
|-----------------|---------|
| "Agents don't wait for Sovereign input to begin work" (ARCH-COCKPIT_OPERATIONAL_PROTOCOL) | They do. Watchers only fire on inbox events, not proactively. |
| "Ajna: webchat/iMessage bridges" | OpenClaw iMessage bridge status unknown; no evidence of active bridge config |
| "Adjudicator: codex --full-auto" | `watch_dispatch.sh` invokes `codex exec` (one-shot), not a persistent `--full-auto` session |
| "Cartographer: gemini --yolo" | Watcher invokes `gemini -p` (one-shot), not a persistent session |
| "Psyche: Tailscale bridge" | BLOCKED -- Tailscale not configured on either machine |
| "Phase 6: Proactive Awareness hooks" | All marked [ASPIRATIONAL] in the protocol doc |
| "Bottom row: per-agent neovim editor piped upward" | `agent-pipe.lua` exists but requires tmux session to be active |
| "cockpit.sh activation" | Pending the 19-minute activation procedure |

The canonical documents are ahead of reality by approximately one activation sprint. The architecture is designed; the activation has not been performed.

---

## Pass 4: Omni-Qualities

### Omniscience Impact
The 4-agent model dramatically increases the system's ability to sense its own state. Cartographer provides corpus-wide awareness (1M+ context), Commander provides architectural understanding, Adjudicator provides quality metrics, and Ajna provides orchestration oversight. The architecture moves toward omniscience of the knowledge substrate.

**Risk**: Omniscience without coordination becomes cacophony. Four agents reading the same IMPLEMENTATION-MAP.md without a locking mechanism will produce four different assessments.

### Omnipresence Impact
Always-on means the system is present even when the Sovereign is absent. This is the first step toward autonomous operation -- the cockpit works overnight, between sessions, during commute.

**Risk**: Omnipresence without intentionality becomes busy-work. Agents need clear criteria for what constitutes "proactive work" versus "churning."

### Omnipotence Impact
Four agents operating in parallel multiply execution capacity by roughly 3-4x (accounting for coordination overhead). Combined with Neo-Blitzkrieg lanes, this approaches the Sovereign's stated goal of institutional-scale output from individual capability.

**Risk**: Omnipotence without guardrails becomes destruction. A full-auto agent with write access and no human review can corrupt the corpus in seconds.

### Omnibenevolence Impact
The architecture serves the Sovereign's intentions (INT-1202, INT-MI19) faithfully. Agent specialization ensures each contribution aligns with its characteristic cognition.

**Risk**: Minimal. The agents are tools, not adversaries.

---

## Pass 5: Five Faces Alignment

| Face | Alignment | Notes |
|------|-----------|-------|
| **Sensing** | HIGH | Cartographer (1M context surveys) + launchd watchers (filesystem events) + intent_compass.sh (prompt signals) |
| **Meaning** | MEDIUM | Agents execute but don't synthesize meaning across themselves; no inter-agent dialogue |
| **Intention** | HIGH | Intention Compass feeds all agents; P0-P3 prioritization is explicit |
| **Embodiment** | LOW | The architecture exists as docs and scripts, not as running processes; activation gap |
| **Harmony** | MEDIUM | Role specialization prevents overlap, but no concurrency coordination prevents conflict |

---

## Pass 6: Rosetta Precision

Key terms and their operational meanings in this context:

| Term | Clarified Meaning |
|------|-------------------|
| **Always-on** | launchd KeepAlive + tmux persistent sessions; NOT "infinite context" -- agents still have session boundaries |
| **Clarescence cycle** | 7-phase operational loop (orient/situate/calibrate/triage/execute/awareness/interaction); NOT the clarescence decision-analysis skill |
| **Proactive work-seeking** | Agent scans for unclaimed work in IMPLEMENTATION-MAP.md and INBOX without Sovereign prompting; NOT autonomous goal-generation |
| **Dispatch** | `dispatch.sh` creates a TASK file in an agent's inbox; NOT direct IPC between processes |
| **Hook** | Claude Code lifecycle event handler (Stop, PreCompact, UserPromptSubmit); NOT applicable to Codex/Gemini CLIs (they lack hook systems) |
| **Skill** | Claude Code `.claude/skills/*.md` invocable procedure; NOT applicable to Codex/Gemini CLIs |
| **Filesystem-kanban** | 00-INBOX0 > 10-IN_PROGRESS > 40-DONE flow via `mv`; the inter-agent communication bus |
| **Neo-Blitzkrieg** | Manual dispatch to parallel lanes with automated connective tissue; the predecessor to always-on |

**Term drift alert**: The user's description uses "7-phase claresce cycle" for all four agents, but only Commander has the hook infrastructure to implement it. Codex CLI and Gemini CLI have no equivalent of UserPromptSubmit or Stop hooks. For those agents, the "cycle" is actually "watcher fires > execute task > write result > wait." The 7-phase framing is aspirational for non-Commander agents.

---

## Pass 7: Backlog Coherence

### What This Unblocks

| Intention/Task | How This Unblocks It |
|----------------|---------------------|
| INT-1202 (heavy machinery velocity) | 4x parallel execution capacity |
| INT-P006 (multi-agent 90.2%) | Realizes the constellation pattern at full scale |
| INT-1203 (5-platform design) | 4 of 5 platforms are cockpit agents |
| PROJ-003 (Tooling Stack 85%) | Cockpit activation completes the remaining 15% |
| PROJ-006b (Ontology Substrate) | Unblocked once cockpit provides persistent corpus sensing |
| INT-MI19 (Palantir ontology) | Cartographer can run continuous corpus coherence audits |

### What This Creates

| New Dependency | Description |
|----------------|-------------|
| TASK-CONCURRENCY-PROTOCOL | Git merge conflict prevention for 4 concurrent committers |
| TASK-RATE-LIMIT-BUDGET | Token/API rate limit allocation across agents |
| TASK-PROACTIVE-CRITERIA | Definition of what "proactive work" means per agent |
| TASK-COCKPIT-ACTIVATION | The 19-minute activation procedure itself |
| TASK-AGENT-HEALTH-MONITOR | Mechanism to detect when an agent's watcher has crashed |

### Priority

This is **P1** work. It is the direct embodiment of the Sovereign's most active urgent intention (INT-1202) and represents the operational culmination of PROJ-003.

---

## Pass 8: nth-Order Effects

### What Breaks

1. **Git coordination**: Four agents committing to the same repo will produce merge conflicts. The filesystem-kanban prevents task collision, but agents may edit shared files (IMPLEMENTATION-MAP.md, DYN-EXECUTION_STAGING.md, DYN-SESSION_LOG.md) simultaneously.

2. **Rate limits**: Claude Max provides ~45 messages/5hr for Opus. If Commander consumes this on proactive work, the Sovereign has no capacity left for interactive sessions. Codex CLI (Account 2, Claude Pro) has separate but lower limits.

3. **Watcher stability**: `watch_dispatch.sh` uses `fswatch` with `set -euo pipefail`. Any unhandled error kills the watcher. launchd's KeepAlive restarts it, but with ThrottleInterval=10s there is a gap.

4. **Disk I/O**: Four agents + four neovim instances + fswatch watchers on the same NVMe. Unlikely to be a bottleneck on M1 Mac mini, but worth monitoring.

5. **Cognitive coherence**: If Cartographer detects corpus drift and Adjudicator simultaneously "repairs" something, their fixes may conflict. There is no arbitration mechanism.

### What Compounds

1. **Execution velocity**: Once running, the system can process the entire IMPLEMENTATION-MAP backlog in parallel -- potentially clearing weeks of work in days.

2. **Corpus quality**: Continuous Cartographer sensing + Adjudicator quality passes creates a self-improving knowledge substrate.

3. **Session continuity**: Always-on means no cold-start penalty. Each session picks up where the last left off, with hooks maintaining pedigree.

4. **Automation learning**: Each cycle generates execution logs that feed into ARCH-EXECUTION_HISTORY.md, creating a growing corpus of operational patterns.

### New Dependencies

- A **lock file** or **branch-per-agent** strategy is required before concurrent committing is safe.
- A **rate limit dashboard** is needed to prevent accidental API exhaustion.
- A **proactive work queue** (distinct from dispatch) is needed so agents don't duplicate effort.

---

## Pass 9: Energy State

### Is This Sustainable to Implement Now?

**Partially.** The implementation decomposes into three tiers:

**Tier 1 -- Immediately executable (30 minutes Sovereign time):**
- Run `cockpit.sh` to activate the tmux 4x2 grid
- Start Commander in pane 3 (`claude --dangerously-skip-permissions`)
- Verify launchd watchers are running (`launchctl list | grep syncrescendence`)
- Test dispatch round-trip: Commander dispatches to Adjudicator, receives CONFIRM back

**Tier 2 -- Requires focused session (2-3 hours):**
- Configure persistent sessions for each agent in their respective panes
- Implement git branch-per-agent or file-lock protocol
- Define proactive work criteria per agent
- Set up rate limit monitoring (even a simple `~/.claude/usage.log` tail)

**Tier 3 -- Aspirational (days/weeks):**
- Proactive awareness hooks (staleness detection, autophagy)
- Inter-agent dialogue (not just dispatch, but conversation)
- Psyche integration via Tailscale
- Self-healing constitution (meta-hook for anti-pattern learning)
- Agent-specific config update hooks (/updateClaudeConfig, etc.)

**Recommendation**: Execute Tier 1 today. Schedule Tier 2 for the next focused session. Defer Tier 3 until Tier 2 is stable.

---

## Pass 10: Authenticity Gate

### Preserves Sovereignty + Optionality?

**Yes.** The architecture explicitly preserves Sovereign authority:
- Agents execute from the Intention Compass, not from self-generated goals
- The Sovereign can kill any agent with `prefix+X` (emergency stop)
- All agent output flows through git, which the Sovereign controls
- Proactive work-seeking is bounded by IMPLEMENTATION-MAP, not unbounded exploration
- Each agent's plist can be individually unloaded (`launchctl bootout`) without affecting others

**Optionality preserved**: The architecture is additive. Running 4 agents does not prevent running 1. Any agent can be disabled. The Sovereign can revert to manual dispatch at any time.

### Sovereign-at-Peak-Clarity Approved?

The Sovereign's own words justify this architecture:
- INT-1202: "capitalize on these heavy machinery"
- INT-P006: "multi-agent 90.2% outperforms single-agent"
- INT-C007: "chunk work into parallel sessions, stop sequential single-terminal habits"

The architecture is a direct translation of expressed sovereign intent into operational infrastructure.

---

## Structural Coherence Analysis: The Loop Design

### What Works

The 7-phase cycle (orient > situate > calibrate > triage > execute+document > awareness > sovereign interaction) is a well-structured OODA-adjacent loop. Its strengths:

1. **Orient before execute**: Agents read their inbox and the Intention Compass before doing anything. This prevents stale-context execution.
2. **Triage is explicit**: P0 > P1 > P2 > P3 ordering prevents agents from cherry-picking easy work.
3. **Execute+Document is atomic**: Writing the execution log alongside the work prevents the "I did the work but forgot to document it" failure mode.
4. **Hooks fire post-completion**: Session logs, pedigree, and execution staging happen automatically at the Stop event.

### What Needs Refinement

1. **The "proactive awareness" phase has no trigger**: In a dispatch-driven model, the loop runs when a TASK arrives. In a proactive model, something must trigger the agent to look for work. The loop design does not specify what happens when there are no TASKs -- does the agent sleep? Poll? Scan IMPLEMENTATION-MAP every N minutes?

2. **Calibrate vs Situate overlap**: Both phases involve reading state files. The distinction ("Situate = what is the repo state" vs "Calibrate = what should I work on") is conceptually clean but operationally redundant for non-Commander agents that don't have Plan Mode.

3. **The loop's REPEAT mechanism is underspecified**: "Continuous loop" could mean (a) poll every 10 seconds, (b) fswatch event-driven, or (c) persistent CLI session that accepts new prompts. These have radically different resource profiles.

### Recommendation

Define three loop modes:
- **DISPATCH mode** (current): Watcher fires on inbox events. Agent executes one task, writes result, returns to sleep.
- **SESSION mode** (target): Persistent CLI session in tmux pane. Agent maintains context across tasks. Loop is driven by Sovereign prompts + inbox events.
- **PROACTIVE mode** (aspirational): Agent periodically scans IMPLEMENTATION-MAP for unclaimed work and self-dispatches. Requires rate-limit awareness.

Start with DISPATCH mode (already working), layer SESSION mode via cockpit activation, and add PROACTIVE mode only after concurrency safety is proven.

---

## Hooks vs Skills vs Human-Triggered Commands

### Decision Framework

| Mechanism | When to Use | Examples |
|-----------|-------------|---------|
| **Hook** (automatic) | Lifecycle events that should ALWAYS fire, regardless of task type | `session_log.sh` on Stop, `intent_compass.sh` on UserPromptSubmit, `pre_compaction.sh` on PreCompact |
| **Skill** (invocable) | Complex procedures that require agent judgment about WHEN and HOW to apply them | `/claresce`, `/pedigree`, `/integrate`, `/readize` |
| **Command** (human-triggered) | Multi-step workflows where the Sovereign wants explicit control over initiation | `/project:blitzkrieg`, `/project:verify`, `/project:repo_validate` |
| **Watcher** (background) | File-system events that should trigger processing without any session being active | `watch_dispatch.sh` (launchd), `watch_canon.sh` (launchd) |

### Platform-Specific Applicability

| Mechanism | Commander (Claude Code) | Adjudicator (Codex CLI) | Cartographer (Gemini CLI) | Ajna (OpenClaw) |
|-----------|------------------------|------------------------|--------------------------|-----------------|
| Hooks | FULL SUPPORT (5 active) | NO SUPPORT (Codex has no hook system) | NO SUPPORT (Gemini has no hook system) | PARTIAL (OpenClaw has HEARTBEAT, no lifecycle hooks) |
| Skills | FULL SUPPORT (8 active) | NO SUPPORT | NO SUPPORT | PARTIAL (OpenClaw has skill files) |
| Commands | FULL SUPPORT | NO SUPPORT | NO SUPPORT | PARTIAL |
| Watchers | ACTIVE (launchd) | ACTIVE (launchd) | ACTIVE (launchd) | ACTIVE (launchd) |

**Critical insight**: The 7-phase clarescence cycle's hook-driven post-task behavior (execution log, pedigree, memory update) is only mechanically supported by Commander and partially by Ajna. For Adjudicator and Cartographer, these phases must be implemented as part of the watcher script itself -- `watch_dispatch.sh` must write the execution log, not a hook that fires on Stop.

### Recommendations

1. **Enhance `watch_dispatch.sh`** to perform post-task documentation for hook-less agents (Adjudicator, Cartographer). After `run_executor` completes, the watcher should append to `DYN-EXECUTION_STAGING.md`.
2. **Keep hooks for Commander only**. Do not try to simulate hooks for other CLIs.
3. **Implement `/claresce` as a skill** for Commander. For other agents, embed claresce-like behavior in the TASK file's instructions.
4. **Proactive awareness should be a watcher-level feature**, not a hook. Add a cron-like scan to `watch_dispatch.sh` that periodically reads IMPLEMENTATION-MAP.md and self-dispatches unclaimed P1/P0 items.

---

## Dependency Graph Between Agents

```
                    SOVEREIGN
                       |
                       v
                 ┌─────────┐
                 │  AJNA    │ (Orchestrator)
                 │ Opus 4.5 │
                 └────┬────┘
                      |
          ┌───────────┼───────────┐
          v           v           v
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │COMMANDER │ │ADJUDICATOR│ │CARTOGR.  │
    │ Opus 4.6 │ │ Sonnet   │ │Gemini 2.5│
    └────┬─────┘ └────┬─────┘ └────┬─────┘
         |            |            |
         └────────────┼────────────┘
                      |
                      v
                 REPOSITORY
                 (ground truth)
```

### Dependency Types

| From | To | Type | Mechanism |
|------|----|------|-----------|
| Sovereign | Ajna | Direct input | Conversation, -INBOX dispatch |
| Sovereign | Commander | Direct input | Conversation, -INBOX dispatch |
| Ajna | Commander | Task dispatch | `dispatch.sh` > TASK file |
| Ajna | Adjudicator | Task dispatch | `dispatch.sh` > TASK file |
| Ajna | Cartographer | Task dispatch | `dispatch.sh` > TASK file |
| Commander | Adjudicator | Task dispatch | `dispatch.sh` > TASK file (mechanical work) |
| Commander | Cartographer | Task dispatch | `dispatch.sh` > TASK file (corpus surveys) |
| Adjudicator | Commander | Result reply | CONFIRM-* / RESULT-* files |
| Cartographer | Commander | Result reply | CONFIRM-* / RESULT-* files |
| All agents | Repository | Git commits | `git add && git commit && git push` |

### Critical Dependencies

1. **Commander is the hub**: Most work flows through Commander. If Commander's rate limit is exhausted, the entire system stalls.
2. **Ajna is the meta-orchestrator**: Ajna can dispatch to all agents but depends on OpenClaw's session stability.
3. **Adjudicator and Cartographer are leaf nodes**: They receive work and return results. They do not dispatch to others.
4. **No agent depends on Psyche**: Psyche is BLOCKED pending Tailscale. The architecture is fully functional without her.

---

## Immediately Implementable vs Aspirational

### Immediately Implementable (Today)

| Item | Effort | Dependency |
|------|--------|------------|
| Run `cockpit.sh` to activate tmux grid | 5 min | None |
| Start Commander session in pane 3 | 2 min | cockpit.sh |
| Verify all 6 launchd watchers are loaded and running | 5 min | None |
| Test dispatch round-trip (Commander > Adjudicator > CONFIRM back) | 10 min | Watchers running |
| Test dispatch round-trip (Commander > Cartographer > CONFIRM back) | 10 min | Watchers running, Gemini API key |

### Short-Term (This Week)

| Item | Effort | Dependency |
|------|--------|------------|
| Define git concurrency protocol (branch-per-agent or file-lock) | 1 hr | Architectural decision |
| Enhance `watch_dispatch.sh` with post-task execution logging | 1 hr | None |
| Define proactive work criteria per agent | 1 hr | IMPLEMENTATION-MAP review |
| Set up rate limit monitoring for Claude Max | 30 min | None |
| Configure Ajna persistent session in pane 1 | 30 min | cockpit.sh, OpenClaw config |

### Aspirational (Weeks/Months)

| Item | Effort | Dependency |
|------|--------|------------|
| Proactive work-seeking (IMPLEMENTATION-MAP scan) | 2-4 hrs | Concurrency protocol |
| Inter-agent dialogue (not just dispatch) | 4-8 hrs | Protocol design |
| Psyche integration via Tailscale | 70 min + config | Tailscale setup on both machines |
| Self-healing constitution (meta-hook) | 4-8 hrs | Pattern corpus |
| Agent-specific config update hooks | 2-4 hrs each | Per-platform research |
| Staleness detection + autophagy | 4-8 hrs | Cartographer proactive mode |
| Session budgeting (token tracking) | 2-4 hrs | API usage logging |

---

## Critical Path to Always-On

```
1. Activate cockpit.sh (tmux 4x2 grid)
   |
2. Verify launchd watchers (all 6 agents)
   |
3. Start Commander persistent session (pane 3)
   |
4. Test dispatch round-trip (Commander <-> Adjudicator)
   |
5. Define git concurrency protocol
   |  ┌─────────────────────────────────────┐
   |  │ DECISION REQUIRED: Which strategy?  │
   |  │ A) Branch-per-agent (safe, complex) │
   |  │ B) File-lock (simple, fragile)      │
   |  │ C) Zone ownership (pragmatic)       │
   |  └─────────────────────────────────────┘
   |
6. Start Adjudicator persistent session (pane 5)
   |
7. Start Cartographer persistent session (pane 7)
   |
8. Start Ajna persistent session (pane 1)
   |
9. Define proactive work criteria
   |
10. Enable proactive scan in watch_dispatch.sh
    |
    ALWAYS-ON ACHIEVED (4 agents in continuous loop)
```

**Bottleneck**: Step 5 (git concurrency protocol) is the gate. Without it, steps 6-10 risk data corruption.

**Recommended concurrency strategy**: **Zone ownership** (option C). Each agent owns specific file patterns:

| Agent | Owned Zones | Shared (Read-Only) |
|-------|-------------|---------------------|
| Commander | 00-ORCHESTRATION/state/, 01-CANON/, -SOVEREIGN/ | IMPLEMENTATION-MAP.md, COCKPIT.md |
| Adjudicator | Test files, formatting passes, -INBOX/adjudicator/ | 01-CANON/ (read), 02-ENGINE/ (read) |
| Cartographer | 05-SIGMA/, survey reports, -INBOX/cartographer/ | 01-CANON/ (read), 02-ENGINE/ (read) |
| Ajna | -INBOX/ajna/, DYN-PEDIGREE_LOG.md | All (orchestration read) |

Shared mutable files (DYN-EXECUTION_STAGING.md, DYN-SESSION_LOG.md) should use append-only semantics with agent-prefixed entries, or be split into per-agent files that compact periodically.

---

## Risk Analysis: 4 Concurrent Agents on the Same Repo

### Risk 1: Git Merge Conflicts (SEVERITY: HIGH)

**Scenario**: Commander edits IMPLEMENTATION-MAP.md to mark a task done. Simultaneously, Cartographer edits it to add a survey finding.
**Mitigation**: Zone ownership + append-only shared files. If both must write to the same file, use per-agent staging files (e.g., `DYN-EXECUTION_STAGING-commander.md`) that compact offline.
**Residual risk**: LOW after mitigation.

### Risk 2: Rate Limit Exhaustion (SEVERITY: HIGH)

**Scenario**: Commander processes 3 proactive tasks. Sovereign arrives and cannot use Commander because daily limit is hit.
**Mitigation**: Reserve 50% of daily capacity for Sovereign interactive use. Proactive work uses the remaining 50%. Monitor via `~/.claude/usage.log` or API dashboard. Offload mechanical work to Adjudicator (Account 2, separate limits).
**Residual risk**: MEDIUM. Proactive work is inherently unpredictable in token consumption.

### Risk 3: Watcher Crash Loop (SEVERITY: MEDIUM)

**Scenario**: `watch_dispatch.sh` encounters an error (e.g., malformed TASK file, missing `python3`). `set -euo pipefail` kills the process. launchd restarts it. Same error. Crash loop with ThrottleInterval=10s.
**Mitigation**: Add error handling around `handle_file` that catches and logs errors without killing the process. Move malformed TASK files to `50_FAILED/` with an error annotation.
**Residual risk**: LOW after mitigation.

### Risk 4: Stale Context (SEVERITY: MEDIUM)

**Scenario**: Commander dispatches a task to Adjudicator based on a file state that Cartographer has already modified. Adjudicator executes against stale context.
**Mitigation**: Every TASK file includes a fingerprint (`git rev-parse --short HEAD`). Agent verifies fingerprint before execution. If fingerprint has changed, re-read context.
**Residual risk**: LOW. The fingerprint check is already in the protocol.

### Risk 5: Runaway Agent (SEVERITY: HIGH)

**Scenario**: Codex CLI in `--full-auto` mode makes a destructive change (deletes a CANON file, overwrites a state file).
**Mitigation**: Zone ownership limits write scope. Additionally, `AGENTS.md` should explicitly list prohibited paths. Git provides rollback via `git revert`. Consider running Adjudicator without `--full-auto` initially.
**Residual risk**: MEDIUM. Even with zone ownership, a misconfigured agent can damage its own zone.

### Risk 6: Coordination Deadlock (SEVERITY: LOW)

**Scenario**: Commander dispatches to Adjudicator, who dispatches back to Commander with a question. Commander's watcher claims the question as a new task. Infinite loop.
**Mitigation**: The CONFIRM/RESULT protocol already differentiates replies from new tasks. Watchers skip CONFIRM-* and RESULT-* files. However, ensure no agent dispatches new TASKs in response to a CONFIRM -- only the Sovereign or Ajna (orchestrator) should create new TASKs from results.
**Residual risk**: LOW.

### Risk 7: Resource Contention (SEVERITY: LOW)

**Scenario**: Four LLM CLIs + four neovim instances + fswatch watchers consume excessive RAM/CPU on M1 Mac mini (16GB RAM).
**Mitigation**: M1 Mac mini with 16GB should handle this. Claude Code ~200MB, Codex CLI ~150MB, Gemini CLI ~100MB, OpenClaw ~200MB, 4x neovim ~400MB total. Well within budget. Monitor with `htop`.
**Residual risk**: LOW.

---

## Relationship to Neo-Blitzkrieg Architecture

The 4-agent always-on cockpit is **Neo-Blitzkrieg v2.0**. The evolution:

| Aspect | Blitzkrieg v1.0 | Neo-Blitzkrieg v1.0 | Always-On Cockpit (v2.0) |
|--------|----------------|---------------------|--------------------------|
| **Trigger** | Sovereign crafts directives manually | Sovereign input + hook automation | Sovereign input + proactive self-dispatch |
| **Dispatch** | Copy-paste to platforms | `dispatch.sh` + watcher | Persistent sessions + filesystem-kanban + proactive scan |
| **Execution** | Sequential per platform | Parallel lanes (A/B/C/D) | Continuous loops per agent |
| **Return** | Manual collection | CONFIRM/RESULT protocol | Automatic bidirectional feedback + CC piping |
| **Persistence** | Per-session | Per-session + hooks | Always-on tmux sessions + launchd watchers |
| **Coordination** | None (Sovereign manages) | Hub-spoke (Commander manages) | Hub-spoke + orchestrator (Ajna manages) |

The key architectural advancement is the shift from **event-driven** (dispatch fires execution) to **loop-driven** (agents continuously seek and execute work). The filesystem-kanban remains the communication bus, but the agents are no longer passive receivers -- they are active participants.

**Compatibility**: The always-on cockpit is backward-compatible with Neo-Blitzkrieg v1.0. Manual dispatch still works. Hooks still fire. The new loop behavior is additive. The Sovereign can use the cockpit in v1.0 mode (manual dispatch) while gradually enabling v2.0 features (proactive scan, persistent sessions).

---

## Recommendations for Phased Implementation

### Phase 0: Activation (Today -- 30 minutes)

**Objective**: Get the cockpit physically running.

1. Execute `cockpit.sh` to create the tmux 4x2 grid
2. Start Commander in pane 3: `claude --dangerously-skip-permissions`
3. Verify launchd watchers: `launchctl list | grep syncrescendence`
4. Test one dispatch round-trip: Commander dispatches a trivial task to Adjudicator
5. Verify CONFIRM arrives back in Commander's inbox

**Exit criteria**: Commander is in a persistent session. At least one dispatch round-trip completes successfully.

### Phase 1: Concurrency Safety (This week -- 2-3 hours)

**Objective**: Make it safe for multiple agents to operate on the same repo.

1. Implement zone ownership map (codify in `ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md`)
2. Split shared mutable files into per-agent staging files
3. Add fingerprint verification to `watch_dispatch.sh` pre-execution
4. Add error handling to `watch_dispatch.sh` to prevent crash loops
5. Test: Commander and Adjudicator both commit within 60 seconds -- verify no conflicts

**Exit criteria**: Two agents can operate concurrently for 1 hour without merge conflicts.

### Phase 2: Persistent Sessions (Next week -- 2-3 hours)

**Objective**: All four agents running in their tmux panes with persistent context.

1. Configure Adjudicator persistent session in pane 5 (Codex CLI)
2. Configure Cartographer persistent session in pane 7 (Gemini CLI)
3. Configure Ajna persistent session in pane 1 (OpenClaw)
4. Set up neovim agent-pipe in panes 2/4/6/8
5. Test: Visual-select text in pane 4 (Commander's editor), pipe to Adjudicator (pane 5)

**Exit criteria**: All 4 agents running in persistent sessions. Agent-pipe working for at least Commander > Adjudicator.

### Phase 3: Proactive Operations (Week 3+ -- 4-6 hours)

**Objective**: Agents seek work without Sovereign prompting.

1. Define proactive work criteria per agent (what tasks can be self-claimed)
2. Add IMPLEMENTATION-MAP scanner to `watch_dispatch.sh`
3. Implement rate limit reservation (50% proactive, 50% Sovereign)
4. Add agent health monitoring (detect watcher crashes, report to Ajna)
5. Test: Leave cockpit running for 4 hours. Verify agents completed work. Verify no corruption.

**Exit criteria**: At least one agent completes a self-dispatched task without Sovereign intervention.

### Phase 4: Refinement (Ongoing)

**Objective**: Continuous improvement of the always-on system.

1. Implement post-task hooks for non-Commander agents (in watch_dispatch.sh)
2. Add Psyche integration when Tailscale is ready
3. Build inter-agent dialogue capability (not just dispatch)
4. Implement staleness detection + autophagy for Cartographer
5. Build the `/conductReviewtrospective` skill
6. Build session budgeting and token tracking

**Exit criteria**: The cockpit runs autonomously for 8+ hours, completing work, maintaining quality, and staying within rate limits.

---

## Convergent Path

The single best path forward is: **Activate the cockpit in DISPATCH mode today, layer concurrency safety this week, enable persistent sessions next week, and add proactive operations only after concurrency is proven safe.**

Do not attempt to implement the full 7-phase clarescence cycle for all agents simultaneously. Commander is the only agent with the hook infrastructure to support it. The other agents should run in simplified dispatch-execute-report loops, with their "clarescence" behavior embedded in the TASK instructions rather than in agent-level automation.

The always-on cockpit is achievable. It is not a leap -- it is a series of 30-minute activation steps gated by one critical architectural decision (concurrency strategy).

---

## Summary Block

```
CLARESCENCE: 4-Agent Always-On Cockpit Architecture
Fidelity: Full
Passes run: 1-10
Convergent Path: Activate in DISPATCH mode (today) > concurrency safety (this week) >
                 persistent sessions (next week) > proactive operations (week 3+)
Rationale (digest):
  - Infrastructure exists: 6 launchd watchers, dispatch.sh, watch_dispatch.sh, filesystem-kanban
  - Gap is activation, not architecture: cockpit.sh has not been run
  - Git concurrency is the critical gate: 4 agents committing without coordination will corrupt
  - Zone ownership is the pragmatic concurrency strategy: each agent owns file patterns
  - Hooks only work for Commander: other agents need watcher-level post-task documentation
  - Rate limits are the economic constraint: reserve 50% capacity for Sovereign interactive use
  - Proactive work-seeking is Tier 3: defer until concurrency and persistence are stable
Dependencies created/updated:
  - TASK-CONCURRENCY-PROTOCOL (new, P1)
  - TASK-COCKPIT-ACTIVATION (new, P0)
  - TASK-RATE-LIMIT-BUDGET (new, P2)
  - TASK-PROACTIVE-CRITERIA (new, P2)
  - TASK-AGENT-HEALTH-MONITOR (new, P3)
Falsifier: If Claude Code, Codex CLI, or Gemini CLI cannot maintain persistent sessions
           in tmux panes (e.g., they timeout, crash, or refuse non-interactive input),
           the persistent-session model fails and the architecture reverts to dispatch-only.
Confidence: HIGH for Phases 0-2, MEDIUM for Phases 3-4
```

---

**END CLARESCENCE-2026-02-08-constellation-modus-operandi.md**
