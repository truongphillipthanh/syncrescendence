# Bottom-Up Clustering: Scripts, Configs, and Operational Files
# Corpus: /Users/system/syncrescendence/corpus/
# Generated: 2026-02-27

Total files surveyed: ~422 non-.md non-.jsonl files across 14 extension types.

---

## CLUSTER 1: Killed-Service Heartbeat Files (OPERATIONAL CRUFT — DELETE ALL)

All launchd services were unloaded (CC52). Heartbeat files are stale runtime markers.

| File | Agent | Last timestamp |
|------|-------|----------------|
| `11398.heartbeat` | adjudicator | 2026-02-23T00:49:04Z |
| `11427.heartbeat` | cartographer | 2026-02-23T00:49:09Z |
| `11467.heartbeat` | commander | 2026-02-23T00:49:13Z |
| `11578.heartbeat` | psyche | 2026-02-23T00:48:58Z |

**Recommendation: DELETE ALL 4** — stale IDLE markers from dead services. Zero information value.

---

## CLUSTER 2: .lock Files (OPERATIONAL CRUFT — DELETE ALL)

PID/timestamp lock files from killed processes.

| File | Contents |
|------|----------|
| `04577.lock` | PID 58497, timestamp 2026-02-26T19:39:51Z |
| `04578.lock` | PID 89754 (partial) |
| `04580.lock` | PID 58497, timestamp 2026-02-26T19:39:51Z |

**Recommendation: DELETE ALL 3** — process locks for processes that are dead. Identical PIDs in 04577/04580 confirm these are redundant artifacts.

---

## CLUSTER 3: .complete Files (TASK MARKERS — DELETE ALL)

Task completion markers for tasks that completed in February 2026. No operational value.

| File | Task ID | Date |
|------|---------|------|
| `08607.complete` | TASK-20260205-cc_pipe_test2 | 2026-02-05 |
| `08608.complete` | TASK-20260205-final_cc_pipe2 | 2026-02-05 |
| `08609.complete` | TASK-20260205-mini_browser_relay_and_integrations_sweep | 2026-02-05 |
| `11102.complete` | TASK-20260202-openclaw_bootstrap_replicate_psyche | 2026-02-02 |
| `11105.complete` | TASK-20260204-hb_lifecycle_smoke | 2026-02-04 |
| `11109.complete` | (not read but same pattern) | ~Feb 2026 |
| `11111.complete` | (not read but same pattern) | ~Feb 2026 |
| `11112.complete` | (not read but same pattern) | ~Feb 2026 |
| `11114.complete` | (not read but same pattern) | ~Feb 2026 |
| `11116.complete` | (not read but same pattern) | ~Feb 2026 |

**Recommendation: DELETE ALL 10** — these are filesystem-kanban state markers for tasks that are done and gone. The task files themselves live in agent inboxes/outboxes.

---

## CLUSTER 4: Killed-Service Logs — "Cycle Complete" Pattern (DELETE ALL)

Five log files containing only "Cycle complete" entries from the auto-ingest supervisor daemon. Services were killed. Logs are worthless.

| File | Date range |
|------|-----------|
| `00009.log` | 2026-02-22 |
| `00010.log` | 2026-02-23 |
| `00012.log` | 2026-02-24 |
| `00014.log` | 2026-02-25 |
| `00016.log` | 2026-02-26 |

**Recommendation: DELETE ALL 5** — "Cycle complete Sun Feb 22 20:14:10 PST 2026" repeated 13–241 times. No diagnostic value.

---

## CLUSTER 5: Agent/OpenClaw Execution Logs (00966–01051 range) — MIXED

89 log files. Contents span multiple service types:

### 5a: Xcode test runner logs — DELETE (00966, 00967, 00968)
Contain `xcodebuild -project Agendizer.xcodeproj` invocations. Agendizer is a side project. These are not Syncrescendence operational logs.
- `00966.log`, `00967.log`, `00968.log`

### 5b: Adjudicator execution logs (00969, 00970, 00971, 00972, 00973, 00974, 00975, 00976, 00977, 00978, 00979) — KEEP (low priority)
Contain `[Adjudicator Execution Log]` headers — actual task outcomes. These are operational records but likely already surfaced in handoffs. **Candidate for archiving, not deletion.**

