# RENDEZVOUS SUMMIT — SITUATION REPORT
## Pedigree Management: Complete Instrument Assessment

**Date**: 2026-02-25 | **Session**: CC34 | **Classification**: INCIDENTAL FORMAL ASSESSMENT
**Compiled by**: Commander (Claude Opus 4.6) at Sovereign request
**Corpus analyzed**: 34+ files — 1 hook script, 1 skill definition, 1 log file (6,019 lines, 158 entries), 1 canon authority document (CANON-25100 Part IX), 1 settings.json hook config, 5 referencing skills, 7 referencing infrastructure docs, 15+ handoff/receipt/task artifacts

---

## I. WHAT THE AJNA PEDIGREE IS

The Ajna Pedigree is a dual-layer decision lineage capture system:

1. **Automated Hook Layer** (`ajna_pedigree.sh`) — fires on every Stop event, captures git metadata, writes to `DYN-PEDIGREE_LOG.md`
2. **Manual Skill Layer** (`/pedigree` SKILL.md v2.0.0) — repository-centric session context management, alternative to document-based handoffs

### Origin and Authority

The instrument has two origin documents:

**CANON-25100 Part IX — Oracle Pedigree Protocol**: The constitutional authority. Defines pedigree as "historical lineage tracking, decision archaeology, and multi-model integration." Written during the pre-constellation Oracle era (Oracle 0-12), it established pedigree as the repository-centric supersession of web-app handoffs.

**SKILL.md v2.0.0**: The operational procedure. Authority: Oracle 13. Defines pedigree components (session lineage, campaign status, project state, key decisions, active intentions) and the process for session initialization.

### The Name

"Ajna Pedigree" is a naming artifact from the constellation's formation. Originally "Oracle Pedigree" (CANON-25100 Part IX still uses this name), it was renamed when the Oracle role was redistributed across the constellation. Ajna (CSO, Kimi K2.5) inherited the pedigree instrument as the strategic meta-analysis agent. The hook script carries the `ajna_` prefix; the canon document says "Oracle"; the CC lineage documentation says both. The naming is inconsistent.

---

## II. THE HOOK — `ajna_pedigree.sh`

### What It Does

```
Source: orchestration/00-ORCHESTRATION/scripts/ajna_pedigree.sh (75 lines)
Trigger: Stop event (via .claude/settings.json hooks)
Output: orchestration/state/DYN-PEDIGREE_LOG.md (append)
```

The script:
1. Gets the repo root, branch, HEAD fingerprint, timestamp
2. Runs `git log --oneline -10 --since="6 hours ago"` for recent commits
3. Counts commits and diffs files modified between HEAD~N and HEAD
4. Categorizes modified files into State, CANON, and ENGINE buckets
5. Counts queued intentions from `DYN-INTENTIONS_QUEUE.md`
6. Appends a structured entry to `DYN-PEDIGREE_LOG.md`

### What It Actually Captures

Each entry contains:
- Timestamp, branch, HEAD fingerprint, commit count
- Last 10 commit messages (capped by `-10` flag)
- State/CANON/ENGINE files touched (or "none")
- Queued intentions count

### What It Does NOT Capture

The hook captures **git metadata** but not **decision lineage**. Despite the script header saying "Captures decision lineage, artifacts, and session pedigree," what it actually records is:
- Which files changed (structural)
- What commits exist (mechanical)
- How many intentions are queued (count only)

Missing from the automated capture:
- **Why** decisions were made (the stated purpose of pedigree)
- **Which agent** made them
- **Which directive** spawned the work
- **Sovereign questions** asked during the session
- **DAG convergence** status
- **Cross-platform** coordination history
- **Verification evidence**

The gap between the hook's stated purpose ("decision lineage and session provenance") and its actual output (git metadata summary) is the central finding of this assessment.

---

## III. THE LOG — `DYN-PEDIGREE_LOG.md`

### Vital Statistics

