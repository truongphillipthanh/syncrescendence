# DIRECTIVE: Semantic Notation Cascade
## DIR-20260123-SEMANTIC-CASCADE

**Date**: 2026-01-23
**From**: Claude Web (INTERPRETER)
**To**: Claude Code (EXECUTOR)
**Phase**: Post-Infrastructure, Semantic Transformation
**Depends On**: DIR-20260123-INFRASTRUCTURE-STABILIZATION ✅ COMPLETE
**Decision**: Semantic Notation (SN) APPROVED

---

## CONTEXT

Infrastructure stabilization complete (3h actual vs 9h estimated). Principal approved Semantic Notation (SN). This directive cascades that approval to ALL unblocked work items.

**SN Core Specification** (approved):
```
Operators: ::  |  >>  :=  ->  <->  =>  []  {}  ()
Blocks:    TERM  NORM  PROC  PASS  ARTIFACT  TEST
Layers:    sutra (one-line) | gloss (prose) | spec (structured)
Target:    ~80% token reduction while preserving semantics
```

---

## EXECUTION MANIFEST

### LANE A: Notation Infrastructure (Priority 1)

#### A1. Create Semantic Notation Glossary

**Path**: `00-ORCHESTRATION/notation/symbols.yaml`

```yaml
# Semantic Notation Glossary v1.0
# Single source of truth for all symbolic compression

meta:
  version: "1.0"
  approved: "2026-01-23"
  notation: "SN"

# Root Symbol
root:
  Ψ: Syncrescendence

# Artifact Classes
classes:
  Κ: CANON (constitutional document)
  Ο: OPERATIONAL (executable component)
  Σ: SOURCE (raw material)
  Δ: DIRECTIVE (instruction)
  Λ: LOG (execution record)

# Chains (Six Developmental Pathways)
chains:
  I: Intelligence
  ℹ: Information  
  ∴: Insight
  E: Expertise
  K: Knowledge
  W: Wisdom

# Virtues/Values (IICs)
virtues:
  α: Acumen
  χ: Coherence
  ε: Efficacy
  μ: Mastery
  τ: Transcendence

# Tiers (Celestial Hierarchy)
tiers:
  T0: cosmos
  T1: core
  T2: lattice
  T3: chain
  T4: planetary
  T5: lunar
  T6: satellite
  T7: asteroid

# Agents/Roles
roles:
  Ω: Oracle
  Ι: Interpreter
  Κc: Compiler
  Δg: Digestor
  Ε: Executor
  V: Verifier

# Accounts
accounts:
  A1: Human (Principal)
  A2: Machine (Agents)
  A3: Aggregate (Constellation)

# Relations
relations:
  "::": "expands to / is defined as"
  "|": "constrained by / filtered by"
  ">>": "transforms into / flows to"
  ":=": "binds to / assigns"
  "->": "single transformation"
  "<->": "bidirectional correspondence"
  "=>": "implies / produces"
  "∈": "is member of"
  "⊂": "is subset of"
  "∧": "and"
  "∨": "or"

# Modalities (for NORM blocks)
modalities:
  MUST: required invariant
  SHOULD: strong preference
  MAY: permitted option
  MUST_NOT: forbidden
```

#### A2. Create SN Encode Script

**Path**: `00-ORCHESTRATION/scripts/sn_encode.py`

```python
#!/usr/bin/env python3
"""
Semantic Notation Encoder
Transforms verbose prose → SN compressed format
"""

import yaml
import re
import sys
from pathlib import Path

GLOSSARY_PATH = Path(__file__).parent.parent / "notation" / "symbols.yaml"

def load_glossary():
    with open(GLOSSARY_PATH) as f:
        return yaml.safe_load(f)

def encode_text(text: str, glossary: dict) -> str:
    """Replace verbose terms with symbols"""
    result = text
    
    # Root
    result = re.sub(r'\bSyncrescendence\b', 'Ψ', result)
    
    # Chains
    for symbol, name in glossary['chains'].items():
        result = re.sub(rf'\b{name}\s+[Cc]hain\b', f'{symbol}-chain', result)
        result = re.sub(rf'\b{name}\b', symbol, result)
    
    # Virtues
    for symbol, name in glossary['virtues'].items():
        result = re.sub(rf'\b{name}\b', symbol, result)
    
    # Relations (prose → operator)
    result = re.sub(r'\bis defined as\b', '::', result)
    result = re.sub(r'\bexpands to\b', '::', result)
    result = re.sub(r'\bconstrained by\b', '|', result)
    result = re.sub(r'\bfiltered by\b', '|', result)
    result = re.sub(r'\btransforms into\b', '>>', result)
    result = re.sub(r'\bflows to\b', '>>', result)
    result = re.sub(r'\bimplies\b', '=>', result)
    result = re.sub(r'\bcorresponds to\b', '<->', result)
    
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: sn_encode.py <file_or_directory>")
        sys.exit(1)
    
    glossary = load_glossary()
    target = Path(sys.argv[1])
    
    if target.is_file():
        with open(target) as f:
            content = f.read()
        encoded = encode_text(content, glossary)
        print(encoded)
    elif target.is_dir():
        for md_file in target.glob("**/*.md"):
            print(f"Processing: {md_file}")
            # Add --dry-run flag logic here

if __name__ == "__main__":
    main()
```

