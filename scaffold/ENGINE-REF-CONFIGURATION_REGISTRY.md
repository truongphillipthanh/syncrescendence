# Syncrescendence Configuration Registry
## Normalized Relational Schema (CSV/SQLite Ready)

---

## TABLE: accounts

| account_id | email | auth_method | teleology | owns_origin | google_ecosystem |
|------------|-------|-------------|-----------|-------------|------------------|
| 1 | truongphillipthanh@icloud.com | apple | sovereign_substrate | TRUE | FALSE |
| 2 | icloud.truongphillipthanh@gmail.com | google | parallel_executor | FALSE | TRUE |
| 3 | truongphillipthanh@gmail.com | google | primary_interface | FALSE | TRUE |

---

## TABLE: devices

| device_id | device_name | device_type | location | always_on | repo_host |
|-----------|-------------|-------------|----------|-----------|-----------|
| 1 | Mac mini | desktop | desk | TRUE | TRUE |
| 2 | MacBook Air | laptop | mobile | FALSE | FALSE |
| 3 | iPhone 15 | mobile | pocket | TRUE | FALSE |
| 4 | iPhone mini | mobile | pocket | TRUE | FALSE |

---

## TABLE: account_device_bindings

| binding_id | account_id | device_id | is_primary |
|------------|------------|-----------|------------|
| 1 | 2 | 1 | TRUE |
| 2 | 3 | 2 | TRUE |
| 3 | 3 | 3 | TRUE |
| 4 | 1 | 4 | TRUE |
| 5 | 1 | 1 | FALSE |
| 6 | 1 | 2 | FALSE |

---

## TABLE: browsers

| browser_id | browser_name | account_id | device_id | purpose |
|------------|--------------|------------|-----------|---------|
| 1 | Chrome | 3 | 2 | primary_account_3 |
| 2 | Chrome | 3 | 1 | backup_account_3 |
| 3 | Atlas+Comet | 1 | 2 | account_1_access |
| 4 | Atlas+Comet | 1 | 1 | account_1_access |
| 5 | Orion | 2 | 1 | account_2_mac_mini |

---

## TABLE: platforms

| platform_id | platform_name | platform_type | vendor | has_projects | has_memory | max_context_tokens |
|-------------|---------------|---------------|--------|--------------|------------|-------------------|
| 1 | Claude Web | web_app | anthropic | TRUE | TRUE | 200000 |
| 2 | Claude Desktop | desktop_app | anthropic | FALSE | FALSE | 200000 |
| 3 | Claude Code | cli | anthropic | FALSE | TRUE | 200000 |
| 4 | ChatGPT Web | web_app | openai | TRUE | TRUE | 128000 |
| 5 | ChatGPT Desktop | desktop_app | openai | FALSE | FALSE | 128000 |
| 6 | Codex CLI | cli | openai | FALSE | TRUE | 128000 |
| 7 | Gemini Web | web_app | google | TRUE | TRUE | 1000000 |
| 8 | Gemini CLI | cli | google | FALSE | FALSE | 1000000 |
| 9 | Grok Web | web_app | xai | FALSE | FALSE | 128000 |
| 10 | Perplexity Web | web_app | perplexity | FALSE | FALSE | 128000 |

---

## TABLE: roles

| role_id | role_name | role_function | specification_tier | invocation_mode |
|---------|-----------|---------------|-------------------|-----------------|
| 1 | INTERPRETER | Transform messy ideation into structured understanding | open_or_guided | continuous |
| 2 | COMPILER | Transform explicit specifications into formatted artifacts | strict | on_demand |
| 3 | DIGESTOR | Transform complex artifacts into digestible summaries | guided | on_demand |
| 4 | ORACLE | Sense corpus state and generate evidence packs | strict | on_demand |
| 5 | EXECUTOR_LEAD | Implement changes with judgment and verification | guided | on_demand |
| 6 | PARALLEL_EXECUTOR | Execute mechanically parallelizable tasks | strict | batch |
| 7 | RED_TEAM | Stress-test and challenge architectural decisions | open | on_demand |
| 8 | VERIFIER | Verify facts with citation-backed research | guided | on_demand |

