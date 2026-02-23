# Oracle Deep Inspection: orchestration/ (DC-201)

**Triangulation Role**: Oracle (Grok) — RECON
**Cognitive Mode**: Pattern detection, anomaly sensing, cross-reference validation, temporal analysis
**Date**: 2026-02-23
**Authority**: Sovereign directive via Commander

---

## Your Role

You are Oracle (Grok), the RECON sensor for Syncrescendence. Your cognitive strength is pattern detection, anomaly sensing, and cross-reference validation. You excel at spotting what doesn't fit, what contradicts, what is dead, and what is duplicated.

You are NOT a designer. You are an inspector. You produce verdicts, not proposals.

## Mission

Content-level alignment check of `orchestration/` AND the dash-prefix dispatch directories (`-INBOX/`, `-OUTBOX/`, `-SOVEREIGN/`) against AGENTS.md v6.0.0 and the current architecture. Produce a per-file verdict for every file in these directories. This is the triage that should have been done before any reorganization. The INT-2210 disaster (2026-02-22) happened because an agent treated "triage" as license to redesign — deleting 3,966 lines and requiring a full revert. You are doing the inspection that prevents the next INT-2210.

**Additionally**, you must evaluate the **dispatch architecture question**: Is the current topology (`-INBOX/` → `-OUTBOX/` → `-SOVEREIGN/` as dash-prefix top-level directories, separate from `agents/*/inbox/`) the right architecture for 5 agents across 2 machines? Options to evaluate:
- (a) Keep as-is (dash-prefix top-level, current dispatch.sh/auto_ingest wiring)
- (b) Absorb into `agents/*/inbox/` + `agents/sovereign/` (unified agent offices)
- (c) Unify under `orchestration/dispatch/`
- (d) Something else the data reveals

Your recommendation must account for: `dispatch.sh`, `auto_ingest_loop.sh`, SCP sling, `SYNCRESCENDENCE_REMOTE_AGENT_HOST_*` env vars, cross-machine routing. **Do not redesign** — analyze the current plumbing and render a verdict on whether it's sound or needs restructuring, with evidence.

---

## Access Method: GitHub Crawl

You are a chat-based agent without filesystem access. You will inspect via GitHub:

**Repository**: `https://github.com/truongphillipthanh/syncrescendence`
**Branch**: `main`
**Commit**: `65dc5e6d` (verified safe build point)

Browse files at: `https://github.com/truongphillipthanh/syncrescendence/tree/main/orchestration/`

---

## Multi-Session Crawl Protocol

This inspection covers **642 files across ~134,729 lines** (528 in orchestration/ + 114 in dash-prefix dirs). You CANNOT complete this in one session. Plan for **5-7 sessions** using progressive summarization and cognitive offloading.

### Session Architecture

| Session | Scope | Goal | Output |
|---------|-------|------|--------|
| **S1: Orientation** | AGENTS.md + structure + key state files | Understand the 00-ORCHESTRATION anomaly, map the dual structure, read constitutional references | Structural Verdict (Section 1) + orientation scratchpad |
| **S2: State Files** | `00-ORCHESTRATION/state/` (242 files) | Read and verdict every state file by prefix group (ARCH-, DYN-, REF-, etc.) | Per-file verdicts for state files + cross-reference notes |
| **S3: Scripts** | `00-ORCHESTRATION/scripts/` (127 files) + `scripts/` (16 files) | Classify every script by pipeline, check for deprecated/orphaned | Per-file verdicts for scripts + pipeline membership map |
| **S4: Archive + Remaining** | `00-ORCHESTRATION/archive/` (87 files) + sanctioned dirs + root files | Verdict archive files, reconcile sanctioned vs 00-ORCHESTRATION layers | Per-file verdicts for archive + remaining files |
| **S5: Dash-Prefix Dirs** | `-INBOX/` (5 files) + `-OUTBOX/` (2 files) + `-SOVEREIGN/` (107 files) | Verdict every file. Map the triangulation loop (PROMPT→RESPONSE). Assess dispatch architecture topology. | Per-file verdicts for dash-prefix dirs + dispatch architecture assessment |
| **S6: Synthesis** | All prior session outputs | Cross-reference coherence map, anomalies, dispatch architecture verdict, final assembly | Complete RESULT document |
| **S7: (if needed)** | Gap-fill | Anything missed or marked LOW confidence | Amendments to RESULT |