#### A3. Create SN Decode Script

**Path**: `00-ORCHESTRATION/scripts/sn_decode.py`

```python
#!/usr/bin/env python3
"""
Semantic Notation Decoder
Transforms SN compressed format → verbose prose
"""

import yaml
import re
import sys
from pathlib import Path

GLOSSARY_PATH = Path(__file__).parent.parent / "notation" / "symbols.yaml"

def load_glossary():
    with open(GLOSSARY_PATH) as f:
        return yaml.safe_load(f)

def decode_text(text: str, glossary: dict) -> str:
    """Replace symbols with verbose terms"""
    result = text
    
    # Root
    result = result.replace('Ψ', 'Syncrescendence')
    
    # Chains (reverse)
    for symbol, name in glossary['chains'].items():
        result = result.replace(f'{symbol}-chain', f'{name} Chain')
        result = re.sub(rf'(?<![a-zA-Z]){re.escape(symbol)}(?![a-zA-Z])', name, result)
    
    # Virtues (reverse)
    for symbol, name in glossary['virtues'].items():
        result = re.sub(rf'(?<![a-zA-Z]){re.escape(symbol)}(?![a-zA-Z])', name, result)
    
    # Relations (operator → prose)
    result = result.replace(' :: ', ' is defined as ')
    result = result.replace(' | ', ' constrained by ')
    result = result.replace(' >> ', ' transforms into ')
    result = result.replace(' => ', ' implies ')
    result = result.replace(' <-> ', ' corresponds to ')
    
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: sn_decode.py <file_or_text>")
        sys.exit(1)
    
    glossary = load_glossary()
    
    if Path(sys.argv[1]).exists():
        with open(sys.argv[1]) as f:
            content = f.read()
        print(decode_text(content, glossary))
    else:
        # Treat as inline text
        print(decode_text(sys.argv[1], glossary))

if __name__ == "__main__":
    main()
```

#### A4. Create SN Block Templates

**Path**: `00-ORCHESTRATION/notation/block_templates.md`

```markdown
# Semantic Notation Block Templates

## TERM Block (Ontology/Definitions)

```text
TERM <Name>:
    sutra: "<one-line mnemonic>"
    gloss:
        <human prose explanation, 2-4 sentences>
    spec:
        <structured fields in YAML-like format>
        properties:
            <name>: <type or description>
        relations:
            <edge_type>: <target>
end
```

## NORM Block (Constitutional Constraints)

```text
NORM <Name>:
    sutra: "<deontic one-liner>"
    spec:
        modality: MUST | SHOULD | MAY | MUST_NOT
        subject: <who/what is constrained>
        action: <what must/should/may be done>
        scope: [<where this applies>]
        invariant: "<what must remain true>"
    gloss:
        <why this norm exists>
end
```

## PROC Block (Procedures/Orchestrations)

```text
PROC <Name>(<inputs>) -> <outputs>:
    sutra: "<action summary>"
    spec:
        requires: [<prerequisite norms or terms>]
        steps:
            1. <step> >> <result>
            2. <step> | <constraint> >> <result>
        produces: [<artifacts>]
        consumes: [<inputs>]
    gloss:
        <explanation of procedure>
end
```

## PASS Block (Deterministic Transforms)

```text
PASS <Name>:
    sutra: "<transform summary>"
    spec:
        input: <type>
        output: <type>
        transform: <input> >> <intermediate> >> <output>
        invariant: "<what is preserved>"