---

## TABLE: role_platform_assignments

| assignment_id | role_id | platform_id | account_id | model_tier | instances |
|---------------|---------|-------------|------------|------------|-----------|
| 1 | 1 | 1 | 3 | opus | 1 |
| 2 | 2 | 4 | 1 | gpt5.2 | 1 |
| 3 | 3 | 7 | 3 | gemini_pro | 1 |
| 4 | 4 | 8 | 3 | gemini_pro | 1 |
| 5 | 5 | 3 | 3 | opus | 1 |
| 6 | 6 | 3 | 2 | sonnet | 2 |
| 7 | 7 | 9 | 1 | grok | 1 |
| 8 | 8 | 10 | NULL | perplexity | 1 |

---

## TABLE: platform_configurations

| config_id | platform_id | account_id | config_type | config_key | config_value | status |
|-----------|-------------|------------|-------------|------------|--------------|--------|
| 1 | 1 | 3 | project | project_name | Syncrescendence IIC | CONFIGURED |
| 2 | 1 | 3 | project | memory_mode | project_specific | CONFIGURED |
| 3 | 4 | 1 | project | project_name | Syncrescendence Compiler | TO_CONFIGURE |
| 4 | 4 | 1 | project | memory_mode | PROJECT_ONLY | CRITICAL |
| 5 | 7 | 3 | gem | gem_name | Constellation Digestor | TO_CONFIGURE |
| 6 | 7 | 3 | gem | drive_folder | Constellation-State/ | TO_CONFIGURE |
| 7 | 3 | 3 | file | config_file | CLAUDE.md | CONFIGURED |
| 8 | 6 | 1 | file | config_file | AGENTS.md | TO_VERIFY |
| 9 | 8 | 3 | file | config_file | GEMINI.md | TO_CREATE |

---

## TABLE: project_files

| file_id | platform_id | account_id | file_name | file_purpose | required | status |
|---------|-------------|------------|-----------|--------------|----------|--------|
| 1 | 1 | 3 | COCKPIT.md | system_overview | TRUE | UPLOADED |
| 2 | 1 | 3 | constellation-teleology.md | architecture_rationale | TRUE | UPLOADED |
| 3 | 1 | 3 | memory-architecture-teleology.md | memory_rationale | TRUE | UPLOADED |
| 4 | 1 | 3 | ARCH-FRONTIER_MODELS_2026-01.md | model_capabilities | FALSE | UPLOADED |
| 5 | 1 | 3 | ARCH-PLATFORM_FEATURES_2026-01.md | platform_features | FALSE | UPLOADED |
| 6 | 4 | 1 | handoff-token-active.txt | current_state | TRUE | TO_UPLOAD |
| 7 | 4 | 1 | compile-templates.md | formatting_templates | TRUE | TO_CREATE |
| 8 | 7 | 3 | COCKPIT.md | system_overview | TRUE | TO_UPLOAD |
| 9 | 7 | 3 | digest-templates.md | output_formats | TRUE | TO_CREATE |

---

## TABLE: connectors

| connector_id | platform_id | account_id | connector_name | enabled | requires_google |
|--------------|-------------|------------|----------------|---------|-----------------|
| 1 | 1 | 3 | GitHub | TRUE | FALSE |
| 2 | 1 | 3 | Google Drive | TRUE | TRUE |
| 3 | 1 | 3 | Gmail | TRUE | TRUE |
| 4 | 7 | 3 | Gmail | TRUE | TRUE |
| 5 | 7 | 3 | Drive | TRUE | TRUE |
| 6 | 7 | 3 | Calendar | TRUE | TRUE |
| 7 | 7 | 3 | YouTube | TRUE | TRUE |

---

## TABLE: cli_configurations

| cli_id | platform_id | account_id | config_file_path | model_default | extended_thinking |
|--------|-------------|------------|------------------|---------------|-------------------|
| 1 | 3 | 3 | ~/.claude/CLAUDE.md | opus_4.5 | TRUE |
| 2 | 3 | 2 | ~/.claude/CLAUDE.md | sonnet_4.5 | TRUE |
| 3 | 6 | 1 | ~/.codex/AGENTS.md | gpt5.2 | FALSE |
| 4 | 8 | 3 | ~/.gemini/config | gemini_pro | FALSE |

