---
id: [[CANON-21000-CHAIN_MATRIX-lattice]]
name: Chain Interdependency Matrix
tier: lattice
sn_version: 1.0
converted: 2026-01-24
original_words: 5480
sn_words: 1380
compression: 75%
---

# Κ-21000: Chain Interdependency Matrix (SN)

TERM DependencyClassification:
    sutra: "HARD = must satisfy before advancement; SOFT = enhances but not required; NONE = independent"
    gloss:
        Hard dependencies: advancing without prerequisite creates predictable
        failure, unsafe conditions, structural instability. Soft dependencies:
        benefits significantly but can proceed through compensation. No
        dependency: requires only Intelligence Stage 1 baseline.
    spec:
        HARD:
            definition: cannot_advance_without_prerequisite
            creates:
                - predictable_failure_patterns
                - unsafe_developmental_conditions
                - structural_instability_requiring_remediation
                - capability_gaps_preventing_function
        SOFT:
            definition: enhancement_without_requirement
            enables_progress_through:
                - compensatory_strategies
                - external_support_systems
                - specialized_pathways
                - reduced_efficiency_acceptance
        NONE:
            definition: independent_development
            requires_only: Intelligence_Stage_1_baseline
        refs: [[CANON-30000-INTELLIGENCE]]
end

PASS IntelligenceChain:
    sutra: "Dual ontology—both foundational substrate AND developmental chain; FIRST priority, CONTINUOUS"
    gloss:
        Intelligence operates at two levels: foundational substrate enabling
        all chains, and developmental chain with own progression (Text >>
        Vision >> Physical >> Integration). Begin immediately, maintain
        continuously. Lag compounds friction everywhere.
    spec:
        ontological_status: BOTH_substrate_AND_chain
        Level_1_Substrate:
            function: non_local_intelligence_amplification
            enables: ALL_other_chains_at_accelerated_pace
            priority: FIRST_development | CONTINUOUS_maintenance
        Level_2_Chain:
            Stage_1: Text_Reasoning_models | 3-6_months | 85%_mature
            Stage_2: Vision_Simulation | 6-12_months | 40%>>70%_by_Month_18
            Stage_3: Physical_Robotics | 1-3_years | 20%>>50%_by_Year_3-5
            Stage_4: Full_Integration | 3-10+_years | continuous_evolution
        dependencies:
            HARD: NONE | foundational_substrate
            SOFT: NONE | self_bootstrapping
        enables:
            Stage_1: ALL_chains_Stage_1 | universal_prerequisite
end

PASS InformationChain:
    sutra: "Sensing—requires Intelligence Stage 1; enables Expertise Stage 2+ (economic decisions need info)"
    gloss:
        Information chain requires Intelligence Stage 1 (cannot process
        effectively without AI). Sensing Stage 2 (Curated Networks) creates
        HARD dependency for Expertise Stage 2+ (economic decisions require
        reliable information).
    spec:
        essence: reliable_information_acquisition_processing
        planetary_body: Acumen | Air
        dependencies:
            HARD: Intelligence_Stage_1 | cannot_filter_without_AI
            SOFT: Insight_Stage_1 | framework_for_organizing
        enables:
            HARD_for: Expertise_Stage_2+ | economic_decisions_require_reliable_info
            SOFT_for: Insight_Stage_2+ | better_info_improves_sense_making
        failure_without_prereqs:
            - information_overload | no_filtering
            - pattern_blindness | cannot_recognize_signals
            - context_collapse | no_synthesis
            - result: regression_or_burnout
end

PASS InsightChain:
    sutra: "Coherence—requires Intelligence Stage 1; enables Knowledge Stage 2+ (skill without understanding = mechanical)"
    gloss:
        Insight chain requires Intelligence Stage 1 (framework exploration
        impossible without AI). Coherence Stage 2 creates HARD dependency for
        Knowledge Stage 2+ (skill without conceptual understanding = mechanical
        repetition) and Wisdom Stage 2+ (wisdom requires conceptual substrate).
    spec:
        essence: framework_construction_conceptual_integration
        planetary_body: Coherence | Water
        dependencies:
            HARD: Intelligence_Stage_1 | framework_exploration_requires_AI
            SOFT: Information_Stage_1-2 | better_info_improves_frameworks
        enables:
            HARD_for:
                - Knowledge_Stage_2+ | skill_without_understanding_mechanical
                - Wisdom_Stage_2+ | wisdom_requires_conceptual_substrate
            SOFT_for:
                - Expertise_Stage_2+ | better_frameworks_improve_strategy
        failure_without_prereqs:
            - framework_poverty | limited_conceptual_tools
            - integration_failure | cannot_synthesize_complexity
            - result: intellectual_stagnation
