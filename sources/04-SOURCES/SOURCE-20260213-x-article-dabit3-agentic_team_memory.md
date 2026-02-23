---
id: SOURCE-20260213-001
title: Agentic Team Memory
platform: x
format: article
creator: dabit3
date_published: 20260213
status: triaged
original_filename: "research-notebooks/03-agent-memory-systems/20260213-x_article-agentic_team_memory-@dabit3.md"
aliases:
  - "Devin Agentic Team Memory"
  - "Nader Dabit Team Knowledge"
teleology: extract
notebooklm_category: ai-agents
synopsis: "Nader Dabit describes Cognition's approach to team knowledge capture through Devin: instead of asking engineers to write docs, the system captures corrections they already make ('don't call fetch directly, use the wrapper') and suggests persisting them as knowledge items. Knowledge accumulates from chat feedback, auto-generated repo scans, and manual creation — scoped per-repo or org-wide."
key_insights:
  - "Knowledge that writes itself stays current — capturing corrections engineers already make eliminates the documentation maintenance burden that kills wikis"
  - "Multi-source knowledge ingestion (chat corrections, repo scans of CLAUDE.md/.cursorrules, manual creation) creates comprehensive coverage without dedicated documentation effort"
  - "Scoped knowledge (per-repo vs org-wide) prevents context pollution — backend deployment conventions don't surface during frontend work"
topics:
  - ai-agents
  - ai-engineering
  - developer-tools
  - best-practices
signal_tier: strategic
url: "https://x.com/dabit3/status/2022459842342916559"
author: "nader dabit (@dabit3)"
captured_date: 2026-02-13
---

# Agentic Team Memory

(Description: Abstract header image with a geometric pattern of blue and orange squares, circles, diamonds, and triangular shapes in white, arranged in a dynamic composition)

Every engineering team has tribal knowledge.

Most teams try to capture this in wikis, READMEs, or onboarding docs. These go stale fairly quickly. Nobody maintains them because the cost of writing documentation always loses to the cost of shipping features.

New engineers take more time to ramp up, senior engineers lose hours answering the same questions, and the same mistakes still keep happening because conventions live in people's heads vs in some up-to-date system.

## Making it a side effect

At @cognition we capture knowledge from corrections they're already making instead of asking people to write docs.

When an engineer says "don't call fetch directly, use the wrapper in src/lib/api-client", @DevinAI suggests saving that as a knowledge item. The engineer reviews it, tweaks the wording if needed, and saves.

From that point on every future session across the org retrieves that knowledge when it's relevant.

You don't have to think about documentation while you're working, you just correct the agent the way you'd correct a teammate, and the system prompts you to persist what's worth keeping.

## Multiple sources

Chat feedback is the most organic source, but knowledge also gets created in other ways:

- **Auto-generated from repos**: When you connect a repo, Devin scans your READMEs, file structure, and contents. It also pulls from AGENTS.md, CLAUDE.md, .cursorrules, and .rules files.

- **Updates to existing items**: Devin suggests updates to knowledge that's already saved, not just new items. Conventions evolve; the knowledge base evolves with them.

- **Manual creation**: Add knowledge directly in the UI or via the API when you want to codify something upfront.

## The result

The team's conventions, deployment quirks, internal library preferences, and common pitfalls accumulate. Nobody sat down and wrote an onboarding guide. It emerged from corrections people were already making.

A new engineer joins, starts a session, and the agent already knows every convention the team has built up without having to read docs or search Slack etc.

This also lowers the barrier for who can contribute, as non-technical people have more guardrails. You can pin knowledge to a specific repo or apply it org-wide. Backend deployment conventions don't surface when someone's working on the marketing site. Org-wide standards like commit message format apply everywhere.

Knowledge that writes itself is knowledge that actually stays current.

---

**Post metadata**: 5 replies, 10 reposts, 109 likes, 196 bookmarks, 20,068 views
**Timestamp**: 3:56 PM · Feb 13, 2026