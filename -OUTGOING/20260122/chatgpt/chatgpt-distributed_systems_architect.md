# Distributed Systems Evidence Pack - Syncrescendence Corpus

Scope: /Users/home/Desktop/syncrescendence
Lens: distributed state machines with concurrent agents (Claude, ChatGPT, Gemini, Grok, Perplexity) writing to a shared repository.

## 1. STATE INVENTORY

### Mutable State (high-churn, authoritative during execution)
- 00-ORCHESTRATION/state/DYN-*.md (dashboard, backlog, tree, corpus index) for operational status and derived summaries. Example: DYN-DASHBOARD.md tracks sprint and queue status (00-ORCHESTRATION/state/DYN-DASHBOARD.md:1).
- 00-ORCHESTRATION/state/DYN-*.csv for ledgers (tasks, projects, burndown, sprints) used for coordination and progress (00-ORCHESTRATION/state/DYN-TASKS.csv:1).
- 04-SOURCES/DYN-SOURCES.csv for per-source lifecycle state and metadata (04-SOURCES/DYN-SOURCES.csv:1).
- 00-ORCHESTRATION/state/events.jsonl, system_state.json, capabilities.json for event log, system snapshot, and platform capabilities (00-ORCHESTRATION/state/events.jsonl:1).
- 00-ORCHESTRATION/blackboard/* (evidence, plans, executions, audits) for IMEP cycle artifacts (00-ORCHESTRATION/blackboard/plans/PLN-20260116-001.json:1).
- 03-QUEUE/* for pending high-signal artifacts (03-QUEUE/README.md:1).
- -INBOX/* and -OUTGOING/* for ingress/egress staging (DYN-CORPUS_INDEX tree captures these roles, 00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:44).

### Immutable / Append-Only State (should not be mutated once canonized)
- 01-CANON/*: defended canonical knowledge (00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:19).
- 05-ARCHIVE/*: historical preservation and prior deliverables (00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:36).
- 00-ORCHESTRATION/state/ARCH-*.md: archaeology records (00-ORCHESTRATION/state/README.md:10).

### Derived State (computed from other state)
- 00-ORCHESTRATION/state/DYN-DASHBOARD.md (generated view over ledgers and queues) (00-ORCHESTRATION/state/DYN-DASHBOARD.md:132).
- 00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md (structure snapshot) (00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:8).
- 00-ORCHESTRATION/state/DYN-TREE.md (filesystem count snapshot) (00-ORCHESTRATION/state/DYN-TREE.md:1).

### Replicated State (same semantics, multiple copies)
- Function definitions in both .md and .xml (e.g., integrate.md vs integrate.xml) (02-OPERATIONAL/functions/integrate.md:1, 02-OPERATIONAL/functions/integrate.xml:1).
- Coordination protocols in multiple locations (DYN-COORDINATION.yaml vs REF-MULTI_CLI_COORDINATION.md) (02-OPERATIONAL/DYN-COORDINATION.yaml:8, 00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:1).
- References to sources ledger in multiple docs (sources.csv vs DYN-SOURCES.csv) (04-SOURCES/README.md:51, 04-SOURCES/DYN-SOURCES.csv:1).

## 2. CONSISTENCY VIOLATIONS (evidence with citations)

1) Ledger naming split-brain (tasks/burndown)
- DYN-DASHBOARD instructs updates to tasks.csv and burndown.csv (00-ORCHESTRATION/state/DYN-DASHBOARD.md:132).
- Actual ledgers are DYN-TASKS.csv and DYN-BURNDOWN.csv (00-ORCHESTRATION/state/DYN-TASKS.csv:1, 00-ORCHESTRATION/state/DYN-BURNDOWN.csv:1).

2) Queue path mismatch (QUEUE/ vs 03-QUEUE/)
- Dashboard references QUEUE/pending and QUEUE/modal1/modal2 (00-ORCHESTRATION/state/DYN-DASHBOARD.md:83).
- Corpus index defines 03-QUEUE as the queue root (00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:30).

3) Coordination protocol divergence (agents and zones)
- DYN-COORDINATION defines ChatGPT as a platform and routing target (02-OPERATIONAL/DYN-COORDINATION.yaml:87).
- REF-MULTI_CLI_COORDINATION only lists Claude Code and Gemini (00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:17).

4) Execution log location mismatch
- REF-MULTI_CLI_COORDINATION declares 00-ORCHESTRATION/logs/ for execution logs (00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:40).
- Corpus index defines 00-ORCHESTRATION/execution_logs/ as the log location (00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:14).

5) Ledger protocol references non-existent path (tasks.csv)
- REF-MULTI_CLI_COORDINATION uses tasks.csv in its atomic update protocol (00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:77).
- Actual ledger file is DYN-TASKS.csv (00-ORCHESTRATION/state/DYN-TASKS.csv:1).

6) Sources ledger naming conflict
- 04-SOURCES README states sources.csv holds integrated status (04-SOURCES/README.md:51).
- Actual ledger file is DYN-SOURCES.csv (04-SOURCES/DYN-SOURCES.csv:1).

7) Internal contradiction: flat directory rule vs required subdirectories
- REF-AGENTS mandates all directories must be flat (02-OPERATIONAL/registries/REF-AGENTS.md:24).
- Same document defines .dispatch with nested subdirectories (02-OPERATIONAL/registries/REF-AGENTS.md:64).

8) Protected path mismatch in coordination file
- Protected list names 02-OPERATIONAL/coordination.yaml (02-OPERATIONAL/DYN-COORDINATION.yaml:199).
- Actual coordination file is 02-OPERATIONAL/DYN-COORDINATION.yaml (02-OPERATIONAL/DYN-COORDINATION.yaml:1).

9) Duplicate function definitions without single source of truth
- integrate.md and integrate.xml both define the same function in different formats (02-OPERATIONAL/functions/integrate.md:1, 02-OPERATIONAL/functions/integrate.xml:1).

10) Tree generator output mismatch
- Makefile tree target writes DYN-ACTUAL_TREE.md (Makefile:82).
- Operational tree snapshot is DYN-TREE.md (00-ORCHESTRATION/state/DYN-TREE.md:1).

## 3. RACE CONDITIONS (scenarios + probability)

- Lost update on ledgers (high): multiple agents append to DYN-TASKS.csv/DYN-PROJECTS.csv without enforced locking; protocol is advisory only (00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:65).
- Write skew on sources status (high): parallel agents update DYN-SOURCES.csv status based on stale reads, causing invalid transitions (00-ORCHESTRATION/state/REF-SOURCES_SCHEMA.md:204).
- Phantom reads on queue state (medium): DYN-DASHBOARD generated from queue snapshots; simultaneous queue edits change counts between read and write (00-ORCHESTRATION/state/DYN-DASHBOARD.md:132).
- Duplicate event emission (medium): events.jsonl is append-only but no global monotonic ID; concurrent agents may emit out-of-order or duplicate events (00-ORCHESTRATION/state/events.jsonl:1).
- Function definition drift (medium): .md and .xml versions diverge when edited by different agents (02-OPERATIONAL/functions/integrate.md:1, 02-OPERATIONAL/functions/integrate.xml:1).
- Tree/index regeneration race (low): DYN-CORPUS_INDEX and DYN-TREE can be generated concurrently, producing mismatched snapshots (00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md:3).

## 4. PARTITION SCENARIOS (what breaks, how to recover)

- Oracle web surface partitioned from repo: Oracle has read-only access via MCP/exports, so authoritative state changes can lag (02-OPERATIONAL/DYN-COORDINATION.yaml:49). Recovery: require handoff token + event replay to converge state (Makefile:125).
- CLI agents isolated from each other: protocol states instances do NOT communicate directly (00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:116). Recovery: treat git commits as consensus boundary; reconcile via audits and rebase.
- Gemini ingestion path offline: sources intake stalls; DYN-SOURCES.csv status drift vs actual raw/processed files. Recovery: periodic reconciliation pass comparing raw/processed to DYN-SOURCES.csv.
- ChatGPT codex_cli partitioned: routing decisions in DYN-COORDINATION may route to a platform with no repo visibility. Recovery: route fallback to Claude Code with filesystem sovereignty.

## 5. CAP ANALYSIS (per subsystem)

- 01-CANON (CP): favors consistency and partition tolerance; availability reduced by protected zones and review gates (02-OPERATIONAL/DYN-COORDINATION.yaml:194).
- 00-ORCHESTRATION/state ledgers (AP leaning, weak consistency): append-only guidance, high availability; conflict resolution is manual (00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md:65).
- 04-SOURCES pipeline (AP): ingestion and processing favor availability; status consistency is eventually reconciled (04-SOURCES/README.md:24).
- 03-QUEUE (AP): availability for intake is prioritized; consistency of queue counts is eventual (03-QUEUE/README.md:16).
- -OUTGOING deliverables (CP for releases, AP for drafts): once exported they are immutable (release-like); in-progress drafts are available but not consistent across agents.
- 00-ORCHESTRATION/blackboard (CP during IMEP cycle): plan/evidence/execution/audit are intended to be atomic for a cycle; availability is lower while verifying (00-ORCHESTRATION/blackboard/plans/PLN-20260116-001.json:6).

## 6. EVENT SCHEMA (proposed event sourcing model)

### Observed event fields
- events.jsonl uses timestamp, event, actor, type, status, details (00-ORCHESTRATION/state/events.jsonl:1).
- Blackboard artifacts include id, timestamp, actor, plan_id, files_changed (00-ORCHESTRATION/blackboard/executions/EXE-20260116-001.json:2).

### Proposed schema (normalized)
```json
{
  "event_id": "EVT-YYYYMMDD-###",
  "timestamp": "2026-01-16T00:36:45Z",
  "actor": "claude_code_2",
  "event_type": "execution.complete",
  "entity": {
    "kind": "directive|plan|execution|audit|ledger|source|canon",
    "id": "DIRECTIVE-046A"
  },
  "correlation_id": "PLN-20260116-001",
  "causation_id": "EVT-...",
  "status": "success|partial|failed",
  "metadata": {
    "files_changed": ["..."],
    "ledger": "DYN-TASKS.csv",
    "delta": {"autonomous_cycles": "+1"}
  }
}
```

### Required event types
- directive.issued, plan.created, execution.started, execution.completed, audit.completed
- ledger.appended, source.status_changed, canon.integrated
- handoff.token_created, partition.detected, reconciliation.completed

## 7. STATE MACHINE SPECIFICATION (core pipeline)

Sources lifecycle (authoritative in DYN-SOURCES.csv):

```
raw -> triaged -> processed -> integrated
                     \-> archived
triaged -> archived
```

Reference: status enumeration and transitions (00-ORCHESTRATION/state/REF-SOURCES_SCHEMA.md:202).

Directive execution lifecycle (derived from templates and logs):

```
issued -> planned -> executing -> complete | partial | blocked
```

Reference: execution log template states COMPLETE/PARTIAL/BLOCKED (02-OPERATIONAL/templates/EXECUTION_LOG_TEMPLATE.md:6).

## 8. REFACTORING FOR CONSISTENCY (targeted fixes)

1) Single source of truth for ledger naming
- Standardize on DYN-* ledgers across docs, scripts, and templates; update DYN-DASHBOARD and REF-MULTI_CLI references.

2) Consolidate coordination protocols
- Merge DYN-COORDINATION.yaml and REF-MULTI_CLI_COORDINATION.md into a single registry that emits machine-readable + human-readable views.

3) Enforce replicated function policy
- Choose one canonical format (xml or md) and generate the other; add a checksum to detect drift.

4) Make derived snapshots explicit
- Add metadata frontmatter for DYN-DASHBOARD, DYN-CORPUS_INDEX, DYN-TREE with source inputs and generation timestamp; store generator command.

5) Event-sourced reconciliation
- Require every state mutation to emit a normalized event; rebuild DYN-DASHBOARD and DYN-CORPUS_INDEX from events + filesystem scan.

6) Partition recovery playbook
- Define a required handoff token and a reconciliation checklist for web/CLI partitions (Makefile:125).

7) Conflict-resistant ledger updates
- Add monotonic event_id and optimistic concurrency checks to CSV append scripts; fail if last row timestamp changed.

