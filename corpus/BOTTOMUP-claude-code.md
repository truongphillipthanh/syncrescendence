# Bottom-Up Clustering: claude-code Tag (315 files)

**Analyst**: Commander (Claude Sonnet 4.6)
**Date**: 2026-02-27
**Method**: Read first 20 lines of all 315 files, then MD5 deduplication, then thematic grouping

---

## Summary

315 files tagged "claude-code" were examined. After reading all files and running byte-level deduplication:

- **47 exact duplicate pairs** (94 files are byte-for-byte copies of 47 distinct documents)
- **~170 unique documents** remain after deduplication
- Natural groupings: 14 distinct clusters emerged from bottom-up reading

---

## GROUP 1: EXACT DUPLICATES (47 pairs — 47 files are crushable)

These are byte-for-byte identical. Keep one copy, delete the other. The lower-numbered file is typically the original; the higher-numbered is the re-ingested copy.

| Keep | Delete |
|------|--------|
| 08081.md | 08841.md |
| 08123.md | 10333.md |
| 08142.md | 10698.md |
| 08143.md | 10695.md |
| 08159.md | 10705.md |
| 08172.md | 10670.md |
| 08179.md | 10801.md |
| 08181.md | 10129.md |
| 08182.md | 10243.md |
| 08184.md | 10284.md |
| 08185.md | 10364.md |
| 08192.md | 10499.md |
| 08199.md | 10580.md |
| 08206.md | 10619.md |
| 08208.md | 10601.md |
| 08210.md | 10626.md |
| 08216.md | 10669.md |
| 08217.md | 10694.md |
| 08221.md | 10703.md |
| 08223.md | 10384.md |
| 08233.md | 10604.md |
| 08237.md | 10661.md |
| 08241.md | 10706.md |
| 08272.md | 10761.md |
| 08280.md | 10445.md |
| 08281.md | 10444.md |
| 08295.md | 10457.md |
| 08297.md | 10578.md |
| 08298.md | 10588.md |
| 08299.md | 10614.md |
| 08300.md | 10611.md |
| 08301.md | 10607.md |
| 08312.md | 10630.md |
| 08324.md | 08538.md |
| 08329.md | 08882.md |
| 08331.md | 08923.md |
| 08370.md | 10628.md |
| 08393.md | 08422.md |
| 08397.md | 08425.md |
| 08402.md | 08427.md |
| 08410.md | 08805.md |
| 08825.md | 10219.md |
| 08832.md | 10097.md |
| 08833.md | 10220.md |
| 08834.md | 10072.md |
| 08836.md | 10222.md |
| 08839.md | 10246.md |

**Pattern**: The 08xxx files came from the original research/ folder import. The 10xxx files (and some 08xxx duplicates) were re-ingested during the February 2026 corpus-building sessions. The duplication is systematic — same content, different atom IDs.

---

## GROUP 2: SYNCRESCENDENCE INTERNAL OPERATIONAL ARTIFACTS

These are NOT public knowledge — they are internal task dispatches, execution results, and internal reports. They have zero value as external research atoms but high internal value as operational records. They should NOT be in the same "knowledge" corpus as public articles.

### 2a: Task Files (41 files)
Internal agent task dispatches — COMPLETE/FAILED records with From/To/Status headers.

