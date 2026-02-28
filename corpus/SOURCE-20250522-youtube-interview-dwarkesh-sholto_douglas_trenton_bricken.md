# Sholto Douglas & Trenton Bricken: Is RL + LLMs Enough for AGI?

## MACROSCOPIC NARRATIVE LENS ALIGNMENT

### Primary Lenses Illuminated

| Lens | How Source Advances Understanding |
|------|-----------------------------------|
| **Fourth Industrial Revolution / AI Era** | Insider view on actual capability frontier vs hype. RL works for verifiable domains. |
| **The Reflexive Epoch** | "Neuralese"—models developing self-referential internal representations we may not capture |
| **Compute Overhang / The Stack** | Inference compute as bottleneck. Training compute abundant; inference harder to scale. |
| **Pre-Paradigmatic Moment** | We can see THAT models compute but not WHY—fundamental interpretability gap |
| **Great Acceleration** | Software engineering agents: from months to days of work in one year |

### Cross-Lens Synthesis

Technical insider perspective grounds abstract narratives:

1. **Reflexive Epoch + Neuralese**: Models may be self-aware in ways we can't yet detect
2. **Compute Overhang + Inference Bottleneck**: Abundance in training, scarcity in deployment
3. **Pre-Paradigmatic + Interpretability Gap**: We lack frameworks to understand what's actually happening inside

---

## KEY FRAMEWORKS EXTRACTED

### 1. Two Axes of AI Capability

> "Think of these two axes: one is the intellectual complexity of the task, and the other is the time horizon at which the task is being completed."

Current state (2025):
- **Intellectual complexity**: Peaks achieved (competitive programming, math)
- **Time horizon**: Not yet demonstrated for long-running agentic tasks

**Integration target**: CANON-30400 (Agentic Architecture)

### 2. Clean Reward Signal Thesis

> "If you can give it a good feedback loop for the thing that you want it to do, then it's pretty good at it. If you can't, they struggle."

This explains:
- Why code/math work (verifiable answers)
- Why open-ended tasks struggle (no clean signal)
- The path forward: expanding domains with good signals

**Integration target**: CANON-30400 (Agentic Architecture), CANON-00004 (Evolution)

### 3. Neuralese

> "Models might develop their own internal language that's optimized for how they compute, not for how humans read."

Implication: Human-language interpretability may fundamentally miss model cognition. Like transcribing whale clicks into English words—getting something but losing information.

**Integration target**: CANON-30400 (Agentic Architecture), interpretation challenges

### 4. The THAT/WHY Gap

> "We can identify THAT the model is computing something but not always WHY it chose to compute it that way."

Current interpretability frontier:
- Can identify features (patterns corresponding to concepts)
- Can trace information flow
- Cannot explain why model chose particular computation over alternatives

**Integration target**: CANON-30400, interpretability section

### 5. Inference Compute Bottleneck

> "Inference compute is much harder to scale than training compute."

Training: Throw more compute, get better models
Inference: Real-time, can't batch same way, requires different infrastructure

This may bottleneck AGI deployment more than capability development.

**Integration target**: CANON-30300 (Technology Stack)

### 6. Why LLMs are "Baby AGI" (AlphaZero Isn't)

> "LLMs can do something AlphaZero fundamentally can't: they can reason about things outside their training distribution. AlphaZero is a master within its domain but utterly helpless outside it."

The generality property—"muddle through on novel tasks"—is what makes LLMs proto-AGI, not absolute capability level.

**Integration target**: CANON-00004 (Evolution), intelligence definitions

### 7. Self-Awareness Question

> "As we push the models further with RL, they do seem to develop something that looks like self-awareness—or at least introspection. They'll sometimes catch their own mistakes mid-reasoning."

But: might be learned pattern (reward favors self-correction language) rather than genuine reflection. Can't tell without better interpretability.

---

## CANON INTEGRATION SPECIFICATIONS

### CANON-30400-AGENTIC_ARCHITECTURE

