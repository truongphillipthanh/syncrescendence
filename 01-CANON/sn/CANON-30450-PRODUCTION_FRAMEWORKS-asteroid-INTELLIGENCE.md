---
id: [[CANON-30450-PRODUCTION_FRAMEWORKS-asteroid-INTELLIGENCE]]
name: Production Frameworks
tier: asteroid
chain: INTELLIGENCE
parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
sn_version: 1.0
converted: 2026-01-24
original_words: 3260
sn_words: 580
compression: 82%
---

# Κ-30450: Production Frameworks (SN)

TERM ProductionFrameworks:
    sutra: "2025 ended experimental toolkits—production-ready frameworks with stability commitments"
    gloss:
        March-October 2025 witnessed dramatic framework consolidation. Production-ready
        frameworks replaced research-oriented prototypes.
    spec:
        identity: PRODUCTION_FRAMEWORKS
        parent: [[CANON-30400-AGENTIC_ARCHITECTURE]]
end

PASS FrameworkTimeline:
    sutra: "OpenAI March, Google ADK April, Microsoft October, LangGraph continuous"
    spec:
        March_2025_OpenAI_SDK:
            replaced: experimental_Swarm
            abstractions: [Agents, Handoffs, Guardrails, Sessions]
            features: provider_agnostic (100+ LLMs) | built_in_tracing | auto_history | Pydantic_validation
            deployments: Coinbase | Klarna (2/3_support) | Clay (10x_growth)
        April_2025_Google_ADK:
            design: multi_agent_from_inception
            composition: LLM_agents | workflow_agents | custom_agents
            features: bidirectional_audio_video (v0.2.0) | Vertex_AI | 200+_models_LiteLLM | native_MCP_A2A
            powers: Agentspace | Customer_Engagement_Suite
        October_2025_Microsoft_AF:
            unified: AutoGen + Semantic_Kernel (ends_fragmentation)
            features: functional_agents_<20_lines | Orleans_distributed | Azure_AI_Foundry | Python + .NET
            note: AutoGen_Semantic_Kernel >> maintenance_mode
        LangGraph:
            version: Python_v0.6.10 | 1.0.0_alpha_September
            performance: lowest_latency | lowest_tokens
            features_2025: supervisor_pattern (Feb) | node_caching (Jun) | dynamic_tools (Aug)
end

PASS FrameworkComparison:
    sutra: "LangGraph graph-DAG, OpenAI minimal, ADK hierarchical, Microsoft enterprise, CrewAI role-based"
    spec:
        LangGraph:
            philosophy: model_as_stateful_directed_graph
            characteristics: [state_persists, HITL_any_node, explicit_control, complex_branching, steeper_curve]
            best_for: production_enterprise | loops_branching_approval | lowest_latency
        OpenAI_SDK:
            philosophy: minimal_abstractions_broad_compatibility
            abstractions: Agents | Handoffs | Guardrails | Sessions
            best_for: simplicity | broad_model_support | minimal_abstraction
        Google_ADK:
            philosophy: multi_agent_from_inception_interop_leader
            composition: LLM_agents + workflow_agents + custom_agents
            best_for: multi_model | interoperability | GCP | audio_video
        Microsoft_AF:
            philosophy: unified_enterprise_solution
            architecture: Orleans_event_driven | Azure_AI_Foundry | Python + .NET
            best_for: Azure | enterprise_governance | .NET
        CrewAI:
            philosophy: role_based_teamwork_simulating_humans
            model: roles_goals_backstories | sequential_or_hierarchical | state_as_outputs
            best_for: business_automation | marketing_sales_research | rapid_prototyping
end

PASS ProtocolSpecs:
    sutra: "MCP universal agent-to-tool, A2A peer collaboration, ACP low-latency, ANP decentralized"
    spec:
        MCP:
            purpose: universal_translation_agent_to_tool
            standard: JSON-RPC_2.0
            mechanism: common_interface >> eliminates_N×M
            June_2025: OAuth_Resource_Server | RFC_8707 | async_support
            adoption: OpenAI (Mar) | Google (Apr) | Microsoft (May) | AWS_steering
            analogy: "USB-C for AI"
            servers: thousands_available
        A2A:
            purpose: peer_agent_communication_collaboration
            launched: April_2025_Google
            backers: 150+_orgs (Microsoft, Salesforce, Atlassian, PayPal, Accenture, BCG, McKinsey, PwC)
            components: AgentCards (discovery) | Task_Lifecycle (submitted >> working >> completed) | Modality_Negotiation
            v0.3_July: gRPC | security_signatures
            governance: Linux_Foundation (June)
            relationship: complements_MCP (tools) + peer_coordination
        ACP: low_latency_controlled (manufacturing | AV)
        ANP: decentralized_identity (W3C_DIDs | JSON-LD)
end

