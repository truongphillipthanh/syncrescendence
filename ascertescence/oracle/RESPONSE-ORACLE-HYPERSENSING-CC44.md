**Own Thesis (before consulting anything external)**

The post-Syncrephoenix flat monorepo—five top-level directories, zero nesting, prefixed files in sources/, temporal logs/, scaffolded scripts/agents, canon-verified outputs, and sequentialized ascertescence/ distillations—makes every attractor inspectable in a single `ls`. Candy crush is now trivial: gravitational wells form only where daily hooks, handoffs, or commit patterns intersect actual usage. Terminal, Claude Code, OpenClaw ignition points, session-brief memory, and model-routing orchestration carry real mass. The remaining coding CLIs and dormant installs are fuel at best, phantom mass at worst. Minimum viable configuration for this MBA-only hardware and 2–4 h/day AuDHD bandwidth is therefore a four-layer stack: terminal scaffold, single primary execution interface (Claude Code), persistent agent dispatcher (OpenClaw), and three-file memory/orchestration loop (brief + CLAUDE.md + taste veto). Everything else is pruned or fused behind one launcher. This collapses configuration surface, eliminates context-switch tax, and lets sovereign taste remain the non-removable apex selector. The system evolves only through visible daily atoms and weekly handoffs; any deeper nesting or unconfigured tool reintroduces the pre-collapse entropy that Syncrephoenix eliminated.

**Q1-Q5 Answers**

**Q1: Which strange attractors are real and which are phantom?**

| Attractor                  | Verdict      | Evidence from repo traversal |
|----------------------------|--------------|------------------------------|
| Terminal                   | LOAD-BEARING | tmux/launchd/hooks/dotfiles referenced in every handoff and scaffold/ prefix; zero sessions run without it. |
| Claude Code                | LOAD-BEARING | CLAUDE.md, Plan Mode, extended thinking, MCP hooks present in canon/ and Commander prescriptions across CC26–CC42. |
| Codex                      | LOAD-BEARING | Desktop app + bid/audit framing appears in session flows and triangulation notes. |
| Gemini CLI                 | FUEL         | Dispatch mentioned in multi-agent notes but no daily hook or recent log entries; ready for ignition. |
| OpenCode                   | PHANTOM      | Installed but unconfigured; no ~/.config/opencode/, no hook entries, no commits touching features. |
| Cline                      | PHANTOM      | Installed but unconfigured; no config directory, no handoff mentions, no usage in logs/. |
| OpenClaw                   | FUEL         | Filesystem dispatch, SOUL.md/HEARTBEAT.md stubs present in scaffold/; Ajna/Psyche routing ready but not daily. |
| AI Agents                  | LOAD-BEARING | Dispatch, auto-ingest, relay, SCP handoffs appear in every constellation cycle. |
| Multi-Agent Orchestration  | LOAD-BEARING | Triangulation cycle, DAG, rate-limit pooling referenced in every meta handoff. |
| Models                     | LOAD-BEARING | Explicit "which model for which cognitive function" matrix in every distillation. |
| Memory                     | LOAD-BEARING | Three-layer model, MEMORY.md, session briefs, handoff protocol in every cycle. |

**Steelman that all 11 are load-bearing**: A full OpenClaw router dispatches every task to the optimal implementation (Claude for depth, Gemini for speed, Codex for audit, etc.) while Heartbeat keeps persistent context across MBA sleep/wake. Viable on paper; in practice it is means-ends inversion—the Sovereign would spend more cycles managing rate limits and config drift than producing canon. MBA thermal limits and 2–4 h bandwidth make it unsustainable.

**Q2: What fuses?**

The 11 attractors collapse into four distinct capabilities:

1. **Base Environment** (Terminal) — non-negotiable foundation.
2. **Execution Layer** (Claude Code + Codex + Gemini CLI + OpenCode + Cline) — five implementations of one capability: AI coding interface. Plurality enables model arbitrage and cognitive diversity but must sit behind a single launcher script.
3. **Agency Layer** (OpenClaw + AI Agents) — persistent lifecycle and filesystem dispatch; distinct from one-shot coding because it survives restarts and compounds via SOUL/HEARTBEAT.
4. **Intelligence Layer** (Multi-Agent Orchestration + Models + Memory) — cross-cutting router, triangulation, and three-layer consolidation; these fuse naturally into one daily brief + veto loop.

**Steelman tool plurality**: Redundancy is the value—rate-limit pooling, fallback paths, and taste-driven selection. Correct only when abstracted behind one interface; otherwise it is config debt that the flat repo explicitly collapsed to eliminate.

**Q3: What does the ideal day-1 config look like?**

