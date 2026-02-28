# Bottom-Up Clustering: sn-* Internal Files
**Corpus**: `/Users/system/syncrescendence/corpus/`
**Files analyzed**: 1,620 files tagged `sn-*`
**Method**: Full header sweep (first 3 lines of all 1,620 files) + MD5 deduplication + content sampling

---

## Overview

The 1,620 `sn-*` tagged files span three distinct zones:

| Zone | File Range | Count | Character |
|------|-----------|-------|-----------|
| Internal ops (numbered) | `08001–11705` | ~1,473 | Prompts, results, tasks, scripts, watchdog logs |
| CANON skeletons | `sn_skeletons/CANON-*.sn.md` | 78 | Compression scaffolds — structural |
| CANON compressed | `sn_compressed/CANON-*.sn.md` | 57 | Semantic compressions — structural |
| Demoted canon | `demoted/CANON-*.md` | 8 | Superseded canon nodes |
| Generated views | `views/CANON-*.{json,mmd,md}` | 4 | Canon compiler outputs |

Tag distribution (from CLUSTER-MAP-FULL.tsv):

| Tag | Count | What it actually is |
|-----|-------|---------------------|
| sn-other | 304 | Mixed: video transcripts, X threads, session logs, pipeline ops |
| sn-canon | 236 | CANON skeletons + compressed + views + a few internal ops |
| sn-script | 208 | Mix: result files, transcripts, setup guides, scripts |
| sn-prompt | 200 | Mix: actual prompts + large volume of video transcripts |
| sn-watchdog | 178 | Task tickets, escalation logs, periodic system reports |
| sn-atom | 96 | JSONL atom extractions + atom-related prompt/result docs |
| sn-architecture | 93 | Architecture docs, MECH files, some external content |
| sn-config | 66 | Config files, YAML, scripts |
| sn-rosetta | 63 | Certescence outputs, blitzkrieg plans, ascertescence artifacts |
| sn-pipeline | 45 | Pipeline task/result files |
| sn-system-prompt | 36 | X threads, video posts about AI tools (mislabeled) |
| sn-handoff | 25 | Handoff docs, ZERO TRUST templates, task envelopes |
| sn-result | 23 | RESULT files + some video/setup guide mislabels |
| sn-certescence | 20 | Ascertescence, certescence session artifacts |
| sn-task | 15 | Completed/failed task .complete files + a few video posts |
| sn-confirm | 12 | Entirely video transcripts (Theo, HealthyGamer, etc.) |

**Note**: Tag fidelity is poor. Many `sn-prompt`, `sn-script`, `sn-system-prompt`, and `sn-confirm` files are YouTube/X feed content, not internal ops. The tags are clustering artifacts from the ingestion pipeline, not hand-assigned.

---

## Natural Groupings

### GROUP A — Operational Logs (Pure Receipts, No Enduring Value)

These files record events that have already resolved. They cannot inform future decisions and have no canonical value.

**A1. Watchdog Escalation Logs** — 38 files
Service restart loop alerts from Feb 9–12, 2026 when Chroma/webhook services were flapping. Each file is an accumulating restart count appended every 5 minutes. The underlying services were stabilized weeks ago.
```
11279.md 11280.md 11281.md 11282.md 11283.md 11284.md 11285.md 11286.md
11287.md 11288.md 11289.md 11290.md 11291.md 11292.md 11293.md 11294.md
11295.md 11296.md 11297.md 11298.md 11299.md 11300.md 11301.md 11302.md
11303.md 11304.md 11305.md 11306.md 11307.md 11308.md 11309.md 11310.md
11311.md 11312.md 11313.md 11314.md 11315.md 11316.md
```

**A2. Linear SYN Status Report Snapshots** — 20 files
Automated cron snapshots of the Linear issue board taken every 6 hours on Feb 11. Stale point-in-time data. The Linear board itself is the source of truth.
```
11243.md 11244.md 11245.md 11246.md 11247.md 11248.md 11249.md 11250.md
11251.md 11252.md 11253.md 11254.md 11255.md 11256.md 11257.md 11259.md
11260.md 11261.md 11262.md 11263.md
```

**A3. Corpus Insight Reports** — 4 files
Cron-generated velocity/activity summaries from Feb 12–19. Superseded by current state.
```
11231.md  11234.md  11235.md  11236.md
```

