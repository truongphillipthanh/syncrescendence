# Resolution Pass: Answers to Outstanding Questions

## Q1: Why Shouldn't We Use Memories?

**Short Answer**: You SHOULD use memories, but strategically by layer.

**Detailed Analysis**:

### Claude Memories: USE THEM
- **Project-Specific Memory**: Enabled. Let Claude learn patterns from your interactions within the Syncrescendence project. This accumulates useful context like "Principal prefers architectural diagrams as ASCII" without you explicitly teaching.
- **Global User Preferences**: Configured. Your cognitive profile (AuDHD architecture, coherence-first processing) lives here and applies across all projects.
- **Past Chat Search**: Essential. This is how Claude maintains continuity across sessions without you re-explaining everything.

### ChatGPT Memories: DISABLE GLOBAL, USE PROJECT-ONLY
- **Global Memory**: DISABLE. This is the source of the "memory regression" problem—ChatGPT's global memory overrides project context unpredictably in GPT-5.x. For the COMPILER role, you need deterministic behavior, not accumulated assumptions.
- **Project-Only Memory**: ENABLE. Within the Compiler project, let it learn that you want fenced code blocks, that directives follow a specific format, that ambiguity should halt compilation.

### Gemini Memories: EXPLICIT SAVED INFO
- **Saved Info**: USE for explicit persistent preferences ("Always use YAML for evidence packs", "Optimize for TTS when digesting").
- **Gem Instructions**: USE. These are the per-role configurations.
- No passive learning like ChatGPT—Gemini only remembers what you explicitly tell it to remember.

### The Pattern
```
INTERPRETER (Claude): Rich memory (helps rapport and continuity)
COMPILER (ChatGPT): Isolated memory (prevents contamination)
DIGESTOR (Gemini): Explicit memory (controlled persistence)
ORACLE (CLI): No memory (ensures fresh sensing)
```

---

## Q2: Does Codex Have CODEX.md or AGENTS.md?

**Answer**: Yes, Codex CLI uses **AGENTS.md** as its configuration file.

### Comparison:
| CLI Tool | Config File | Location | Hierarchy |
|----------|-------------|----------|-----------|
| Claude Code | CLAUDE.md | Repo root + ~/.claude/ | 5-hop recursion from repo root |
| Codex CLI | AGENTS.md | Repo root | Single file, no hierarchy |
| Gemini CLI | None | ~/.gemini/config | API config only, no instructions |

### AGENTS.md Structure (Codex)
```markdown
# AGENTS.md

## Project Overview
[Brief description of Syncrescendence]

## Coding Standards
[How code should be written]

## GitHub Integration
- PR conventions
- Commit message format
- Branch naming

## Execution Patterns
[How Codex should approach tasks]
```

### Key Difference from CLAUDE.md
- CLAUDE.md supports hierarchical loading (parent directories, 5 hops)
- AGENTS.md is flat—one file at repo root
- Codex is more GitHub-integrated; AGENTS.md emphasizes repo conventions
- Claude Code has extended thinking triggers; Codex has headless mode focus

---

## Q3: What Files Should Be Uploaded to Each Platform's Project/RAG?

### Claude Web Project Knowledge

| File | Purpose | Priority |
|------|---------|----------|
| COCKPIT.md | System overview, 30,000ft view | REQUIRED |
| constellation-teleology.md | Why each component exists | REQUIRED |
| memory-architecture-teleology.md | Memory layer rationale | REQUIRED |
| CONFIGURATION_REGISTRY.md | Normalized platform configs | REQUIRED |
| ARCH-FRONTIER_MODELS_2026-01.md | Model capability reference | RECOMMENDED |
| ARCH-PLATFORM_FEATURES_2026-01.md | Platform feature reference | RECOMMENDED |
| active-handoff-tokens/ (last 3) | Recent state for continuity | ROLLING |

**Rationale**: Claude is the INTERPRETER—it needs comprehensive architectural context to synthesize effectively. Past chat search handles thread continuity; Project Knowledge handles structural knowledge.

### ChatGPT Web Project Files

| File | Purpose | Priority |
|------|---------|----------|
| handoff-token-active.txt | Current state (replaced each handoff) | REQUIRED |
| compile-templates.md | Formatting templates | REQUIRED |
| CHATGPT_COMPILER_HANDOFF.md | Role + CLI awareness | REQUIRED |
| directive-template.md | Directive format reference | RECOMMENDED |

**Rationale**: ChatGPT is the COMPILER—it needs templates and the current handoff, nothing more. Excess context increases risk of interpretation when you want mechanical transformation. Keep it minimal and explicit.

