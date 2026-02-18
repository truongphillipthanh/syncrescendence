# WORKFLOW_TEMPLATES — Executable Workflow Definitions

**Version**: 1.0.0
**Author**: Commander (Claude Opus 4.6)
**Date**: 2026-02-11
**Templates**: 11 (6 existing apparatus + 5 new)
**Steps**: 72

---

## Templates Table

| code | name | description | apparatus_code | use_frequency | avg_duration_minutes |
|------|------|-------------|----------------|---------------|---------------------|
| wf_research | Research & Synthesis | Multi-source research with structured synthesis output | research_apparatus | frequent | 45 |
| wf_writing | Writing & Publishing | Draft, refine, review, and publish written content | writing_apparatus | frequent | 60 |
| wf_coding | Software Development | Implement, test, review, and deploy code changes | coding_apparatus | constant | 90 |
| wf_design | Design & Creation | Create, iterate, and finalize design artifacts | design_apparatus | periodic | 120 |
| wf_analysis | Data Analysis | Collect, process, analyze, and present data insights | analysis_apparatus | frequent | 30 |
| wf_communication | Communication & Collaboration | Draft, review, send, and follow up on communications | communication_apparatus | constant | 15 |
| wf_orchestration | Agent Orchestration | Dispatch, coordinate, and collect results from multiple agents | | constant | 20 |
| wf_sensing | Sensing & Intelligence | Detect changes, ingest signals, classify, and route to handlers | | frequent | 10 |
| wf_deployment | Build & Deployment | Build artifacts, run checks, version, and deploy to targets | | periodic | 30 |
| wf_maintenance | System Maintenance | Health check, diagnose, fix, and verify system components | | periodic | 25 |
| wf_clarescence | Clarescence Protocol | Multi-pass progressive refinement of a decision space | | periodic | 40 |

---

## Steps Table

