# Environment Manifest
**Generated**: 2026-01-17 14:45 UTC
**Mode**: READ-ONLY + PROPOSAL (APPLY not armed)

## Git State
- **HEAD**: `35b0f97375e48f5bd58cd0025eb7dda34879761d`
- **Branch**: main
- **Working Tree Status**: Modified and untracked files present

### Staged/Modified Files
```
 M .DS_Store
 D 00-ORCHESTRATION/EXECUTION_LOG-2026-01-15-046B.md
 M 00-ORCHESTRATION/state/DYN-TREE.md
```

### Untracked Files (significant)
```
?? .tmp.driveupload/
?? 00-ORCHESTRATION/execution_logs/EXECUTION_LOG-2026-01-15-046B.md
?? 02-OPERATIONAL/THREAD_HANDOFF_ORACLE13_SUNSET.md
?? 02-OPERATIONAL/prompts/canonical/PROMPT-IMEP-*.md
?? 02-OPERATIONAL/prompts/canonical/STATION_PROMPTS_REGISTRY.md
?? DIRECTIVE-046A.md
?? DIRECTIVE-046B.md
?? INTERACTION_PARADIGM.md
?? ORACLE13_CONTEXT.md
?? OUTGOING/
?? SOURCES_ANALYSIS_REPORT.md
?? "Stop Using Claude Code Like This (Use Sub-Agents Instead).md"
?? "Why I Stopped Using MCPs in Claude Code (And What I Use Instead).md"
?? agents/
?? checklist.md
?? claudecode/
?? clitool/
?? codex/
?? cowork/
?? deviser1_continuity.md
?? frontier_models.md
?? oracle_memories.md
?? oracle_process_archaelogy.md
?? oracle_verification_manifest.md
?? platform_features.md
?? previous_thread.md
?? promptengineering/
?? rapport_contract.md
```

## Tool Availability
| Tool | Path | Version |
|------|------|---------|
| ripgrep (rg) | /opt/homebrew/bin/rg | 15.1.0 |
| fd | /opt/homebrew/bin/fd | 10.3.0 |
| tree | /opt/homebrew/bin/tree | 2.2.1 |
| python3 | /opt/homebrew/bin/python3 | 3.14.2 |
| node | /opt/homebrew/bin/node | available |

## APPLY Status
**APPLY is NOT armed.**

File `APPLY_DEFRAG_APPROVAL.txt` does not exist at repo root.
To arm APPLY, create the file with contents: `I_APPROVE_DEFRAG_APPLY`

## Observations
1. **Root pollution**: 30+ untracked files at repo root, many are orphaned working docs
2. **Execution log misplacement**: Log deleted from wrong location, recreated in proper location
3. **New directories at root**: `agents/`, `claudecode/`, `codex/`, `cowork/`, `promptengineering/` violate flat principle
4. **Outgoing bundles**: Multiple teleology passes accumulated, some zipped
5. **Temporary files**: `.tmp.driveupload/` exists (Drive sync artifact)
