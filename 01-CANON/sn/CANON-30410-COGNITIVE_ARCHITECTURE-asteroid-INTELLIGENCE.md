---
id: [[CANON-30410-COGNITIVE_ARCHITECTURE-asteroid-INTELLIGENCE]]
name: Cognitive Architecture
tier: asteroid
chain: INTELLIGENCE
parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
sn_version: 1.0
converted: 2026-01-24
original_words: 2085
sn_words: 420
compression: 80%
---

# Κ-30410: Cognitive Architecture (SN)

TERM CognitiveArchitecture:
    sutra: "CoALA modules + reasoning patterns + primitives = autonomous agent cognition"
    gloss:
        Detailed specifications for cognitive architectures powering autonomous agents.
        Implementation depth for CoALA framework, reasoning patterns, and cognitive primitives.
    spec:
        identity: COGNITIVE_ARCHITECTURE
        parent: [[CANON-30400-AGENTIC_ARCHITECTURE]]
end

PASS CoALAFramework:
    sutra: "Perception → Memory → Planning → Action → Learning—modular with defined interfaces"
    spec:
        perception_module:
            function: raw_environmental_data >> structured_representations
            inputs: [text, images, APIs, user_interactions, sensors]
            components: [text_encoder, visual_encoder, multimodal_fusion, entity_intent_extractors]
        memory_module:
            function: store_retain_retrieve_across_timescales
            types:
                working: immediate_context | rapid_access | limited_capacity
                episodic: interaction_sequences | experience_replay
                semantic: facts_concepts_relationships
                procedural: skills_action_sequences
                prospective: future_intentions_scheduled
            interfaces: [write(content,type,metadata), read(query,type,top_k), update(id,delta), forget(criteria)]
        planning_module:
            function: goals >> actionable_steps
            capabilities: [goal_hierarchy, subgoal_lattice, action_sequence, contingency_branches, resource_reasoning]
            interfaces: [plan(goal,context,constraints), replan(feedback,partial), evaluate(plan,criteria)]
        action_module:
            function: execute_environment_interactions
            capabilities: [tool_invocation, response_generation, state_modification, sub_agent_spawning]
            interfaces: [execute(action,params), validate(result,expectation), rollback(action_id)]
        learning_module:
            function: improve_through_experience
            capabilities: [performance_evaluation, error_analysis, strategy_refinement, knowledge_extraction]
            interfaces: [evaluate(trajectory,outcome), reflect(experience,criteria), update(policy,feedback)]
end

PASS ReasoningPatterns:
    sutra: "ReAct interleaves, Reflexion self-corrects, HTN decomposes, ToT explores, Extended CoT deliberates"
    spec:
        ReAct:
            pattern: Thought >> Action >> Observation >> Loop
            performance: +34%_ALFWorld | +10%_WebShop
            limitation: linear_trial_error | prone_to_loops | requires_formatted_observations
        Reflexion:
            components: Actor (ReAct) + Evaluator (scores) + Self_Reflection (linguistic_proposals)
            loop: Attempt >> Evaluate >> Reflect >> Store >> Retry_with_reflection
            key: no_fine_tuning | learning_through_NL | episodic_enables_cross_attempt
        HTN:
            structure: high_level_root >> sub_tasks >> primitive_actions_at_leaves
            hybrid: symbolic_planner (structured) + LLM (generates_when_rules_missing)
            optimal: HTN_generates_tree + Reflexion_agents_execute_leaves + local_self_correction
        Tree_of_Thoughts:
            structure: tree_of_coherent_intermediate_states | branches = alternative_paths
            search: BFS (parallel) | DFS (deep_promising)
            evaluation: sure | maybe | impossible >> enables_backtracking
            performance: +8%_NATURAL_PLAN | +4%_OlympiadBench | +7%_DocFinQA
        Extended_CoT:
            mechanism: cold_start_SFT + GRPO + multi_stage_deliberation
            characteristics: extended_reasoning_invisible | trades_latency_for_accuracy
            performance: ~83%_AIME
            models: DeepSeek-R1 | GPT-o1
            tradeoff: increased_latency + compute >> significantly_improved_accuracy_on_complex
end

PASS PerceptionPrimitives:
    sutra: "Text NLU, visual detection, multimodal fusion—raw to structured"
    spec:
        text_perception:
            intent: classify_category | extract_verbs_targets | identify_implicit
            entity: named_entities | temporal | quantities | domain_specific
            sentiment: polarity | emotion | urgency
            relationship: subject_predicate_object | causal | temporal_sequences
        visual_perception:
            object_detection: identify_localize | bounding_box | confidence
            scene_understanding: classification | spatial_relations | activity
            OCR: text_extraction | document_structure | handwriting
        multimodal_integration:
            fusion: early (raw_features) | late (merge_outputs) | cross_attention (during)
            capabilities: [diagrams_in_PDFs, webpages_text_layout, video_with_audio, charts_graphs]
end

PASS PlanningPrimitives:
    sutra: "Decompose goals, anticipate contingencies, replan dynamically"
    spec:
        goal_decomposition:
            hierarchical: top_level >> abstract_subgoals >> concrete_tasks >> primitives
            temporal: deadlines_durations | dependency_ordering | parallel_opportunities
            resource_aware: token_budget | API_optimization | compute_distribution
        contingency_planning:
            anticipate: common_failures | external_dependencies | edge_cases
            prepare: alternative_paths | fallback_actions | graceful_degradation
            implement: if_then_else_branches | exponential_backoff | escalation_triggers
        dynamic_replanning:
            triggers: action_failure | unexpected_observation | goal_modification | resource_change
            process: assess_state >> identify_deviation >> generate_alternatives >> select_execute
            constraints: preserve_completed | minimize_disruption | maintain_consistency
end

PASS PrimitiveComposition:
    sutra: "Sequential simple, parallel efficient, hierarchical recursive, feedback loops iterate"
    spec:
        sequential_pipeline:
            pattern: Perception >> Reasoning >> Planning >> Execution >> Observation >> Loop
            property: simple_debuggable | errors_cascade
            mitigation: intermediate_validation
        parallel_processing:
            pattern: multiple_threads_or_attempts_concurrent
            conflict: voting | confidence_based_selection
        hierarchical_recursive:
            pattern: parent_spawns_sub_agents >> sub_agents_spawn_helpers
            requirement: meta_level_control | stopping_criteria | prevent_infinite_recursion
        feedback_loops:
            pattern: Plan >> Do >> Check >> Act (PDCA)
            safeguards: iteration_limits | convergence_detection
end