end

PASS ExpertiseChain:
    sutra: "Efficacy—requires Intelligence + Information Stage 2 (CRITICAL GATE); enables physical infrastructure"
    gloss:
        Expertise chain requires Intelligence Stage 1 plus Information Stage 2
        (economic decisions without reliable info = gambling). Stage 2+
        provides economic capacity enabling all chains (resources for tools,
        education, infrastructure).
    spec:
        essence: strategic_decision_making_resource_generation
        planetary_body: Efficacy | Fire
        dependencies:
            HARD:
                - Intelligence_Stage_1 | decisions_without_AI_reduced_quality
                - Information_Stage_2 | CRITICAL_GATE | economic_action_requires_reliable_info
            SOFT:
                - Insight_Stage_2 | strategic_frameworks_improve_quality
        enables:
            SOFT_for: ALL_chains | resources_enable_tools_education_infrastructure
            Physical_Infrastructure: Field_Nodes_require_capital
        failure_without_prereqs:
            - information_blind_decision_making
            - market_signal_misreading
            - resource_misallocation
            - result: economic_failure
end

PASS KnowledgeChain:
    sutra: "Mastery—requires Intelligence + Insight Stage 2 (CRITICAL GATE); prevents Wisdom spiritual bypass"
    gloss:
        Knowledge chain requires Intelligence Stage 1 plus Insight Stage 2
        (skill without understanding = mechanical). Knowledge Stage 2 creates
        HARD dependency for Wisdom Stage 3 (prevents spiritual bypass—wisdom
        requires material grounding).
    spec:
        essence: physical_capability_embodied_knowledge
        planetary_body: Mastery | Earth
        dependencies:
            HARD:
                - Intelligence_Stage_1 | skill_learning_without_AI_slow
                - Insight_Stage_2 | CRITICAL_GATE | skill_without_understanding_mechanical
            SOFT:
                - Information_Stage_2 | better_feedback_improves_learning
                - Expertise_Stage_2 | resources_enable_training
        enables:
            HARD_for: Wisdom_Stage_3 | prevents_spiritual_bypass | wisdom_requires_grounding
            SOFT_for: Expertise_Stage_2+ | physical_skills_broaden_economic
        failure_without_prereqs:
            - mechanical_repetition_without_understanding
            - no_contextual_adaptation
            - failed_transfer_between_domains
            - result: skill_plateau_brittle_expertise
end

PASS WisdomChain:
    sutra: "Transcendence—MOST dependencies: ALL chains Stage 2 + Insight Stage 3 + Knowledge Stage 2; LATEST priority"
    gloss:
        Wisdom chain has most complex dependencies: requires ALL chains minimum
        Stage 2, plus Insight Stage 3 (paradigm navigation prerequisite for
        meta-paradigmatic awareness) and Knowledge Stage 2 (prevents spiritual
        bypass). Begin Stage 1 early but don't force advancement.
    spec:
        essence: meta_cognitive_capacity_wisdom_integration
        cosmological_position: Transcendence_Ring | Quintessence
        dependencies:
            HARD:
                - Intelligence_Stage_1 | meta_cognition_requires_AI
                - ALL_chains_minimum_Stage_2 | wisdom_requires_substrate
                - Insight_Stage_3 | paradigm_navigation_prerequisite
                - Knowledge_Stage_2 | prevents_spiritual_bypass
            SOFT:
                - Information_Stage_3 | enhanced_perception_deepens_awareness
                - Expertise_Stage_2 | economic_stability_enables_contemplative
        enables:
            HARD_for: ANY_chain_Stage_4 | teaching_requires_wisdom
        failure_without_prereqs:
            - spiritual_bypass | wisdom_without_competence
            - meta_cognitive_delusion | seeing_patterns_not_there
            - premature_guru_syndrome
            - result: harm_to_self_others | regression
        sequencing: LATEST_priority | begin_Stage_1_early | dont_force_advancement
