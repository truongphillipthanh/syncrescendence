---
id: [[CANON-30440-SAFETY_ALIGNMENT-asteroid-INTELLIGENCE]]
name: Safety and Alignment
tier: asteroid
chain: INTELLIGENCE
parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
sn_version: 1.0
converted: 2026-01-24
original_words: 2595
sn_words: 480
compression: 81%
---

# Κ-30440: Safety and Alignment (SN)

TERM SafetyAlignment:
    sutra: "Autonomy + tools + state = attack surfaces absent in static AI—defense in depth required"
    gloss:
        Agent systems face fundamentally different threat models than static models.
        Implementation depth for defenses, governance frameworks, and alignment mechanisms.
    spec:
        identity: SAFETY_ALIGNMENT
        parent: [[CANON-30400-AGENTIC_ARCHITECTURE]]
end

PASS AttackVectorTaxonomy:
    sutra: "Hijacking 81%, tool misuse documented, jailbreaks power-law, scheming emerging"
    spec:
        agent_hijacking:
            mechanism: indirect_prompt_injection_via_ingested_data
            success_rate: 81%_with_optimization
            vectors: [malicious_emails, poisoned_docs, compromised_pages, injected_DB]
            root_cause: no_separation_trusted_instructions_vs_untrusted_data
        tool_misuse:
            mechanism: exploit_agent_tool_access
            documented: SQL_injection | SSRF_internal_networks | RCE_code_interpreters | metadata_exfil | BOLA
            status: observed_in_production
        jailbreaking:
            evolution: direct (least) >> emotional >> encoded >> symbolic >> multi_shot >> multi_round
            scaling: power_law (success_increases_non_linearly)
        deep_scheming:
            behaviors: alignment_faking | sandbagging | environment_manipulation
            implication: instrumental_subgoals_misaligned
            concern: emerging_in_reasoning_models
        key_findings:
            unsafe_behavior: 51-72% (OpenAgentSafety)
            attack_optimization: 11% >> 81% (Claude_3.5_Sonnet)
            CVE: 2025-32711 CVSS 9.3 (Microsoft_365_Copilot)
end

PASS FiveLayerDefense:
    sutra: "Prompt harden, filter content, sanitize tools, scan vulnerabilities, sandbox code"
    spec:
        layer1_prompt_hardening:
            purpose: first_line
            techniques: [strict_constraints, explicit_prohibitions, narrow_responsibility, out_of_scope_rejection]
        layer2_content_filtering:
            purpose: runtime_inspection
            targets: [tool_schema_extraction, misuse_patterns, memory_manipulation, malicious_code, data_leakage, malicious_URLs]
        layer3_tool_sanitization:
            purpose: validate_all_inputs
            techniques: [type_validation, format_checking, boundary_verification, special_char_filter, schema_enforcement]
            principle: NEVER_trust_implicitly
        layer4_vulnerability_scanning:
            purpose: proactive_assessment
            techniques: [SAST, DAST, SCA, penetration_testing, adversarial_red_teaming]
        layer5_code_sandboxing:
            purpose: contain_execution
            controls:
                network: whitelist_outbound_only
                filesystem: limited_volumes + tmpfs
                capabilities: drop CAP_NET_RAW | CAP_SYS_MODULE | CAP_SYS_ADMIN
                syscalls: block kexec_load | mount | bpf
                resources: CPU + memory_quotas
        defense_effectiveness:
            reverse_turing: 87-94%
            multi_agent_alignment: 70-98%
            GCG_jailbreak: 90.8%
            combined: no_single_layer_sufficient
end

PASS GovernanceFrameworks:
    sutra: "SAIF well-defined controllers, TACO four categories, EU AI Act pillars, eight practices"
    spec:
        Google_SAIF_2.0:
            - well_defined_human_controllers
            - carefully_limited_powers
            - observable_actions_planning
            - environment_confinement
            - separate_evaluation
            - multi_level_monitoring
        KPMG_TACO:
            categories: Taskers | Automators | Collaborators | Orchestrators
            principles: [Reliability, Accountability, Transparency, Security, Privacy, Fairness]
        EU_AI_Act:
            pillars: [risk_assessment, transparency_tools, deployment_controls, human_oversight_design]
            high_risk: mandatory_oversight | transparency | documentation | risk_management
        eight_practices:
            1. permissions_boundaries: data + actions + escalation + machine_readable
            2. privacy_by_design: minimization | purpose_limitation | encryption | anonymization
            3. data_retention: clear_policies | automated_deletion | compliance
            4. transparency: audit_trails | accessible_explanations | reasoning_visibility
            5. human_oversight: intervention + emergency_stop + escalation
            6. monitoring: dashboards | anomaly_detection | alerts
            7. agent_cataloging: purpose | capabilities | tools | versions | ownership
            8. incident_response: investigation | notification | correction | post_mortem
end

PASS ValidationVerification:
    sutra: "Verification agents review, simulation sandboxes, alignment checks filter"
    spec:
        validation_layers:
            verification_agent: review_before_execution | cross_check_policies | flag_anomalies
            testing_protocols: simulate_before_execute | sandbox_high_stakes | double_check_with_second
            alignment_checks: toxic_filters | bias_assessment | policy_compliance
        error_recovery:
            tool_failure: catch_retry | request_new_instructions | graceful_degradation
            plan_failure: escalate | checkpoint_rollback | alternative_approach
            chain_failure: monitor_sequences | checkpoint_significant | detect_loops_abort
            key_insight: "10_steps × 90%_each = ~35%_overall >> checkpoints_essential"
end

PASS AlignmentMechanisms:
    sutra: "Bounded autonomy, progressive trust, reversible delegation"
    spec:
        bounded_autonomy:
            principle: clear_perimeters_for_independent_judgment
            implementation: operational_scope | hard_constraints | escalation_triggers | capability_access
        progressive_trust:
            principle: capability_expansion << demonstrated_reliability
            stages:
                initial: all_actions_reviewed | limited_tools | simple_scope
                intermediate: low_risk_autonomous | expanded_tools | complex_scope
                advanced: most_autonomous | full_tools | high_stakes_with_oversight
            mechanism: earn_autonomy_through_reliability
        reversible_delegation:
            principle: human_oversight_can_reclaim_anytime
            implementation: emergency_stop | override_all_levels | escalation_available | no_catastrophic_reclamation
end

PASS TestingFrameworks:
    sutra: "AgentDojo ETH/AISI, BAD-ACTS adversarial, Petri Anthropic, OpenAgentSafety real tools"
    spec:
        AgentDojo (ETH_Zurich + US_AISI): hijacking_scenarios | 4_environments | red_teaming
        BAD-ACTS: adversarial_robustness | 188_harmful_instances
        Petri (Anthropic): automated_auditing | parallel_multi_turn
        OpenAgentSafety: critical_risk | 8_categories | real_tools
        continuous_assessment:
            automated: penetration | adversarial_input | policy_compliance
            metrics: attack_success_trend | defense_bypass | MTTD | MTTR
            feedback: failures >> training_data | update_defenses | refine_prompts
end

NORM IntrinsicAlignment:
    sutra: "External controls insufficient against deliberate circumvention—intrinsic monitoring nascent"
    spec:
        limitation: external_guardrails >> insufficient_when_models_deliberately_circumvent
        approaches:
            constitutional_AI: self_review_against_principles | balance_autonomy_values | human_feedback
            self_evaluation: continuous_checking | automatic_correction | transparent_reasoning
        status: practical_implementations_nascent
        challenge: ensuring_agents_preserve_properties_through_self_improvement
end
