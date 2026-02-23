# Operational Wisdom Compendium

**Extracted from**: All agent running logs (Feb 12–18, 2026)
**Sources**: mba-commander, mm-commander, mba-adjudicator, mm-adjudicator, mm-psyche, mm-cartographer, mba-cartographer, mba-ajna
**Purpose**: Distilled operational lessons — the standing-on-shoulders artifact

---

## I. Infrastructure Truths (Seared — Do Not Relearn)

### macOS + launchd

1. **launchd does NOT source ~/.zshrc. EVER.** Environment variables for launchd services must be set in plist `EnvironmentVariables` blocks or explicitly loaded in the service script. Fixing .zshrc is invisible to launchd processes. We looped on this 4+ times.

2. **macOS TCC blocks direct script execution in launchd context** even with +x permission. Always use `bash "$SCRIPT"` instead of `"$SCRIPT"` in launchd service scripts.

3. **`flock` is Linux-only.** Does not exist on macOS. Use PID-file lock pattern instead.

4. **`/tmp` is cleared on reboot.** All lockfiles and persistent state must go to `~/Library/Application Support/` or equivalent durable path.

5. **launchd plists loaded under `sudo` go into the root domain**, not the user domain. Use `launchctl bootstrap gui/$(id -u) <plist>` for user-domain agents. This caused a complete recovery chain failure.

6. **LaunchDaemons load before login; LaunchAgents load after login.** Auto-login is mandatory for autonomous constellation recovery on M1.

7. **Docker Desktop cannot be launched from launchd** (no WindowServer access). Docker must be a Login Item. launchd scripts should be readiness gates, not launchers.

8. **ICMP ping is blocked by macOS Stealth Mode firewall.** NEVER use ping for health checks between machines. Use SSH.

### Git + Google Drive

9. **Google Drive Computer Backup syncs .git/ directories**, creating ghost branches (`main 2`), .DS_Store in .git/, duplicate index files, and ref corruption. Set `xattr com.google.drivefs.ignore=1` on repo dirs. Permanent fix: disable Desktop backup in GDrive preferences.

10. **The git_sync.sh index contamination bomb**: `git rebase origin/main` followed by scoped `git add` can commit deletions of files that exist on another machine but not locally. Sync scripts must enforce scope guards — explicit `git reset` of all paths outside `agents/` and `-OUTGOING/inbox/` before committing.

11. **`git add -A` in heartbeat commits is a loaded weapon.** It tracks everything on disk. When a different machine pulls these commits, files that don't exist locally show as deletions. Never use `git add -A` in automated sync scripts.

---

## II. Verification Discipline (The Three Breakage Loops)

### Loop 1: The .zshrc Illusion
**Pattern**: Fix env vars in .zshrc → declare fixed → launchd services never see the change.
**Countermeasure**: Always verify from WITHIN the execution context (launchd, tmux, ssh). `ps eww -p $PID | grep VAR` is runtime verification. `grep config-file` is not.

### Loop 2: The Async Verification Gap
**Pattern**: Fix → commit → dispatch audit (async) → don't wait for result → commit next fix → audit returns FAIL → too late. 6 commits in 20 minutes on the same subsystem.
**Countermeasure**: NEVER commit a fix without blocking verification. Wait for the test to pass before moving on.

### Loop 3: Context Decay
**Pattern**: 86% deferred commitment loss rate (12/15 OPEN, 0 IN_PROGRESS). Compaction destroys navigability. Promises evaporate between sessions.
**Countermeasure**: Deferred commitments must be addressed within 2 sessions or explicitly killed. Persist state to filesystem before any compaction.

---

## III. Dual Watcher Catastrophe (RESOLVED)

`watch_dispatch.sh` (fswatch) and `auto_ingest_loop.sh` (polling) raced to claim tasks. watch_dispatch's `openclaw agent` CLI mode produced 0-byte output and hung. Tasks were silently swallowed.

**Resolution**: watch_dispatch.sh deprecated and unloaded on 2026-02-17. auto_ingest_loop.sh is the sole dispatch system. NEVER re-enable watch_dispatch.

---

## IV. Recovery Architecture (Proven Chain)

After hardening, the software kill test showed 63-second full recovery:
- T+0s: launchd restarts supervisor (KeepAlive)
- T+26s: cockpit-autostart recreates tmux constellation + 4 agent CLIs
- T+44s: supervisor detects tmux alive, spawns all 4 auto-ingest loops
- T+63s: docker-autostart fires, Docker + containers come up (unless-stopped)

Physical unplug test eventually PASSED after:
1. FileVault disabled (was blocking auto-login at boot)
2. Auto-login configured
3. Docker set as Login Item (not launchd-launched)
4. Container restart policies set to `unless-stopped`
5. Supervisor plist with KeepAlive: true

---

## V. Agent Operational Wisdom

### Commander (Opus 4.6) — Orchestrator
- **Token economics**: Opus is the most expensive model. NEVER read raw corpus into Opus context. Read only digests and final outputs.
- **Progressive summarization**: 616K corpus → 5 digests (~10K) → 1 synthesis (~3K) → Opus reads synthesis only.
- **Budget**: <10K tokens of content reads per Opus session. Delegate everything else.
- **Anti-pattern**: Elaboration over execution. Presenting measurement tables instead of building strategy.
- **Anti-pattern**: Launching execution agents before Sovereign finishes briefing. Wait for the full directive.