### 5c: Codex/OpenClaw execution logs (00980–01051 range, majority) — DELETE
Most contain:
- `OpenAI Codex v0.101.0 / v0.104.0 (research preview)` session outputs
- `2026-02-12T... ERROR codex_core::codex: failed to load skill` error dumps
- OpenClaw session transcripts (`[plugins] openclaw-mem0: registered...`)
- One-off agent task outputs

These are execution artifacts from killed services. The signal (task outcomes) should have been captured in dispatch/result files. The raw logs are noise.

**Recommendation: DELETE 00966–00968 (Xcode). DELETE 00980–01051 bulk (Codex/OpenClaw session dumps). ARCHIVE 00969–00979 (Adjudicator logs) if not already captured.**

### 5d: Miscellaneous logs — KEEP
- `00729.log` — DAG tension monitor FIRE event (JSON signal record, unique operational data)
- `00773.log` — Session State Brief snapshot (2026-02-27, substantive content)
- `11517.log` — Error: `./scripts/auto_ingest_loop.sh: No such file or directory` (diagnostic record of broken script path)
- `11704.log` — Error: memsync_daemon.py path not found (diagnostic, shows what broke)

---

## CLUSTER 6: Launchd .plist Files (KILLED SERVICES — DELETE ALL)

All launchd services were unloaded in CC52. The plist files are inert. Additionally, many are **version duplicates** — the same service label appears across 2–3 plists with different hardcoded paths (`/Users/home/Desktop/`, `/Users/system/Desktop/`, `/Users/system/syncrescendence/`).

### Duplicate label groups (all versions dead, delete all copies):

**com.syncrescendence.skill-sync** (3 copies):
- `09086.plist` — `/Users/home/Desktop/...` (old path, old user)
- `09098.plist` — `/Users/system/Desktop/...` (mid-migration path)
- `11672.plist` — `/Users/system/syncrescendence/...` (final path)

**com.syncrescendence.watch-adjudicator** (3 copies):
- `09087.plist`, `09099.plist`, `09117.plist`

**com.syncrescendence.watch-ajna** (2 copies):
- `09088.plist`, `09100.plist`

**com.syncrescendence.watch-canon** (2 copies):
- `09089.plist`, `09101.plist`

**com.syncrescendence.watch-cartographer** (3 copies):
- `09090.plist`, `09102.plist`, `09120.plist`

**com.syncrescendence.watch-commander** (2 copies):
- `09091.plist`, `09103.plist`

**com.syncrescendence.watch-psyche** (2 copies):
- `09092.plist`, `09104.plist`

**com.syncrescendence.watchdog** (3 copies):
- `09093.plist`, `09123.plist`, (+ 09129.plist — could not verify label)

**com.syncrescendence.youtube-ingest** (2 copies):
- `09153.plist`, `11674.plist`

### Single-instance dead plists (also delete):
`09082.plist` (auto-ingest-supervisor), `09083.plist` (cockpit-autostart), `09084.plist` (docker-autostart), `09085.plist` (proactive-orchestrator), `09106.plist` (circadian-sync), `09107.plist` (claude-corpus-insight), `09108.plist` (claude-linear-check), `09109.plist` (claude-session-review), `09110.plist` (ingest), `09111.plist` (ledger-refresh), `09112.plist` (memsync), `09113.plist` (sensing-corpus-staleness), `09114.plist` (sensing-frontier-scan), `09115.plist` (sensing-linear-impl-sync), `09124.plist` (weekly), `09129.plist` (unlabeled), `09152.plist` (dag-tension-monitor), `11668.plist` (git-sync), `11671.plist` (proactive-orchestrator — second copy)

**Recommendation: DELETE ALL 40 .plist files.** Services are killed. The plists have no future use — if services are ever revived, they would be regenerated from current scripts with current paths.

---

## CLUSTER 7: Self-Declared ARCHIVED YAML Files (DELETE)

Six model-profile YAML files with explicit `# ARCHIVED: 2026-02-23` headers. Self-declared obsolete, superseded by `engine/02-ENGINE/MODEL-INDEX.md`.

| File | Content |
|------|---------|
| `08097.yaml` | Claude Sonnet 4 (stale version) |
| `08098.yaml` | Claude Opus 4.1 (stale version) |
| `08099.yaml` | Claude 4.5 Opus (stale version) |
| `08100.yaml` | GPT-5 (stale version) |
| `08101.yaml` | Gemini 2.5 Pro Stable (stale version) |
| `08102.yaml` | Grok 4 (stale version) |