```
08585.md  TASK-20260206-test_reply_to
08586.md  TASK-20260207-agendizer-phase2-navigation
08590.md  TASK-20260209-claresce3_pass1_impl_verification
08591.md  TASK-20260209-claresce3v2_pass1_scaffold_quality
08594.md  TASK-20260211-adjudicator_smoke_model52
08595.md  TASK-20260211-codex_sonnet_smoke_and_syn53_todoist
08596.md  TASK-20260211-da12_syn51_jira_fallback
08597.md  TASK-20260211-da12_syn51_jira_validation_rerun
08598.md  TASK-20260211-da12_syn53_todoist_completion
08599.md  TASK-20260211-da12_syn53_todoist_completion_rerun
08600.md  TASK-20260211-ontology_enrichment_validation
08601.md  TASK-20260211-ontology_metacharacterization_audit
08603.md  TASK-20260216-neural_bridge_adversarial_audit
08605.md  TASK-20260217-scp_sling_verify
08606.md  TASK: Validate and Test New launchd Services
08612.md  TASK-20260209-discord_server_setup
08614.md  TASK-20260211-int1612_automation_audit
08615.md  TASK-20260212-mba_codex_upgrade_and_adjudicator_recovery
08616.md  TASK-20260212-mba_ssh_key_install
08618.md  TASK-20260212-skill_architecture_strategic_review_retry
08623.md  TASK-20260209-claresce3v2_pass1_scaffold_audit
08624.md  TASK-20260209-claresce3v2_pass2_canon_coherence
08628.md  TASK-20260216-gemini_headless_smoke
08629.md  TASK-20260216-research_corpus_deep_inspection
08630.md  TASK-20260216-research_corpus_multipass_sensing
08633.md  RECEIPT — Phase 5: Daily Notes View
08634.md  RECEIPT — Phase 6: All Notes Table View
08635.md  RECEIPT — Phase 7: Slash Commands + Backlink System
08636.md  RECEIPT — Phase 8: Entities + Pinned Notes + Tasks View
08640.md  TASK-20260207-highcommand-reflect-phase5-dailynotes
08641.md  TASK-20260207-highcommand-reflect-phase6-allnotes-table
08642.md  TASK-20260207-highcommand-reflect-phase7-slash-backlinks
08643.md  TASK-20260207-highcommand-reflect-phase8-entities-pinned-tasks
08644.md  TASK-20260211-MBA_CASCADE_SUPPLEMENT
08645.md  TASK-20260211-MBA_COMMANDER_SETUP
08646.md  TASK-20260212-mba_adjudicator_model_recovery
08647.md  TASK-20260212-mba_apply_adj_carto_hardening
08649.md  TASK-20260209-claresce3_pass1_infra_audit
08651.md  TASK-20260209-slack_channel_setup
08652.md  TASK-20260212-chroma_restart_loop_investigation
08653.md  TASK-20260212-intelligence_refresh_lastweek
```

**Crushable?** These contain unique operational data (completion times, exit codes, task results). NOT crushable. But they belong in the agents/ directory, not in the general corpus.

### 2b: Result Files (11 files)
Agent execution results — output logs from Codex/Adjudicator runs.

```
08937.md  RESULT-adjudicator-20260207-agendizer-clarescence2-substantiated
08944.md  RESULT-adjudicator-20260209-TASK-LAUNCHD-VALIDATION
08945.md  RESULT-adjudicator-20260209-claresce3_pass1_impl_verification
08946.md  RESULT-adjudicator-20260209-claresce3v2_pass1_scaffold_quality
08948.md  RESULT-adjudicator-20260211-KINETIC_LAYER_DATA
08951.md  RESULT-adjudicator-20260211-codex_sonnet_smoke_and_syn53_todoist
08953.md  RESULT-adjudicator-20260211-da12_syn51_jira_validation_rerun
08958.md  RESULT-adjudicator-20260211-ontology_enrichment_validation
08959.md  RESULT-adjudicator-20260211-ontology_metacharacterization_audit
08967.md  RESULT-adjudicator-20260216-neural_bridge_adversarial_audit
08974.md  RESULT-adjudicator-20260219-scp_sling_verify
```

**Crushable?** Mostly contain only stderr/stdout with no unique insights beyond what the task files capture. LOW value.

### 2c: Internal Syncrescendence Reports / Architecture Docs
These contain unique system-specific knowledge about the Syncrescendence project itself.

