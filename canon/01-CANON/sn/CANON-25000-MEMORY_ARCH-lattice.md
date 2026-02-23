---
id: [[CANON-25000-MEMORY_ARCH-lattice]]
name: Memory Architecture
tier: lattice
sn_version: 1.0
converted: 2026-01-24
original_words: 4680
sn_words: 1280
compression: 73%
---

# Κ-25000: Memory Architecture (SN)

TERM MemorySovereignty:
    sutra: "File system = ground truth; platform memory = operational cache. Control memory architecture = control augmented cognition"
    gloss:
        Memory sovereignty spectrum: Captured (platform-locked, opaque) ↔ Sovereign
        (file-based, git-versioned, auditable). Syncrescendence maximizes sovereignty
        through file-based canonical memory while leveraging platform-native memory
        for operational convenience. Who controls memory controls continuity.
    spec:
        spectrum:
            Captured: platform_locked | no_export | opaque | platform_dependent
            Hybrid: portable | inspectable | adaptable
            Sovereign: file_system | git_versioned | fully_auditable | platform_agnostic
        position: file_system_is_ground_truth | platform_memory_is_cache
        refs: [[CANON-00005-SYNCRESCENDENCE]], [[CANON-31140-IIC]]
end

TERM SevenStrata:
    sutra: "Constitutional >> Preference >> Accumulated >> Project >> Canonical >> Thread >> Tool-Extended"
    gloss:
        Seven memory strata operate in every AI interaction: Constitutional (immutable
        platform identity), Preference (user calibrations), Accumulated (system-inferred
        facts), Project (scoped workspace), Canonical (RAG/corpus), Thread (active
        conversation), Tool-Extended (MCP/file system). Earlier strata constrain later.
    spec:
        Stratum_1_Constitutional:
            definition: immutable_identity_layer
            control: NONE | platform_determines
            examples: Anthropic_system_prompt | OpenAI_behaviors | model_weights
        Stratum_2_Preference:
            definition: user_specified_behavioral_calibrations
            control: FULL | user_authored_edited
            examples: Claude_User_Preferences | ChatGPT_Custom_Instructions | Gemini_Saved_Info
            protocol: signal_sophistication_level | keep_minimal | reserve_complexity_for_project
        Stratum_3_Accumulated:
            definition: system_generated_inferences
            control: PARTIAL | can_view_edit_delete | generation_automated
            examples: Claude_Memory | ChatGPT_Memory_feature
            protocol: curate_periodically | audit_for_drift | treat_as_cache_not_truth
        Stratum_4_Project:
            definition: scoped_context_for_workspaces
            control: FULL | user_created_configured
            examples: Claude_Projects | ChatGPT_Projects | Gemini_Gems | Perplexity_Spaces
            protocol: primary_operational_layer | configure_per_IIC
        Stratum_5_Canonical:
            definition: static_documents_for_retrieval
            control: FULL | user_curated_structured
            examples: Project_Files | uploads | vector_databases
            protocol: corpus_lives_here | structure_for_machine_parsability
        Stratum_6_Thread:
            definition: active_conversation_history
            control: FULL_within_session
            components: attachments | messages | artifacts
            protocol: working_memory | subdivide_by_persistence
        Stratum_7_Tool_Extended:
            definition: external_capabilities_via_tools
            control: FULL_self_hosted | PARTIAL_platform_provided
            examples: MCP_servers | conversation_search | file_system_access
            protocol: CLI_foyer_architecture | cross_platform_coordination
        cascade_principle: earlier_strata_constrain_later_strata
end

PROC CLIFoyerPattern:
    sutra: "CLI as coordination space—multiple AI systems access shared sovereign file context"
    gloss:
        CLI serves as foyer where multiple AI systems (Claude Code, Gemini CLI, Codex)
        access shared file-based context. Sovereign file system provides cross-platform
        coordination, git versioning, scriptability. Serious AI-augmented cognition
        happens in CLI—web interfaces constrain to conversational modality.
    spec:
        why_CLI_primary:
            1: file_system_access | read_write_sovereign_memory
            2: tool_execution | arbitrary_code_scripts_processes
            3: version_control | git_integration_for_memory_versioning
            4: cross_platform | multiple_CLI_tools_same_workspace
            5: scriptability | automation_of_cognitive_workflows
        foyer_structure:
            ~/syncrescendence/:
                corpus/: canonical_documents
                context/: active_context_files
                memory/: distilled_learnings
                .claude/: CLAUDE.md_hierarchy
        CLAUDE.md_hierarchy:
            enterprise: organization_wide_standards
            user: ~/.claude/CLAUDE.md | personal_defaults
            project: ./CLAUDE.md | project_specific_context
            directory: nested | subsystem_context
        cross_platform_coordination:
            shared: file_system | git_history | output_artifacts
            isolated: conversation_history | internal_reasoning | platform_memory
            protocol: files_as_communication | git_commits_as_sync_points
end

