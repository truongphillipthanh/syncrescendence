---
id: [[CANON-25100-CONTEXT_TRANS-lattice]]
name: Context Transition Protocol
tier: lattice
sn_version: 1.0
converted: 2026-01-24
original_words: 4380
sn_words: 1120
compression: 74%
---

# Κ-25100: Context Transition Protocol (SN)

TERM UnifiedInterface:
    sutra: "Single command triggers context analysis—AI determines optimal mode(s), practitioner maintains strategic sovereignty"
    gloss:
        Context transitions are a single category with multiple modes. The AI is the
        librarian determining what's needed; practitioner doesn't choose between
        culmination/continuation/compression—system analyzes context and produces
        appropriate output. Terminal architecture thesis: AI mediates complexity.
    spec:
        principal_commands:
            - "Handle context transition"
            - "Close this session"
            - "Continue from [previous]"
            - "Context getting long—compress"
            - implicit: approaching_limits | natural_conclusion
        system_response:
            1: analyze_current_context_state
            2: determine_appropriate_modes
            3: generate_transition_artifacts
            4: present_for_principal_review
        design_principle: practitioner_doesnt_select_mode | AI_does
        refs: [[CANON-25000-MEMORY_ARCH]]
end

TERM ContextStateVariables:
    sutra: "Position + Capacity + Value Density + Continuation Need + Temporal Gap + Complexity → mode selection"
    gloss:
        AI evaluates state variables to determine mode: Position (thread start/mid/end),
        Capacity (% context used), Value Density (insights generated?), Continuation
        Need (will work resume?), Temporal Gap (time since last session), Complexity
        (simple or rich state?).
    spec:
        variables:
            Position: thread_start_mid_end >> continuation_vs_culmination_vs_compression
            Capacity: percent_context_window >> compression_urgency
            Value_Density: insights_generated >> culmination_depth_needed
            Continuation_Need: will_resume >> continuation_artifact_needed
            Temporal_Gap: time_since_last >> context_restoration_depth
            Complexity: simple_or_rich >> artifact_comprehensiveness
        mode_selection_logic:
            IF_thread_ending_OR_explicit_close:
                IF_significant_insights: INCLUDE_culmination_mode
                IF_work_resumes: INCLUDE_continuation_mode
            IF_capacity_gt_70%_AND_continuing: INCLUDE_compression_mode
            IF_thread_starting_AND_prior_context: INCLUDE_continuation_mode_as_injection
            GENERATE: composite_artifact(selected_modes)
end

TERM ThreeModes:
    sutra: "Culmination (capture value) | Continuation (enable resumption) | Compression (reduce footprint)"
    gloss:
        Three modes serve distinct teleologies: Culmination (thread ending with value—
        capture insights, identify canonical candidates), Continuation (thread boundary
        where work resumes—enable seamless resumption), Compression (context approaching
        limits—preserve essential, reduce tokens).
    spec:
        Culmination:
            trigger: thread_ending_with_value_to_preserve
            teleology: capture_insights | identify_canonical_candidates | create_historical_record
            output_focus: what_was_learned | what_should_persist
        Continuation:
            trigger: thread_boundary_where_work_resumes
            teleology: enable_seamless_resumption_without_re_explanation
            output_focus: what_state_must_restore | whats_entry_point
        Compression:
            trigger: context_approaching_limits_mid_stream
            teleology: preserve_essential_while_reducing_footprint
            output_focus: what_must_survive | what_can_regenerate
end

PROC TransitionArtifact:
    sutra: "Single adaptive template with sections activated by mode—Context State + Synthesis + Continuation + Compression + Next Actions"
    gloss:
        Unified template with sections activated based on mode selection. Always includes
        Context State Summary and Next Actions. Synthesis section for culmination mode,
        Continuation State for continuation mode, Compression section when compressing.
        Quality: stands alone, mode-appropriate, actionable, auditable, efficient.
    spec:
        structure:
            header: timestamp | thread_reference | modes_active
            ALWAYS_Context_State_Summary:
                position: where_in_work
                capacity: utilization_if_relevant
                principal_focus: current_objective
            IF_Culmination_Synthesis:
                trajectory: how_work_evolved | key_turns_pivots_discoveries
                key_insights: insight_title + elaboration + implication
                canonical_candidates: insight | proposed_CANON_location | status
                unresolved_questions: open_items
            IF_Continuation_State:
                essential_context: minimum_viable_for_resumption
                key_decisions_made: list
                active_constraints: list
                current_objective: statement
                entry_point: "We were [state]. Next step is [action]. Key context: [facts]"
                resource_pointers: relevant_CANON | prior_artifacts
            IF_Compression:
                compressed_state: single_paragraph_essential
                preserved_elements: critical_items
                regeneration_guide: pointers_to_expand_if_needed
                discarded_elements: what_removed_why | enables_audit
            ALWAYS_Next_Actions: immediate_steps
        common_combinations:
            productive_session_will_resume: Culmination + Continuation | Full_Synthesis + Entry_Point
            context_limit_mid_work: Compression | Compressed_State + Regeneration_Guide
            starting_on_prior_work: Continuation_consumption | Entry_Point_as_injection
            thread_concluding_no_resume: Culmination_only | Full_Synthesis + Canonical_Candidates
            quick_checkpoint: Continuation_only | Essential_Context + Entry_Point
        quality_criteria:
            - stands_alone | readable_without_original_thread
            - mode_appropriate | includes_relevant_sections
            - actionable | clear_next_steps
            - auditable | shows_preserved_and_discarded
            - efficient | no_empty_sections_no_redundancy
