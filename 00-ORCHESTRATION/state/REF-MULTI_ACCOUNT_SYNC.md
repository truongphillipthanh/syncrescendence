# REF-MULTI_ACCOUNT_SYNC: Cross-IIC Synchronization Protocol
## Reference Document for PROJ-014: Multi-Account Orchestration
### Version: 1.0.0 | Created: 2026-01-09

---

## Purpose

This document establishes the synchronization protocol for coordinating multiple Identity-Intelligence Complexes (IICs) across platforms and accounts. The goal is to maintain coherent cognitive continuity while preserving functional compartmentalization.

**Core Principle**: The corpus (file system) is ground truth. Platform memory is operational cache. All synchronization flows through the sovereign file system.

---

## Part I: Synchronization Architecture

### The Corpus-First Model

```
┌─────────────────────────────────────────────────────────────┐
│                 SOVEREIGN FILE SYSTEM                        │
│              (Git-versioned, Principal-controlled)           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ~/syncrescendence/                                  │    │
│  │  ├── 01-CANON/          (canonical knowledge)        │    │
│  │  ├── 02-ENGINE/    (prompts, memory configs)    │    │
│  │  ├── 04-SOURCES/        (raw + processed sources)    │    │
│  │  └── 00-ORCHESTRATION/  (state, directives, logs)    │    │
│  └─────────────────────────────────────────────────────┘    │
│              │                │                │             │
│              ▼                ▼                ▼             │
│    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│    │   Acumen    │    │  Coherence  │    │  Efficacy   │    │
│    │    IIC      │    │    IIC      │    │    IIC      │    │
│    │ (Claude +   │    │ (Claude +   │    │ (Claude +   │    │
│    │  ChatGPT +  │    │  ChatGPT)   │    │  ChatGPT)   │    │
│    │  Gemini +   │    │             │    │             │    │
│    │   Grok)     │    │             │    │             │    │
│    └─────────────┘    └─────────────┘    └─────────────┘    │
│              │                │                │             │
│              └────────────────┼────────────────┘             │
│                               ▼                              │
│                    ┌─────────────────────┐                   │
│                    │   Human Operator    │                   │
│                    │   (Principal)       │                   │
│                    └─────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Synchronization Primitives

| Primitive | Description | Implementation |
|-----------|-------------|----------------|
| **Corpus Documents** | Canonical knowledge shared by all IICs | CANON files in 01-CANON/ |
| **Memory Configs** | Per-IIC platform configurations | 02-ENGINE/memory/*.md |
| **Thread Culminations** | Session summaries for context transfer | 00-ORCHESTRATION/logs/*.md |
| **Context Files** | Active context for handoffs | 02-ENGINE/context/*.md |
| **State Files** | Orchestration state | 00-ORCHESTRATION/state/*.md |

---

## Part II: Inter-IIC Flow Patterns

### Primary Intelligence Flow

```
Acumen (Sensing) ──► Coherence (Synthesis) ──► Transcendence (Integration)
                                                        │
Mastery (Teaching) ◄── Efficacy (Operations) ◄─────────┘
```

### Flow Specifications

#### Acumen → Coherence
**Content**: Transcribed primary sources, qualified content, pattern observations
**Format**: Weekly intelligence package
**Transfer Method**:
1. Acumen generates weekly summary + transcript bundle
2. Bundle saved to 04-SOURCES/processed/
3. Coherence project updated with new source references
4. Human operator initiates Coherence session with handoff context

**Template**:
```markdown
# ACUMEN → COHERENCE HANDOFF
## Week of [DATE]

### Intelligence Package Summary
- Total sources processed: [N]
- Paradigm-level items: [N]
- Significant items: [N]
- Confirmatory items: [N]

### Priority Synthesis Candidates
1. [Source ID]: [Brief description + why it warrants deep synthesis]
2. [Source ID]: [Brief description + why it warrants deep synthesis]
...

### Cross-Domain Patterns Detected
- [Pattern 1]: Observed in [sources], potential framework implication
- [Pattern 2]: Observed in [sources], potential framework implication

