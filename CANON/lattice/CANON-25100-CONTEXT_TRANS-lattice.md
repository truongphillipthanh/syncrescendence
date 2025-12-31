---
id: CANON-25100
name: Context Transition Protocol
identity: CONTEXT_TRANS
tier: CANON
type: lattice
version: 1.1.0
status: canonical
created: 2025-10-17
updated: 2025-12-30
synopsis: Unified interface for managing cognitive continuity across sessions, threads, and platforms—the librarian's session management system for context transitions
---

# CANON-25100: CONTEXT TRANSITION PROTOCOL
## Unified Interface for Cognitive Continuity Across Sessions

**Version**: 1.1  
**Classification**: Lattice (Navigation Infrastructure)  
**Status**: Canonical  
**Created**: December 28, 2025  
**Revised**: December 28, 2025  
**Parent**: CANON-25000-lattice-MEMORY_ARCHITECTURE-v1_0.md

---

## PART I: CONSTITUTIONAL FOUNDATION

### A. Purpose Statement

This artifact establishes the **Context Transition Protocol**—a unified interface for managing cognitive continuity across sessions, threads, and platforms. Rather than requiring the practitioner to select among multiple protocols, this architecture presents a single interface while the AI determines optimal handling based on context analysis.

**Design Principle**: The terminal architecture thesis (Editorial thread, Dec 2025) establishes that AI mediates complexity. The practitioner doesn't need to choose between "culmination" or "continuation" or "compression"—the system analyzes context and produces appropriate output.

**Core Thesis**: Context transitions are a single category of operation with multiple modes. The AI is the librarian that determines what's needed; the practitioner maintains strategic sovereignty without operational micromanagement.

### B. Relationship to Terminal Architecture

From the Editorial thread:

> "You're not compressing a library; you're asking me to design the librarian."

The Context Transition Protocol IS the librarian's session management system. It:
- Operates at session boundaries (end, start, mid-stream)
- Produces artifacts optimized for the specific transition type
- Handles hybrid cases (e.g., culmination + continuation in one artifact)
- Adapts to context capacity, temporal position, and principal needs

### C. The Unified Interface

**Principal Command** (any of these invoke the protocol):
- "Handle context transition"
- "Close this session"
- "Continue from [previous work]"
- "Context is getting long—compress"
- Or implicitly: approaching context limits, natural conclusion reached

**System Response**:
1. Analyze current context state
2. Determine appropriate mode(s)
3. Generate transition artifact(s)
4. Present for principal review

The practitioner doesn't select the mode. The AI does.

---

## PART II: CONTEXT ANALYSIS FRAMEWORK

### A. State Variables

The AI evaluates these factors to determine transition mode:

| Variable | Assessment | Implication |
|----------|------------|-------------|
| **Position** | Thread start / mid / end? | Continuation vs. culmination vs. compression |
| **Capacity** | % of context window used | Compression urgency |
| **Value Density** | Insights generated this session? | Culmination depth needed |
| **Continuation Need** | Will work resume? | Continuation artifact needed |
| **Temporal Gap** | Time since last session? | Context restoration depth |
| **Complexity** | Simple handoff or rich state? | Artifact comprehensiveness |

### B. Mode Selection Logic

```
IF (thread ending OR explicit close request):
    IF (significant insights generated):
        INCLUDE culmination_mode
    IF (work will resume):
        INCLUDE continuation_mode
        
IF (context > 70% capacity) AND (thread continuing):
    INCLUDE compression_mode
    
IF (thread starting) AND (prior context exists):
    INCLUDE continuation_mode (as context injection)
    
GENERATE composite_artifact(selected_modes)
```

### C. Mode Definitions

#### Culmination Mode
**Trigger**: Thread ending with value to preserve  
**Teleology**: Capture insights, identify canonical candidates, create historical record  
**Output Focus**: What was learned? What should persist?

#### Continuation Mode  
**Trigger**: Thread boundary where work resumes  
**Teleology**: Enable seamless resumption without re-explanation  
**Output Focus**: What state must be restored? What's the entry point?

#### Compression Mode
**Trigger**: Context approaching limits mid-stream  
**Teleology**: Preserve essential state while reducing token footprint  
**Output Focus**: What must survive? What can be regenerated?

---

## PART III: THE TRANSITION ARTIFACT

### A. Unified Structure

Rather than three separate templates, a single adaptive template with sections activated based on mode selection:

