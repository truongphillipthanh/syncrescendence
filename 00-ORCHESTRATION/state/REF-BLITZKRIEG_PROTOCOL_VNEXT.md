# BLITZKRIEG PROTOCOL vNEXT
## Multi-Lane Parallel Execution with Cross-Platform Return

**Version**: 2.0.0
**Created**: 2026-01-18
**Authority**: Oracle13
**Status**: Constitutional Reference

---

## OVERVIEW

Blitzkrieg vNext is a formalized workflow for parallel execution across multiple AI toolchains. The protocol captures decisions from the originating platform (typically ChatGPT/Deviser), spawns parallel execution lanes (A/B/C), and generates return artifacts pasteable back into the originating thread.

### Workflow Summary

```
DEVISER (ChatGPT)                    REPOSITORY                         EXECUTION
─────────────────                    ──────────                         ─────────
Decision Snapshot  ──────────►  /blitzkrieg_issue  ──────────►  Lane A (claude_code)
     │                               │                         Lane B (codex_cli)
     │                               │                         Lane C (gemini_cli)
     │                               ▼
     │                         Bundle Created
     │                         -OUTGOING/YYYYMMDD-blitzkrieg-<slug>/
     │                               │
     │                               ▼
     │                         Lanes Execute
     │                               │
     │                               ▼
     ◄───────────────────────  /blitzkrieg_finalize
   merged_return_packet.md           │
   audized scripts                   │
   agent relay JSON                  │
```

---

## ARTIFACT DEFINITIONS

### 1. CONTEXT (`context.md`)

The decision snapshot from the originating Deviser thread. Contains:
- Session identity (Oracle number, platform, timestamp)
- Current state summary
- Key decisions made in this thread
- Constraints and boundaries

**Purpose**: Provides shared situational awareness across all lanes.

### 2. PEDIGREE (`pedigree.md`)

Historical lineage and accumulated decisions. Contains:
- Oracle lineage (0 → N)
- Active decisions from current session
- Constitutional reminders
- Critical file references

**Purpose**: Ensures continuity with prior work and prevents drift.

### 3. INTENTION_ARCHAEOLOGY (Reference)

Snapshot or reference to `ARCH-INTENTION_COMPASS.md` and `DYN-BACKLOG.md`.

**Purpose**: Grounds execution in Principal's intentions.

### 4. DIRECTIVES (`directive-A.md`, `directive-B.md`, `directive-C.md`)

Parallel task specifications with lane-specific metadata.

**Required Headers**:
```yaml
Lane: A | B | C
Toolchain: claude_code | codex_cli | gemini_cli | chatgpt | other
Model: opus-4.5 | sonnet-4.5 | haiku | gemini-2.0-flash | gpt-4o | <custom>
Thinking: ultrathink | megathink | think | default
Success_Criteria: [Measurable completion conditions]
Inputs: [Files/artifacts this lane reads]
Outputs: [Files/artifacts this lane produces]
```

### 5. EXECUTION_LOGS (`lane-A/`, `lane-B/`, `lane-C/`)

Per-lane execution records. Each contains:
- `execution_log.md` — Human-readable narrative
- `execution_log.json` — Structured data for agent relay
- Output artifacts produced by the lane

### 6. RETURN_PACKET (`merged_return_packet.md`)

Consolidated summary for pasting back into the originating Deviser thread.

**Structure**:
```markdown
BLITZKRIEG RETURN: <slug> | <date>

EXECUTION SUMMARY
[What each lane accomplished]

WHAT CHANGED
[Concrete changes made to repository]

WHAT REMAINS
[Incomplete work, blockers, deferrals]

NEXT ACTIONS
[Prioritized follow-up tasks]

ATTACHMENTS TO CARRY FORWARD
[Files that must be referenced in continuation]
```

**Critical**: No preamble. First line must be the BLITZKRIEG RETURN header.

### 7. AUDIO SCRIPTS (`07_audio/`)

TTS-optimized versions following `audizer.md` protocol:
- `audized_context.txt` — Context as audio script
- `audized_pedigree.txt` — Pedigree as audio script
- `audized_return_packet.txt` — Return packet as audio script

**Requirements** (per audizer.md):
- NO markdown syntax (no `**bold**`, no `## headers`, no `` `code` ``)
- NO preamble/postscript
- Capitalized signposts (SECTION:, TRANSITION:, NOTE:)
- Punctuation for breath pauses
- Preserve semantic content and metaphor

### 8. AGENT RELAY JSON (`08_agent_relay/`)

Structured data for LLM-to-LLM handoff:
- `return_packet.json` — Merged summary in JSON
- `lane-A.json`, `lane-B.json`, `lane-C.json` — Per-lane structured logs

---

## NAMING AND FOLDER SCHEMA

