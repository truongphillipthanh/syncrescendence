---
id: CANON-30410
canonical_name: Cognitive Architecture
title: "Cognitive Architecture"

tier: lattice
chain: intelligence
layer: lattice
developmental_status: active
celestial_type: asteroid
volatility_band: dynamic
refresh_cadence: monthly

parent: CANON-30400
requires:
  - CANON-30400
siblings: []
synthesizes: []

status: canonical
operational_status: theoretical
version: 2.0.0
created: 2025-12-30
updated: 2025-12-30
last_verified: 2026-02-05

element: quintessence
ooda_phase: null
volatile_sections: []
entities_defined:
  - "CoALA Architecture (STR)"
  - "ReAct Pattern (PROTO)"
  - "Reflexion Architecture (PROTO)"
  - "Hierarchical Task Network (PROTO)"
  - "Tree-of-Thoughts (PROTO)"
  - "Extended Chain-of-Thought (PROTO)"
  - "Perception Primitives (CAP)"
  - "Planning Primitives (CAP)"
  - "Primitive Composition Patterns (STR)"
---
# CANON-30410: COGNITIVE ARCHITECTURE
## Intelligence Chain Asteroid

**Parent**: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)

---

## PURPOSE

This asteroid provides detailed specifications for cognitive architectures powering autonomous agents. Where [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] surveys the landscape, this document provides implementation depth for the CoALA framework, reasoning patterns, and cognitive primitives.

---

## PART I: CoALA FRAMEWORK

### 1.1 Core Architecture

Cognitive Architectures for Language Agents (CoALA) organizes agent cognition into modular components with defined interfaces:

```yaml
CoALA_Architecture:
  Perception_Module:
    function: Transform raw environmental data into structured representations
    inputs: Text, images, APIs, user interactions, sensor data
    outputs: Structured semantic representations
    components:
      - Text encoder (NLU pipeline)
      - Visual encoder (CNN/ViT)
      - Multimodal fusion layer
      - Entity and intent extractors

  Memory_Module:
    function: Store, retain, retrieve information across timescales
    types:
      working: Immediate context, rapid access, limited capacity
      episodic: Specific interaction sequences, experience replay
      semantic: Factual knowledge, concepts, relationships
      procedural: Learned skills, action sequences
      prospective: Future intentions, scheduled actions
    interfaces:
      - write(content, type, metadata)
      - read(query, type, top_k)
      - update(id, delta)
      - forget(criteria)

  Planning_Module:
    function: Decompose goals into actionable steps
    capabilities:
      - Goal hierarchy construction
      - Subgoal lattice generation
      - Action sequence formulation
      - Contingency branch creation
      - Resource and constraint reasoning
    interfaces:
      - plan(goal, context, constraints)
      - replan(feedback, partial_execution)
      - evaluate(plan, criteria)

  Action_Module:
    function: Execute interactions with environment
    capabilities:
      - Tool invocation (API calls, code execution)
      - Response generation
      - State modification
      - Sub-agent spawning
    interfaces:
      - execute(action, parameters)
      - validate(result, expectation)
      - rollback(action_id)

  Learning_Module:
    function: Improve strategies through experience
    capabilities:
      - Performance evaluation
      - Error analysis
      - Strategy refinement
      - Knowledge extraction
    interfaces:
      - evaluate(trajectory, outcome)
      - reflect(experience, criteria)
      - update(policy, feedback)
```

### 1.2 Module Coordination

```
┌─────────────────────────────────────────────────────────────┐
│                     PERCEPTION                               │
│  Environmental data → Structured representations            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                       MEMORY                                 │
│  Store/retrieve context, facts, skills, intentions          │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      PLANNING                                │
│  Goals → Subgoals → Action sequences                        │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                       ACTION                                 │
│  Execute tools, generate responses, modify state            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      LEARNING                                │
│  Evaluate outcomes → Refine strategies → Update knowledge   │
└─────────────────────────────────────────────────────────────┘
```

