# APP_ACTIONS — App-to-Action Mappings

**Version**: 1.0.0
**Author**: Commander (Claude Opus 4.6)
**Date**: 2026-02-11
**Coverage**: 40 priority apps mapped to action types
**Total**: 230 rows

---

## App-Action Mapping Table

| app_slug | action_code | quality_rating | is_primary | automation_support | notes |
|----------|-------------|----------------|------------|-------------------|-------|
| obsidian | capture_text | excellent | TRUE | mcp | Primary knowledge capture via vault notes |
| obsidian | persist_file | excellent | TRUE | mcp | Native markdown file persistence |
| obsidian | index_document | good | FALSE | mcp | Frontmatter + Dataview indexing |
| obsidian | keyword_search | excellent | TRUE | mcp | Vault-wide search with Obsidian MCP |
| obsidian | modify_file | excellent | TRUE | mcp | Edit notes via MCP write operations |
| obsidian | render_markdown | excellent | TRUE | native | Native markdown rendering with plugins |
| obsidian | browse_filesystem | good | FALSE | mcp | Vault directory traversal via MCP |
| neovim | modify_file | excellent | TRUE | cli | Primary code editor with LSP integration |
| neovim | refactor_code | excellent | TRUE | cli | LSP-powered refactoring (rename, extract) |
| neovim | lint_code | excellent | TRUE | cli | Integrated linting via conform.nvim/nvim-lint |
| neovim | keyword_search | good | FALSE | cli | Telescope grep integration |
| neovim | merge_changes | good | FALSE | cli | Diffview and fugitive for merge resolution |
| neovim | browse_filesystem | good | FALSE | cli | Oil.nvim and neo-tree file navigation |
| claude-code | run_inference | excellent | TRUE | cli | Primary CLI agent for Opus 4.6 reasoning |
| claude-code | modify_file | excellent | TRUE | cli | Edit tool for targeted file modifications |
| claude-code | dispatch_task | excellent | TRUE | cli | Task tool for subagent dispatch |
| claude-code | run_script | excellent | TRUE | cli | Bash tool for command execution |
| claude-code | semantic_search | good | FALSE | mcp | Via Qdrant/Graphiti MCP servers |
| claude-code | coordinate_agents | excellent | TRUE | cli | Native team and Task tool coordination |
| claude-code | code_review | excellent | TRUE | cli | Inline code analysis and suggestions |
| claude-code | generate_report | excellent | TRUE | cli | Structured output generation |
| cursor | modify_file | excellent | FALSE | native | AI-assisted code editing with Cmd+K |
| cursor | refactor_code | excellent | FALSE | native | AI-powered code refactoring |
| cursor | run_inference | good | FALSE | native | Integrated chat with multiple models |
| cursor | lint_code | good | FALSE | native | LSP integration for diagnostics |
| cursor | code_review | good | FALSE | native | Inline code suggestions and review |
| chatgpt | run_inference | excellent | FALSE | api | GPT-5/5.3-codex via desktop or web |
| chatgpt | summarize | excellent | FALSE | api | Long document summarization |
| chatgpt | research_synthesize | good | FALSE | api | Web-browsing research mode |
| chatgpt | compose_message | good | FALSE | api | Draft messages and communications |
| chatgpt | classify | good | FALSE | api | Content classification and tagging |
| notion | persist_file | good | FALSE | api | Document storage in Notion pages |
| notion | generate_report | good | FALSE | api | Structured report pages with databases |
| notion | post_update | good | FALSE | api | Status updates in Notion databases |
| notion | capture_text | good | FALSE | api | Quick capture via web clipper or API |
| notion | browse_web | basic | FALSE | api | Limited web content embedding |
| linear | post_update | excellent | TRUE | mcp | Primary issue tracker for T1a operations |
| linear | dispatch_task | good | FALSE | mcp | Issue creation as task dispatch |
| linear | track_metrics | good | FALSE | mcp | Cycle time and velocity tracking |
| linear | query_database | good | FALSE | mcp | Issue queries via MCP/GraphQL |
| linear | schedule_workflow | basic | FALSE | mcp | Workflow state automation |
| clickup | post_update | good | FALSE | mcp | T1b task tracking (personal/professional) |
| clickup | dispatch_task | good | FALSE | mcp | Task creation in ClickUp spaces |
| clickup | track_metrics | basic | FALSE | mcp | Basic time and status tracking |
| clickup | query_database | good | FALSE | mcp | Task queries via MCP API |
| git | push_code | excellent | TRUE | cli | Primary VCS for all code operations |
| git | merge_changes | excellent | TRUE | cli | Branch merging and conflict resolution |
| git | archive_content | good | FALSE | cli | Version history as content archive |
| git | check_integrity | good | FALSE | cli | Status, diff, and log verification |
| git | release_version | excellent | TRUE | cli | Tag-based versioning |
| git | audit_trail | excellent | TRUE | cli | Commit log as authoritative audit trail |
| gh | push_code | good | FALSE | cli | PR creation and management |
| gh | code_review | good | FALSE | cli | PR review via gh pr review |
| gh | post_update | good | FALSE | cli | Issue/PR comments and labels |
| gh | query_database | good | FALSE | cli | API queries for repo metadata |
| gh | release_version | good | FALSE | cli | GitHub Releases management |
| lazygit | merge_changes | excellent | FALSE | cli | Visual git merge and rebase interface |
| lazygit | browse_filesystem | good | FALSE | cli | Visual file staging and navigation |
| lazygit | push_code | good | FALSE | cli | Interactive push with branch selection |
| lazygit | check_integrity | good | FALSE | cli | Visual diff and status overview |
| tmux | switch_context | excellent | TRUE | cli | Primary pane/window context switching |
| tmux | coordinate_agents | good | FALSE | cli | Multi-pane agent workspace management |
| tmux | run_script | good | FALSE | cli | Send-keys for script execution in panes |
| tmux | browse_filesystem | basic | FALSE | cli | Pane-based directory navigation |
| ghostty | run_script | excellent | TRUE | native | Primary terminal emulator for all CLI ops |
| ghostty | switch_context | good | FALSE | native | Tab/split-based context switching |
| ghostty | capture_text | basic | FALSE | native | Terminal output capture |
| raycast | execute_macro | excellent | TRUE | native | Primary launcher and macro execution |
| raycast | browse_web | good | FALSE | native | Quick web search and URL launching |
| raycast | switch_context | good | FALSE | native | App switching and window management |
| raycast | capture_text | good | FALSE | native | Clipboard history and snippets |
| raycast | run_script | good | FALSE | scripted | Script commands and extensions |
| figma | render_markdown | basic | FALSE | native | Design artifact presentation |
| figma | compose_message | basic | FALSE | native | Design annotation and commenting |
| figma | capture_screenshot | good | FALSE | native | Design frame export |
| slack | send_message | excellent | TRUE | api | Primary team communication channel |
| slack | notify_agent | good | FALSE | api | Webhook-based agent notifications |
| slack | post_update | good | FALSE | api | Channel updates and thread replies |
| slack | compose_message | good | FALSE | native | Message drafting with formatting |
| discord | send_message | good | FALSE | api | Community communication channel |
| discord | notify_agent | good | FALSE | api | Bot-based notifications |
| discord | post_update | basic | FALSE | api | Channel announcements |
| perplexity | browse_web | excellent | TRUE | api | Primary web research with citations |
| perplexity | research_synthesize | excellent | TRUE | api | Multi-source research synthesis |
| perplexity | summarize | good | FALSE | api | Source-backed summarization |
| perplexity | query_database | good | FALSE | api | Structured knowledge queries |
| gemini-cli | run_inference | excellent | FALSE | cli | Gemini 2.5 Pro reasoning via CLI |
| gemini-cli | corpus_survey | excellent | TRUE | cli | Long-context vault surveys (1M tokens) |
| gemini-cli | summarize | good | FALSE | cli | Document summarization |
| gemini-cli | research_synthesize | good | FALSE | cli | Multi-file synthesis |
| gemini-cli | extract_entities | good | FALSE | cli | Entity extraction from large corpora |
| codex-cli | run_inference | good | FALSE | cli | GPT-5.3-codex via Codex CLI |
| codex-cli | modify_file | good | FALSE | cli | File editing with full-auto mode |
| codex-cli | run_script | good | FALSE | cli | Command execution in sandbox |
| codex-cli | validate_schema | good | FALSE | cli | Schema validation tasks |
| codex-cli | lint_code | good | FALSE | cli | Code quality checks |
| openclaw | run_inference | good | FALSE | api | Multi-model gateway for agent orchestration |
| openclaw | coordinate_agents | good | FALSE | api | Agent management via OpenClaw framework |
| openclaw | dispatch_task | good | FALSE | api | Task routing through gateway |
| openclaw | send_message | good | FALSE | api | Inter-agent messaging via plugins |
| ollama | run_inference | good | FALSE | api | Local model inference (Llama, etc.) |
| ollama | embed_text | good | FALSE | api | Local embedding generation |
| ollama | fine_tune | basic | FALSE | api | Model customization via Modelfile |
| docker-desktop | build_artifact | excellent | TRUE | cli | Container image building and management |
| docker-desktop | release_version | good | FALSE | cli | Image versioning and registry push |
| docker-desktop | health_check | good | FALSE | cli | Container health monitoring |
| docker-desktop | sandbox_operation | excellent | TRUE | cli | Isolated execution environments |
| ripgrep | keyword_search | excellent | FALSE | cli | Ultra-fast content search across codebase |
| ripgrep | check_integrity | good | FALSE | cli | Pattern verification in source files |
| ripgrep | browse_filesystem | basic | FALSE | cli | File listing with pattern matching |
| fzf | browse_filesystem | excellent | TRUE | cli | Fuzzy file and content finder |
| fzf | keyword_search | good | FALSE | cli | Interactive fuzzy search |
| fzf | switch_context | good | FALSE | cli | Quick selection for context switching |
| 1password | manage_credentials | excellent | TRUE | cli | Primary credential vault and manager |
| 1password | rotate_keys | good | FALSE | cli | Password and key rotation |
| 1password | encrypt_data | good | FALSE | native | Secure note and document encryption |
| 1password | audit_trail | good | FALSE | native | Access log and credential audit |
| devonthink | index_document | excellent | FALSE | scripted | Advanced document indexing and AI classification |
| devonthink | archive_content | excellent | TRUE | scripted | Long-term document archival with metadata |
| devonthink | semantic_search | good | FALSE | scripted | AI-powered document search |
| devonthink | capture_url | good | FALSE | scripted | Web archive and clipping |
| devonthink | classify | good | FALSE | scripted | Auto-classification of documents |
| zotero | capture_url | excellent | TRUE | scripted | Academic reference capture and management |
| zotero | index_document | good | FALSE | scripted | Research paper indexing with metadata |
| zotero | archive_content | good | FALSE | scripted | Reference library archival |
| zotero | extract_entities | basic | FALSE | scripted | Citation data extraction |
| airtable | query_database | excellent | TRUE | mcp | Structured data queries via MCP |
| airtable | persist_file | good | FALSE | mcp | Record creation and update |
| airtable | generate_report | good | FALSE | mcp | View-based reporting |
| airtable | track_metrics | good | FALSE | mcp | Dashboard and summary views |
| airtable | classify | good | FALSE | mcp | Multi-select and linked record classification |
| keyboard-maestro | execute_macro | excellent | FALSE | native | Complex multi-step macro automation |
| keyboard-maestro | trigger_webhook | good | FALSE | native | HTTP request actions in macros |
| keyboard-maestro | run_script | good | FALSE | native | Script execution within macros |
| keyboard-maestro | schedule_cron | good | FALSE | native | Time-based macro triggers |
| keyboard-maestro | switch_context | good | FALSE | native | App/window manipulation macros |
| hazel | archive_content | excellent | TRUE | native | Automated file organization and archival |
| hazel | classify | excellent | TRUE | native | Rule-based file classification |
| hazel | run_script | good | FALSE | native | Shell script actions on file events |
| hazel | trigger_webhook | basic | FALSE | native | Notification on file events |
| things3 | dispatch_task | good | FALSE | native | Personal task creation and management |
| things3 | schedule_workflow | good | FALSE | native | Project and area organization |
| things3 | prioritize | good | FALSE | native | Today/upcoming priority management |
| things3 | commit_to | good | FALSE | native | Task acceptance and deadline setting |
| brave-browser | browse_web | excellent | FALSE | native | Primary web browser with privacy |
| brave-browser | capture_url | good | FALSE | native | Bookmark and reading list capture |
| brave-browser | research_synthesize | basic | FALSE | native | Tab-based multi-source research |
| brave-browser | capture_screenshot | good | FALSE | native | Full-page and region screenshots |
| sesh | switch_context | excellent | FALSE | cli | tmux session management and switching |
| sesh | coordinate_agents | basic | FALSE | cli | Session-based agent workspace navigation |
| sesh | browse_filesystem | basic | FALSE | cli | Session directory navigation |
| starship | render_markdown | basic | FALSE | native | Shell prompt context rendering |
| starship | health_check | basic | FALSE | native | Git status and env indicators in prompt |
| whisper-cpp | capture_audio | excellent | TRUE | cli | Primary speech-to-text transcription |
| whisper-cpp | transform_text | good | FALSE | cli | Audio-to-text format conversion |
| whisper-cpp | extract_entities | basic | FALSE | cli | Keyword spotting in transcriptions |
| bat | render_markdown | good | FALSE | cli | Syntax-highlighted file viewing |
| bat | browse_filesystem | good | FALSE | cli | File content preview with line numbers |
| bat | keyword_search | basic | FALSE | cli | Highlighted search result display |
| fd | browse_filesystem | excellent | FALSE | cli | Fast file finding by name/pattern |
| fd | keyword_search | basic | FALSE | cli | Filename-based search |
| fd | check_integrity | basic | FALSE | cli | File existence verification |
| yazi | browse_filesystem | excellent | FALSE | cli | Terminal file manager with preview |
| yazi | switch_context | good | FALSE | cli | Directory navigation and switching |
| yazi | persist_file | basic | FALSE | cli | File move/copy/rename operations |
| yazi | capture_screenshot | basic | FALSE | cli | Image preview in terminal |
| atuin | audit_trail | excellent | TRUE | cli | Shell command history with context |
| atuin | keyword_search | good | FALSE | cli | Fuzzy search across command history |
| atuin | query_database | good | FALSE | cli | SQLite-backed history queries |