### Bundle Root
```
-OUTGOING/YYYYMMDD-blitzkrieg-<slug>/
```

Where:
- `YYYYMMDD` = Date (e.g., 20260118)
- `<slug>` = Operator-provided identifier (e.g., `platform-expand`, `iic-complete`)

### Internal Structure
```
-OUTGOING/YYYYMMDD-blitzkrieg-<slug>/
├── 00_manifest/
│   ├── environment.md
│   ├── git_state.txt
│   └── inputs_used.md
├── 01_context/
│   └── context.md
├── 02_pedigree/
│   └── pedigree.md
├── 03_intention/
│   ├── intention_snapshot.md   (or)
│   └── intention_reference.md
├── 04_directives/
│   ├── directive-A.md
│   ├── directive-B.md
│   └── directive-C.md
├── 05_execution/
│   ├── lane-A/
│   │   ├── execution_log.md
│   │   └── execution_log.json
│   ├── lane-B/
│   │   └── ...
│   └── lane-C/
│       └── ...
├── 06_return_to_webapp/
│   └── merged_return_packet.md
├── 07_audio/
│   ├── audized_context.txt
│   ├── audized_pedigree.txt
│   └── audized_return_packet.txt
└── 08_agent_relay/
    ├── return_packet.json
    ├── lane-A.json
    ├── lane-B.json
    └── lane-C.json
```

---

## LANE MODEL

### Lane Designations

| Lane | Primary Use | Default Toolchain |
|------|-------------|-------------------|
| **A** | Strategic/architectural work | claude_code (Opus) |
| **B** | Tactical execution | claude_code (Sonnet) or codex_cli |
| **C** | Validation/secondary work | gemini_cli or claude_code (Haiku) |

### Toolchain Options

| Toolchain | Description | Model Options |
|-----------|-------------|---------------|
| `claude_code` | Claude Code CLI | opus-4.5, sonnet-4.5, haiku |
| `codex_cli` | OpenAI Codex CLI | codex, gpt-4o |
| `gemini_cli` | Google Gemini CLI | gemini-2.0-flash, gemini-pro |
| `chatgpt` | ChatGPT web app | gpt-4o, gpt-4o-mini |
| `other` | Custom toolchain | <operator-specified> |

### Thinking Levels

| Level | Tokens | Use When |
|-------|--------|----------|
| `ultrathink` | ~32K | Architectural synthesis, complex multi-file changes |
| `megathink` | ~10K | Moderate complexity, multi-step reasoning |
| `think` | ~4K | Standard deliberation |
| `default` | auto | Let model self-regulate |

---

## COMMAND REFERENCE

### /blitzkrieg_issue

**Purpose**: Create bundle skeleton and directive templates.

**Inputs**: Operator provides `<slug>` argument.

**Actions**:
1. Create bundle directory: `-OUTGOING/YYYYMMDD-blitzkrieg-<slug>/`
2. Generate `00_manifest/` with environment info
3. Create template `01_context/context.md` (operator fills in)
4. Create template `02_pedigree/pedigree.md` (operator fills in)
5. Create `03_intention/intention_reference.md` pointing to compass/backlog
6. Create directive templates `04_directives/directive-{A,B,C}.md`
7. Create empty `05_execution/lane-{A,B,C}/` directories
8. Create placeholders for `06_return_to_webapp/`, `07_audio/`, `08_agent_relay/`

### /blitzkrieg_finalize

**Purpose**: Validate and generate return artifacts.

**Inputs**: Path to existing bundle (auto-detected or specified).

**Actions**:
1. Validate required files exist (context.md, pedigree.md, at least one directive)
2. Validate directive headers are complete
3. Generate `06_return_to_webapp/merged_return_packet.md`
4. Generate `07_audio/` scripts (audizer-compliant)
5. Generate `08_agent_relay/` JSON files
6. Report completion status

---

## RETURN-TO-WEBAPP PASTE CONTRACT

The `merged_return_packet.md` must be directly pasteable into the Deviser thread.

### Requirements

1. **No preamble**: First character must be the start of content
2. **No closing remarks**: End with actionable content, not "Let me know if..."
3. **Clear header**: First line identifies the blitzkrieg
4. **Scannable structure**: Sections clearly labeled
5. **Actionable closure**: Ends with NEXT ACTIONS or ATTACHMENTS

### Template

```markdown
BLITZKRIEG RETURN: <slug> | <date>

LANES EXECUTED
Lane A (<toolchain>/<model>): <one-line summary>
Lane B (<toolchain>/<model>): <one-line summary>
Lane C (<toolchain>/<model>): <one-line summary>

EXECUTION SUMMARY
<2-3 paragraphs describing what was accomplished>

WHAT CHANGED
- <file or artifact>: <change description>
- <file or artifact>: <change description>

WHAT REMAINS
- <incomplete item>
- <blocker>

NEXT ACTIONS
1. <immediate priority>
2. <second priority>
3. <third priority>

ATTACHMENTS TO CARRY FORWARD
- <filename>: <why needed>
- <filename>: <why needed>
```