| Metric | Value |
|--------|-------|
| Total size | 303.2 KB, 6,019 lines |
| Total entries | 158 sessions |
| Date range | 2026-02-23 01:36:43 → 2026-02-25 20:50:05 |
| Span | 2 days, 19 hours (3 calendar days) |
| Average entries/day | 52.7 |
| Unique git fingerprints | 61 |

The hook has been active for exactly 3 days. It was installed during the CC22/CC23 infrastructure buildout (2026-02-23).

### Session Frequency

| Date | Sessions | Notes |
|------|----------|-------|
| 2026-02-23 | 59 | Installation day. CC24-CC25 era. |
| 2026-02-24 | 72 | CC26-CC28 era. Peak activity. |
| 2026-02-25 | 27 | CC29-CC33 era. |

### The Commit Count Problem

| Commits Shown | Sessions | % |
|---------------|----------|---|
| 10 (capped) | 117 | 74.1% |
| 0-9 (actual) | 41 | 25.9% |

**74% of all entries show "10 commits"** — this is the display cap from `git log --oneline -10`, not a meaningful session metric. The hook records the 10 most recent commits in the repo at the time of firing, not the commits produced during that session. This makes the commit count field **useless as a per-session metric**.

### The Duplicate Problem

**97 out of 157 consecutive session pairs share the same fingerprint.** The hook fires multiple times against the same HEAD without intervening commits. Notable patterns:

| Pattern | Count | Example |
|---------|-------|---------|
| Runs of 2 same-fingerprint | 31 occurrences | Throughout |
| Runs of 5+ same-fingerprint | 8 occurrences | Multiple |
| Run of 14 same-fingerprint | 1 | 2026-02-23, fingerprint `b0268441`, 14 fires over ~2 hours |
| Run of 12 same-fingerprint | 1 | 2026-02-24, fingerprint `d80f7df4`, 12 fires in 33 minutes |
| 6 fires in 18 seconds | 1 | 2026-02-23 15:40:46-15:41:04, fingerprint `01db01fd` |

The 6-fires-in-18-seconds burst suggests the Stop hook triggers on every sub-agent termination, not just primary session end. This produces redundant identical entries that inflate the log without adding information.

**61 unique fingerprints across 158 entries** means each unique state of the repo is logged an average of 2.6 times. The log is ~60% redundant by this measure.

### File Touch Patterns

| Category | Sessions with "none" | Sessions with files | % touching |
|----------|---------------------|---------------------|-----------|
| State files | 64 (40.5%) | 94 (59.5%) | 59.5% |
| CANON files | 115 (72.8%) | 43 (27.2%) | 27.2% |
| ENGINE files | 60 (38.0%) | 98 (62.0%) | 62.0% |

**Only 2 unique canon files have ever been touched** across all 158 entries:
1. `canon/01-CANON/CANON-ONTOLOGY-GATE_v1.md`
2. `canon/01-CANON/sn/CANON-PROTEASE_AXIOMS.sn.md`

Both were created during CC32-CC33. This confirms the canon protection is holding and the first content transformation is visible in the pedigree trail.

### The CLAUDE.md Anomaly

`CLAUDE.md` appears in 50 sessions' "State Files Touched" section. This is a generated config file (`make configs` output), not an orchestration state file. The hook's file categorization regex (`grep -E "state/|CLAUDE\.md|COCKPIT\.md"`) treats CLAUDE.md as state, which is architecturally incorrect.

### Intentions Growth

| Range | Sessions | Interpretation |
|-------|----------|---------------|
| 0 intentions | 2 (1.3%) | Early installation |
| 4-10 | 17 | Early Feb-23 |
| 11-20 | 37 | Mid Feb-23 |
| 21-30 | 23 | Feb-24 |
| 31-47 | 81 | Feb-24-25 |

The intentions count monotonically increased from 4 to 47 over 3 days. This reflects the intentions queue accumulating without being drained — the hook captures growth but cannot trigger action.

---

## IV. THE SKILL — PEDIGREE v2.0.0

### Pedigree vs. Handoff (as defined by the skill)