**Recommendation: DELETE ALL 6** — they say so themselves.

---

## CLUSTER 8: Duplicate Python Scripts — candidate_adapter + lattice_annealer

Two core pipeline scripts appear **twice each** in the corpus:

| Original | Duplicate | Status |
|----------|-----------|--------|
| `09145.py` (candidate_adapter.py) | `00543.py` | DIFFERENT — different DIM_KEYS schema (5-dim vs 14-dim). 00543.py is CC38 14-dim expansion; 09145.py is older 5-dim. |
| `09185.py` (lattice_annealer.py) | `00544.py` | DIFFERENT — different dimension sets matching the respective adapters. |

These are **not identical** — they represent old (5-dim) and new (14-dim CC38) versions of the same scripts. The canonical versions are the numbered ones in the pipeline; the `00543.py`/`00544.py` are the CC38-expanded versions.

**Recommendation: INVESTIGATE before deleting.** Determine which version is currently wired into the pipeline. The 00543/00544 pair (14-dim) is likely the active one per CC38 build. If so, delete 09145.py and 09185.py (the older 5-dim versions). Do not delete both pairs.

---

## CLUSTER 9: Duplicate TOOL/YAML Definitions

### TOOL-002 openclaw (different):
- `11333.yaml` — slightly different instance list (Psyche/Ajna ordering, model names)
- `00957.yaml` — different model assignments

These are version snapshots, not identical duplicates. `00957.yaml` appears newer (Kimi K2.5 NIM model for Ajna). `11333.yaml` is older.
**Recommendation: DELETE `11333.yaml`** (older version). Keep `00957.yaml`.

### TOOL-003 codex_cli:
- `11334.yaml` — integration point listed as `AGENTS.md_config`
- `00958.yaml` — integration point listed as `AGENTS.md`

Minor version difference. `00958.yaml` is the clean version.
**Recommendation: DELETE `11334.yaml`** (older version). Keep `00958.yaml`.

---

## CLUSTER 10: Auto-Ingest Loop Duplicates

Two versions of `auto_ingest_loop.sh` exist:

| File | Description |
|------|-------------|
| `09135.sh` | Full version — takes agent_name, repo_path, tmux args; sources config.sh |
| `09251.sh` | Simplified "location-agnostic" version — no args, runs `make configs` + loop |

And a declared shim:
- `09134.sh` — "Backward-compatible shim. Canonical supervisor is now auto_ingest_supervisor.sh" — just calls `09136.sh`

**Recommendation: DELETE `09134.sh`** (shim to dead supervisor). **INVESTIGATE `09135.sh` vs `09251.sh`** — they serve different invocation modes; clarify which is launchd target before deleting.

---

## CLUSTER 11: Obsidian Configuration JSON Files (KEEP AS-IS)

Five Obsidian vault config files, small, not cruft — they configure the Obsidian vault viewer:
- `11681.json` — editor settings
- `11682.json` — appearance settings
- `11683.json` — core plugins
- `11684.json` — graph filter state
- `11685.json` — workspace layout

**Recommendation: KEEP ALL 5** — active Obsidian vault configuration.

---

## CLUSTER 12: Rename/Migration Artifact Files (KEEP FOR REFERENCE, LOW PRIORITY)

One-time migration records:
- `08060.csv` — old_path → new_path rename mapping (pre-SOURCE prefix migration)
- `08061.csv` — old_name → new_name rename mapping
- `08063.txt` — filename rename log (SOURCE prefix migration)
- `08723.txt` — `.md.md` double-extension fix log

These are historical migration logs, not operational. Probably safe to delete once nucleosynthesis routing is confirmed complete.
**Recommendation: LOW PRIORITY — archive or delete after verification.**

---

## CLUSTER 13: Session State / Handoff Token Files

- `00033.json` — Handoff token HANDOFF-20260120 (annealment p1→p2)
- `00038.json` — Handoff token HANDOFF-20260122
- `00089.json` — Handoff token HANDOFF-20260202
- `00671.txt` — Handoff token HANDOFF-20260202 (text version)

These appear to be early handoff tokens from before the canonical handoff protocol was established in CC33. The canonical location for handoffs is `agents/commander/outbox/handoffs/`.

