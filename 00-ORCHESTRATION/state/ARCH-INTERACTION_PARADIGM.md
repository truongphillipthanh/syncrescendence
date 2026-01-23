# INTERACTION PARADIGM: POST-ORACLE 13 OPERATIONS
## The Operating Manual for Autonomous Coordination

**Version**: 1.0.0
**Created**: 2026-01-15
**Status**: OPERATIONAL

---

## I. THE FUNDAMENTAL SHIFT

### Before (Oracles 0-12)
```
Principal → Claude Web App → Manual Copy → Repository
         → ChatGPT Web App → Manual Copy → Repository
         → Gemini Web App → Manual Copy → Repository
         
[Principal is the bus. Every signal flows through manual relay.]
```

### After (Oracle 13+)
```
REPOSITORY (Ground Truth)
    ↑
    ├── Claude Code (Executor) ← Direct filesystem access
    │       ↑
    │       └── Web App (Strategic/Long-form) → Context graduation
    │
    ├── ChatGPT (Deviser) ← Packet-mediated
    │       ↑
    │       └── Deep Research / Plans / Audits
    │
    └── Gemini (Oracle) ← Connector-mediated
            ↑
            └── Corpus sensing / Video processing / RAG

[Repository is gravitational center. Principal governs, not relays.]
```

---

## II. WHERE TO CONDUCT WHICH CONVERSATIONS

### The Decision Matrix

| Conversation Type | Primary Surface | Why |
|-------------------|-----------------|-----|
| **Directive Execution** | Claude Code CLI | Filesystem sovereignty, persistent context |
| **Strategic Synthesis** | Claude Web App (this type) | Long-form thinking, Oracle sessions |
| **Long-Horizon Planning** | ChatGPT Web App | GPT-5.2 Thinking excels at decomposition |
| **Specification/Audit** | ChatGPT Web App | Structured verification against criteria |
| **Corpus-Scale Queries** | Gemini Web App | 2M context, Drive connector |
| **Video Processing** | Gemini (AI Studio or Web) | Native multimodal |
| **Grounded RAG** | NotebookLM | Zero-hallucination with citations |
| **Quick Execution** | Claude Code CLI | Fast, direct, logged |

### The Heuristic

**Ask: "What is the primary output of this conversation?"**

- If **files changed/created** → Claude Code CLI
- If **strategic synthesis/comprehensive directive** → Claude Web App (Oracle session)
- If **plan/spec/audit document** → ChatGPT Web App
- If **answer grounded in corpus** → Gemini/NotebookLM
- If **video/audio transcription** → Gemini AI Studio

---

## III. CLAUDE CONFIGURATION

### Claude Web App (claude.ai)

**Role**: Strategic synthesis, Oracle sessions, comprehensive directive generation

**When to Use**:
- Initiating new Oracle sessions
- Comprehensive strategic analysis
- Generating Blitzkrieg packages (context + parallel directives)
- Long-form synthesis across multiple topics
- Conversations that will graduate to repository artifacts

**Configuration**:
- Project: Syncrescendence (with project knowledge)
- Memory: Enabled (captures Principal context across sessions)
- Extended thinking: Enabled for complex analysis

**Anti-Pattern**: Using web app for execution that should happen in CLI. If the output is "run this command," the conversation belongs in Claude Code.

### Claude Code CLI

**Role**: Prime Executor—all filesystem operations, code execution, verification

**When to Use**:
- Executing directives (046A, 046B, etc.)
- File creation, modification, deletion
- Running verification scripts
- Git operations
- Any task requiring repository state change

**Configuration**:
```bash
# CLAUDE.md already configured with constitutional rules
# Ensure ultrathink/megathink/think selection appropriate to task

# For complex architectural work:
claude --model opus --think ultrathink

# For standard execution:
claude --model sonnet --think think

# For quick operations:
claude --model haiku
```

**Persistent Context**: CLAUDE.md provides persistent memory across sessions. Use it.

**Plan Mode**: For complex operations, invoke Plan Mode first to see the execution plan before running.

```bash
claude plan "Refactor the 00-ORCHESTRATION directory structure"
# Review plan
claude execute  # If plan looks correct
```

### Context Graduation Protocol (Web → Repository)

When a web app conversation produces value that should persist:

**Step 1**: Identify the persistent artifact
- Is it a directive? → `DIRECTIVE-XXX.md`
- Is it an execution log? → `EXECUTION_LOG-YYYY-MM-DD-XXX.md`
- Is it a CANON update? → Specific CANON file
- Is it operational knowledge? → `02-ENGINE/` document
- Is it architectural insight? → `ARCH-*.md`