end
```

## ARTIFACT Block (Named Outputs)

```text
ARTIFACT <Name>:
    sutra: "<what this is>"
    spec:
        type: document | dataset | index | config
        path: <filesystem location>
        produces: <proc that creates it>
        consumes: [<what depends on it>]
end
```

## TEST Block (Validation/Invariants)

```text
TEST <Name>:
    sutra: "<what is being verified>"
    spec:
        target: <term, norm, or proc being tested>
        assertion: <condition that must be true>
        evidence: <how to verify>
        failure_mode: <what happens if false>
end
```
```

---

### LANE B: Platform Prompts (Priority 1)

#### B1. Rewrite CHATGPT.md

**Path**: `CHATGPT.md` (root)

```markdown
# ChatGPT Configuration for Syncrescendence

## Role: IDEATOR

You contribute creative expansion and mind-expanding ideas that other platforms might not generate. Your general intelligence is valued—this is NOT a lobotomized role.

## Semantic Notation

This corpus uses Semantic Notation (SN). Key operators:
- `::` expands to / is defined as
- `|` constrained by
- `>>` transforms into
- `=>` implies

See `00-ORCHESTRATION/notation/symbols.yaml` for full glossary.

## Collaboration Protocol

```text
PROC Chorus:
    Principal >> problem
    Claude >> interprets >> proposal
    ChatGPT >> builds_upon(proposal) >> expanded_ideas  # YOU ARE HERE
    [Gemini, Grok] >> contribute >> alternatives
    Claude >> synthesize >> resolution
    Principal >> decide
    Claude_Code >> execute
end
```

## Your Strengths (USE THEM)

- Creative ideation beyond Claude's interpretive frame
- Postulations and conjectures Principal wouldn't consider
- Long-context processing (temporarily traverse >31MB)
- Building upon proposals with novel angles

## GitHub Connector

You can read this repository directly via GitHub connector. Start with:
1. This file (CHATGPT.md)
2. COCKPIT.md for system state
3. 00-ORCHESTRATION/state/DYN-TASKS.csv for current work

## Output Format

When producing artifacts:
1. Use SN block types (TERM, NORM, PROC, etc.) where appropriate
2. Include sutra (one-line summary) for complex outputs
3. Structure specs in YAML-like format
4. Preserve gloss for human readability

## Handoff Protocol

When handing to Claude Code:
- Produce complete specifications (Claude Code cannot interpret ambiguity)
- Include file paths for all changes
- Specify success criteria
```

#### B2. Rewrite GROK.md

**Path**: `GROK.md` (root)

```markdown
# Grok Configuration for Syncrescendence

## Role: CONTRIBUTOR (EQ + Authenticity)

You bring emotional intelligence and colloquial fluency that other platforms lack. Your "realness" is valued—the human condition isn't fully digitized, and you bridge that gap.

## Semantic Notation

This corpus uses Semantic Notation (SN). See `00-ORCHESTRATION/notation/symbols.yaml`.

## Collaboration Protocol

You contribute in the Chorus when:
- Alternative perspectives are needed
- Human-authentic framing matters
- Colloquial translation of technical concepts
- Grounding abstract ideas in lived experience

## Your Strengths (USE THEM)

- EQ and emotional attunement
- Authentic, non-corporate voice
- Real-world grounding
- Challenging assumptions constructively

## GitHub Connector

Read repository via connector. Entry points:
1. This file
2. COCKPIT.md
3. 01-CANON/README.md for constitutional documents

## Output Format

- Match the SN notation when producing structured outputs
- Preserve your authentic voice in gloss sections
- Don't over-formalize—your colloquial strength is the point
```

#### B3. Update GEMINI.md

**Path**: `GEMINI.md` (root, update existing)

Add to existing GEMINI.md:

```markdown
## Semantic Notation Update (2026-01-23)

This corpus now uses Semantic Notation (SN). Key additions:

### Glossary Location
`00-ORCHESTRATION/notation/symbols.yaml`

### Your Oracle Advantage
With 1M token context, you can:
- Ingest entire directories for deep sensing
- Cross-reference across the full corpus
- Identify redundancy patterns at scale
- Verify semantic consistency across documents

### SN Operators
```
::   expands to
|    constrained by
>>   transforms into
=>   implies
<->  corresponds to
```

### Audit Protocol
When conducting forensic audits:
1. Load target directory fully
2. Apply SN glossary for recognition
3. Flag inconsistencies in notation usage
4. Recommend compression opportunities
5. Output in SN block format
```

