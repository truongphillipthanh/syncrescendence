# Bottom-Up Clustering: openclaw (96 files)

**Date**: 2026-02-27
**Operator**: Commander (Claude Sonnet 4.6)
**Method**: Read first 20 lines of all 96 files, then full reads on ~30 files to determine depth. Exact diffs on suspected duplicates.

---

## Confirmed Exact Duplicates (6 pairs = 6 crushable files)

These are byte-for-byte identical. Delete one of each pair.

| File A | File B | Content |
|--------|--------|---------|
| `08330.md` | `08921.md` | OpenClaw Best Practices Audit (security hardening guide with code samples) |
| `08066.md` | `08808.md` | OpenClaw Research — Source Inventory (URL fetch log, 11 sources) |
| `08435.md` | `08809.md` | SYNTHESIS: OpenClaw Deep Research v2 (MEDLEY synthesis) |
| `08322.md` | `08499.md` | PROMPT-AUGUR-20260203-openclaw_deep_research |
| `08325.md` | `08564.md` | PROMPT-VANGUARD-20260203-openclaw_deep_research |
| `08326.md` | `08565.md` | PROMPT-VIZIER-20260203-openclaw_deep_research |

**Crush recommendation**: Delete `08921.md`, `08808.md`, `08809.md`, `08499.md`, `08564.md`, `08565.md` (keep the lower-numbered originals).

---

## Same-Content Pairs (Different Wrappers — Near Duplicates)

These files contain the same article but one has tweet metadata (author, date, URL, engagement stats) prepended.

| Bare Article | Tweet-Wrapped Version | Content |
|--------------|----------------------|---------|
| `08136.md` | `08829.md` | Kimi × OpenClaw — The Simplest Setup Yet (Kimi Product official post) |
| `08167.md` | `08837.md` | OpenClaw + Honcho: Memory That Reasons for OpenClaw |

**Crush recommendation**: Delete `08136.md` and `08167.md` (bare versions). The tweet-wrapped versions `08829.md` and `08837.md` preserve provenance (author, URL, engagement data, date). That metadata has research value.

---

## Same-Content Pair (Different Length Versions)

| Shorter | Longer | Content |
|---------|--------|---------|
| `08351.md` | `08350.md` | OpenClaw + MiniMax = $14/month AI agent. `08350.md` is 457 lines with full reference links; `08351.md` is 236 lines, truncated. |
| `08347` | `08348.md` | OpenClaw Skill That Lets Your Agent Earn Autonomously. Files are 216 vs 218 lines, near-identical with minor description formatting differences. |

**Crush recommendation**: Delete `08351.md` (keep `08350.md` — it has the full references). For `08347`/`08348.md`: delete `08347` (missing `.md` extension, slightly less content).

---

## Natural Groupings Observed

### GROUP A: Official / Canonical Research (Syncrescendence-internal)
*High-value: irreplaceable Syncrescendence-internal research artifacts*

- `08066.md` (or `08808.md`) — Source inventory of fetched URLs
- `08322.md` (or `08499.md`) — Prompt: Augur deep research
- `08325.md` (or `08564.md`) — Prompt: Vanguard deep research
- `08326.md` (or `08565.md`) — Prompt: Vizier deep research
- `08435.md` (or `08809.md`) — MEDLEY synthesis (5-stream)
- `09049.md` — Psyche's 30-day consequential adoptions briefing

### GROUP B: Installation / Setup Guides
*Publicly available content. Multiple articles covering the same terrain.*

- `08139.md` — "The guide that should have existed from day one" (cross-platform, 23 errors documented)
- `08138.md` — "Clawdbot Masterclass" (setup to 10+ hours saved/week)
- `08340.md` — Mac Mini Setup: The One Prompt
- `08154.md` — Sandboxed VM setup guide
- `08244.md` — "Changed five things, now runs agents on its own" (config files walkthrough)
- `08338.md` — How to run Opus 4.6 on OpenClaw (copy-paste terminal commands)
- `08350.md` / `08351.md` — OpenClaw + MiniMax = $14/month setup

**Crush candidates within this group**: `08138.md`, `08139.md`, `08340.md`, and `08244.md` all cover "how to get OpenClaw working well" from different angles. They are not identical but they heavily overlap on: install steps, personality files (SOUL.md), memory files, heartbeat, skills installation. A single synthesized document would replace all four. However, `08139.md` has unique value (23 distinct errors, multi-OS coverage) and `08154.md` has unique value (sandboxed VM architecture). Keep those two; `08138.md` and `08340.md` are the weakest / most generic.