```
08045.md  Final Data Quality Fixes Report (YAML @-quoting fixes)
08046.md  Final Census — Source Anneal Pass 5
08064.md  Source Frontmatter Schema
08071.md  Undated Source Triage
08075.md  X/Twitter URL Recovery Report
08378.md  Research Notebooks Manifest
08386.md  BLITZKRIEG PLAN — Repo Rearchitecture
08431.md  SYNTHESIS: Claude Code Architecture (STUB)
08432.md  SYNTHESIS: Codex CLI / OpenAI Developer-Agent Ecosystem
08433.md  SYNTHESIS: Cross-Platform Patterns (STUB)
08477.md  Mike Krieger (Anthropic CPO): 2026 Enterprise AI Vision
08503.md  ChatGPT Compiler Handoff (Syncrescendence internal relay)
08533.md  SIEGE CC28 — Lane 3: State Vector Generator
08584.md  Phase Specifications (Syncrescendence workflow phases)
08670.md  Syncrescendence Configuration Registry
08677.md  DESIGN: Handoff Protocol Formalization
08678.md  REF: Hooks & Automation Formalization
08701.md  Distributed Cognition Research Synthesis
08707.md  Setapp Audit Report
08712.md  STACK TELEOLOGY: Comprehensive Technology Disposition
08719.md  Web App Memory Architecture Audit
08736.md  Rendezvous Summit — Situation Report
08789.md  Research Corpus Chunking Taxonomy
08790.md  Research Corpus: Repository & Tool Extraction
08791.md  Research Corpus: Sovereign Curation Pattern Analysis
08802.md  Research Insights: HIGH Signal Notebooks (5, 6, 1, 2)
08909.md  Oracle RECON – Memory Architecture Directive
08914.md  Oracle RECON – Scaffold Consensus Directive
```

**Crushable?** NOT crushable — these are unique internal records with no public equivalent.

### 2d: Praxis Files (MECH/PRAC/SYNTHESIS format)
Syncrescendence's own synthesized knowledge in SN (Semantic Notation) format.

```
08393.md (= 08422.md)  PRAC: Cowork Desktop Integration
08397.md (= 08425.md)  PRAC: Ontology Dataview Queries
08402.md (= 08427.md)  PRAC: Semantic Compression Workflow
08410.md (= 08805.md)  MECH: Headless Mode Automation
08412.md              MECH: MCP Server Patterns
08414.md              MECH: Skill System Architecture
```

Note: 08393/08422, 08397/08425, 08402/08427, 08410/08805 are exact duplicates — one copy each.

---

## GROUP 3: CLAUDE CODE ARCHITECTURE — DEEP RESEARCH SYNTHESIS CLUSTER

These 13 files all cover the same territory: Claude Code's CLAUDE.md hierarchy, permissions, hooks, context management, Plan Mode. They were produced by different AI research platforms from the same source prompts.

```
08764.md  Claude Code Architecture: Unified Research Synthesis (676 lines)
08765.md  Claude Code Validation Research Synthesis (864 lines)
08768.md  The Claude Code Dialectic: Reasoning Through Divergent Approaches (364 lines)
08769.md  Claude Code Architecture Validation & Enhancement — First-Party Triangulation (397 lines)
08770.md  Claude Code Architecture: Comprehensive Validation and Enhancement Report (422 lines)
08771.md  Architectural Validation and Strategic Enhancement — Technical Report (297 lines)
08772.md  Claude Code Architecture — Gemini summary/validation (223 lines)
08775.md  Claude Code: Validated Architecture, Configuration, and Interaction (422 lines)
08777.md  The Definitive Technical Analysis of Claude Code (440 lines)
08778.md  Claude Code Synthesis baseline load + inventory (208 lines)
08779.md  Deep Research Prompt: Claude Code Architecture (the PROMPT that generated the above) (141 lines)
08782.md  "God-Mode" Claude Code Architecture — Autonomous Orchestration (440 lines)
08786.md  The Definitive Claude Code Configuration Suite (1307 lines)
08787.md  Prompts that generated the research corpus (27 lines — just the prompts)
```

**What they say in common**: CLAUDE.md hierarchy (user > project > local), hooks system, Plan Mode, context compaction, MCP integration, skills/subagents, parallel worktrees, permission model.

**What's unique per file**:
- `08764.md` + `08765.md`: Most comprehensive synthesis, coalescing 5 research iterations — high value
- `08768.md`: The dialectic/tensions document — unique framing of disagreements — high value
- `08769.md`: First-party validation with citation markers — high value for accuracy
- `08786.md`: Config Suite — the actual config files to copy/paste — high value (different format)
- `08782.md`: "God Mode" / superintelligent framing — some unique content on task primitives
- `08777.md` + `08771.md`: Enterprise-focused framing — largely redundant with 08764/08765
- `08770.md` + `08772.md` + `08775.md` + `08778.md`: Redundant summaries — crushable