PROC DistillationProtocol:
    sutra: "Fluid >> Operational >> Canonical >> Eternal—structured movement between temporal horizons"
    gloss:
        Without principled distillation, memory suffers unbounded growth (retrieval
        degradation) or premature loss (reinvention overhead). Structured distillation
        moves knowledge: Thread → Memory → Corpus → Constitution. Thread culmination
        captures insights; corpus updates graduate stable patterns.
    spec:
        cascade:
            Fluid_Thread: thread_ends | insight_captured >> culmination_document
            Operational_Memory: pattern_emerges | worth_preserving >> memory_edit_or_context_file
            Canonical_Corpus: principle_proven | framework_stable >> corpus_update
            Eternal_Constitution: constitution_revision | rare
        thread_culmination:
            triggers:
                - context_gt_80%_capacity
                - natural_intellectual_milestone
                - significant_synthesis_requiring_preservation
                - explicit_practitioner_request
            output:
                1: trajectory_summary | how_conversation_evolved
                2: key_insights | novel_understanding_generated
                3: unresolved_questions | what_remains_open
                4: continuation_context | minimum_viable_for_resumption
                5: canonical_candidates | insights_worthy_of_corpus
        corpus_update_criteria:
            - insight_stable_across_multiple_applications
            - genuine_framework_evolution | not_task_specific
            - fills_identified_gap_in_coverage
            - aligns_with_constitutional_principles
        forgetting_protocol:
            decay_candidates: task_specific_after_completion | superseded_drafts | exploratory_nowhere | operational_details_after_pattern
            preservation_triggers: referenced_by_canonical | active_project | explicitly_marked | unreplicated_insights
end

TERM IICMemoryConfig:
    sutra: "Each IIC chain requires distinct memory configuration—breadth vs depth, turnover vs persistence"
    gloss:
        IIC accounts need memory calibrated to chain function: Acumen (breadth, rapid
        turnover), Coherence (pattern integration, moderate persistence), Efficacy
        (process knowledge, high procedure persistence), Mastery (stable pedagogical),
        Transcendence (meta-patterns, maximum persistence across longest timescales).
    spec:
        Acumen_IIC:
            chain: Information_Sensing
            priority: breadth_over_depth | high_volume | rapid_turnover
            canonical_focus: feed_curation | source_evaluation | signal_detection
            forgetting_bias: AGGRESSIVE | most_sensing_decays_quickly
            persistence: only_patterns_and_qualified_signals
        Coherence_IIC:
            chain: Insight_Synthesis
            priority: pattern_integration | medium_volume | medium_persistence
            canonical_focus: frameworks | models | synthesis_artifacts
            forgetting_bias: MODERATE | preserve_frameworks | decay_examples
            persistence: synthesis_outputs_persist | raw_inputs_decay
        Efficacy_IIC:
            chain: Expertise_Operations
            priority: process_knowledge | task_oriented | high_procedure_persistence
            canonical_focus: workflows | checklists | operational_protocols
            forgetting_bias: LOW_for_procedures | HIGH_for_task_details
            persistence: proven_procedures_canonical | experiments_decay
        Mastery_IIC:
            chain: Knowledge_Curriculum
            priority: pedagogical_structure | stable | curated | polished
            canonical_focus: teaching_materials | explanations | curricula
            forgetting_bias: VERY_LOW | educational_content_stable
            persistence: HIGH | distilled_transmission_ready
        Transcendence_IIC:
            chain: Wisdom_Meta_cognitive
            priority: meta_patterns | long_horizons | civilizational_scale
            canonical_focus: strategic_frameworks | phase_transition_signals | eternal_principles
            forgetting_bias: MINIMAL | wisdom_accumulates_across_longest_timescales
            persistence: MAXIMUM | integration_point_for_all_chains
        synchronization: corpus_itself | all_IICs_access_same_canonical_documents
        refs: [[CANON-31140-IIC]], [[CANON-31130-SEVEN_LAYER]]
end

ARTIFACT MemoryOperational:
    sutra: "Checklists for session start, culmination, corpus update, monthly hygiene"
    gloss:
        Operational protocols: New session (verify context, check memory, inject
        continuation), Thread culmination (generate document, identify candidates,
        save artifacts), Corpus update (verify criteria, check placement, git commit),
        Monthly hygiene (audit memory, remove obsolete, archive completed).
    spec:
        new_session_checklist:
            - verify_correct_account_project_context
            - check_relevant_corpus_accessible
            - review_accumulated_memory_accuracy
            - inject_required_continuation_context
            - confirm_tool_access
        culmination_checklist:
            - generate_culmination_document
            - identify_canonical_candidates
            - save_artifacts_to_appropriate_location
            - update_context_files_if_needed
            - git_commit_if_CLI
        corpus_update_checklist:
            - verify_graduation_criteria_met
            - check_chain_tier_placement
            - update_version_number
            - verify_cross_references
            - git_commit_descriptive_message
            - propagate_to_relevant_IIC_projects
        monthly_hygiene_checklist:
            - audit_accumulated_memory_accuracy
            - remove_obsolete_memory_entries
            - archive_completed_project_contexts
            - review_forgetting_candidates
            - verify_corpus_integrity
        refs: [[CANON-25100-CONTEXT_TRANS]]
end

