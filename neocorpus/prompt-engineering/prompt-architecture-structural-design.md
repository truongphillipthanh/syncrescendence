# Prompt Architecture & Structural Design

> A prompt is not a request — it is a behavioral specification, and every ambiguity you leave in it is a decision you hand back to the model.

## Source Provenance

| File | Contribution |
|------|-------------|
| `00118.md` | Full XML tag taxonomy (core + advanced), three worked prompt examples with architectural breakdowns, debugging diagnostic map |
| `03490.jsonl` | Atomized claims and praxis hooks extracted from 00118.md — reinforces and extends the tag system with distilled assertions |
| `03184.jsonl` | The 5-layer anatomy (Identity, Context, Task, Process, Output), completeness contract, the role-library / constraints-doc / output-format-library operational toolkit, the prompting-as-leverage thesis |
| `10325.md` | Context engineering as successor discipline to prompt engineering, the four context strategies (Write/Select/Compress/Isolate), the system prompt formula, model-specific format preferences, RAG grounding |
| `04449.md` | Negative evidence: a prompt-library website (copy-paste catalog) representing exactly the anti-pattern that structural design supersedes |
| `09308.md` | Out-of-scope source (robotics/physical intelligence interview) — contributed zero prompt-architecture content; noted for provenance integrity |

---

## The Epistemological Shift

The foundational reframe is this: a language model is a pattern-completion engine. It generates the statistically most probable continuation of its input. Vague input makes generic output probable. Generic is the model's default — the gravitational center everything falls toward when structure is absent.

