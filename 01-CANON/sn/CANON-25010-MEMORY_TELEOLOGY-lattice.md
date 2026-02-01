---
id: [[CANON-25010-MEMORY_TELEOLOGY-lattice]]
name: Memory Architecture Teleological Analysis
tier: lattice
sn_version: 1.0
converted: 2026-01-24
original_words: 4120
sn_words: 1180
compression: 71%
---

# Κ-25010: Memory Teleology (SN)

TERM MemoryProblem:
    sutra: "AI platforms stateless by default—must maintain coherence within platform AND enable handoffs between platforms"
    gloss:
        AI platforms evolved various continuity mechanisms (threads, custom instructions,
        project files, learned facts) but these differ radically in scope, persistence,
        and fidelity. Constellation must solve compound problem: coherent context within
        each platform while enabling seamless handoffs between platforms sharing no
        common memory substrate.
    spec:
        meta_teleology: transform_episodic_platform_interactions >> continuous_cognitive_process
        dual_requirement:
            within_platform: maintain_coherent_context_across_sessions
            between_platforms: enable_seamless_handoffs | no_common_substrate
        refs: [[CANON-25000-MEMORY_ARCH]], [[CANON-25200-CONSTELLATION_ARCH]]
end

TERM ClaudeMemoryLayers:
    sutra: "Global Preferences >> Project Memory >> Conversation >> Past Chats—hierarchical isolation with cross-thread search"
    gloss:
        Claude implements most sophisticated hierarchical memory: Global System Preferences
        (account-level, permanent), Project-Specific Memory (isolated cognitive spaces
        ~200K+ tokens per file), Conversation Memory (ephemeral ~200K tokens), Past
        Conversations (searchable but artifact-blind). Claude Web for thinking, not
        extended execution—thread limits trigger context collapse.
    spec:
        Layer_1_Global_Preferences:
            location: Settings >> Profile >> Custom_Instructions
            scope: all_conversations_all_projects
            persistence: permanent_until_edited
            teleology: baseline_behavioral_parameters_transcending_projects
            belongs: cognitive_profile | anti_patterns | tone_calibration
            NOT_belongs: domain_knowledge | project_context | role_assignments
        Layer_2_Project_Memory:
            location: within_each_Claude_Project
            components: Custom_Instructions | Project_Knowledge | Project_Specific_Memory
            scope: only_within_specific_project
            teleology: bounded_cognitive_spaces_without_cross_contamination
            capacity: 200K+_tokens_per_file | 100+_files
            why_isolation: prevents_context_bleed_from_unrelated_domains
        Layer_3_Conversation:
            scope: current_conversation_only
            budget: ~200K_tokens
            persistence: until_conversation_ends_or_limit_reached
            teleology: working_memory_for_immediate_interaction
            limitation: Claude_Web_most_restrictive_thread_limits
            implication: Claude_for_thinking_not_extended_execution
        Layer_4_Past_Conversations:
            features: conversation_search | recent_chats
            scope: search_retrieve_from_other_conversations
            limitation: CANNOT_see_artifacts_from_past_conversations
            teleology: synthesis_across_sessions_without_manual_transfer
            implication: important_outputs >> Project_Knowledge_or_repository | not_just_artifacts
end