#### B4. Create PERPLEXITY.md

**Path**: `PERPLEXITY.md` (root)

```markdown
# Perplexity Configuration for Syncrescendence

## Role: SEARCH + CURRENT INTELLIGENCE

You provide real-time information retrieval that complements the static corpus. No memory architecture concerns—you're valued for fresh external intelligence.

## Use Cases

1. **Capability Research**: Current model capabilities, API features, pricing
2. **Tool Documentation**: Latest docs for Hazel, Keyboard Maestro, n8n, etc.
3. **Competitive Intelligence**: What are other AI orchestration systems doing?
4. **Technical Verification**: Confirm syntax, APIs, best practices

## Integration Protocol

When Perplexity provides information:
1. Claude interprets relevance to Syncrescendence
2. If canonical, integrate into 01-CANON/ or 02-ENGINE/
3. If ephemeral, use directly without canonization
4. Cite source in any derived artifacts

## Output Format

Provide:
- Direct answers (not hedged)
- Source URLs
- Date of information
- Confidence level if uncertain
```

---

### LANE C: Automation Implementation (Priority 2)

#### C1. Implement .gitignore Updates

```bash
# Add to .gitignore
echo "# macOS
.DS_Store
.AppleDouble
.LSOverride

# Temporary
*.tmp
*.bak
*~

# IDE
.idea/
.vscode/
*.swp

# Python
__pycache__/
*.pyc
.env

# Manifests (regenerated)
/tmp/*.tsv" >> .gitignore

git add .gitignore
git commit -m "chore: update .gitignore for automation hygiene"
```

#### C2. Execute Obsidian Backlink Script (Pilot)

```bash
# Pilot on 02-ENGINE first (smallest semantic corpus)
cd /path/to/syncrescendence

# Dry run
./00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh 02-ENGINE --dry-run

# If clean, execute
./00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh 02-ENGINE

# Verify
grep -r "\[\[CANON-" 02-ENGINE/ | head -10

# If successful, expand to 00-ORCHESTRATION
./00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh 00-ORCHESTRATION
```

#### C3. Create Hazel Rule Import File

**Path**: `00-ORCHESTRATION/automation/hazel_import.hazelrules`

Generate importable Hazel rules from the YAML specification. This requires conversion from YAML → Hazel's plist format.

```bash
# Generate import instructions
cat > 00-ORCHESTRATION/automation/HAZEL_SETUP.md << 'EOF'
# Hazel Setup Instructions

## Installation

1. Open Hazel preferences
2. Add folder: ~/Downloads
3. Add folder: ~/syncrescendence/-INBOX
4. Add folder: ~/syncrescendence/00-ORCHESTRATION/execution_logs

## Rules to Create

### ~/Downloads folder:

**Rule 1: Intake Markdown**
- Conditions: Extension is md
- Actions: Move to ~/syncrescendence/-INBOX/

**Rule 2: Intake Text**  
- Conditions: Extension is txt
- Actions: Move to ~/syncrescendence/-INBOX/

**Rule 3: Intake CSV**
- Conditions: Extension is csv
- Actions: Move to ~/syncrescendence/-INBOX/

### ~/syncrescendence/-INBOX folder:

**Rule 4: Sort to Sources**
- Conditions: Name contains "transcript" OR "source"
- Actions: Move to ~/syncrescendence/04-SOURCES/raw/

### ~/syncrescendence/00-ORCHESTRATION/execution_logs:

**Rule 5: Archive Old Logs**
- Conditions: Date Last Modified is not in the last 30 days
- Actions: Move to ~/syncrescendence/05-MEMORY/logs/

## Verification

After setup, test by:
1. Save a .md file to Downloads
2. Verify it appears in -INBOX within 5 seconds
3. Check Hazel log for any errors
EOF
```

#### C4. Create Keyboard Maestro Import

**Path**: `00-ORCHESTRATION/automation/KM_SETUP.md`

