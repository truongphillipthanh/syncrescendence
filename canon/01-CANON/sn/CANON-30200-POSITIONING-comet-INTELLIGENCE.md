---
id: [[CANON-30200-POSITIONING-comet-INTELLIGENCE]]
name: Strategic Positioning
tier: comet
chain: INTELLIGENCE
parent: [[CANON-30000-INTELLIGENCE-chain]]
sn_version: 1.0
converted: 2026-01-24
original_words: 5316
sn_words: 820
compression: 85%
---

# Κ-30200: Strategic Positioning (SN)

TERM StrategicPositioning:
    sutra: "Technology embodies values—navigate ecosystems knowing corporate objectives"
    gloss:
        Institutional intelligence framework for understanding corporate personalities,
        platform strategies, and tool selection implications. Tools aren't neutral;
        savvy navigation requires understanding institutional incentives.
    spec:
        identity: Strategic Positioning Supplement
        purpose: rational_tool_selection | platform_strategy | risk_assessment | workflow_design
        quarterly_update: corporate_landscapes_shift_rapidly
end

PASS AnalyticalDimensions:
    sutra: "Six lenses: coherence, business model, innovation, control, lock-in, trust"
    spec:
        coherence_philosophy:
            integration_maximalist: vertical_closed (Apple)
            interoperability_pragmatist: open_with_proprietary (Google)
            platform_neutral: operates_across_ecosystems (Microsoft, Adobe)
        business_model:
            hardware_sales: device_premium (Apple)
            advertising: attention_extraction (Google, Meta)
            subscriptions: recurring_revenue (Microsoft, Adobe)
            enterprise_services: B2B_stability (AWS, Salesforce)
            API_usage: pay_per_use (OpenAI, Anthropic)
        innovation_posture:
            conservative_refinement: iterate_proven (Apple)
            experimental_abundance: ship_early_iterate_fast (Google)
            adaptive_following: let_others_pioneer_execute_better (Microsoft)
            fundamental_research: long_term_capability (Anthropic, DeepMind)
        user_control:
            benevolent_dictatorship: "we know best" (Apple)
            algorithmic_mediation: ML_curates_experience (Google, Meta)
            power_user_empowerment: tools_for_sophisticated (Microsoft)
            constitutional_respect: user_sovereignty_as_principle (rare)
        lock_in_strategy:
            ecosystem_capture: deep_integration (Apple)
            data_gravity: content_trapped (Meta, Google)
            format_standardization: open_formats (Markdown, Linux)
            skill_investment: learning_curve_as_moat (Adobe)
        trust_relationship:
            benign_neglect: pro_user_until_monetization
            extractive_optimization: user_secondary_to_metrics
            contractual_clarity: explicit_value_exchange
            adversarial: user_interests_opposed
end

PASS CorporateProfiles:
    sutra: "Apple benevolent dictator, Google algorithmic, Meta extractive, Anthropic cautious"
    spec:
        Apple:
            personality: benevolent_design_dictatorship
            coherence: integration_maximalist
            business: hardware + services_expansion
            lock_in: ecosystem_capture (HIGH_risk)
            trust: generally_benign | privacy_differentiator
            tool_selection: use_when_integration_valuable | maintain_export_paths
        Google:
            personality: algorithmic_abundance_through_advertising
            coherence: interoperability_pragmatist
            business: advertising_dominance (user_is_product)
            lock_in: data_gravity (MEDIUM_risk)
            trust: extractive_optimization | "don't be evil" retired
            tool_selection: use_for_collaboration | assume_products_can_be_killed | backup_essential
        Microsoft:
            personality: adaptive_pragmatist
            coherence: platform_neutral (post_Nadella)
            business: enterprise_subscriptions + cloud
            lock_in: skill_investment + format_dominance (MEDIUM)
            trust: rehabilitated_but_mercenary
            tool_selection: M365_for_enterprise | VSCode_excellent | GitHub_essential
        Meta:
            personality: extractive_attention_maximizer
            coherence: algorithmic_mediation_dominance
            business: advertising_extraction (user_interests_opposed)
            lock_in: social_graph_capture (VERY_HIGH)
            trust: openly_adversarial | documented_harm
            tool_selection: AVOID_where_possible | minimize_if_unavoidable
        OpenAI:
            personality: commercialized_research_lab
            coherence: API_first_ecosystem
            lock_in: ecosystem_dependency (MEDIUM)
            trust: opaque_and_evolving | safety_secondary_to_deployment
            tool_selection: use_for_cutting_edge | diversify_dependencies
        Anthropic:
            personality: constitutional_AI_research_lab
            coherence: safety_first_development
            lock_in: quality_and_alignment (LOW)
            trust: cautiously_optimistic | safety_appears_genuine
            tool_selection: use_when_alignment_matters | lower_switching_risk
        X_Twitter:
            personality: chaotic_transformation_under_Musk
            lock_in: social_graph + cultural_gravity (HIGH)
            trust: deteriorated | misinformation_amplified
            tool_selection: use_tactically | don't_build_critical | export_followers
        TikTok:
            personality: algorithmic_engagement_optimizer
            lock_in: attention_capture (MEDIUM)
            trust: extractive + geopolitical_risk
            tool_selection: AVOID_for_knowledge_work | extreme_addiction_potential