| Aspect | Handoff | Pedigree |
|--------|---------|----------|
| Context | Document-centric | Repository-centric |
| Assumption | Next instance lacks context | Repository IS the context |
| Format | Detailed narrative | Structured reference |
| Use Case | Web app transitions | Claude Code continuity |

**Rule from skill**: "Use Pedigree when the repository is authoritative. Use Handoff only for web-app-only sessions."

### What the Skill Prescribes

Session initialization:
1. Read `ORACLE_ARC.md` for trajectory
2. Read latest `EXECUTION_LOG-*` for recent activity
3. Read `DYN-BACKLOG.md` for project status
4. Read `ARCH-INTENTION_COMPASS.md` for active intentions
5. Synthesize into working context

### What Actually Happened

The pedigree skill has been **completely superseded by the CC handoff protocol**. Since CC26 (Feb 24), every session uses:
1. Read `HANDOFF-CC{N}.md` (the document-centric approach pedigree explicitly rejects)
2. Run `git status` + `git log`
3. Scan inbox
4. Check DAG convergence

The skill's prescribed initialization (ORACLE_ARC.md, EXECUTION_LOG-*, DYN-BACKLOG.md) references files from the pre-constellation Oracle era. Several of these may no longer exist at the documented paths:
- `ORACLE_ARC.md` — not verified in current repo structure
- `EXECUTION_LOG-*` — the format changed; now `DYN-EXECUTION_STAGING.md`
- `DYN-BACKLOG.md` — not verified; may have been renamed/reorganized

### The Blitzkrieg Integration

The skill defines a Blitzkrieg pedigree format (`ORACLE [N] PEDIGREE: BLITZKRIEG [M]`). This references the Blitzkrieg campaign system from the Oracle era (campaigns 1-45+). The CC era does not use Blitzkriegs — it uses CC sessions with ascertescence triangulation. This integration is vestigial.

---

## V. THE CANON AUTHORITY — CANON-25100 PART IX

### What Part IX Defines

CANON-25100 Part IX ("Oracle Pedigree Protocol") is the constitutional authority for the pedigree system. It defines:

- **Purpose**: Historical lineage (Oracle 0 → current), decision archaeology (what decided and why), multi-model integration (tracks across platforms)
- **Components**: thread_id, campaign, phase, date, decisions (with verbatim principal words + interpretation + lenses applied + score + outcome), artifacts produced, handoff state
- **Locations**: Four distributed files (ARCH-ORACLE_ARC_SUMMARY.md, ARCH-ORACLE_DECISIONS.md, ARCH-INTENTION_COMPASS.md, EXECUTION_LOG-*.md)
- **Cross-platform tracking**: Platform-specific implications for each decision

### The Gap Between Canon and Implementation

| Canon Prescribes | Implementation Delivers |
|-------------------|------------------------|
| Verbatim Sovereign words captured per decision | Not captured by hook |
| Oracle's interpretation of each decision | Not captured by hook |
| 18-lens evaluation scores | Not captured by hook |
| Decision IDs (DEC-XXX-NNN format) | Not captured by hook |
| Artifacts produced per decision | Partially — file diffs captured but not decision-linked |
| Cross-platform pedigree (Claude/Gemini/ChatGPT) | Not captured by hook |
| Pedigree maintenance protocol (during/after/across sessions) | Not implemented |
| Four distributed location files | Only DYN-PEDIGREE_LOG.md exists; ARCH-ORACLE_ARC_SUMMARY.md, ARCH-ORACLE_DECISIONS.md status unknown |

The canon specification describes a rich decision archaeology system. The implemented hook captures git metadata. The gap is approximately **80%** — the hook delivers ~20% of what the canon authority prescribes.

---

## VI. THE INTEGRATION WEB

### What References Pedigree