**DO NOT UPLOAD to ChatGPT**:
- Teleology documents (too much interpretive context)
- Research documents (unnecessary for compilation)
- Multiple handoff tokens (only active one matters)

### Gemini Web Gem Knowledge

| File | Purpose | Priority |
|------|---------|----------|
| COCKPIT.md | System overview | REQUIRED |
| digest-templates.md | Output format templates | REQUIRED |
| (Drive Link) Constellation-State/ | Live-synced state files | REQUIRED |

**Rationale**: Gemini is the DIGESTOR—it needs to understand the system well enough to clarify it, plus templates for consistent output. The magic is the Drive link: state auto-syncs without manual upload.

**Drive Folder Contents** (auto-synced via rclone):
```
Constellation-State/
├── tokens/
│   └── active.json
├── state/
│   └── current.yaml
└── context/
    └── recent-decisions.md
```

### Gemini CLI (No RAG—Stateless)

Gemini CLI receives context via command arguments, not persistent files. Each invocation includes:
- Corpus manifest (file listing)
- Survey query
- Output format specification

### Grok Web (No Projects)

Grok has no project/memory system. Context must be provided each conversation:
- Paste the grok-red-team-instructions.md content
- Paste the specific proposal to attack

### Perplexity Web (No Projects)

Similar to Grok—stateless queries with complete context in each message.

---

## Q4: Watch Folder Architecture for Multi-Agent Orchestration

### The Problem
Currently, triggering Claude Code (x3), Codex CLI, and Gemini CLI requires:
1. Principal manually opening each CLI
2. Principal pasting directive into each
3. Principal monitoring each for completion

This doesn't scale.

### Proposed Solution: Hazel + Watch Folders

```
Repository Structure:
├── .dispatch/
│   ├── claude-lead/        # Watched for Account 3 Claude Code
│   │   └── pending/
│   │   └── processing/
│   │   └── complete/
│   ├── claude-parallel-a/  # Watched for Account 2 Claude Code (instance 1)
│   ├── claude-parallel-b/  # Watched for Account 2 Claude Code (instance 2)
│   ├── codex/              # Watched for Codex CLI
│   └── gemini/             # Watched for Gemini CLI
```

### Hazel Rules (per watch folder)

**Rule: claude-lead-pickup**
```
Folder: .dispatch/claude-lead/pending/
Condition: File added, extension is .md
Action: 
  1. Move to processing/
  2. Run shell script: claude-code-execute.sh
  3. On completion, move to complete/
```

**Shell Script: claude-code-execute.sh**
```bash
#!/bin/bash
DIRECTIVE_FILE="$1"
LOG_FILE="00-ORCHESTRATION/logs/execution-log.md"

# Extract directive content
CONTENT=$(cat "$DIRECTIVE_FILE")

# Invoke Claude Code headlessly
claude -p "$CONTENT" --output-format json > /tmp/claude-output.json

# Log result
echo "$(date -Iseconds) | $(basename $DIRECTIVE_FILE) | COMPLETE" >> "$LOG_FILE"

# Move output to -OUTGOING
cp /tmp/claude-output.json -OUTGOING/
```

### Orchestration Flow

```
1. ChatGPT (COMPILER) produces Blitzkrieg directive
2. Principal downloads, drops into -INBOX/
3. Dispatcher (manual or automated) routes to .dispatch/[agent]/pending/
4. Hazel detects new file, triggers execution script
5. CLI executes, outputs to -OUTGOING/
6. Hazel detects completion, moves directive to complete/
7. Principal (or Claude Web) reviews -OUTGOING/
```

### Stream Deck Integration