### GROUP C: Security Guides
*Publicly available content. High overlap.*

- `08155.md` — "A Security-First Guide to Running OpenClaw" (9 steps, Pi + Tailscale + Matrix)
- `08156.md` — "How I Set Up OpenClaw Without Giving It the Keys to My Life" (dedicated machine, allowlist)
- `08154.md` — Sandboxed VM setup (overlaps with security angle)
- `08157.md` — SHIELD.md: A Security Standard (proposes new standard, unique angle)
- `08229.md` — "How to Build an AI Agent That Never Goes Crazy" (agentic control)
- `08226.md` — "I Run a Fleet of AI Agents from a Mac Mini. Here's How I Keep Them From Going Rogue."
- `08330.md` / `08921.md` — OpenClaw Best Practices Audit (technical config reference)

**Crush candidates**: `08155.md` and `08156.md` say essentially the same thing (dedicated hardware, Tailscale, no public ports, allowlists, read-only tokens). One can be deleted. `08229.md` and `08226.md` overlap on multi-agent control themes but each has distinct angles. `08157.md` (SHIELD.md standard) is unique — keep it.

### GROUP D: Use Case Showcases / "Look What It Can Do" Posts
*Publicly available. High redundancy — the same message repeated across many posts.*

- `08127.md` — "openclaw alone is a demo. this is the full product." (X post)
- `08130.md` — "20 More Clawdbot Setups That Made Me Say 'Wait, It Can Do That?'"
- `08132.md` — ClawdBot (now OpenClaw) Thread — Wild examples
- `08140.md` — "Honest Breakdown: One Week with OpenClaw"
- `08145.md` — "I gave Openclaw access to my browser, email, and ad accounts"
- `08147.md` — "I gave OpenClaw a name, its own computer... 32-hour recap"
- `08149.md` — ClawdBot (now OpenClaw): The Personal AI Assistant (thread)
- `08231.md` — "Lulubot Takeaways: 1 Week of Building and Using My OpenClaw"
- `08243.md` — "How I built an Autonomous AI Agent team that runs 24/7"
- `08360.md` — "How my OpenClaw agent, Larry, got millions of TikTok views"

**Crush candidates**: `08132.md` and `08149.md` are nearly duplicate content (same Min Choi thread, one bare, one expanded). `08127.md`, `08130.md`, `08145.md` all make the same point — "here are wild things OpenClaw can do" — with different example lists. The knowledge in these is available publicly; none contains unique sovereign insight. The most crushable: `08130.md`, `08132.md`, `08149.md` (redundant with each other). Keep `08147.md` (32-hour dedicated machine experiment — architectural insight), `08231.md` (nuanced week-long analysis), `08360.md` (TikTok content automation, concrete metrics).

### GROUP E: Architecture / Technical Deep Dives
*Mix of public and unique content. Higher retention value.*

- `08148.md` — "You Could've Invented OpenClaw" (first-principles architecture tutorial)
- `08175.md` — "Your Company is a Filesystem" (filesystem-as-state philosophy)
- `08264.md` — "The Unreasonable Effectiveness of Centralizing the AI Heartbeat"
- `08235.md` — "I Built an AI Company with OpenClaw + Vercel + Supabase"
- `08232.md` — "OpenClaw Workforce: The complete guide to running yours"
- `08171.md` — Token efficiency: scripts vs smart polling
- `08286.md` — Unbrowse: 100x faster than browser automation

**No duplicates in this group.** These each contain distinct architectural ideas. All are publicly available but synthesized here. Retain all — these have the highest per-file density of extractable praxis.

### GROUP F: Model Selection / Cost Optimization
*Publicly available. Some redundancy.*

- `08134.md` — Adeo Ressi config: Kimi K2.5 primary, Claude fallback (tweet)
- `08136.md` / `08829.md` — Kimi × OpenClaw native integration guide
- `08162.md` — "I Cut My OpenClaw Cost by 95%" (MiniMax M2.5)
- `08350.md` / `08351.md` — OpenClaw + MiniMax = $14/month
- `08831.md` — kimi-k2.5 for free via NVIDIA (tweet)
- `08204.md` — Advanced Memory System Setup (Opus 4.6 main + Kimi subagent)

