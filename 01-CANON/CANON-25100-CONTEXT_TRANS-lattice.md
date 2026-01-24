---
id: [[CANON-25100-CONTEXT_TRANS-lattice]]
name: Context Transition Protocol
identity: CONTEXT_TRANS
tier: CANON
type: lattice
version: 2.1.0
status: canonical
created: 2025-10-17
updated: 2026-01-11
synopsis: Unified interface for managing cognitive continuity across sessions, threads, and platforms—the librarian's session management system for context transitions
---

# CANON-25100-CONTEXT_TRANS-lattice (SN Format)

**Note**: This is a Semantic Notation compressed version.
**Original**: 2,493 words, 20,536 characters

---

TERM UnifiedInterfaceforCognitiveContinuityAcrossSessions:
    sutra: "Version: 1.1   Classification: Lattice (Navigation Infrastructure)   Status: Canonical   Created:..."
    gloss:
        **Version**: 1.1  
**Classification**: Lattice (Navigation Infrastructure)  
**Status**: Canonical  
**Created**: December 28, 2025  
**Revised**: December 28, 2025  
**Parent**: CANON-25000-lattice-MEMORY_ARCHITECTURE-v1_0.md

---
end


TERM APurposeStatement:
    sutra: "This artifact establishes the Context Transition Protocol—a unified interface for managing cognit..."
    gloss:
        This artifact establishes the **Context Transition Protocol**—a unified interface for managing cognitive continuity across sessions, threads, and platforms. Rather than requiring the practitioner to select among multiple protocols, this architecture presents a single interface while the AI determine...
end


TERM BRelationshiptoTerminalArchitecture:
    sutra: "From the Editorial thread:  > "You're not compressing a library; you're asking me to design the l..."
    gloss:
        From the Editorial thread:

> "You're not compressing a library; you're asking me to design the librarian."

The Context Transition Protocol IS the librarian's session management system. It:
- Operates at session boundaries (end, start, mid-stream)
- Produces artifacts optimized for the specific tra...
end


TERM CTheUnifiedInterface:
    sutra: "Sovereign Command (any of these invoke the protocol): - "Handle context transition" - "Close this..."
    gloss:
        **Sovereign Command** (any of these invoke the protocol):
- "Handle context transition"
- "Close this session"
- "Continue from [previous work]"
- "Context is getting long—compress"
- Or implicitly: approaching context limits, natural conclusion reached

**System Response**:
1. Analyze current conte...
end


TERM AStateVariables:
    sutra: "The AI evaluates these factors to determine transition mode:  | Variable | Assessment | Implicati..."
    gloss:
        The AI evaluates these factors to determine transition mode:

| Variable | Assessment | Implication |
|----------|------------|-------------|
| **Position** | Thread start / mid / end? | Continuation vs. culmination vs. compression |
| **Capacity** | % of context window used | Compression urgency |...
end


TERM BModeSelectionLogic:
    sutra: "`` IF (thread ending OR explicit close request):     IF (significant insights generated):        ..."
    gloss:
        ```
IF (thread ending OR explicit close request):
    IF (significant insights generated):
        INCLUDE culmination_mode
    IF (work will resume):
        INCLUDE continuation_mode
        
IF (context > 70% capacity) AND (thread continuing):
    INCLUDE compression_mode
    
IF (thread starting...
end


NORM CulminationMode:
    sutra: "Trigger: Thread ending with value to preserve   Teleology: Capture insights, identify canonical c..."
    gloss:
        **Trigger**: Thread ending with value to preserve  
**Teleology**: Capture insights, identify canonical candidates, create historical record  
**Output Focus**: What was learned? What should persist?
end


NORM ContinuationMode:
    sutra: "Trigger: Thread boundary where work resumes   Teleology: Enable seamless resumption without re-ex..."
    gloss:
        **Trigger**: Thread boundary where work resumes  
**Teleology**: Enable seamless resumption without re-explanation  
**Output Focus**: What state must be restored? What's the entry point?
end


NORM CompressionMode:
    sutra: "Trigger: Context approaching limits mid-stream   Teleology: Preserve essential state while reduci..."
    gloss:
        **Trigger**: Context approaching limits mid-stream  
**Teleology**: Preserve essential state while reducing token footprint  
**Output Focus**: What must survive? What can be regenerated?

---
end


TERM AUnifiedStructure:
    sutra: "Rather than three separate templates, a single adaptive template with sections activated based on..."
    gloss:
        Rather than three separate templates, a single adaptive template with sections activated based on mode selection:

```markdown
end


