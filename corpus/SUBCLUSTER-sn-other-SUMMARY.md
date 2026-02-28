# Classification Summary: sn-other → Refined Topics

## Overview
Processed 375 files previously tagged as "sn-other" (operational junk drawer) and reclassified them into more specific topics.

**Output File**: `SUBCLUSTER-sn-other.tsv`
**Format**: `filename[TAB]refined_topic[TAB]one_line_summary`

## Classification Distribution

| Topic | Count | Percentage |
|-------|-------|-----------|
| sn-operational-cruft | 246 | 65.6% |
| sn-session-log | 90 | 24.0% |
| sn-blitzkrieg | 30 | 8.0% |
| sn-sovereign | 3 | 0.8% |
| sn-dispatch | 2 | 0.5% |
| sn-audit | 2 | 0.5% |
| sn-memory | 1 | 0.3% |
| sn-inbox | 1 | 0.3% |

## Topic Definitions

### sn-session-log (90 files)
Execution logs, task completion records, results from agent operations.
- **Examples**: Task results, RESULT/STATUS headers, execution reports
- **Pattern**: Contains `**result**:`, `**status**:`, `**task**:`, or `completed at`
- **Key files**: RESULT-* files, execution logs, completion records

### sn-blitzkrieg (30 files)
Parallel execution plans, multi-lane coordination, swarm strategies, and architectural registries.
- **Examples**: Skill registries, phase plans, parallel execution strategies
- **Pattern**: Contains `blitzkrieg`, `parallel`, `swarm`, `lane` + execution/phase context
- **Key files**: Architecture documents, coordination plans, registry files

### sn-operational-cruft (246 files)
Research articles, reference materials, tutorials, guides, social media content, empty/stub files, and database artifacts.
- **Sub-categories**:
  - Research articles about Clawdbot/Moltbot
  - Tutorial and setup guides
  - Social media threads and discussions
  - Empty files, stubs, database artifacts (.db-shm, .db-wal, .breaker files)
- **Why here**: Not core operational files, but archived reference material or system artifacts

### sn-sovereign (3 files)
Sovereign directives, mandates, and decision queue items.
- **Pattern**: Explicit `# sovereign` headers, sovereign directive language
- **Key files**: Directive documents, decision records

### sn-dispatch (2 files)
Handoff packages and inter-agent coordination messages.
- **Pattern**: **From**:, **To**:, Kind: headers
- **Key files**: Handoff documents, relay messages

### sn-audit (2 files)
Quality reviews, audit assessments, and defect reports.
- **Pattern**: Assessment + audit keywords, or finding/defect language
- **Key files**: Review reports, assessment documents

### sn-memory (1 file)
Agent memory files, context records.
- **Pattern**: Explicit memory headers or persistent context markers
- **Key files**: Memory snapshots, knowledge base files

### sn-inbox (1 file)
Inbox or inbound task items.
- **Pattern**: `# inbox` or inbox item markers
- **Key files**: Inbox collection files

## Methodology

1. **Extraction**: Extracted all 375 filenames from CLUSTER-MAP-FULL.tsv
2. **Classification**: Read first 5,000 characters of each file
3. **Pattern Matching**: Applied topic-specific heuristics based on:
   - Header patterns (# headers)
   - Metadata fields (**field**:)
   - Content keywords
   - File structure
4. **Fallback**: Files not matching operational patterns → sn-operational-cruft (research/reference material)

## Key Findings

- **65.6% are operational-cruft**: Primarily archived research articles, reference materials, and database artifacts
- **24.0% are session logs**: Significant volume of execution/completion records
- **8.0% are blitzkrieg**: Coordination and architectural documents
- **<2% are other types**: Relatively few sovereign directives, dispatch messages, or audits in this subset

## Quality Notes

- Database artifacts (.db-shm, .db-wal) classified as operational-cruft
- Empty files classified as operational-cruft
- Research articles about Clawdbot/Moltbot clearly identified in summaries
- All 375 files successfully classified