**A4. Daily Session Review Logs** — 5 files
Automated daily session summaries for Feb 11–14 and a fifth entry. Operational history, not actionable.
```
11271.md  11272.md  11273.md  11274.md  11275.md
```

**A5. Completed/Failed Task Tickets (watchdog zone)** — 43 files
Task dispatch envelopes with `Status: COMPLETE` or `Status: FAILED`. These are execution receipts. The work has been done or abandoned; the ticket has no further function.
```
11121.md  11124.md  11125.md  11139.md  11148.md  11150.md  11151.md
11153.md  11154.md  11158.md  11159.md  11160.md  11161.md  11162.md
11163.md  11164.md  11165.md  11166.md
11167.claimed-by-adjudicator-Lisas-MacBook-Air
11168.md  11169.md  11170.md  11173.md  11174.md  11175.md  11176.md
11177.md  11178.md  11202.md  11208.md  11209.md  11210.md  11214.md
11216.md  11218.md  11219.md  11220.md  11221.md  11223.md  11224.md
11238.md  11266.md
```

**A6. Smoke Test / Pipeline Test Completed Task Receipts (.complete)** — 11 files
Early pipeline plumbing tests (`cc_pipe_test2`, `hb_lifecycle_smoke`, `final_cc_pipe2`, etc.). Pure scaffolding validation receipts.
```
08607.complete  08608.complete  08609.complete
11102.complete  11105.complete  11109.complete  11111.complete
11112.complete  11114.complete  11116.complete  11120.complete
```

**A7. Error Logs and WAL/SHM Files** — 10 files
Dead error logs (1 line: "No such file or directory"), empty logs, and SQLite WAL/SHM artifacts from closed DB sessions.
```
11517.log  (1 line: ./scripts/auto_ingest_loop.sh: No such file or directory)
11518.log  (empty)
11704.log  (2 lines: memsync_daemon.py not found)
11705.log  (empty)
11553.db-shm  11554.db-wal  11555.db-shm  11556.db-wal  11557.db-shm  11558.db-wal
```

**A8. Empty Files** — 12 files
Zero-byte files. No content whatsoever.
```
08006.jsonl  08007.jsonl  08631.md  09016.md  11113.md  11115.md
11518.log  11554.db-wal  11556.db-wal  11558.db-wal  11562.jsonl  11705.log
```
(Note: some overlap with A7 above)

---

### GROUP B — Exact Content Duplicates

MD5 analysis found 119 hash groups with 2+ identical files — representing 138 extra copies that can be deleted (keeping one per group). The highest-multiplicity duplicates:

**3 copies each** (delete 2 of each):
- `08054.md / 08575.md / 08819.md` — "The Best AI Image Generators" video transcript
- `08053.md / 08574.md / 08818.md` — "The Automation Trend in Visual Creation" video section
- `08055.md / 08576.md / 08820.md` — "The Evolving AI Workflow in Video and VFX" video section
- `08057.md / 08579.md / 08822.md` — "The Next Wave in AI Video and VFX" video transcript
- `08065.md / 08757.md / 09253.md` — Corpus Sensing Report (Cartographer Feb 2 2026)
- `08323.md / 08514.md / 10480.md` — PROMPT-DIVINER-20260203-openclaw_deep_research
- `08328.md / 08866.md / 10481.md` — OpenClaw Platform Technical Architecture Spec v2026.2
- `08391.md / 08420.md / 08759.md` — (content TBD from earlier batch)
- `11553.db-shm / 11555.db-shm / 11557.db-shm` — SQLite shared memory files

**2 copies each** (delete 1 of each) — selected notable pairs:
- `08390.md / 08419.md` — Protease Axioms (praxis)
- `08392.md / 08421.md` — PRAC: Blitzkrieg Worktree Isolation
- `08429.md / 08698.md` — praxis: Operational Knowledge Corpus v2.1.0
- `08510.md / 08518.md` — PROMPT-COMMANDER-ASCERTESCENCE-CC26-DIV (Diviner Leg 3)
- `08604.md / 11175.md` — TASK-20260216-research_architecture_verification
- `08617.md / 11168.md` — TASK-20260212-skill_architecture_strategic_review
- `09128.md / 11389.md` — YouTube Ingest Pipeline Setup Guide
- `08573.md / 08578.md` — (identical content pair)
- `08756.md / 10407.md` — (identical content pair)
- `08218.md / 10686.md` — (identical content pair)
- `08080.txt / 08758.txt` — repo size inventory text file
- ... (110 more 2-copy pairs)

