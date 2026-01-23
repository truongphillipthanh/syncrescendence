# DIRECTIVE: Infrastructure Stabilization
## DIR-20260123-INFRASTRUCTURE-STABILIZATION

**Date**: 2026-01-23
**From**: Claude Web (INTERPRETER)
**To**: Claude Code (EXECUTOR)
**Phase**: Pre-Semantic-Compression Infrastructure

---

## CONTEXT

The Principal is evaluating four semantic compression notations (Canon Block IR, RCN, SNL, SLN) for the corpus's content layer. This directive addresses infrastructure and mechanical fixes that are **independent of that decision** and can execute immediately.

These tasks stabilize the corpus foundation so semantic compression has a clean substrate to operate on.

---

## SCOPE: What This Directive Does NOT Touch

- Content of CANON files (will be semantically compressed)
- Platform prompts (CHATGPT.md, GEMINI.md, etc.) - will adopt new notation
- Symbolic glossary implementation - depends on notation choice
- Pseudo-code structures within documents - depends on notation choice

---

## EXECUTION SEQUENCE

### Phase A: Critical Fixes (2 hours)

#### A1. Fix CANON-00011 Identity Collision

```bash
# Verify the collision
grep -n "CANON-00007" 01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md

# Replace all internal references from 00007 to 00011
sed -i 's/CANON-00007/CANON-00011/g' 01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md

# Verify fix
grep -n "CANON-00007" 01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md
# Should return nothing
```

#### A2. Resolve 10 Consistency Violations

Execute these renames/fixes in order:

```bash
# 1. Ledger naming: tasks.csv → DYN-TASKS.csv (if not already done)
# Check current state
ls -la 00-ORCHESTRATION/state/tasks.csv 2>/dev/null
ls -la 00-ORCHESTRATION/state/DYN-TASKS.csv 2>/dev/null

# 2. Queue path: ensure references point to 03-QUEUE/ not QUEUE/
grep -rn "QUEUE/" --include="*.md" 00-ORCHESTRATION/ | grep -v "03-QUEUE"
# Fix any found references

# 3. Sources ledger: ensure DYN-SOURCES.csv is canonical
ls -la 00-ORCHESTRATION/state/*SOURCES*

# 4. Tree generator output: DYN-TREE.md vs DYN-ACTUAL_TREE.md
ls -la 00-ORCHESTRATION/state/DYN-TREE.md
ls -la 00-ORCHESTRATION/state/DYN-ACTUAL_TREE.md
# Determine which is canonical; remove/rename the other

# 5. Coordination path: DYN-COORDINATION.yaml consistency
grep -rn "coordination.yaml" --include="*.md" 00-ORCHESTRATION/
# Update to DYN-COORDINATION.yaml if needed

# 6. Remove .bak files from tracked state
find 00-ORCHESTRATION/state -name "*.bak" -type f
# Move to 05-ARCHIVE or delete after verification

# 7. Duplicate function definitions: integrate.md vs integrate.xml
ls -la 02-OPERATIONAL/*integrate*
# Choose one as canonical, move other to archive

# 8. Execution log location: standardize path references
grep -rn "execution_log" --include="*.md" 00-ORCHESTRATION/
# Ensure all point to 00-ORCHESTRATION/execution_logs/

# 9. Protected path standardization
grep -rn "PROTECTED" --include="*.md" 00-ORCHESTRATION/state/
# Ensure consistent path references

# 10. Prefix standardization in state/
ls 00-ORCHESTRATION/state/ | cut -c1-4 | sort | uniq -c
# Audit ARCH-, DYN-, REF-, SCAFF- distribution
```

### Phase B: Navigation Layer (3 hours)

#### B1. Create 01-CANON/README.md

```markdown
# CANON Index

## Purpose
This directory contains the constitutional documents of Syncrescendence—verified canonical knowledge that is PROTECTED (Principal approval required for modifications).

## Organization by Tier

### Cosmos Tier (00000-00017)
Constitutional documents defining system identity.
| ID | Name | Description |
|----|------|-------------|
| 00000 | SCHEMA | Root type definitions |
| 00001 | ORIGIN | System genesis |
| ... | ... | ... |

### Core Tier (10000-11000)
Gravitational center concepts.

### Lattice Tier (20000-25000)
Structural frameworks and geometries.

### Chain Tier (30000-35000)
Six developmental pathways.
- 30000-30999: INTELLIGENCE chain
- 31000-31999: INFORMATION chain
- 32000-32999: INSIGHT chain
- 33000-33999: EXPERTISE chain
- 34000-34999: KNOWLEDGE chain
- 35000-35999: WISDOM chain

### Planetary/Lunar/Satellite Tiers
Nested within chains by suffix convention.

## Quick Navigation

**To understand the system**: Start with CANON-00000-SCHEMA
**To understand the cosmology**: Read CANON-00005-SYNCRESCENDENCE
**To understand the chains**: See CANON-30000 through CANON-35000 roots

## Naming Convention

`CANON-NNNNN-NAME-tier[-tier[-tier]].md`

Where:
- NNNNN = 5-digit ID (encodes hierarchy)
- NAME = Human-readable descriptor
- tier = cosmos|core|lattice|chain|planetary|lunar|satellite
```