The copy-paste prompt-library model (exemplified by 04449.md's "The #1 Best AI Prompt Library") is not a skill; it is a dependency. Wearing someone else's prescription glasses. A prompt built for someone else's use case, context, and output will underperform a prompt you built yourself — not because of mystical fit, but because context specificity is what shifts the model's probability distribution toward your actual target.

The people who achieve exceptional AI results are not using secret incantations. They are willing to be *uncomfortably specific*. Vagueness is not flexibility — it is a form of quitting, handing the model a half-baked idea and hoping probability lands in your favor.

---

## The XML Tag Taxonomy

XML tags eliminate guessing by creating labeled containers — each tag is a boundary, and each boundary is a decision you made so the model does not have to. Anthropic uses XML tags in their own system prompts; the architecture exploits how the model was trained to parse structured instructions.

### Core Tags (Required for Most Prompts)

**`<role>`** — The lens through which all other instructions are filtered. Not a personality, a specific expert: domain, years of experience, specialization. "Marketing expert" is a guess. "Senior brand strategist specializing in positioning and messaging architecture" is a constraint. The more specific the role, the less the model interpolates.

**`<mission>`** — A directive, not a description. Defines scope: what goes in, what comes out, what the model does, and critically what it does not do. An ambiguous mission is a prompt that will do whatever it wants — which defaults to generic.

**`<rules>`** — Behavioral controls. Override the model's default rails: bullet points when you wanted prose, assumptions made when you wanted interrogation, softened bad news when you wanted directness. Rules are the "never do this / always do this" layer. They shape how the model thinks.

**`<constraints>`** — Hard limits on the output itself. Length, language, content exclusions. Distinction matters: rules govern behavior, constraints govern output. The model processes them differently.

**`<output_format>`** — The most overlooked tag. Without it, you get whatever the model feels like giving. Same role, same mission, but `<output_format>One sentence.</output_format>` gives a headline while `<output_format>JSON with keys: summary, confidence, next_steps.</output_format>` gives structured data. The model's underlying capabilities do not change — only the control over output format does.

**`<examples>`** — The single most powerful and most underused tag. One good example teaches the model more than a paragraph of instructions: format, depth, tone, structure, and reasoning all at once. Two examples is typically sufficient for calibration. Three is overkill for most prompts. (Exception: systems with persistent contextual memory benefit from more.)

### Advanced Tags (The Other 20%)

**`<context>`** — Background the model needs before acting; reference material, not a directive. Without it, the model gives generic advice for a generic person.

**`<persona>` / `<tone>`** — Role defines expertise; persona defines personality; tone defines emotional register. A senior financial analyst can be warm or clinical. The role does not determine the voice.

**`<audience>`** — Shifts vocabulary, depth, and assumed knowledge. The same API explanation looks different for a developer versus a non-technical CEO.

**`<knowledge>`** — Domain-specific factual material injected as reference. Distinct from `<context>` (situational background) — this is institutional knowledge: pricing structures, product specs, competitive data.

**`<method>` / `<steps>`** — A sequenced process the model follows, not just a list of things to do. Critical when step 3 depends on step 2. Forces read-first-then-analyze rather than the model attempting all three simultaneously and missing patterns.

**`<anti_patterns>`** — Concrete examples of bad output, not just abstract prohibitions. "Don't be vague" is a rule. Showing exactly what vague looks like is an anti-pattern. Models pattern-match against concrete examples far more reliably than against abstract instructions.

**`<fallback>`** — Instructions for when the model cannot complete the task. Without a fallback, the model's default behavior is to guess confidently. This is where hallucination lives.

**`<evaluation>`** — Self-check criteria before delivery. A QA checklist built into the prompt itself: "Is every claim specific and actionable? Would a busy person find this useful in under 60 seconds?" Forces a second pass.

**`<discovery_engine>`** — Questions the model asks before acting. Flips the dynamic from "user provides everything and hopes" to "model extracts what it needs." Essential for consulting, scoping, and creative brief prompts where initial input is reliably incomplete. Instruct the model to ask everything upfront, not drip-feed questions — one extraction pass, not a therapy session.

**`<chain>`** — Links prompts in a pipeline. Step 2 knows it receives the output of Step 1 and produces input for Step 3. Enforces clean handoffs and prevents scope creep between phases.

---

## The 5-Layer Anatomy

Independent of which specific XML tags you use, effective prompts converge on five layers that map to how models process and prioritize information:

1. **Identity** — Specific, fine-tuned role with domain, skill expertise, and perspective. Not "helpful assistant." "Senior product marketer specializing in B2B SaaS positioning" accesses different clusters of training data, stylistic patterns, and reasoning approaches.

2. **Context** — Background information, prior decisions, and constraints that would be obvious to a human collaborator but invisible to the model. Must be ordered, scoped, and labeled — the model pattern-matches relevance, it does not remember emotionally. Unstructured context dumps treat all information as equally optional.

3. **Task** — The specific action required, precisely defined. Not "write landing page copy" but "produce a 500-word product description emphasizing time-saving benefits for busy executives." Precision collapses the model's solution space to what you actually want.

4. **Process** — How to approach the task: thinking order, decision checkpoints, internal validation steps. Not just "what to produce" but "how to produce it." Describing the process converts correct output from a one-time result into a repeatable one.

5. **Output** — What a completed task looks like, including format specification. "Output your response as a JSON with inputs for headline, subheadline, and body text. Do not return any messaging, chat, notes, etc. Only the JSON." Removes interpretive latitude from the delivery layer.

---

## The Completeness Contract

A prompt is a contract. Four non-negotiable elements must be present: Role (who the model is), Task (what it must accomplish), Constraints (directions to constrain behavior and output), and Output format (what "done" looks like). If any element is missing, the model fills the gap with assumptions — which are guesses, which generate hallucinations or drift.

The completeness contract has an asymmetric consequence structure: a vague prompt can produce acceptable output by chance, which trains the prompter to keep prompting vaguely. A structurally complete prompt produces acceptable output by design, which compounds.

---

## The Operational Toolkit

The completeness contract implies a persistent infrastructure problem: you cannot rebuild the contract from scratch for every interaction. The solution is a system of reusable documents:

**Role Library** — 5–10 specific role definitions stored externally and pulled by reference. Each role is operationally complete: domain, experience, specialization, and any quirks that affect behavior. Paste into every relevant prompt.

**Context Templates** — Structured templates for categories of information you provide repeatedly (app details, content requirements, project context). Templates ensure critical context is never accidentally omitted.

**Constraints Doc** — Universal rules that must never change across all AI work. "Never use corporate jargon. Never assume the user is technical. Never contradict information in our canonical documents." Referenced in every significant prompt, not reconstructed from memory.

**Output Format Library** — Frequently requested output formats: JSON schemas, Markdown patterns, specific paragraph structures. Paste the relevant spec rather than describing it imprecisely each time.

The purpose of these documents is consistency derived from explicit instruction, not from the model's memory. AI models typically start each conversation from zero unless relevant constraints are explicitly loaded. Consistency comes from the prompter's system, not the model's recall.

---

## Context Engineering: The Successor Discipline

Prompt engineering is the 2024–2025 skill. Context engineering is the 2025–2026 skill. The shift is from "how do I write better sentences?" to "what information environment do I create around my AI interactions?"

Shopify CEO Tobi Lutke defined it: "the art of providing all the context for the task to be plausibly solvable by the LLM." The individual prompt matters less than the total information architecture.

Four strategies:

- **Write** — Save context outside the active window using scratchpads and reference files the AI can access across sessions.
- **Select** — Choose what enters context through RAG and dynamic retrieval rather than dumping everything in. One focused project per task beats one massive project with hundreds of files competing for attention.
- **Compress** — Summarize verbose information before including it. Context window is a finite resource.
- **Isolate** — Use separate conversation threads or sub-agents for contexts that should not bleed into each other.

RAG (Retrieval Augmented Generation) is the structural solution to hallucination in domain-specific queries: before answering, search your actual documents and include the relevant material in context. The model responds from your evidence base, not its training distribution. Canonical documentation — PRDs, design systems, app flows — functions as the persistent reality the model is anchored to. If canonical rulesets are not explicitly referenced and protected, models assume everything, including core decisions, is mutable.

---

## Prompt Combination Profiles

Tag selection should match the complexity tier of the task:

| Tier | Tags |
|------|------|
| Simple task (summarize, rewrite, answer) | `<role>` + `<mission>` + `<output_format>` |
| Professional output (client deliverable, formal analysis) | Core tags + `<rules>` + `<constraints>` + `<examples>` |
| Interactive/conversational (coaching, consulting) | `<role>` + `<mission>` + `<rules>` + `<discovery_engine>` + `<fallback>` |
| Complex workflow (multi-step analysis, production pipeline) | All core tags + `<method>` + `<evaluation>` + `<chain>` + `<anti_patterns>` |

Six tags all doing genuine work is better than twelve tags where half are padding.

---

## Debugging Diagnostics

When a prompt fails, the failure maps to a specific structural gap:

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Generic or shallow output | `<role>` is too vague | Add domain, years, specialization |
| Wrong output format | `<output_format>` missing or loose | Specify exact format |
| Instructions ignored | `<rules>` / `<constraints>` buried or contradictory | Move earlier, shorten, check for conflicts |
| Sugarcoating / hedging | No concrete negative examples | Add `<anti_patterns>` with specific instances |
| Output misses the point | `<mission>` allows multiple interpretations | Tighten until only one reading is possible |
| Fabricated facts | No `<fallback>` | Instruct "I need more information" path explicitly |
| Inconsistent across runs | No `<examples>` | Add one concrete example |
| Right answer, wrong process | No `<method>` | Add explicit sequenced steps |

---

## Antipatterns

**Copy-paste prompting** — Borrowing someone else's prompt is wearing their prescription glasses. The prompt was built for their context, their output, their model. It will underperform a prompt you built for yours. A bookmark library is not a system.

**Vagueness as flexibility** — "Make it awesome" is not a constraint. It is an abdication. The model's probability distribution defaults to generic when specific vocabulary is absent. Vagueness does not preserve optionality; it degrades output.

**Prompt portability myth** — Writing one prompt and expecting identical behavior across models is a category error. Models differ in preferences for structured language, verbosity tolerance, constraint adherence, and hallucination tendencies. Claude responds exceptionally well to XML tags (it was trained this way). GPT and Gemini work well with JSON for structured data. Plain text works for simple requests. Model-specific adaptation is the essential skill.

**Instructions without examples** — Rules describe what bad output looks like in the abstract. Anti-patterns show it concretely. Fallback instructions tell the model what to do when it cannot complete the task; without them, confident hallucination is the default. Instructions alone are consistently weaker than instructions plus one example.

**Context dumping without structure** — Unordered, unlabeled context is treated as equally optional. The model pattern-matches relevance; it does not emotionally weight information the way a human collaborator would. If context matters, structure it explicitly.

**Treating consistency as a model property** — Consistency is not something the model learns; it is something the prompter engineers. Models begin each conversation from zero. Every constraint not loaded explicitly into the prompt is a constraint the model will not respect.

---

## The Lesson

A prompt is an act of design: every tag is a boundary, every boundary is a decision you made so the model does not have to guess, and every guess the model makes is a potential hallucination or regression to generic. The shift from "asking nicely" to engineering behavior is not stylistic — it is structural, and the structure compounds: a Role Library, Constraints Doc, and Output Format Library make every subsequent prompt start from an already-specified reality instead of zero. Context engineering extends this further: the real leverage is not the individual prompt but the information architecture that persists across all interactions.