---

## PART II: REASONING PATTERNS

### 2.1 ReAct (Reason + Act)

The foundational pattern synergizing reasoning and acting:

```yaml
ReAct_Pattern:
  loop:
    1_Thought: Generate reasoning trace about current state
    2_Action: Determine and execute appropriate action
    3_Observation: Receive and process action result
    4_Repeat: Until goal achieved or failure detected

  example:
    thought: "I need to find the population of Tokyo. I should search for this."
    action: search("Tokyo population")
    observation: "Tokyo has a population of approximately 13.96 million"
    thought: "I now have the answer."
    action: finish("13.96 million")

  performance:
    ALFWorld: +34% absolute success vs baselines
    WebShop: +10% absolute success vs baselines

  limitations:
    - Linear trial-and-error can be inefficient
    - Prone to loops without escape mechanisms
    - Requires well-formatted observations
```

### 2.2 Reflexion

Self-correction loop enabling verbal reinforcement learning:

```yaml
Reflexion_Architecture:
  components:
    Actor: Performs actions using ReAct-style loop
    Evaluator: Scores outcomes against goals
    Self_Reflection: Generates linguistic improvement proposals

  loop:
    1_Attempt: Actor executes task
    2_Evaluate: Evaluator scores outcome
    3_Reflect: Self-reflection analyzes failures
    4_Store: Reflection stored in episodic memory
    5_Retry: Actor retries with reflection as context

  key_innovation:
    - No model fine-tuning required
    - Learning through natural language reflection
    - Episodic memory enables cross-attempt improvement

  example_reflection:
    "In my previous attempt, I searched for the wrong keyword.
     The query 'Tokyo demographics' would be more specific than
     'Tokyo info'. I should use more precise search terms."
```

### 2.3 Hierarchical Task Network (HTN)

Classical AI planning integrated with LLM flexibility:

```yaml
HTN_Pattern:
  structure:
    - High-level abstract task at root
    - Decomposition into sub-tasks
    - Primitive executable actions at leaves

  hybrid_approach:
    symbolic_planner: Handles structured decomposition
    llm_component: Generates decompositions when rules missing

  example:
    goal: "Write research report on AI agents"
    decomposition:
      1: "Gather sources"
         1.1: "Search academic databases"
         1.2: "Search industry reports"
      2: "Analyze sources"
         2.1: "Extract key findings"
         2.2: "Identify themes"
      3: "Draft report"
         3.1: "Write introduction"
         3.2: "Write body sections"
         3.3: "Write conclusion"
      4: "Review and refine"

  optimal_architecture:
    - HTN planner generates high-level task tree
    - Reflexion-style agents execute leaf tasks
    - Local self-correction at each primitive
```

### 2.4 Tree-of-Thoughts

Parallel exploration with evaluation:

```yaml
Tree_of_Thoughts:
  structure:
    - Maintain tree of coherent intermediate reasoning states
    - Each node represents a "thought" or partial solution
    - Branches represent alternative reasoning paths

  search_strategies:
    BFS: Parallel exploration of multiple branches
    DFS: Deep investigation of promising paths

  self_evaluation:
    - Each thought assessed as: sure | maybe | impossible
    - Enables backtracking from dead ends
    - Pruning of unpromising branches

  performance:
    NATURAL_PLAN: +8% improvement
    OlympiadBench: +4% improvement
    DocFinQA: +7% improvement

  implementation:
    - Best-of-N sampling for initial thoughts
    - Constraint-guided verification
    - REBASE algorithms for refinement
```

### 2.5 Extended Chain-of-Thought

Multi-stage internal reasoning for complex problems:

