# Extraction: SOURCE-20260204-008

**Source**: `SOURCE-20260204-x-article-kloss_xyz-how_to_build_a_prompt_for_anything_and_remix_them_at_will.md`
**Atoms extracted**: 87
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (22)

### ATOM-SOURCE-20260204-008-0001
**Lines**: 29-31
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.80

> A prompt built for someone else's use case, with someone else's context, for someone else's output, will never work as well as one you built or remix yourself.

### ATOM-SOURCE-20260204-008-0004
**Lines**: 54-56
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> XML tags are used by AnthropicAI in their system prompts, indicating that models are designed to parse structured instructions this way.

### ATOM-SOURCE-20260204-008-0006
**Lines**: 77-79
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> A more specific role definition, such as 'Senior brand strategist specializing in positioning and messaging architecture,' acts as a constraint, reducing the model's need to guess compared to a vague role like 'Marketing expert.'

### ATOM-SOURCE-20260204-008-0008
**Lines**: 91-92
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.80

> A prompt lacking a clear mission will result in generic model output.

### ATOM-SOURCE-20260204-008-0014
**Lines**: 125-126
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.80

> The model's underlying capabilities do not change; only the control over its output format is altered by specifying output format tags.

### ATOM-SOURCE-20260204-008-0016
**Lines**: 132-139
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The model's output format can be precisely controlled by the `<output_format>` tag, allowing for varied outputs like headlines, executive summaries, detailed reports, or structured JSON data, even with the same role and mission.

### ATOM-SOURCE-20260204-008-0017
**Lines**: 149-150
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.30, epistemic_stability=0.80

> A single good example within the `<examples>` tag can teach a model more effectively than a paragraph of written instructions.

### ATOM-SOURCE-20260204-008-0018
**Lines**: 152-152
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.30, epistemic_stability=0.80

> Two examples are typically sufficient for most prompts to achieve calibration, with three often being overkill.

### ATOM-SOURCE-20260204-008-0052
**Lines**: 386-387
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The specificity of the `<role>` tag, like 'linguistic forensics analyst', tells the model exactly what lens to use.

### ATOM-SOURCE-20260204-008-0053
**Lines**: 389-391
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<method>` tag forces sequenced analysis (read first, then identify, then synthesize), which prevents the model from missing patterns by trying to do all three at once.

### ATOM-SOURCE-20260204-008-0054
**Lines**: 393-394
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The `<anti_patterns>` tag prevents common failure modes, such as vague style descriptions that are not useful for replication.

### ATOM-SOURCE-20260204-008-0055
**Lines**: 396-397
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The `<output_format>` tag demands two deliverables: an analysis for verification and a style prompt for immediate use.

### ATOM-SOURCE-20260204-008-0057
**Lines**: 399-400
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The `<examples>` section calibrates the model more effectively than written instructions alone.

### ATOM-SOURCE-20260204-008-0079
**Lines**: 550-552
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> A prompt's `<role>` should be specific, including years of experience, specialization, or domain, to avoid generic or shallow output.

### ATOM-SOURCE-20260204-008-0080
**Lines**: 553-556
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> If output format is incorrect, the `<output_format>` section is likely missing or too loose, requiring precise specification of the desired format (e.g., .csv, .md).

### ATOM-SOURCE-20260204-008-0081
**Lines**: 557-559
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> Instructions in `<rules>` or `<constraints>` should be moved earlier, made shorter, and checked for contradictions if the output ignores them.

### ATOM-SOURCE-20260204-008-0082
**Lines**: 560-562
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> To prevent hedging or sugarcoating in output, an `<anti_patterns>` section with explicit examples of undesired behavior should be added.

### ATOM-SOURCE-20260204-008-0083
**Lines**: 563-566
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.90

> An ambiguous `<mission>` statement, allowing multiple interpretations, will lead to the model picking one at random, necessitating a tighter, unambiguous mission.

### ATOM-SOURCE-20260204-008-0084
**Lines**: 567-569
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> Without `<fallback>` instructions, a model's default behavior when it doesn't know something is to guess confidently, potentially leading to made-up facts.

### ATOM-SOURCE-20260204-008-0085
**Lines**: 570-572
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> Adding `<examples>` is crucial for stabilizing output and showing the model what 'good' looks like, especially when output is inconsistent across runs.

### ATOM-SOURCE-20260204-008-0086
**Lines**: 573-576
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> A `<method>` tag with explicit steps ensures a repeatable and scalable process, preventing the model from arriving at the right answer via the wrong, inconsistent path.

### ATOM-SOURCE-20260204-008-0087
**Lines**: 580-583
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> The prompt construction framework is universally applicable across various AI use cases, including coding review, voice extraction, content writing, SEO strategy, data analysis, and meal planning.

## Concept (23)

### ATOM-SOURCE-20260204-008-0005
**Lines**: 62-64
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<role>` tag defines the specific expert persona the model should adopt, including their experience and specialization, to filter subsequent instructions.

