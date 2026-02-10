---
id: [[CANON-30460-INTERACTION_DYNAMICS-comet]]
name: Interaction Dynamics
tier: comet
chain: INTELLIGENCE
sn_version: 1.0
converted: 2026-01-24
original_words: 6244
sn_words: 900
compression: 86%
---

# Κ-30460: Interaction Dynamics (SN)

TERM InteractionDynamics:
    sutra: "Constellation operates as state machine—platforms transform, repository records ground truth"
    gloss:
        Operational configuration for Ψ constellation. Each platform executes
        transformations; handoff tokens carry state; repository commits ground truth.
    spec:
        identity: INTERACTION_DYNAMICS
        purpose: collapse_tentative_architecture >> operational_configuration
end

PASS StateDefinitions:
    sutra: "CAPTURED → INTERPRETED → COMPILED/DIGESTED/SENSED → STAGED → COMMITTED"
    spec:
        CAPTURED: Principal_mind | external_source | unstructured_ephemeral >> INTERPRETED
        INTERPRETED: Claude_Web_artifact | structured_understanding >> COMPILED | DIGESTED | SENSED
        COMPILED: ChatGPT_Canvas | formatted_artifact >> STAGED
        DIGESTED: Gemini_export_Docs | clarified_summary >> INTERPRETED | STAGED
        SENSED: Gemini_CLI_output | evidence_pack >> INTERPRETED
        VERIFIED: Perplexity_Grok_output | externally_validated >> INTERPRETED
        STAGED: -OUTGOING/ | ready_for_commit >> COMMITTED
        COMMITTED: Repository (git) | ground_truth | Terminal
end

PASS MultiRoundPatterns:
    sutra: "Convergent same-platform, oscillating cross-platform, triangulated parallel, sensing CLI-loop"
    spec:
        pattern_A_convergent:
            mechanism: thread_continuity_within_platform
            limitation: ~10-15_heavy_exchanges >> context_eviction
            mitigation: /compact_at_70% | capture_before_compact
        pattern_B_oscillating:
            mechanism: handoff_tokens_carry_state_fingerprint + delta
            limitation: manual_copy_paste
            mitigation: standardized_token_format | clipboard_automation
        pattern_C_triangulated:
            structure: Claude (hub) >> Gemini (digest) + Perplexity (facts) + Grok (social) >> Claude (synthesize)
            limitation: manual_parallel_management
            mitigation: split_screen | batch_queries
        pattern_D_sensing:
            structure: Gemini_CLI (survey) >> Claude_Web (interpret) >> Claude_Code (implement) >> Gemini_CLI (verify)
            mechanism: file_based_handoff >> -OUTGOING/
            limitation: CLI_stateless
            mitigation: external_state_via_scripts
end

PASS PredictabilityAccuracyTradeoff:
    sutra: "Strict for mechanical, guided for structured, open for creative"
    spec:
        tiers:
            strict: complete_template + constraints | mechanical_transformation
            guided: output_structure + quality_criteria | structured_creation
            open: goal + constraints_only | creative_synthesis
        platform_mapping:
            Claude_Web: open_or_guided (interpretation_benefits_from_latitude)
            ChatGPT_Web: strict (compilation_requires_determinism)
            Gemini_Web: guided (digestion_needs_structure_not_rigidity)
            Gemini_CLI: strict (sensing_must_be_reproducible)
            Grok: open (red_teaming_benefits_from_unpredictability)
            Perplexity: guided (verification_needs_focus_allows_exploration)
        mechanisms: templates | checklists | verification_hashes | constraint_lists
end

PASS PlatformLimitations:
    sutra: "Claude threads, ChatGPT memory, Gemini Gem files, CLI stateless—each has workarounds"
    spec:
        Claude_Web:
            limitations: ~45_Pro/5hr | artifacts_not_searchable | no_Drive_connector | shared_rate_limits
            overcome: focused_1-3hr_sessions | capture_immediately | don't_rely_on_old_threads
        ChatGPT_Web:
            limitations: memory_regression_in_Projects | weak_ambiguity | no_thread_search
            overcome: PROJECT_ONLY_mode | ultra_explicit_specs | self_contained_handoffs
        Gemini_Web:
            limitations: no_cross_Gem_memory | context_drift | 10_file_Gem_limit | export_friction
            overcome: one_Gem_per_session | periodic_summary_anchors | Drive_links
        Gemini_CLI:
            limitations: completely_stateless | no_continuation | stdout_output
            overcome: embrace_statelessness | external_state_scripts | redirect_to_files
        Grok:
            limitations: no_persistent_config | X_only_data | no_projects
            overcome: single_query | capture_immediately | use_for_X_Firehose_only
        Perplexity:
            limitations: no_persistent_config | citation_optimized_not_synthesis | limited_API
            overcome: discrete_verification_only | extract_citations >> Claude
end

PASS CrossPlatformPorting:
    sutra: "Claude→ChatGPT 45s, ChatGPT→Gemini 60s, Claude→CLI 30s—handoff token verifies"
    spec:
        Claude_to_ChatGPT:
            payload: specification + template + constraints + fingerprint
            process: produce_artifact >> download >> paste >> "Compile, do not interpret, ASK if ambiguous" >> download_Canvas
            time: ~45s
        ChatGPT_to_Gemini:
            payload: artifact + digest_goal + audience + format + length
            process: export_Canvas >> upload_or_sync_Drive >> invoke_Digestor_Gem >> export_Docs
            time: ~60s
        Claude_to_CLI:
            payload: NL_query_in_shell_command
            process: construct_command >> execute >> redirect_to_-OUTGOING/ >> paste_evidence
            time: ~30s
        Gemini_to_Claude:
            payload: digest + original_goal + integration_need
            process: copy_from_Docs >> paste_with_framing
            time: ~20s
