# DIRECTIVE-042B: MULTI-CLI INTEGRATION
## Stream B Execution for Claude Code Instance 2
**Date**: 2026-01-09
**Priority**: P1
**Projects**: PROJ-012 (Multi-CLI), System Prompt Correction
**Estimated Duration**: 2-3 hours

---

## MISSION

1. Create Gemini CLI configuration files for Syncrescendence integration
2. Correct the system prompt files in 02-ENGINE/prompts/unified/
3. Document multi-CLI coordination protocol

---

## CONTEXT

Read the attached ORACLE11_CONTEXT_BLITZKRIEG.md for full strategic context.

**Critical Finding**: The authoritative system prompts are in synthesis-*.md files from system_prompts.zip. The current unified-prompt files in the repository are INCORRECT versions with different structure.

**Gemini CLI Key Facts**:
- Context file: GEMINI.md (analogous to CLAUDE.md)
- Hierarchical loading: ~/.gemini/GEMINI.md → project root → subdirectories
- MCP configuration: ~/.gemini/settings.json
- Commands: /memory show, /memory refresh, /chat, /help
- Headless mode: `gemini -p "prompt" --output-format json`
- Free tier: 60 req/min, 1,000 req/day with personal Google account
- Models: Gemini 2.5 Pro (1M context), Gemini 3 Pro, Gemini 3 Flash

---

## DELIVERABLES

### 1. GEMINI.md (Project Root Context File)

Create a GEMINI.md file for Syncrescendence that mirrors the structure and intent of CLAUDE.md:

```markdown
# Syncrescendence Knowledge Management System

## Identity
This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are executing directives as part of a multi-CLI coordination system alongside Claude Code instances.

## Constitutional Rules

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06. Do not create unnumbered directories at root.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Sovereign approval for deletions.

### Semantic (ABSOLUTE)
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ → EXTRACT unique value → COMPRESS → DELETE originals. NOT organizational restructuring.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION. State/ and logs/ are living infrastructure—never delete.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify actual state, not execution reports.

### Operational (ABSOLUTE)
7. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

## Directory Structure
- `00-ORCHESTRATION/` — Strategic coordination (directives, logs, state)
- `01-CANON/` — Verified canonical knowledge (PROTECTED)
- `02-ENGINE/` — Functions, prompts, model profiles
- `03-QUEUE/` — Pending items by modal
- `04-SOURCES/` — Source documents (raw/, processed/)
- `05-MEMORY/` — Historical preservation
- `06-EXEMPLA/` — Templates and examples

## Critical Commands
```bash
make verify              # Run all validation checks
make update-ledgers      # Sync CSV ledgers with validation
make sync                # Pull latest, rebase, push
make tree                # Generate current tree
```

## Processing Patterns
- Source intake: See @00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md
- Ledger updates: See @00-ORCHESTRATION/state/REF-STANDARDS.md
- Verification: Run before ANY completion claim

## Gemini-Specific Notes
- Use `/memory show` to verify context loading
- Use `/memory refresh` after any GEMINI.md changes
- Headless mode: `gemini -p "prompt" --output-format json` for scripting
- Checkpoint conversations with `/chat save`

## Coordination with Claude Code
- Gemini CLI operates in parallel with Claude Code instances
- Same repository, same worktrees
- Follow zone ownership per coordination.yaml
- Ledger updates are append-only with row-level locking

## Anti-Patterns (PROHIBITED)
- Creating subdirectories anywhere
- Skipping verification to "save time"
- Deferring ledger updates to "later"
- Claiming integration without grep verification
- Modifying state/ without validation
- Conflicting with Claude Code instance zones
```

### 2. gemini-settings.json (MCP Configuration Template)

```json
{
  "models": {
    "default": "gemini-2.5-pro",
    "reasoning": "gemini-3-pro",
    "fast": "gemini-3-flash"
  },
  "sandbox": {
    "enabled": true,
    "profile": "default"
  },
  "contextFileName": "GEMINI.md",
  "includeDirectories": [],
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-filesystem", "/path/to/syncrescendence"],
      "enabled": true
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-github"],
      "enabled": true,
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  },
  "theme": "dark",
  "telemetry": false
}
```

### 3. MULTI_CLI_COORDINATION.md

```markdown
# MULTI-CLI COORDINATION PROTOCOL
## Syncrescendence Parallel Execution Framework

### Available CLI Tools

| Tool | Location | Capability | Status |
|------|----------|------------|--------|
| Claude Code 1 | iTerm Alpha | Full agentic execution | Active |
| Claude Code 2 | iTerm Beta | Full agentic execution | Active |
| Claude Code 3 | iTerm Gamma | Full agentic execution | Active |
| Gemini CLI | iTerm (any) | Full agentic execution | Validating |

### Context File Mapping

| CLI | Context File | Location |
|-----|--------------|----------|
| Claude Code | CLAUDE.md | Project root |
| Gemini CLI | GEMINI.md | Project root + ~/.gemini/ |

### Zone Ownership (per coordination.yaml)

Claude instances operate in designated zones:
- **Alpha**: 04-SOURCES/processed/a-*, execution logs *-A.md
- **Beta**: 04-SOURCES/processed/b-*, execution logs *-B.md
- **Gamma**: 04-SOURCES/processed/c-*, execution logs *-C.md

Gemini CLI follows same zone pattern:
- **Delta**: 04-SOURCES/processed/d-*, execution logs *-D.md

### Parallel Execution Protocol

1. **Same Repository**: All CLIs access same git repository
2. **Worktree Isolation**: Each CLI uses separate worktree (optional)
3. **Branch Strategy**: {instance}/directive-{number}
4. **Merge Target**: develop branch
5. **Conflict Resolution**: Branch per instance, rebase on merge

### Capability Comparison

| Capability | Claude Code | Gemini CLI |
|------------|-------------|------------|
| File operations | ✓ | ✓ |
| Shell commands | ✓ | ✓ |
| Web search | ✓ | ✓ (Google Search) |
| MCP servers | ✓ | ✓ |
| Extended context | 200K | 1M |
| Headless mode | ✓ | ✓ |
| Checkpointing | ✓ (/compact) | ✓ (/chat save) |

### Communication Between Instances

Instances do NOT communicate directly. Coordination happens via:
1. **Git repository**: Shared state through commits
2. **Directive files**: Oracle issues directives
3. **Execution logs**: Each instance reports completion
4. **Ledger files**: Append-only shared state

### Best Practices

1. **Verify context loading**: `/memory show` (Gemini), no equivalent (Claude)
2. **Frequent commits**: Prevents conflict accumulation
3. **Zone discipline**: Stay in assigned zones
4. **Ledger protocol**: Backup → temp file → validate → rename

### Troubleshooting

**Gemini CLI context not loading**:
```bash
gemini
> /memory refresh
> /memory show
```

**Claude Code context not loading**:
- Verify CLAUDE.md exists at project root
- Check .claude/settings.json configuration

**Merge conflicts**:
- Pull before starting work
- Commit frequently
- Use assigned zones
```