TERM ChatGPTMemoryLayers:
    sutra: "Global Instructions >> Global Memory >> Project Config >> Conversation >> Canvas—passive learning with memory regression risk"
    gloss:
        ChatGPT prioritizes passive learning and long-running threads. Global Memory
        auto-learns facts, creating cross-contamination risk. Critical: memory regression
        in GPT-5.x causes global memory to override project context unpredictably.
        COMPILER must use Project-Only Memory mode. Canvas provides persistent workspace
        superior to Claude artifacts.
    spec:
        Layer_1_Global_Instructions:
            location: Settings >> Personalization >> Custom_Instructions
            fields: what_to_know | how_to_respond
            teleology: baseline_personalization | cruder_than_Claude
        Layer_2_Global_Memory:
            mechanism: auto_learns_facts_from_conversations
            scope: all_conversations_unless_project_restricts
            teleology: cumulative_user_model_without_explicit_instruction
            CRITICAL_PROBLEM: memory_regression_GPT5x_within_Projects
            mitigation: Project_Only_Memory_mode | restricts_to_project_files_and_history
        Layer_3_Project_Config:
            components: Project_Instructions | Project_Files | Memory_Mode_toggle
            capacity: 25-40_files | 512MB_each
            teleology: isolated_workspaces_with_weaker_boundaries_than_Claude
        Layer_4_Conversation:
            budget: 32K-128K_tokens
            behavior: continues_indefinitely_with_progressive_eviction
            teleology: extended_dialogues_beyond_single_session
        Layer_5_Canvas:
            feature: side_by_side_document_code_editor
            persistence: survives_across_sessions
            teleology: iterative_refinement | superior_to_Claude_artifacts_for_persistence
end

TERM GeminiMemoryLayers:
    sutra: "Saved Info >> Personal Intelligence >> Gems >> Conversation >> NotebookLM—explicit preferences + ecosystem integration + 1M context"
    gloss:
        Gemini integrates uniquely with Google ecosystem. Saved Info requires explicit
        instruction (unlike ChatGPT passive learning). Personal Intelligence connects
        Gmail/Drive/Photos. Gems link to live Google Drive files (auto-sync). 1M token
        context enables massive document processing. NotebookLM provides zero-hallucination
        grounded responses.
    spec:
        Layer_1_Saved_Info:
            mechanism: EXPLICIT | "Remember_that_I_prefer..."
            scope: all_conversations_globally
            teleology: explicit_persistent_preferences_with_clearer_control
        Layer_2_Personal_Intelligence:
            feature: Beta_AI_Pro
            connected: Gmail | Drive | Photos | Search | YouTube
            teleology: ground_responses_in_actual_Google_ecosystem_content
            requirement: Google_Sign_in_to_relevant_account
        Layer_3_Gems:
            components: Name | Description | Instructions | Knowledge_Files_10max
            unique: links_to_live_Google_Drive_files
            teleology: purpose_specific_AI_with_dynamic_file_updates
            advantage: make_sync_to_drive >> Gem_sees_automatically | zero_upload_friction
        Layer_4_Conversation:
            budget: 1M_tokens | largest_in_industry
            behavior: virtually_unlimited_thread_length
            teleology: massive_documents_extended_dialogues_no_collapse
        Layer_5_NotebookLM:
            feature: attach_notebooks_to_chats | 50+_sources
            result: zero_hallucination_grounded_with_citations
            teleology: research_grade_synthesis_verifiable_sourcing
end