ARTIFACT CONTEXTTRANSITIONARTIFACT:
    sutra: "Generated: [Timestamp] Thread: [Reference/Title] Modes Active: [Culmination | Continuation | Comp..."
    gloss:
        **Generated**: [Timestamp]
**Thread**: [Reference/Title]
**Modes Active**: [Culmination | Continuation | Compression | Hybrid]

---
end


TERM CONTEXTSTATESUMMARY:
    sutra: "[Always included: Brief description of current cognitive state]  Position: [Where we are in the w..."
    gloss:
        [Always included: Brief description of current cognitive state]

Position: [Where we are in the work]
Capacity: [Context utilization if relevant]
Sovereign focus: [Current objective]

---
end


TERM SYNTHESISCulminationMode:
    sutra: "[Activated when culmination mode selected]"
    gloss:
        [Activated when culmination mode selected]
end


TERM Trajectory:
    sutra: "[How the work evolved—key turns, pivots, discoveries]"
    gloss:
        [How the work evolved—key turns, pivots, discoveries]
end


TERM KeyInsights:
    sutra: "1"
    gloss:
        1. **[Insight title]**: [Elaboration]
   - Implication: [What this means for practice]

2. **[Insight title]**: [Elaboration]
   - Implication: [What this means for practice]
end


TERM CanonicalCandidates:
    sutra: "| Insight | Proposed Location | Status | |---------|-------------------|--------| | [Your insight..."
    gloss:
        | Insight | Proposed Location | Status |
