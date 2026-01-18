# Failure Modes Catalog
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Enumerate system failure modes with detection, prevention, and recovery

---

## Category 1: Context Invisibility

### FM-001: Webapp Context Not Persisting
**Description**: Insights generated in Claude Web App are not visible to Claude Code sessions.

**Detection Signal**:
- Claude Code asks questions already answered in web session
- Duplicate work on previously resolved issues
- "I don't have context about..." responses

**Prevention**:
- Context graduation protocol: export web artifacts to repo
- Use ORACLE_CONTEXT.md as bridge document
- Don't rely on implicit memory transfer

**Recovery Protocol**:
1. Export relevant web conversation sections
2. Create context document in repo
3. Load context into Claude Code session
4. Log event: `{"event": "context_graduation", "source": "web_session"}`

**Artifact Proving Recovery**: Context document exists in repo, Claude Code references it

---

### FM-002: Project Memory Opacity
**Description**: Claude Project memory contains information but user cannot inspect/verify.

**Detection Signal**:
- Model recalls facts user cannot verify source of
- Memory claims contradict repo state
- "I remember that..." without citation

**Prevention**:
- Periodically export Project memory snapshots
- Treat memory as cache, repo as truth
- Verify claims against repo artifacts

**Recovery Protocol**:
1. Ask model to cite sources for claims
2. Verify citations against repo
3. If mismatch, trust repo, flag memory corruption
4. Consider resetting project memory if severe

**Artifact Proving Recovery**: Verification log documenting claim vs repo comparison

---

### FM-003: Cross-Platform Context Loss
**Description**: Context developed in one platform not available in another.

**Detection Signal**:
- ChatGPT plan references findings Gemini has but not vice versa
- Integration packets missing evidence
- "I don't have access to that information"

**Prevention**:
- All platform outputs culminate in repo packets
- Evidence packets capture Gemini findings
- Plan packets reference evidence IDs

**Recovery Protocol**:
1. Identify missing context
2. Create appropriate packet (EVD/PLN/etc)
3. Store in blackboard
4. Reference packet in subsequent work

**Artifact Proving Recovery**: Packet exists in blackboard/

---

## Category 2: Premature Convergence

### FM-004: Outputs Before Objectives Lock
**Description**: Execution begins before plan is approved, leading to wasted work.

**Detection Signal**:
- Code written that doesn't match eventual requirements
- Multiple revisions to same artifact
- "Wait, I thought we were doing..."

**Prevention**:
- Plan packet required before execution packet
- Stop conditions must be defined
- Principal approval for significant work

**Recovery Protocol**:
1. Stop execution
2. Complete plan packet with acceptance criteria
3. Verify plan addresses actual objective
4. Resume execution only after plan approval

**Artifact Proving Recovery**: PLN packet with Principal approval, EXE packet references PLN

---

### FM-005: Analysis Paralysis
**Description**: Planning phase never completes, no execution occurs.

**Detection Signal**:
- Multiple plan revisions without execution
- Growing backlog with zero completions
- "We need to think about this more"

**Prevention**:
- Time-box planning phases
- Minimum viable plan sufficient to start
- Prefer iteration over perfection

**Recovery Protocol**:
1. Recognize paralysis pattern
2. Define minimum viable deliverable
3. Execute on minimum viable plan
4. Iterate based on real results

**Artifact Proving Recovery**: EXE packet created, backlog decreasing

---

## Category 3: Transcription Loss

### FM-006: Video Content Not Captured
**Description**: Video's unique value (visual, tonal) lost in transcript.

**Detection Signal**:
- Transcript missing context that video provides
- "The diagram shows..." but no diagram reference
- Tonal nuance absent from text

**Prevention**:
- value_modality field in frontmatter
- visual_notes field for visual assessment
- Keep video URL for reference

**Recovery Protocol**:
1. Review original video for lost content
2. Add visual_notes to processed source
3. Flag as visual_primary if visual is essential
4. Consider screenshot extraction for key visuals

**Artifact Proving Recovery**: visual_notes field populated, value_modality accurate

---

### FM-007: Audio Nuance Ignored
**Description**: Emotional/tonal content lost in text conversion.

**Detection Signal**:
- Sarcasm/irony missed in transcript
- Speaker emphasis not captured
- "They seemed uncertain" not reflected

**Prevention**:
- audio_notes field for audio assessment
- Mark dialogue_primary vs audio_primary
- Preserve speaker identification

**Recovery Protocol**:
1. Re-listen to relevant segments
2. Add annotation for tonal context
3. Update value_modality if needed

**Artifact Proving Recovery**: Annotations added to processed source

---

## Category 4: Parallel Truth Systems

### FM-008: Canon Drift from Reality
**Description**: Canon documents diverge from external reality or current understanding.

