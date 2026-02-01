# CANON-31150: PLATFORM CAPABILITY CATALOG
## SN: Definitive Inventory of Constellation Capabilities

```yaml
id: CANON-31150
tier: lunar
chain: INFORMATION
parent: CANON-31100
status: CRYSTALLINE
sn_version: 1.0.0
compression: ~85%
regeneration_source: 00-ORCHESTRATION/state/platform_capabilities.json
```

---

## SUTRA

Trinity Architecture: Oracle (Gemini) senses, Deviser (ChatGPT) plans, Executor (Claude) delivers—repository is ONLY place where truth congeals.

---

## GLOSS

Auto-generated capability inventory demonstrating metabolic pattern: temporal data lives externally (platform_capabilities.json), evergreen structure lives in template. Defines current platform configurations, routing decision tables, cost optimization strategies, and integration patterns for the Oracle-Deviser-Executor trinity. Regenerate when capabilities change—DO NOT edit directly.

---

## SPEC

### TERM::TrinityArchitecture
```
sutra: Oracle >> Evidence | Deviser >> Plan | Executor >> Delivery

spec:
  flow:
    oracle_gemini:
      role: sensing | RAG | corpus_scale
      output: evidence_packet
      NEVER: plans | executes

    deviser_chatgpt:
      role: planning | specification | audit
      output: plan_packet | audit_packet
      NEVER: executes_code

    executor_claude:
      role: implementation | filesystem_sovereignty
      output: execution_packet
      NEVER: corpus_scale_sensing

  communication: IMEP_protocol
    oracle >> deviser: evidence_packet
    deviser >> executor: plan_packet
    executor >> deviser: execution_packet
    deviser >> audit: audit_packet

  ground_truth: "repository is ONLY place where truth congeals"
```

---

### TERM::PlatformCapabilities
```
sutra: Current capability matrix per platform

spec:
  claude_executor:
    account: truongphillipthanh@gmail.com (+2 others)
    models: Opus_4.5 | Sonnet_4.5
    cost: $60/mo (3 x $20)
    capabilities:
      - filesystem_access: full_repository_sovereignty
      - code_generation: Opus/Sonnet
      - MCP_integration: external_tool_access
      - plan_mode: separates_planning_execution
      - context: ~200K_auto_compact
    routing_strengths:
      - execution | filesystem_ops
      - code_generation | writing_functions
      - file_manipulation | read_edit_write
      - verification | command_based_proof
      - repository_ops | git_ledgers
    routing_weaknesses:
      - corpus_scale_RAG (context_limit)
      - video_processing (no_native_multimodal)
      - long_horizon_planning (better_executor_than_planner)

  gemini_oracle:
    account: truongphillipthanh@gmail.com
    models: Gemini_2.5_Pro | Gemini_2.5_Flash
    cost: $20/mo
    capabilities:
      - 2M_context: entire_corpus_fits
      - drive_connector: repository_visibility
      - notebookLM: grounded_RAG_zero_hallucination
      - video_processing: 263_tok/sec_native
      - audio_processing: speaker_diarization
    routing_strengths:
      - corpus_scale_sensing (2M context)
      - video_transcription (native multimodal)
      - large_context_queries (repo + conversations)
      - grounded_RAG (NotebookLM)
      - historical_analysis (Oracle 0-13 single context)
    routing_weaknesses:
      - filesystem_access (read-only)
      - code_execution (not designed)
      - planning (sensing role)

  chatgpt_deviser:
    account: truongphillipthanh@icloud.com
    models: GPT-5.2_Instant | GPT-5.2_Thinking
    cost: $20/mo
    capabilities:
      - GPT-5.2_Thinking: ~3K_messages/week
      - deep_research: comprehensive_investigation
      - canvas: collaborative_editing
      - codex_CLI: GitHub_integration (if enabled)
      - connectors: Drive_GitHub (if enabled)
    routing_strengths:
      - long_horizon_planning (GPT-5.2 Thinking)
      - specification (clear acceptance criteria)
      - audit (verification against plan)
      - abstract_reasoning (architectural decisions)
      - multi_step_decomposition
    routing_weaknesses:
      - corpus_scale_sensing (context limit)
      - video_processing (no native multimodal)
      - code_execution (not designed)
```

---

### NORM::RoutingDecisionTable
```
sutra: Task type >> Primary platform >> Fallback

spec:
  routing[8]:
    corpus_sensing:
      primary: Gemini
      rationale: 2M_context_window
      fallback: Claude (limited context)

    video_processing:
      primary: Gemini
      rationale: native_multimodal
      fallback: manual_transcription

    planning:
      primary: ChatGPT
      rationale: GPT-5.2_Thinking
      fallback: Claude_Plan_Mode

    audit:
      primary: ChatGPT
      rationale: spec_verification
      fallback: Claude_verification

    execution:
      primary: Claude
      rationale: filesystem_sovereignty
      fallback: manual_operations

    code_generation:
      primary: Claude
      rationale: Opus/Sonnet
      fallback: ChatGPT

    grounded_RAG:
      primary: Gemini
      rationale: NotebookLM
      fallback: Claude_with_citations

    long_horizon_decomposition:
      primary: ChatGPT
      rationale: GPT-5.2_Thinking
      fallback: Claude_ultrathink

  decision_flow:
    1: identify_task_type
    2: route_to_primary
    3: if_unavailable >> fallback
    4: if_both_unavailable >> escalate_Principal

  override_conditions:
    - Principal_explicitly_specifies
    - task_requires_unique_capability
    - cost_optimization
```