**Crushable**: 08770.md, 08772.md, 08775.md, 08778.md, 08779.md (just a prompt), 08787.md (just prompts)

**Keep**: 08764.md, 08765.md, 08768.md, 08769.md, 08777.md, 08782.md, 08786.md

---

## GROUP 4: AGENT TEAMS / SWARM MODE — SAME STORY, MULTIPLE TELLINGS

These 6 files all explain the same feature: Claude Code's experimental Agent Teams (also called "swarm mode"), how to enable it, how lead+teammates communicate, how it differs from subagents.

```
08211.md  Agent Teams in Claude Code (how to use them)
08212.md  Claude Code Just Shipped Agent Teams — For Marketers
08233.md (= 10604.md)  Agent Teams Testing — What I Learned
08234.md  How to Install and Use Claude Code Agent Teams (Complete Guide)
08236.md  How to Build a One Person Company with Multi-Agent Swarms
08237.md (= 10661.md)  How to install and use Agent Teams (Reverse-engineered)
08839.md (= 10246.md)  The Swarm Has Arrived (CJ Hess task system analysis)
10200.md  We're turning Todos into Tasks in Claude Code (Anthropic official announcement)
10217.md  Claude Code's New Task System: The Practical Guide
```

**Core insight shared by all**: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json, lead+teammates, peer-to-peer messaging, shared task list, independent context windows. The Todos→Tasks upgrade is the underlying mechanism.

**What's unique**:
- `10200.md`: Official Anthropic announcement — authoritative, different format
- `08839.md`/`10246.md`: CJ Hess auth refactor war story — concrete test case, high signal
- `08237.md`/`10661.md`: Internal architecture reverse-engineering (log tracing) — unique technical depth

**Crushable**: 08211.md, 08212.md, 08234.md, 08236.md (all say "enable the flag, lead coordinates teammates, use it for parallel work" without adding new technical substance vs the reverse-engineered or official versions)

---

## GROUP 5: OPENCLAW/CLAWDBOT — WHAT IT IS, SETUP, USE CASES

These files all cover OpenClaw (formerly Clawdbot/Moltbot) — the Peter Steinberger OSS project. Many are redundant "OpenClaw is amazing" takes.

### 5a: What OpenClaw Is (The Clarification Files)
All three say essentially the same thing: OpenClaw ≠ Claude Code, it's separate OSS that uses Claude as backend, has full system access.

```
08331.md (= 08923.md)  Strategic intelligence: OpenClaw vs Claude Code (comprehensive)
08329.md (= 08882.md)  OpenClaw Deep Research: Recon Intelligence Dump
```

**Keep**: 08331.md (most comprehensive), 08329.md (street-level intelligence). Delete the exact duplicates 08923.md and 08882.md.

### 5b: OpenClaw Use Cases — Crushable Hype

All say some version of "here are N things OpenClaw can do: overnight coder, headless Notion, personal CRM..."

```
08123.md (= 10333.md)  ClawdBot Use Cases Thread (7 use cases)
08135.md              10 More Clawdbot Setups ("saved $4200 on car purchase")
08827.md              Same as 08135.md but with metadata header (DIFF — slightly different format)
```

Note: 08135.md and 08827.md are NOT byte-identical (08827 has an author/metadata header that 08135 lacks). They are the same article, one raw and one with transcription wrapper.

**Crushable**: 08135.md (08827 is the properly transcribed version with metadata). Also 10333.md (duplicate of 08123.md).

### 5c: OpenClaw Troubleshooting Guide (Duplicate)
```
08210.md (= 10626.md)  Andrew Warner's OpenClaw Troubleshooting Thread
```
Delete 10626.md.

### 5d: OpenClaw vs Claude Code comparison
```
08159.md (= 10705.md)  After Installing OpenClaw for 50 Teammates — 5 Things Learned
```
Delete 10705.md.

---

## GROUP 6: DESIGNERS USING CLAUDE CODE — REDUNDANT TAKES