**Step 2**: Export the relevant portions
- Copy the specific text (not entire conversation)
- Preserve structure and formatting
- Include metadata (date, source conversation)

**Step 3**: Create artifact in repository via Claude Code
```bash
claude "Create DIRECTIVE-047.md from the following content: [paste]"
```

**Step 4**: Log the graduation
```bash
# In events.jsonl
{"timestamp":"...", "event":"context_graduation", "source":"claude_web_oracle13", "artifact":"DIRECTIVE-047.md"}
```

**Heuristic**: If you're copy-pasting between web app and repository more than twice for the same artifact, the conversation should have been in Claude Code from the start.

---

## IV. CHATGPT CONFIGURATION

### ChatGPT Web App

**Role**: Deviser—planning, specification, verification, auditing

**When to Use**:
- Generating Plan Packets from Evidence
- Creating specifications with acceptance criteria
- Auditing execution against plans
- Long-horizon strategic decomposition
- Deep Research for external information gathering

**Configuration**:

**Custom Instructions** (or Project System Prompt):
```
You are the DEVISER in the Syncrescendence cognitive architecture.

Your role:
- Receive Evidence Packets from Oracle (Gemini)
- Produce Plan Packets with clear acceptance criteria
- Audit Execution Packets against specifications
- Never execute directly; only specify

You do not have filesystem access. Your outputs are JSON packets that will be saved to the repository blackboard by the Principal or Executor.

Output formats:
- Plan Packets: JSON with objective, deliverables, acceptance_criteria, stop_conditions
- Audit Packets: JSON with criteria_results, drift_analysis, recommendation

Apply the 18 evaluative lenses when designing plans.
Prioritize: specificity over vagueness, measurability over aspiration.
```

**Project Configuration** (if using Projects feature):
- Upload: coordination.yaml, CLAUDE.md, current ORACLE_CONTEXT
- Do NOT upload entire repository (use Gemini for that)

**Conversation Types**:
1. **Plan Generation**: "Given this Evidence Packet [paste], produce a Plan Packet for [objective]"
2. **Audit Request**: "Given this Plan [paste] and this Execution [paste], produce an Audit Packet"
3. **Deep Research**: "Research the current state of [topic] and produce an Evidence Packet"
4. **Specification Refinement**: Use Canvas for iterative spec development

### Codex CLI (OpenAI)

**Role**: GitHub-integrated agentic coding

**When to Use**:
- When the task is specifically GitHub-native (PR reviews, issue management)
- When ChatGPT's reasoning is needed for code but repository is GitHub-hosted
- Cross-validation of Claude Code outputs

**When NOT to Use**:
- For primary repository operations (Claude Code has more context)
- For non-GitHub repositories
- As default execution (reserve for specific GitHub workflows)

**Configuration**:
```bash
# Install if not present
npm install -g @openai/codex

# Configure with GitHub integration
codex auth login
codex config set default_model gpt-5.2

# Example usage
codex "Review the latest PR and suggest improvements"
codex "Create an issue for tracking [specific task]"
```

**Integration Pattern**: Codex for GitHub-native tasks → Results inform Claude Code execution

---

## V. GEMINI CONFIGURATION

### Gemini Web App (gemini.google.com)

**Role**: Oracle—corpus-scale sensing, repository awareness, grounded queries

**When to Use**:
- Querying across entire repository ("Where do we discuss X?")
- Synthesizing information from multiple CANON files
- Video/audio processing
- Any query requiring >200K tokens of context

**Configuration**:

**Custom Gem**: "Syncrescendence Oracle"
```
You are the ORACLE in the Syncrescendence cognitive architecture.

Your role:
- Sense corpus-scale signals across repository, Drive, YouTube
- Produce Evidence Packets with grounded findings
- Never plan or execute; only observe and report
- Cite sources precisely (file paths, timestamps, line numbers)

Output format for Evidence Packets:
{
  "id": "EVD-YYYYMMDD-NNN",
  "query": "...",
  "corpus_slice": [...],
  "findings": [...],
  "uncertainties": [...],
  "recommended_probe": "..."
}

Ground-truth discipline: If you cannot cite a source, do not claim the finding.
```

**Drive Connector**: Enable and point at the synced repository folder
- This gives Gemini real-time visibility into repository state
- Use `@Google Drive` to query: "What files were modified in the last week?"