### Transcripts Attached
- [List of transcript files in 04-SOURCES/processed/]
```

#### Coherence → Efficacy
**Content**: Frameworks, implementation guidance, operational protocols
**Format**: Framework document + implementation spec
**Transfer Method**:
1. Coherence produces framework in 01-CANON/
2. Efficacy-relevant implementation notes added to 02-ENGINE/
3. Human operator initiates Efficacy session with framework context

#### Coherence → Transcendence
**Content**: Meta-patterns, framework connections, civilizational implications
**Format**: Strategic synthesis document
**Transfer Method**:
1. Coherence identifies cross-framework patterns
2. Pattern report saved to 00-ORCHESTRATION/state/
3. Transcendence review during quarterly strategic sessions

#### Efficacy → Mastery
**Content**: Proven procedures, validated workflows, operational knowledge
**Format**: Procedural documentation
**Transfer Method**:
1. Efficacy validates workflow through execution
2. Proven procedures documented in 02-ENGINE/
3. Mastery receives for pedagogical packaging

#### Transcendence → Acumen
**Content**: Strategic priorities, focus areas, pruning criteria
**Format**: Strategic directive
**Transfer Method**:
1. Transcendence updates strategic priorities
2. Acumen curation criteria updated accordingly
3. Feed qualification rubrics recalibrated

---

## Part III: Platform Synchronization

### Cross-Platform Memory Coordination

Each IIC may operate across multiple platforms. Synchronization occurs through the corpus, not directly between platforms.

```
Platform A (Claude)  ←───────┐
                              │
Platform B (ChatGPT) ←────── CORPUS ──────► Platform C (Gemini)
                              │
Platform D (Grok)    ←───────┘
```

### Platform-Specific Sync Operations

#### Corpus → Platform (Outbound)
**Trigger**: New CANON document, updated configuration, new source
**Action**: Upload relevant files to platform's project/gem/thread
**Frequency**: As needed (document creation/update)

**Procedure**:
1. Identify platforms where content is relevant
2. Upload/update project files
3. Update platform's custom instructions if needed
4. Log sync action in session execution log

#### Platform → Corpus (Inbound)
**Trigger**: Valuable insight generated in platform session
**Action**: Extract insight to corpus document
**Frequency**: End of each substantive session

**Procedure**:
1. Generate thread culmination summary
2. Identify canonical candidates
3. If insight warrants corpus status, create/update CANON document
4. If operational, update relevant 02-ENGINE/ document
5. If context-specific, save to 00-ORCHESTRATION/state/

### Memory Feature Sync Table

| Feature | Claude | ChatGPT | Gemini | Grok | Sync Method |
|---------|--------|---------|--------|------|-------------|
| Preferences | User Preferences | Custom Instructions | Saved Info | User Settings | Manual (update each) |
| Auto-Memory | Basal + Project | Memory | Personalization | Context | Review monthly, prune inconsistencies |
| Projects | Projects | Projects | Gems | N/A | Upload same docs |
| Files | Project Files | Project uploads | Gem attachments | Thread uploads | Upload from corpus |
| Tools | search, MCP | plugins, GPT | extensions | X, DeepSearch | Platform-specific |

---

## Part IV: Conflict Resolution

### Hierarchy of Authority

1. **CANON documents** (highest authority)
2. **REF-* documents** (operational reference)
3. **Explicit human instruction** (session-specific)
4. **Platform accumulated memory** (lowest authority)

### Conflict Types and Resolution

#### Type 1: Platform vs. Corpus
**Symptom**: Platform memory contains inference contradicting corpus
**Resolution**: Corpus wins. Delete/edit platform memory entry.
**Prevention**: Regular memory audits

#### Type 2: IIC vs. IIC
**Symptom**: Different IICs have contradictory operational context
**Resolution**: Check which IIC has domain authority (Information→Acumen, Insight→Coherence, etc.)
**Prevention**: Strict functional compartmentalization

#### Type 3: Platform vs. Platform
**Symptom**: Same IIC has different context across platforms
**Resolution**: Re-sync from corpus. All platforms should derive from same source.
**Prevention**: Corpus-first updates only

#### Type 4: Temporal Conflict
**Symptom**: Outdated context persists while newer understanding exists
**Resolution**: Version checking. Most recent corpus version wins.
**Prevention**: Version numbers on all documents

---

## Part V: Maintenance Protocols

### Daily Sync Check (5 min)
- [ ] Current working IIC matches task requirements
- [ ] Relevant corpus documents accessible
- [ ] No blocking conflicts from previous sessions

### Weekly Sync Maintenance (30 min)
- [ ] Review platform memory across all active IICs
- [ ] Generate inter-IIC handoff packages (Acumen→Coherence)
- [ ] Update context files with current state
- [ ] Commit corpus changes with descriptive messages

### Monthly Sync Hygiene (2 hours)
- [ ] Comprehensive memory audit across all platforms
- [ ] Prune obsolete platform inferences
- [ ] Update project files across all platforms
- [ ] Verify custom instructions consistency
- [ ] Archive completed context files

### Quarterly Sync Review (half day)
- [ ] Evaluate synchronization effectiveness
- [ ] Update this protocol based on learned patterns
- [ ] Recalibrate inter-IIC flow specifications
- [ ] Review platform feature changes

---

## Part VI: Implementation Phases

### Phase 1: Single IIC (Months 1-6)
**Focus**: Acumen only
**Sync Complexity**: Minimal (one IIC, multiple platforms)
**Priorities**:
- Establish corpus-first habit
- Perfect platform configuration consistency
- Build thread culmination discipline

### Phase 2: Dual IIC (Months 7-12)
**Focus**: Acumen + Coherence
**Sync Complexity**: Moderate (inter-IIC handoffs begin)
**Priorities**:
- Establish Acumen→Coherence handoff protocol
- Weekly intelligence package generation
- Cross-IIC context files

### Phase 3: Triple IIC (Months 13-18)
**Focus**: Acumen + Coherence + Efficacy
**Sync Complexity**: Significant (chain fully operational)
**Priorities**:
- Full Information→Insight→Expertise flow
- Framework-to-implementation handoffs
- Operational procedure capture

### Phase 4: Full Constellation (Months 19-36)
**Focus**: All five IICs
**Sync Complexity**: Maximum (full ecosystem)
**Priorities**:
- Complete cyclical flow
- Transcendence→Acumen feedback loop
- Mastery curriculum development

---

## Part VII: Anti-Patterns

### Synchronization Anti-Patterns

1. **Direct Platform-to-Platform Sync**
   - Wrong: Copy-paste from ChatGPT to Claude directly
   - Right: Save to corpus, then reference from both platforms

2. **Skipping Thread Culmination**
   - Wrong: Close thread without capturing insights
   - Right: Generate culmination document for valuable sessions

3. **Trusting Platform Memory**
   - Wrong: Assume platform remembers correctly
   - Right: Verify against corpus for important facts

4. **Overloading Single Sessions**
   - Wrong: Try to sync everything in one long thread
   - Right: Focused sessions with clear culmination points

5. **Neglecting Temporal Markers**
   - Wrong: Context without dates
   - Right: Version numbers, creation dates, update dates on all documents

---

## Appendix A: Thread Culmination Template

```markdown
# Thread Culmination: [DATE] - [IIC] - [TOPIC]