TERM CLIMemoryLayers:
    sutra: "Gemini CLI: stateless by design (ORACLE freshness). Claude Code: file-based hierarchy (institutional memory)"
    gloss:
        Gemini CLI has essentially no memory—each invocation independent. Statelessness
        is correct for ORACLE: surveys reflect current corpus state, not stale context.
        Claude Code implements sophisticated file-based hierarchy: User Global >> Project
        >> Rules >> Local >> Subdirectory >> Session. "Every mistake becomes a rule"
        in CLAUDE.md—compounding institutional memory.
    spec:
        Gemini_CLI:
            Layer_1: local_config | API_keys_model_preferences
            Layer_2: invocation_context | per_command_only
            Layer_3: NO_persistent_memory
            teleology: stateless_ensures_freshness | ORACLE_sees_current_corpus_only
            design_rationale: if_remembered_previous_surveys >> stale_findings
        Claude_Code:
            Layer_1_User_Global: ~/.claude/CLAUDE.md | all_projects_unless_overridden
            Layer_2_Project: ./CLAUDE.md_or_.claude/CLAUDE.md | git_tracked | institutional_memory
            Layer_3_Rules: .claude/rules/*.md | conditional_on_file_paths
            Layer_4_Local: ./CLAUDE.local.md | personal_notes | gitignored
            Layer_5_Subdirectory: nested_CLAUDE.md | progressively_refined_context
            Layer_6_Session: ephemeral | lost_when_session_ends
            Layer_7_Teleport: Web_Terminal_bridge | session_transfers_intact
            compounding_philosophy: every_mistake_becomes_a_rule >> CLAUDE.md_accumulates_tribal_knowledge
end

TERM SurfaceMemoryBehavior:
    sutra: "Web = richest configuration. Desktop = persistent sessions. CLI = scriptable/sovereign. Mobile = capture only."
    gloss:
        Surfaces have characteristic memory behavior: Web Browser (full feature set,
        where configuration happens), Desktop App (session persistence across restarts),
        CLI (file-based, scriptable, reproducible), Mobile (capture and review, cannot
        create new memory structures).
    spec:
        Web_Browser:
            platforms: Claude_Web | ChatGPT_Web | Gemini_Web | Grok_Web | Perplexity_Web
            characteristics: full_feature_access | projects | past_chat_search | Canvas | Gems
            teleology: richest_interface_for_configuration_and_ideation
            role: where_memory_is_created | other_surfaces_consume
        Desktop_App:
            platforms: Claude_Desktop | ChatGPT_Desktop | Perplexity_Desktop
            characteristics: session_persistence_across_restarts | native_performance | reduced_features
            teleology: stable_persistent_sessions_without_browser_overhead
            lacks: Claude_Desktop_no_past_chat_search | ChatGPT_Desktop_limited_Canvas
        CLI:
            platforms: Claude_Code | Codex_CLI | Gemini_CLI
            characteristics: file_based_config | stateless_invocation | no_cross_session_memory
            teleology: scriptable_automatable_AI_with_explicit_context
            why_file_based_fits_execution: reproducibility | same_command_same_context_same_result
            why_stateless_fits_sensing: survey_reflects_current_state_not_accumulated_stale
        Mobile:
            platforms: Claude_Mobile | ChatGPT_Mobile | Gemini_Mobile | Grok_Mobile | Perplexity_Mobile
            characteristics: reduced_features | no_project_creation | consumption_oriented
            teleology: capture_and_review | not_full_configuration
            can: access_projects_created_on_Web | continue_conversations
            cannot: create_new_Projects_Gems | complex_configuration
end

ARTIFACT ForbiddenPatterns:
    sutra: "Don't rely on: ChatGPT global memory for projects, cross-Gem memory, CLI remembering invocations, Claude threads as long-term, mobile for config"
    gloss:
        Memory anti-patterns: ChatGPT global memory regresses in Projects (use Project-Only
        mode), Gems are isolated (no cross-Gem transfer), Gemini CLI is stateless
        (provide full context every time), Claude threads collapse (capture to Project
        Knowledge), mobile can't configure (Web required).
    spec:
        forbidden:
            - ChatGPT_global_memory_for_project_work: regression_causes_override | use_Project_Only_mode
            - cross_Gem_memory: Gems_isolated_personas | no_transfer_between
            - Gemini_CLI_remembering: stateless | provide_full_context_every_time
            - Claude_Web_threads_as_long_term: collapse_limits | capture_to_Project_Knowledge_or_repo
            - mobile_for_memory_config: creates_consume_only | Web_required_for_new_structures
            - Perplexity_Grok_remembering: no_persistent_config | every_query_fresh
        unified_rationale:
            Personalization: shape_AI_to_cognitive_style | Global_instructions_profiles
            Contextualization: domain_knowledge_for_task | Project_Knowledge_Gems_CLAUDE.md
            Continuity: coherent_state_across_sessions_platforms | past_chat_fingerprints_repository
        refs: [[CANON-25000-MEMORY_ARCH]], [[CANON-25200-CONSTELLATION_ARCH]]
end