end

PASS AutomationPathways:
    sutra: "rclone+Make state broadcast, CLI wrapper scripts, Alfred clipboard, git hooks"
    spec:
        state_broadcast (rclone + Make):
            purpose: sync_repository_state_to_all_platforms
            targets: generate_token | sync_drive | sync_all
            result: token_to_clipboard >> paste_into_platform
        CLI_wrappers:
            purpose: standardized_corpus_sensing
            scripts: corpus-survey.sh | evidence-pack.sh
            output: YAML_evidence_pack >> -OUTGOING/
        clipboard_automation (Alfred/Raycast):
            purpose: one_keystroke_handoff
            workflows: ⌘⇧H (get_token) | ⌘⇧N (new_handoff)
        git_hooks:
            purpose: automatic_state_capture
            hook: post-commit >> update_fingerprint >> sync_Drive
end

PASS PlatformConfigurations:
    sutra: "Claude Project, ChatGPT Project-Only, Gemini Gem+Drive, CLI wrapper scripts"
    spec:
        claude_web:
            role: INTERPRETER
            project: "Syncrescendence IIC"
            knowledge: [COCKPIT.md, frontier_models, platform_features, teleology_docs]
            memory: project_specific
            connectors: [github, gdrive, gmail]
        chatgpt_web:
            role: COMPILER
            project: "Syncrescendence Compiler"
            memory_mode: PROJECT_ONLY (CRITICAL)
            files: [handoff_token_template, compile_templates]
        gemini_web:
            role: DIGESTOR
            gem: "Constellation Digestor"
            drive_folder: Constellation-State/ (rclone_synced)
            personal_intelligence: enabled
        gemini_cli:
            role: ORACLE
            model: gemini-2.0-flash (default) | gemini-2.0-pro (complex)
            max_tokens: 1M
            state: external_via_scripts
        claude_code:
            role: EXECUTOR
            surfaces: [EXECUTOR-LEAD (Air, Opus), PARALLEL-A (mini, Sonnet), PARALLEL-B (mini, Sonnet)]
            thinking: auto-enabled (keywords cosmetic, budget managed by runtime)
        grok: role: RED_TEAM | stateless | X_Firehose
        perplexity: role: VERIFIER | stateless | citations
end

PASS RelationshipMatrix:
    sutra: "Memory layers map to platform capabilities, roles to functions, dynamics to protocols"
    spec:
        memory_layer_mapping:
            Constitutional: system_prompts (Claude | ChatGPT | Gemini)
            Global: settings (User_Prefs | Custom_Instructions | Saved_Info)
            Accumulated: auto_memory (Claude_yes | ChatGPT_DISABLED | Gemini_no)
            Project: knowledge_instructions (all_platforms)
            Session: thread_context (Claude_200K | ChatGPT_32-128K | Gemini_1M)
            Cross_Thread: Claude_search | others_none | CLI_filesystem
            Live_Sync: Claude_GitHub | Gemini_Drive | CLI_filesystem
        role_capability_matrix:
            INTERPRETER: rapport★★★★★ | deterministic★★★ | long_context★★ | memory★★★★★
            COMPILER: rapport★ | deterministic★★★★★ | long_context★★★ | memory★
            DIGESTOR: rapport★★★ | deterministic★★★ | long_context★★★★★ | memory★★★
            ORACLE: deterministic★★★★★ | long_context★★★★★ | filesystem★★★★★
            EXECUTOR: deterministic★★★★ | memory★★★★ | filesystem★★★★★ | automation★★★★★
end

PROC ExecutionDirective:
    sutra: "Claude Code creates files, Principal configures web apps—hybrid approach"
    spec:
        claude_code_CAN:
            - create .constellation/ infrastructure
            - generate Makefile + wrapper_scripts
            - create git_hooks
            - generate template_content_for_copy_paste
        principal_MUST:
            - configure_web_app_projects_via_UI
            - run rclone_config (OAuth)
            - test_each_platform
            - verify_cross_platform_handoffs
        phases:
            phase1_infrastructure: directive >> Claude_Code >> .constellation | Makefile | scripts | templates
            phase2_configuration: manual >> each_web_app | rclone_OAuth | ~75min
            phase3_validation: hybrid >> scripts_generate | Principal_executes_cross_platform
end

TEST ValidationSequence:
    sutra: "Generate token, Claude verifies, ChatGPT compiles, Gemini sees Drive, cycle complete"
    spec:
        steps:
            1. git_commit >> make_sync_all PHASE=0
            2. paste >> Claude >> verify_fingerprint_state
            3. make_sync_all PHASE=1 >> paste >> ChatGPT >> compile_without_interpretation
            4. Gemini_Gem >> process_active_token_from_Drive
            5. download_to_-OUTGOING/ >> commit >> make_generate_token
        success_criteria:
            - handoff_time < 30s_per_transition
            - no_re_explanation_required
            - fingerprints_match_throughout
end