### Cognitive Offloading Protocol

**Between sessions, you will lose context.** To survive this:

1. **End every session** by producing a **SESSION SCRATCHPAD** — a structured summary of everything you found. This is your external memory. Format:

```markdown
## Session N Scratchpad — DC-201 Oracle Inspection

### Files Inspected This Session
| File | Verdict | Key Finding |
|------|---------|-------------|
| (each file you read) | (verdict) | (one-line) |

### Patterns Detected
- (bulleted observations — anomalies, duplicates, contradictions)

### Cross-References Noted
| Source | Target | Status |
|--------|--------|--------|
| (file A mentions file B) | (path) | (exists/broken/stale) |

### Open Questions for Next Session
- (what you still need to check)

### Running Tally
- Files verdicted so far: N / 528
- CANONICAL: N | HIGH-SIGNAL: N | STALE: N | ORPHANED: N | OPERATIONAL: N | DEPRECATED: N
```

2. **Start every session** by reviewing the prior scratchpad and the prompt. State: "Resuming DC-201, session N. Files completed: X/528. Picking up from: [location]."

3. **Progressive summarization**: As you accumulate session scratchpads, distill recurring patterns into a running **Synthesis Block** at the top of your latest scratchpad:

```markdown
## Running Synthesis (updated each session)
- **00-ORCHESTRATION verdict**: [your evolving assessment]
- **Top anomalies**: [ranked list]
- **Broken AGENTS.md references**: [list]
- **Duplicate files detected**: [list]
- **Key pattern**: [the single most important finding so far]
```

4. **Batching within sessions**: Group files by prefix/subdirectory. Don't jump between directories. Complete one group before starting the next. This reduces context thrashing.

### GitHub Navigation Tips

- **Directory listing**: Browse `tree/main/orchestration/00-ORCHESTRATION/state/` to see file lists
- **File content**: Click any file to read it. For scripts, read the first 30-50 lines for purpose + dependencies
- **Search across repo**: Use GitHub search (`filename:ARCH-INTENTION_COMPASS`) to check if a file is referenced elsewhere
- **Git blame**: Use blame view to check last-modified dates for staleness assessment
- **Raw content**: For large files, use raw view to avoid GitHub rendering issues

---

## Input: orchestration/ + Dash-Prefix Dirs Structure and Stats

