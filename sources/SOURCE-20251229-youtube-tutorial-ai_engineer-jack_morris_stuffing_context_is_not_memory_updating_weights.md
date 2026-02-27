---
id: SOURCE-20251229-697
platform: youtube
format: tutorial
cadence: evergreen
value_modality: audio_primary
signal_tier: paradigm
status: raw
chain: null
topics:
  - "jack"
  - "morris"
  - "stuffing"
  - "context"
  - "memory"
creator: "AI Engineer"
guest: null
title: "Jack Morris: Stuffing Context is not Memory, Updating Weights is"
url: "https://www.youtube.com/watch?v=Jty4s9-Jb78"
date_published: 2025-12-29
date_processed: 2026-02-22
date_integrated: null
processing_function: transcribe_youtube
integrated_into: []
duration: "1h 2m 44s"
has_transcript: no
synopsis: "Jack Morris: Stuffing Context is not Memory, Updating Weights is by AI Engineer. A tutorial covering jack, morris, stuffing."
key_insights: []
visual_notes: null
teleology: synthesize
notebooklm_category: ai-engineering
aliases:
  - "Jack Morris: Stuffing Context"
  - "Jack Morris: Stuffing Context is not"
---

# Jack Morris: Stuffing Context is not Memory, Updating Weights is

**Channel**: AI Engineer
**Published**: 2025-12-29
**Duration**: 1h 2m 44s
**URL**: https://www.youtube.com/watch?v=Jty4s9-Jb78

## Description (no transcript available)

Understanding how memory works in large language models through the lens of weights and activations. This workshop will explore the internal mechanisms of how LLMs store and retrieve information during inference.

https://x.com/jxmnop

**Summary**
Jack Morris discusses the limitations of current Large Language Models (LLMs) in handling niche, "long-tail" knowledge that falls outside their training data or within knowledge cutoffs. He critiques the reliance on massive context windows and Retrieval Augmented Generation (RAG) due to their high cost and latency (quadratic complexity of self-attention). The core thesis advocates for a third paradigm: **"training things into weights,"** or efficiently injecting specific knowledge directly into model parameters, effectively treating weights as a memory storage mechanism distinct from the "working memory" of activations.

**Timestamps**

00:00 The Knowledge Cutoff & Long-Tail Problem
02:22 Three Methods for Knowledge Injection (Context, RAG, Weights)
03:29 Limitations of "Full Context" (Cost & Latency)
05:12 The Transformer Bottleneck: Self-Attention Complexity
06:49 Context Rot: Performance degradation in long context
58:49 Q&A: The Return of Federated Learning
59:34 Q&A: Specialized Knowledge Models vs. Karpathy’s "Reasoning Engines"
01:01:21 Q&A: Temporal Information & Future Research

**Technical Summary**

* **The "Long Tail" Knowledge Problem**: Morris identifies a critical failure mode in current LLMs: they excel at general knowledge (e.g., "Did the Blue Jays win the World Series?") but fail catastrophically at **niche, specific tasks** (e.g., "Optimize this AMD GPU kernel" or "What are the terms of the BlackRock partnership?").
* *Constraint*: These tasks are either outside the training data, subject to knowledge cutoffs, or require private data.
* *Failure of Prompting*: No amount of "please" or prompt engineering can force a model to know facts it simply doesn't have stored.


* **The Three Paradigms of Knowledge Injection**:
* **Full Context**: Stuffing all relevant data into the prompt. Works for small domains (e.g., a single medical record) but scales poorly.
* **RAG (Retrieval Augmented Generation)**: Retrieving only relevant chunks.
* **Training into Weights**: The proposed solution. Injecting knowledge directly into the model's parameters (weights) rather than its transient state (activations).


* **The "Context Trap": Cost and Latency**:
* **Quadratic Dependency**: The self-attention mechanism in Transformers requires every token to look at every other token, creating a quadratic compute cost.
* **Latency Impact**: Morris shares benchmarks: "If you have 1,000 tokens of context, we can output **10,000 tokens per second**. If you have 128k tokens of context, we can output **130 tokens per second**." This is an orders-of-magnitude slowdown.
* **Performance Degradation**: He cites the *Chroma "Context Context Broad"* report, showing that as context grows, reasoning capabilities degrade even if the model doesn't "break".


* **Weights vs. Activations (Inferred from thesis)**:
* The talk distinguishes between **activations** (short-term, expensive context) and **weights** (long-term, efficient storage).
* Morris argues that for niche, static knowledge (like internal company wikis or specialized codebases), updating weights is more efficient than re-feeding context every inference cycle.


* **Q&A: Federated Learning & Distributed Training**:
* Federated learning (training across many machines) failed previously due to network costs of syncing massive models.
* Morris predicts a comeback because "you only need to train a million parameters instead of a trillion," making the network overhead manageable for specialized knowledge updates.


* **Q&A: Specialized Models vs. General Reasoners**:
* Responding to Andrej Karpathy's view of LLMs as pure "reasoning engines" (small brains, using tools), Morris argues there is a middle ground.
* *Analogy*: "A lawyer doesn't have the entire legal code memorized, but they know how to use tools." However, a model that "knows nothing" is inefficient. He advocates for **specialized models** that are "good at something you care about but bad at other things," rather than a generic reasoning engine that relies entirely on external retrieval.
