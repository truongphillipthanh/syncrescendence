# Claude Opus 4.6 vs 4.5: What changed

**Claude Opus 4.6, released February 5, 2026, is a major upgrade over Opus 4.5 that doubles the output limit, introduces a 1M-token context window, and nearly doubles reasoning scores on hard benchmarks — all at the same price.** The model, accessed via the API string `claude-opus-4-6`, shifts Anthropic's flagship from a coding-focused powerhouse to a broader enterprise workhorse capable of financial analysis, multi-agent coordination, and long-horizon agentic tasks. Opus 4.5 launched just 73 days earlier on November 24, 2025, and itself represented a steep price cut and capability jump over Opus 4.1. Together, the two releases mark the fastest back-to-back Opus upgrades in Anthropic's history, reflecting intensifying competition with OpenAI's GPT-5.2 and Google's Gemini 3 Pro.

## Benchmarks reveal targeted gains — and two regressions

The performance gap between the models varies sharply by domain. Opus 4.6 delivers its most dramatic improvement on **ARC AGI 2**, a benchmark testing problems easy for humans but hard for AI: it scores **68.8%** versus Opus 4.5's 37.6% — an 83% relative jump that also surpasses GPT-5.2 (54.2%) and Gemini 3 Pro (45.1%). On **GDPval-AA**, which measures economically valuable knowledge work, Opus 4.6 leads Opus 4.5 by **190 Elo points** and GPT-5.2 by 144 points, translating to roughly 70% win rates in head-to-head comparisons.

Coding benchmarks show solid but more modest progress. Terminal-Bench 2.0 improves from 59.8% to **65.4%**, and OSWorld (computer use) climbs from 66.3% to **72.7%**. BrowseComp, testing deep agentic web search, jumps from 67.8% to 84.0%. The τ2-bench retail score edges up from 88.9% to 91.9%, while the telecom score hits 99.3%.

Two areas show small regressions worth noting. **SWE-bench Verified** dips slightly from 80.9% to 80.8%, and **MCP Atlas** (tool usage) drops from 62.3% to 59.5%. Anthropic has not commented on these regressions, though The New Stack called them "a bit of an anomaly" given the model's strong performance on analogous agentic benchmarks. On long-context retrieval, Opus 4.6 scores **76% on MRCR v2** (8-needle, 1M tokens), compared to Sonnet 4.5's 18.5% — a metric that reflects the new context window capability rather than a direct Opus 4.5 comparison.

| Benchmark | Opus 4.5 | Opus 4.6 | Change |
|-----------|----------|----------|--------|
| Terminal-Bench 2.0 | 59.8% | 65.4% | +5.6 pp |
| SWE-bench Verified | 80.9% | 80.8% | −0.1 pp |
| OSWorld (computer use) | 66.3% | 72.7% | +6.4 pp |
| ARC AGI 2 | 37.6% | 68.8% | +31.2 pp |
| GDPval-AA Elo | ~1,416 | 1,606 | +190 |
| BrowseComp | 67.8% | 84.0% | +16.2 pp |
| MCP Atlas | 62.3% | 59.5% | −2.8 pp |
| τ2-bench (retail) | 88.9% | 91.9% | +3.0 pp |

## Context window, output limits, and pricing held flat

The most consequential technical change is the **1M-token context window**, available in beta via the `context-1m-2025-08-07` header. This is a first for any Opus-class model — previously only Sonnet 4.5 and Gemini models offered million-token contexts. Opus 4.6's max output doubles from **64K to 128K tokens**, enabling longer code generations and more extensive documents in a single API call.

Pricing remains unchanged at **$5 per million input tokens and $25 per million output tokens**, with prompt caching offering up to 90% savings and batch processing 50% savings. A new premium tier applies to the 1M context window: $10/$37.50 per million tokens for prompts exceeding 200K tokens. US-only data residency inference is available at a 10% premium (1.1× pricing). This pricing parity with Opus 4.5 is notable — Anthropic had previously cut prices by 67% when moving from Opus 4.1 ($15/$75) to Opus 4.5.

## Four new API features reshape developer workflows

Opus 4.6 introduces several features that change how developers interact with the model:

- **Adaptive thinking** (`thinking: {type: "adaptive"}`) replaces the binary on/off extended thinking toggle, letting the model dynamically decide when and how deeply to reason based on task complexity. At default "high" effort, the model almost always engages thinking; at lower levels, it may skip it for simple queries.
- **Effort parameter GA** with four levels (low, medium, high, max) is now generally available without a beta header, giving developers explicit control over the intelligence-speed-cost tradeoff. The new "max" tier provides the absolute highest capability.
- **Context compaction** (beta) enables automatic server-side context summarization, allowing effectively infinite conversations by summarizing earlier portions when context approaches the window limit.
- **Agent teams** in Claude Code let multiple AI agents work on different parts of a project in parallel — one on the frontend, another on the API, a third on database migration — coordinating directly with each other.

Two **breaking changes** affect existing integrations. Prefilling assistant messages (last-assistant-turn prefills) now returns a **400 error** rather than being silently accepted. The `output_format` parameter has been moved to `output_config.format`; the old parameter still works but is deprecated. Additionally, JSON string escaping in tool call arguments may differ slightly, though standard JSON parsers handle this automatically.

## Enterprise positioning and cybersecurity capabilities

Anthropic frames Opus 4.6 around "first-try" deliverables — the model's ability to find information, analyze it, and produce finished artifacts in a single pass with fewer revision cycles. New integrations reinforce this: **Claude in PowerPoint** (research preview) reads existing slide masters, fonts, and brand layouts to generate or edit decks without breaking templates, while **Claude in Excel** handles more complex multi-step spreadsheet operations.

The model's cybersecurity credentials are striking. During sandboxed pre-release testing, Anthropic's frontier red team gave Opus 4.6 access to standard security tools — Python, debuggers, fuzzers — with no specialized instructions. The model discovered **over 500 previously unknown zero-day vulnerabilities** in open-source software, each validated by Anthropic staff or external researchers. These ranged from crash-inducing flaws in GhostScript to buffer overflows in OpenSC and CGIF. "I wouldn't be surprised if this was one of — or the main way — in which open-source software moving forward was secured," said Logan Graham, head of Anthropic's frontier red team.

Safety evaluations show Opus 4.6 matching or exceeding Opus 4.5's profile across deception, sycophancy, and misalignment metrics. Anthropic published a detailed system card alongside the launch. Notably, Anthropic added new security controls to mitigate potential abuse of the model's enhanced cyber capabilities, including real-time detection tools that could block traffic deemed potentially malicious.

## Conclusion

The Opus 4.5-to-4.6 upgrade is less about raw intelligence gains and more about operational capability. The benchmarks that improved most — ARC AGI 2, BrowseComp, GDPval-AA — measure the kind of flexible reasoning and sustained effort that enterprise workflows demand, while the 1M context window and 128K output limit remove practical constraints that previously forced task fragmentation. The introduction of agent teams and adaptive thinking signals Anthropic's bet that the next competitive frontier is not just model quality but orchestration — how well AI coordinates complex, multi-step work. For developers migrating from Opus 4.5, the main friction points are the removal of assistant message prefilling and the `output_format` deprecation; beyond those, the `claude-opus-4-6` model string is a drop-in upgrade at identical pricing. The small regressions on SWE-bench and MCP Atlas warrant monitoring but appear to be narrow trade-offs against broad gains elsewhere.