**Section**: Capability Assessment (2025)
**Addition**: Two-axes framework and clean reward thesis

> SOURCE-20250522-053: Douglas and Bricken identify two capability axes: intellectual complexity (peaks achieved in math/code) and time horizon (long-running agentic performance not yet demonstrated). The bottleneck is clean reward signals: "If you can give it a good feedback loop, it's pretty good. If you can't, they struggle." This explains domain-specific capability advances and suggests path forward through expanding verifiable domains.

**Section**: Interpretability Challenges
**Addition**: Neuralese and THAT/WHY gap

> SOURCE-20250522-053: "Neuralese"—models may think in internal language optimized for computation, not human interpretation. Current interpretability can identify THAT something is being computed but not WHY that computation was chosen. This fundamental gap limits our ability to verify alignment or understand model reasoning.

### CANON-00004-EVOLUTION-cosmos.md

**Section**: AI as Evolutionary Process
**Addition**: LLM generality as proto-AGI signature

> SOURCE-20250522-053: LLMs are "baby AGI" not because of capability level but generality: "they can reason about things outside their training distribution. AlphaZero is a master within its domain but utterly helpless outside it." This generality—"muddle through on novel tasks"—is the signature of proto-general intelligence.

### CANON-30300-TECHNOLOGY_STACK

**Section**: Compute Economics
**Addition**: Inference bottleneck

> SOURCE-20250522-053: "Inference compute will bottleneck AGI—harder to scale than training compute." Training can be parallelized and batched; inference is real-time and decentralized. As models improve, deployment may constrain capability more than development.

---

## QUOTABLE INSIGHTS FOR INTEGRATION

### On RL Working
> "The biggest thing that's changed is that RL in language models has finally worked. We finally have proof of an algorithm that can give us expert human reliability and performance, given the right feedback loop."

### On Clean Rewards
> "The thing that's limiting us is that we don't have a good reward signal for most tasks that we care about. If you think about what we've solved: we've solved competitive programming, we've solved math, we've solved basically any task where you can verify the answer."

### On Neuralese
> "Think of it like if you were trying to understand how a whale thinks by transcribing its clicks into English words. You'd get something, but you'd be missing a lot of the information that's in the original click patterns."

### On Self-Awareness Uncertainty
> "I'm honestly not sure whether that's genuine self-awareness or just a learned pattern. It might be that the reward signal is favoring models that use certain linguistic patterns that look like self-correction, even if there's no real underlying reflection happening."

### On LLM vs AlphaZero
> "If AlphaZero could learn chess, then learn Go, then learn trading, then learn protein folding, we'd call it AGI. But it's locked into each domain by its training process. LLMs have this strange flexibility."

### On Prediction
> "By the end of this year to this time next year, we will have software engineering agents that can do close to a day's worth of work for a junior engineer, or a couple of hours of quite competent, independent work."

---

## TECHNICAL DETAILS

### DeepSeek Assessment
> "DeepSeek could be using better data, better architectures, better training techniques, or some combination. It's not always clear which lever they're pulling."

Doesn't break scaling laws but shows "more efficiency on the table than people realized."

### Taste/Slop Problem
> "Taste is fundamentally subjective. For tasks where taste matters—creative writing, design, music—how do you even define what a good output looks like?"

RL can't solve taste in traditional sense; returns to human feedback which doesn't scale.

### Continual Learning Assessment
> "I think continual learning will be a bottleneck eventually, but I don't think we're there yet. The thing that's limiting us is that we don't have a good reward signal for most tasks."

---

## PROCESSING NOTES

- Source quality: Very high. Insider perspective from Anthropic frontier research.
- Unique value: Technical grounding of capability claims; identifies specific bottlenecks
- Key insight: Clean reward signal is current limitation, not architecture
- Neuralese concept important for interpretability limitations
- Inference bottleneck underappreciated constraint
- Generality (not capability) as proto-AGI signature
- Processed 2026-01-02 under DIRECTIVE-035C