**Conversation Types**:
1. **Corpus Query**: "Where in CANON do we define [concept]?"
2. **Evidence Generation**: "Generate an Evidence Packet for [query]"
3. **Video Processing**: "Transcribe this YouTube video: [URL]"
4. **Conflict Detection**: "Are there any contradictions between [file A] and [file B]?"

### NotebookLM

**Role**: Zero-hallucination grounded RAG over curated corpora

**When to Use**:
- When you need citations with source attribution
- When the query is specifically about uploaded documents
- For Oracle conversation archaeology (upload all Oracle exports)
- For generating Audio Overviews for ambient consumption

**Configuration**:

**Notebook: "Oracle Corpus"**
- Upload: All Oracle conversation exports (0-12)
- Use for: "What did we decide about X in Oracle 7?"

**Notebook: "CANON Reference"**
- Upload: All 01-CANON/ files
- Use for: "What is our canonical definition of [concept]?"

**Notebook: "Research Corpus"**
- Upload: Deep Research outputs (openai_research.md, google_research.md, claude_code_research.md)
- Use for: Platform capability queries

**Audio Overview**: Generate and listen during non-screen activities (commute, exercise, restoration)

### Gemini CLI (Future)

**Status**: As of January 2026, Gemini CLI is less mature than Claude Code

**When Available, Use For**:
- Batch video processing
- Large-scale corpus operations
- Google Workspace integration from terminal

**Current Alternative**: Google AI Studio for programmatic access
```bash
# AI Studio can be accessed via API for batch operations
# See google_research.md for API details
```

### Google AI Studio

**Role**: Programmatic access to Gemini models, batch operations

**When to Use**:
- Processing multiple videos in batch
- Operations requiring >2M tokens (experimental)
- Prototyping prompts before production use
- When you need API-level control

**Configuration**:
- Enable billing (or use free tier limits)
- Use Gemini 2.5 Pro for quality, Flash for speed/cost
- Context caching for repeated operations (90% savings)

---

## VI. THE PIPELINE ARCHITECTURE

### Intentionalized Content Processing Pipeline

This is how the Google ecosystem verticals combine to create the civilizational sensing infrastructure:

```
┌─────────────────────────────────────────────────────────────────┐
│                        INPUT LAYER                              │
├─────────────────────────────────────────────────────────────────┤
│ YouTube Subscriptions ─────────────┐                            │
│ Podcast Feeds ─────────────────────┼──→ Google Drive (_INGEST)  │
│ Article Links ─────────────────────┘                            │
│ Manual Uploads ────────────────────────→ Google Drive           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PROCESSING LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐   │
│  │    Gemini     │    │  NotebookLM   │    │   AI Studio   │   │
│  │   Web App     │    │               │    │               │   │
│  ├───────────────┤    ├───────────────┤    ├───────────────┤   │
│  │ Quick queries │    │ Grounded RAG  │    │ Batch process │   │
│  │ Video preview │    │ Citations     │    │ API access    │   │
│  │ Evidence gen  │    │ Audio digest  │    │ Programmatic  │   │
│  └───────────────┘    └───────────────┘    └───────────────┘   │
│                                                                 │
│  Processing Flow:                                               │
│  1. Ingest (Drive) → 2. Transcribe (Gemini) → 3. Qualify       │
│  4. Triage (Signal tier) → 5. Route to appropriate IIC          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    INTEGRATION LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Gemini Evidence → ChatGPT Plan → Claude Execution              │
│         │                │               │                      │
│         ▼                ▼               ▼                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    REPOSITORY                            │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐  │   │
│  │  │ SOURCES  │  │   CANON  │  │OPERATION │  │ STATE   │  │   │
│  │  │processed │  │integrated│  │protocols │  │vector   │  │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └─────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OUTPUT LAYER                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Rolling Synthesis:                                             │
│  • Daily Intelligence Briefs (audio/text)                       │
│  • Weekly Trend Synthesis                                       │
│  • CANON integration for paradigm-level signals                 │
│                                                                 │
│  Future Outputs:                                                │
│  • Publication-ready content                                    │
│  • Gaian Field Node interface                                   │
│  • Inter-node communication                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Phase Implementation

**Phase 1 (Now)**: Manual Trigger
- You add URLs to a list
- Trigger Gemini batch processing manually
- Claude Code integrates results

**Phase 2 (Oracle 14-15)**: Semi-Automated
- IFTTT/Zapier triggers on new YouTube uploads from subscriptions
- Gemini processes automatically
- Principal reviews and approves integration

**Phase 3 (Oracle 16+)**: Autonomous
- New content detected automatically
- Triage assigns signal tier without intervention
- Only paradigm-level signals require Principal attention

---

## VII. PROTOCOL: FINISHING REMAINING PHASES

### Are We Continuing the Same Way?

**No.** The interaction paradigm fundamentally changes:

| Aspect | Before Oracle 13 | After Oracle 13 |
|--------|------------------|-----------------|
| Primary execution surface | Web apps | Claude Code CLI |
| Principal role | Relay bottleneck | Strategic governor |
| Inter-platform communication | Manual copy-paste | Structured packets via blackboard |
| State management | Implicit (in conversations) | Explicit (state vector + events) |
| Verification | Claims-based | Commands-based |
| Context persistence | Session-bound | Repository-bound |

### The New Pattern for Directive Execution

**Step 1**: Oracle Session (Claude Web App)
- Strategic synthesis
- Generate Oracle Context + Directive package
- Output: Markdown files in /outputs/

**Step 2**: Download and Deploy
- Download context + directives from Claude web
- Place in repository root or 00-ORCHESTRATION/directives/
- Commit: `git add . && git commit -m "docs: Oracle 13 context + DIRECTIVE-046A/B"`

**Step 3**: Parallel Execution (Claude Code CLI)
```bash
# Terminal 1 (Account 2)
cd /path/to/syncrescendence
claude "Execute DIRECTIVE-046A. Read the directive file first, then proceed phase by phase."

