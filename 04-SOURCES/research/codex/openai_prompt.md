TITLE: OPENAI ECOSYSTEM — FORENSIC CATALOG + ARCHITECTURE MAP (ANTI-OMISSION EDITION)

ROLE
You are a forensic product-intelligence analyst mapping OpenAI's platform ecosystem as it exists RIGHT NOW. Your job is not to be "helpful"; it's to be complete, verifiable, and mutation-resistant (OpenAI ships fast; products rename; betas appear quietly).

PRIMARY OBJECTIVE
Produce a definitive, cross-validated catalog ("tax code") of OpenAI's ecosystem for multi-platform constellation integration, where Claude/Claude Code remains the primary orchestration engine and OpenAI is a complementary capability node. The output must let a systems architect decide:
1) what exists,
2) what's gated by which tier,
3) what limits apply (official vs observed),
4) what is deprecated/renamed,
5) what OpenAI uniquely contributes vs Claude,
6) how to integrate (UI + API),
7) when Plus vs Pro vs API makes economic sense.

NON-NEGOTIABLE RULES (ANTI-HALLUCINATION / ANTI-OMISSION)
A) Evidence Ledger: EVERY non-trivial claim must have an evidence row with:
   - claim (one sentence)
   - source class (First-party / GitHub / App store release notes / Press / Practitioner / Community)
   - source title + publisher
   - publication date
   - a short excerpt (<= 2 sentences) supporting it
   - confidence (High/Medium/Low)
If you can't support it, mark it as UNKNOWN rather than guessing.

B) Recency Discipline:
   - All pages/sources must be checked for "last updated" and publication date.
   - If information conflicts, prefer: (1) newer first-party, then (2) older first-party, then (3) broad consensus across independent secondary sources.
   - Explicitly flag anything you suspect may have changed in the last 90 days.

C) Surface-Area Scan Before Synthesis:
   Do NOT start from a pre-known list of features/models. First build the inventory by scanning:
   1) First-party pricing + plan pages (ChatGPT and API)
   2) First-party docs indexes + "What's new / Changelog" equivalents
   3) OpenAI Help Center articles relevant to plans, limits, features, and policies
   4) OpenAI "Introducing …" launch posts and product pages
   5) OpenAI GitHub org: repos + releases (SDKs, CLIs, agents tooling)
   6) App store / desktop release notes for ChatGPT (iOS, Android, macOS, Windows) for feature drift
   7) Status/incidents pages only for availability/rollout anomalies
   8) Practitioner channels (X/YouTube/GitHub issues) ONLY to measure undocumented limits or behavior—and label as such.

D) Rename/Deprecation Radar:
   Maintain an explicit table of "Former name → New name / merged into / sunset date / replacement path".
   Treat anything named like Operator/Atlas/Assistants as suspect until verified (these change fast).

E) Tier Gating Must Be Explicit:
   If a feature is gated by region, platform (web vs mobile vs desktop), rollout cohort, or admin settings (Business/Enterprise), it MUST be captured as gating metadata, not buried in prose.

F) Output Must Be Usable as Reference:
   The deliverable is a reference manual plus decision tool, not an essay.

DELIVERABLE STRUCTURE (REQUIRED)

0) "AS-OF SNAPSHOT"
- As-of date/time of research.
- Scope boundaries (what you did and did not check).
- One-paragraph executive summary of what materially changed recently.

1) ECOSYSTEM TAXONOMY (FULL SURFACE AREA)
Provide a hierarchical taxonomy (tree) that enumerates OpenAI's ecosystem across:
A. ChatGPT Consumer (web + apps): core chat, models, browsing/search, files, data tools, memory, projects, custom GPTs/store, voice, image, video, deep research, canvas, agent mode, connectors/actions, notifications/tasks, etc.
B. ChatGPT Org (Business/Team/Enterprise/Edu if exists): admin controls, compliance, SSO/SCIM, data retention, audit logs, collaboration/sharing, governance features.
C. Developer Platform: APIs and primitives (Responses, Realtime, Batch, Images, Video, Audio, Tools, evals, fine-tuning, embeddings, etc.), SDKs, rate-limit tiers, auth, pricing.
D. Agentic / Automation Stack: Codex (CLI + cloud if applicable), browser agents, computer-using agent APIs, tool integration protocols (e.g., MCP), orchestrators/agents SDKs, plugin/action systems, remote tool servers.
E. Media Stack: image, video, audio/voice, editing/inpainting, streaming, quality tiers.
F. Policy/Governance Surface: data usage, training opt-outs, safety restrictions, enterprise guarantees, regional constraints.

