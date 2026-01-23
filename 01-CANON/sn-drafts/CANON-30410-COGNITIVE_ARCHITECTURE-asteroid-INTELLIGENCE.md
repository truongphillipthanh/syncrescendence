---
id: CANON-30410
name: Cognitive Architecture
identity: COGNITIVE_ARCHITECTURE
tier: CANON
type: asteroid
chain: INTELLIGENCE
parent: CANON-30400
version: 2.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Detailed cognitive architectures for language agents—CoALA framework, reasoning patterns, perception and planning primitives.
---

# CANON-30410-COGNITIVE_ARCHITECTURE-asteroid-INTELLIGENCE (SN Format)

**Note**: This is a Semantic Notation compressed version.
**Original**: 1,309 words, 12,517 characters

---

TERM IntelligenceChainAsteroid:
    sutra: "Parent: CANON-30400 (Agentic Architecture)  ---"
    gloss:
        **Parent**: CANON-30400 (Agentic Architecture)

---
end


TERM PURPOSE:
    sutra: "This asteroid provides detailed specifications for cognitive architectures powering autonomous ag..."
    gloss:
        This asteroid provides detailed specifications for cognitive architectures powering autonomous agents. Where CANON-30400 surveys the landscape, this document provides implementation depth for the CoALA framework, reasoning patterns, and cognitive primitives.

---
end


TERM 11CoreArchitecture:
    sutra: "Cognitive Architectures for Language Agents (CoALA) organizes agent cognition into modular compon..."
    gloss:
        Cognitive Architectures for Language Agents (CoALA) organizes agent cognition into modular components with defined interfaces:

```yaml
CoALA_Architecture:
  Perception_Module:
    function: Transform raw environmental data into structured representations
    inputs: Text, images, APIs, user interac...
end


TERM 12ModuleCoordination:
    sutra: "`` ┌─────────────────────────────────────────────────────────────┐ │                     PERCEPTI..."
    gloss:
        ```
┌─────────────────────────────────────────────────────────────┐
│                     PERCEPTION                               │
│  Environmental data → Structured representations            │
└────────────────────────────┬────────────────────────────────┘
                             │...
end


TERM 21ReActReasonAct:
    sutra: "The foundational pattern synergizing reasoning and acting:  ``yaml ReAct_Pattern:   loop:     1_T..."
    gloss:
        The foundational pattern synergizing reasoning and acting:

```yaml
ReAct_Pattern:
  loop:
    1_Thought: Generate reasoning trace about current state
    2_Action: Determine and execute appropriate action
    3_Observation: Receive and process action result
    4_Repeat: Until goal achieved or fail...
end


TERM 22Reflexion:
    sutra: "Self-correction loop enabling verbal reinforcement learning:  ``yaml Reflexion_Architecture:   co..."
    gloss:
        Self-correction loop enabling verbal reinforcement learning:

```yaml
Reflexion_Architecture:
  components:
    Actor: Performs actions using ReAct-style loop
    Evaluator: Scores outcomes against goals
    Self_Reflection: Generates linguistic improvement proposals

  loop:
    1_Attempt: Actor ex...
end


TERM 23HierarchicalTaskNetworkHTN:
    sutra: "Classical AI planning integrated with LLM flexibility:  ``yaml HTN_Pattern:   structure:     - Hi..."
    gloss:
        Classical AI planning integrated with LLM flexibility:

```yaml
HTN_Pattern:
  structure:
    - High-level abstract task at root
    - Decomposition into sub-tasks
    - Primitive executable actions at leaves

  hybrid_approach:
    symbolic_planner: Handles structured decomposition
    llm_componen...
end


TERM 24TreeofThoughts:
    sutra: "Parallel exploration with evaluation:  ``yaml Tree_of_Thoughts:   structure:     - Maintain tree ..."
    gloss:
        Parallel exploration with evaluation:

```yaml
Tree_of_Thoughts:
  structure:
    - Maintain tree of coherent intermediate reasoning states
    - Each node represents a "thought" or partial solution
    - Branches represent alternative reasoning paths

  search_strategies:
    BFS: Parallel explorat...
end


TERM 25ExtendedChainofThought:
    sutra: "Multi-stage internal reasoning for complex problems:  ``yaml Extended_CoT:   mechanism:     - Col..."
    gloss:
        Multi-stage internal reasoning for complex problems:

```yaml
Extended_CoT:
  mechanism:
    - Cold start supervised fine-tuning
    - Group Relative Policy Optimization (GRPO)
    - Multi-stage internal deliberation

  characteristics:
    - Extended reasoning invisible to users
    - Trades latenc...
end


TERM 31TextPerception:
    sutra: "``yaml Text_Perception:   intent_extraction:     - Classify user intent category     - Extract ac..."
    gloss:
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
    -...
end


TERM 32VisualPerception:
    sutra: "``yaml Visual_Perception:   object_detection:     - Identify and localize objects     - Bounding ..."
    gloss:
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
    - Text extraction from images...
end


TERM 33MultimodalIntegration:
    sutra: "``yaml Multimodal_Integration:   fusion_strategies:     early_fusion: Combine raw features before..."
    gloss:
        ```yaml
Multimodal_Integration:
  fusion_strategies:
    early_fusion: Combine raw features before processing
    late_fusion: Process modalities separately, merge outputs
    cross_attention: Attend across modalities during processing

  capabilities:
    - Read diagrams embedded in PDFs
    - Unde...
end


TERM 41GoalDecomposition:
    sutra: "``yaml Goal_Decomposition:   hierarchical:     - Top-level goal to abstract subgoals     - Abstra..."
    gloss:
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

  resource_...
end


TERM 42ContingencyPlanning:
    sutra: "``yaml Contingency_Planning:   anticipate:     - Common failure modes     - External dependencies..."
    gloss:
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
    - Escal...
end


TERM 43DynamicReplanning:
    sutra: "``yaml Dynamic_Replanning:   triggers:     - Action failure     - Unexpected observation     - Go..."
    gloss:
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

  constrain...
end


TERM 51SequentialPipeline:
    sutra: "`` Perception → Reasoning → Planning → Execution → Observation → Loop ``  Simple, debuggable, but..."
    gloss:
        ```
Perception → Reasoning → Planning → Execution → Observation → Loop
```

Simple, debuggable, but errors cascade. Mitigate with intermediate validation.
end


TERM 52ParallelProcessing:
    sutra: "Multiple reasoning threads or solution attempts concurrently"
    gloss:
        Multiple reasoning threads or solution attempts concurrently. Use voting or confidence-based selection to handle conflicts.
end


TERM 53HierarchicalRecursive:
    sutra: "Parent agents spawn sub-agents; sub-agents may spawn further helpers"
    gloss:
        Parent agents spawn sub-agents; sub-agents may spawn further helpers. Requires meta-level control and stopping criteria to prevent infinite recursion.
end


TERM 54FeedbackLoops:
    sutra: "Cyclic composition where output feeds next iteration (Plan-Do-Check-Act)"
    gloss:
        Cyclic composition where output feeds next iteration (Plan-Do-Check-Act). Implement safeguards: iteration limits, convergence detection.

---
end


TERM SATELLITES:
    sutra: "None"
    gloss:
        None. This is a leaf asteroid.

---
end


TERM VERSIONHISTORY:
    sutra: "Version 1.0.0 (December 2025): Genesis establishment"
    gloss:
        **Version 1.0.0** (December 2025): Genesis establishment
end