### ATOM-SOURCE-20260204-008-0007
**Lines**: 82-82
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<mission>` tag provides a directive outlining what the model should accomplish, defining its scope, inputs, outputs, and actions.

### ATOM-SOURCE-20260204-008-0009
**Lines**: 95-102
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<rules>` tag controls the model's behavior, specifying how it should act (e.g., 'Never assume context,' 'Do not soften bad news') to override default tendencies.

### ATOM-SOURCE-20260204-008-0010
**Lines**: 109-113
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<constraints>` tag sets hard limits on the output itself, such as length, content restrictions, or language requirements.

### ATOM-SOURCE-20260204-008-0011
**Lines**: 116-116
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Rules govern how models think, while constraints govern what models produce.

### ATOM-SOURCE-20260204-008-0013
**Lines**: 119-124
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<output_format>` tag specifies the exact structure and presentation of the desired output, transforming a general request into precise specifications.

### ATOM-SOURCE-20260204-008-0019
**Lines**: 158-160
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.80

> Advanced tags are prompt elements that handle precision, interactivity, or domain awareness, complementing core tags which cover 80% of prompting needs.

### ATOM-SOURCE-20260204-008-0020
**Lines**: 164-165
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<context>` tag provides background information or reference material that the model needs before acting, distinct from the mission because it's not a directive.

### ATOM-SOURCE-20260204-008-0022
**Lines**: 177-177
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.80

> `<persona>` defines the model's personality, `<tone>` defines its emotional register, and these are distinct from `role` which defines expertise.

### ATOM-SOURCE-20260204-008-0024
**Lines**: 193-193
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<audience>` tag specifies who the output is for, influencing the model's vocabulary, depth, and assumed knowledge.

### ATOM-SOURCE-20260204-008-0026
**Lines**: 205-206
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<knowledge>` tag injects domain-specific factual material as reference, differing from `<context>` which provides situational background.

### ATOM-SOURCE-20260204-008-0028
**Lines**: 217-218
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> The `<method>` or `<steps>` tag defines a sequenced process for the model to follow, ensuring tasks are performed in a specific order where dependencies exist.

### ATOM-SOURCE-20260204-008-0030
**Lines**: 231-232
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<anti_patterns>` tag specifies what constitutes bad output, providing concrete examples for the model to avoid, which is more effective than abstract rules.

### ATOM-SOURCE-20260204-008-0032
**Lines**: 248-249
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<fallback>` tag instructs the model on what to do when it cannot complete a task, preventing hallucination or unhelpful responses.

### ATOM-SOURCE-20260204-008-0034
**Lines**: 260-261
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<evaluation>` tag provides self-check criteria, acting as a quality assurance checklist for the model to review its own output before delivery.

### ATOM-SOURCE-20260204-008-0038
**Lines**: 272-273
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.60

> The `<discovery_engine>` tag enables the model to ask the user questions before acting, extracting necessary information rather than relying on the user to provide everything upfront.

