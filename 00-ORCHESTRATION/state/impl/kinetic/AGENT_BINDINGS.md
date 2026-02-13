# AGENT_BINDINGS — Constellation Agent App-Action Bindings

**Version**: 1.0.0
**Author**: Commander (Claude Opus 4.6)
**Date**: 2026-02-11
**Agents**: 6 (Sovereign, Ajna, Psyche, Commander, Adjudicator, Cartographer)
**Total**: 126 bindings

---

## Agent Binding Table

| agent_code | app_slug | action_code | binding_strength | invocation_method | frequency | notes |
|------------|----------|-------------|-----------------|-------------------|-----------|-------|
| sovereign | obsidian | capture_text | primary | gui | constant | Primary knowledge capture interface |
| sovereign | obsidian | modify_file | primary | gui | frequent | Direct note editing in vault |
| sovereign | obsidian | keyword_search | primary | gui | frequent | Vault search for decision context |
| sovereign | brave-browser | browse_web | primary | gui | frequent | Web research and information gathering |
| sovereign | brave-browser | capture_url | primary | gui | frequent | Bookmark strategic references |
| sovereign | slack | send_message | primary | gui | frequent | Team and external communication |
| sovereign | slack | compose_message | primary | gui | frequent | Draft communications |
| sovereign | discord | send_message | secondary | gui | periodic | Community engagement |
| sovereign | things3 | dispatch_task | primary | gui | frequent | Personal task management |
| sovereign | things3 | prioritize | primary | gui | frequent | Daily priority decisions |
| sovereign | things3 | commit_to | primary | gui | frequent | Accept obligations with deadlines |
| sovereign | notion | capture_text | secondary | gui | periodic | Supplementary knowledge capture |
| sovereign | notion | generate_report | secondary | gui | periodic | Report viewing and annotation |
| sovereign | linear | post_update | secondary | gui | periodic | Review and update Linear issues |
| sovereign | clickup | post_update | secondary | gui | periodic | Review T1b task status |
| sovereign | figma | render_markdown | secondary | gui | rare | Design review and annotation |
| sovereign | obsidian | approve | primary | gui | frequent | Sovereign authorization gate via vault decisions |
| sovereign | things3 | decline | primary | gui | periodic | Refuse obligations via task rejection |
| sovereign | things3 | renegotiate | primary | gui | periodic | Modify commitment terms via task updates |
| sovereign | obsidian | allocate_attention | primary | gui | constant | Direct cognitive resources via vault planning |
| sovereign | obsidian | set_boundary | primary | gui | periodic | Define operational limits in vault notes |
| commander | claude-code | run_inference | primary | cli | constant | Primary reasoning engine |
| commander | claude-code | modify_file | primary | cli | constant | File editing via Edit tool |
| commander | claude-code | dispatch_task | primary | cli | frequent | Subagent and team dispatch |
| commander | claude-code | run_script | primary | cli | constant | Bash command execution |
| commander | claude-code | coordinate_agents | primary | cli | frequent | Multi-agent coordination |
| commander | claude-code | code_review | primary | cli | frequent | Code analysis and review |
| commander | claude-code | generate_report | primary | cli | frequent | Structured report generation |
| commander | claude-code | research_synthesize | primary | cli | frequent | Multi-source research |
| commander | claude-code | clarescence | primary | cli | periodic | Decision space refinement |
| commander | obsidian | capture_text | primary | mcp | frequent | Vault writes via Obsidian MCP |
| commander | obsidian | keyword_search | primary | mcp | frequent | Vault search via MCP |
| commander | obsidian | modify_file | primary | mcp | frequent | Note editing via MCP |
| commander | linear | post_update | primary | mcp | frequent | T1a issue management via MCP |
| commander | linear | query_database | primary | mcp | frequent | Issue queries via GraphQL |
| commander | linear | dispatch_task | secondary | mcp | periodic | Issue creation as task proxy |
| commander | clickup | post_update | primary | mcp | periodic | T1b task updates via MCP |
| commander | clickup | query_database | primary | mcp | periodic | Task queries via API |
| commander | git | push_code | primary | cli | frequent | Code commits and pushes |
| commander | git | merge_changes | primary | cli | periodic | Branch management |
| commander | git | check_integrity | primary | cli | constant | Status verification |
| commander | git | audit_trail | primary | cli | constant | Commit log management |
| commander | gh | push_code | secondary | cli | periodic | PR creation and management |
| commander | gh | code_review | secondary | cli | periodic | PR review operations |
| commander | ripgrep | keyword_search | primary | cli | constant | Codebase text search |
| commander | fzf | browse_filesystem | secondary | cli | frequent | Fuzzy file finding |
| commander | tmux | switch_context | primary | cli | frequent | Pane and session management |
| commander | tmux | coordinate_agents | secondary | cli | periodic | Multi-pane workspace ops |
| commander | airtable | query_database | secondary | mcp | periodic | Structured data queries |
| commander | docker-desktop | sandbox_operation | secondary | cli | periodic | Container-based isolation |
| commander | docker-desktop | health_check | secondary | cli | periodic | Service health monitoring |
| adjudicator | codex-cli | run_inference | primary | cli | constant | Primary reasoning via GPT-5.3-codex |
| adjudicator | codex-cli | modify_file | primary | cli | constant | File editing in full-auto mode |
| adjudicator | codex-cli | run_script | primary | cli | frequent | Command execution |
| adjudicator | codex-cli | validate_schema | primary | cli | frequent | Schema and data validation |
| adjudicator | codex-cli | lint_code | primary | cli | frequent | Code quality enforcement |
| adjudicator | git | push_code | primary | cli | frequent | Commit and push completed work |
| adjudicator | git | check_integrity | primary | cli | constant | Working tree verification |
| adjudicator | git | audit_trail | secondary | cli | frequent | Commit log entries |
| adjudicator | neovim | modify_file | secondary | cli | periodic | Direct file editing when needed |
| adjudicator | neovim | refactor_code | secondary | cli | periodic | Code restructuring |
| adjudicator | neovim | lint_code | secondary | cli | periodic | LSP diagnostics |
| adjudicator | ripgrep | keyword_search | primary | cli | constant | Pattern search for validation |
| adjudicator | ripgrep | check_integrity | secondary | cli | frequent | Reference verification |
| adjudicator | fd | browse_filesystem | primary | cli | frequent | Fast file discovery |
| adjudicator | bat | render_markdown | secondary | cli | frequent | Syntax-highlighted file review |
| adjudicator | bat | browse_filesystem | secondary | cli | frequent | File content inspection |
| adjudicator | codex-cli | run_tests | primary | cli | frequent | Test suite execution via Codex CLI |
| adjudicator | codex-cli | check_integrity | primary | cli | frequent | Data integrity verification via Codex CLI |
| cartographer | gemini-cli | run_inference | primary | cli | constant | Primary reasoning via Gemini 2.5 Pro |
| cartographer | gemini-cli | corpus_survey | primary | cli | frequent | Long-context vault surveys |
| cartographer | gemini-cli | summarize | primary | cli | frequent | Document distillation |
| cartographer | gemini-cli | research_synthesize | primary | cli | frequent | Multi-source synthesis |
| cartographer | gemini-cli | extract_entities | primary | cli | periodic | Entity extraction from corpora |
| cartographer | obsidian | keyword_search | secondary | mcp | frequent | Vault search for survey context |
| cartographer | obsidian | capture_text | secondary | mcp | periodic | Survey result persistence |
| cartographer | ripgrep | keyword_search | primary | cli | constant | Codebase content search |
| cartographer | fd | browse_filesystem | primary | cli | frequent | File discovery for surveys |
| cartographer | git | check_integrity | secondary | cli | periodic | Repo state verification |
| cartographer | git | audit_trail | secondary | cli | periodic | History analysis |
| cartographer | perplexity | browse_web | secondary | api | periodic | Web research for intelligence |
| cartographer | perplexity | research_synthesize | secondary | api | periodic | External source synthesis |
| psyche | openclaw | run_inference | primary | api | constant | GPT-5.3-codex via OpenClaw gateway |
| psyche | openclaw | coordinate_agents | primary | api | frequent | Agent management via OpenClaw |
| psyche | openclaw | dispatch_task | primary | api | frequent | Task routing through gateway |
| psyche | openclaw | send_message | primary | api | frequent | Inter-agent messaging |
| psyche | git | push_code | secondary | cli | periodic | Commit system cohesion changes |
| psyche | git | check_integrity | secondary | cli | frequent | Repo state verification |
| psyche | obsidian | modify_file | secondary | mcp | periodic | Vault writes via MCP adapter |
| psyche | obsidian | keyword_search | secondary | mcp | periodic | Vault search for policy context |
| psyche | openclaw | trigger_webhook | secondary | api | periodic | Automation triggers via OpenClaw (Make/Zapier) |
| psyche | openclaw | schedule_cron | secondary | api | rare | Automation scheduling via OpenClaw |
| psyche | openclaw | pipeline_fusion | primary | api | periodic | Pipeline wiring via OpenClaw integration |
| psyche | openclaw | run_script | secondary | cli | frequent | System cohesion scripts via OpenClaw |
| psyche | openclaw | health_check | secondary | cli | periodic | Service monitoring via OpenClaw |
| ajna | openclaw | run_inference | primary | api | constant | Kimi K2.5 via NVIDIA NIM API |
| ajna | openclaw | coordinate_agents | primary | api | frequent | Strategic dispatch optimization |
| ajna | openclaw | dispatch_task | secondary | api | periodic | Strategic task routing |
| ajna | git | push_code | secondary | cli | periodic | MBA-side commits |
| ajna | git | check_integrity | secondary | cli | frequent | MBA repo state verification |
| ajna | obsidian | keyword_search | experimental | mcp | rare | Vault search (MBA MCP pending) |
| ajna | openclaw | clarescence | secondary | api | periodic | Strategic decision refinement via OpenClaw |
| ajna | openclaw | prioritize | primary | api | frequent | Strategic priority reordering via OpenClaw |
| ajna | openclaw | allocate_attention | secondary | api | periodic | Macro attention allocation via OpenClaw |
| ajna | openclaw | research_synthesize | secondary | api | periodic | Strategic research synthesis via OpenClaw |
| ajna | openclaw | blitzkrieg_dispatch | experimental | api | rare | Parallel multi-agent strategic dispatch via OpenClaw |