PASS ToolIntegration:
    sutra: "Claude API May: code execution, MCP connectors, Files API, 1hr cache"
    spec:
        Claude_API_May_2025:
            code_execution: Python_sandbox + visualization
            MCP_connectors: direct_API >> remote_servers
            Files_API: upload_once >> reference_repeatedly
            caching: 1hr_TTL (12x_improvement) | 90%_cost | 85%_latency
        Claude_Code_October:
            features: remote_MCP | plugin_system (commands | subagents | servers | hooks)
            growth: 160%_active_users (post_Claude_4)
        integration_architecture:
            discovery: capability_registry | semantic_search | dynamic_add_remove
            invocation: standardized_request_response | JSON_or_function_call | normalized_result
            reliability: auto_retry | circuit_breakers | schema_validation
end

PASS EvaluationFrameworks:
    sutra: "CLASSic: Cost, Latency, Accuracy, Stability, Security—specialized outperform all five"
    spec:
        CLASSic (ICLR_2025):
            source: Aisera
            dimensions:
                cost: API | tokens | infrastructure >> domain_specific_dramatically_cheaper
                latency: E2E_response >> specialized_2.1s_vs_longer
                accuracy: workflow_correctness >> domain_specific_82.7%_IT_ops
                stability: consistency_across_inputs >> specialized_72%
                security: adversarial_resilience >> increasingly_critical
            validation: specialized_outperform_all_five
        Trajectory_Evaluation (Vertex_AI):
            focus: reasoning_quality_over_final_answers
            metrics: [exact_match, in_order_match, tool_correctness, tool_efficiency, reasoning_quality, error_recovery]
        benchmarks:
            AgentBench: LLM_as_Agent | 8_environments | 5-50_turns
            WebArena: web_tasks | 812_templated
            GAIA: general_AI_assistants | 466_human_annotated
            BrowseComp: info_retrieval | multi_site_complex
            SWE-bench: GitHub_issues | real_SWE
            OSWorld: OS_level | extremely_challenging (5%_best)
end

PASS EnterpriseAdoption:
    sutra: "Ollama 51%, LangChain 33%, Redis 43%—accuracy 87%, security 81% concerns"
    spec:
        Stack_Overflow_2025:
            orchestration: Ollama 51% | LangChain 33%
            memory: Redis 43% | ChromaDB 20% | pgvector 18%
            observability: Grafana_Prometheus 43% | Sentry 32%
            concerns: accuracy 87% | security_privacy 81%
            active_users: 48%
            impact: reduced_time 70% | productivity 69% | collaboration 17% (lowest)
        deployment_stack:
            observability: OpenTelemetry | prompt_logging | tool_tracking | token_monitoring
            tracing: correlation_IDs | E2E_tracking | latency_breakdowns
            monitoring: Phoenix | GALILEO | anomaly_detection | auto_rollbacks
end

PASS IndustryDeployments:
    sutra: "JPMorgan 360K hrs→seconds, Microsoft cancer hours→minutes, Klarna 2/3 support"
    spec:
        financial:
            JPMorgan_COIN: 50K+_agreements/yr | 360K_hrs >> seconds | quantum_resistant
            algorithmic_trading: 75%_equity_trades | ESG + crypto_arbitrage
            Darktrace_Antigena: autonomous_threat_neutralization (milliseconds)
        healthcare:
            Seattle_Children: clinical_notes + literature + images >> evidence_info
            eClinicalWorks: patient_data_extraction
            Microsoft_Cancer: <1%_multidisciplinary >> multi_agent >> hours_to_minutes
        technology:
            Netlify (Oct_2025): Claude_Code + Codex + Gemini | live_production
            Azure_AI_Foundry (Sep_2025): enterprise_ready | Deep_Research
            Salesforce_Agentforce: 70%_tier1_support
end

ARTIFACT GenAIParadox:
    sutra: "78% deploy, 80% no earnings impact—horizontal easy, vertical stuck in pilots"
    spec:
        paradox: 78%_deploy | 80%_no_material_earnings
        resolution:
            horizontal_copilots: easy | task_assistance | low_org_impact
            vertical_transformation: high_impact | stuck_in_pilots | requires_CEO-led
        success_examples: Northwestern_Mutual | Teladoc | AXA
        requirements: CEO-led | cross_functional_squads | process_reinvention | industrialized_delivery
end

PASS ForwardTrajectory:
    sutra: "MCP+A2A dual standards, multi-agent default, specialists over generalists"
    spec:
        protocols: MCP + A2A_dual_standards | Linux_Foundation + AWS_backing | network_effects
        architectures: multi_agent_default | specialists_over_generalists | hybrid_hub_spoke_mesh
        operational: observability + security + cost >> differentiate | feature_proliferation >> operational_excellence
        upcoming:
            Nov_2025: MCP_async + scalability + auth
            Q1_2026: Microsoft_AF_GA
            Q2_2026: Semantic_Kernel_Process_GA (Dapr + Orleans)
end