---

## TABLE: automation_tools

| tool_id | tool_name | tool_type | purpose | status | integration_method |
|---------|-----------|-----------|---------|--------|-------------------|
| 1 | rclone | sync | google_drive_sync | TO_CONFIGURE | cli |
| 2 | Make | build | task_orchestration | TO_CREATE | cli |
| 3 | Git Hooks | vcs | state_capture | TO_CREATE | file |
| 4 | Keyboard Maestro | macro | system_automation | AVAILABLE | gui |
| 5 | Hazel | watch | folder_monitoring | AVAILABLE | gui |
| 6 | Automator | workflow | macos_automation | AVAILABLE | gui |
| 7 | AppleScript | script | macos_scripting | AVAILABLE | cli |
| 8 | Stream Deck | hardware | physical_triggers | AVAILABLE | hardware |
| 9 | Better Touch Tool | input | gesture_triggers | AVAILABLE | gui |
| 10 | LogiOptions+ | input | mouse_customization | AVAILABLE | gui |
| 11 | TextExpander | snippet | text_expansion | AVAILABLE | system |
| 12 | Scheduler | cron | scheduled_tasks | AVAILABLE | gui |
| 13 | n8n | workflow | api_automation | AVAILABLE | web |
| 14 | Google Cloud | cloud | vertex_ai_studio | AVAILABLE | api |

---

## TABLE: chrome_extensions

| extension_id | extension_name | platform_id | account_id | purpose |
|--------------|----------------|-------------|------------|---------|
| 1 | Claude Extension | 1 | 3 | quick_claude_access |
| 2 | Gemini Extension | 7 | 3 | quick_gemini_access |

---

## TABLE: states

| state_id | state_name | location | characteristic | terminal |
|----------|------------|----------|----------------|----------|
| 1 | CAPTURED | sovereign_mind | unstructured_ephemeral | FALSE |
| 2 | INTERPRETED | claude_web_artifact | structured_understanding | FALSE |
| 3 | COMPILED | chatgpt_canvas | formatted_artifact | FALSE |
| 4 | DIGESTED | gemini_docs | clarified_summary | FALSE |
| 5 | SENSED | gemini_cli_output | evidence_pack | FALSE |
| 6 | VERIFIED | perplexity_grok | externally_validated | FALSE |
| 7 | STAGED | outgoing_directory | ready_for_commit | FALSE |
| 8 | COMMITTED | repository | ground_truth | TRUE |

---

## TABLE: transitions

| transition_id | from_state_id | to_state_id | via_platform_id | payload_type | time_target_sec |
|---------------|---------------|-------------|-----------------|--------------|-----------------|
| 1 | 1 | 2 | 1 | raw_ideation | NULL |
| 2 | 2 | 3 | 4 | full_specification | 30 |
| 3 | 2 | 4 | 7 | artifact_with_goal | 20 |
| 4 | 2 | 5 | 8 | survey_command | 10 |
| 5 | 2 | 6 | 10 | verification_query | 15 |
| 6 | 3 | 7 | NULL | download | 15 |
| 7 | 4 | 7 | NULL | docs_export | 15 |
| 8 | 5 | 2 | NULL | evidence_reintegration | 10 |
| 9 | 6 | 2 | NULL | citation_reintegration | 10 |
| 10 | 7 | 8 | 3 | git_commit | 5 |

---

## TABLE: handoff_protocols

| protocol_id | from_role_id | to_role_id | payload_size | manual_steps | automation_potential |
|-------------|--------------|------------|--------------|--------------|---------------------|
| 1 | 1 | 2 | large | 3 | medium |
| 2 | 1 | 3 | medium | 2 | high |
| 3 | 1 | 4 | small | 1 | high |
| 4 | 2 | 1 | medium | 3 | medium |
| 5 | 2 | 3 | medium | 2 | high |
| 6 | 3 | 1 | small | 2 | medium |
| 7 | 4 | 1 | medium | 2 | high |
| 8 | 5 | 8 | small | 1 | high |