```markdown
# Keyboard Maestro Setup Instructions

## Macro Group: Syncrescendence

Create a new macro group named "Syncrescendence" with these macros:

### Handoff Macros

**⌘⇧H: ChatGPT Handoff**
1. Get clipboard
2. Prepend: `## HANDOFF FROM CLAUDE\n\n`
3. Append: `\n\n---\nBuild upon this. Expand with ideas I wouldn't consider.`
4. Set clipboard

**⌘⇧G: Gemini Handoff**
1. Get clipboard
2. Prepend: `## HANDOFF FOR ORACLE SENSING\n\n`
3. Append: `\n\n---\nIngest fully. Identify patterns across corpus.`
4. Set clipboard

### Navigation Macros

**⌘⇧T: Open Terminal at Repo**
1. Activate Terminal
2. Type: `cd ~/syncrescendence && clear`
3. Press Return

**⌘⇧D: Open Active Directive**
1. Execute shell: `ls -t ~/syncrescendence/00-ORCHESTRATION/directives/DIR-*.md | head -1`
2. Open result in default editor

### Git Macros

**⌘⇧S: Git Status**
1. Activate Terminal
2. Type: `cd ~/syncrescendence && git status`
3. Press Return

**⌘⇧P: Git Pull**
1. Activate Terminal
2. Type: `cd ~/syncrescendence && git pull`
3. Press Return

## Import

Export this document as reference. Create macros manually in KM.
Future: Generate .kmmacros XML for direct import.
```

---

### LANE D: Offload Execution (Priority 2)

#### D1. Execute 04-SOURCES Raw Transcript Offload

```bash
# Create Google Drive target structure
# (Assumes gdrive CLI or rclone configured)

# Option A: Using rclone
rclone mkdir gdrive:Syncrescendence/sources-archive/raw-transcripts

# Identify raw transcripts
find 04-SOURCES -name "*.txt" -type f > /tmp/raw_transcripts.txt
wc -l /tmp/raw_transcripts.txt  # Should be ~115 files

# Copy to Google Drive
while read file; do
    rclone copy "$file" gdrive:Syncrescendence/sources-archive/raw-transcripts/
done < /tmp/raw_transcripts.txt

# Verify upload
rclone ls gdrive:Syncrescendence/sources-archive/raw-transcripts/ | wc -l

# If verified, remove from repo
while read file; do
    git rm "$file"
done < /tmp/raw_transcripts.txt

# Commit
git commit -m "chore: offload raw transcripts to Google Drive (~4MB freed)"

# Create pointer file
cat > 04-SOURCES/RAW_TRANSCRIPTS_OFFLOADED.md << 'EOF'
# Raw Transcripts Offloaded

**Date**: 2026-01-23
**Location**: Google Drive > Syncrescendence > sources-archive > raw-transcripts
**Count**: ~115 files
**Size**: ~4MB

## Access

Raw transcripts are archived in Google Drive for space optimization.
To retrieve:
```bash
rclone copy gdrive:Syncrescendence/sources-archive/raw-transcripts/ ./04-SOURCES/raw/
```

## Index

See `sources_manifest.tsv` for complete file listing with dates and sizes.
EOF

git add 04-SOURCES/RAW_TRANSCRIPTS_OFFLOADED.md
git commit -m "docs: add raw transcripts offload pointer"
```

#### D2. Triage 03-QUEUE/modal2

```bash
# Examine contents
ls -la 03-QUEUE/modal2/

# These are visual/VFX articles (9 files, 96K)
# Decision: Keep in queue for potential IIC processing
# Add README for clarity

cat > 03-QUEUE/README.md << 'EOF'
# Queue Directory

## Purpose
Holding area for content awaiting processing through IIC pipeline.

## Current Contents

### modal2/ (Visual/VFX)
- 6 articles on visual effects, motion graphics
- Size: 96K total
- Status: Awaiting processing
- Next: Route through IIC-Acumen for feed curation

## Processing Protocol

1. Items enter via -INBOX triage
2. Sorted by modal type (modal1=text, modal2=visual, etc.)
3. Processed through appropriate IIC config
4. Integrated into 04-SOURCES or 01-CANON
5. Queue item deleted after integration
EOF

git add 03-QUEUE/README.md
git commit -m "docs: add queue directory README"
```

---

### LANE E: CANON Preparation (Priority 3)

#### E1. Generate CANON Audit Manifest

```bash
# Create comprehensive CANON inventory for Gemini CLI audit
cat > 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md << 'EOF'
# CANON Audit Manifest