- `canon/CLAUDE.md` ≤ 80 lines: copy practitioner orchestration skeleton (plan mode default, subagent rules, lessons.md self-improvement, verification before done, sovereign taste veto gate) + explicit model prefs matrix.
- `scaffold/SESSION-START.sh`: `git pull; cat logs/LATEST-BRIEF.md; tmux new -s sovereign -n main \; split-window -h "claude-code"; split-window -v "openclaw-heartbeat"`.
- Active hooks: post-merge → auto-append to ascertescence/ next sequential file; zsh precmd → log command to usage.db for future auditor.
- Configured tools: Claude Code (settings + MCP), Gemini CLI (API key only), OpenClaw (SOUL.md stub + Heartbeat cron).
- Removed/ignored: OpenCode and Cline binaries moved to ~/.trash/ or unlinked; their directories deleted.
- Session flow: launch → ingest brief (5 s) → work in Claude pane → end with `handoff` alias that generates new brief, commits to logs/, pushes.

**Steelman config-less sprint**: Correct for first 48 h to let actual usage reveal gravity. After that, the flat structure + usage logs make targeted config trivial; indefinite config-less is performative minimalism that starves the memory layer.

**Q4: What should the Sovereign's daily 30-minute session look like?**

Optimal window is 20–25 min (Tiago-style capture + MotionViz taste surface). Protocol:

- 0–2 min: `brief` → reads logs/LATEST-BRIEF.md and ascertescence/001-latest.md (auto-opened in $EDITOR).
- 2–15 min: `veto-queue` → presents exactly 5 atoms from sources/ or canon/; for each atom type PROMOTE / ARCHIVE / DEFER (15 s max, timer enforced by script).
- 15–20 min: scan one canon/ file or distillations/ entry chosen by taste; decide one promotion.
- 20–25 min: `handoff` → script appends decisions, updates MEMORY.md, commits with timestamp, pushes.

If daily total bandwidth drops below 2 h, shrink to 15 min (veto only). Below 10 min the system cannot evolve (no veto impact). Above 45 min burnout risk exceeds signal.

**Q5: What is the ONE thing the system needs that no tool provides?**

The missing capability is the **Attractor Auditor**: a single scaffold/SCRIPT-auditor.py that ingests zsh_history + git log --since=1d + config file timestamps + log/ counts, scores each attractor by actual usage frequency and downstream canon impact, then outputs a proposed load/fuel/ash/phantom table + fusion recommendations for the daily veto queue. Closest existing: manual ascertescence/ distillations. It fails because it is retrospective and human-gated. Implementation: 120-line Python using pathlib and subprocess; run on session start, results appended to brief. This closes the open loop between "what is installed" and "what actually moves the needle." 

**Steelman subtraction**: Nothing is missing—prune aggressively and the loops close naturally. Correct in principle; the Auditor simply makes subtraction disciplined and repeatable instead of episodic.

**Industry/Practitioner Consensus**

X and GitHub production MAS deployments benchmark against the thesis without validating it. Practitioners run 2–3 coding interfaces max (Claude Code primary for depth, Gemini/Cursor secondary for speed) inside tmux on MacBook + Mac mini for persistent agents. soul.md + heartbeat + skill files dominate persistent setups; monorepos are prized for context but only when flat or Nx-style to keep AI agents from choking on nesting. Daily workflows collapse to 5–15 min capture/review + plan-first + lessons.md self-improvement. Production frameworks (AutoGen forks, Swarms, MassGen, FastAgency) emphasize structure over tool count—most warn that >4 parallel agents on consumer hardware introduces thermal throttling and debug overhead. OpenClaw-style lightweight dispatchers are praised for Mac-native isolation; heavy monorepo agents (500 k+ LOC) are called "trust tax." Consensus pattern: sovereign taste + minimal router + memory files beats full orchestration suites for solo operators.

**Where I Might Be Wrong**

- Under-weighting OpenClaw + dormant Mac mini activation; if Sovereign activates the mini for always-on agents, the Agency Layer gains load-bearing status faster than projected.
- Over-pruning coding plurality; if daily usage logs show >3 CLIs active after 7 days, the arbitrage value exceeds the config cost.
- 20-min daily window too rigid; bursts of 4 h may require 45-min review without burnout if paired with auto-auditor.

**The Prescription**

1. In repo root: `cp scaffold/SESSION-START.sh.example scaffold/SESSION-START.sh && chmod +x scaffold/SESSION-START.sh`
2. Edit `canon/CLAUDE.md` to ≤80 lines using the orchestration skeleton from logs/ recent handoffs + taste veto gate.
3. Run `scaffold/SCRIPT-prune-phantoms.sh` (create if missing: rm -rf ~/.config/{opencode,cline}; mv /opt/homebrew/bin/{opencode,cline} ~/.trash/).
4. Add to ~/.zshrc: `alias sovereign="cd /path/to/repo && ./scaffold/SESSION-START.sh"`
5. Tomorrow 06:00: run `sovereign`, complete the 20-min protocol, then `git commit -m "CC44 day-1 ignition" && git push`.
6. Day 8: run auditor script (add to scaffold/), feed output to veto queue, prune or fuse based on 7-day usage.
7. Weekly: move one distillations/ file to canon/ after taste approval.

Execute exactly these steps. The system will report its own health in the next brief.