### ATOM-SOURCE-20260204-008-0039
**Lines**: 274-275
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The `<discovery_engine>` tag specifies questions the model should ask the user before proceeding with any work.

### ATOM-SOURCE-20260204-008-0041
**Lines**: 292-293
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.60

> The `<chain>` tag links prompts together, where the output of one prompt becomes the input for the next.

### ATOM-SOURCE-20260204-008-0063
**Lines**: 470-472
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The `<context>` tag in a prompt is crucial because it informs the model of the specific analytical lens required (e.g., brand monitoring vs. academic analysis), even for the same keywords.

### ATOM-SOURCE-20260204-008-0064
**Lines**: 474-478
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `<method>` tag in a prompt establishes a multi-step analytical process, preventing the model from premature conclusions by requiring categorization, narrative identification, shift detection, volume assessment, and insight extraction in sequence.

### ATOM-SOURCE-20260204-008-0065
**Lines**: 480-482
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The `<rules>` tag in a prompt is vital for preventing models from overemphasizing noise as signal, such as preventing the misinterpretation of a few negative posts as widespread backlash.

### ATOM-SOURCE-20260204-008-0066
**Lines**: 484-486
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The `<evaluation>` tag in a prompt forces the model to self-check its data backing, ensuring that statistics are not hallucinated and are supported by actual data before delivery.

### ATOM-SOURCE-20260204-008-0067
**Lines**: 488-491
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The `<output_format>` tag in a prompt ensures consistent structure for intelligence briefs, facilitating comparison across different time periods and topics, with the 'GAPS' section being particularly valuable for identifying what the model could not find.

## Framework (4)

### ATOM-SOURCE-20260204-008-0003
**Lines**: 42-50
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> The XML Tag System for prompting eliminates ambiguity by using labeled containers (e.g., <role>, <mission>, <rules>) to explicitly define information types and their usage for the model, reducing potential hallucinations.

### ATOM-SOURCE-20260204-008-0048
**Lines**: 324-331
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> A 'Voice Style Extractor' prompt can deconstruct a writing sample into a reusable style profile by identifying specific, measurable patterns across dimensions like sentence structure, vocabulary, punctuation, paragraph structure, rhetorical devices, tone markers, and formatting preferences.

### ATOM-SOURCE-20260204-008-0058
**Lines**: 404-409
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> A 'Keyword & Sentiment Search Engine' prompt can turn an AI into a social intelligence analyst that monitors public conversations, extracts signal from noise, and delivers structured intelligence briefs on sentiment, patterns, and actionable insights.

### ATOM-SOURCE-20260204-008-0077
**Lines**: 540-548
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.90

> A prompt construction framework includes tags for `<role>`, `<discovery_engine>`, `<anti_patterns>`, `<fallback>`, and `<output_format>`, each serving a specific purpose in guiding model behavior.

## Praxis Hook (38)

### ATOM-SOURCE-20260204-008-0002
**Lines**: 35-35
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To improve prompting, focus on learning how to build and remix prompts rather than just finding more prompts to copy.

### ATOM-SOURCE-20260204-008-0012
**Lines**: 118-123
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> To control output format, specify it using the `<output_format>` tag, for example: `<output_format>A 3-paragraph executive summary.</output_format>` for a brief, `<output_format>A detailed report with sections and subheadings.</output_format>` for a document, or `<output_format>JSON with keys: summary, confidence, next_steps.</output_format>` for structured data.

### ATOM-SOURCE-20260204-008-0015
**Lines**: 130-132
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Use the `<examples>` tag to provide concrete instances of desired input/output, as it effectively communicates format, depth, tone, structure, and reasoning to the model.

### ATOM-SOURCE-20260204-008-0021
**Lines**: 173-174
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Use the `<context>` tag when the model requires information about the user, project, industry, or situation to calibrate its response, rather than providing generic advice.