### 4. Corrected System Prompts

Extract from system_prompts.zip and copy authoritative files:

**Action**: The following files in 02-ENGINE/prompts/unified/ must be REPLACED:

| Current File | Replace With | Source |
|--------------|--------------|--------|
| Claude-unified-prompt.md | synthesis-claude.md | system_prompts.zip |
| ChatGPT-unified-prompt.md | synthesis-chatgpt.md | system_prompts.zip |
| Gemini-unified-prompt.md | synthesis-gemini.md | system_prompts.zip |
| Grok-unified-prompt.md | synthesis-grok.md | system_prompts.zip |

**Additionally**: Archive justification-*.md files to 05-MEMORY/

---

## EXECUTION STEPS

### Phase 1: System Prompt Correction (45 min)

1. Locate the extracted system_prompts/ directory (from previous Oracle session)
2. If not available, extract from system_prompts.zip attachment
3. Copy authoritative files:
   ```bash
   cp synthesis-claude.md → 02-ENGINE/prompts/unified/Claude-unified-prompt.md
   cp synthesis-chatgpt.md → 02-ENGINE/prompts/unified/ChatGPT-unified-prompt.md
   cp synthesis-gemini.md → 02-ENGINE/prompts/unified/Gemini-unified-prompt.md
   cp synthesis-grok.md → 02-ENGINE/prompts/unified/Grok-unified-prompt.md
   ```
4. Archive justification files:
   ```bash
   cp justification-*.md → 05-MEMORY/
   ```
5. Verify with diff that files are correctly replaced

### Phase 2: GEMINI.md Creation (30 min)

1. Create GEMINI.md at project root
2. Use CLAUDE.md as structural template
3. Add Gemini-specific sections (memory commands, coordination notes)
4. Copy to /mnt/user-data/outputs/

### Phase 3: Settings Template (15 min)

1. Create gemini-settings.json template
2. Document required environment variables
3. Note MCP server options
4. Copy to /mnt/user-data/outputs/

### Phase 4: Coordination Protocol (30 min)

1. Create MULTI_CLI_COORDINATION.md
2. Document capability comparison
3. Define zone ownership for Gemini (Delta zone)
4. Establish best practices
5. Copy to /mnt/user-data/outputs/

### Phase 5: Verification and Output (15 min)

1. Verify all files complete
2. Run diffs on corrected system prompts
3. Copy all deliverables to /mnt/user-data/outputs/
4. Create execution log
5. Update tasks.csv

---

## OUTPUT REQUIREMENTS

All files to: `/mnt/user-data/outputs/`

Files to produce:
1. `GEMINI.md`
2. `gemini-settings.json`
3. `MULTI_CLI_COORDINATION.md`
4. `Claude-unified-prompt.md` (corrected)
5. `ChatGPT-unified-prompt.md` (corrected)
6. `Gemini-unified-prompt.md` (corrected)
7. `Grok-unified-prompt.md` (corrected)
8. `EXECUTION_LOG-2026-01-09-042B.md`

---

## SUCCESS CRITERIA

| Criterion | Verification |
|-----------|--------------|
| System prompts corrected | diff shows correct replacement |
| GEMINI.md complete | All CLAUDE.md sections adapted |
| Settings template valid | JSON validates |
| Coordination protocol documented | All sections present |
| Files in outputs | All 8 files accessible |

---

## LEDGER UPDATES

Add to tasks.csv:
```csv
TASK-053,PROJ-012,Create GEMINI.md context file,task,done,P1,Claude_Code_2,null,0.5,[actual],2026-01-09,2026-01-09,Syncrescendence-adapted for Gemini CLI
TASK-054,PROJ-012,Create gemini-settings.json template,task,done,P2,Claude_Code_2,null,0.25,[actual],2026-01-09,2026-01-09,MCP and model configuration
TASK-055,PROJ-012,Create multi-CLI coordination protocol,task,done,P1,Claude_Code_2,null,0.5,[actual],2026-01-09,2026-01-09,Parallel execution framework
TASK-056,null,Correct unified-prompt files,task,done,P0,Claude_Code_2,null,0.75,[actual],2026-01-09,2026-01-09,4 files replaced from authoritative sources
```

Update projects.csv:
- PROJ-012 status: in_progress
- PROJ-012 updated: 2026-01-09

---

*Execute with precision. Multi-CLI coordination enables scaling execution capacity beyond single-instance limits.*