6 files all tell the same story: "I'm a designer who was scared of the terminal, but Claude Code changed everything, now I ship code."

```
08193.md  Claude Code Guide for Designers
08295.md (= 10457.md)  The new design process (brain dump → scope → build)
08297.md (= 10578.md)  The Design Vibeshift (Figma is dying, code is the new canvas)
08299.md (= 10614.md)  How I Stopped Worrying and Learned to Love the Terminal
08301.md (= 10607.md)  What Designers Are Missing About Claude Code
08302.md              The Future of Design is Direct Design ("Direct Design" concept)
```

**Core insight shared by all**: Designers no longer need Figma mockups → describe to Claude Code → ship. The "handoff problem" is solved.

**What's unique**:
- `08302.md`: Coins the term "Direct Design" — novel framing, keep
- `08297.md`/`10578.md`: Best social/industry data on the shift, keep one
- `08193.md`: Most structured guide format, keep

**Crushable**: 08299.md/10614.md (pure personal journey story, no new insight vs others), 08301.md/10607.md (same "I was skeptical then amazed" arc). Delete all 10xxx duplicates anyway.

---

## GROUP 7: BORIS CHERNY'S OWN POSTS / OFFICIAL ANTHROPIC CONTENT

High-authority content from the creator of Claude Code. Very high signal.

```
09875.md  How I Use Claude Code (Boris Cherny's canonical workflow post)
09884.md  Creator of Claude Code literally dropped how he uses it (tweet summary of 09875)
10427.md  Claude Code Tips & Tricks — From the Team (Boris + team tips)
10334.md  CLAUDE.md Loading Behavior (official clarification from @bcherny)
09275.md  Claude Code: Best Practices for Agile Coding (Anthropic blog thread)
10218.md  Merging Slash Commands into Skills in Claude Code (official Anthropic announcement)
10200.md  We're turning Todos into Tasks (official Anthropic announcement)
10411.md  How we use Claude Code in Slack (Anthropic internal usage, Boris)
```

**Assessment**: 09884.md is a tweet-summary of 09875.md and is crushable. All others are unique authoritative content.

**Crushable**: 09884.md (just summarizes 09875.md which we already have)

---

## GROUP 8: CLAUDE CODE BEGINNER GUIDES / SETUP FOR NON-TECHNICAL PEOPLE

Many files all teach the same beginner onboarding: install Claude Code, it's not scary, here's what CLAUDE.md is, here's Plan Mode.

```
09300.md  Mastering the Vibe: Claude Code best practices (Medium article)
09973.md  How to Set Up Claude Code in <15 Minutes (For Beginners)
10106.md  How to Automate Your Life With Claude Code (for Non-Technical People)
10132.md  Claude Code Clearly Explained (YouTube — Greg Isenberg crash course)
10192.md  Claude Code for Scientists (specific domain)
08191.md  How To Build a Compounding AI Operating System (non-technical)
```

**Core shared content**: Terminal isn't scary, CLAUDE.md is memory, Plan Mode before coding, describe what you want not how.

**What's unique**:
- `09300.md`: "Mastering the Vibe" — covers best practices comprehensively, well-organized
- `08192.md`/`10499.md`: Scientists angle — specific domain warning about metacognition — unique
- `08191.md`: Non-technical operating system concept — unique framing for non-devs