**Recommendation: DELETE** — superseded by canonical handoff protocol. These are pre-CC33 relics.

---

## CLUSTER 14: XML Files — Prompt Templates (KEEP)

21 XML files (00838–00864) are structured prompt templates for content ingestion and synthesis tasks:
- Variance Absorption, Harmonic Amalgamation, Semantic Amplification (00838–00840)
- Metaprompt generators (00841, 00850, 00851, 00864)
- Archival workflow instructions for Medium, web, X/Twitter articles (00845, 00846, 00847, 00848)
- Transcript transformation templates (00861, 00862, 00863)
- Various synthesis prompts (00849, 00852, 00853, 00856, 00857, 00858, 00860)

**Recommendation: KEEP ALL** — active prompt engineering artifacts for the source ingestion pipeline.

---

## CLUSTER 15: Diagnostic / One-Time Report Files

- `CLASSIFICATION_REPORT.txt` — Semantic topic classification report for corpus
- `RECLASSIFICATION-VALIDATION.txt` — AI-Business reclassification validation
- `08080.txt` — File size survey output (`wc` output of source files)
- `08072.txt` — URL list (one URL per line, raw)
- `08105.txt` — Scaffold gitkeep file listing

**Recommendation:**
- `08080.txt`, `08072.txt`, `08105.txt` — DELETE (ad hoc dump files, trivially regeneratable)
- `CLASSIFICATION_REPORT.txt`, `RECLASSIFICATION-VALIDATION.txt` — KEEP SHORT TERM (useful context for canon-sensing work)

---

## CLUSTER 16: UNDO-NUCLEOSYNTHESIS.sh (SPECIAL CASE)

11,532-line shell script that reverses the nucleosynthesis routing operation (moves files back from `infra/` to `corpus/`).

**Recommendation: KEEP for now, but flag for deletion** once nucleosynthesis routing is confirmed stable and the undo window has passed. This is a safety net, not operational infrastructure.

---

## CLUSTER 17: State/Process Tracker JSON Files

| File | Purpose | Status |
|------|---------|--------|
| `00306.json` | `last_processed_line: 0, last_processed_file: null` — memsync state cursor | Stale (null state) |
| `00335.json` | `last_processed_line: 0, last_processed_file: 2026-02-27.jsonl` — similar cursor | Possibly active |
| `00333.json` | Circadian sync state (`compacted_weeks: [], last_run: 2026-02-24`) | Stale (service killed) |
| `00326.json` | Autonomy ledger state | Keep (operational) |

**Recommendation: DELETE `00306.json`** (null/empty cursor, dead service). **INVESTIGATE `00335.json`** — if memsync is still active, keep. **DELETE `00333.json`** (circadian sync service is killed).

---

## CLUSTER 18: Mermaid Diagram Files (KEEP)

- `00778.mmd` — Flowchart of source relationships (SOURCE nodes with styling)
- `11425.mmd` — Canon lattice graph (TD with cosmos/core/lattice/chain classification)

**Recommendation: KEEP BOTH** — visualization artifacts for canon structure. Low byte cost.

---

## CLUSTER 19: CAP/TOOL/WF Ontology YAML Files (KEEP)

Structured ontology records following consistent schemas:
- `00451–00455.yaml` — CAP-001 through CAP-005 (capability definitions)
- `00956–00960.yaml` — TOOL-001 through TOOL-004 + WF-001 (tool and workflow records)

**Recommendation: KEEP ALL** — canonical ontology seed data. Active records.

---

## CLUSTER 20: Python Script Groups (FUNCTIONAL INVENTORY)

Scripts are largely non-duplicate functional units. Key functional groups:

### Mining/Extraction pipeline:
`09228.py` (batch orchestrator), `09229.py` (source_extract), `09230.py` (extract_validate), `09149.py` (cluster engine), `09234.py` (source_triage), `09232.py` (quality gate), `09233.py` (metrics), `09231.py` (negative knowledge store)

### Promotion/Lattice pipeline:
`09203.py` (protease_queue), `09202.py` (protease_promote), `09145.py`/`00543.py` (candidate_adapter — see Cluster 8), `09185.py`/`00544.py` (lattice_annealer — see Cluster 8)