end

PASS PlatformEvolutionPatterns:
    sutra: "Enshittification cycle inevitable—build platform-independent before phase 3"
    spec:
        enshittification_cycle:
            phase1: user_acquisition (generous | network_effects)
            phase2: business_acquisition (monetization | organic_reach_declines)
            phase3: shareholder_extraction (experience_degrades | hostile)
            defense: recognize_early | build_platform_independent | diversify | never_depend_solely
        commoditization_escape:
            sequence: infrastructure_commodity >> proprietary_features >> lock_in >> price_increase
            defense: use_open_standards | maintain_fallbacks | accept_lock_in_only_when_strategic
        acquisition_integration:
            sequence: independent_thrives >> acquisition >> integration >> user_fear
            examples: GitHub_improved | Instagram_degraded | Minecraft_neutral
            defense: assess_incentives | maintain_exports | wait_6-12mo | prepare_alternative
end

PASS LockInAssessment:
    sutra: "Score 5 dimensions, multiply relationships by 2—social lock-in most powerful"
    spec:
        dimensions:
            data_migration: low_1 (open_formats) >> high_5 (no_export)
            relationship_dependency: low_1 (personal) >> high_5 (public_audience) × 2
            workflow_integration: low_1 (standalone) >> high_5 (deep_integration)
            skill_investment: low_1 (minimal) >> high_5 (years_development)
            format_obsolescence: low_1 (universal) >> high_5 (platform_specific)
        scoring:
            max: 30
            low: 0-10 (acceptable_dependency)
            medium: 11-20 (maintain_exit_paths)
            high: 21-30 (minimize_reliance)
        examples:
            Instagram: 21 (HIGH)
            Notion: 15 (MEDIUM)
            Obsidian: 8 (LOW)
            Adobe: 15 (MEDIUM)
end

NORM ToolAdoptionCriteria:
    sutra: "Sovereignty, sustainability, effectiveness, integrity—four tests before adoption"
    spec:
        sovereignty_test:
            - export_in_open_format
            - migrate_to_alternative
            - control_content_distribution
            - own_IP
        sustainability_test:
            - business_model_aligned
            - financially_stable_or_open_source
            - track_record_respecting_users
            - exit_strategy_if_fails
        effectiveness_test:
            - genuine_productivity_increase
            - better_than_alternatives
            - smooth_integration
            - learning_curve_justified
        integrity_test:
            - ethical_business_practices
            - privacy_respected
            - user_wellbeing_considered
            - social_impact_acceptable
        decision:
            all_four: adopt_with_confidence
            three: adopt_with_monitoring
            two: adopt_tactically_with_exit_plan
            one_or_zero: avoid_or_minimize
end

NORM WorkflowArchitecture:
    sutra: "Data over tools, diversification over optimization, independence over integration"
    spec:
        data_over_tools:
            - own_data_in_portable_formats
            - tools_interchangeable_if_data_free
            - plain_text_markdown_csv_when_possible
        diversification_over_optimization:
            - multi_platform_presence
            - multi_tool_workflow
            - redundancy_is_resilience
        independence_over_integration:
            - deep_integration_creates_dependency
            - loose_coupling_enables_substitution
            - automation_only_after_stability
        reversibility_over_commitment:
            - prefer_low_switching_costs
            - test_before_migration
            - maintain_parallel_systems
            - never_burn_bridges
        simplicity_over_features:
            - more_features = more_lock_in
            - use_subset_of_features
            - prefer_specialized_tools
end

PASS PlatformPortfolio:
    sutra: "Tier 1 owned, Tier 2 high-trust, Tier 3 tactical, Tier 4 opportunistic"
    spec:
        tier1_owned (max_sovereignty):
            - personal_blog (WordPress | Ghost | static)
            - email_list (ConvertKit | Mailchimp)
            - personal_domain
        tier2_high_trust (aligned_models):
            - Substack (subscription_based)
            - Discord (user_control_no_algorithm)
            - YouTube (stable_creator_friendly)
        tier3_tactical (strategic_necessity):
            - X_Twitter (declining_but_relevant)
            - LinkedIn (monopoly_requires_presence)
        tier4_opportunistic (limited_use):
            - Instagram (extractive_but_network_strong)
            - TikTok (geopolitical_risk)
            - Facebook (declining_relevance)
        flow:
            create: owned_infrastructure
            distribute: high_trust_platforms
            amplify: tactical_platforms
            repurpose: opportunistic (only_if_justified)
end

TEST QuarterlyReview:
    sutra: "Corporate developments, platform evolution, personal stack, strategic positioning"
    spec:
        corporate_developments:
            - acquisitions_mergers
            - business_model_changes
            - leadership_changes
            - regulatory_developments
        platform_evolution:
            - enshittification_phase_changes
            - new_platforms_emerging
            - API_export_capability_changes
            - ToS_affecting_user_rights
        personal_stack:
            - high_risk_tools_in_critical_workflows
            - lock_in_increasing
            - alternatives_viable
            - export_paths_tested
        strategic_positioning:
            - tier1_stable
            - tier2_still_high_trust
            - tier3_tactical_justified
            - tier4_worth_effort
end