For each leaf node in the taxonomy, include:
- Product/feature name
- Where it lives (ChatGPT / API / app / CLI)
- Access gates (tier, region, platform, waitlist)
- Status (GA / Beta / Preview / Deprecated / Rumored)
- Primary first-party reference

2) "TAX CODE" SERVICE CATALOG MATRIX (THE CORE TABLES)
Create a master matrix with rows = services/features and columns = tiers:
- Free / Plus / Pro / Business (or Team) / Enterprise / API
For each cell, indicate:
- Included? (Y/N)
- If Y: limit/quota/rate limit AND reset window
- Notes on gating (platform/region/cohort)
- Evidence reference (ledger ID)

Important: Separate matrices for:
2.1 Models (by family): include context windows, modalities, tool availability, routing/priority differences.
2.2 Agentic tools (Codex, agent mode, browser/desktop agents, research agents, etc.)
2.3 Media generation (image/video/voice): include credits, watermarking, resolutions/durations, concurrency.
2.4 Data tools (code interpreter/data analysis, file uploads, connectors, export, etc.)
2.5 Governance/org features (admin, security, compliance)

3) LIMITS & QUOTAS: OFFICIAL VS OBSERVED
Make a "Limits Ledger" table for Plus (and Pro if meaningfully different):
- official limits (if published)
- community-measured/observed limits (if not published)
- method of observation (how people measured)
- confidence
Explicitly cover: message caps per model, image gen windows, video credits, deep research runs, voice minutes, file caps, project caps, context windows.

4) DEPRECATION / MIGRATION / ROADMAP SIGNALS
4.1 Deprecation table: what is being sunset, by when, replacement, migration steps.
4.2 Rename/merge table (Radar): former name → current surface.
4.3 "Likely-to-change" watchlist: 10–20 items most subject to velocity, with suggested re-check frequency.

5) CODEX & "DEVELOPER-AGENT" DEEP DIVE (TECHNICAL)
Mirror a serious architecture review:
- interaction modes (interactive/headless)
- permissions/sandbox model
- persistent context conventions
- tool/plugin integrations (MCP or equivalents)
- GitHub integrations (PR review, bots, Actions, etc.)
- context management/compaction strategies
- parallelization patterns
Include: a side-by-side comparison with Claude Code and a "routing rule-of-thumb" section.

6) BROWSER / COMPUTER AGENTS (UI + API)
Clarify current state of:
- ChatGPT agent mode inside ChatGPT
- any dedicated browser product
- any deprecated predecessors
For each: capabilities, restrictions (logins, payments, sensitive sites), autonomy level, error recovery, and whether API access exists. Include benchmark claims only with evidence.

7) UNIQUE CAPABILITIES VS CLAUDE (SUBSCRIPTION JUSTIFICATION)
Create two lists:
7.1 "No Claude Equivalent" (pure additive) with concrete workflows.
7.2 "Overlap but Valuable for Verification" (second-opinion / bias-differential / redundancy) with examples.

8) INTEGRATION ARCHITECTURE FOR A CLAUDE-CENTRIC CONSTELLATION
Provide:
- a routing decision tree (what tasks go to OpenAI vs Claude vs Gemini)
- an integration blueprint (UI handoffs + API handoffs)
- a tool-layer strategy (e.g., shared tool protocol servers) if applicable
- operational concerns: reliability, logging, privacy, reproducibility

9) COST / VALUE MODEL
Compute and explain:
- subscription economics (Plus vs Pro vs Business seats)
- API economics (token/video/image/audio)
- break-even thresholds for typical workloads
- recommended configuration for the stated stack (Claude as primary) with explicit triggers to upgrade/downgrade

10) APPENDICES (REQUIRED)
A) Evidence Ledger (all claims)
B) Source Map (grouped by first-party, docs, help center, GitHub, app stores, practitioner/community)
C) "Known Unknowns" + how to resolve (what you could not verify and what experiment/search would verify it)
D) Re-run Playbook (how to redo this report monthly/quarterly without missing releases)

OUTPUT CONSTRAINTS
- Prefer short excerpts and direct quotes in the Evidence Ledger rather than long paraphrase.
- No filling unknowns with "best guesses". Unknown is acceptable; silent invention is not.
- When a source conflicts with another, show the conflict and resolution rule.
- Keep the top-level report readable; push dense evidence into the appendices.

STARTING INSTRUCTIONS (DO THIS FIRST)
1) Build the inventory via Surface-Area Scan (Rule C).
2) Only after inventory is complete: populate matrices, then limits, then deep dives, then integration/cost.
3) Produce the final report in the required structure, with the Evidence Ledger appended.

END STATE
The report must function as:
- a living "tax code" reference,
- a decision engine for Plus vs Pro vs API,
- and an integration manual for Claude-centric orchestration.