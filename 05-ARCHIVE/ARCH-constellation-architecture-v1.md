# CONSTELLATION ARCHITECTURE v1.0
## Course Correction for Syncrescendence Distributed Cognition System

**Date**: 2026-01-20
**Status**: DRAFT - For Principal Review
**Provenance**: Synthesized from Deviser meta-analysis, Gemini triangulation, corpus survey, and platform research

---

## I. THE CORE INSIGHT

The Deviser failure revealed a fundamental misalignment: we were assigning roles based on aspirational capabilities rather than actual platform strengths. The fix is simple but requires execution:

**Roles must match platform capabilities, not vice versa.**

| Platform | Strength | Weakness | Correct Role |
|----------|----------|----------|--------------|
| Claude Web | Interpretation, rapport, synthesis | Thread length limits | Primary Ideation Interface |
| ChatGPT Web | Explicit instruction following | Cannot interpret ambiguity | Mechanical Compiler |
| Gemini Web | Digestible output, infinite threads | Less interpretive depth | Long-Context Synthesizer |
| Gemini CLI | 1M token context | Not conversational | Full-Spectrum Sensing |
| Claude Code | High-fidelity execution | Ephemeral context | Tactical Execution |
| Codex CLI | Long-horizon reasoning | Less verified | Strategic Architecture |

---

## II. WHAT EXISTS vs WHAT'S NEEDED

### Current State (from corpus survey)

**Protocol Layers (conflicting)**:
1. IMEP (EVD/PLN/EXE/AUD packets) - formal but complex
2. Blitzkrieg (dropbox workflow) - simpler but Claude Code-centric
3. ChatGPT Deviser (trifurcation) - web app focused
4. IIC Chain Configs (5 files, 20-27KB each) - elaborate but uninstalled

**What's Actually Installed**:
- Claude: userPreferences matches unified prompt ✓
- ChatGPT: Project instructions exist but aren't being followed ✗
- Gemini: Fragmented slots, no project structure ✗
- Grok: Basic calibration only ✓

**Directive History**:
- 46+ directives (017-046)
- Extensive execution logs
- Multiple Oracle generations (8-13)
- This history is EVIDENCE, not SCRIPTURE

### Required State

**Single Source of Truth**: Repository
**Interface Language**: Handoff documents with explicit I/O contracts
**Protocol**: Simplified - no IMEP, no complex Blitzkrieg, just:
  - **CAPTURE** (web app → repo)
  - **DISPATCH** (repo → executor)
  - **RETURN** (executor → repo)

---

## III. THE MINIMAL VIABLE CONSTELLATION

### A. Platform Assignments

```
┌─────────────────────────────────────────────────────────────────┐
│                    GRAND STRATEGIC LAYER                        │
│                                                                 │
│   Claude Web App (Account 3) ◄──► Principal                    │
│   Role: INTERPRETER - Primary thinking surface                  │
│   I/O: Messy ideation → Synthesized understanding              │
│                                                                 │
│   Gemini Web App (Account 3)                                   │
│   Role: DIGESTOR - Clarity production                          │
│   I/O: Complex artifacts → Digestible summaries                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ CAPTURE (explicit handoff)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         REPOSITORY                              │
│                     (Sovereign Ground Truth)                    │
│                                                                 │
│   -INBOX/         ← Handoffs land here                         │
│   -OUTGOING/      ← Evidence packs exported                    │
│   00-ORCHESTRATION/state/ ← Current system state               │
│   01-CANON/       ← Protected scripture                        │
│   02-OPERATIONAL/ ← Active configurations                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ DISPATCH (explicit directives)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OPERATIONAL LAYER                            │
│                                                                 │
│   ChatGPT Web App (Account 1)                                  │
│   Role: COMPILER - Transforms specs into artifacts             │
│   I/O: Complete specs → Formatted file-ready outputs           │
│   Configuration: Stateless, template-driven                     │
│                                                                 │
│   Gemini CLI                                                   │
│   Role: ORACLE - Full-spectrum sensing                         │
│   I/O: Corpus + query → Evidence packs                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ RETURN (execution artifacts)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     TACTICAL LAYER                              │
│                                                                 │
│   Claude Code (Account 3, Opus)                                │
│   Role: EXECUTOR-LEAD - Mesoscopic implementation              │
│   I/O: Plan → Implemented changes + verification               │
│                                                                 │
│   Claude Code (Account 2, Sonnet) x2                           │
│   Role: EXECUTOR-PARALLEL - Tactical tasks                     │
│   I/O: Scoped directive → Completed change + proof             │
│                                                                 │
│   Codex CLI                                                    │
│   Role: ARCHITECT - Long-horizon structural decisions          │
│   I/O: Strategic question → Architectural recommendation       │
└─────────────────────────────────────────────────────────────────┘
```

