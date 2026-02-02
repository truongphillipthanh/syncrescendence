# CANON-31150: PLATFORM CAPABILITY CATALOG
## SN: Definitive Inventory of Constellation Capabilities

```yaml
id: CANON-31150
tier: lunar
chain: INFORMATION
parent: CANON-31100
status: CRYSTALLINE
sn_version: 2.0.0
compression: ~85%
regeneration_source: 00-ORCHESTRATION/state/platform_capabilities.json
```

---

## SUTRA

Constellation Architecture: Cartographer (Gemini) senses, Vanguard (ChatGPT) plans, Commander (Claude) delivers—repository is ONLY place where truth congeals.

---

## GLOSS

Auto-generated capability inventory demonstrating metabolic pattern: temporal data lives externally (platform_capabilities.json), evergreen structure lives in template. Defines current platform configurations, routing decision tables, cost optimization strategies, and integration patterns for the Constellation. Regenerate when capabilities change—DO NOT edit directly.

---

## SPEC

### TERM::ConstellationArchitecture
```
sutra: Cartographer >> Evidence | Vanguard >> Plan | Commander >> Delivery

spec:
  flow:
    cartographer_gemini:
      role: sensing | RAG | corpus_scale
      output: evidence_packet
      NEVER: plans | executes

    vanguard_chatgpt:
      role: planning | specification | audit
      output: plan_packet | audit_packet
      NEVER: executes_code

    commander_claude:
      role: implementation | filesystem_sovereignty
      output: execution_packet
      NEVER: corpus_scale_sensing

  dispatch_protocol:
    cartographer >> vanguard: evidence_packet
    vanguard >> commander: plan_packet
    commander >> vanguard: execution_packet
    vanguard >> audit: audit_packet

  ground_truth: "repository is ONLY place where truth congeals"
```

---

### TERM::PlatformCapabilities
```
sutra: Current capability matrix per platform

spec:
  claude_commander:
    account: truongphillipthanh@icloud.com (A1 Max) + icloud.truongphillipthanh@gmail.com (A2 Pro)
    models: Opus_4.5 | Sonnet_4.5 | Haiku_4.5
    cost: $120/mo (Max $100 + Pro $20)
    capabilities:
      - filesystem_access: full_repository_sovereignty
      - code_generation: Opus/Sonnet/Haiku
      - MCP_integration: external_tool_access
      - plan_mode: separates_planning_execution
      - context: ~200K_auto_compact | 1M_beta
      - extended_thinking: auto_31999_tokens
      - hooks: Stop | PreCompact | UserPromptSubmit
      - skills: 7_operational
    routing_strengths:
      - execution | filesystem_ops
      - code_generation | writing_functions
      - file_manipulation | read_edit_write
      - verification | command_based_proof
      - repository_ops | git_ledgers
      - multi_agent_dispatch | hook_automation
    routing_weaknesses:
      - corpus_scale_RAG (context_limit)
      - video_processing (no_native_multimodal)
      - long_horizon_planning (better_executor_than_planner)

  gemini_cartographer:
    account: icloud.truongphillipthanh@gmail.com (A2 Google AI Pro)
    models: Gemini_3_Pro | Gemini_3_Flash | Gemini_3_Deep_Think
    cost: $20/mo
    capabilities:
      - 1M_context: full_corpus_sensing
      - drive_connector: repository_visibility_via_Gems
      - notebookLM: grounded_RAG_zero_hallucination
      - video_processing: native_multimodal_ingestion
      - audio_processing: speaker_diarization
      - gems: custom_instruction_profiles
      - CLI_access: installed | API_key_pending
    routing_strengths:
      - corpus_scale_sensing (1M context)
      - video_transcription (native multimodal)
      - large_context_queries (repo + conversations)
      - grounded_RAG (NotebookLM)
      - multimodal_clarification (text, image, audio, video)
    routing_weaknesses:
      - filesystem_access (read-only)
      - code_execution (not designed)
      - planning (sensing role)

  chatgpt_vanguard:
    account: truongphillipthanh@icloud.com (A1 Plus)
    models: GPT-5.2_Instant | GPT-5.2_Thinking
    cost: $20/mo
    capabilities:
      - GPT-5.2_Thinking: ~3K_messages/week
      - deep_research: comprehensive_investigation
      - canvas: collaborative_editing
      - codex_CLI: installed | API_key_pending
      - connectors: Drive_GitHub (if enabled)
      - projects: context_isolation | project_only_memory
    routing_strengths:
      - long_horizon_planning (GPT-5.2 Thinking)
      - specification (clear acceptance criteria)
      - audit (verification against plan)
      - abstract_reasoning (architectural decisions)
      - multi_step_decomposition
      - creative_expansion_ideation
    routing_weaknesses:
      - corpus_scale_sensing (128K context limit)
      - video_processing (no native multimodal)
      - code_execution (not designed)
```