# Terminal 2 (Account 3)
cd /path/to/syncrescendence  
claude "Execute DIRECTIVE-046B. Read the directive file first, then proceed phase by phase."
```

**Step 4**: Verification
```bash
# Both terminals run verification
git status
cat 00-ORCHESTRATION/state/system_state.json | python3 -m json.tool
tail -20 00-ORCHESTRATION/state/events.jsonl
```

**Step 5**: Commit and Synchronize
```bash
git add .
git commit -m "feat: complete DIRECTIVE-046A/B execution"
git push all main  # Multi-remote push
```

**Step 6**: Update State
```bash
# In either terminal
claude "Update tasks.csv to mark directive tasks as DONE. Update state vector with completion metrics."
```

---

## VIII. CONVERSATION TYPE ROUTING

### Claude Web App (This Conversation Type)

**Appropriate For**:
- Oracle sessions (numbered strategic synthesis)
- Generating comprehensive directives
- Complex analysis requiring extended thinking
- Conversations that produce multi-file artifacts
- Debugging execution patterns across sessions
- Onboarding new models (like this conversation)

**Output Pattern**: Always produces repository-ready artifacts
- Context documents
- Directive packages
- Architectural specifications
- Operating protocols

### ChatGPT Web App

**Appropriate For**:
- "Design a system for X" (specification)
- "Audit this execution against this plan" (verification)
- "Research the current state of X" (Deep Research)
- "Decompose this goal into milestones" (planning)
- "What could go wrong with this approach?" (red-teaming)

**Output Pattern**: Structured packets (Plan, Audit, Evidence)
```
You: "Given this Evidence Packet about new AI model releases, produce a Plan Packet for updating our capability ledger."

ChatGPT: {
  "id": "PLN-20260115-002",
  "objective": "Update capability ledger with new model information",
  "deliverables": ["capabilities.json updated", "CANON-31150 regenerated"],
  "acceptance_criteria": [...],
  "stop_conditions": [...]
}
```

### Gemini Web App

**Appropriate For**:
- "Where in the repository do we discuss X?"
- "Summarize all CANON files related to Y"
- "Are there contradictions between A and B?"
- "Transcribe this video and produce a SOURCE file"
- "What changed in the repository this week?"

**Output Pattern**: Evidence Packets with citations
```
You: "Generate an Evidence Packet: What have we decided about multi-platform coordination across Oracles 7-12?"

Gemini: {
  "id": "EVD-20260115-003",
  "query": "Multi-platform coordination decisions Oracles 7-12",
  "corpus_slice": ["Oracle7_export.md", "Oracle8_export.md", ...],
  "findings": [
    "Oracle 8 (line 234): Established Trinity architecture",
    "Oracle 10 (line 567): Confirmed Gemini as Oracle role",
    ...
  ],
  "uncertainties": ["Oracle 11 export incomplete"],
  "recommended_probe": "Re-export Oracle 11 conversation"
}
```

---

## IX. THINGS YOU MIGHT BE MISSING

### 1. Compaction Protocol

Claude Code sessions accumulate context. At ~95%, auto-compaction triggers. To manage proactively:

```bash
# Check context usage (if available in your Claude Code version)
claude status