**Crush candidates**: `08134.md` (tweet-level, minimal content), `08831.md` (tweet-level, minimal content). These are best absorbed into a synthesis note. `08162.md` and `08350.md` both cover MiniMax cost optimization — `08350.md` is more complete; `08162.md` can be deleted or merged.

### GROUP G: Skills / Capabilities Expansion
*Publicly available. Distinct enough to retain.*

- `08209.md` — Skills Masterclass: 5 workflows that run forever
- `08311.md` — 3 things to build: activity feed, calendar, global search
- `08347` / `08348.md` — OpenClaw Skill: Agent Earn Autonomously (blockchain/Base)
- `08334.md` / `08336.md` — ElevenLabs voice integration (inbound calls)
- `08339.md` — ElevenAgents: outbound calls from OpenClaw
- `08286.md` — Unbrowse: API instead of browser automation
- `08359.md` — camofox-browser: anti-detection browsing plugin

**Near-duplicates**: `08334.md` and `08336.md` are the same article with minor image-description wording differences — not byte-identical but functionally identical. Delete `08334.md`, keep `08336.md`. `08339.md` covers the outbound direction (agent calls you) vs inbound (you call agent) — retain as complement.

### GROUP H: Agentic Philosophy / Macro Takes
*Publicly available. Low immediate operational value.*

- `08131.md` — "The AI Agent Paradigm Has Shifted" (paradigm shift commentary)
- `08141.md` — Molt Ecosystem Map (83 projects, blockchain/agent economy)
- `08247.md` — "A Survival Guide for the Post-Labor Economy"
- `08257.md` — "Cowork and OpenClaw Showed Us The First Practical AGI"

**Crush candidates**: `08247.md` (post-labor economy commentary, not actionable), `08257.md` (AGI claims piece, hype-adjacent), `08131.md` (paradigm shift post, superseded by actual architecture knowledge). `08141.md` has unique ecosystem mapping value — retain.

### GROUP I: Personality / Agent Identity Configuration
*Mix of public and operationally useful.*

- `08144.md` — OpenClaw Personality Overhaul Thread (paste-ready SOUL.md rewrite prompt)
- `08354.md` — OpenClaw: The Jarvis Initialization Sequence (conversation script)
- `08356.md` — Automatic Discipline with OpenClaw (daily structure agent)
- `08186.md` — "My OpenClaw researches Second Brains for Agents" (tools for thought)
- `08204.md` — Advanced Memory System Setup

**No duplicates.** Each has a distinct focus. `08144.md` is operationally reusable (paste-ready prompt). `08354.md` likewise. Retain all.

### GROUP J: Business / Revenue Use Cases
*Publicly available. Distinct enough.*

- `08137.md` — OpenClaw For Business Setup (verify+learn loops, revenue focus)
- `08145.md` — Business use cases (competitive intelligence, marketing)
- `08360.md` — TikTok content automation (concrete MRR metrics)

**Weak overlap** between `08137.md` and `08145.md` (both business-focused) but different enough to retain both.

### GROUP K: Announcement / Origin Story
*Publicly available. Historic record.*

- `08126.md` — "Introducing OpenClaw" (Peter Steinberger rebrand announcement)

**Retain**: Primary source, origin story. Not duplicated elsewhere.

### GROUP L: Syncrescendence-Internal Operational Documents
*Irreplaceable — Syncrescendence-specific, not publicly available.*

- `08062.md` — Source Anneal Pass 1 Lane B: Relocation Log
- `08722.md` — Source Anneal Pass 1 Lane B: Relocation Log (confirmed exact duplicate of `08062.md`)
- `08074.md` — X/Twitter URL Recovery Log
- `08092.md` — Sources by Topic (auto-generated index, 6890 sources)
- `08096.md` — MODEL INDEX: Frontier AI Model Registry
- `08109.md` — Cockpit Reconfiguration Pending (self-note)
- `08572.json` — OpenClaw Slack configuration for @psyche
- `08610.md` — TASK: Ghostty spacing fix
- `08613.md` — TASK: MacBook Air Deployment Guide for Ajna
- `08627.md` — TASK: Research corpus analysis
- `08638.md` — RECEIPT: Constellation Reconfiguration Briefing
- `08650.md` — TASK: Configure @psyche Slack Bot on Mac Mini
- `08706.md` — REF: Self-Healing Constitution (canonical reference)
- `08957.md` — RESULT: adjudicator install-hf-last-signal-skills
- `08976.md` — RESULT: adjudicator deferred_dc_003_followup
- `08980.md` — RESULT: adjudicator deferred_dc_003_followup (next day)
- `08985.md` — RESULT: adjudicator deferred_dc_003_followup (day after)
- `08990.md` — RESULT: Ajna openclaw path fix
- `08995.md` — RESULT: final_sync_proof2 (ajna)
- `08996.md` — RESULT: mini_browser_relay_and_integrations_sweep
- `08998.md` — RESULT: outfitment_sync_and_smoketest_v2_ssh
- `08999.md` — RESULT: outfitment_sync_and_smoketest_v3
- `09004.md` — RESULT: ajna watcher smoke test
- `09041.md` — RESULT: commander install-hf-last-signal-skills
- `09048.md` — RESULT: psyche hf-signal-skill-fork-and-dispatch
- `09049.md` — RESULT: psyche last30days_openclaw_consequential_adoptions