| System | How It References Pedigree |
|--------|---------------------------|
| **commit-work skill** | "Commits feed the pedigree skill, which records provenance metadata (which agent, which directive, which session)" |
| **memory-systems skill** | "Memory updates feed the pedigree hook chain, creating an audit trail" |
| **verification-before-completion skill** | "The pedigree hook chain checks for verification evidence in commit metadata" |
| **REF-NEO_BLITZKRIEG_BUILDOUT** | Lists pedigree as second layer in automation stack |
| **REF-SKILLS_PIPELINE_MAP** | Positions pedigree hook as terminal-stage COMMIT automation |
| **README.md** | Lists in active hooks inventory + skills inventory |
| **CLAUDE.md** | Hooks table (Stop event) |
| **CC lineage (cc-lineage.md)** | "This is equivalent to the ajna pedigree (Ajna) and oracle transitions" |
| **Handoff CC29-CC31** | References pedigree as part of the "compile everything" synthesis |

### The Three-Lineage System

The constellation has three parallel lineage tracking systems:

| Lineage | Agent | Instrument | Status |
|---------|-------|-----------|--------|
| **Oracle Pedigree** | Pre-constellation Oracle | Decision archaeology | SUPERSEDED by CC lineage |
| **Ajna Pedigree** | Ajna (CSO) | Strategic meta-analysis + hook | PARTIALLY ACTIVE (hook runs; Ajna dormant) |
| **CC Lineage** | Commander (COO) | Ascertescence + handoffs | ACTIVE — primary system since CC26 |

The CC lineage has become the *de facto* pedigree system. It captures what the Oracle Pedigree Protocol prescribed (decisions with rationale, Sovereign intent, verification evidence, cross-session continuity) but through handoff documents rather than the pedigree mechanism.

---

## VII. EVALUATION

### What Works

1. **The hook fires reliably**. 158 entries across 3 days with no gaps. The Stop event trigger in `.claude/settings.json` is correctly configured.

2. **CANON file tracking is valuable**. The fact that only 2 unique canon files appear across 158 entries is meaningful — it proves canon protection is holding and pinpoints exactly when content transformation began.

3. **The concept is sound**. Decision archaeology and session lineage are genuinely needed. The canon authority (CANON-25100 Part IX) describes a comprehensive system that would be valuable if implemented.

### What Doesn't Work

1. **The hook doesn't capture what it claims to**. The header says "decision lineage and session provenance." It captures git metadata. The gap between claim and reality is the same verification theater pattern identified in the clarescence assessment.

2. **60% redundancy**. 97 of 157 consecutive pairs are identical-fingerprint duplicates. The hook fires on every sub-agent Stop, not just session end, producing ~2.6 entries per unique repo state.

3. **Commit count is meaningless**. `git log -10` caps at 10 commits regardless of session activity. 74% of entries show "10" which tells you nothing about that session.

4. **The `--since="6 hours ago"` window is wrong**. If a session spans >6 hours, earlier commits are excluded. If two sessions occur within 6 hours, later sessions include earlier sessions' commits. The window doesn't align with session boundaries.

5. **CLAUDE.md misclassification**. A generated config file appears in 50 entries as a "State file," polluting the state tracking signal.

6. **The skill is vestigial**. It references Oracle-era files (ORACLE_ARC.md, DYN-BACKLOG.md), Blitzkrieg campaigns, and an initialization process that no session has followed since CC26. The CC handoff protocol has completely replaced it.

7. **No deduplication or compaction**. 303KB after 3 days. At this rate, ~37MB/year. The log grows monotonically with no archival, compaction, or deduplication mechanism.

8. **Naming confusion**. "Ajna Pedigree" in the hook, "Oracle Pedigree" in the canon, "pedigree" in the skill, "CC lineage" in practice. Four names for overlapping concepts, no reconciliation.

### The Quantitative Assessment

| Dimension | Rating | Evidence |
|-----------|--------|----------|
| **Reliability** | 8/10 | Hook fires consistently, no gaps, 158/158 entries logged |
| **Signal quality** | 3/10 | 60% duplicate entries, 74% meaningless commit counts, CLAUDE.md misclassification |
| **Canon compliance** | 2/10 | Implements ~20% of CANON-25100 Part IX specification |
| **Skill currency** | 2/10 | References Oracle-era files, Blitzkrieg campaigns; superseded by CC handoff |
| **Decision capture** | 1/10 | Captures zero decisions, zero rationale, zero Sovereign words, zero verification evidence |
| **Storage efficiency** | 2/10 | 303KB in 3 days, no compaction, ~60% redundant |
| **Integration** | 5/10 | Referenced by 5 skills and 3 infrastructure docs, but the references describe capabilities the hook doesn't actually have |
| **Naming coherence** | 2/10 | 4 different names for overlapping concepts across 7+ documents |