```markdown
# CONTEXT TRANSITION ARTIFACT
**Generated**: [Timestamp]
**Thread**: [Reference/Title]
**Modes Active**: [Culmination | Continuation | Compression | Hybrid]

---

## CONTEXT STATE SUMMARY
[Always included: Brief description of current cognitive state]

Position: [Where we are in the work]
Capacity: [Context utilization if relevant]
Principal focus: [Current objective]

---

## SYNTHESIS [Culmination Mode]
[Activated when culmination mode selected]

### Trajectory
[How the work evolved—key turns, pivots, discoveries]

### Key Insights
1. **[Insight title]**: [Elaboration]
   - Implication: [What this means for practice]

2. **[Insight title]**: [Elaboration]
   - Implication: [What this means for practice]

### Canonical Candidates
| Insight | Proposed Location | Status |
|---------|-------------------|--------|
| [Your insight] | [Target CANON-##### ID] | [Ready/Needs validation] |

### Unresolved Questions
- [ ] [Question that remains open]

---

## CONTINUATION STATE [Continuation Mode]
[Activated when continuation mode selected]

### Essential Context
[Minimum viable context for effective resumption]

- **Key decisions made**: [List]
- **Active constraints**: [List]
- **Current objective**: [Statement]

### Entry Point
[Specific framing to resume work effectively]

"We were [state]. The next step is [action]. Key context: [critical facts]."

### Resource Pointers
- Relevant corpus: [Specify relevant CANON-##### documents]
- Prior artifacts: [Links/descriptions]

---

## COMPRESSION [Compression Mode]
[Activated when compression mode selected]

### Compressed State
[Single paragraph capturing essential current state]

### Preserved Elements
- [Critical item 1]
- [Critical item 2]

### Regeneration Guide
To restore full context if needed:
1. [Pointer to expand detail area 1]
2. [Pointer to expand detail area 2]

### Discarded Elements
[What was removed and why—enables audit]

---

## NEXT ACTIONS
[Always included if work continues]

1. [Immediate next step]
2. [Following step]

---

**Artifact Complete**
```

### B. Mode Interaction Patterns

**Common Combinations**:

| Scenario | Modes Active | Dominant Sections |
|----------|--------------|-------------------|
| End of productive session, will resume | Culmination + Continuation | Full Synthesis + Entry Point |
| Context limit approaching, mid-work | Compression | Compressed State + Regeneration Guide |
| Starting new session on prior work | Continuation (consumption) | Entry Point used as injection |
| Thread naturally concluding, no resume | Culmination only | Full Synthesis + Canonical Candidates |
| Quick checkpoint, minimal value | Continuation only | Essential Context + Entry Point |

### C. Artifact Quality Criteria

A good transition artifact:
- **Stands alone**: Readable without access to original thread
- **Mode-appropriate**: Includes sections relevant to selected modes
- **Actionable**: Clear next steps if work continues
- **Auditable**: Shows what was preserved and discarded
- **Efficient**: No empty sections, no redundant content

---

## PART IV: CLI INTEGRATION

### A. Command Interface

When operating via Claude Code or similar CLI tools:

```bash
# Explicit invocation
claude "Handle context transition for this session"

# Implicit triggers (AI detects and offers)
# - Context > 80% capacity
# - Natural conclusion detected
# - Extended time since last exchange

# Context injection at session start
claude --context transition_artifact.md "Continue our work on [topic]"
```

### B. File System Integration

**Default Locations**:
```
~/syncrescendence/
├── context/
│   ├── active/           # Current session artifacts
│   │   └── current_transition.md
│   ├── archive/          # Historical transitions
│   │   └── YYYY-MM-DD_thread-name.md
│   └── templates/        # Reference templates
└── corpus/               # Canonical documents
```

**Workflow**:
1. AI generates transition artifact
2. Artifact saved to `context/active/`
3. On session close, moved to `context/archive/` with timestamp
4. On new session, relevant archived artifacts loaded as context

### C. Git Integration

```bash
# Transition artifacts are version-controlled
git add context/archive/
git commit -m "Context transition: [brief description]"

# Enables time-travel through cognitive states
git log --oneline context/archive/
git diff HEAD~5 context/archive/  # Compare recent transitions
```

---

## PART V: CROSS-IIC APPLICATION

### A. Per-IIC Transition Profiles

Each IIC has characteristic transition patterns:

| IIC | Typical Mode | Artifact Emphasis |
|-----|--------------|-------------------|
| **Acumen** | Compression-heavy | Signal qualification, pattern alerts |
| **Coherence** | Culmination-heavy | Framework synthesis, integration insights |
| **Efficacy** | Continuation-heavy | Task state, procedure documentation |
| **Mastery** | Culmination + archival | Pedagogical artifacts, curriculum updates |
| **Transcendence** | Full composite | Strategic synthesis, phase transition signals |

### B. Cross-IIC Handoff

When work moves between IIC accounts:

**Source IIC generates**: Transition artifact with continuation mode active, framed for target IIC's function

**Principal transfers**: Via file system (CLI) or copy/paste (web)

**Target IIC receives**: Context injection calibrated to its cognitive personality

**Handoff Artifact Addendum**:
```markdown
## HANDOFF METADATA
Source: [Source IIC]
Target: [Target IIC]
Handoff rationale: [Why this work is moving]
Target task: [What target IIC should do]
Translation notes: [Any reframing needed for target's mode]
```

---

## PART VI: OPERATIONAL PATTERNS