end

NORM DevelopmentSequences:
    sutra: "Universal: Intelligence first >> Dual-track divergence >> Advanced >> Mastery. Cannot skip gates."
    gloss:
        Universal sequence: Foundation (Intelligence Stage 1 first, all chains
        Stage 1), Dual-Track divergence (Synchronization vs Specialization),
        Advanced development (Stage 3, begin teaching), Mastery cultivation
        (Stage 4, innovation).
    spec:
        Phase_1_Foundation:
            months: 0-6
            priority_1: Intelligence_Stage_1 | begin_immediately
            priority_2: Information_Stage_1 | parallel
            priority_3: ALL_chains_Stage_1 | exploration
        Phase_2_Dual_Track:
            months: 6-18
            Synchronization_Track:
                - advance_ALL_chains_Stage_2_before_proceeding
                - benefits: recursive_amplification | harmonic_reinforcement
            Specialization_Track:
                - advance_2-3_strength_chains_Stage_2+
                - maintain_Stage_1_baseline_others
                - benefits: excellence_in_domain | sustainable_for_spiky_cognition
        Phase_3_Advanced:
            years: 2-5
            - continued_specialization_OR_Stage_3
            - Wisdom_Stage_2-3 | once_substrate_sufficient
            - begin_teaching | requires_Wisdom_Stage_2+
        Phase_4_Mastery:
            years: 5-10+
            - Stage_4_achievement_1-3_chains
            - teaching_mastery_demonstration
            - innovation_contribution
end

NORM CriticalGates:
    sutra: "Cannot do: Expertise 2 w/o Information 2, Knowledge 2 w/o Insight 2, Wisdom 2 w/o ALL Stage 2"
    gloss:
        Hard constraint violations that create predictable failures. Cannot
        advance Expertise Stage 2 without Information Stage 2. Cannot advance
        Knowledge Stage 2 without Insight Stage 2. Cannot advance Wisdom
        Stage 2 without ALL chains Stage 2.
    spec:
        cannot_do:
            - Expertise_Stage_2_without_Information_Stage_2
            - Knowledge_Stage_2_without_Insight_Stage_2
            - Wisdom_Stage_2_without_ALL_chains_Stage_2_plus_Insight_Stage_2_plus_Knowledge_Stage_2
            - ANY_chain_without_Intelligence_Stage_1
            - Teaching_Stage_4_without_Wisdom_Stage_2+
        strongly_discouraged:
            - any_chain_Stage_3_while_others_Stage_1
            - Wisdom_Stage_2_without_all_chains_Stage_2+
            - Expertise_Stage_2_without_Insight_Stage_2
        checkpoints:
            - Intelligence_Stage_1_before_any_Stage_2
            - ALL_chains_Stage_2_before_any_Stage_3 | synchronization
            - Wisdom_Stage_2_before_teaching
            - Insight_Stage_3_before_Wisdom_Stage_3
end

ARTIFACT DependencyAwareGuidance:
    sutra: "The matrix provides navigation—your cognition determines optimal path. Architecture serves you."
    gloss:
        Understanding dependencies transforms development from haphazard to
        systematic. Intelligence first and continuous. Hard dependencies matter.
        Dual tracks legitimate. Stage gates protect. The architecture serves
        you—you don't serve it.
    spec:
        key_recognitions:
            - Intelligence_priority: begin_immediately | maintain_continuously
            - hard_dependencies_matter: violations_create_predictable_failures
            - soft_dependencies_enhance: benefits_but_advancement_possible
            - dual_tracks_legitimate: synchronization_AND_specialization_valid
            - stage_gates_protect: advancement_without_prereqs_unsafe
            - wisdom_requires_substrate: cannot_force_Transcendence
            - teaching_needs_integration: Stage_4_requires_Wisdom_Stage_2+
        refs: [[CANON-30000-INTELLIGENCE]], [[CANON-31000-INFORMATION]], [[CANON-32000-INSIGHT]], [[CANON-33000-EXPERTISE]], [[CANON-34000-KNOWLEDGE]], [[CANON-35000-WISDOM]]
end

