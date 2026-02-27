# ARC-AGI v3 and Measuring Intelligence

## Executive Summary
Francois Chollet and Mike Knoop discuss ARC-AGI benchmark v3, which adds goal discovery, temporal planning, and interactive learning to v1/v2's passive model-fitting. They define intelligence as skill acquisition efficiency—how well you extract generalizable programs from experience. LLMs are not AGI because gradient descent is 4-5 orders of magnitude less efficient than human learning. Solving ARC v3 efficiently (without brute force) would demonstrate a micro-version of AGI properties that could scale to real-world applications.

## Key Insights

### Skill Acquisition Efficiency as Intelligence
Intelligence is defined not by what you know but by how efficiently you acquire skills and knowledge. The key is extracting programs from experience that generalize well. LLMs encode programs acquired via gradient descent, which is 4-5 orders of magnitude less sample-efficient than human learning.

### ARC v3 Additions
V3 adds critical capabilities beyond v1/v2's passive model-fitting:
- **Goal discovery**: Infer your own objectives from experience
- **Temporal planning**: Plan sequences of actions over time
- **Interactive learning**: Collect your own data by interacting with environment

### LLMs Are Not Sufficient
LLMs could be a component of AGI—the memory/knowledge representation layer. But the defining characteristic of general intelligence is efficient skill acquisition, which is precisely what LLMs lack. Gradient descent is the wrong algorithm for intelligence.

### Reasoning vs. Perception
ARC is fundamentally a reasoning benchmark, not a perception benchmark. The visual format is arbitrary—you could convert it to text or audio. What makes it hard is inferring the underlying rule/program. Reasoning models (o1, etc.) show perception isn't the bottleneck.

### Human-Level General Intelligence
"General" means the space of solvable tasks is vast and diverse (effectively infinite for humans). We're not targeting universal intelligence (any task whatsoever) but human-level generality. The "no free lunch" theorem suggests truly universal intelligence is impossible, but human-level generality is achievable.

### Micro-AGI Properties
Solving ARC v3 efficiently would demonstrate AGI-like properties on a small scale: efficient goal discovery, planning, interactive learning. The games are simple—any human can play them—but the underlying capabilities are what scale to real-world AGI.

### Program Synthesis + Deep Learning Merger
Real progress requires merging program synthesis (explicit symbolic reasoning) with deep learning (pattern recognition, knowledge representation). Neither alone is sufficient.

## Quotable Passages
> "LLMs are basically a way to acquire and encode programs. They're a repository for reusable vector programs acquired via gradient descent on human data. That's not what AGI is." — Francois Chollet

> "The defining characteristic of general intelligence is how efficiently you acquire skills and knowledge—how efficiently you extract information from the world, from your experience, and turn it into programs that generalize well." — Francois Chollet

> "Gradient descent is four to five orders of magnitude less efficient than human intelligence at skill acquisition." — Francois Chollet

## Integration Notes
- Connects to CANON-30000-INTELLIGENCE: Skill acquisition efficiency as core definition; LLMs as component not solution
- Connects to CANON-00003-PRINCIPLES: Efficiency lens directly relevant; first principles on what intelligence actually is
- Novel contribution: Skill acquisition efficiency definition; LLM efficiency gap quantified; program synthesis + deep learning merger thesis

## Metadata
- Duration: ~20 minutes (fireside chat)
- Quality: Clean transcript with verification notes
- Processing notes: Paradigm-tier content defining intelligence and critiquing LLM-only approaches