**Action**: Generate this README by scanning actual files in 01-CANON/.

#### B2. Create 00-ORCHESTRATION/README.md

```markdown
# ORCHESTRATION Index

## Purpose
Living infrastructure for system coordination. Contains directives, execution logs, state ledgers, and operational scripts.

## Directory Structure

### /directives/
Active and historical directives. 
- Current: DIRECTIVE-041 through DIRECTIVE-046
- Historical: DIRECTIVE-018 through DIRECTIVE-040 (completed)

### /execution_logs/
Timestamped logs of directive execution.
Format: EXECUTION_LOG-YYYY-MM-DD-NNNX.md

### /state/
Dynamic ledgers and reference documents.
- DYN-* = Dynamic (changes frequently)
- REF-* = Reference (stable, rarely changes)
- ARCH-* = Archaeological (frozen historical record)
- SCAFF-* = Scaffolding (temporary, to be integrated or deleted)

### /scripts/
Automation and utility scripts.

## Quick Start

1. Check active work: See /directives/DIRECTIVE-046*.md
2. Check system state: See /state/DYN-DASHBOARD.md
3. Check task backlog: See /state/DYN-TASKS.csv
```

#### B3. Create 02-OPERATIONAL/README.md

```markdown
# OPERATIONAL Index

## Purpose
Executable components: functions, prompts, protocols, and model configurations. This is the "engine room" of Syncrescendence.

## Directory Structure

### /functions/
Processing functions (integrate, triage, process, etc.)

### /prompts/
LLM prompt templates

### /protocols/
Interaction protocols and handoff procedures

### /models/
Model-specific configurations

### IIC-*.md Files
Information Integration Constellation configurations:
- IIC-Acumen-config.md
- IIC-Coherence-config.md
- IIC-Efficacy-config.md
- IIC-Mastery-config.md
- IIC-Transcendence-config.md
- IIC-shared-protocols.md

## TODO: Reorganization Pending
This directory needs structural cleanup. See DIRECTIVE-046 for planned changes.
```

### Phase C: Infrastructure Protocols (2 hours)

#### C1. Create .github/CONNECTOR_PROTOCOL.md

```markdown
# GitHub Connector Protocol

## Purpose
All three web applications (Claude, ChatGPT, Gemini) can sense directly into this repository via GitHub connectors. This document defines the protocol for that access.

## Capabilities

### Read Access
- All platforms can read any file in the repository
- Connector provides directory listings and file contents
- Token limits apply per-platform

### Write Access
- Claude Web: Read-only via connector; writes via Claude Code CLI
- ChatGPT Web: Read-only via connector
- Gemini Web: Read-only via connector

## Synchronization Protocol

1. **Canonical State**: The `main` branch is ground truth
2. **Platform Reads**: Always read from `main`
3. **Platform Writes**: 
   - Stage changes in appropriate tool (Claude Code, Codex CLI)
   - Commit with descriptive message
   - Push to `main`
   - Other platforms refresh on next query

## Token Economics

When traversing the corpus via connector:
1. Start with entry points (CLAUDE.md, COCKPIT.md)
2. Use grep/search rather than reading entire files
3. Request specific line ranges when possible
4. Cache frequently-accessed documents in thread context

## Platform-Specific Notes

### Claude Web
- Entry point: CLAUDE.md
- Primary focus: Interpretation, specification
- Connector scope: Full repository read

### ChatGPT Web  
- Entry point: CHATGPT.md (to be created)
- Primary focus: Ideation, compilation
- Connector scope: Full repository read

### Gemini Web
- Entry point: GEMINI.md
- Primary focus: Digestion, oracle-scale sensing
- Connector scope: Full repository read
```

#### C2. Create Obsidian Backlink Infrastructure

```bash
# Add [[backlink]] format to cross-references where appropriate
# This makes the corpus Obsidian-navigable

# Example transformation for a CANON file:
# Before: "See CANON-00005 for details"
# After: "See [[CANON-00005-SYNCRESCENDENCE-cosmos]] for details"

# Create script to add backlinks
cat > 00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh << 'EOF'
#!/bin/bash
# Transforms CANON-XXXXX references to [[CANON-XXXXX-*]] backlinks
# Usage: ./add_obsidian_backlinks.sh <directory>

DIR=${1:-.}
find "$DIR" -name "*.md" -exec sed -i -E 's/CANON-([0-9]{5})([^-\]])/[[CANON-\1]]\2/g' {} \;
EOF
chmod +x 00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh
```