---

## VIII. SYNTHESIS — THE PEDIGREE'S PLACE IN THE CONSTELLATION

### The Historical Arc

The pedigree system evolved through three eras:

**Era 1 — Oracle (pre Feb-23)**: The Oracle Pedigree Protocol was designed as part of the CANON-25100 context management architecture. It prescribed rich decision archaeology with verbatim Sovereign words, 18-lens evaluation, cross-platform tracking. This was the aspirational specification.

**Era 2 — Hook Activation (Feb 23)**: The `ajna_pedigree.sh` hook was implemented as a minimal automated version. It captures git metadata — a small fraction of what the protocol prescribes. The skill (v2.0.0) was written to bridge the gap but references Oracle-era infrastructure that may no longer exist.

**Era 3 — CC Lineage (Feb 24+)**: The Commander Council handoff protocol emerged organically and took over the pedigree function. CC handoffs capture what the Oracle Pedigree Protocol prescribed — decisions with rationale, Sovereign intent, what was accomplished, what remains, verification evidence. But they do it through narrative documents, not structured metadata.

### The Fundamental Question

The pedigree system is split between three things that don't talk to each other:

1. **A canon specification** (CANON-25100 Part IX) that describes a rich decision archaeology system
2. **A bash hook** that captures git metadata on Stop events
3. **A skill definition** that references Oracle-era infrastructure
4. **A CC handoff protocol** that actually does what pedigree was supposed to do, but under a different name

The question for the Summit: **should these be unified, or should pedigree be formally deprecated in favor of the CC handoff protocol that replaced it?**

### Options

**Option A — Deprecate pedigree, formalize CC lineage as the successor**:
- Remove or disable the `ajna_pedigree.sh` hook (saves ~100KB/day of low-signal log)
- Update CANON-25100 Part IX to reference CC lineage as the successor protocol
- Retire the `/pedigree` skill
- The CC handoff already does what pedigree was supposed to do

**Option B — Fix the hook to actually capture decision lineage**:
- Rewrite `ajna_pedigree.sh` to extract decisions from handoffs, not just git metadata
- Add deduplication (skip if fingerprint matches last entry)
- Fix commit counting (track session-specific commits, not repo-wide)
- Fix CLAUDE.md misclassification
- Add compaction mechanism
- This would make the hook useful but would duplicate work already done by CC handoffs

**Option C — Reactivate pedigree as Ajna's instrument when Ajna awakens**:
- Keep the hook dormant but maintained
- When Ajna (CSO) reactivates on the MBA, pedigree becomes Ajna's decision archaeology instrument — complementary to Commander's CC handoffs
- This defers the decision but preserves optionality

**Option D — Merge pedigree into CC handoff protocol**:
- Add structured metadata (the yaml-style components from CANON-25100) to CC handoff format
- Retire the separate hook and skill
- CC handoffs become the single lineage capture mechanism with both narrative and structured components

---

*Compiled from: `ajna_pedigree.sh` (75 lines), `SKILL.md` v2.0.0 (220 lines), `DYN-PEDIGREE_LOG.md` (6,019 lines, 158 entries), `CANON-25100-CONTEXT_TRANS-lattice.md` Part IX (110 lines), `.claude/settings.json` hook config, 5 referencing skills (memory-systems, commit-work, verification-before-completion, blitzkrieg_issue, blitzkrieg_finalize), 7 referencing infrastructure docs (REF-NEO_BLITZKRIEG_BUILDOUT, REF-SKILLS_PIPELINE_MAP, README.md, CLAUDE.md, CLAUDE-EXT.md, cc-lineage.md), 15+ handoff/receipt/task artifacts.*