| workflow_code | step_number | app_slug | action_description | input_from_previous | output_to_next | avg_duration_minutes | notes |
|---------------|-------------|----------|-------------------|---------------------|----------------|---------------------|-------|
| wf_research | 1 | obsidian | Define research question and scope in vault note | none | research brief | 5 | Capture objective and boundaries |
| wf_research | 2 | perplexity | Search web for primary sources with citations | research brief | source list | 10 | Use focused queries from brief |
| wf_research | 3 | gemini-cli | Deep-read and extract entities from long sources | source list | extracted data | 10 | Leverage 1M token context |
| wf_research | 4 | claude-code | Synthesize findings into structured analysis | extracted data | synthesis draft | 10 | Cross-reference multiple sources |
| wf_research | 5 | obsidian | Persist synthesis as canonical vault document | synthesis draft | vault document | 5 | Apply frontmatter and tags |
| wf_research | 6 | git | Commit research artifact with semantic prefix | vault document | committed file | 2 | docs: or feat: prefix |
| wf_research | 7 | linear | Update relevant SYN issue with research outcome | committed file | issue updated | 3 | Link commit to issue |
| wf_writing | 1 | obsidian | Create draft document with outline structure | none | outline | 5 | Use templates for structure |
| wf_writing | 2 | claude-code | Generate first draft from outline and context | outline | first draft | 15 | Provide relevant vault context |
| wf_writing | 3 | neovim | Edit and refine draft for voice and precision | first draft | refined draft | 15 | Human-in-the-loop editing |
| wf_writing | 4 | claude-code | Review for coherence, style, and completeness | refined draft | review notes | 10 | Check against standards |
| wf_writing | 5 | neovim | Apply final edits from review feedback | review notes | final draft | 10 | Sovereign review if needed |
| wf_writing | 6 | git | Commit final document to repository | final draft | committed file | 2 | docs: prefix |
| wf_writing | 7 | obsidian | Cross-link document to related vault notes | committed file | linked document | 3 | Update backlinks and tags |
| wf_coding | 1 | claude-code | Analyze requirements and design implementation plan | none | implementation plan | 10 | Read relevant code first |
| wf_coding | 2 | claude-code | Implement code changes across target files | implementation plan | code changes | 30 | Edit tool for precise modifications |
| wf_coding | 3 | codex-cli | Run test suite and validate changes | code changes | test results | 10 | Adjudicator validation |
| wf_coding | 4 | ripgrep | Verify no broken references or orphaned code | test results | integrity report | 5 | grep for removed identifiers |
| wf_coding | 5 | neovim | Manual review and refinement of edge cases | integrity report | reviewed code | 15 | Human review for complex changes |
| wf_coding | 6 | git | Stage and commit with semantic message | reviewed code | commit | 5 | feat:/fix:/refactor: prefix |
| wf_coding | 7 | gh | Create PR if branch-based workflow | commit | pull request | 5 | Include test evidence |
| wf_coding | 8 | linear | Update SYN issue status and link commit | pull request | issue updated | 5 | Close or advance issue |
| wf_design | 1 | obsidian | Capture design brief and requirements | none | design brief | 10 | Reference existing patterns |
| wf_design | 2 | figma | Create initial design mockups and wireframes | design brief | mockups | 40 | Iterate on layout and hierarchy |
| wf_design | 3 | claude-code | Review design against system patterns and constraints | mockups | design feedback | 15 | Check consistency with Canon |
| wf_design | 4 | figma | Refine design based on feedback | design feedback | refined design | 30 | Apply systematic corrections |
| wf_design | 5 | obsidian | Document design decisions and rationale | refined design | design doc | 15 | Persist to vault |
| wf_design | 6 | git | Commit design documentation | design doc | committed file | 5 | docs: prefix |
| wf_design | 7 | linear | Update project issue with design artifacts | committed file | issue updated | 5 | Link to design files |
| wf_analysis | 1 | airtable | Query structured data from relevant bases | none | raw data | 5 | Use MCP for queries |
| wf_analysis | 2 | claude-code | Process and transform data for analysis | raw data | processed data | 5 | Clean and normalize |
| wf_analysis | 3 | claude-code | Run analytical queries and compute metrics | processed data | analysis results | 10 | Statistical summaries |
| wf_analysis | 4 | claude-code | Generate structured report with findings | analysis results | analysis report | 5 | Markdown tables and charts |
| wf_analysis | 5 | obsidian | Persist analysis report to vault | analysis report | vault document | 3 | Apply appropriate tags |
| wf_analysis | 6 | git | Commit analysis artifact | vault document | committed file | 2 | docs: or feat: prefix |
| wf_communication | 1 | obsidian | Draft communication content and key points | none | draft content | 3 | Reference relevant context |
| wf_communication | 2 | claude-code | Refine message for audience and channel | draft content | refined message | 3 | Adjust tone and format |
| wf_communication | 3 | slack | Send message to appropriate channel or DM | refined message | sent message | 2 | Or discord/email as needed |
| wf_communication | 4 | linear | Log communication outcome if project-relevant | sent message | logged event | 2 | Update issue if applicable |
| wf_communication | 5 | obsidian | Archive significant communications in vault | logged event | archived record | 3 | For decisions and agreements |
| wf_communication | 6 | atuin | Command history preserves execution context | archived record | history entry | 2 | Automatic via shell integration |
| wf_orchestration | 1 | claude-code | Assess task scope and decompose into subtasks | none | task decomposition | 3 | Identify parallelizable work |
| wf_orchestration | 2 | claude-code | Dispatch tasks to appropriate agents via inbox | task decomposition | dispatched tasks | 3 | Use dispatch.sh or Task tool |
| wf_orchestration | 3 | tmux | Monitor agent panes for progress signals | dispatched tasks | progress signals | 5 | Visual monitoring across panes |
| wf_orchestration | 4 | claude-code | Collect and integrate results from agents | progress signals | integrated results | 5 | Read RESULT/CONFIRM files |
| wf_orchestration | 5 | git | Commit integrated results | integrated results | committed files | 2 | Merge agent contributions |
| wf_orchestration | 6 | linear | Update tracking with orchestration outcome | committed files | issues updated | 2 | Close or advance issues |
| wf_sensing | 1 | ripgrep | Scan filesystem for new or changed signals | none | change list | 2 | Monitor inbox and state files |
| wf_sensing | 2 | claude-code | Classify signal type and urgency | change list | classified signals | 2 | Route P0 immediately |
| wf_sensing | 3 | obsidian | Log signal to appropriate dynamic ledger | classified signals | ledger entry | 2 | DYN-GLOBAL_LEDGER.md |
| wf_sensing | 4 | claude-code | Route actionable signals to handler agents | ledger entry | dispatched actions | 2 | Trigger workflows or tasks |
| wf_sensing | 5 | linear | Create issue if signal warrants T1a tracking | dispatched actions | issue created | 2 | P0/P1 signals only |
| wf_deployment | 1 | claude-code | Verify all changes committed and tests passing | none | readiness check | 3 | Pre-deployment validation |
| wf_deployment | 2 | docker-desktop | Build container image or artifact package | readiness check | build artifact | 5 | Versioned build |
| wf_deployment | 3 | codex-cli | Run deployment validation suite | build artifact | validation results | 5 | Schema, lint, integrity checks |
| wf_deployment | 4 | git | Tag release version and push | validation results | tagged release | 3 | Semantic versioning |
| wf_deployment | 5 | gh | Create GitHub release with changelog | tagged release | published release | 5 | Include build artifacts |
| wf_deployment | 6 | claude-code | Verify deployment health post-release | published release | health report | 5 | Run health checks |
| wf_deployment | 7 | linear | Close deployment issue and update project | health report | issue closed | 4 | Link release to issue |
| wf_maintenance | 1 | claude-code | Run health checks across all services | none | health report | 3 | 8 services + launchd agents |
| wf_maintenance | 2 | docker-desktop | Check container status and resource usage | health report | container status | 3 | Neo4j, Graphiti, Qdrant |
| wf_maintenance | 3 | claude-code | Diagnose any failing services or anomalies | container status | diagnosis | 5 | Root cause analysis |
| wf_maintenance | 4 | claude-code | Apply fixes for diagnosed issues | diagnosis | fixes applied | 8 | Restart, config change, patch |
| wf_maintenance | 5 | codex-cli | Verify fixes and run regression checks | fixes applied | verification report | 4 | Adjudicator validation |
| wf_maintenance | 6 | git | Commit maintenance changes | verification report | committed fixes | 2 | fix: prefix |
| wf_clarescence | 1 | claude-code | Orient and situate: read Triumvirate, git status, inbox | none | orientation context | 5 | Pass 0: mandatory grounding |
| wf_clarescence | 2 | claude-code | Calibrate against intentions and verify current state | orientation context | calibration data | 5 | Pass 1: Triumvirate Calibration |
| wf_clarescence | 3 | claude-code | Run 18-lens sweep scoring pass/fail per lens | calibration data | lens scores | 8 | Pass 2: require >= 12/18 |
| wf_clarescence | 4 | obsidian | Check Canon coherence and flag stale documents | lens scores | coherence report | 5 | Pass 3: Canon alignment |
| wf_clarescence | 5 | claude-code | Run remaining passes based on fidelity level | coherence report | analysis results | 10 | Passes 4-10 as needed |
| wf_clarescence | 6 | obsidian | Write clarescence record to impl/clarescence/ | analysis results | clarescence record | 5 | Structured markdown artifact |
| wf_clarescence | 7 | git | Commit clarescence record | clarescence record | committed file | 2 | docs: prefix |