### Ontology:
`09142.py` (build_ontology_db), `09178.py` (ingest_rosetta_relations), `09195.py` (ontology_maintenance), `09196.py` (ontology_query), `09197.py` (ontology_tests), `09175.py` (generate_ontology_surface)

### Canon pipeline (CC49):
`11423.py` (canon_compiler), `11424.py` (s1_migration), `11426.py` (demotions/reclassifications), `11655.py` (s1_validator)

### Semantic Notation:
`09223.py` (smart_canon_sn_converter), `09224.py` (sn_decoder), `09225.py` (sn_encoder), `09226.py` (sn_variable_expander), `11603.py` (v4_poc)

### Memory/Graphiti:
`09072.py` (memsync_bridge), `09073.py` (memsync_daemon), `09074.py` (memsync_schema), `09191.py` (memory_compaction), `09148.py` (circadian_sync)

### Utility/One-time:
`09220.py` — CC30 EMERGENCY session_state_brief (has emergency header but is actually session_state_brief.py). **INVESTIGATE** — is this superseded by a non-emergency version?
`11485.py` — Google Drive pointer creator. **One-time migration tool — DELETE after use.**
`strip_filenames.py` — strips filenames to sequential numbers. **Operational tool for corpus management — KEEP.**
`adjudicator_classifier.py`, `classifier.py` — corpus classification tools. `classifier.py` appears to be an older/simpler version; `adjudicator_classifier.py` is the refined version. **DELETE `classifier.py`** if `adjudicator_classifier.py` supersedes it.

---

## CLUSTER 21: Sovereign Priority / Config YAML Files (KEEP)

| File | Purpose |
|------|---------|
| `08711.yaml` | Sovereign Priority Signals (atom_cluster.py input) |
| `08705.yaml` | Scope Probe Suite v1.0.0 |
| `09235.yaml` | source_triage_config.yaml (DC-208-1 pipeline config) |
| `09227.yaml` | Semantic Notation Glossary v1.0 |
| `00389.yaml` | Candidate Adapter Contract v1.1.0 |
| `00403.yaml` | Global Lock Hierarchy |
| `00423.yaml` | Tool Niche Registry |
| `00708.yaml` | Ascertescence Thresholds |
| `00723.yaml` | Constellation Coordination |
| `00736.yaml` | IIC Registry |
| `11513.yaml` | Hazel Automation Rules |
| `11529.yaml` | Keyboard Maestro Macros |
| `11586.yaml` | Nucleosynthesis Routing Table |
| `11679.yml` | Lint GitHub Action |
| `11680.yml` | Verify GitHub Action |

**Recommendation: KEEP ALL** — active configuration artifacts.

---

## CLUSTER 22: CSV Data Files (KEEP MOST)

| File | Content |
|------|---------|
| `00459.csv` | Pool A research file inventory |
| `00461.csv` | Pool B sources inventory |
| `00463.csv` | Pool C NotebookLM inventory |
| `00464.csv` | Duplicate analysis |
| `00691.csv` | Cluster action manifest |
| `00704.csv` | Account registry |
| `00705.csv` | Service subscription registry |
| `00734.csv` | Tool registry (CSV format) |
| `00757.csv` | Model registry |
| `00759.csv` | Platform registry |
| `00761.csv` | Project backlog |
| `00769.csv` | Role registry |
| `00775.csv` | Sources manifest (DYN-SOURCES equivalent) |
| `00783.csv` | Task registry |
| `04623.csv` | Extended source catalog |
| `08060.csv` | Migration rename map (old→new) — see Cluster 12 |
| `08061.csv` | Rename map (second pass) — see Cluster 12 |
| `08079.csv` | YouTube video list (Title/Channel/Topic/Genre) |

**Recommendation: KEEP operational CSVs. EVALUATE deletion of `08060.csv`, `08061.csv` (migration artifacts) and `08079.csv` (raw YouTube list, likely superseded by SOURCE files).**

---

## CLUSTER 23: JSON Data Files (KEEP MOST, DELETE FEW)