```yaml
Extended_CoT:
  mechanism:
    - Cold start supervised fine-tuning
    - Group Relative Policy Optimization (GRPO)
    - Multi-stage internal deliberation

  characteristics:
    - Extended reasoning invisible to users
    - Trades latency for accuracy
    - Particularly effective on mathematics

  performance:
    AIME_mathematics: ~83% accuracy
    Complex_reasoning: Dramatic improvement

  models:
    - DeepSeek-R1
    - GPT-o1 series

  tradeoff:
    increased_latency: Yes
    increased_compute: Yes
    improved_accuracy: Significantly on complex tasks
```

---

## PART III: PERCEPTION PRIMITIVES

### 3.1 Text Perception

```yaml
Text_Perception:
  intent_extraction:
    - Classify user intent category
    - Extract action verbs and targets
    - Identify implicit requirements

  entity_recognition:
    - Named entities (people, places, organizations)
    - Temporal expressions
    - Quantities and measurements
    - Domain-specific entities

  sentiment_analysis:
    - Polarity (positive/negative/neutral)
    - Emotion detection
    - Urgency assessment

  relationship_extraction:
    - Subject-predicate-object triples
    - Causal relationships
    - Temporal sequences
```

### 3.2 Visual Perception

```yaml
Visual_Perception:
  object_detection:
    - Identify and localize objects
    - Bounding box generation
    - Confidence scoring

  scene_understanding:
    - Scene classification
    - Spatial relationship extraction
    - Activity recognition

  OCR:
    - Text extraction from images
    - Document structure recognition
    - Handwriting recognition

  multimodal_fusion:
    - Image-text alignment
    - Visual question answering
    - Diagram interpretation
```

### 3.3 Multimodal Integration

```yaml
Multimodal_Integration:
  fusion_strategies:
    early_fusion: Combine raw features before processing
    late_fusion: Process modalities separately, merge outputs
    cross_attention: Attend across modalities during processing

  capabilities:
    - Read diagrams embedded in PDFs
    - Understand webpages by text and layout
    - Process video with audio transcription
    - Interpret charts and graphs
```

---

## PART IV: PLANNING PRIMITIVES

### 4.1 Goal Decomposition

```yaml
Goal_Decomposition:
  hierarchical:
    - Top-level goal to abstract subgoals
    - Abstract subgoals to concrete tasks
    - Concrete tasks to primitive actions

  temporal:
    - Deadline and duration constraints
    - Dependency ordering
    - Parallel execution opportunities

  resource_aware:
    - Token budget allocation
    - API call optimization
    - Compute distribution
```

### 4.2 Contingency Planning

```yaml
Contingency_Planning:
  anticipate:
    - Common failure modes
    - External dependencies
    - Edge cases

  prepare:
    - Alternative paths
    - Fallback actions
    - Graceful degradation

  implement:
    - If-then-else branches in plan
    - Retry with exponential backoff
    - Escalation triggers
```

### 4.3 Dynamic Replanning

```yaml
Dynamic_Replanning:
  triggers:
    - Action failure
    - Unexpected observation
    - Goal modification
    - Resource constraint change

  process:
    - Assess current state
    - Identify deviation from plan
    - Generate alternative paths
    - Select and execute new plan

  constraints:
    - Preserve completed work
    - Minimize disruption
    - Maintain consistency
```

---

## PART V: PRIMITIVE COMPOSITION

### 5.1 Sequential Pipeline

```
Perception → Reasoning → Planning → Execution → Observation → Loop
```

Simple, debuggable, but errors cascade. Mitigate with intermediate validation.

### 5.2 Parallel Processing

Multiple reasoning threads or solution attempts concurrently. Use voting or confidence-based selection to handle conflicts.

### 5.3 Hierarchical Recursive

Parent agents spawn sub-agents; sub-agents may spawn further helpers. Requires meta-level control and stopping criteria to prevent infinite recursion.

### 5.4 Feedback Loops

Cyclic composition where output feeds next iteration (Plan-Do-Check-Act). Implement safeguards: iteration limits, convergence detection.

---

## SATELLITES

None. This is a leaf asteroid.

---

## VERSION HISTORY

**Version 1.0.0** (December 2025): Genesis establishment
