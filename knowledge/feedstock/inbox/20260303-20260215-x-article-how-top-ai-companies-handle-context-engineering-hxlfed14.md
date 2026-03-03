---
url: https://x.com/hxlfed14/status/2022984467380682856
author: Himanshu (@Hxlfed14)
captured_date: 2026-02-15
---
# How Top AI Companies Handle Context Engineering
The companies building the most capable AI agents today: @Manus, @cursor_ai, @AnthropicAI, @OpenAI, @GoogleDeepMind, @LangChain are all solving the same problem: what information should an LLM see, when should it see it, and how should it be structured?
What is interesting is that these companies have been publishing their approaches openly through detailed blog posts, SDK cookbooks, research papers.
Each started from different constraints and arrived at different solutions. Some of those solutions converge. Some directly contradict each other.
I went through all of it. This article breaks down what each company does, compares their strategies head-to-head, and maps the techniques that are emerging as industry standard versus those that remain experimental.
## Sources analyzed
(All sources listed at the end of the article)
(Description: A dark table with six rows listing companies and their published sources. Columns: Company, Source, Published. Companies listed: Manus, Cursor, Anthropic, OpenAI, Google DeepMind, LangChain)
## The Core Problem
Every company here faces the same constraint: **context windows are finite, and agents generate tokens exponentially.**
A typical @ManusAI task involves ~50 tool calls. Each appends observations to the context. Without intervention, the window fills and performance degrades: "context rot."
The companies frame this differently, Anthropic calls it an "attention budget" problem, LangChain uses the "context window = RAM" analogy but all converge on the same conclusion: **smarter context management beats bigger context windows.**
## How Each Company Does It
### @ManusAI: "Six Principles from Production"
**Context:** Manus serves millions of users. A typical task averages 50 tool calls with a 100:1 input-to-output token ratio.
They have rewritten their agent framework four times each time after discovering a better way to shape context. They call this process **"Stochastic Gradient Descent"**
**Six principles, condensed:**
- **KV-Cache is sacred.** Cached tokens cost $0.30/MTok vs $3/MTok uncached (10x). Keep the prompt prefix stable, logs append-only. Even reordered JSON keys invalidate the cache.
(Description: Two side-by-side diagrams titled "Design Around the KV-Cache." Left diagram shows CONTEXT @ step 0 with Instruction, Actions 1-2, Observations 1-3, and CONTEXT @ step n+1 with similar structure. Annotations show "Cache Hit" and "Cache Miss" in red. Right diagram shows the same with correct caching. An X mark indicates the bad approach on the left, a checkmark indicates the correct approach on the right.)
- **Logit masking over tool removal.** All tools stay loaded permanently. Availability per step is controlled by constraining output token probabilities during decoding. Context stays stable; only behavioral constraints change.
(Description: Two diagrams titled "Mask, Don't Remove." Both show CONTEXT @ step 0 and CONTEXT @ step n+1 with Instruction blocks. Left side shows Tool A, Tool B, Tool C in different colors (some marked with X). Right side shows Tool A in blue, Tool B in green, Tool C in red. Checkmark on right indicates correct approach.)
- **File system as extended memory.** Large observations go to files; only lightweight references stay in context. Compression is fine as long as it is reversible.
- **Attention manipulation via recitation.** A living todo.md is updated and re-read every step, placing the current objective in the high-attention zone (end of context).
(Description: Two diagrams titled "Manipulate Attention Through Recitation." Left shows CONTEXT @ step 0 with Objectives, Actions 1-2, Observations 1-3, and an X mark. Right shows CONTEXT @ step n+1 with Objectives highlighted in green at the top and bottom, with an X mark on the left and checkmark on the right.)
- **Errors preserved, not cleaned.** Failed actions stay in context for implicit belief updating, reducing repeated mistakes.
- **Structured variation against fixation.** Different serialization templates and phrasing across iterations prevent the model from falling into rigid, repetitive patterns.
### @cursor_ai: "Dynamic Context Discovery"
**Context:** Their Jan 2026 research blog describes five techniques they developed after observing that as