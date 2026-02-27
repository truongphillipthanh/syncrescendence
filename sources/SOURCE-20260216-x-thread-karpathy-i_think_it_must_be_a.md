---
url: https://x.com/karpathy/status/2023476423055601903
author: "@karpathy"
captured_date: 2026-02-16
id: SOURCE-20260216-022
original_filename: "20260216-x_thread-i_think_it_must_be_a-@karpathy.md"
status: triaged
platform: x
format: thread
creator: karpathy
signal_tier: paradigm
topics: [ai-engineering, llm-architecture, developer-tools]
teleology: synthesize
notebooklm_category: ai-engineering
aliases: ["karpathy - programming languages optimized for LLMs"]
synopsis: "Karpathy observes that LLMs fundamentally change the constraints landscape of programming languages. LLMs are especially good at code translation (original code acts as detailed prompt + reference for tests). Rust is nowhere near optimal as an LLM target language - an entirely new kind of language may be needed. Predicts large fractions of all software will be rewritten many times."
key_insights:
  - "LLMs excel at translation over de novo generation - original code is a detailed prompt and test reference"
  - "What language is optimal for LLMs as a target? Current languages were designed for human constraints that no longer apply"
  - "We will likely rewrite large fractions of all software ever written many times over"
---
# Andrej Karpathy on Programming Languages and LLMs
I think it must be a very interesting time to be in programming languages and formal methods because LLMs change the whole constraints landscape of software completely. Hints of this can already be seen, e.g. in the rising momentum behind porting C to Rust or the growing interest in upgrading legacy code bases in COBOL or etc. In particular, LLMs are *especially* good at translation compared to de-novo generation because 1) the original code base acts as a kind of highly detailed prompt, and 2) as a reference to write concrete tests with respect to.
That said, even Rust is nowhere near optimal for LLMs as a target language. What kind of language is optimal? What concessions (if any) are still carved out for humans? Incredibly interesting new questions and opportunities. It feels likely that we'll end up re-writing large fractions of all software ever written many times over.
---
**Note:** This post quotes Thomas Wolf's thread "Shifting structures in a software world dominated by AI. Some first-order reflections (TL;DR at the end): Reducing software supply chains, the return of software monoliths – When rewriting code and understanding large foreign codebases becomes cheap, the incentive to rely on..."
**Post metadata:** 11:15 AM · Feb 16, 2026 · 1M Views · 670 replies · 774 reposts · 7.9K likes · 3.7K bookmarks