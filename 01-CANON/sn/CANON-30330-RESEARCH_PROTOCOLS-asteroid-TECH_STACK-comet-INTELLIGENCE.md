---
id: [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
name: Research Protocols
tier: asteroid
chain: INTELLIGENCE
parent: [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
sn_version: 1.0
converted: 2026-01-24
original_words: 1897
sn_words: 360
compression: 81%
---

# Κ-30330: Research Protocols (SN)

TERM ResearchProtocols:
    sutra: "Source triad + verdicting—decision-bearing questions first, few high-confidence > many unvalidated"
    gloss:
        Methodologies and quality standards for AI-augmented research. Every research
        question produces verdicts with confidence, recency, volatility, and design deltas.
    spec:
        identity: RESEARCH_PROTOCOLS
        goal: better_decisions_faster_knowing_what's_true_uncertain_changing_actionable
end

PROC SourceTriadMethod:
    sutra: "Primary → Expert Analysis → Counter-Position for every decision-bearing question"
    spec:
        pass1_primary:
            targets: academic_papers | official_docs | engineering_blogs | government_reports | patents
            evaluate: is_original | institution_credibility | recency | methodology
            red_flags: secondary_without_primary | marketing_as_research | claims_without_evidence
        pass2_secondary:
            targets: technical_deep_dives | research_reviews | industry_analysis | expert_commentary
            evaluate: adds_interpretation | analyst_expertise | rigor_vs_speculation | non_obvious_revealed
            red_flags: hype | cherry_picking | undisclosed_conflicts | extrapolation_beyond_evidence
        pass3_counter:
            targets: academic_rebuttals | skeptical_analyses | limitations | competing_approaches
            evaluate: genuine_limitations | assumptions_that_fail | alternative_explanations | failure_modes
            red_flags: strawman | dismissal_without_engagement | ideological_opposition
end

NORM DecisionBearingFirst:
    sutra: "What decision? What if X vs Y? What confidence to act? Cost of being wrong?"
    spec:
        research_when: answer_materially_changes | uncertainty_blocks_action | time_justified
        skip_when: no_decision_impact | uncertainty_acceptable | other_info_more_critical
end

PASS VerdictingProcess:
    sutra: "Claim + Confidence + Recency + Volatility + Design Delta"
    spec:
        claim: clear_testable_statement
        confidence:
            high_85+: multiple_primary | expert_consensus | replicated
            medium_50-85: primary + analysis | plausible_inconclusive
            low_sub50: single_report | unverified | speculative
            speculative_sub25: rumor | prediction | no_evidence
        recency:
            current_0-3mo: likely_accurate
            recent_3-12mo: worth_checking
            dated_1-2yr: may_have_changed
            stale_2yr+: use_with_caution
        volatility:
            stable: unlikely_to_change (fundamental)
            shifting: actively_evolving (capabilities)
            speculative: not_yet_real (predictions)
        design_delta: "If true, we should [specific_action]"
end

NORM ResearchAntiPatterns:
    sutra: "No benchmark shopping, link dumping, hype amplification, recency bias, confirmation bias"
    spec:
        benchmark_shopping: selectively_citing >> include_context_cite_competing_note_unmeasured
        link_dumping: many_without_synthesis >> few_well_analyzed
        hype_amplification: repeating_marketing >> distinguish_claims_from_evidence
        recency_bias: newer_always_better >> assess_volatility_value_timeless
        confirmation_bias: seeking_supporting >> actively_seek_counter_always_pass3
end

PASS FrontierTracking:
    sutra: "Weekly ArXiv, monthly depth, quarterly landscape"
    spec:
        weekly: lab_blogs | ArXiv_cs.AI | HN | subreddits
        monthly: 3-5_papers_deep | major_releases | frontier_map_update | prediction_reassess
        quarterly: comprehensive_landscape | paradigm_shifts | taxonomy_update | framework_revision
        targets:
            academic: Stanford_HAI | MIT_CSAIL | Berkeley_BAIR | CMU_ML | Oxford_Cambridge
            labs: Anthropic | OpenAI | DeepMind | Meta_AI | xAI
            mission: CAIS | AI_Alignment_Forum | FHI
            commercial: Cursor | Replit | Perplexity | Palantir | Anduril
end

PROC InfrastructureEvaluation:
    sutra: "Vendor docs, third-party benchmarks, limitations and alternatives"
    spec:
        source_triad:
            pass1: vendor_docs | benchmarks | pricing | SLAs | certs
            pass2: third_party_benchmarks | case_studies | technical_reviews
            pass3: known_limitations | complaints | alternatives | exit_feasibility
        dimensions:
            technical: latency_p50_p95_p99 | throughput | reliability | quality | scalability
            business: funding | market_position | strategic_risk | pricing_stability | support
            governance: security_certs | privacy | compliance | audit | incident_response
            lock_in: data_portability | API_compatibility | feature_dependency | migration_cost
        capability_contract:
            - performance_SLOs_documented
            - data_governance (residency | retention | deletion)
            - provenance (trace_outputs_to_sources)
            - exit_strategy (migration_path | transition_support)
            - cost_accounting (transparent_pricing)
        decision_framework: Data_Sensitivity × Latency × Economic_Leverage × Lock_in >> OWN | LEASE | HYBRID
end

PROC CapabilityAudit:
    sutra: "Monthly metrics, quarterly full review, annual reassessment"
    spec:
        monthly: performance_metrics | cost_vs_budget | incident_scan | degradation_trends
        quarterly: full_contract_review | vendor_health | alternatives | renegotiate
        annual: own_vs_lease_reassessment | landscape_analysis | migration_consideration
        classification:
            green: all_met | stable | expected_cost | no_risks
            yellow: borderline | minor_degradation | creeping_cost >> monitor_closely
            red: critical_violations | significant_issues | overruns >> action_required
end

TEST QualityChecklist:
    sutra: "Source, confidence, design delta—every claim attributed, every output actionable"
    spec:
        - every_claim_has_source
        - sources_primary_when_possible
        - secondary_adds_analysis
        - counter_positions_included
        - confidence_explicit_with_rationale
        - recency_volatility_tagged
        - design_deltas_specified
        - contradictions_acknowledged
        - no_benchmark_shopping_or_link_dumping
        - hype_distinguished_from_evidence
end
