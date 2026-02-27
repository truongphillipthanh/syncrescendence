---
id: SOURCE-20251228-704
platform: youtube
format: tutorial
cadence: evergreen
value_modality: audio_primary
signal_tier: strategic
status: raw
chain: null
topics:
  - "one"
  - "year"
  - "mcp"
  - "david"
  - "soria"
creator: "Latent Space"
guest: null
title: "One Year of MCP — with David Soria Parria and AAIF leads from OpenAI, Goose, Linux Foundation"
url: "https://www.youtube.com/watch?v=z6XWYCM3Q8s"
date_published: 2025-12-28
date_processed: 2026-02-22
date_integrated: null
processing_function: transcribe_youtube
integrated_into: []
duration: "1h 39m 19s"
has_transcript: no
synopsis: "One Year of MCP — with David Soria Parria and AAIF leads from OpenAI, Goose, Linux Foundation by Latent Space. A tutorial covering one, year, mcp."
key_insights: []
visual_notes: null
teleology: implement
notebooklm_category: agents-orchestration
aliases:
  - "One Year of MCP"
  - "One Year of MCP — with"
---

# One Year of MCP — with David Soria Parria and AAIF leads from OpenAI, Goose, Linux Foundation

**Channel**: Latent Space
**Published**: 2025-12-28
**Duration**: 1h 39m 19s
**URL**: https://www.youtube.com/watch?v=z6XWYCM3Q8s

## Description (no transcript available)

One year ago, Anthropic launched the *Model Context Protocol (MCP)*—a simple, open standard to connect AI applications to the data and tools they need. Today, MCP has exploded from a local-only experiment into the de facto protocol for agentic systems, adopted by OpenAI, Microsoft, Google, Block, and hundreds of enterprises building internal agents at scale. And now, MCP is joining the newly formed *Agentic AI Foundation (AAIF)* under the Linux Foundation, alongside Block's *Goose* coding agent, with founding members spanning the biggest names in AI and cloud infrastructure.
We sat down with *David Soria Parra* (MCP lead, Anthropic), *Nick Cooper* (OpenAI), *Brad Howes* (Block / Goose), and *Jim Zemlin* (Linux Foundation CEO) to dig into the one-year journey of MCP—from Thanksgiving hacking sessions and the first remote authentication spec to long-running tasks, MCP Apps, and the rise of agent-to-agent communication—and the behind-the-scenes story of how three competitive AI labs came together to donate their protocols and agents to a neutral foundation, why enterprises are deploying MCP servers faster than anyone expected (most of it invisible, internal, and at massive scale), what it takes to design a protocol that works for both simple tool calls _and_ complex multi-agent orchestration, how the foundation will balance taste-making (curating meaningful projects) with openness (avoiding vendor lock-in), and the 2025 vision: MCP as the communication layer for asynchronous, long-running agents that work while you sleep, discover and install their own tools, and unlock the next order of magnitude in AI productivity.
We discuss:

* The *one-year MCP journey:* from local stdio servers to remote HTTP streaming, OAuth 2.1 authentication (and the enterprise lessons learned), long-running tasks, and MCP Apps (iframes for richer UI)
* Why *MCP adoption is exploding internally* at enterprises: invisible, internal servers connecting agents to Slack, Linear, proprietary data, and compliance-heavy workflows (financial services, healthcare)
* The *authentication evolution:* separating resource servers from identity providers, dynamic client registration, and why the March spec wasn't enterprise-ready (and how June fixed it)
* How *Anthropic dogfoods MCP:* internal gateway, custom servers for Slack summaries and employee surveys, and why MCP was born from "how do I scale dev tooling faster than the company grows?"
* *Tasks:* the new primitive for long-running, asynchronous agent operations—why tools aren't enough, how tasks enable deep research and agent-to-agent handoffs, and the design choice to make tasks a "container" (not just async tools)
* *MCP Apps:* why iframes, how to handle styles and branding, seat selection and shopping UIs as the killer use case, and the collaboration with OpenAI to build a common standard
* The *registry problem:* official registry vs. curated sub-registries (Smithery, GitHub), trust levels, model-driven discovery, and why MCP needs "npm for agents" (but with signatures and HIPAA/financial compliance)
* *Code mode vs. MCP:* why they're complementary (MCP is connectivity, code mode is optimization), and how Anthropic trains models with "opinions" about tools (preferring rg over grep)
* The *founding story of AAIF:* how Anthropic, OpenAI, and Block came together (spoiler: they didn't know each other were talking to Linux Foundation), why neutrality matters, and how Jim Zemlin has never seen this much day-one inbound interest in 22 years

—
David Soria Parra (Anthropic / MCP)

* MCP: https://modelcontextprotocol.io

Nick Cooper (OpenAI)

* X: https://x.com/nicoaicopr

Brad Howes (Block / Goose)

* Goose: https://github.com/block/goose

Jim Zemlin (Linux Foundation)

* LinkedIn: https://www.linkedin.com/in/zemlin/

Agentic AI Foundation

* https://agenticai.foundation

00:00:00 Introduction: MCP's First Year and Foundation Launch
00:01:17 MCP's Journey: From Launch to Industry Standard
00:02:06 Protocol Evolution: Remote Servers and Authentication
00:08:52 Enterprise Authentication and Financial Services
00:11:42 Transport Layer Challenges: HTTP Streaming and Scalability
00:15:37 Standards Development: Collaboration with Tech Giants
00:34:27 Long-Running Tasks: The Future of Async Agents
00:30:41 Discovery and Registries: Building the MCP Ecosystem
00:30:54 MCP Apps and UI: Beyond Text Interfaces
00:26:55 Internal Adoption: How Anthropic Uses MCP
00:23:15 Skills vs MCP: Complementary Not Competing
00:36:16 Community Events and Enterprise Learnings
01:03:31 Foundation Formation: Why Now and Why Together
01:07:38 Linux Foundation Partnership: Structure and Governance
01:11:13 Goose as Reference Implementation
01:17:28 Principles Over Roadmaps: Composability and Quality
01:21:02 Foundation Value Proposition: Why Contribute
01:27:49 Practical Investments: Events, Tools, and Community
01:34:58 Looking Ahead: Async Agents and Real Impact
