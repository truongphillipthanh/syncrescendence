---
id: SOURCE-20260108-525
platform: youtube
format: tutorial
cadence: evergreen
value_modality: audio_primary
signal_tier: tactical
status: raw
chain: null
topics:
  - "dspy"
  - "end"
  - "prompt"
  - "engineering"
  - "kevin"
creator: "AI Engineer"
guest: null
title: "DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners"
url: "https://www.youtube.com/watch?v=-cKUW6n8hBU"
date_published: 2026-01-08
date_processed: 2026-02-22
date_integrated: null
processing_function: transcribe_youtube
integrated_into: []
duration: "1h 13m 13s"
has_transcript: no
synopsis: "DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners by AI Engineer. A tutorial covering dspy, end, prompt."
key_insights: []
visual_notes: null
teleology: implement
notebooklm_category: prompt-engineering
aliases:
  - "DSPy: The End of"
  - "DSPy: The End of Prompt Engineering"
---

# DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners

**Channel**: AI Engineer
**Published**: 2026-01-08
**Duration**: 1h 13m 13s
**URL**: https://www.youtube.com/watch?v=-cKUW6n8hBU

## Description (no transcript available)

Applications developed for the enterprise need to be rigorous, testable, and robust. The same is true for applications that use AI, but LLMs can make this challenging. In other words, you need to be able to program with LLMs, not just tweak prompts. In this talk we'll cover why DSPy really is all you need in building applications with LLMs. We'll dive into real-world examples where we have successfully automated manual work using an opinionated DSPy-first approach to structuring applications, covering everything from simple modules to using SoTA optimizers to measurably improve performance.

https://x.com/kmad/


**Summary**
Kevin Madura, a consultant at AlixPartners, argues that building robust enterprise AI applications requires shifting from brittle "prompt engineering" to "programming with LLMs" using **DSPy**. He contends that prompts should be treated as implementation details optimized by the system, while developers focus on defining typed interfaces (Signatures) and modular logic (Modules). The session moves from a conceptual overview of DSPy's primitives—Signatures, Modules, Adapters, and Optimizers—to a live code walkthrough. Madura demonstrates real-world use cases, including a complex pipeline that routes files by type (SEC filings vs. contracts) and a "boundary detector" that uses visual layout to segment legal documents. The talk concludes with a demonstration of how Optimizers (like MIPRO) can automatically tune these programs to outperform manual baselines, followed by a Q&A on production costs and feedback loops.

**Timestamps**

00:00 Introduction & The Enterprise AI Challenge
07:12 The 6 Core Concepts of DSPy (Signatures, Modules, Adapters)
13:23 Deep Dive: Class-based vs. Shorthand Signatures
19:57 Adapters: Controlling the Prompt Format (JSON vs. BAML)
24:17 Optimizers: The "Killer Feature" for Transferability
31:08 Code Walkthrough: Setup & Model Mixing
36:24 Handling Documents: "Poor Man's RAG" with Attachments
42:10 Adapter Comparison: Improving Token Efficiency with BAML
47:20 Optimizers in Practice: Creating Datasets & Metrics
51:13 Complex Pipeline: Routing & Classifying Arbitrary Files
56:00 Advanced Use Case: PDF Boundary Detection via Visuals
01:01:22 Analyzing Optimization Results & The "DSPy Hub" Concept
01:09:02 Q&A: Handling Delayed Feedback & Online Learning
01:13:00 Conclusion