| Button | Action | Target |
|--------|--------|--------|
| Dispatch Lead | Move -INBOX/*.md to .dispatch/claude-lead/pending/ | Keyboard Maestro |
| Dispatch Parallel | Split and distribute to parallel-a and parallel-b | Keyboard Maestro |
| Dispatch Codex | Move to .dispatch/codex/pending/ | Keyboard Maestro |
| Dispatch Gemini | Move to .dispatch/gemini/pending/ | Keyboard Maestro |
| Status Check | Show pending/processing/complete counts | AppleScript |

### TextExpander Snippets

| Abbreviation | Expansion |
|--------------|-----------|
| `;htoken` | Current handoff token template |
| `;directive` | Directive template with placeholders |
| `;blitz` | Blitzkrieg header template |
| `;compile` | Compilation request template |

---

## Q5: Handoff Documentation Protocol

### Should We Document Handoffs?

**Yes**, but efficiently. Two levels:

### Level 1: Inline (Always)
Every artifact includes a header comment:
```
---
handoff: HANDOFF-20260120-143022-p1-to-p2
fingerprint: 7a3f9c2e
from: claude_web
to: chatgpt_web
timestamp: 2026-01-20T14:30:22Z
---
```

### Level 2: Log (Cumulative)
A rolling log maintained by Claude Code:
```
00-ORCHESTRATION/logs/handoff-log.csv

timestamp,handoff_id,from,to,fingerprint,artifact,status
2026-01-20T14:30:22Z,HANDOFF-20260120-143022-p1-to-p2,claude_web,chatgpt_web,7a3f9c2e,spec-001.md,COMPLETE
2026-01-20T14:45:11Z,HANDOFF-20260120-144511-p2-to-p3,chatgpt_web,gemini_web,8b4e1a9f,directive-001.md,COMPLETE
```

### Who Maintains the Log?

**Option A**: Claude Code appends on each commit (via git hook)
**Option B**: ChatGPT includes log entry in each compilation (copy-paste to log)
**Option C**: n8n workflow triggered by file changes (automated)

**Recommendation**: Start with Option A (git hook), graduate to Option C when volume warrants.

---

## Q6: Long Horizon Context for ChatGPT

### The Concern
ChatGPT is good at long horizon work, but:
- It can't search past chats
- Memory is unreliable in Projects
- How do we relay enough context?

### The Solution: Self-Contained Handoffs + Templates

Every handoff to ChatGPT includes:
1. **Complete context** (not references to past conversations)
2. **Template library** (in Project Files, always available)
3. **Active token** (current state, replaced each handoff)

ChatGPT doesn't need to remember—it needs to receive complete specifications each time. The COMPILER role is explicitly designed for this: stateless transformation of complete inputs.

### For Multi-Session Projects

If a compilation spans multiple ChatGPT sessions:
1. Use **Canvas** (persists across sessions)
2. Include session continuity marker:
```
CONTINUATION FROM: [previous session timestamp]
CURRENT STATE: [description]
REMAINING TASKS: [list]
```
3. Principal maintains the thread (don't start new chat mid-compilation)

---

## Q7: Slash Commands and Semantic Heuristics

### Proposed Slash Command Registry

| Command | Platform | Effect |
|---------|----------|--------|
| `/blitz` | ChatGPT | Enter Blitzkrieg mode, expect parallel streams |
| `/compile [type]` | ChatGPT | Begin compilation of specified type |
| `/directive [target]` | ChatGPT | Format directive for target CLI |
| `/handoff [next]` | All Web | Prepare output for specified platform |
| `/token` | Claude Web | Generate/display current handoff token |
| `/status` | Claude Web | Show constellation state summary |
| `/compact` | Claude Code | Compress thread context |
| `/memory` | Claude Code | Show current memory state |
| `/survey [query]` | Gemini CLI | Execute corpus survey |

### TextExpander Implementation

Each slash command can be a TextExpander snippet that expands to the full invocation pattern:

`;/blitz` → 
```
BLITZKRIEG MODE ACTIVATED
========================
Expecting parallel directive streams.
Format: Stream A (Lead), Stream B (Parallel), Stream C (Codex)
Synchronization point: [SPECIFY]
```

### Stream Deck Visual Feedback

LED colors indicate state:
- 🟢 Green: Platform ready
- 🟡 Yellow: Processing
- 🔴 Red: Error/attention needed

---

## Summary: Resolution Pass Complete

### Configured ✓
- Claude Project Instructions (x3 accounts)
- ChatGPT Project Instructions (x3 accounts)  
- Gemini Gem Instructions (x2 accounts)

### To Configure
- ChatGPT Project-Only Memory mode
- Gemini Drive folder link
- rclone sync
- Hazel watch folders
- Stream Deck buttons
- TextExpander snippets
- Git hooks

### Artifacts Produced This Session
1. constellation-architecture.jsx (React visualization)
2. CONFIGURATION_REGISTRY.md (normalized schema)
3. grok-red-team-instructions.md
4. CHATGPT_COMPILER_HANDOFF.md (with CLI awareness)
5. This Q&A document

### Next Actions
1. Drop all artifacts into -INBOX/
2. Relay CHATGPT_COMPILER_HANDOFF.md to ChatGPT
3. Have ChatGPT compile initial infrastructure directive
4. Execute via Claude Code
5. Verify watch folder concept