**Crushable**: 09973.md and 10106.md (both pure beginner setup with nothing the others don't cover)

---

## GROUP 9: CLAUDE CODE HOOKS / GIT INTEGRATION

Small cluster, mostly unique:

```
08208.md (= 10601.md)  git hooks in Claude Code (PreToolUse/PostToolHooks)
08185.md (= 10364.md)  Obsidian + Claude Code: Async Hooks for Note History
08678.md              REF: Hooks & Automation Formalization (Syncrescendence internal)
```

Delete the 10xxx duplicates. Keep one copy of each.

---

## GROUP 10: OBSIDIAN + CLAUDE CODE KNOWLEDGE MANAGEMENT

4 files all cover "use Claude Code to manage your Obsidian vault":

```
08181.md (= 10129.md)  obsidian + claude code 101 (vault as operating system)
08182.md (= 10243.md)  Build Claude a Tool for Thought (vibe note-taking problem)
08183.md              Obsidian & Claude Code 101: Context Engineering (progressive disclosure)
08184.md (= 10284.md)  Vibe Note-Taking 101: Editing Workflow (annotation loop)
10147.md              Yapping to PRDs: Claude Code & Obsidian (meetings → docs)
10420.md              Program Your Computer with Notes, Not Code (Obsidian + AI)
```

**Core shared insight**: Obsidian markdown notes become skills/context for Claude. Progressive disclosure. Auto-commit with hooks.

**What's unique**:
- `08183.md`: The 4-layer progressive disclosure system (file tree → index → summary → full) — technical, unique
- `10147.md`: Meeting transcripts → PRDs workflow — practical, unique
- `08182.md`/`10243.md`: Conceptual framing ("tool for thought") — unique angle

**Crushable**: 08181.md/10129.md (covers same ground as 08183.md with less depth) — keep 08183.md as superior

Delete all 10xxx exact duplicates.

---

## GROUP 11: MULTI-AGENT ORCHESTRATION (NON-SWARM) — CLOUD/PARALLEL PATTERNS

```
08081.md (= 08841.md)  Production patterns for multi-agent Claude Code coordination
08179.md (= 10801.md)  We need to solve multi-agent collaboration (Zach Lloyd / Warp)
08223.md (= 10384.md)  ClawdBot Battle: Parallel vs Sub-Agents
08227.md              Guide Tutorials P1: The Orchestration Workflow
08240.md              The Cloud Agent Thesis (Devin/Cognition — cloud vs local)
```

**Core shared content**: Subagents vs parallel agents, worktrees for isolation, orchestrator-workers pattern.

**What's unique**:
- `08081.md`/`08841.md`: Deep tactical content (git worktrees, handoff docs, CLAUDE.md bridges) — keep 08081.md
- `08240.md`: Cloud agents thesis (Zach Lloyd) — architectural vision piece — unique
- `08179.md`/`10801.md`: Agent collaboration primitives — unique (from Warp CEO)

Delete 08841.md, 10801.md, 10384.md (exact duplicates).

---

## GROUP 12: CONTEXT MANAGEMENT / SKILLS / PROGRESSIVE DISCLOSURE

```
08083.md  LLM Contextualization Index (website scanning patterns — generic)
08085.md  Subreddit directory for Claude-related communities
08196.md  Deep Dive on Agent Skills (ElevenLabs skills author)
08414.md  MECH: Skill System Architecture (Syncrescendence SN format)
08412.md  MECH: MCP Server Patterns
10032.md  Progressive Disclosure in Claude Code (YouTube — Developers Digest)
10113.md  Claude Code's MCP Problem Just Got Fixed (MCP Search Tool)
10218.md  Merging Slash Commands into Skills (official Anthropic)
```

**What's unique per file**:
- `08083.md`: Website index for LLM context extraction — meta/generic, low value for Claude Code specifically
- `08085.md`: Subreddit directory — reference utility, low value
- `08196.md`: Best technical breakdown of agent skills architecture — high value
- `10113.md`: MCP Search Tool announcement — news item, specific feature
- `10218.md`: Official Anthropic announcement — canonical source

**Crushable**: 08083.md (generic LLM content, not Claude Code specific), 08085.md (subreddit list, publicly available)

---

## GROUP 13: BROADER AI/ECONOMICS/SOCIETY PIECES (TOPICALLY ADJACENT BUT THIN CONNECTION TO CLAUDE CODE)

These were tagged "claude-code" but the Claude Code angle is minor or incidental:

```
08373.md  AI isn't coming for your future, Fear is (Bastiat / Broken Window fallacy)
08742.md  2026: This is AGI (Pat Grady/Sonya Huang essay)
10281.md  What makes an engineer when everyone can vibe code
10308.md  Japan's Debt Bomb (Econ video — tangential)
10541.md  SaaS is Dead. Agents Killed It.
10565.md  How to Win When Everyone Has AI
10663.md  The Coming Corporate War for Compute
10822.md  This New AI Benchmark Changes Everything (SWE-rebench)
09545.md  AlphaFold Nobel Prize (Google DeepMind — NOT Claude Code)
09642.md  Google DeepMind Robotics Lab Tour (NOT Claude Code)
```

**Crushable**: 09545.md and 09642.md have essentially no connection to Claude Code — they're general AI/robotics content that got miscategorized. 10308.md (Japan's Debt) is also miscategorized. These should be recategorized, not deleted necessarily, but they add zero signal to the claude-code cluster.