---

### NORM::EvergreenPrinciples
```
sutra: Constants regardless of capability changes

spec:
  trinity_roles:
    oracle: sensing_RAG_corpus | NEVER_plans_executes | ONLY_observes_reports
    deviser: planning_specification_audit | NEVER_executes | ONLY_designs_verifies
    executor: implementation_filesystem | NEVER_corpus_sensing | ONLY_executes_verifies

  IMEP_protocol:
    format: structured_packets | NOT_free_form
    flow: Oracle(Evidence) >> Deviser(Plan) >> Executor(Execution) >> Deviser(Audit)
    truth: repository_ONLY

  routing_by_teleology:
    principle: functional_fit | NOT_brand_loyalty
    consider: task_requirements | cost_performance | role_boundaries

  ground_truth_discipline:
    oracle: cite_every_claim (file:line, timestamp)
    deviser: specify_verifiable_acceptance_criteria
    executor: verify_every_deliverable (command output)

  capability_evolution:
    models_upgrade | features_added | pricing_changes
    catalog_regenerates: track_current | principles_persist
```

---

### TERM::IntegrationPatterns
```
sutra: Common multi-platform workflows

spec:
  source_processing:
    1_oracle: sense_video/article >> evidence_packet
    2_deviser: plan_workflow >> plan_packet
    3_executor: process_integrate_ledger >> execution_packet
    4_deviser: verify_complete >> audit_packet
    assignments:
      gemini: native_video/audio | signal_tier
      chatgpt: decompose_steps | specify_verification
      claude: transcribe | update_sources.csv | integrate_CANON

  corpus_scale_query:
    1_oracle: load_repo+history | search | cite >> evidence_packet
    2_principal: review_findings
    note: no_Deviser/Executor_unless_findings_trigger_action
    assignments:
      gemini: 2M_context | upload_corpus | comprehensive_search

  complex_implementation:
    1_deviser: decompose >> plan_packet_batch
    2_executor: phase_1 >> execution_1
    3_deviser: audit_1 >> audit_1
    4_executor: phase_2 >> execution_2
    [continue_until_complete]
    assignments:
      chatgpt: GPT-5.2_Thinking | long_horizon
      claude: Opus_complex | Sonnet_execution
```

---

### TERM::CostOptimization
```
sutra: $100/mo total | maximize ROI

spec:
  spend:
    claude: $60/mo (3 x Pro) | 75% utilization
    gemini: $20/mo (Advanced) | 40% utilization
    chatgpt: $20/mo (Plus) | 30% utilization
    total: $100/mo

  strategies:
    model_selection: Sonnet > Opus when well-specified
    thinking_budget: reserve GPT-5.2_Thinking for complex
    context_reuse: load_corpus_once | query_multiple
    batch_operations: group_similar | minimize_switching

  ROI_metrics:
    autonomous_IMEP_cycles: target ≥10
    relay_reduction: target ≥25%
    sources_processed: track
    CANON_integrations: track
```

---

### TERM::FutureProjections
```
sutra: Capability evolution expectations

spec:
  phase_2_juvenile_apr_2026:
    changes:
      - API_based_IMEP
      - direct_inter_platform_communication
      - automated_routing
      - cost_reduction_efficiency
    additions:
      claude: MCP_server_integrations
      gemini: NotebookLM_API (Enterprise)
      chatgpt: Codex_CLI_GitHub

  phase_3_adolescent_jan_2027:
    changes:
      - multi_modal_outputs
      - external_API_endpoints
      - fine_tuned_model_optimization
    additions:
      claude: video_generation_if_available
      gemini: advanced_multimodal_synthesis
      chatgpt: agent_mode_orchestration
```

---

### PROC::Regeneration
```
sutra: Update catalog when capabilities change

steps:
  1: edit_data_source >> vim 00-ORCHESTRATION/state/platform_capabilities.json
  2: regenerate >> python3 00-ORCHESTRATION/scripts/regenerate_canon.py 31150
  3: review_diff >> git diff 01-CANON/CANON-31150*.md
  4: commit >> feat(canon): regenerate 31150 with updated platform data

triggers:
  - new_platform_added_removed
  - capability_status_change
  - pricing_change
  - major_model_upgrade
  - monthly_system_health_review
```

---

## XREF

```yaml
parent: [[CANON-31100-ACUMEN-planetary-INFORMATION]]
siblings:
  - [[CANON-31140-IIC-lunar-ACUMEN-planetary-INFORMATION]]
integration_points:
  - IMEP_protocol: packet_flow_specification
  - Technology_Stack: platform_selection_rationale
  - Operations: routing_decision_implementation
```

---

**Status**: CRYSTALLINE | auto-regenerated
**Last Regenerated**: 2026-01-16
**Data Version**: 1.0.0
**Compression**: 12KB prose → ~3KB SN (~85% reduction)