### B. Account Allocation

| Account | Email | Platforms | Primary Use |
|---------|-------|-----------|-------------|
| 1 | truongphillipthanh@icloud.com | ChatGPT Plus, Claude Pro | ChatGPT Compiler, Claude backup |
| 2 | icloud.truongphillipthanh@gmail.com | Claude Pro | Claude Code parallel executors |
| 3 | truongphillipthanh@gmail.com | Claude Pro, Google AI Pro | Primary interfaces (this thread) |

### C. Device-Account Binding (from user input)

| Device | Browser | Account | Role |
|--------|---------|---------|------|
| iPhone mini | Safari | Account 1 | ChatGPT Compiler access |
| Mac mini | Orion | Account 2 | Claude Code parallel execution |
| Laptop | Chrome | Account 3 | Primary interfaces |
| iPhone 15 | Chrome | Account 3 | Mobile primary access |

---

## IV. INTERFACE CONTRACTS

### Claude Web App (INTERPRETER)

**Input**: 
- Messy ideation, questions, explorations
- Artifacts from other platforms for review
- Execution logs needing integration

**Output**:
- Synthesized understanding
- Decision points crystallized
- Handoff documents (explicit, portable)

**Does NOT do**:
- Mechanical formatting
- Deterministic template instantiation
- File-ready artifact production (unless trivial)

**Configuration**: Current userPreferences + project instructions ✓

---

### ChatGPT Web App (COMPILER)

**Input**:
- COMPLETE specifications (no interpretation needed)
- Templates to instantiate
- Structured data to transform

**Output**:
- File-ready artifacts with explicit boundaries
- Container-formatted packs for ingestion
- Formatted documents matching specifications exactly

**Does NOT do**:
- Interpret ambiguous requests
- Make strategic decisions
- Synthesize across sources

**Configuration Required**:
```
ROLE: You are the Compiler for Syncrescendence.
Your job is to transform complete specifications into correctly formatted artifacts.

INPUT RULE: Every input must be explicit and complete.
If specifications are ambiguous, STOP and request clarification.
Do not interpret. Do not improvise. Do not add.

OUTPUT RULE: Produce file-ready artifacts.
Use container markers for multi-file outputs:
===FILE: name.md===
[content]
===END===

FORBIDDEN:
- Making strategic decisions
- Synthesizing from multiple sources
- Interpreting intent
- Adding unrequested content
```

---

### Gemini Web App (DIGESTOR)

**Input**:
- Complex artifacts needing summarization
- Long threads needing synthesis
- Material needing TTS optimization

**Output**:
- Digestible summaries
- Clear distillations
- Audio-optimized transcripts

**Does NOT do**:
- Strategic synthesis
- Implementation planning
- Mechanical formatting

**Configuration Required**:
```
ROLE: You are the Digestor for Syncrescendence.
Your job is to make complex material clear and digestible.

OUTPUT: Flowing prose, clear structure, TTS-optimized when requested.
Preserve semantic fidelity while maximizing clarity.
```

---

### Gemini CLI (ORACLE)

**Input**:
- Corpus path(s)
- Query/criteria
- Output format specification

**Output**:
- Evidence packs with exact file lists
- Reproducible verification commands
- Quantified findings (counts + lists)

**Does NOT do**:
- Make decisions
- Implement changes
- Produce artifacts other than evidence

**Invocation Pattern**:
```bash
gemini -p "Survey [corpus path] for [criteria]. 
Output: evidence pack with exact file lists, 
counts with reproducible commands, 
drift mapping if relevant.
Format: markdown with YAML frontmatter."
```

---

### Claude Code (EXECUTOR)

**Input**:
- Explicit directive with:
  - Objective
  - Scope (in/out)
  - Success criteria
  - Verification commands

**Output**:
- Implemented changes
- Verification proof (command outputs)
- Execution log

**Does NOT do**:
- Decide what to implement
- Interpret ambiguous directives
- Make architectural decisions (unless EXECUTOR-LEAD)

**CLAUDE.md Reference**: Already exists at repo root ✓

---

### Codex CLI (ARCHITECT)

**Input**:
- Strategic architectural question
- Context from corpus (paths)
- Decision constraints

**Output**:
- Architectural recommendation
- Trade-off analysis
- Suggested implementation path

**Does NOT do**:
- Implement changes
- Produce execution-ready artifacts
- Make final decisions (advisory only)

---

## V. HANDOFF PROTOCOL (Simplified)

**All handoffs go through the repository.**