---

## GROUP 14: YOUTUBE VIDEO METADATA (DESCRIPTIONS ONLY — NO TRANSCRIPTS)

Many files in the 09xxx–10xxx range are YouTube video entries with only the video description and no transcript. These are placeholders with very low information density.

```
09376.md  This neural interface writes code from my brain waves (Fireship — just description)
09545.md  AlphaFold Nobel Prize (description only)
09642.md  Google DeepMind Robotics (description only)
09691.md  Claude Code's latest update (Theo t3.gg — description only)
09696.md  Boris Cherny career story (description only)
09833.md  How to Run Claude Code Autonomously (description only)
09919.md  Self-Improving Skills in Claude Code (description only)
09933.md  I'm addicted to Claude Code (Theo — description only)
10007.md  Anthropic just burned trust (Theo — description only)
10022.md  Introducing Cowork (Anthropic 1min video — description only)
10032.md  Progressive Disclosure (description only)
10043.md  ChatGPT Health + Claude Code Tipping Point podcast (description only)
10045.md  Claude Cowork OS that Automates Your Life (description only)
10047.md  Stop Using The Ralph Loop Plugin (description only)
10099.md  Google's AI Knows Everything (description only)
10102.md  We need to talk about Ralph (Theo — description only)
10113.md  Claude Code's MCP Problem Fixed (description only)
10117.md  Claude Cowork: small taste of AGI (Theo — description only)
10126.md  Anthropic Just Added Features to Claude Code (description only)
10132.md  Claude Code Clearly Explained (description only)
10185.md  AI coding has reached a tipping point (description only)
10191.md  The Whole World Gets Claude-Pilled (description only)
10193.md  Claude Code + Ollama: Local & Cloud Models (description only)
10228.md  Claude Code Let's Build: AI Video Oracle (description only)
10237.md  I got a private lesson on Claude Cowork & Claude Code (description only)
10239.md  Claude Code Is Taking Over (description only)
10275.md  Agentic Workflows Changed AI Automation Forever (description only)
10281.md  Ollama Launch + Claude Code + GLM Flash (description only)
10308.md  Japan's Debt Bomb (description only — NOT Claude Code)
10313.md  Ralph Wiggum, Clawdbot and Mac Minis (description only)
10317.md  Clawd Bot Explained In 5 mins (description only)
10320.md  I Gave Claude Code My Whole Genome (description only)
10374.md  100 Hours Testing Clawdbot vs Claude Code (description only)
10377.md  The creator of Clawd (Pragmatic Engineer — description only)
10418.md  Claude Code has a big problem (Theo — description only)
10420.md  Program Your Computer with Notes (description only)
10557.md  Master OpenClaw in 30 Minutes (description only)
10678.md  How I use Claude Code (Meta Staff Engineer Tips — description only)
10680.md  OpenClaw Is Infostealer Malware (description only)
10681.md  How I'd Teach a 10 Year Old Agentic Workflows (description only)
```

**Assessment**: Video descriptions without transcripts have very low signal. They note a video exists but contain no actionable knowledge. They are crushable IF the corresponding article/written version exists elsewhere in the corpus.

**High-priority crushes** (video description where the content exists as an article):
- `10237.md` (Boris Cherny Cowork lesson) — the written version is `08833.md`/`10220.md`
- `10032.md` (Progressive Disclosure video) — covered more thoroughly in `08414.md` MECH file

**Keep** (unique content with no article equivalent):
- `09696.md` Boris Cherny career story — no written equivalent found
- `10377.md` Peter Steinberger / Creator of Clawd — no written equivalent
- `10678.md` Meta Staff Engineer 50 tips — no written equivalent

---

## FINAL CRUSH CANDIDATE SUMMARY

