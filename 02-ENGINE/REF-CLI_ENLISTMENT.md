---
id: ref-cli_enlistment
kind: reference
scope: engine
target: engine
---

# CLI Tool Enlistment Reference
## Triggering Constellation CLI Tools Programmatically

**Version**: 2.0.0
**Created**: 2026-02-01
**Purpose**: Operational reference for invoking each CLI tool in the Constellation

---

## Commander — Claude Code (Opus 4.5)

**Account**: 1 (Claude Max)
**Trigger**: Native — this is the primary execution surface.

```bash
# Already running. To invoke from scripts:
claude --model opus "directive text here"

# With context file:
claude --model opus --context CLAUDE.md "directive text here"

# Batch mode (non-interactive):
claude --print "task description" | tee output.md
```

**Config**: `CLAUDE.md` (project root), `.claude/settings.json`

---

## Adjudicator — Codex CLI

**Account**: 2 (Claude Pro)
**Trigger**: `codex` command

```bash
# Direct task execution:
codex "implement the function described in SPEC.md"

# With approval mode:
codex --approval-mode suggest "review this PR"

# Batch execution (full-auto):
codex --approval-mode full-auto "run the test suite and fix failures"
```

**Config**: `AGENTS.md` (if present) or Codex will read from context
**Setup**: `npm install -g @openai/codex` (requires OpenAI API key)

---

## Cartographer — Gemini CLI

**Account**: 2 (Google AI Pro)
**Trigger**: `gemini` command

```bash
# Corpus survey (1M context):
gemini --model gemini-2.5-pro "Survey all files in 01-CANON/ for structural inconsistencies"

# With settings file:
gemini --settings 02-ENGINE/gemini-settings.json "analyze corpus"

# Stateless evidence pack generation:
gemini --model gemini-3-flash "Generate token count inventory for 04-SOURCES/"
```

**Config**: `02-ENGINE/gemini-settings.json`, context file: `02-ENGINE/AVATAR-GEMINI-CLI.md`
**Setup**: `npm install -g @anthropic/gemini-cli` (requires Google AI API key)

---

## Psyche — OpenClaw (GPT-5.2, M4 MBA)

**Account**: Local (no API key needed for OpenClaw)
**Trigger**: Task file in `agents/psyche/inbox/` + filesystem watcher

```bash
# From Commander, dispatch a task:
bash 00-ORCHESTRATION/scripts/dispatch.sh psyche "TOPIC" "Task description..."

# Psyche watches agents/psyche/inbox/pending/ for TASK-*.md files
# On the M4 MBA, start the watcher:
bash 00-ORCHESTRATION/scripts/watch_dispatch.sh psyche
```

**Config**: OpenClaw config on M4 MBA
**Protocol**: See `DYN-TWIN_COORDINATION_PROTOCOL.md`

---

## Ajna — OpenClaw (Opus 4.5, M1 Mini)

**Account**: Local
**Trigger**: Task file in `agents/ajna/inbox/` + filesystem watcher

```bash
# From any agent, dispatch a task to Ajna:
bash 00-ORCHESTRATION/scripts/dispatch.sh ajna "TOPIC" "Task description..."

# On the M1 Mini, start the watcher:
bash 00-ORCHESTRATION/scripts/watch_dispatch.sh ajna
```

**Config**: OpenClaw config on M1 Mini
**Protocol**: See `DYN-TWIN_COORDINATION_PROTOCOL.md`

---

## Orchestration Patterns

### Sequential Pipeline
```bash
# Commander analyzes → Cartographer surveys → Adjudicator implements
claude --print "analyze the codebase structure" > analysis.md
gemini "survey 01-CANON/ using analysis from analysis.md"
codex "implement changes based on survey results"
```

### Parallel Execution
```bash
# Commander + Adjudicator in parallel (different branches)
claude --print "refactor module A" &
codex "refactor module B" &
wait
```

### Autonomous Twin Loop
```bash
# Commander dispatches to Psyche, continues working
bash 00-ORCHESTRATION/scripts/dispatch.sh psyche \
  "QA_REVIEW" \
  "Review all files modified in the last commit for quality issues"
# Commander continues with other work...
# Psyche processes and writes results to agents/psyche/outbox/
```

---

## Enlistment Checklist

| Tool | Installed | API Key | Config | Status |
|------|-----------|---------|--------|--------|
| Claude Code (Commander) | Yes | Claude Max (A1) | CLAUDE.md | ACTIVE |
| Codex CLI (Adjudicator) | Yes | OpenAI (A2) | AGENTS.md | CONFIGURE |
| Gemini CLI (Cartographer) | Yes | Google AI Pro (A2) | gemini-settings.json | CONFIGURE |
| OpenClaw/Ajna | Yes | Local | openclaw config | ACTIVE |
| OpenClaw/Psyche | Yes | Local | openclaw config | ACTIVE |

### Missing Infrastructure
- [x] Codex CLI AGENTS.md configuration file
- [ ] Gemini CLI API key setup on Account 2
- [x] `fswatch` on primary machine (Sovereign confirmed)
- [ ] launchd plist for always-on dispatch watching
- [ ] MCP server configuration for cross-tool data sharing

---

## Cross-References

- `README.md` — Constellation overview and platform configs
- `02-ENGINE/gemini-settings.json` — Gemini CLI settings template
- `00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md` — Twin coordination
- `02-ENGINE/DYN-COORDINATION.yaml` — Platform coordination state