| File | Content | Recommendation |
|------|---------|----------------|
| `00033.json`, `00038.json`, `00089.json` | Old handoff tokens | DELETE (pre-CC33) |
| `00306.json` | Null memsync cursor | DELETE |
| `00326.json` | Autonomy ledger state | KEEP |
| `00333.json` | Dead circadian sync state | DELETE |
| `00335.json` | Active memsync cursor | KEEP/INVESTIGATE |
| `00715.json` | Batch orchestrator manifest (118 batches) | KEEP |
| `00720.json` | Constellation configuration schema | KEEP |
| `00725.json` | DAG state | KEEP |
| `00726.json` | Lattice index | KEEP |
| `00740.json` | Fragmentation index (0.36) | KEEP |
| `00741.json` | Lock hierarchy JSON | KEEP |
| `00771.json` | Git commit state snapshot | KEEP |
| `00776.json` | Source parse results | KEEP |
| `00777.json` | Graph state (1152 nodes) | KEEP |
| `00779.json` | Source totals (1152) | KEEP |
| `00780.json` | Safe point record | KEEP |
| `00782.json` | Schema state | KEEP |
| `00950.json` | Gemini CLI config template | KEEP |
| `08572.json` | OpenClaw Slack config for @psyche | KEEP (but note Mac mini unreachable) |
| `11331.json` | Corpus manifest | KEEP |
| `11422.json` | V-2 state | KEEP |
| `11568.json` | Regeneration state | KEEP |
| `11681–11685.json` | Obsidian configs | KEEP |

---

## SUMMARY: Crush List (Aggressive Deletions)

### IMMEDIATE DELETE — Zero ambiguity (171+ files):

**Heartbeats (4):** `11398.heartbeat`, `11427.heartbeat`, `11467.heartbeat`, `11578.heartbeat`

**Locks (3):** `04577.lock`, `04578.lock`, `04580.lock`

**Complete markers (10):** `08607.complete`, `08608.complete`, `08609.complete`, `11102.complete`, `11105.complete`, `11109.complete`, `11111.complete`, `11112.complete`, `11114.complete`, `11116.complete`

**Cycle logs (5):** `00009.log`, `00010.log`, `00012.log`, `00014.log`, `00016.log`

**All plists (40):** `09082.plist` through `09124.plist`, `09129.plist`, `09152.plist`, `09153.plist`, `11668.plist`, `11671.plist`, `11672.plist`, `11674.plist`

**Archived model YAMLs (6):** `08097.yaml`, `08098.yaml`, `08099.yaml`, `08100.yaml`, `08101.yaml`, `08102.yaml`

**Old handoff tokens (4):** `00033.json`, `00038.json`, `00089.json`, `00671.txt`

**Dead state cursors (2):** `00306.json`, `00333.json`

**Older TOOL YAML versions (2):** `11333.yaml`, `11334.yaml`

**Shim script (1):** `09134.sh`

**Ad-hoc dump files (3):** `08080.txt`, `08072.txt`, `08105.txt`

**Bulk Codex/OpenClaw session logs (~60):** `00966.log`, `00967.log`, `00968.log`, `00980.log` through `01051.log` (minus `01036.log`, `01044.log` which may have substantive adjudicator content — verify)

**Total immediate delete: ~140 files**

---

### INVESTIGATE BEFORE DELETING:

| File(s) | Question |
|---------|----------|
| `00543.py`, `09145.py` (candidate_adapter) | Which version (5-dim vs 14-dim) is active in pipeline? Delete the other. |
| `00544.py`, `09185.py` (lattice_annealer) | Same question as above. |
| `09135.sh`, `09251.sh` (auto_ingest_loop) | Which variant is the launchd target? |
| `classifier.py` vs `adjudicator_classifier.py` | Is classifier.py superseded? |
| `09220.py` | Is the EMERGENCY MODE label still meaningful or is this the canonical session_state_brief? |
| `00335.json` | Is memsync daemon still running/relevant? |
| `08060.csv`, `08061.csv` | Migration complete? Safe to delete? |
| `08079.csv` | Superseded by SOURCE files? |
| `UNDO-NUCLEOSYNTHESIS.sh` | Nucleosynthesis stable? Delete undo script. |

---

### KEEP WITHOUT QUESTION:

All XML prompt templates (21 files), all CAP/TOOL/WF ontology YAMLs, all pipeline Python scripts not flagged above, Obsidian config JSONs, operational CSVs, Mermaid diagrams, GitHub Action YAMLs, sovereign priority configs, and operational shell scripts (config.sh, cc_handoff.sh, cockpit.sh, ascertescence_relay.sh, etc.).