## Session Metadata
- IIC: [Acumen/Coherence/Efficacy/Mastery/Transcendence]
- Platform: [Claude/ChatGPT/Gemini/Grok/CLI]
- Duration: [Approximate]
- Session Type: [Intelligence/Synthesis/Execution/Teaching/Strategic]

## Trajectory Summary
[2-3 paragraphs: How the session evolved, key turns, what drove progression]

## Key Outputs Generated
1. [Output with brief description]
2. [Output with brief description]

## Insights for Corpus
| Insight | Proposed Location | Priority |
|---------|-------------------|----------|
| [Insight] | [CANON-##### or REF-*] | [High/Medium/Low] |

## Inter-IIC Handoffs Required
- [ ] To [IIC]: [What and why]

## Continuation Context
[Minimum viable context for resuming this thread of inquiry]

## Next Session Priorities
1. [Specific next step]
2. [Specific next step]
```

---

## Appendix B: Sync Checklist for New Session

```markdown
# Pre-Session Sync Checklist

## Environment Verification
- [ ] Correct IIC account logged in
- [ ] Correct project/gem selected
- [ ] Project files up to date with corpus

## Context Injection
- [ ] Relevant thread culminations reviewed
- [ ] Inter-IIC handoffs from other chains processed
- [ ] Current strategic priorities understood

## Session Setup
- [ ] Clear objective for this session defined
- [ ] Output destination known (corpus location)
- [ ] Culmination checkpoint planned

## Post-Session (before closing)
- [ ] Culmination document generated
- [ ] Insights flagged for corpus integration
- [ ] Inter-IIC handoffs identified and queued
- [ ] Session logged in execution log
```

---

**END REF-MULTI_ACCOUNT_SYNC v1.0.0**