**Detection Signal**:
- External research contradicts Canon claims
- Temporal content in Canon becoming outdated
- "But that's not how it works anymore"

**Prevention**:
- 18 Lenses includes temporal stability check
- Regular Canon review cycles
- Source citations enable verification

**Recovery Protocol**:
1. Identify specific drifted claims
2. Research current state
3. Update Canon with corrections
4. Log correction with source citation

**Artifact Proving Recovery**: Canon file updated, git commit references correction

---

### FM-009: Ledger/Reality Mismatch
**Description**: tasks.csv or sources.csv don't reflect actual state.

**Detection Signal**:
- Task marked DONE but file doesn't exist
- Source marked integrated but Canon unchanged
- Metrics don't match reality

**Prevention**:
- Verification commands before marking complete
- Atomic updates with validation
- Regular ledger audits

**Recovery Protocol**:
1. Audit ledger against filesystem
2. Correct mismatched entries
3. Log correction event
4. Consider adding automated verification

**Artifact Proving Recovery**: Audit log, corrected ledger entries

---

## Category 5: Account Membrane Leaks

### FM-010: Cross-Account Credential Exposure
**Description**: Credentials or sensitive data leaks between account contexts.

**Detection Signal**:
- API key appears in wrong context
- Personal data in work context
- Account confusion in responses

**Prevention**:
- Strict account separation
- No credentials in repo
- Environment variables for secrets

**Recovery Protocol**:
1. Identify leaked credential
2. Rotate credential immediately
3. Audit for usage
4. Review boundary controls

**Artifact Proving Recovery**: Credential rotated, audit log clean

---

### FM-011: Memory Cross-Contamination
**Description**: Project memory from one context bleeds into another.

**Detection Signal**:
- Model references client A in client B context
- Personal preferences appear in professional context
- "Wasn't that from..."

**Prevention**:
- Use separate Projects per context
- Regular memory review
- Don't rely on memory isolation

**Recovery Protocol**:
1. Clear affected project memory
2. Re-establish clean context
3. Verify isolation

**Artifact Proving Recovery**: Memory cleared confirmation, clean context test

---

## Category 6: Role Confusion

### FM-012: Planner Executing
**Description**: Platform assigned to planning role attempts execution.

**Detection Signal**:
- ChatGPT attempts to modify files
- "I'll just run this command..." from web platform
- Output contains execution artifacts

**Prevention**:
- Clear role definitions in prompts
- Packet protocol enforces separation
- Route execution to Claude Code only

**Recovery Protocol**:
1. Recognize role violation
2. Redirect to correct platform
3. Discard invalid execution attempt
4. Reinforce role in prompt

**Artifact Proving Recovery**: Correct routing event logged

---

### FM-013: Executor Planning
**Description**: Execution platform makes strategic decisions without plan.

**Detection Signal**:
- Claude Code redefines objectives mid-execution
- Scope creep beyond directive
- "I think we should also..."

**Prevention**:
- Clear acceptance criteria in plans
- Stop conditions defined
- Deviate only with Principal approval

**Recovery Protocol**:
1. Pause execution
2. Document proposed change
3. Escalate to Principal
4. Resume only with approved scope

**Artifact Proving Recovery**: Escalation logged, scope change approved or rejected

---

### FM-014: Verifier Modifying
**Description**: Audit role makes changes instead of reporting.

**Detection Signal**:
- Audit packet contains modifications
- "I fixed it" from auditor
- State changes during audit

**Prevention**:
- Audit is read-only assessment
- Separate audit and fix phases
- Clear recommendation vs action

**Recovery Protocol**:
1. Rollback unauthorized changes
2. Complete proper audit
3. Create new execution for fixes
4. Separate audit and execution packets

**Artifact Proving Recovery**: Clean audit packet, separate execution packet for fixes

---

## Failure Mode Summary Matrix

| ID | Category | Severity | Detection Ease | Recovery Effort |
|----|----------|----------|----------------|-----------------|
| FM-001 | Context | Medium | Medium | Low |
| FM-002 | Context | Medium | Hard | Medium |
| FM-003 | Context | High | Medium | Low |
| FM-004 | Convergence | High | Medium | Medium |
| FM-005 | Convergence | Medium | Easy | Medium |
| FM-006 | Transcription | Medium | Medium | Medium |
| FM-007 | Transcription | Low | Medium | Low |
| FM-008 | Truth Systems | High | Hard | High |
| FM-009 | Truth Systems | High | Medium | Medium |
| FM-010 | Membrane | Critical | Medium | High |
| FM-011 | Membrane | High | Hard | Medium |
| FM-012 | Role | Medium | Easy | Low |
| FM-013 | Role | Medium | Medium | Medium |
| FM-014 | Role | Medium | Easy | Medium |