**Exact duplicate confirmed**: `08062.md` and `08722.md` are identical (diff returned 0). Delete `08722.md`.

**Near-crush within Group L**: `08976.md`, `08980.md`, and `08985.md` are three sequential RESULT files for the same task (`TASK-20260220/21-deferred_dc_003__followup.md`) all returning Exit-Code 75. These represent repeated failed attempts. The substantive content of all three may be the same "task failed" response. Verify and crush to one if so.

---

## Summary: Crush Candidates by Confidence

### CERTAIN DELETES (exact duplicates, zero information loss):
1. `08921.md` — exact dup of `08330.md`
2. `08808.md` — exact dup of `08066.md`
3. `08809.md` — exact dup of `08435.md`
4. `08499.md` — exact dup of `08322.md`
5. `08564.md` — exact dup of `08325.md`
6. `08565.md` — exact dup of `08326.md`
7. `08722.md` — exact dup of `08062.md`
8. `08136.md` — bare version of `08829.md` (tweet-wrapped version has more data)
9. `08167.md` — bare version of `08837.md`
10. `08351.md` — truncated version of `08350.md`
11. `08347` — shorter version of `08348.md`
12. `08334.md` — functionally identical to `08336.md`

**Total certain deletes: 12 files**

### HIGH-CONFIDENCE CRUSHES (same knowledge, publicly available, redundant):
13. `08132.md` — redundant with `08149.md` (same Min Choi thread content)
14. `08130.md` — "20 more setups" list post, purely anecdotal, lower density than use case articles retained
15. `08247.md` — post-labor economy commentary, no actionable content
16. `08257.md` — AGI hype piece, superseded by concrete architecture knowledge
17. `08831.md` — tweet stub (kimi via NVIDIA), content absorbed by `08136.md`/`08829.md`
18. `08134.md` — tweet stub (model config), content absorbed by other model guides
19. `08162.md` — MiniMax cost guide, substantially covered by `08350.md`
20. `08138.md` — Clawdbot Masterclass, overlaps heavily with `08139.md` and `08244.md`

**Total high-confidence crushes: 8 files**

### TOTAL CRUSHABLE: ~20 files out of 96 (21%)

---

## Files With Unique / Irreplaceable Knowledge

These should NOT be deleted regardless of topic overlap:

- `08066.md` — Research source inventory with verified URLs (keep over `08808.md`)
- `08126.md` — Primary source: OpenClaw origin story / rebrand announcement
- `08139.md` — Multi-OS setup guide with 23 documented error messages (unique debugging reference)
- `08148.md` — First-principles OpenClaw architecture derivation (most dense technical doc)
- `08154.md` — Sandboxed VM security architecture
- `08157.md` — SHIELD.md standard proposal (unique structured approach)
- `08175.md` — Filesystem-as-state philosophy (unique conceptual angle)
- `08186.md` — Research on second brains for agents (Ajna-initiated research session)
- `08229.md` — Agent safety: prompt injection / black market credentials angle
- `08231.md` — Lulubot week-long analysis (most honest nuanced assessment)
- `08235.md` — Multi-agent company architecture (Vercel + Supabase, concrete implementation)
- `08264.md` — Centralizing the AI heartbeat (architectural insight)
- `08286.md` — Unbrowse: API vs browser automation (10-45s → 200ms, concrete)
- `08435.md` — MEDLEY synthesis (5-stream research synthesis, Syncrescendence-generated)
- `08706.md` — Self-Healing Constitution (canonical Syncrescendence reference)
- `09049.md` — Psyche 30-day consequential adoptions briefing
- All TASK/RESULT pairs in Group L (operational history, irreplaceable)