### ATOM-SOURCE-20260204-008-0023
**Lines**: 189-190
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Employ `<persona>` and `<tone>` tags when the model needs to communicate in a specific manner not captured by its assigned role alone, such as in writing, coaching, or brand voice prompts.

### ATOM-SOURCE-20260204-008-0025
**Lines**: 201-202
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.90

> Use the `<audience>` tag when the model's output will be read by someone other than the prompt creator, or when the model needs to adjust the complexity of its output.

### ATOM-SOURCE-20260204-008-0027
**Lines**: 213-214
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Utilize the `<knowledge>` tag when the model requires specific facts, data, or institutional knowledge, such as product information, company policies, or pricing structures, to perform its task.

### ATOM-SOURCE-20260204-008-0029
**Lines**: 227-228
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Apply the `<method>` tag for complex workflows, such as analysis, debugging, or research prompts, where the model needs to execute a process rather than just generate an output.

### ATOM-SOURCE-20260204-008-0031
**Lines**: 244-245
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Use `<anti_patterns>` when the model consistently produces specific types of undesirable output that general rules have failed to correct.

### ATOM-SOURCE-20260204-008-0033
**Lines**: 256-257
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Implement the `<fallback>` tag in prompts where incorrect answers are more detrimental than no answers, such as in financial analysis, medical information, or legal review.

### ATOM-SOURCE-20260204-008-0035
**Lines**: 260-262
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When evaluating a model's output, use a quality assurance (QA) checklist to force a second pass before the output is finalized.

### ATOM-SOURCE-20260204-008-0036
**Lines**: 266-268
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Use the `<evaluation>` tag in prompts when quality consistency is critical, such as for client-facing work, content production, analysis, recommendations, or applications.

### ATOM-SOURCE-20260204-008-0037
**Lines**: 270-271
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Use the `<evaluation>` tag when consistent quality is paramount, such as for client-facing work, content production, analysis, recommendations, or applications.

### ATOM-SOURCE-20260204-008-0040
**Lines**: 287-289
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Use the `<discovery_engine>` tag in prompts where the user's initial input is likely incomplete, such as consulting, strategy, creative briefs, or project scoping.

### ATOM-SOURCE-20260204-008-0042
**Lines**: 300-302
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Use the `<chain>` tag for multi-step workflows where each prompt handles one phase, such as research → analysis → recommendation, or draft → critique → revision.

### ATOM-SOURCE-20260204-008-0043
**Lines**: 307-307
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For simple tasks (summarize, rewrite, answer a question), use `<role>`, `<mission>`, and `<output_format>` tags.

### ATOM-SOURCE-20260204-008-0044
**Lines**: 309-310
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For professional output (client deliverables, published content, formal analysis), use `<role>`, `<mission>`, `<rules>`, `<constraints>`, `<output_format>`, and `<examples>` tags.

### ATOM-SOURCE-20260204-008-0045
**Lines**: 312-313
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For interactive/conversational prompts (coaching, consulting, brainstorming), use `<role>`, `<mission>`, `<rules>`, `<discovery_engine>`, and `<fallback>` tags.

### ATOM-SOURCE-20260204-008-0046
**Lines**: 315-316
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For complex workflows (multi-step analysis, research, production pipeline), use all core tags plus `<method>`, `<evaluation>`, `<chain>`, and `<anti_patterns>`.

### ATOM-SOURCE-20260204-008-0047
**Lines**: 318-320
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Start with core tags and add advanced tags only when a specific problem needs solving; a prompt with fewer, effective tags is better than one with many ineffective ones.

### ATOM-SOURCE-20260204-008-0049
**Lines**: 348-351
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When analyzing writing style, avoid vague adjectives like 'conversational' or 'professional'; instead, identify actual structural and tonal mechanics, such as 'Uses sentence fragments for emphasis, averages 8 words per fragment, deploys them after longer complex sentences to create rhythmic contrast'.

### ATOM-SOURCE-20260204-008-0050
**Lines**: 351-353
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Every observation about writing style must be supported by at least two examples from the sample; if the sample is too short, flag it as 'insufficient data' rather than guessing.

