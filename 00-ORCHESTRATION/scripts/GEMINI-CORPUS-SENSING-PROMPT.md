# GEMINI CLI CORPUS SENSING SWEEP

## Invocation

```bash
# From repository root
cd /path/to/syncrescendence

# Create output directory
mkdir -p -OUTGOING/$(date +%Y%m%d)-corpus-annealment-survey

# Run sensing sweep (adjust paths as needed)
gemini -p "$(cat 00-ORCHESTRATION/scripts/GEMINI-CORPUS-SENSING-PROMPT.md)" \
  -f "$(find . -name '*.md' -o -name '*.txt' -o -name '*.csv' -o -name '*.yaml' | head -500 | tr '\n' ' ')" \
  > -OUTGOING/$(date +%Y%m%d)-corpus-annealment-survey/SENSING_REPORT.md
```

Alternative if corpus-survey.sh exists:
```bash
./00-ORCHESTRATION/scripts/corpus-survey.sh
```

---

## Prompt (save as `00-ORCHESTRATION/scripts/GEMINI-CORPUS-SENSING-PROMPT.md`)

---

# Corpus Sensing Sweep: Syncrescendence Repository

You are performing a comprehensive sensing operation on a distributed cognition system's knowledge repository. Your role is **DIGESTOR**: you have massive context capacity and must produce ground-truth analysis that other agents (with smaller context windows) can act upon.

## Your Task

Analyze the entire corpus and produce a structured report identifying:

1. **Semantic Clusters** — Groups of documents that address the same concept but may be fragmented, duplicated, or inconsistently named
2. **Strays & Orphans** — Documents that don't fit the taxonomy or reference nothing and are referenced by nothing
3. **Scaffold Residue** — Working documents that served their purpose and should archive (look for prefixes: SCAFF-, WIP-, DRAFT-, TODO-)
4. **Canonization Candidates** — Documents in -INBOX/, -OUTGOING/, or other staging areas that are mature enough for 01-CANON/ or 02-ENGINE/
5. **Hidden Intentions** — Documents in 05-MEMORY/ or elsewhere that contain unexecuted plans, decisions, or insights worth surfacing
6. **Nomenclature Drift** — Inconsistent naming patterns that violate the established conventions (ARCH-, CANON-, REF-, DYN-, etc.)
7. **Duplication Clusters** — Near-identical content across multiple files (semantic duplicates, not just filename matches)
8. **Token Economics** — Documents that exceed reasonable context-load size (>50KB) and should be split or compressed

## Repository Structure Context

```
00-ORCHESTRATION/  — Coordination infrastructure (directives, state, logs, scripts)
01-CANON/          — Constitutional documents (stable, high-value)
02-ENGINE/    — Active working documents (prompts, functions, specs)
03-QUEUE/          — Processing queue (staged for work)
04-SOURCES/        — Source material (raw/, processed/)
05-MEMORY/        — Historical/superseded documents (prefix: ARCH-)
06-EXEMPLA/        — Templates and examples
-INBOX/            — Unsorted incoming (needs triage)
-OUTGOING/         — Execution outputs (timestamped batches)
```

## Naming Conventions (Detect Violations)

- `ARCH-` — Archived, superseded
- `CANON-` — Canonical, stable
- `REF-` — Reference document
- `DYN-` — Dynamic, frequently updated
- `SCAFF-` — Scaffold, temporary
- `DIR-` — Directive
- `TEMPLATE-` — Template file

## Output Format

Produce a single Markdown report with these sections:

```markdown
# Corpus Sensing Report
Generated: [timestamp]
Files Analyzed: [count]
Total Size: [KB]

## Executive Summary
[3-5 sentences: overall corpus health, critical findings, recommended priority actions]

## 1. Semantic Clusters Identified

### Cluster: [Topic Name]
- **Core Document**: [path] — [why it's the anchor]
- **Related**:
  - [path] — [relationship: duplicate | elaboration | outdated version | fragment]
  - [path] — [relationship]
- **Recommendation**: [consolidate | keep separate | archive N of M]

[Repeat for each cluster]

## 2. Strays & Orphans

| File | Location | Issue | Recommendation |
|------|----------|-------|----------------|
| [name] | [path] | [orphan/misplaced/unclear purpose] | [archive/delete/investigate] |

## 3. Scaffold Residue (Archive Candidates)

| File | Location | Evidence | Action |
|------|----------|----------|--------|
| [name] | [path] | [why it's scaffold] | ARCHIVE → 05-MEMORY/ARCH-[name] |

## 4. Canonization Candidates

| File | Current Location | Proposed Destination | Rationale |
|------|------------------|---------------------|-----------|
| [name] | -INBOX/ | 01-CANON/CANON-[name] | [why ready] |

## 5. Hidden Intentions (Surfaced from Archive)

| File | Location | Intention Found | Status |
|------|----------|-----------------|--------|
| [name] | 05-MEMORY/ | [what was planned] | [still relevant? / superseded?] |

## 6. Nomenclature Violations

| File | Current Name | Issue | Suggested Fix |
|------|--------------|-------|---------------|
| [name] | [current] | [missing prefix/wrong prefix/inconsistent] | [corrected name] |

## 7. Duplication Clusters

### Duplicate Set: [description]
- **Keep**: [path] — [why this is the canonical version]
- **Archive/Delete**:
  - [path] — [similarity: exact | near-exact | semantic]
  - [path]

## 8. Token Economics (Oversized Documents)

| File | Size | Issue | Recommendation |
|------|------|-------|----------------|
| [name] | [KB] | Exceeds 50KB threshold | [split into N parts | compress | summarize] |

## 9. -INBOX Deep Dive

Current -INBOX contents requiring Principal decision:

| File | Size | Apparent Purpose | Recommended Action | Confidence |
|------|------|------------------|-------------------|------------|
| [name] | [KB] | [what it seems to be] | [canonize/operationalize/archive/delete/investigate] | [high/medium/low] |

## 10. Recommended Immediate Actions

1. **[Priority 1]**: [specific action with file paths]
2. **[Priority 2]**: [specific action]
3. **[Priority 3]**: [specific action]

## Appendix: File Inventory by Directory

[Tree listing with file counts and total sizes per directory]
```

## Critical Instructions

1. **Be exhaustive** — Your large context exists for this purpose. Don't summarize when you can enumerate.
2. **Be specific** — File paths, not descriptions. "the teleology document" → `01-CANON/CANON-constellation-teleology.md`
3. **Flag uncertainty** — If you can't determine a file's purpose, say so explicitly with "INVESTIGATE" recommendation
4. **Preserve intentions** — When you find planning documents or decision records, surface the *content* of the intention, not just the file's existence
5. **Think like a librarian** — The goal is a corpus where any document can be found, understood, and trusted

## What Success Looks Like

A future agent with 100K context should be able to:
- Read your report
- Execute a triage pass without needing to examine individual files
- Trust that nothing important was missed

---

*This prompt is part of the Syncrescendence constellation. Output should be saved to `-OUTGOING/YYYYMMDD-corpus-annealment-survey/SENSING_REPORT.md`*