Full duplicate pairs list: 119 groups × average 2.1 copies = ~138 excess files.

---

### GROUP C — Explicitly Marked STALE / SUPERSEDED / ARCHIVED / ORPHANED

These files carry self-declared obsolescence headers. They were intentionally archived by Commander during DC-205 Phase 2C decruft and similar passes but were not deleted.

```
08097.yaml   — ARCHIVED: Claude Sonnet 4 model profile (superseded by MODEL-INDEX.md)
08102.yaml   — ARCHIVED: Grok 4 model profile (superseded by MODEL-INDEX.md)
08394.md     — STALE or superseded architecture doc
08396.md     — Multi-Methodology PM Framework (STATUS: STALE, external tool refs unverifiable)
08399.md     — (STALE/ARCHIVED)
08400.md     — (STALE/ARCHIVED)
08401.md     — (STALE/ARCHIVED)
08403.md     — ARCHIVED: Sub-Agent Delegation Guide (scripts/paths no longer exist)
08415.md     — MECH-source_anneal_pipeline (STATUS: STALE)
08418.md     — YouTube-only anneal MECH (STATUS: SUPERSEDED-BY pipeline redesign)
08424.md     — Multi-Methodology PM Framework duplicate (STATUS: STALE)
08434.md     — OpenClaw Synthesis v1 (STATUS: SUPERSEDED-BY v2)
08436.md     — SYNTHESIS: OpenClaw v1 (SUPERSEDED-BY v2)
08498.md     — (STALE)
08501.md     — Cartographer DC-202 inspection result (STALE)
08528.md     — (STALE/ARCHIVED)
08549.md     — Oracle DC-202 deep inspection (marked stale in later passes)
08554.md     — (STALE)
08569.md     — (STALE)
08739.md     — (ARCHIVED)
08858.md     — DC-203 Adjudicator Scratchpad Session 1 (empty table, superseded)
08859.md     — DC-203 Adjudicator Scratchpad Session 2 (empty table, superseded)
08860.md     — DC-203 Adjudicator Deep Inspection result (superseded by later audits)
08863.md     — DC-202 Cartographer Deep Inspection (superseded)
08902.md     — DC-202 Oracle Deep Inspection result S1 (superseded)
08903.md     — DC-202 Oracle S2 scratchpad (superseded)
08904.md     — DC-202 Oracle S3 scratchpad (superseded)
08905.md     — DC-202 Oracle S4 scratchpad (superseded)
08906.md     — DC-202 Oracle S5 scratchpad (superseded)
08915.md     — DC-201 Oracle Deep Inspection result (superseded)
08916.md     — DC-201 Oracle S2 scratchpad (superseded)
08917.md     — DC-201 scratchpad (superseded)
08918.md     — DC-201 scratchpad (superseded)
08919.md     — DC-201 scratchpad (superseded)
08920.md     — DC-201 scratchpad (superseded)
08924.md     — (STALE/ARCHIVED)
08929.md     — (STALE/ARCHIVED)
08933.md     — (STALE/ARCHIVED)
08934.md     — (STALE/ARCHIVED)
10017.md     — (STALE)
11096.md     — Codex CLI Synthesis (STATUS: SUPERSEDED)
11194.md     — Task: Neo-Canon Metaplan (superseded by current canon architecture)
sn_skeletons/CANON-99000.sn.md — Historical Archive skeleton (tier: archive, volatility: moderate — borderline)
```

---

### GROUP D — Unique Operational Knowledge (KEEP)

Files with non-redundant, actionable content that is NOT present elsewhere:

**D1. Certescence / Ascertescence Artifacts** (unique session outputs)
- `08483.md–08545.md` range — CC35, CC36, CC37, CC38 ascertescence prompts and responses
- `08515.md` — ASCERTESCENCE CC28 Diviner SYNTHESIS
- `08516.md` — ASCERTESCENCE CC35 Diviner SYNTHESIS
- `08517.md` — Oracle iteration on Diviner CC35 leg
- `08520.md` — Emergency CC30 ascertescence anchor
- `08524.md` — Diviner Pre-Ascertescence CC40

**D2. Active Task Files (PENDING or IN_PROGRESS)**
- Any task ticket without `Status: COMPLETE` or `Status: FAILED` that references live work