---

## AUDIZER COMPLIANCE

Audio scripts in `07_audio/` must strictly follow `audizer.md`:

### Forbidden
- `**bold**`, `_italics_`, `### headers`
- `` `code blocks` ``
- `> blockquotes`
- Preambles like "Here is the script"
- Postscripts like "Let me know if you need changes"

### Required
- UPPERCASE signposts: `SECTION:`, `TRANSITION:`, `NOTE:`
- Sequential numbering for lists: "First... Second... Third..."
- Punctuation for breath: commas and periods liberally
- Preserve semantic content and domain terminology

### Example Transformation

**Input (markdown)**:
```markdown
## Lane A: Strategic Architecture
- **Completed**: CANON-25200 update
- Remaining: Cross-IIC testing
```

**Output (audized)**:
```
SECTION: LANE A. STRATEGIC ARCHITECTURE.
First, completed: CANON twenty-five two hundred update.
Second, remaining: Cross I-I-C testing.
```

---

## AGENT RELAY JSON SCHEMA

### return_packet.json

```json
{
  "type": "blitzkrieg_return",
  "version": "2.0.0",
  "blitzkrieg_id": "YYYYMMDD-blitzkrieg-<slug>",
  "generated": "ISO8601 timestamp",
  "git_head": "commit hash",
  "lanes": {
    "A": {
      "toolchain": "claude_code",
      "model": "opus-4.5",
      "status": "completed|in_progress|blocked",
      "summary": "one-line summary"
    },
    "B": { ... },
    "C": { ... }
  },
  "execution_summary": "paragraph",
  "what_changed": ["item1", "item2"],
  "what_remains": ["item1", "item2"],
  "next_actions": ["action1", "action2"],
  "attachments": ["file1", "file2"]
}
```

### lane-X.json

```json
{
  "type": "blitzkrieg_lane_execution",
  "version": "2.0.0",
  "lane": "A",
  "blitzkrieg_id": "YYYYMMDD-blitzkrieg-<slug>",
  "directive_id": "DIRECTIVE-XXX",
  "toolchain": "claude_code",
  "model": "opus-4.5",
  "thinking": "ultrathink",
  "status": "completed",
  "inputs": ["file1", "file2"],
  "outputs": ["file1", "file2"],
  "success_criteria": "criteria text",
  "success_achieved": true,
  "execution_notes": "narrative"
}
```

---

## INTEGRATION WITH /deviser_reint

Blitzkrieg bundles complement `/deviser_reint` continuity exports:

1. **Session Archaeology**: `/deviser_reint` should reference recent blitzkrieg folders
2. **Artifact Manifest**: Blitzkrieg return packets can be listed in artifacts manifest
3. **Ground Truth**: Both write to `-OUTGOING/` with dated folders

**Recommended Workflow**:
1. Issue blitzkrieg with `/blitzkrieg_issue`
2. Execute lanes
3. Finalize with `/blitzkrieg_finalize`
4. Paste `merged_return_packet.md` into Deviser thread
5. If ending session, run `/deviser_reint` for full continuity export

---

## VALIDATION RULES

### /blitzkrieg_issue Validation

- [ ] Slug is provided and valid (alphanumeric + hyphens)
- [ ] `-OUTGOING/` exists
- [ ] No duplicate bundle exists (or append suffix)

### /blitzkrieg_finalize Validation

- [ ] `01_context/context.md` exists and non-empty
- [ ] `02_pedigree/pedigree.md` exists and non-empty
- [ ] At least one `04_directives/directive-*.md` exists
- [ ] Each directive has all required headers
- [ ] Lane execution logs exist for claimed lanes

---

## ERROR HANDLING

### Missing Context
```
ERROR: 01_context/context.md not found or empty.
Populate with decision snapshot from Deviser thread.
```

### Missing Pedigree
```
ERROR: 02_pedigree/pedigree.md not found or empty.
Populate with Oracle lineage and active decisions.
```

### Invalid Directive Headers
```
ERROR: directive-A.md missing required header: Toolchain
Required: Lane, Toolchain, Model, Thinking, Success_Criteria, Inputs, Outputs
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-18 | Initial protocol (02-OPERATIONAL/BLITZKRIEG_PROTOCOL.md) |
| 2.0.0 | 2026-01-18 | vNext with 3-lane model, audio scripts, agent relay JSON |

---

*This document is a constitutional reference. Modifications require Principal approval.*