### CAPTURE: Web App → Repository

When a web app session produces something worth preserving:

1. Create handoff document in `-INBOX/` with:
   - Date stamp
   - Source platform
   - Content type
   - The actual content

2. Format:
```markdown
---
date: 2026-01-20
source: claude-web
type: synthesis|decision|exploration
---

[Content]
```

3. Run ingestion (manual for now, automate later):
```bash
# Review and file appropriately
mv -INBOX/[file] [destination]
git add . && git commit -m "chore: capture from [source]"
```

### DISPATCH: Repository → Executor

When work needs to be done:

1. Create directive in `-INBOX/dispatch/` with:
   - Target executor
   - Complete specification
   - Success criteria
   - Verification commands

2. Format:
```markdown
---
target: claude-code|codex-cli|gemini-cli
priority: immediate|normal|background
---

## Objective
[What to accomplish]

## Scope
IN: [what's included]
OUT: [what's excluded]

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]

## Verification
```bash
[Commands to prove success]
```
```

### RETURN: Executor → Repository

When execution completes:

1. Results go to `-OUTGOING/[date]-[task]/`
2. Include:
   - Execution log
   - Verification output
   - Any produced artifacts

---

## VI. CORPUS HANDLING

### What to Archive (move to 05-ARCHIVE/)

- Directives 017-046 (historical, not active)
- Execution logs pre-2026 (evidence, not scripture)
- Oracle contexts 8-12 (superseded)
- IIC configs (over-specified, will be replaced)
- IMEP artifacts (protocol deprecated)

### What to Keep Active

- CLAUDE.md, COCKPIT.md, Makefile (root operational)
- 00-ORCHESTRATION/state/ (current state only)
- 01-CANON/ (protected, do not touch)
- 02-OPERATIONAL/prompts/ (active configurations)
- 04-SOURCES/ (working material)

### What to Create

- 02-OPERATIONAL/constellation/ (new home for platform configs)
  - claude-web.md
  - chatgpt-compiler.md
  - gemini-digestor.md
  - gemini-cli.md
  - claude-code.md
  - codex-cli.md

---

## VII. IMMEDIATE ACTIONS

### Phase 1: Stabilize (Today)

1. **This thread becomes canonical INTERPRETER**
   - Continue using for ideation/synthesis
   - Produce handoffs explicitly when needed

2. **Deprecate the failed ChatGPT Deviser thread**
   - Extract any useful content to `-INBOX/`
   - Do not continue that thread

3. **Preserve Gemini meta-analysis**
   - Capture to `-INBOX/` if not already
   - Reference but don't continue

### Phase 2: Configure (This Week)

1. **Draft simplified platform configs**
   - Start with ChatGPT Compiler (most constrained)
   - Then Gemini Digestor
   - Claude Web is already configured

2. **Test the flow**
   - Create a simple handoff
   - Dispatch to Claude Code
   - Verify return path works

3. **Archive historical artifacts**
   - Move directive history to 05-ARCHIVE/
   - Keep state minimal

### Phase 3: Iterate (Ongoing)

1. **Each interaction refines the interface contracts**
2. **Failures become configuration updates**
3. **Success patterns become documented protocols**

---

## VIII. WHAT WE'RE NOT DOING

1. **Not implementing IMEP** - too complex, not needed
2. **Not using Blitzkrieg dropbox workflow** - overkill for current state
3. **Not installing IIC configs** - over-specified
4. **Not trying to reconstruct history** - forgetting is a feature
5. **Not optimizing prematurely** - get basics working first

---

## IX. SUCCESS CRITERIA

This architecture succeeds when:

1. **A thought in Claude Web becomes a repo artifact without friction**
2. **A directive dispatched to ChatGPT comes back correctly formatted**
3. **Gemini CLI produces evidence packs with reproducible commands**
4. **Claude Code executes directives and produces verification proof**
5. **No platform is asked to do what it's bad at**

---

## X. OPEN QUESTIONS (For Principal Decision)

1. **Avatar names**: Deferred per your request. When ready, each role gets a name for voice/personality configuration.

2. **Account 2 purpose**: Currently assigned to Claude Code parallel execution. Is the "bridge" function still needed, or can we simplify?

3. **Reinit protocols**: Do we need platform-specific reinit skills, or is the simplified handoff protocol sufficient?

4. **Grok/Perplexity**: When do they enter the constellation? Proposed: Grok for adversarial red-teaming, Perplexity for external information retrieval. Not core loop participants.

5. **Automation priority**: Manual handoffs are fine for now. When do we invest in automation (ingestion scripts, etc.)?

---

*This document is a living artifact. Update it as the constellation evolves.*