### Phase D: Offload Preparation (1 hour)

#### D1. Audit 04-SOURCES for Google Offload

```bash
# Count files and size
find 04-SOURCES -type f | wc -l
du -sh 04-SOURCES

# List file types
find 04-SOURCES -type f -name "*.*" | sed 's/.*\.//' | sort | uniq -c | sort -rn

# Identify raw transcripts (candidates for offload)
find 04-SOURCES -type f -name "*.txt" -o -name "*transcript*" | head -20

# Generate manifest for offload
find 04-SOURCES -type f -printf "%p\t%s\t%T@\n" > /tmp/sources_manifest.tsv
```

#### D2. Audit 03-QUEUE for Offload

```bash
# These are YouTube transcripts - candidates for Google Drive offload
find 03-QUEUE -type f | wc -l
du -sh 03-QUEUE

# Generate manifest
find 03-QUEUE -type f -printf "%p\t%s\t%T@\n" > /tmp/queue_manifest.tsv
```

#### D3. Audit 05-ARCHIVE for Semantic Organization

```bash
# Current state
ls -la 05-ARCHIVE/
find 05-ARCHIVE -type f | wc -l
du -sh 05-ARCHIVE

# Identify duplicates (same content, different names)
find 05-ARCHIVE -type f -exec md5sum {} \; | sort | uniq -d -w32
```

### Phase E: Automation Scaffolding (1 hour)

#### E1. Create Hazel Rule Specifications

```yaml
# 00-ORCHESTRATION/automation/hazel_rules.yaml
rules:
  - name: "Intake from Downloads"
    watch: ~/Downloads
    conditions:
      - extension: [md, txt, pdf, csv]
      - name_contains: [syncrescendence, canon, directive]
    actions:
      - move_to: ~/syncrescendence/-INBOX/
      - notify: "File moved to intake"

  - name: "Archive Completed Logs"
    watch: ~/syncrescendence/00-ORCHESTRATION/execution_logs/
    conditions:
      - date_modified: "> 30 days"
      - name_matches: "EXECUTION_LOG-*"
    actions:
      - move_to: ~/syncrescendence/05-ARCHIVE/logs/
```

#### E2. Create Keyboard Maestro Macro Specifications

```yaml
# 00-ORCHESTRATION/automation/km_macros.yaml
macros:
  - name: "Copy for ChatGPT Handoff"
    trigger: "⌘⇧C"
    actions:
      - get_clipboard
      - prepend: "## HANDOFF FROM CLAUDE\n\n"
      - append: "\n\n---\nContinue from this context."
      - set_clipboard
      
  - name: "Quick Directive Template"
    trigger: "⌘⇧D"
    actions:
      - insert_text: |
          # DIRECTIVE: [NAME]
          ## DIR-YYYYMMDD-[CODE]
          
          **Date**: {{date}}
          **From**: [ROLE]
          **To**: [ROLE]
          
          ## CONTEXT
          
          ## EXECUTION
          
          ## SUCCESS CRITERIA
```

---

## SUCCESS CRITERIA

- [ ] CANON-00011 no longer contains "CANON-00007" internally
- [ ] All 10 consistency violations resolved
- [ ] README.md exists in 01-CANON/, 00-ORCHESTRATION/, 02-OPERATIONAL/
- [ ] .github/CONNECTOR_PROTOCOL.md exists
- [ ] Obsidian backlink script created
- [ ] 04-SOURCES and 03-QUEUE manifests generated
- [ ] Automation rule specifications created

---

## TIME ESTIMATE

| Phase | Hours |
|-------|-------|
| A: Critical Fixes | 2 |
| B: Navigation Layer | 3 |
| C: Infrastructure Protocols | 2 |
| D: Offload Preparation | 1 |
| E: Automation Scaffolding | 1 |
| **TOTAL** | **9** |

---

## DOES NOT REQUIRE PRINCIPAL DECISION

All items in this directive are:
- Mechanical (not semantic)
- Reversible (git safety)
- Foundation work (enables semantic compression later)

Execute without waiting for semantic notation choice.

---

## HANDOFF TOKEN

```
HANDOFF-20260123-INTERPRETER-TO-EXECUTOR
Directive: DIR-20260123-INFRASTRUCTURE-STABILIZATION
Phase: Pre-compression infrastructure
Dependencies: None
Blocks: Nothing (parallel-safe)
```