|---------|-------------------|--------|
| [Your insight] | [Target CANON-##### ID] | [Ready/Needs validation] |
end


TERM UnresolvedQuestions:
    sutra: "- [ ] [Question that remains open]  ---"
    gloss:
        - [ ] [Question that remains open]

---
end


TERM CONTINUATIONSTATEContinuationMode:
    sutra: "[Activated when continuation mode selected]"
    gloss:
        [Activated when continuation mode selected]
end


TERM EssentialContext:
    sutra: "[Minimum viable context for effective resumption]  - Key decisions made: [List] - Active constrai..."
    gloss:
        [Minimum viable context for effective resumption]

- **Key decisions made**: [List]
- **Active constraints**: [List]
- **Current objective**: [Statement]
end


TERM EntryPoint:
    sutra: "[Specific framing to resume work effectively]  "We were [state]"
    gloss:
        [Specific framing to resume work effectively]

"We were [state]. The next step is [action]. Key context: [critical facts]."
end


TERM ResourcePointers:
    sutra: "- Relevant corpus: [Specify relevant CANON-##### documents] - Prior artifacts: [Links/description..."
    gloss:
        - Relevant corpus: [Specify relevant CANON-##### documents]
- Prior artifacts: [Links/descriptions]

---
end


TERM COMPRESSIONCompressionMode:
    sutra: "[Activated when compression mode selected]"
    gloss:
        [Activated when compression mode selected]
end


TERM CompressedState:
    sutra: "[Single paragraph capturing essential current state]"
    gloss:
        [Single paragraph capturing essential current state]
end


TERM PreservedElements:
    sutra: "- [Critical item 1] - [Critical item 2]"
    gloss:
        - [Critical item 1]
- [Critical item 2]
end


TERM RegenerationGuide:
    sutra: "To restore full context if needed: 1"
    gloss:
        To restore full context if needed:
1. [Pointer to expand detail area 1]
2. [Pointer to expand detail area 2]
end


TERM DiscardedElements:
    sutra: "[What was removed and why—enables audit]  ---"
    gloss:
        [What was removed and why—enables audit]

---
end


TERM NEXTACTIONS:
    sutra: "[Always included if work continues]  1"
    gloss:
        [Always included if work continues]

1. [Immediate next step]
2. [Following step]

---

**Artifact Complete**
```
end


TERM BModeInteractionPatterns:
    sutra: "Common Combinations:  | Scenario | Modes Active | Dominant Sections | |----------|--------------|..."
    gloss:
        **Common Combinations**:

| Scenario | Modes Active | Dominant Sections |
|----------|--------------|-------------------|
| End of productive session, will resume | Culmination + Continuation | Full Synthesis + Entry Point |
| Context limit approaching, mid-work | Compression | Compressed State + Re...
end


ARTIFACT CArtifactQualityCriteria:
    sutra: "A good transition artifact: - Stands alone: Readable without access to original thread - Mode-app..."
    gloss:
        A good transition artifact:
- **Stands alone**: Readable without access to original thread
- **Mode-appropriate**: Includes sections relevant to selected modes
- **Actionable**: Clear next steps if work continues
- **Auditable**: Shows what was preserved and discarded
- **Efficient**: No empty secti...
end


TERM ACommandInterface:
    sutra: "When operating via Claude Code or similar CLI tools:  ```bash"
    gloss:
        When operating via Claude Code or similar CLI tools:

```bash
end


TERM Explicitinvocation:
    sutra: "claude "Handle context transition for this session""
    gloss:
        claude "Handle context transition for this session"
end


TERM Contextinjectionatsessionstart:
    sutra: "claude --context transition_artifact.md "Continue our work on [topic]" ```"
    gloss:
        claude --context transition_artifact.md "Continue our work on [topic]"
```
end


TERM BFileSystemIntegration:
    sutra: "Default Locations: `` ~/syncrescendence/ ├── context/ │   ├── active/           # Current session..."
    gloss:
        **Default Locations**:
```
~/syncrescendence/
├── context/
│   ├── active/           # Current session artifacts
│   │   └── current_transition.md
│   ├── archive/          # Historical transitions
│   │   └── YYYY-MM-DD_thread-name.md
│   └── templates/        # Reference templates
└── corpus/...
end


ARTIFACT Transitionartifactsareversioncontrolled:
    sutra: "git add context/archive/ git commit -m "Context transition: [brief description]""
    gloss:
        git add context/archive/
git commit -m "Context transition: [brief description]"
end


TERM Enablestimetravelthroughcognitivestates:
    sutra: "git log --oneline context/archive/ git diff HEAD~5 context/archive/  # Compare recent transitions..."
    gloss:
        git log --oneline context/archive/
git diff HEAD~5 context/archive/  # Compare recent transitions
```

---
end


TERM APerIICTransitionProfiles:
    sutra: "Each IIC has characteristic transition patterns:  | IIC | Typical Mode | Artifact Emphasis | |---..."
    gloss:
        Each IIC has characteristic transition patterns:

| IIC | Typical Mode | Artifact Emphasis |
|-----|--------------|-------------------|
| **Acumen** | Compression-heavy | Signal qualification, pattern alerts |
| **Coherence** | Culmination-heavy | Framework synthesis, integration insights |
| **Effi...
end


TERM BCrossIICHandoff:
    sutra: "When work moves between IIC accounts:  Source IIC generates: Transition artifact with continuatio..."
    gloss:
        When work moves between IIC accounts:

**Source IIC generates**: Transition artifact with continuation mode active, framed for target IIC's function

**Sovereign transfers**: Via file system (CLI) or copy/paste (web)

**Target IIC receives**: Context injection calibrated to its cognitive personality...
end


NORM HANDOFFMETADATA:
    sutra: "Source: [Source IIC] Target: [Target IIC] Handoff rationale: [Why this work is moving] Target tas..."
    gloss:
        Source: [Source IIC]
Target: [Target IIC]
Handoff rationale: [Why this work is moving]
Target task: [What target IIC should do]
Translation notes: [Any reframing needed for target's mode]
```

---
end


TERM ASessionLifecyclewithUnifiedProtocol:
    sutra: "`` ┌─────────────────────────────────────────────────────────────────────┐ │                     ..."
    gloss:
        ```
┌─────────────────────────────────────────────────────────────────────┐
│                      SESSION LIFECYCLE                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  SES...
end


TERM BAutomaticvsExplicitTriggers:
    sutra: "Automatic (AI detects and offers): - Context utilization > 80% - Natural conclusion detected (goa..."
    gloss:
        **Automatic** (AI detects and offers):
- Context utilization > 80%
- Natural conclusion detected (goal achieved, question answered)
- Extended gap in conversation (session likely ending)
- Significant insight generated (worth capturing)

**Explicit** (Sovereign requests):
- "Let's close this session...
end


TERM CSovereignOverride:
    sutra: "The AI proposes; the sovereign disposes"
    gloss:
        The AI proposes; the sovereign disposes. Override options:
- "Just culmination, I won't continue this"
- "Skip synthesis, just give me continuation context"
- "Compress more aggressively"
- "Include [specific element] I need preserved"

---
end


TERM AFromTransitiontoCorpus:
    sutra: "Transition artifacts are Fluid tier"
    gloss:
        Transition artifacts are Fluid tier. Insights may graduate to Canonical:

```
Transition Artifact (Fluid)
         │
         ▼ [Sovereign review]
Canonical Candidate identified
         │
         ▼ [Validation period]
Insight proves stable across sessions
         │
         ▼ [Corpus update]
New/...
end


TERM BGraduationCriteria:
    sutra: "From transition artifact to corpus: - Insight has proven stable across 3+ sessions - Represents f..."
    gloss:
        From transition artifact to corpus:
- Insight has proven stable across 3+ sessions
- Represents framework evolution (not just task-specific)
- Fills identified gap in corpus coverage
- Aligns with constitutional principles
- Sovereign approves graduation
end


TERM CForgettingInterface:
    sutra: "Not all transitions warrant preservation:  Archive (default): Transition artifacts kept for poten..."
    gloss:
        Not all transitions warrant preservation:

**Archive** (default): Transition artifacts kept for potential reference
**Prune**: Transitions with no lasting value can be deleted
**Merge**: Multiple related transitions can consolidate
**Graduate**: Insights can move to canonical documents

Monthly hygi...
end


TERM AAnticipatedEnhancements:
    sutra: "As CLI capabilities mature: - Auto-injection: CLI tools automatically load relevant transition ar..."
    gloss:
        As CLI capabilities mature:
- **Auto-injection**: CLI tools automatically load relevant transition artifacts
- **Semantic linking**: Transitions linked by topic, not just time
- **Cross-platform sync**: Transition artifacts portable across AI platforms
- **Proactive transitions**: AI initiates trans...
end


TERM BMCPIntegrationPath:
    sutra: "When MCP achieves universality: - Transition artifacts as MCP resources - Cross-platform context ..."
    gloss:
        When MCP achieves universality:
- Transition artifacts as MCP resources
- Cross-platform context injection via MCP
- Standardized transition format across platforms
end


TERM CMeasurement:
    sutra: "Success Metrics: - Time to productive state after session start - Context restoration completenes..."
    gloss:
        **Success Metrics**:
- Time to productive state after session start
- Context restoration completeness (measured by follow-up questions needed)
- Compression ratio achieved vs. semantic fidelity maintained
- Canonical graduation rate from transition artifacts

---
end


TERM APurpose:
    sutra: "As work increasingly moves from web app to repository, traditional handoff documents become less ..."
    gloss:
        As work increasingly moves from web app to repository, traditional handoff documents become less necessary. The Oracle Pedigree provides:

1. **Historical Lineage Tracking**: Oracle 0 → current thread
2. **Decision Archaeology**: What was decided and why
3. **Multi-Model Integration**: Tracks decisi...
end


TERM BPedigreevsHandoff:
    sutra: "Handoff Documents remain useful for: - Session initialization prompts - Context restoration acros..."
    gloss:
        **Handoff Documents** remain useful for:
- Session initialization prompts
- Context restoration across model resets
- Cross-platform synchronization (push context)

**Oracle Pedigree** supersedes handoff for:
- Decision archaeology (pull context)
- Multi-model coordination history
- Repository-centr...
end


TERM CPedigreeComponents:
    sutra: "Each Oracle session generates pedigree metadata:  ``yaml oracle_pedigree:   thread_id: "Oracle 12..."
    gloss:
        Each Oracle session generates pedigree metadata:

```yaml
oracle_pedigree:
  thread_id: "Oracle 12"
  campaign: "Campaign Phase 2: Architecture"
  phase: "Construction"
  date: "2026-01-11"

  decisions:
    - id: DEC-043A-001
      sovereign_words: "retain all 3 Claude Pro accounts"
      interpret...
end


TERM DPedigreeLocation:
    sutra: "Pedigree information is distributed across:  | Component | Location | Purpose | |-----------|----..."
    gloss:
        Pedigree information is distributed across:

| Component | Location | Purpose |
|-----------|----------|---------|
| Thread summaries | ARCH-ORACLE_ARC_SUMMARY.md | Historical lineage |
| Decisions | ARCH-ORACLE_DECISIONS.md | Decision archaeology |
| Intentions | ARCH-INTENTION_COMPASS.md | Active/...
end


TERM ECrossPlatformPedigree:
    sutra: "When decisions involve multiple platforms:  ```markdown"
    gloss:
        When decisions involve multiple platforms:

```markdown
end


TERM DecisionDEC043A001:
    sutra: "Platforms Involved: Claude (Oracle, Alpha, Beta), Gemini, ChatGPT Decision Point: Platform specia..."
    gloss:
        **Platforms Involved**: Claude (Oracle, Alpha, Beta), Gemini, ChatGPT
**Decision Point**: Platform specialization architecture
**Sovereign's Words**: "design/architect for 3 Claude + 1 Gemini + 1 ChatGPT paid"
end


TERM PlatformSpecificImplications:
    sutra: "| Platform | Role | Action Required | |----------|------|-----------------| | Claude Oracle | Arc..."
    gloss:
        | Platform | Role | Action Required |
|----------|------|-----------------|
| Claude Oracle | Architect | Produce [[CANON-25200-CONSTELLATION_ARCH-lattice]] |
| Claude Alpha | Execute | Implement architecture |
| Gemini | Ingest | Configure for YouTube |
| ChatGPT | Review | Codex CLI integration |
end


TERM Verification:
    sutra: "- [ ] [[CANON-25200-CONSTELLATION_ARCH-lattice]] created - [ ] coordination.yaml updated - [ ] Each platform configured ```"
    gloss:
        - [ ] [[CANON-25200-CONSTELLATION_ARCH-lattice]] created
- [ ] coordination.yaml updated
- [ ] Each platform configured
```
end


TERM FPedigreeMaintenance:
    sutra: "During Oracle Session: 1"
    gloss:
        **During Oracle Session**:
1. Capture Sovereign's words verbatim
2. Document Oracle's interpretation
3. Record 18-lens evaluation (if strategic)
4. Note artifacts produced

**After Oracle Session**:
1. Update ARCH-ORACLE_ARC_SUMMARY.md with thread summary
2. Update ARCH-ORACLE_DECISIONS.md with key...
end


TERM ContextTransitionDate:
    sutra: "State: [One sentence on where we are] Key point: [Most important thing to remember] Resume with: ..."
    gloss:
        **State**: [One sentence on where we are]
**Key point**: [Most important thing to remember]
**Resume with**: "[Exact prompt to continue]"
```
end


TERM ContextTransitionDateTopic:
    sutra: "Modes: [Active modes]"
    gloss:
        **Modes**: [Active modes]
end


TERM State:
    sutra: "[2-3 sentences on current position]"
    gloss:
        [2-3 sentences on current position]
end


TERM Continuationifresuming:
    sutra: "Entry point: "[Prompt]" Context needed: [Brief list]"
    gloss:
        Entry point: "[Prompt]"
Context needed: [Brief list]
end


NORM HandoffSourceTarget:
    sutra: "Topic: [What's being transferred] For target: [What they should do] Context: [Compressed relevant..."
    gloss:
        **Topic**: [What's being transferred]
**For target**: [What they should do]
**Context**: [Compressed relevant state]
**Entry**: "[Prompt for target IIC]"
```

---
end


TERM APPENDIXBMIGRATIONFROMSEPARATEPROTOCOLS:
    sutra: "If you have existing separate culmination, continuation, or compression artifacts:  They remain v..."
    gloss:
        If you have existing separate culmination, continuation, or compression artifacts:

**They remain valid**. This unified protocol doesn't invalidate prior work.

**Going forward**: Use the unified interface. The system produces whatever combination is needed.

**Conversion**: Existing artifacts can b...
end