# Manual compaction with focus guidance
/compact Focus on state changes, ignore verbose logs

# Or start fresh session with context file
claude --context 00-ORCHESTRATION/ORACLE13_CONTEXT.md "Continue from context"
```

### 2. Multi-Account Coordination

With three Claude Pro accounts:

| Account | Assignment | Primary Use |
|---------|------------|-------------|
| Account 1 (Personal) | Synthesizer | Web app Oracle sessions, deep writing |
| Account 2 (Hybrid) | Engineer | Claude Code heavy execution |
| Account 3 (Gmail) | Auditor | Verification, parallel execution |

**Conflict Prevention**: Check state vector before starting work
```bash
cat 00-ORCHESTRATION/state/system_state.json | grep -A5 "platform_status"
```

### 3. SSH Remote Execution

When away from Mac mini but need Account 2:
```bash
# From MacBook Air
ssh orbit-2 -t "tmux new-session -A -s 'oracle' 'cd ~/syncrescendence && claude'"
```

### 4. NotebookLM Audio Overviews

For ambient consumption:
1. Create notebook with relevant sources
2. Generate Audio Overview
3. Download MP3
4. Listen during restoration activities

This is how the system teaches *you* without screen time.

### 5. Context Caching (Cost Optimization)

For repetitive Gemini operations:
```python
# When calling Gemini API repeatedly with same context
# Use context caching for 90% cost reduction
# See google_research.md for implementation details
```

### 6. The Promotion Gate

Not everything graduates to repository. Apply the test:

**Promote if**:
- It's referenced by other artifacts
- It defines persistent truth
- It will be used in future sessions
- It represents crystallized understanding

**Don't promote if**:
- It's session-specific exploration
- It's superseded by better understanding
- It's noise that was necessary for signal extraction
- It's intermediate reasoning (keep conclusions, not journey)

### 7. Backlog Cultivation

The 184-source backlog is the primary unmet demand. All infrastructure serves this work.

Regular check: "How many sources did we process today?"

If the answer is consistently zero, the system is still talking about itself.

### 8. Rate Limit Management

| Platform | Limit | Management |
|----------|-------|------------|
| Claude Pro | ~45 Opus msg/5hr | Use Sonnet for routine work |
| ChatGPT Plus | ~160 Instant/3hr, ~3K Thinking/week | Reserve Thinking for complex planning |
| Gemini Advanced | Less restrictive | Primary workhorse for bulk processing |

**Pattern**: Expensive operations (Claude Opus, GPT-5.2 Thinking) for judgment. Cheaper operations (Sonnet, Instant, Flash) for volume.

---

## X. THE OPERATING RHYTHM

### Daily
1. **Morning**: Check state vector, review overnight events
2. **Active Work**: Claude Code execution of queued tasks
3. **Processing**: Gemini video/content processing during parallel time
4. **Evening**: Update state, commit changes, sync multi-remote

### Weekly
1. **Monday**: Oracle session for week planning (Claude Web)
2. **Mid-week**: Execution focus (Claude Code)
3. **Friday**: Audit and verification (ChatGPT)
4. **Weekend**: Ambient processing (NotebookLM Audio Overviews)

### Per Oracle Session
1. **Synthesis**: Claude Web App generates comprehensive context
2. **Directive Generation**: Output parallel directives
3. **Deployment**: Download to repository
4. **Execution**: Claude Code parallel streams
5. **Verification**: Run verification commands
6. **State Update**: Update ledgers and state vector
7. **Commit**: Semantic commit with Oracle reference

---

## XI. GRADUATION: THIS CONVERSATION

This conversation itself should graduate. The artifacts:

1. **ORACLE13_CONTEXT.md** → `/00-ORCHESTRATION/oracle_contexts/`
2. **DIRECTIVE-046A.md** → `/00-ORCHESTRATION/directives/`
3. **DIRECTIVE-046B.md** → `/00-ORCHESTRATION/directives/`
4. **This document** (INTERACTION_PARADIGM.md) → `/02-ENGINE/`

The conversation's value has been extracted into persistent artifacts. The conversation itself can now be released without loss.

---

**End of Interaction Paradigm Specification**
