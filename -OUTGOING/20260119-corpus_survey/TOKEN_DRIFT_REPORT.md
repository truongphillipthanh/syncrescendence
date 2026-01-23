# Token Drift Report

**Date**: 2026-01-19

This report documents legacy and conflicting tokens/aliases found repo-wide.

---

## 1. OUTGOING Path Variants

### Canonical: `-OUTGOING/`
### Legacy: `OUTGOING/`, `outgoing/`

| Classification | File Count | Status |
|----------------|------------|--------|
| Canon surface (prompts, protocols) | 15 | Needs update |
| Evidence (reports, logs) | 24 | Historical—may preserve |
| Scaffold (scripts, commands) | 10 | Needs update |

**Occurrences by File Type**:

| Path | Classification | Notes |
|------|----------------|-------|
| `CLAUDE.md` | Canon | Constitutional doc—references `-OUTGOING/` correctly |
| `COCKPIT.md` | Canon | Navigation index—correct references |
| `00-ORCHESTRATION/scripts/structural_verify.sh` | Scaffold | Contains warning logic for legacy refs |
| `00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md` | Canon | Correct `-OUTGOING/` usage |
| `.claude/commands/project/*.md` | Scaffold | Mixed—some need update |
| `-OUTGOING/*/CODIFY_REPORT.md` | Evidence | Historical reports |
| `-OUTGOING/TURBINE_BAKEOFF_*/*` | Evidence | Bakeoff artifacts |

**Total**: 49 files with `OUTGOING/` or `outgoing/` references
- 18 uppercase `OUTGOING/` (should be `-OUTGOING/`)
- 60 lowercase `outgoing/` (should be `-OUTGOING/`)

---

## 2. INBOX Path Variants

### Canonical: `-INBOX/`
### Legacy: `INBOX/` (without dash)

**Status**: Generally correct. Most references use canonical `-INBOX/`.

**Files with INBOX references**: 30+
- Majority correctly use `-INBOX/`
- Constitutional compliance verified

---

## 3. Audizable Marker Variants

### Canonical (NEW): Final fenced code block (no marker)
### Retired: `===AUDIZABLE===`, `===END===`
### Legacy: `---AUDIZABLE---`, `---END AUDIZABLE---`

**Files Still Containing Legacy Markers**:

| File | Marker Type | Classification |
|------|-------------|----------------|
| `00-ORCHESTRATION/scripts/ingest_chatgpt_container.py` | `===AUDIZABLE===` | Scaffold (parsing logic) |
| `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md` | `===AUDIZABLE===` | Canon (container format docs) |
| `00-ORCHESTRATION/state/REF-CHATGPT_CONTAINER_PROTOCOL.md` | `===AUDIZABLE===` | Canon (retired marker note) |
| `-OUTGOING/20260119-transcript_codefence_canon/RIPPLE_REPORT.md` | `===AUDIZABLE===` | Evidence (ripple report) |
| `-OUTGOING/20260119-tighten_audizable_and_smoketest/*.md` | `===AUDIZABLE===` | Evidence (tighten reports) |
| `-OUTGOING/20260118-codify_validation_and_trifurcation/CODIFY_REPORT.md` | `===AUDIZABLE===` | Evidence (codify report) |
| `-INBOX/claude_code_repo_ripple_prompt.md` | `---AUDIZABLE---` | Scaffold (directive) |
| `.tmp.driveupload/14655.*` | `---AUDIZABLE---` | Temp (ignore) |

**Note**: The 2026-01-19 ripple retired `===AUDIZABLE===` in favor of final-fence convention. Evidence files contain historical references (acceptable). Canon files updated to document the retirement.

---

## 4. Label Variants

### Canonical (NEW): No explicit labels
### Legacy: "Readable version", "Audizable version", "Part 1/Part 2"

**Files Containing Legacy Labels**:

| File | Label Found | Classification |
|------|-------------|----------------|
| `02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-*` | "Readable version" | Canon (prohibition context) |
| `02-ENGINE/specs/REF-AUDIZER_PROTOCOL.md` | "Audizable version" | Canon (prohibition context) |
| `-OUTGOING/*/CODIFY_REPORT.md` | "Readable version" | Evidence (historical) |
| `04-SOURCES/raw/google_research.md` | "Part 1" | Evidence (source doc) |
| `04-SOURCES/raw/DEEP_RESEARCH_PROMPT-*.md` | "Part 1", "Part 2" | Evidence (prompts) |

**Note**: Canon files mention labels in prohibition context ("do not use"). Evidence files may contain legacy usage from historical artifacts.

---

## 5. Organ Name Variants

### Potential Competing Terms

| Concept | Variants Found | Recommendation |
|---------|----------------|----------------|
| Context document | "Context", "context.md" | Standardized |
| Pedigree document | "Pedigree", "pedigree.md" | Standardized |
| ADR | "ADR" (Architecture Decision Record) | Not conflicting—different purpose |

**Files with Pedigree/Context/ADR**:

| File | Term | Context |
|------|------|---------|
| `02-ENGINE/BLITZKRIEG_PROTOCOL.md` | Pedigree, Context | Protocol definition |
| `-INBOX/blitzkrieg_drop/context.md` | Context | Artifact |
| `00-ORCHESTRATION/state/REF-CHATGPT_CONTAINER_PROTOCOL.md` | Pedigree, Context | Container grammar |

**Total**: 65 occurrences across 30 files (healthy—terms are well-defined, not competing)

---

## 6. Config/Coordination Path Drift

### Canonical: `02-ENGINE/coordination.yaml`
### Legacy: `config/coordination`, `config/coordination.yaml`

**Status**: 25 references to `config/coordination` found
- Likely stale post-defrag references
- Needs batch update to `02-ENGINE/coordination.yaml`

---

## Summary Table

| Token Category | Canonical | Legacy/Variants | Files Affected | Action |
|----------------|-----------|-----------------|----------------|--------|
| OUTGOING path | `-OUTGOING/` | `OUTGOING/`, `outgoing/` | 49 | Batch fix |
| INBOX path | `-INBOX/` | `INBOX/` | ~5 | Minor fix |
| Audizable markers | Final fence | `===AUDIZABLE===`, `---AUDIZABLE---` | 9 | Complete ripple |
| Output labels | None | "Readable/Audizable version" | 17 | Evidence OK |
| Organ names | Pedigree/Context | ADR | 30 | No conflict |
| Config path | `02-ENGINE/` | `config/` | 25 | Batch fix |

---

## Classification Legend

- **Canon surface**: Files that define system behavior (prompts, protocols, commands)
- **Evidence**: Historical artifacts, reports, logs (preserve as-is unless misleading)
- **Legacy**: Deprecated patterns that should be updated
- **Scaffold**: Supporting infrastructure (scripts, templates)