---

### NORM::RoutingDecisionTable
```
sutra: Task type >> Primary platform >> Fallback

spec:
  routing[10]:
    corpus_sensing:
      primary: Gemini
      rationale: 1M_context_window
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
      fallback: Codex_CLI

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

    real_time_discourse:
      primary: Grok
      rationale: X_Twitter_integration
      fallback: Perplexity

    external_verification:
      primary: Perplexity
      rationale: citation_backed_search
      fallback: Gemini

  decision_flow:
    1: identify_task_type
    2: route_to_primary
    3: if_unavailable >> fallback
    4: if_both_unavailable >> escalate_Sovereign

  override_conditions:
    - Sovereign_explicitly_specifies
    - task_requires_unique_capability
    - cost_optimization
```

---

### NORM::EvergreenPrinciples
```
sutra: Constants regardless of capability changes

spec:
  constellation_roles:
    oracle_grok: cultural_sensing | EQ | reality_checks | adversarial_grounding | NEVER_plans_executes | ONLY_observes_reports
    vanguard_chatgpt: planning_specification_audit | NEVER_executes | ONLY_designs_verifies
    commander_claude: implementation_filesystem | NEVER_corpus_sensing | ONLY_executes_verifies
    cartographer_gemini: corpus_sensing | evidence_packs | 1M_context | stateless_reproducible
    diviner_gemini_web: multimodal_clarification | TTS_digests | Gems_Drive

  dispatch_protocol:
    format: structured_packets | NOT_free_form
    flow: Cartographer(Evidence) >> Vanguard(Plan) >> Commander(Execution) >> Vanguard(Audit)
    truth: repository_ONLY

  routing_by_teleology:
    principle: functional_fit | NOT_brand_loyalty
    consider: task_requirements | cost_performance | role_boundaries

  ground_truth_discipline:
    oracle_grok: cite_every_claim (file:line, timestamp)
    vanguard: specify_verifiable_acceptance_criteria
    commander: verify_every_deliverable (command output)

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
    1_cartographer: sense_video/article >> evidence_packet
    2_vanguard: plan_workflow >> plan_packet
    3_commander: process_integrate_ledger >> execution_packet
    4_vanguard: verify_complete >> audit_packet
    assignments:
      gemini: native_video/audio | signal_tier
      chatgpt: decompose_steps | specify_verification
      claude: transcribe | update_sources.csv | integrate_CANON

  corpus_scale_query:
    1_cartographer: load_repo+history | search | cite >> evidence_packet
    2_sovereign: review_findings
    note: no_Vanguard/Commander_unless_findings_trigger_action
    assignments:
      gemini: 1M_context | upload_corpus | comprehensive_search

  complex_implementation:
    1_vanguard: decompose >> plan_packet_batch
    2_commander: phase_1 >> execution_1
    3_vanguard: audit_1 >> audit_1
    4_commander: phase_2 >> execution_2
    [continue_until_complete]
    assignments:
      chatgpt: GPT-5.2_Thinking | long_horizon
      claude: Opus_complex | Sonnet_execution
```

---

### TERM::CostOptimization
```
sutra: $160/mo total | maximize ROI

spec:
  spend:
    claude_code: $100/mo (Max 5x) | 80% utilization
    claude_web: $20/mo (Pro) | 30% utilization
    chatgpt: $20/mo (Plus) | 25% utilization
    google_ai: $20/mo (AI Pro) | 20% utilization
    total: $160/mo

  strategies:
    model_selection: Sonnet > Opus when well-specified
    thinking_budget: reserve GPT-5.2_Thinking for complex
    context_reuse: load_corpus_once | query_multiple
    batch_operations: group_similar | minimize_switching

  ROI_metrics:
    autonomous_dispatch_cycles: target ≥10
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
      - API_based_dispatch
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
  - dispatch_protocol: packet_flow_specification
  - Technology_Stack: platform_selection_rationale
  - Operations: routing_decision_implementation
```

---

**Status**: CRYSTALLINE | auto-regenerated
**Last Regenerated**: 2026-02-06
**Data Version**: 2.0.0
**Compression**: 12KB prose → ~3KB SN (~85% reduction)
