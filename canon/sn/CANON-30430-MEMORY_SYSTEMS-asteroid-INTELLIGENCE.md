---
id: [[CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE]]
name: Memory Systems
tier: asteroid
chain: INTELLIGENCE
parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
sn_version: 1.0
converted: 2026-01-24
original_words: 2360
sn_words: 420
compression: 82%
---

# Κ-30430: Memory Systems (SN)

TERM MemorySystems:
    sutra: "Memory is context engineering—what enters window determines capability"
    gloss:
        Agent intelligence constrained by ability to remember and learn. Multi-layered
        memory architecture manages information across timescales and abstraction levels.
    spec:
        identity: MEMORY_SYSTEMS
        parent: [[CANON-30400-AGENTIC_ARCHITECTURE]]
end

PASS MemoryTaxonomy:
    sutra: "Working fast, episodic chronological, semantic factual, procedural skilled, prospective scheduled"
    spec:
        working:
            function: immediate_task_context
            characteristics: fast_volatile | rapid_access | limited_capacity
            implementation: context_window | in_memory_structures
        episodic:
            function: chronological_record_of_experiences
            characteristics: event_sequences | actions_outcomes | session_transcripts
            implementation: event_logs | vector_stores
            use: case_based_reasoning | learning_from_trial_error
        semantic:
            function: factual_knowledge_repository
            characteristics: general_facts | concepts_relationships | domain_knowledge
            implementation: knowledge_graphs | RAG
            analogy: internal_encyclopedia
        procedural:
            function: learned_skills_workflows
            characteristics: multi_step_sequences | automated_patterns | tool_usage
            implementation: tool_definitions | workflow_templates
            benefit: execute_without_first_principles
        prospective:
            function: future_intentions_schedules
            characteristics: planned_actions | scheduled_tasks | todo_queues
            implementation: planning_state | task_queues
end

PASS ArchitecturalInnovations:
    sutra: "A-MEM Zettelkasten-inspired, MIRIX six-tier, MemGPT OS-hierarchy"
    spec:
        A_MEM (NeurIPS_2025):
            inspiration: Zettelkasten_PKM
            shift: passive_consumer >> active_curator
            mechanism:
                notes: contextual_descriptions + keywords + vectors (all-MiniLM-L6-v2)
                dynamic_indexing: new_memories >> existing_memory_updates | semantic_similarity_linking
            results: superior_across_6_foundation_models | outperforms_baselines | no_fixed_schemas
        MIRIX:
            architecture: six_tier_taxonomy
            tiers: [Core, Episodic, Semantic, Procedural, Resource, Knowledge_Vaults]
            benchmarks: ScreenshotVQA +35% | Storage -99.9% | LOCOMO 85.4%
        MemGPT (Letta):
            inspiration: OS_memory_hierarchy
            architecture: core (RAM) | conversational (buffer) | archival (long_term) | external (disk)
            mechanism: agents_manage_via_function_calls | autonomous_tier_management | creates_unlimited_illusion
            benchmark: LoCoMo 74%
            principle: "Memory is context engineering"
end

PASS VectorDatabases:
    sutra: "Redis 43%, ChromaDB 20%, pgvector 18%—semantic similarity over keyword"
    spec:
        function: high_dimensional_embedding_storage | nearest_neighbor_retrieval
        adoption:
            Redis: 43% | fast_versatile_production
            ChromaDB: 20% | open_source_developer_friendly
            pgvector: 18% | PostgreSQL_SQL_integration
            Pinecone: enterprise | managed_scalable
            Milvus: enterprise | open_source_distributed
            Weaviate: enterprise | GraphQL_modular
        memory_platforms:
            Mem0: hybrid (vector + graph + KV) | personalization
            Zep: long_term + session | graph_based
            LangMem: LangChain_ecosystem | modular_types
            Memary: knowledge_graph | entity_relationships
end

PASS ContextEngineering:
    sutra: "200K+ context doesn't eliminate intelligent management—indiscriminate stuffing degrades"
    spec:
        context_evolution: Claude_3.5 200K+ | Gemini_1.5 200K+
        implication: reduced_retrieval | but_stuffing_degrades_quality
        strategies:
            semantic_chunking: divide_by_meaning | preserve_coherence
            relevance_scoring: score_by_task | prioritize_high | exclude_low
            temporal_decay: recent_weighted_higher | old_decays_unless_reinforced
            hierarchical_summarization: compress_older | retain_detail_recent
        sleep_time_compute: async_during_idle | reorganize | optimize_indices | prune_stale
end

PASS MemoryArchitecture:
    sutra: "Message buffer → Core memory → External database—layered with retrieval optimization"
    spec:
        layers:
            layer1_message_buffer: recent_conversational | rolling_window | immediate_access
            layer2_core_memory: persistent_facts_preferences | KV_store | explicit_updates
            layer3_external_database: retrievable_knowledge | vector + graph | semantic_search
        retrieval_strategies:
            ANN_indexing: approximate_nearest_neighbor | sub_linear | slight_accuracy_tradeoff
            hybrid_search: semantic + keyword | BM25 + vector_fusion
            reranking: LLM_based | context_aware | additional_latency
end

PASS MemoryInterfaces:
    sutra: "Write, read, update, forget—plus memory-aware planning"
    spec:
        write: content + type + metadata >> store >> index + link
        read: query + type + top_k >> ranked_list
        update: id + delta >> modify >> re_index + propagate
        forget: criteria >> remove_deprecate (privacy | relevance)
        memory_integrated_planning:
            before_action: query_episodic (done_before?) + semantic (facts?) + procedural (approach?)
            during_action: update_working + log_episodic
            after_action: extract_to_semantic + update_procedural + schedule_prospective
end

NORM ConsistencyCoherence:
    sutra: "Contradiction, staleness, fragmentation, hallucination—resolve with version, TTL, linking, scoring"
    spec:
        contradiction: version_tracking | recency_weighting | explicit_resolution
        staleness: TTL_mechanisms | periodic_refresh | source_verification
        fragmentation: linking_mechanisms | periodic_consolidation
        hallucination_propagation: confidence_scoring | source_attribution | verification_gates
        session_continuity:
            persistent_core: user_preferences + relationship_history + learned_patterns
            bridging: start >> load_context | end >> summarize_persist
            identity: consistent_behavior + accumulated_knowledge + relationship_continuity
end

TEST ProductionMetrics:
    sutra: "Retrieval <100ms, precision >80%, context utilization >60%"
    spec:
        retrieval_latency: <100ms P95
        storage_efficiency: high_compression (bytes_per_item)
        relevance_precision: >80% (usefulness)
        context_utilization: >60% (useful_tokens / total)
        scaling: shard_by_user | distribute_index | load_balance | hot/warm/cold_tiers | age_prune
        security: agent_isolation | user_segregation | capability_access | encryption | PII_handling | audit
end

ARTIFACT ToolOverloadInsight:
    sutra: "Diminishing returns beyond 8-10 tools—use multi-agent with focused subsets"
    spec:
        finding: single_agent >> diminishing_returns > 8-10_tools
        cause: context_window_constraints + selection_complexity
        solution: multi_agent >> specialized_agents_each_access_focused_tool_subsets
end