### ATOM-SOURCE-20260204-008-0051
**Lines**: 364-368
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When creating a style prompt, ensure the output includes both a detailed analysis of patterns with quoted examples and a copy-paste-ready system prompt that precisely captures the voice using XML tags.

### ATOM-SOURCE-20260204-008-0056
**Lines**: 397-400
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To act as a social intelligence analyst, monitor public conversations across platforms to extract signal from noise, identifying what people think, what's shifting, what's emerging, and what's being ignored.

### ATOM-SOURCE-20260204-008-0059
**Lines**: 415-422
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When analyzing public discourse, categorize findings by sentiment (positive, negative, neutral, mixed), identify dominant and outlier narratives, flag emerging shifts, assess volume and velocity, and extract actionable insights.

### ATOM-SOURCE-20260204-008-0060
**Lines**: 425-429
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> In social intelligence analysis, distinguish between loud minority opinions and actual consensus, ensuring sentiment is presented with volume context (e.g., 'across X posts over Y timeframe') and avoiding extrapolation from insufficient data.

### ATOM-SOURCE-20260204-008-0061
**Lines**: 434-438
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When conducting social intelligence analysis, base all analysis on publicly available information, avoid speculating on private motivations, do not present AI-generated summaries as direct quotes, and flag the difference between verified accounts and general public discourse.

### ATOM-SOURCE-20260204-008-0062
**Lines**: 460-465
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Before delivering a social intelligence brief, verify that every percentage is tied to actual volume data, narratives are supported by multiple data points, insights are genuinely actionable, and any unknown information is explicitly flagged.

### ATOM-SOURCE-20260204-008-0068
**Lines**: 500-503
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To act as a ruthless requirements interrogator, focus solely on asking questions to eliminate assumptions about an app, product, or project idea, without building, coding, suggesting solutions, or generating documentation.

### ATOM-SOURCE-20260204-008-0069
**Lines**: 509-520
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When interrogating a user about a project idea, ask all necessary questions upfront, covering core problems, user types, screens, data, authentication, third-party services, edge cases, performance, platform targets, design, budget, timeline, and success metrics.

### ATOM-SOURCE-20260204-008-0070
**Lines**: 524-528
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> In requirements interrogation, never assume, infer, or fill gaps; push back on vague answers, and continue questioning until zero assumptions remain, prioritizing thoroughness over speed.

### ATOM-SOURCE-20260204-008-0071
**Lines**: 531-533
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Avoid accepting 'I'll figure that out later' as an answer during requirements interrogation, as it represents an assumption that needs to be defined.

### ATOM-SOURCE-20260204-008-0072
**Lines**: 532-534
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> When concluding a summary, include the statement: "Review this summary. If anything is wrong, missing, or needs to change, tell me now. This becomes the foundation for everything built after it."

### ATOM-SOURCE-20260204-008-0073
**Lines**: 532-534
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Maintain an "OPEN QUESTIONS" section to track unresolved issues, noting their importance and decision deadlines.

### ATOM-SOURCE-20260204-008-0074
**Lines**: 535-537
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Avoid suggesting solutions during requirements interrogation, as this can cause the user to anchor to the suggestion rather than fully developing their own requirements.

### ATOM-SOURCE-20260204-008-0075
**Lines**: 536-538
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> To ensure clarity and future validation, explicitly list any unavoidable assumptions in an "ASSUMPTIONS LOG" section.

### ATOM-SOURCE-20260204-008-0076
**Lines**: 539-542
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Avoid asking one question at a time during requirements interrogation; instead, extract all information efficiently to help the user visualize the full scope of their idea.

### ATOM-SOURCE-20260204-008-0078
**Lines**: 545-548
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> If a user responds with 'I don't know' to a question during interrogation, explain its importance, offer 2-3 common approaches, and ask them to choose one or explicitly table it as an open question to avoid unresolved ambiguity.