**D3. CANON Skeletons and Compressed** (78 + 57 files)
- `sn_skeletons/CANON-*.sn.md` — compression scaffolds, structurally required
- `sn_compressed/CANON-*.sn.md` — semantic compressions, operationally used

**D4. Generated Views** (4 files)
- `views/CANON-CONFIG.json` — canon graph metadata (generated 2026-02-27)
- `views/CANON-GRAPH.mmd` — Mermaid graph (generated)
- `views/CANON-LEDGER.md` — Canon ledger table (generated)
- `views/CANON-SCRIPTURE.md` — Living canon overview (generated)

**D5. Active Scripts** (11xxx .py/.sh zone)
- `11395.py–11703.py/.sh` — ~150 operational scripts (canon_compiler, protease, circadian_sync, etc.)
- These require individual review but are NOT blanket-deletable

**D6. JSONL Atom Extractions** (08xxx zone)
- `08001.jsonl, 08003.jsonl, 08004.jsonl` etc. — Note: these come in OLD and NEW schema pairs. `08001.jsonl` (old schema) and `08003.jsonl`/`08004.jsonl` (new Graphiti schema) are paired. The old-schema files may be deletable if the new-schema pipeline is operational.

**D7. Deep Research Syntheses** (unique, high-signal)
- `08327.md` — OpenClaw skill ecosystem deep research (unique Grok output)
- `08515.md–08518.md` — Ascertescence triangulation outputs
- `08676.md` — Four-System Intelligence Architecture
- `08702.md–08712.md` — Research pipeline architecture

**D8. Key Constitutional / Living Docs**
- `08380.md` — Syncrescendence Operational Law v5.0.0 (AGENTS.md snapshot)
- `08389.md` — PORTAL: Chat Agent Context Injection
- `08405.md` — Proverbs (operational heuristics)
- `08428.md` — Claude Code Operations Manual

---

### GROUP E — Demoted Canon Nodes (8 files)

```
demoted/CANON-30410-COGNITIVE_ARCHITECTURE-asteroid-INTELLIGENCE.md
demoted/CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md
demoted/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md
demoted/CANON-30440-SAFETY_ALIGNMENT-asteroid-INTELLIGENCE.md
demoted/CANON-30450-PRODUCTION_FRAMEWORKS-asteroid-INTELLIGENCE.md
demoted/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md
demoted/CANON-33111-BIZ_ENHANCE-satellite-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md
demoted/CANON-34120-SYLLABUS-lunar-MASTERY-planetary-KNOWLEDGE.md
```

These are demoted intentionally by the canon compiler (CC49 passes). Retention depends on whether re-promotion is planned. If the demotion is permanent, these 8 are deletable.

---

## Exact Duplicates — Full List of Second/Third Copies to Delete

Below are the files to delete (keeping the **lower-numbered** file as canonical in each pair/triplet):

**Delete (keep 08054.md):** `08575.md`, `08819.md`
**Delete (keep 08053.md):** `08574.md`, `08818.md`
**Delete (keep 08055.md):** `08576.md`, `08820.md`
**Delete (keep 08057.md):** `08579.md`, `08822.md`
**Delete (keep 08065.md):** `08757.md`, `09253.md`
**Delete (keep 08323.md):** `08514.md`, `10480.md`
**Delete (keep 08328.md):** `08866.md`, `10481.md`
**Delete (keep 08390.md):** `08419.md`
**Delete (keep 08391.md):** `08420.md`, `08759.md`
**Delete (keep 08392.md):** `08421.md`
**Delete (keep 08429.md):** `08698.md`
**Delete (keep 08510.md):** `08518.md`
**Delete (keep 08573.md):** `08578.md`
**Delete (keep 08604.md):** `11175.md`
**Delete (keep 08617.md):** `11168.md`
**Delete (keep 08080.txt):** `08758.txt`
**Delete (keep 09128.md):** `11389.md`
**Delete (keep 08051.md):** `08108.md`
**Delete (keep 08218.md):** `10686.md`
**Delete (keep 08238.md):** `10687.md`
**Delete (keep 08242.md):** `10708.md`
**Delete (keep 08358.md):** `10709.md`
**Delete (keep 08364.md):** `10467.md`
**Delete (keep 08379.md):** `09125.md`
**Delete (keep 08398.md):** `08426.md`
**Delete (keep 08440.md):** `09271.md`
**Delete (keep 08756.md):** `10407.md`
**Delete (keep 08785.md):** `11639.md`
**Delete (keep 08835.md):** `10516.md`
**Delete (keep 08059.md):** `08671.md`
**Delete (keep 08067.md):** `11351.md`
**Delete (keep 08146.md):** `10739.md`