---

## TABLE: memory_configurations

| memory_id | platform_id | account_id | memory_layer | scope | persistence | editable |
|-----------|-------------|------------|--------------|-------|-------------|----------|
| 1 | 1 | 3 | user_preferences | global | permanent | TRUE |
| 2 | 1 | 3 | project_knowledge | project | permanent | TRUE |
| 3 | 1 | 3 | project_memory | project | auto_learned | TRUE |
| 4 | 1 | 3 | thread_context | session | ephemeral | FALSE |
| 5 | 1 | 3 | past_chat_search | cross_thread | permanent | FALSE |
| 6 | 4 | 1 | custom_instructions | global | permanent | TRUE |
| 7 | 4 | 1 | global_memory | global | auto_learned | DISABLE |
| 8 | 4 | 1 | project_files | project | permanent | TRUE |
| 9 | 4 | 1 | project_only_memory | project | isolated | TRUE |
| 10 | 7 | 3 | saved_info | global | explicit | TRUE |
| 11 | 7 | 3 | gem_instructions | gem | permanent | TRUE |
| 12 | 7 | 3 | drive_links | gem | live_sync | TRUE |

---

## VIEW: full_platform_config (Denormalized for Reference)

```sql
SELECT 
    a.account_id,
    a.email,
    a.auth_method,
    p.platform_name,
    r.role_name,
    r.specification_tier,
    pc.config_key,
    pc.config_value,
    pc.status
FROM accounts a
JOIN role_platform_assignments rpa ON a.account_id = rpa.account_id
JOIN platforms p ON rpa.platform_id = p.platform_id
JOIN roles r ON rpa.role_id = r.role_id
LEFT JOIN platform_configurations pc ON p.platform_id = pc.platform_id AND a.account_id = pc.account_id
ORDER BY a.account_id, p.platform_name;
```

---

## NOTES

### Foreign Key Relationships
- `account_device_bindings.account_id` → `accounts.account_id`
- `account_device_bindings.device_id` → `devices.device_id`
- `browsers.account_id` → `accounts.account_id`
- `role_platform_assignments.role_id` → `roles.role_id`
- `role_platform_assignments.platform_id` → `platforms.platform_id`
- `role_platform_assignments.account_id` → `accounts.account_id`
- `transitions.from_state_id` → `states.state_id`
- `transitions.to_state_id` → `states.state_id`
- `transitions.via_platform_id` → `platforms.platform_id`

### Change Propagation
When updating a value in a normalized table, all referencing views/queries automatically reflect the change. Examples:
- Update `accounts.email` → All platform bindings show new email
- Update `roles.specification_tier` → All handoff protocols adjust
- Update `platform_configurations.status` → Status dashboard updates

### Export Formats
- **CSV**: Each TABLE section is directly exportable
- **SQLite**: Use CREATE TABLE statements with types inferred from data
- **Airtable**: Each TABLE maps to a base table with linked records
- **Notion**: Each TABLE becomes a database with relations

---

## SYMBOLIC COMPRESSION TARGETS

For future corpus-wide symbolic representation:

| Symbol | Expansion | Usage |
|--------|-----------|-------|
| `$A1` | Account 1 (truongphillipthanh@icloud.com) | References |
| `$A2` | Account 2 (icloud.truongphillipthanh@gmail.com) | References |
| `$A3` | Account 3 (truongphillipthanh@gmail.com) | References |
| `$INT` | INTERPRETER role | Role references |
| `$CMP` | COMPILER role | Role references |
| `$DIG` | DIGESTOR role | Role references |
| `$ORC` | ORACLE role | Role references |
| `$EXE` | EXECUTOR role | Role references |
| `$CW` | Claude Web | Platform references |
| `$GW` | ChatGPT Web | Platform references |
| `$GEM` | Gemini Web | Platform references |
| `$CC` | Claude Code | Platform references |
| `$CDX` | Codex CLI | Platform references |
| `$GCL` | Gemini CLI | Platform references |
| `$FP` | Fingerprint (git hash) | State references |
| `$GT` | Ground Truth (repository) | State references |

---