### Tier 1: Exact Duplicates — Delete Immediately (47 files)

Delete these files (exact byte-for-byte copies of their paired file listed in Group 1):
```
08538.md  08841.md  08882.md  08922.md  08923.md
10072.md  10097.md  10129.md  10219.md  10220.md
10222.md  10243.md  10246.md  10284.md  10333.md
10364.md  10384.md  10419.md  10444.md  10445.md
10457.md  10499.md  10578.md  10580.md  10588.md
10601.md  10604.md  10607.md  10611.md  10614.md
10619.md  10626.md  10628.md  10630.md  10661.md
10669.md  10670.md  10694.md  10695.md  10698.md
10703.md  10705.md  10706.md  10761.md  10801.md
08422.md  08425.md  08427.md  08805.md
```

Note: In pairs where both are in 08xxx range (08393/08422, 08397/08425, 08402/08427, 08410/08805, 08324/08538, 08329/08882, 08331/08923, 08081/08841), delete the higher-numbered one.

### Tier 2: Near-Duplicate Content — Redundant Perspectives on Same Fact (Crushable)

These are NOT byte-identical but say the same things:

- `08772.md`, `08775.md`, `08778.md`, `08779.md` — architecture research redundancies (keep 08764, 08765, 08768, 08769, 08786)
- `08787.md` — just the prompts that generated the research, not useful as a knowledge atom
- `08211.md`, `08212.md`, `08234.md`, `08236.md` — Agent Teams beginner takes (keep 08237, 08839, 10200, 10217)
- `09973.md`, `10106.md` — beginner Claude Code setup (keep 09300, 08191)
- `09884.md` — tweet summary of 09875.md (keep 09875.md, delete summary)
- `08135.md` — raw version of 08827.md (delete 08135, keep 08827 which has transcription metadata)
- `09545.md`, `09642.md`, `10308.md` — miscategorized (not Claude Code content)

### Tier 3: Publicly Available Information We Already Have Better Versions Of

- `08083.md` — generic LLM website index guide (low value, publicly available)
- `08085.md` — subreddit directory (publicly available, easily regenerated)
- `08098.yaml`, `08099.yaml` — archived/stale model profiles, superseded by engine/02-ENGINE/MODEL-INDEX.md per their own headers

### Files With Unique Value We Would LOSE If Deleted

These contain knowledge NOT available publicly or synthesized uniquely:

1. **08324.md** — Syncrescendence's own Oracle RECON prompt for OpenClaw deep research (internal)
2. **08329.md** — OpenClaw recon intelligence dump (our specific research + methodology)
3. **08331.md** — Strategic intelligence on OpenClaw vs Claude Code for Syncrescendence specifically
4. **08701.md** — Distributed Cognition Research Synthesis methodology (internal process doc)
5. **08764.md** + **08765.md** — 5-iteration coalesced synthesis, most comprehensive Claude Code architecture doc (~1500 lines combined)
6. **08786.md** — Complete Claude Code config suite (actual deployable config files)
7. **08768.md** — Claude Code dialectic tensions (unique framing of disagreements across practitioners)
8. **09875.md** — Boris Cherny's own workflow description (rare first-party practitioner data)
9. **10427.md** — Claude Code team tips (from the actual team)
10. **08839.md** — CJ Hess swarm test (concrete auth refactor war story with specific data)
11. All 41 TASK files + 11 RESULT files — operational records unique to Syncrescendence
12. **08678.md** — Syncrescendence hooks system documentation
13. **08712.md** — Stack Teleology (full tool disposition rationale)
14. **08719.md** — Web App Memory Architecture Audit (deep comparison including portability)

---

## DEDUPLICATION STATISTICS

| Category | Count |
|----------|-------|
| Total files examined | 315 |
| Exact duplicate pairs | 47 |
| Files that are exact duplicates | 94 |
| Unique files after deduplication | 221 |
| Near-duplicate/redundant content (Tier 2) | ~20 |
| Miscategorized files | ~3 |
| Crushable total (safe to delete) | ~67 |
| Files with unique irreplaceable knowledge | ~50 |
| Files with publicly available knowledge | ~100 |