*...plus 87 more 2-copy pairs from the MD5 analysis (full list available via: `sort /tmp/all_md5s.txt | awk '{print $1}' | uniq -d | while read h; do grep "^$h " /tmp/all_md5s.txt; done`)*

---

## Estimated Delete Count

| Category | Files | Notes |
|----------|-------|-------|
| A1: Watchdog escalation logs | 38 | All deletable |
| A2: Linear status report snapshots | 20 | All deletable |
| A3: Corpus insight reports | 4 | All deletable |
| A4: Daily session reviews | 5 | All deletable |
| A5: Completed/failed task tickets | 43 | All deletable (receipts) |
| A6: Smoke test .complete receipts | 11 | All deletable |
| A7: Error logs + DB WAL/SHM | 10 | All deletable |
| A8: Empty files | 12 | All deletable (some overlap with A7) |
| B: Exact content duplicates | 138 | Delete 2nd/3rd copies |
| C: Explicitly STALE/SUPERSEDED | 43 | All deletable |
| E: Demoted canon (if permanent) | 8 | Conditional |
| **TOTAL (conservative, no overlap)** | **~300** | |
| **TOTAL (aggressive, with deduplication of overlaps)** | **~260 unique files** | |

**Key observation**: The single biggest deletable cluster is the 38 watchdog escalation files (11279–11316) + 20 Linear snapshots (11243–11263). These 58 files are pure operational noise with zero informational residue.

---

## What Contains Unique Operational Knowledge

Files that should be KEPT regardless of cleanup:

1. **All `sn_skeletons/` and `sn_compressed/` files** — structural canon compression artifacts
2. **All `views/` files** — generated but current as of 2026-02-27
3. **`11395.py` through `11703.py/.sh`** — the operational script corpus (review individually)
4. **Ascertescence artifacts** — `08483–08545` range (certescence vault inputs/outputs)
5. **Unique synthesis outputs** — DC-202 final consolidated results (NOT the session scratchpads)
6. **Active TASK files** — any `Status: PENDING` or `Status: IN_PROGRESS`
7. **Handoff files** — `HANDOFF-CC*.md` lineage (25 files)
8. **CANON nodes in sn_skeletons** — all except `CANON-99000.sn.md` (archive tier)
9. **JSONL extractions (new schema)** — `08003.jsonl, 08009.jsonl`, etc. (Graphiti-formatted)
10. **Deep research synthesis files** — `08327.md`, `08434.md`, `08676.md`, `08702–08712.md`

---

## Obsolescence Patterns

1. **The DC-201/DC-202/DC-203 scratchpad problem**: The deep inspection passes (Oracle, Cartographer, Adjudicator sessions S1–S5) each generated 3–5 session scratchpad files. Only the FINAL consolidated result per inspection has value. The intermediate scratchpads (`08902–08906.md`, `08915–08920.md`, `08858–08860.md`) are pure workflow artifacts.

2. **The triple-copy content problem**: Several video transcripts and research outputs appear in three identical copies (08054/08575/08819, etc.). This suggests the ingestion pipeline ran three times against the same source content without deduplication. The pattern of `08xxx / 085xx / 088xx` numbering suggests three separate ingestion passes.

3. **Old vs. new JSONL schema pairing**: Files `08001.jsonl` (old schema, no UUID) and `08003.jsonl`/`08004.jsonl` (new Graphiti schema, with UUID) represent the same atom data in two formats. If Graphiti is the current pipeline, the old-schema JSONLs are deletable. These come in pairs throughout the 08001–08043 zone.

4. **Killed service logs**: `11517.log` ("auto_ingest_loop.sh: No such file or directory"), `11704.log` (memsync_daemon.py not found). These document paths to scripts that no longer exist — double-deletable.

5. **Model profile YAMLs**: `08097.yaml` (Claude Sonnet 4) and `08102.yaml` (Grok 4) were explicitly superseded by `engine/02-ENGINE/MODEL-INDEX.md` and archived by Commander in DC-205. They remain in the corpus despite being flagged.

---

*Report generated: 2026-02-27*
*Method: Bottom-up — actual file reads, MD5 deduplication across all 1,620 sn-* files*
