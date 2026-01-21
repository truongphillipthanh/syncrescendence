# Metabolism Map

**Date**: 2026-01-19

This document maps the intended and observed flows for each artifact class.

---

## 1. Prompts

### Intended Flow
```
Entry: -INBOX/ (from ChatGPT/external) or direct creation
  ↓
Processing: Review, add YAML frontmatter, normalize
  ↓
Staging: 02-OPERATIONAL/prompts/{canonical,chatgpt}/
  ↓
Validation: ops_lint.sh (checks frontmatter: id, kind, scope, target)
  ↓
Exit: Active use in ChatGPT/Claude Code sessions
```

### Observed Flow
- **Entry**: `-INBOX/` receives prompts from ChatGPT (e.g., `PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER_updated.md`)
- **Processing**: Manual review, frontmatter addition
- **Location**: `02-OPERATIONAL/prompts/canonical/` (9 files), `02-OPERATIONAL/prompts/chatgpt/` (3 files)
- **Validation**: `ops_lint.sh` verifies frontmatter (currently passing 17 files)
- **Exit**: Copy to ChatGPT project instructions, CLAUDE.md references

### Validators
- `02-OPERATIONAL/scripts/ops_lint.sh` — Frontmatter validation
- Manual review — Content accuracy

---

## 2. Protocols/Specs

### Intended Flow
```
Entry: Design in ChatGPT/Claude Code session
  ↓
Processing: Formalize, add frontmatter, document invariants
  ↓
Staging: 02-OPERATIONAL/specs/ or 00-ORCHESTRATION/state/REF-*
  ↓
Validation: ops_lint.sh, structural_verify.sh
  ↓
Exit: Referenced by prompts, scripts, other protocols
```

### Observed Flow
- **Entry**: Designed via ChatGPT Deviser or Claude Code sessions
- **Processing**: Formalization with version bumps (v2.0.0 → v3.0.0 observed)
- **Locations**:
  - `02-OPERATIONAL/specs/` — REF-AUDIZER_PROTOCOL.md, REF-CHATGPT_MEMORY_POLICY.md
  - `00-ORCHESTRATION/state/` — REF-* protocol files (45 files in state/)
- **Validation**: ops_lint.sh (specs/ checked), structural_verify.sh (constitutional compliance)
- **Exit**: Ripple to dependent files, ChatGPT memory updates

### Validators
- `ops_lint.sh` — Frontmatter validation
- `structural_verify.sh` — Path references, structural integrity

---

## 3. Commands/Scripts

### Intended Flow
```
Entry: Need identified in directive or session
  ↓
Processing: Write script, test locally
  ↓
Staging: .claude/commands/project/ or 00-ORCHESTRATION/scripts/
  ↓
Validation: Manual test, structural_verify.sh
  ↓
Exit: Available as /project:<command> or bash <script>
```

### Observed Flow
- **Entry**: Created during Claude Code sessions
- **Processing**: Written to appropriate location
- **Locations**:
  - `.claude/commands/project/` — Claude Code slash commands (6 files)
  - `00-ORCHESTRATION/scripts/` — Shell/Python scripts (13 files)
  - `02-OPERATIONAL/scripts/` — Operational scripts (3 files)
- **Validation**: Manual testing, structural_verify.sh for path references
- **Exit**: Executed via `/project:` prefix or direct bash invocation

### Validators
- Manual testing
- `structural_verify.sh` — Path validity

---

## 4. Logs/Reports

### Intended Flow
```
Entry: Generated during execution
  ↓
Processing: Timestamped, linked to directive
  ↓
Staging: 00-ORCHESTRATION/execution_logs/ or -OUTGOING/<date>-<slug>/
  ↓
Validation: Structural completeness (directive linkage)
  ↓
Exit: Reference in future sessions, archival
```

### Observed Flow
- **Entry**: Created by Claude Code during directive execution
- **Processing**: Timestamped with EXECUTION_LOG-YYYY-MM-DD-NNN.md format
- **Locations**:
  - `00-ORCHESTRATION/execution_logs/` — 56 execution logs
  - `-OUTGOING/YYYYMMDD-<slug>/` — Bundled reports (SURVEY_REPORT.md, etc.)
- **Validation**: No automated validation; manual review
- **Exit**: Reference in COCKPIT.md, future sessions

### Validators
- Manual review
- Git history for provenance

---

## 5. Evidence Packs

### Intended Flow
```
Entry: Research output from Gemini/Deep Research
  ↓
Processing: Extract key findings, add metadata
  ↓
Staging: 04-SOURCES/raw/ → 04-SOURCES/processed/
  ↓
Validation: sources.csv update, frontmatter check
  ↓
Exit: Integrated into CANON or referenced by directives
```

### Observed Flow
- **Entry**: `-INBOX/` or `04-SOURCES/raw/` (199 raw files)
- **Processing**: Frontmatter addition, signal tier assignment
- **Locations**:
  - `04-SOURCES/raw/` — Unprocessed sources (199 files)
  - `04-SOURCES/processed/` — Processed sources (46 files)
- **Validation**: sources.csv tracking, REF-PROCESSING_PATTERN.md procedure
- **Exit**: Integration into CANON documents, citation

### Validators
- `sources.csv` — Tracking ledger
- Manual review — Signal tier assignment

---

## 6. Registries/Manifests

### Intended Flow
```
Entry: Need for cross-cutting index identified
  ↓
Processing: Enumerate items, add metadata
  ↓
Staging: 02-OPERATIONAL/registries/ or 00-ORCHESTRATION/state/
  ↓
Validation: ops_lint.sh (frontmatter)
  ↓
Exit: Reference for navigation, tooling
```

### Observed Flow
- **Entry**: Created to track artifacts across zones
- **Processing**: Enumeration with metadata
- **Locations**:
  - `02-OPERATIONAL/registries/` — 3 registry files
    - `REF-PROMPT_REGISTRY.md`
    - `REF-OPERATIONS_ARTIFACT_TAXONOMY.md`
    - `REF-OPERATIONS_TREE.md`
- **Validation**: ops_lint.sh checks frontmatter
- **Exit**: Navigation aid, tooling input

### Validators
- `ops_lint.sh` — Frontmatter validation

---

## Validation Gates Summary

| Artifact Class | Entry Gate | Processing Gate | Exit Gate |
|----------------|------------|-----------------|-----------|
| Prompts | Manual review | ops_lint.sh | ChatGPT sync |
| Protocols | Manual review | ops_lint.sh, structural_verify.sh | Ripple verification |
| Commands | Manual test | — | Execution test |
| Logs | — | — | Git commit |
| Evidence | Signal tier | sources.csv | CANON integration |
| Registries | Manual review | ops_lint.sh | Navigation check |

---

## Flow Diagram

```
External Input
     │
     ▼
  -INBOX/
     │
     ├──[prompts]──▶ 02-OPERATIONAL/prompts/
     │                      │
     │                      ▼
     │              ops_lint.sh
     │                      │
     │                      ▼
     │              ChatGPT/Claude
     │
     ├──[sources]──▶ 04-SOURCES/raw/
     │                      │
     │                      ▼
     │              04-SOURCES/processed/
     │                      │
     │                      ▼
     │              01-CANON/
     │
     └──[directives]──▶ -INBOX/blitzkrieg_drop/
                              │
                              ▼
                       00-ORCHESTRATION/directives/
                              │
                              ▼
                       00-ORCHESTRATION/execution_logs/
                              │
                              ▼
                       -OUTGOING/<bundle>/
```