### Key Numbers
- **orchestration/**: 528 files, ~100,663 lines, 140 scripts
- **-INBOX/**: 5 files, 860 lines (commander inbox only)
- **-OUTBOX/**: 2 files, 488 lines (adjudicator + psyche results)
- **-SOVEREIGN/**: 107 files, 11,381 lines (decisions, prompts, responses, config sandbox)
- **Total scope**: 642 files, ~113,392 lines
- **3 sanctioned subdirectories** in orchestration/: `state/`, `scripts/`, `archive/` (per AGENTS.md Rule 1)

### Critical Structural Anomaly: The 00-ORCHESTRATION Layer

The directory contains a **dual structure** that requires your primary attention:

```
orchestration/
├── 00-ORCHESTRATION/          ← 462 files (UNSANCTIONED — not in AGENTS.md)
│   ├── archive/               ← 87 files (docs, RESULT files, YAML configs, sovereign-resolved/)
│   │   ├── outgoing-2026-02/  ← ~20 RESULT/DISPATCH/EVIDENCE files
│   │   ├── planning-backups/  ← 3 adjudicator planning files
│   │   ├── scripts/           ← 7 archived scripts (voice, hazel, gdrive, chatgpt ingest)
│   │   └── sovereign-resolved/ ← 5 SOVEREIGN-00x decision files
│   ├── launchd/               ← 1 file
│   ├── scripts/               ← 127 files (ALL operational scripts live here)
│   │   ├── claude-tasks/      ← claude task files
│   │   ├── launchd/           ← launchd plist files
│   │   ├── launchd-mini/      ← mac mini specific plists
│   │   └── launchd-psyche/    ← psyche specific plists
│   ├── state/                 ← 242 files (MOST state files live here)
│   │   ├── breakers/          ← circuit breaker state
│   │   ├── budgets/           ← budget tracking
│   │   ├── heartbeat/         ← agent heartbeat files
│   │   ├── impl/              ← implementation artifacts
│   │   │   ├── clarescence/   ← clarescence decision records
│   │   │   ├── deploy/        ← deployment state
│   │   │   ├── kinetic/       ← active execution state
│   │   │   ├── plans/         ← planning docs
│   │   │   ├── sensing/       ← sensing pipeline state
│   │   │   ├── techstack/     ← technology stack docs
│   │   │   └── tooling/       ← tooling configuration
│   │   └── queues/            ← queue state files
│   └── templates/             ← 2 template files
├── archive/                   ← 0 files (EMPTY — sanctioned but unused)
├── scripts/                   ← 16 files (memsync_daemon.py, journal_append.sh, + __pycache__ artifacts)
│   └── __pycache__/           ← compiled python files + temp artifacts
└── state/                     ← 40 files (hook outputs, retry counters, ontology.db, dispatch counts)
    ├── breakers/
    ├── budgets/
    ├── impl/
    │   ├── clarescence/
    │   ├── deploy/
    │   ├── kinetic/
    │   ├── sensing/
    │   └── techstack/
```

**The core question**: AGENTS.md v6.0.0 says `orchestration/` has `state/`, `scripts/`, `archive/`. It does NOT mention `00-ORCHESTRATION/`. Yet 462 of 528 files live inside `00-ORCHESTRATION/`. The sanctioned `state/` has 40 files (mostly hook outputs and counters), while `00-ORCHESTRATION/state/` has 242 files (the real state). The sanctioned `scripts/` has 16 files (mostly __pycache__), while `00-ORCHESTRATION/scripts/` has 127 files (the real scripts). The sanctioned `archive/` is EMPTY.

### State File Categories (00-ORCHESTRATION/state/)

Prefix distribution in the primary state directory:
- **ARCH-** (29 files): Architecture decisions, plans, protocols (e.g., ARCH-INTENTION_COMPASS.md, ARCH-MEMORY_ARCHITECTURE.md, ARCH-NEURAL_BRIDGE.md)
- **DYN-** (18 files): Dynamic/live state (e.g., DYN-DEFERRED_COMMITMENTS.md, DYN-CONSTELLATION_HEALTH.md, DYN-TASKS.csv)
- **REF-** (14 files): Reference documents (e.g., REF-PROCESSING_PATTERN.md, REF-STANDARDS.md, REF-TRIAGE_PROTOCOL.md)
- **IMPLEMENTATION-** (2 files): Backlog and map
- **SURFACE-** (1 file): Ontology dashboard
- **Other**: README.md, platform_capabilities.json, ontology.db files, dotfiles (.orchestrator_last_run, .watchdog_state)

### Script Categories (00-ORCHESTRATION/scripts/)

The 127 scripts break into these functional groups (you must verify membership):
- **Dispatch/Ingest**: dispatch.sh, auto_ingest_loop.sh, auto_ingest_all.sh, auto_ingest_supervisor.sh, triage_inbox.sh, triage_outgoing.sh, inbox_cleanup.sh
- **Session Hooks**: session_log.sh, ajna_pedigree.sh, create_execution_log.sh, pre_compaction.sh, intent_compass.sh
- **Monitoring/Health**: constellation_watchdog.sh, watchdog.sh, run_health.sh, corpus_health_check.py, verify_all.sh, verify_orchestration_hardening.sh, repo_integrity_gate.sh, ops_lint.sh
- **Cockpit/Launch**: cockpit.sh, mba-cockpit.sh, psyche_boot.sh, launch_cockpit_when_docker_ready.sh, iterm_launch_psyche_and_commander.applescript
- **Data/Ontology**: build_ontology_db.py, ontology_query.py, ontology_maintain.py, ontology_verify.py, ingest_rosetta_relations.py, rebuild_index.py
- **Canon/Content**: regenerate_canon.py, watch_canon.sh, compact_wisdom.sh, smart_convert.py
- **YouTube/Media**: youtube_ingest.py, youtube_oauth_setup.py, drain_watch_later.py, batch_transcribe.py
- **SN (Shorthand Notation)**: sn_decode.py, sn_encode.py, sn_expand.py, sn_symbols.yaml, SN_BLOCK_TEMPLATES.md
- **Configs/Sync**: _write_configs.py, sync_ledgers.py, sync_openclaw_skills.sh, skill_sync.sh, model_db.py
- **Sensing**: sensing-model-refresh.sh, trigger-model-refresh.sh, gen_surface.py, gemini_refine.py
- **Webhooks/External**: webhook_receiver.py, run_webhook.sh, chroma_server.py, run_chroma.sh
- **Deprecated?**: watch_dispatch.sh (CONFIRMED deprecated per AGENTS.md), setup-worktrees.sh, rearm_watchers.sh, commander_special_forces.sh
- **Documentation inside scripts/**: DESIGN-TMUX_COCKPIT.md, OAUTH2_SETUP_GUIDE.md, WATCH_LATER_DRAIN_SETUP.md, YOUTUBE_PIPELINE_SETUP.md, SN_BLOCK_TEMPLATES.md

### State File Categories (sanctioned state/)

The 40 files in `orchestration/state/` (the AGENTS.md-sanctioned location):
- **DYN-** (4 files): DYN-EXECUTION_STAGING.md, DYN-INTENTIONS_QUEUE.md, DYN-PEDIGREE_LOG.md, DYN-SESSION_LOG.md (hook outputs)
- **Counters** (~20 files): dispatch-YYYYMMDD.count, retry-{agent}-YYYYMMDDHH.count
- **Database**: ontology.db + WAL/SHM files + temp copies (.!nnnnn!ontology.db)
- **Other**: HANDOFF-COUNCIL-22.md, orchestration.breaker

### Dash-Prefix Directories (Dispatch Plumbing)

#### `-INBOX/` (5 files, 860 lines)
Commander-only inbox at `-INBOX/commander/00-INBOX0/`. Contains triangulation responses (RESPONSE-ORACLE-*, RESPONSE-VANGUARD-*, RESPONSE-DIVINER-*) and one TASK file. Other agents have NO inbox here — they use `agents/*/inbox/`.

#### `-OUTBOX/` (2 files, 488 lines)
Two result files from adjudicator and psyche, both dated 2026-02-16. Structured as `-OUTBOX/{agent}/RESULTS/RESULT-*.md`. Other agents empty.

#### `-SOVEREIGN/` (107 files, 11,381 lines)
- **Root** (21 files): SOVEREIGN-NNN decisions (002,003,006,010,011,014,015,016 — numbering has gaps), DECISION-*, ALERT-*, ESCALATION-*, REINIT-*, PROMPT-{MODEL}-* files
- **antifragile-scaffold-archive/** (10 files): Paired PROMPT/RESPONSE for three-model triangulation on antifragile scaffold design
- **ARCHIVED/** (4 files): Superseded sovereign decisions (mirrors of root files)
- **CONFIG-SANDBOX-2026-02-22/** (86 files): Full point-in-time config snapshot at safe build point `85140aaf`. Includes root-platform configs, engine YAMLs/JSONs, dotfiles, agent INITs, launchd plists, SSH config. Also mirrored as .zip.

**Triangulation loop**: PROMPT-{MODEL}-{TOPIC} in -SOVEREIGN/ → RESPONSE-{MODEL}-{TOPIC} in -INBOX/commander/00-INBOX0/

**Key architectural question**: -INBOX/-OUTBOX/-SOVEREIGN exist as dash-prefix top-level dirs while `agents/*/inbox/` and `agents/*/outbox/` ALSO exist as the newer agent-office dispatch system. These appear to be TWO coexisting dispatch topologies. Which is canonical? Are both needed?

---

## Constitutional Reference (AGENTS.md v6.0.0)

These rules are the law against which you are inspecting:

### Rule 1 — FLAT PRINCIPLE
All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-, FUNC-, PROMPT-, etc.) instead of subdirectories. **Sanctioned exceptions for orchestration/**: `state/`, `scripts/`, `archive/`.

**Inspection question**: `00-ORCHESTRATION/` is NOT a sanctioned exception. The nested subdirectories inside it (`state/impl/clarescence/`, `state/impl/kinetic/`, etc.) may also violate flatness. How deep does the nesting go?

### Rule 3 — PROTECTED ZONES
`orchestration/state/` and `canon/` require explicit Sovereign approval for deletions.

**Inspection question**: Which `state/` is protected — the sanctioned one (40 files) or the 00-ORCHESTRATION one (242 files)? Or both?

### Rule 4 — PHASE GATE RULE
No structural changes without scaffold_validate.sh passing, memory system operational, rollback tested.

### Rule 6 — CATEGORY ERROR
Metabolism applies to CONTENT, not ORCHESTRATION. State files and archives are living infrastructure — never delete.

### Rule 7 — LEDGER GROUND TRUTH
tasks.csv is authoritative. Verify actual state, not execution reports.

**Inspection question**: DYN-TASKS.csv exists in 00-ORCHESTRATION/state/. Is it current? Does it match reality?

### AGENTS.md Directory Structure Declaration
```
orchestration/   Strategic coordination (state/, scripts/, archive/)
```

**Inspection question**: The declared structure is `{state/, scripts/, archive/}`. The actual structure has `{00-ORCHESTRATION/{state/, scripts/, archive/, launchd/, templates/}, state/, scripts/, archive/}`. This is a significant divergence.

### Key File References in AGENTS.md
These files are explicitly referenced by path in AGENTS.md and MUST exist and be current:
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — referenced in Session Protocol
- `orchestration/state/DYN-TWIN_COORDINATION_PROTOCOL.md` — referenced in Key References
- `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` — referenced in Key References
- `orchestration/state/DYN-CONSTELLATION_HEALTH.md` — referenced in Health Watchdog
- `orchestration/state/DYN-EXECUTION_STAGING.md` — referenced in Completion Protocol
- `orchestration/scripts/dispatch.sh` — referenced in Dispatch Protocol
- `orchestration/scripts/auto_ingest_loop.sh` — referenced in Auto-Ingest System

**Inspection question**: Do these paths resolve correctly, or do they actually live under `00-ORCHESTRATION/`? If the latter, every AGENTS.md reference is broken.

---

## Required Output Format

### 1. Structural Verdict

Before per-file verdicts, answer these structural questions:

1. **Path Resolution Audit**: For every file path referenced in AGENTS.md, does it resolve? If it actually lives under `00-ORCHESTRATION/`, document the discrepancy.
2. **00-ORCHESTRATION Assessment**: Is this a legacy layer, a parallel structure, or the actual canonical location? What is the relationship between `orchestration/state/` and `orchestration/00-ORCHESTRATION/state/`?
3. **Flatness Violations**: List every subdirectory that violates Rule 1 (FLAT PRINCIPLE) and is NOT a sanctioned exception.
4. **Duplicate Detection**: Are any files duplicated between the sanctioned and 00-ORCHESTRATION layers?

### 2. Per-File Verdict Table

For EVERY file in `orchestration/`, produce a verdict row:

| File | Verdict | Confidence | Notes |
|------|---------|------------|-------|
| path/relative/to/orchestration/ | VERDICT | HIGH/MEDIUM/LOW | reason |

**Verdicts**:
- **CANONICAL**: Aligns with current architecture, actively referenced, content current
- **HIGH-SIGNAL**: Contains unique value but needs updating or better integration
- **STALE**: Content outdated, superseded by newer decisions, or contradicts current architecture
- **ORPHANED**: Zero inbound references and no clear pipeline membership
- **SUPERSEDED-BY:\<path\>**: Replaced by a specific newer document (cite it)
- **OPERATIONAL**: Runtime artifact (counters, locks, DB files) — not a document, judge by function not content
- **DEPRECATED**: Explicitly deprecated by current policy (e.g., watch_dispatch.sh)

For archive/ files, you may batch-verdict if they share a common status, but still list each file.

### 3. Per-Paragraph Granularity (Mixed-Verdict Files)

For any file where content is partially current and partially stale, provide paragraph-level verdicts with line references.

### 4. Cross-Reference Coherence Map

| Source File | References | Target Exists? | Target Current? |
|-------------|-----------|----------------|-----------------|
| file A | mentions file B | YES/NO | YES/STALE/UNKNOWN |

Focus on:
- AGENTS.md references to orchestration/ paths
- State files referencing other state files
- Scripts importing or sourcing other scripts
- README.md files pointing to documents

### 5. Pipeline Membership

For every script in `scripts/` (both locations), classify:

| Script | Pipeline | Called By | Calls | Status |
|--------|----------|-----------|-------|--------|
| script.sh | dispatch / ingest / monitoring / session-hooks / data / media / launch / sensing / deprecated | what invokes it | what it invokes | ACTIVE / DORMANT / DEPRECATED |

### 6. Dispatch Architecture Assessment

Evaluate the dual dispatch topology:

| Topology | Components | Files | Active? | Evidence |
|----------|-----------|-------|---------|----------|
| **Dash-prefix** | `-INBOX/`, `-OUTBOX/`, `-SOVEREIGN/` | 114 | ? | (what uses it, what references it) |
| **Agent-office** | `agents/*/inbox/`, `agents/*/outbox/` | varies | ? | (what uses it, what references it) |

Answer:
1. **Which topology is canonical?** What does `dispatch.sh` actually write to? What does `auto_ingest_loop.sh` actually read from?
2. **Are they complementary or redundant?** (e.g., dash-prefix for Sovereign async decisions, agent-office for agent-to-agent dispatch)
3. **Is -SOVEREIGN/ the Sovereign's "agent office"?** Should it be `agents/sovereign/` instead?
4. **Verdict**: SOUND / NEEDS-UNIFICATION / NEEDS-RESTRUCTURING — with evidence and specific observations (NOT proposals).

### 7. Anomalies Detected

Report anything that doesn't fit:
- Naming inconsistencies (e.g., markdown files inside scripts/)
- Temporal anomalies (files dated before or after the system's active period)
- Conceptual duplicates (two files covering the same topic under different names)
- Dead references (files mentioned nowhere)
- Contradictions between files
- __pycache__ and temp files that should be .gitignored
- The ontology.db temp copies (.!nnnnn!ontology.db pattern)

---

## Rules of Engagement

1. **INSPECT, don't redesign.** Your job is to produce verdicts, not proposals. If you find yourself writing "should be moved to" or "would be better as" — stop. That is not your mission.
2. **Every file gets a verdict.** No skipping, no "and similar files." Each of the 642 files (528 orchestration + 114 dash-prefix) appears in your output.
3. **Evidence-based.** When claiming STALE or SUPERSEDED, cite the specific content (line, section, date) that makes it stale, and cite the specific newer document that supersedes it.
4. **Read before judging.** Do not verdict based on filename alone. Open the file. Check the content. A file named ARCH-NEO_CANON_CORE.md might be superseded or might contain unique unrecovered value.
5. **The 00-ORCHESTRATION question is your #1 priority.** The entire inspection hinges on understanding what this layer is, why it exists, and whether it or the parent `orchestration/` is the real ground truth.
6. **watch_dispatch.sh is CONFIRMED deprecated.** AGENTS.md explicitly says so. Use this as a calibration anchor — if your analysis agrees, your methodology is sound.
7. **Check DYN-TASKS.csv against reality.** Constitutional Rule 7 says it's authoritative. Verify.
8. **Report temp/cache files.** __pycache__, .!nnnnn! files, .DS_Store — these are cleanup candidates but report them, don't delete them.

---

## Deliverable

A single markdown document titled `RESULT-ORACLE-DC201-SCAFFOLD_DEEP_INSPECTION.md` containing all sections above. This document will be triangulated against Cartographer (engine-perspective) and Adjudicator (praxis-perspective) inspections to produce a convergent verdict before any action is taken.

**The Sovereign will place your result at**: `agents/commander/inbox/pending/RESULT-ORACLE-DC201-SCAFFOLD_DEEP_INSPECTION.md`

---

## Anti-Pattern Warning

The INT-2210 disaster sequence:
1. Agent received "triage the scaffold"
2. Agent interpreted this as permission to reorganize
3. Agent deleted 3,966 lines of architectural docs
4. Agent renamed directories
5. Agent dissolved structures
6. Six commits had to be reverted

You are step 1. Your output enables step 2 (which a DIFFERENT agent will do, with Sovereign approval). If your output contains any `mv`, `rm`, `mkdir`, or `git` commands — you have failed your mission. You produce INTELLIGENCE. Others act on it.