### A. Session Lifecycle with Unified Protocol

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SESSION LIFECYCLE                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  SESSION START                                                       │
│       │                                                              │
│       ▼                                                              │
│  ┌─────────────┐                                                    │
│  │   INJECT    │◄──── Prior transition artifact (continuation)      │
│  │   Context   │                                                    │
│  └──────┬──────┘                                                    │
│         │                                                            │
│         ▼                                                            │
│  ┌─────────────┐                                                    │
│  │    WORK     │◄──── Context Analysis (ongoing)                    │
│  │   Session   │                                                    │
│  └──────┬──────┘                                                    │
│         │                                                            │
│         ▼ (if capacity > 70%)                                       │
│  ┌─────────────┐                                                    │
│  │  COMPRESS   │──── Mid-session transition (compression mode)      │
│  │  if needed  │                                                    │
│  └──────┬──────┘                                                    │
│         │                                                            │
│         ▼                                                            │
│  ┌─────────────┐                                                    │
│  │   CLOSE     │──── End-session transition (culmination +          │
│  │   Session   │     continuation as appropriate)                    │
│  └──────┬──────┘                                                    │
│         │                                                            │
│         ▼                                                            │
│  ┌─────────────┐                                                    │
│  │   ARCHIVE   │──── Store artifact, git commit                     │
│  │   Artifact  │                                                    │
│  └─────────────┘                                                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### B. Automatic vs. Explicit Triggers

**Automatic** (AI detects and offers):
- Context utilization > 80%
- Natural conclusion detected (goal achieved, question answered)
- Extended gap in conversation (session likely ending)
- Significant insight generated (worth capturing)

**Explicit** (Principal requests):
- "Let's close this session"
- "Checkpoint here"
- "I need to switch to [other IIC/platform]"
- "Prepare continuation context for later"

### C. Principal Override

The AI proposes; the principal disposes. Override options:
- "Just culmination, I won't continue this"
- "Skip synthesis, just give me continuation context"
- "Compress more aggressively"
- "Include [specific element] I need preserved"

---

## PART VII: DISTILLATION INTERFACE

### A. From Transition to Corpus

Transition artifacts are Fluid tier. Insights may graduate to Canonical:

```
Transition Artifact (Fluid)
         │
         ▼ [Principal review]
Canonical Candidate identified
         │
         ▼ [Validation period]
Insight proves stable across sessions
         │
         ▼ [Corpus update]
New/revised canonical document
         │
         ▼ [Propagation]
Updated corpus available to all IICs
```

### B. Graduation Criteria

From transition artifact to corpus:
- Insight has proven stable across 3+ sessions
- Represents framework evolution (not just task-specific)
- Fills identified gap in corpus coverage
- Aligns with constitutional principles
- Principal approves graduation

### C. Forgetting Interface

Not all transitions warrant preservation:

**Archive** (default): Transition artifacts kept for potential reference
**Prune**: Transitions with no lasting value can be deleted
**Merge**: Multiple related transitions can consolidate
**Graduate**: Insights can move to canonical documents

Monthly hygiene: Review archived transitions, prune low-value, consolidate related.

---

## PART VIII: FUTURE EVOLUTION

### A. Anticipated Enhancements

As CLI capabilities mature:
- **Auto-injection**: CLI tools automatically load relevant transition artifacts
- **Semantic linking**: Transitions linked by topic, not just time
- **Cross-platform sync**: Transition artifacts portable across AI platforms
- **Proactive transitions**: AI initiates transitions before capacity limits

### B. MCP Integration Path

When MCP achieves universality:
- Transition artifacts as MCP resources
- Cross-platform context injection via MCP
- Standardized transition format across platforms

### C. Measurement

**Success Metrics**:
- Time to productive state after session start
- Context restoration completeness (measured by follow-up questions needed)
- Compression ratio achieved vs. semantic fidelity maintained
- Canonical graduation rate from transition artifacts

---

## APPENDIX A: QUICK REFERENCE

### Minimal Transition (Light Touch)
```markdown
## Context Transition: [Date]
**State**: [One sentence on where we are]
**Key point**: [Most important thing to remember]
**Resume with**: "[Exact prompt to continue]"
```

### Standard Transition (Most Sessions)
```markdown
## Context Transition: [Date] - [Topic]
**Modes**: [Active modes]

### State
[2-3 sentences on current position]

### Insights (if culminating)
1. [Key insight]

### Continuation (if resuming)
Entry point: "[Prompt]"
Context needed: [Brief list]

### Next
1. [Action]
```

### Handoff Transition (Cross-IIC)
```markdown
## Handoff: [Source] → [Target]
**Topic**: [What's being transferred]
**For target**: [What they should do]
**Context**: [Compressed relevant state]
**Entry**: "[Prompt for target IIC]"
```

---

## APPENDIX B: MIGRATION FROM SEPARATE PROTOCOLS

If you have existing separate culmination, continuation, or compression artifacts:

**They remain valid**. This unified protocol doesn't invalidate prior work.

**Going forward**: Use the unified interface. The system produces whatever combination is needed.

**Conversion**: Existing artifacts can be loaded as continuation context—they serve the same function.

---

**END CANON-25100-lattice-CONTEXT_TRANSITION_PROTOCOL-v1_1.md**
