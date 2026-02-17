---
id: SOURCE-20251222-youtube-interview-mlst-categorical_deep_learning
title: "MLST: Categorical Deep Learning - From Alchemy to Science"
creator: Machine Learning Street Talk
guest: Bruno Gavranovic (presumably)
date_published: 2025-12-22
date_processed: 2026-01-05
signal_tier: paradigm
status: processed
chain_relevance: Intelligence, Knowledge
integration_targets: CANON-30000, CANON-30410, CANON-00016
---

# MLST: Categorical Deep Learning - From Alchemy to Science

## Executive Summary

A paradigm-shifting framework arguing that deep learning is currently in its "alchemy phase" and needs category theory to become a systematic science. Demonstrates that LLMs fundamentally cannot perform addition—they learn patterns that work most of the time but fail when computational structure matters. Proposes categorical deep learning as the bridge between constraints and implementation, recovering geometric deep learning as a special case while naturally expressing recursion, weight tying, and non-invertible computation.

## Key Insights

### LLM Arithmetic Failure
"Language models cannot do addition. Not really." Demonstrates that when you change one digit in a trick problem (changing an eight to a seven), the model fails because "it has to actually know what it's doing. It has to walk up, hit the seven, and stop propagating zeros. And it simply fails."

### Tool Use is Insufficient
"Just because we can achieve some level of progress by hooking up a really potent tool to a language model doesn't mean we shouldn't think about what the next generation of these models should look like." Even frontier models perform hundreds of billions of multiplications to produce one token yet cannot reliably multiply small numbers—"a great misalignment between what we are training these systems to do."

### From Alchemy to Science
"Right now, deep learning is in its alchemy phase. We have powerful results, but we lack a unifying theory that tells us how to systematically design architectures for specific tasks." Category theory provides the systematic framework—"Lego-like approach to building neural architectures."

### Synthetic vs. Analytic Mathematics
Shift from "what things are made of" to "how things behave and relate." In synthetic terms, a vector is defined by what you can do with it (add, scale, combine), not as a tuple of numbers. "This turns out to be exactly the right level of abstraction for designing neural networks."

### The Mathematics of Carrying
"There's something very basic in mathematics that we all learned in elementary school that has been overlooked in the design of graph neural networks: the notion of a carry." Describes how carry operations are fundamentally at odds with how GNNs work—"In traditional GNNs, you send the whole state between nodes. But with carries, the information isn't in the state—it's only in the change of state."

### Hopf Fibration Connection
The simplest geometric example of carry-like behavior occurs in three-dimensional manifolds. The Hopf fibration shows how ℤ mod 100 differs fundamentally from the product of ℤ mod 10 with ℤ mod 10—pointing toward how to "start building actual CPUs in neural networks."

## Quotable Passages

> "If we want AI to solve the world's hardest scientific problems, it can't just be a stochastic parrot. It needs to internalize the rules of logic and computation. By imbuing neural networks with categorical priors, we're attempting to build a future where AI doesn't just predict the next word—it understands the underlying structure of the universe."

> "Think of category theory as 'algebra with colors'—a way of doing mathematics where you can only compose operations when their types match, like magnets that only snap together when the colors align. This partial compositionality is the secret to building more complex internal reasoning."

> "Group theory is powerful for describing reversible symmetries, but much of computation is fundamentally irreversible. When you compress information, when you aggregate data in a graph neural network, when you fold a list down to a single value—these operations destroy information."

## Integration Notes

- **CANON-30000 (Intelligence Chain)**: Fundamental architecture critique of LLM limitations; validates need for hybrid approaches
- **CANON-30410 (Cognitive Architecture)**: Category theory as principled framework for neural architecture design
- **CANON-00016 (Ontological Framework)**: Synthetic vs. analytic mathematics as epistemological distinction; structure-behavior over substance
- Novel contribution: Mathematical rigor on why LLMs fail at algorithmic tasks; Hopf fibration as geometric basis for discrete computation in continuous systems
