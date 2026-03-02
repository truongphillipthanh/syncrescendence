# Neural Memory Architectures

## What the Sources Actually Say

Google published research on "Titans" and "MIRAS" (referenced as "Mira" in some coverage) under the framing of helping AI have long-term memory. A December 2025 Wes Roth video (09623.md) describes these as papers on long-term memory and "surprise" metrics in AI, linking to a Google research blog post titled "Titans + MIRAS: Helping AI have long-term memory." The video timeline notes a segment at 04:40 titled "Google Research: Titans, Mira & Long-Term Memory" and another at 06:00 titled "The 'Surprise' Metric: How AI Learns Like Humans." No transcript is available; the corpus file contains only the video description and metadata.

The source does not explain what Titans or MIRAS actually do architecturally, what the surprise metric measures, how it modulates attention, or what the claimed memory mechanism is. The entry in 09623.md is a brief description-level mention within a video covering multiple unrelated topics (Grok 4.20, OpenAI "Code Red," Google TPU sales, SpaceX data centers).

## Platform Memory Convergence (Verified)

The mid-January 2026 platform survey (08814.md) documents convergence across major AI platforms toward persistent and personalized memory features:

- **Gemini Personal Intelligence** (beta, January 14 2026): Opt-in feature connecting Gmail, Photos, YouTube, and Search for proactive, hyper-personalized responses. Described as bridging "memory gaps for Google users."
- **ChatGPT improved memory** (January 15 2026): Better detail recall from past chats for Plus/Pro users.
- **Claude project memory**: Described as project-scoped, with API enhancements bridging GUI-API gaps. "Memory remains project-scoped" per the survey.

The survey frames this as "convergence in memory architectures" across platforms, though the implementations described are external/session-level memory systems (connected apps, chat history recall), not architectural changes to model weights.

## What Is Not Supported by Sources

The following claims have no basis in the corpus files:

- Detailed mechanics of how Titans or MIRAS implement memory as learnable parameters
- The surprise metric as a specific mechanism for attention allocation
- Any claim about retrieval latency elimination
- Neural memory enabling long-term memory without long context windows
- RAG having a hard ceiling or being complementary to neural memory
- Convergence of Titans with Complementary Learning Systems neuroscience
- The context window arms race being misdirected
- Write-read asymmetry as a property of neural memory systems

---

## Syncrescendence Operational Notes

*Claims specific to Syncrescendence operations, not derivable from corpus sources.*

Agent memory in the constellation currently lives in external systems: project files, handoff documents, MEMORY.md. Whether future model architectures could internalize this state is an open architectural question that the current sources do not address.

---

## Source Provenance

| Source | File | Actual Content |
|--------|------|----------------|
| Wes Roth — Dec 2025 AI news roundup | `corpus/ai-models/09623.md` | Brief mention of Titans + MIRAS papers on long-term memory and surprise metrics; no transcript, no technical detail |
| Frontier AI platform survey (mid-Jan 2026) | `corpus/ai-models/08814.md` | Platform-level memory feature rollouts: Gemini Personal Intelligence, ChatGPT memory improvements, Claude project memory |
| Wes Roth — AI in 2026 outlook | `corpus/ai-models/10270.md` | Generic AI news video; no transcript, no technical content relevant to neural memory |

---

*Compendium entry 8 of 21 -- ai-models*
*Remediated: 2026-03-02 — stripped fabricated claims; entry reflects only source-supported content*
