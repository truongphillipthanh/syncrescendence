# ACTION_TYPES — Kinetic Layer Vocabulary

**Version**: 1.0.0
**Author**: Commander (Claude Opus 4.6)
**Date**: 2026-02-11
**Anchored to**: 15 existing roles in `roles` table
**Total**: 66 action types across 4 categories

---

## Action Types Table

| code | name | category | parent_role | description | input_type | output_type | write_back | requires_approval | automation_level |
|------|------|----------|-------------|-------------|------------|-------------|------------|-------------------|------------------|
| capture_text | Capture Text | core | capture | Ingest raw text content from any source into the system | text | text | TRUE | FALSE | automated |
| capture_screenshot | Capture Screenshot | core | capture | Take a visual snapshot of screen, app, or region | signal | file | TRUE | FALSE | assisted |
| capture_url | Capture URL | core | capture | Bookmark and archive a web resource with metadata | text | object | TRUE | FALSE | automated |
| capture_audio | Capture Audio | core | capture | Record or ingest audio for transcription or storage | signal | file | TRUE | FALSE | assisted |
| transform_text | Transform Text | core | process | Convert text between formats (markdown, HTML, JSON, etc.) | text | text | FALSE | FALSE | automated |
| extract_entities | Extract Entities | core | process | Identify and tag named entities, concepts, or primitives from text | text | data | FALSE | FALSE | automated |
| summarize | Summarize | core | process | Produce a concise distillation of longer content | text | text | FALSE | FALSE | automated |
| classify | Classify | core | process | Assign categorical labels, tags, or tiers to content | mixed | data | FALSE | FALSE | automated |
| render_markdown | Render Markdown | core | present | Format structured data or text as readable markdown output | data | text | FALSE | FALSE | automated |
| generate_report | Generate Report | core | present | Produce a structured analytical report from data inputs | data | text | TRUE | FALSE | automated |
| compose_message | Compose Message | core | present | Draft a communication for a specific audience and channel | text | text | FALSE | FALSE | assisted |
| dispatch_task | Dispatch Task | core | orchestrate | Create and route a TASK file to an agent inbox | object | file | TRUE | FALSE | automated |
| coordinate_agents | Coordinate Agents | core | orchestrate | Synchronize work across multiple Constellation agents | signal | signal | FALSE | FALSE | assisted |
| schedule_workflow | Schedule Workflow | core | orchestrate | Queue a multi-step workflow for deferred or periodic execution | object | object | TRUE | FALSE | automated |
| route_request | Route Request | core | orchestrate | Direct an inbound request to the appropriate handler agent | signal | signal | FALSE | FALSE | automated |
| persist_file | Persist File | core | store | Write a file to the filesystem with proper path and naming | file | file | TRUE | FALSE | automated |
| archive_content | Archive Content | core | store | Move completed or superseded content to archive with metadata | file | file | TRUE | FALSE | automated |
| index_document | Index Document | core | store | Add a document to a search index (Qdrant, Chroma, BM25) | file | data | TRUE | FALSE | automated |
| semantic_search | Semantic Search | core | search | Find content by meaning via vector similarity | text | data | FALSE | FALSE | automated |
| keyword_search | Keyword Search | core | search | Find content by exact or fuzzy text matching | text | data | FALSE | FALSE | automated |
| query_database | Query Database | core | search | Execute structured queries against SQLite, Neo4j, or APIs | text | data | FALSE | FALSE | automated |
| browse_web | Browse Web | core | search | Fetch and extract information from web URLs | text | text | FALSE | FALSE | automated |
| send_message | Send Message | core | communicate | Deliver a message to a specific agent or platform channel | text | signal | TRUE | FALSE | automated |
| post_update | Post Update | core | communicate | Publish a status update to a tracking platform (Linear, ClickUp) | text | object | TRUE | FALSE | automated |
| notify_agent | Notify Agent | core | communicate | Send a targeted notification or alert to a Constellation agent | signal | signal | FALSE | FALSE | automated |
| trigger_webhook | Trigger Webhook | core | automate | Fire an HTTP webhook to an external service | data | signal | TRUE | FALSE | autonomous |
| run_script | Run Script | core | automate | Execute a shell script, Python script, or CLI command | text | mixed | TRUE | FALSE | automated |
| execute_macro | Execute Macro | core | automate | Run a pre-defined Keyboard Maestro or Raycast macro | signal | mixed | TRUE | FALSE | autonomous |
| schedule_cron | Schedule Cron | core | automate | Register or modify a claudecron or launchd scheduled task | object | object | TRUE | TRUE | assisted |
| validate_schema | Validate Schema | core | verify | Check data structure against defined schema constraints | data | data | FALSE | FALSE | automated |
| run_tests | Run Tests | core | verify | Execute test suites and report pass/fail results | signal | data | FALSE | FALSE | automated |
| check_integrity | Check Integrity | core | verify | Verify FK consistency, orphan checks, and data completeness | data | data | FALSE | FALSE | automated |
| lint_code | Lint Code | core | verify | Run static analysis or style checks on source code | file | data | FALSE | FALSE | automated |
| encrypt_data | Encrypt Data | core | secure | Apply encryption to sensitive data at rest or in transit | data | data | TRUE | FALSE | automated |
| manage_credentials | Manage Credentials | core | secure | Store, retrieve, or update authentication credentials | object | object | TRUE | TRUE | assisted |
| rotate_keys | Rotate Keys | core | secure | Generate new API keys and update all consuming services | object | object | TRUE | TRUE | assisted |
| browse_filesystem | Browse Filesystem | core | navigate | List and explore directory structures and file metadata | text | data | FALSE | FALSE | automated |
| traverse_graph | Traverse Graph | core | navigate | Walk knowledge graph relationships in Neo4j or Graphiti | text | data | FALSE | FALSE | automated |
| switch_context | Switch Context | core | navigate | Change active working directory, tmux pane, or agent focus | signal | signal | TRUE | FALSE | assisted |
| modify_file | Modify File | core | edit | Make targeted changes to a specific file | text | file | TRUE | FALSE | automated |
| refactor_code | Refactor Code | core | edit | Restructure code while preserving behavior | file | file | TRUE | FALSE | assisted |
| merge_changes | Merge Changes | core | edit | Combine changes from branches, PRs, or agent outputs | file | file | TRUE | FALSE | assisted |
| run_inference | Run Inference | core | model | Send a prompt to an AI model and receive a response | text | text | FALSE | FALSE | automated |
| embed_text | Embed Text | core | model | Generate vector embeddings from text content | text | data | FALSE | FALSE | automated |
| fine_tune | Fine-Tune Model | core | model | Train or adapt a model on domain-specific data | data | object | TRUE | TRUE | manual |
| push_code | Push Code | core | deploy | Push committed changes to a remote git repository | signal | signal | TRUE | FALSE | assisted |
| build_artifact | Build Artifact | core | deploy | Compile, bundle, or package a deployable artifact | file | file | TRUE | FALSE | automated |
| release_version | Release Version | core | deploy | Tag and publish a versioned release | signal | signal | TRUE | TRUE | assisted |
| track_metrics | Track Metrics | core | monitor | Collect and record operational metrics over time | data | data | TRUE | FALSE | autonomous |
| detect_anomaly | Detect Anomaly | core | monitor | Identify deviations from expected patterns or thresholds | data | signal | FALSE | FALSE | autonomous |
| health_check | Health Check | core | monitor | Verify that services, agents, and pipelines are operational | signal | data | FALSE | FALSE | autonomous |
| research_synthesize | Research & Synthesize | compound | | Search multiple sources, process findings, and produce a structured synthesis | text | text | TRUE | FALSE | assisted |
| code_review | Code Review | compound | | Analyze code changes for correctness, style, security, and design | file | text | FALSE | FALSE | assisted |
| clarescence | Clarescence | compound | | Multi-pass progressive refinement of a decision space to convergence | text | file | TRUE | FALSE | assisted |
| blitzkrieg_dispatch | Blitzkrieg Dispatch | compound | | Parallel multi-agent task dispatch with coordination | object | signal | TRUE | FALSE | assisted |
| metabolize_content | Metabolize Content | compound | | Capture, extract unique value, compress, and archive original | file | file | TRUE | FALSE | assisted |
| corpus_survey | Corpus Survey | compound | | Comprehensive scan of vault or codebase for patterns and gaps | text | text | FALSE | FALSE | assisted |
| pipeline_fusion | Pipeline Fusion | compound | | Wire together multiple automation stages into a continuous pipeline | object | object | TRUE | TRUE | assisted |
| approve | Approve | governance | | Sovereign authorization gate for protected operations | signal | signal | TRUE | TRUE | manual |
| delegate | Delegate | governance | | Assign responsibility for a task or domain to another agent | object | signal | TRUE | FALSE | assisted |
| revoke | Revoke | governance | | Remove a permission, cancel a running task, or withdraw approval | signal | signal | TRUE | TRUE | manual |
| sandbox_operation | Sandbox Operation | governance | | Isolate an operation in a safe execution environment | object | object | TRUE | FALSE | automated |
| escalate | Escalate | governance | | Bump an issue to a higher authority or broader attention | signal | signal | TRUE | FALSE | assisted |
| gate | Gate | governance | | Block progression until a specified condition is met | signal | signal | FALSE | FALSE | automated |
| audit_trail | Audit Trail | governance | | Record a decision, action, or state change with full lineage | data | data | TRUE | FALSE | automated |
| commit_to | Commit To | personal | | Accept an obligation or allocate resources to a commitment | text | object | TRUE | TRUE | manual |
| decline | Decline | personal | | Refuse an obligation or request with recorded rationale | text | object | TRUE | FALSE | manual |
| renegotiate | Renegotiate | personal | | Modify the terms, timeline, or scope of an existing commitment | text | object | TRUE | TRUE | manual |
| allocate_attention | Allocate Attention | personal | | Direct cognitive resources to a specific domain or task | signal | signal | TRUE | FALSE | manual |
| set_boundary | Set Boundary | personal | | Define operational limits on time, energy, or scope | text | object | TRUE | FALSE | manual |
| recover_energy | Recover Energy | personal | | Schedule recovery time and reduce operational load | signal | signal | TRUE | FALSE | manual |
| prioritize | Prioritize | personal | | Reorder the commitment stack based on current values and constraints | data | data | TRUE | FALSE | assisted |