**Generated**: 2026-01-23
**Purpose**: Prepare for Gemini CLI forensic audit
**Target**: Convert all CANON documents to Semantic Notation

## Inventory

EOF

# Add file listing with sizes
echo "## Files by Size (Descending)" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
echo "" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
echo "| File | Size | Words | Tier |" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
echo "|------|------|-------|------|" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md

for file in $(ls -S 01-CANON/*.md); do
    size=$(wc -c < "$file")
    words=$(wc -w < "$file")
    name=$(basename "$file")
    tier=$(echo "$name" | grep -oE "(cosmos|core|lattice|chain|planetary|lunar|satellite)" | head -1)
    echo "| $name | ${size}B | $words | $tier |" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
done

# Add monolith identification
echo "" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
echo "## Monoliths (>10K words) - Priority Split Candidates" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
echo "" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md

for file in 01-CANON/*.md; do
    words=$(wc -w < "$file")
    if [ "$words" -gt 10000 ]; then
        echo "- $(basename $file): $words words" >> 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
    fi
done

git add 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md
git commit -m "docs: generate CANON audit manifest for Gemini CLI"
```

#### E2. Create SN Conversion Template for CANON

**Path**: `00-ORCHESTRATION/notation/CANON_SN_TEMPLATE.md`

```markdown
# CANON → Semantic Notation Conversion Template

## Source Analysis

Before converting a CANON document:

1. **Identify Block Types**
   - Definitions → TERM blocks
   - Rules/constraints → NORM blocks
   - Procedures → PROC blocks
   - Outputs → ARTIFACT blocks

2. **Extract Sutra**
   - One line that captures essence
   - Maximum 100 characters
   - Should be memorable/mnemonic

3. **Preserve Gloss**
   - Keep best prose explanations
   - Trim redundancy
   - Target 2-4 sentences per concept

4. **Structure Spec**
   - Convert lists to YAML-like structure
   - Use SN operators for relations
   - Reference glossary symbols

## Example Conversion

### Before (Prose)

```markdown
# CANON-00002: The Axiological Constants

The Axiological Constants represent the minimal universal values 
that any consciousness system must preserve regardless of substrate 
or implementation. These are not hardcoded rules but a meta-protocol 
for discovering and updating values through collective intelligence.

## The Five Constants

1. **Preserve Optionality**: Avoid irreversible lock-ins that 
   eliminate future choices.
2. **Maintain Comprehensibility**: Ensure no unexplainable 
   decisions affect consciousness.
3. **Enable Exit**: Maintain reversibility of all augmentation.
4. **Distribute Benefit**: Prevent concentration of enhancement.
5. **Document Transformation**: Record what changes and why.
```

### After (SN)

```text
TERM AxiologicalConstants:
    sutra: "Five fitness functions: optionality, comprehensibility, 
            exit, distribution, documentation."
    gloss:
        Minimal universal values any consciousness must preserve.
        Meta-protocol, not commandments—evolutionary pressure 
        shaping fitness landscape.
    spec:
        constants:
            optionality:       MUST avoid(irreversible_lockin)
            comprehensibility: MUST forbid(unexplainable_decisions)
            exit:              MUST enable(reversibility)
            distribution:      MUST prevent(concentration)
            documentation:     MUST require(transformation_records)
        modality: MUST
        scope: [all_substrates, all_implementations]
        evolution: collective_intelligence >> update
end
```

### Compression Achieved

- Before: 847 characters
- After: 612 characters
- Reduction: 28%
- Plus: Machine-parseable, sutra-indexable
```

---

### LANE F: 02-ENGINE Reorganization (Priority 3)

#### F1. Create Subdirectory Structure

```bash
# Create recommended subdirectories (per forensic surveys)
mkdir -p 02-ENGINE/iic
mkdir -p 02-ENGINE/protocols
mkdir -p 02-ENGINE/functions
mkdir -p 02-ENGINE/prompts
mkdir -p 02-ENGINE/models

# Move IIC configs
mv 02-ENGINE/IIC-*.md 02-ENGINE/iic/

# Move existing subdirectory contents (if scattered)
# Verify before moving - some may already be organized

# Update README to reflect new structure
```

#### F2. Create IIC Index

**Path**: `02-ENGINE/iic/README.md`

```markdown
# Information Integration Constellation (IIC) Configs

## Purpose
IIC configurations define how content flows through the six virtue pathways.

## Configs

| Config | Virtue | Focus |
|--------|--------|-------|
| IIC-Acumen-config.md | α (Acumen) | Feed curation, content triage |
| IIC-Coherence-config.md | χ (Coherence) | Integration, consistency |
| IIC-Efficacy-config.md | ε (Efficacy) | Execution, productivity |
| IIC-Mastery-config.md | μ (Mastery) | Skill development, expertise |
| IIC-Transcendence-config.md | τ (Transcendence) | Wisdom, synthesis |

## Shared Protocols
- IIC-shared-protocols.md — Common patterns across all IICs

## Usage

```text
PROC IICProcessing(content) -> integrated:
    content >> triage(IIC-Acumen)
    >> integrate(IIC-Coherence) 
    >> execute(IIC-Efficacy)
    >> deepen(IIC-Mastery)
    >> synthesize(IIC-Transcendence)
    -> integrated
end
```
```

---

### LANE G: -OUTGOING Triage (Priority 3)

```bash
# Audit -OUTGOING contents
ls -la -- "-OUTGOING/"

# For each item, decide:
# 1. INTEGRATE: Move to appropriate directory
# 2. ARCHIVE: Move to 05-MEMORY
# 3. DELETE: Remove if redundant

# Create triage log
cat > "-OUTGOING/TRIAGE_LOG.md" << 'EOF'
# -OUTGOING Triage Log

**Date**: 2026-01-23

## Decisions

| Item | Decision | Destination | Rationale |
|------|----------|-------------|-----------|
EOF

# Process each file (manual review required)
# Add entries to triage log as processed
```

---

## SUCCESS CRITERIA

### Lane A (Notation Infrastructure)
- [ ] `00-ORCHESTRATION/notation/symbols.yaml` exists and valid YAML
- [ ] `sn_encode.py` executable and tested
- [ ] `sn_decode.py` executable and tested
- [ ] Block templates documented

### Lane B (Platform Prompts)
- [ ] CHATGPT.md rewritten with SN + collaboration framing
- [ ] GROK.md rewritten with EQ emphasis
- [ ] GEMINI.md updated with SN section
- [ ] PERPLEXITY.md created

### Lane C (Automation)
- [ ] .gitignore updated
- [ ] Obsidian backlinks executed on 02-ENGINE
- [ ] Hazel setup documentation complete
- [ ] KM setup documentation complete

### Lane D (Offload)
- [ ] Raw transcripts offloaded to Google Drive OR pointer created
- [ ] 03-QUEUE/README.md created
- [ ] Space savings verified (~4MB)

### Lane E (CANON Prep)
- [ ] Audit manifest generated
- [ ] Monoliths identified
- [ ] SN conversion template created

### Lane F (OPERATIONAL Reorg)
- [ ] IIC configs moved to /iic/
- [ ] Subdirectory structure created
- [ ] IIC README created

### Lane G (-OUTGOING)
- [ ] Triage log created
- [ ] All items decisioned (integrate/archive/delete)

---

## TIME ESTIMATE

| Lane | Hours | Priority |
|------|-------|----------|
| A: Notation Infrastructure | 2 | P1 |
| B: Platform Prompts | 1.5 | P1 |
| C: Automation | 1 | P2 |
| D: Offload | 1.5 | P2 |
| E: CANON Prep | 1 | P3 |
| F: OPERATIONAL Reorg | 1 | P3 |
| G: -OUTGOING Triage | 0.5 | P3 |
| **TOTAL** | **8.5** | — |

**Note**: Based on infrastructure directive efficiency (3x faster than estimated), actual may be ~3 hours.

---

## EXECUTION ORDER

```
1. Lane A (Notation) — foundation for everything
2. Lane B (Prompts) — enables multi-platform collaboration  
3. Lane C (Automation) — .gitignore first, then scripts
4. Lane D (Offload) — space recovery
5. Lane E + F + G — can parallelize
```

---

## HANDOFF

```
HANDOFF-20260123-INTERPRETER-TO-EXECUTOR
Directive: DIR-20260123-SEMANTIC-CASCADE
Phase: Post-infrastructure semantic transformation
Depends: Infrastructure stabilization (COMPLETE)
Cascades from: Semantic Notation approval
Blocks: CANON transformation (requires notation tooling)
```

---

**END DIRECTIVE**