end

PROC SessionLifecycle:
    sutra: "START (inject prior) >> WORK (ongoing analysis) >> COMPRESS (if >70%) >> CLOSE (culmination+continuation) >> ARCHIVE"
    gloss:
        Session lifecycle with unified protocol: Start (inject prior transition artifact),
        Work (ongoing context analysis), Compress (mid-session if capacity >70%),
        Close (end-session culmination + continuation as appropriate), Archive (store
        artifact, git commit).
    spec:
        lifecycle:
            SESSION_START:
                inject_context: prior_transition_artifact | continuation
            WORK_SESSION:
                context_analysis: ongoing
            COMPRESS_IF_NEEDED:
                trigger: capacity_gt_70%
                output: mid_session_transition | compression_mode
            CLOSE_SESSION:
                output: end_session_transition | culmination + continuation_as_appropriate
            ARCHIVE:
                action: store_artifact | git_commit
        triggers:
            automatic:
                - context_gt_80%
                - natural_conclusion_detected
                - extended_gap_in_conversation
                - significant_insight_generated
            explicit:
                - "Let's close this session"
                - "Checkpoint here"
                - "Need to switch to [other IIC/platform]"
                - "Prepare continuation context"
        principal_override:
            - "Just culmination, I won't continue this"
            - "Skip synthesis, just continuation context"
            - "Compress more aggressively"
            - "Include [specific element] I need preserved"
end

TERM IICTransitionProfiles:
    sutra: "Acumen=compression-heavy, Coherence=culmination-heavy, Efficacy=continuation-heavy, Mastery=archival, Transcendence=full composite"
    gloss:
        Each IIC has characteristic transition patterns: Acumen (compression-heavy,
        signal qualification), Coherence (culmination-heavy, framework synthesis),
        Efficacy (continuation-heavy, task state), Mastery (culmination + archival,
        pedagogical), Transcendence (full composite, strategic synthesis).
    spec:
        profiles:
            Acumen: compression_heavy | signal_qualification_pattern_alerts
            Coherence: culmination_heavy | framework_synthesis_integration_insights
            Efficacy: continuation_heavy | task_state_procedure_documentation
            Mastery: culmination_plus_archival | pedagogical_artifacts_curriculum_updates
            Transcendence: full_composite | strategic_synthesis_phase_transition_signals
        cross_IIC_handoff:
            source_generates: transition_artifact_with_continuation | framed_for_target_function
            principal_transfers: via_file_system_CLI_or_copy_paste_web
            target_receives: context_injection_calibrated_to_cognitive_personality
            addendum: Source | Target | handoff_rationale | target_task | translation_notes
        refs: [[CANON-31140-IIC]]
end

PROC OraclePedigree:
    sutra: "Historical lineage + decision archaeology + multi-model integration—repository-centric supersedes web-app handoffs"
    gloss:
        As work moves from web app to repository, Oracle Pedigree provides historical
        lineage tracking (Oracle 0 → current), decision archaeology (what decided and
        why), multi-model integration (tracks decisions across platforms). Handoffs
        remain useful for session init; Pedigree supersedes for decision archaeology.
    spec:
        pedigree_vs_handoff:
            handoff_useful_for: session_initialization | context_restoration | cross_platform_sync_push
            pedigree_supersedes_for: decision_archaeology_pull | multi_model_history | repo_centric_workflows | long_term_patterns
        pedigree_components:
            thread_id: "Oracle 12"
            campaign: phase_reference
            date: YYYY-MM-DD
            decisions:
                - id: DEC-XXX-NNN
                  principal_words: verbatim_quote
                  interpretation: Oracle_understanding
                  lenses_applied: [lens_numbers]
                  score: "N/18"
                  outcome: artifact_produced
            artifacts_produced: list
            handoff_state: open_threads | blocked_by | ready_for
        locations:
            thread_summaries: ARCH-ORACLE_ARC_SUMMARY.md
            decisions: ARCH-ORACLE_DECISIONS.md
            intentions: ARCH-INTENTION_COMPASS.md
            execution: EXECUTION_LOG-*.md
        refs: [[CANON-25200-CONSTELLATION_ARCH]]
end

ARTIFACT DistillationInterface:
    sutra: "Transition artifacts (Fluid) → validation period → corpus update (Canonical) → propagation to all IICs"
    gloss:
        Transition artifacts are Fluid tier; insights may graduate to Canonical.
        Graduation requires: stable across 3+ sessions, represents framework evolution
        (not task-specific), fills identified gap, aligns with constitutional, principal
        approves. Options: Archive (default), Prune (low value), Merge (consolidate),
        Graduate (move to canonical).
    spec:
        graduation_path:
            1: Transition_Artifact_Fluid
            2: Principal_review
            3: Canonical_Candidate_identified
            4: Validation_period | stable_across_3+_sessions
            5: Corpus_update
            6: Propagation_to_all_IICs
        graduation_criteria:
            - insight_stable_3+_sessions
            - framework_evolution_not_task_specific
            - fills_gap_in_corpus
            - aligns_constitutional
            - principal_approves
        forgetting_interface:
            Archive: default | kept_for_potential_reference
            Prune: no_lasting_value | delete
            Merge: related_transitions | consolidate
            Graduate: insights >> canonical_documents
        hygiene: monthly_review | prune_low_value | consolidate_related
        refs: [[CANON-25000-MEMORY_ARCH]]
end