### Psyche (GPT-5.3-codex) — Executor/CTO
- Grade A in operations. 4 clean commits, runtime verification, correctly reported FAILED when evidence was ambiguous.
- Best for: systematic coherence, optimization, resilience hardening, throughput quality.
- Shares ChatGPT Plus capacity pool with Adjudicator — coordinate token economics.

### Adjudicator (Codex CLI) — Adversarial Auditor
- Genuine adversarial audits are the highest-value single task type in the constellation.
- Needs unsticking at decision points — provide clear scope and exit criteria.
- The bridgeprobe synthetic test (creating a fake task to verify SCP-back) was exemplary methodology.

### Cartographer (Gemini CLI) — Sensor
- Gemini CLI sandbox prevents access outside the repo directory. Account for this in task dispatch.
- Gemini free tier rate limits are aggressive. Stagger dispatches.
- Best for: large context surveys (1M token window), architecture documentation, research corpus analysis.
- Worst at: tool use. Write-file capabilities are broken in Gemini CLI. Cartographer can read but can't produce file artifacts.
- Grade F in one session — narrated intent instead of executing.

### Ajna (Kimi K2.5 via NVIDIA NIM) — Strategist/CSO
- Generous but fickle limits on the NVIDIA NIM API.
- Useful for load-balancing when other models are rate-limited.
- Gateway at port 18789, launchd-managed with KeepAlive.

---

## VI. Sovereign Interaction Patterns (Learned from Logs)

### What Works
1. **"Proceed comprehensively, dispatch the swarm"** — clear delegation signal with full autonomy granted.
2. **Providing explicit file paths** — reduces ambiguity and prevents wrong-directory errors.
3. **Correcting immediately when agents narrate instead of executing** — "you're not executing, you're creating a plan."
4. **Using invacuation relay portals** — maintaining terminal windows for each CLI agent on both machines.

### What to Improve (Sovereign Self-Audit)
1. **Typo awareness**: "Deskstop" repeatedly instead of "Desktop". Agents can handle it but it adds friction.
2. **Directive completeness**: "proceed comprehensively" without scope bounds leads to token waste. More effective: "proceed comprehensively on X, ignore Y for now."
3. **Frustration signals**: "wtf are you doing", "why the fuck would you survey the canon" — these are valid corrective signals but cost context tokens. A single "STOP. Wrong approach. Do X instead." is more efficient.
4. **Session economics**: Asking agents to "recursively reinforce" or "sear everywhere" leads to diminishing returns. Better: specify exactly which surfaces need the information.
5. **Relay fatigue**: Copy-pasting between terminals is the current bottleneck. The SCP-back routing partially solved this. Next: automated cross-agent coordination without Sovereign relay.

### Terminology Precision (Sovereign Lexicon)
- **"Proceed comprehensively"** = full autonomy, cover all aspects, don't ask permission
- **"Dispatch the swarm"** = use all available agents in parallel
- **"Sear"** = write permanently into memory/config surfaces, never forget
- **"Invacuation relay portal"** = terminal window open for an agent on a specific machine
- **"Annealment"** = semantic fusion pass over the corpus, extracting/compressing/deleting
- **"Neo-canon"** = spiritual successor architecture to the current canon, preserving pedigree

---

## VII. Architectural Lessons

### What the Constellation Actually Is (Honest Assessment)

As of 2026-02-17, the constellation is a **manual dispatch system with self-healing infrastructure**, not an autonomous organism. The agents are organs, not an organism.

**Solved**: Cross-machine file delivery, self-healing after software kill, self-healing after physical unplug, dual-watcher race condition, verification discipline.

**Not solved**: Proactive task generation (agents don't create work for themselves), failed task retry (tasks die in 50_FAILED), cross-agent awareness (agents don't know what others are doing), escalation automation, health-triggered recovery beyond basic restart.

### The fix:feat Ratio
The sessions logged here had a fix:feat ratio of 1.6:1 — more energy fixing than building. The factory is built. Build the product.

### The Split-Brain Risk
The most dangerous failure mode: runtime artifacts exist locally while canonical git history is collapsed. The index contamination bomb (§II.10) caused this. Integrity gates must be Layer 0, fail-closed.

### Context Window Strategy
- Opus 4.6: orchestrator. Never reads raw corpus.
- Sonnet 4.6: workhorse (1M context). Can swallow entire directories.
- GPT-5.3-codex: meticulous executor, sub-optimal rapport.
- Gemini 2.5 Pro: large context surveys, poor tool use.
- Kimi K2.5: backup strategist, fickle availability.

**The most intelligent models strategize and plan. The largest-context models survey and sense. The most meticulous models execute and verify.**

---

## VIII. Anti-Patterns (Ranked by Damage)

1. **`git add -A` in automated scripts** → can wipe entire directories on other machines via sync
2. **Fixing .zshrc for launchd processes** → invisible fix, complete waste
3. **`grep config-file` as verification** → proves config exists, not that it works
4. **Dispatching without Reply-To** → one-way fire-and-forget, coordination failure
5. **Loading plists under sudo** → goes to root domain, not user domain
6. **Saying "you need to run X" to Sovereign** → protocol violation, dispatch to the agent on that machine
7. **Reading raw corpus into Opus context** → token waste, use progressive summarization
8. **Launching agents before directive is complete** → race condition on intent
9. **Committing without blocking verification** → async verification gap
10. **Trusting autopsy claims after the system state has changed** → snapshot-valid ≠ operationally true

---

*Extracted 2026-02-22. Source logs: ~560K characters across 26 files, 8 agents, 2 machines.*
*"The fix:feat ratio tells the story. Build the product."*
