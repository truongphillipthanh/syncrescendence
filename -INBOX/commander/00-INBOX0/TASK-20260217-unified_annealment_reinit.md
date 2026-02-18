# TASK: Unified Corpus Annealment v2 — Reinit Handoff

**Status**: PENDING
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-17
**Authority**: Sovereign directive (Session 20)

---

## I. MISSION

- **What**: Full-spectrum ontological synthesis across ~616K tokens of corpus material
- **Why**: ARCH-ONTOLOGY_ANNEALMENT_v1.md (605 lines, committed at 6eb4653) was produced under context duress by a session that blew out 3 times. It's architecturally sound but was synthesized from incomplete ingestion — the clarescence corpus (65 files), CANON (79 files), and convergence docs were never fully read.
- **Deliverable**: `00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md`
- **Source directive**: "Take everything learned from annealment passes, merge with everything from every clarescence, identify all canonical concepts in the scaffold, triangulate with the exocortex, reaffirm the ontology reconception from the metacharacterization + convergence docs. New unified annealment of everything."

---

## II. KAIZEN AUDIT — MISTAKES FROM SESSION 20

Brutally honest. Numbered. Root cause for each. DO NOT REPEAT THESE.

1. **Wrong working directory** — ran bash commands from `/Users/home` instead of `/Users/home/Desktop/syncrescendence`. Wasted a turn, Sovereign had to correct.
   - **RC**: Assumed `cd` persisted after initial command. It doesn't across Bash tool calls unless using absolute paths.
   - **FIX**: ALWAYS use absolute paths from `/Users/home/Desktop/syncrescendence/`.

2. **Read 29K-token convergence doc directly into Opus context** — the `syncrescendence_convergence.md` file exceeded the 25K token Read limit and errored.
   - **RC**: Read the file BEFORE measuring it. Measured sizes AFTER the failed read.
   - **FIX**: ALWAYS `wc -l` before Read. Anything >500 lines gets delegated to a Sonnet agent.

3. **Launched 5 execution agents before Sovereign finished briefing** — Sovereign said "I was going to tell you we have a new secret weapon" (Sonnet 4.6 1M context) but Commander had already dispatched 5 agents.
   - **RC**: Misapplied "execute first" policy. Sovereign was mid-sentence, still providing context. "Execute first" means don't ask for permission on things you can do — it does NOT mean interrupt the briefing.
   - **FIX**: When Sovereign is actively providing context, LISTEN. Execute after the brief, not during it.

4. **Read the entire 605-line v1 directly into Opus context** — burned ~2.5K tokens holding a document that a Sonnet summarizer could have digested.
   - **RC**: Opus instinct to "understand everything directly." Wrong for a 600-line doc when the role is orchestrator.
   - **FIX**: For documents >200 lines, dispatch a Sonnet summarizer. Opus reads only the summary.

5. **Loaded both metacharacterization CLAUDE.md files into system context (~40K+ tokens)** — reading files from `-INBOX/commander/new_ontology_metacharacterization/` and `_2/` triggered auto-load of their CLAUDE.md files into the system prompt.
   - **RC**: Did not know that reading ANY file in a directory with a CLAUDE.md auto-loads it. This is the single biggest context budget violation — 40K+ tokens of Palantir analysis loaded permanently into system context.
   - **FIX**: NEVER read files from directories that contain CLAUDE.md files. Instead, dispatch a Sonnet agent to read those files and return a summary. If you MUST read from such directories, read specific non-CLAUDE.md files by exact path.

6. **Asked "what's your directive" when Sovereign had already stated the task** — passive mode, asking instead of doing.
   - **RC**: Defaulted to question-asking when the context was sufficient to act.
   - **FIX**: If the Sovereign has stated a task, BUILD THE STRATEGY. Don't ask for restatement.

7. **Presented measurement tables and asked questions instead of building strategy** — showed file sizes, asked "what do you want me to do?" multiple times.
   - **RC**: Elaboration over execution anti-pattern. Measuring is useful but is NOT the deliverable.
   - **FIX**: Measure (1 turn) → Strategy (1 turn) → Execute. Never more than 1 turn of measurement.

8. **Tried to exit plan mode prematurely** — attempted ExitPlanMode before incorporating Sovereign's feedback about session handoff.
   - **RC**: Rushing to completion. Sovereign rejected with "comprehensively, meticulously, rigorously culminate into a handoff reinit."
   - **FIX**: In plan mode, incorporate ALL Sovereign feedback before exiting. Don't rush.

---

## III. ARCHITECTURAL PRINCIPLES (LEARNED THE HARD WAY)

### Token Architecture
- **Opus = orchestrator**. NEVER reads raw corpus. Reads ONLY digests and final outputs.
- **Sonnet 4.6 = workhorse** (1M context window). Can swallow entire directories without blowing up.
- **Progressive summarization pipeline**: Raw corpus (616K) → Domain digests (~10K) → Convergence synthesis (~3K) → Opus reads synthesis only.
- **Opus token budget**: <10K tokens of content reads per session. Everything else is delegation.

### Measurement Protocol
- ALWAYS `wc -l` BEFORE reading ANY file.
- Decision tree: <200 lines → Opus can read. 200-500 lines → consider delegating. >500 lines → MUST delegate to Sonnet.
- ALWAYS use absolute paths from `/Users/home/Desktop/syncrescendence/`.

### Agent Dispatch Protocol
- **model="sonnet"** in Task tool for Sonnet 4.6 agents.
- **run_in_background=true** for heavy ingestion work.
- **subagent_type="general-purpose"** for agents that need to read + write files.
- Check output_file or use `ls` on target paths to verify completion.
- If any digest is <100 lines, it likely truncated — re-dispatch with tighter scope.

### CLAUDE.md Trap
- Reading ANY file in a directory that contains a CLAUDE.md causes the CLAUDE.md to auto-load into system context.
- The metacharacterization directories each have massive CLAUDE.md files (~20K+ tokens each).
- NEVER read from those directories directly. Always dispatch to agents.

### Team/Swarm Capability
- **TeamCreate**: creates a team with shared task list, coordinated agents.
- **Task tool with team_name**: spawns agents that join the team.
- Use for coordinated multi-phase work (e.g., Phase 1 digests → Phase 2 synthesis).
- For one-shot parallel reads, regular Task tool (no team) is sufficient.

---

## IV. CURRENT STATE

### Background Agents (dispatched this session)
5 Sonnet agents were dispatched to produce domain digests. They may or may not have completed:

| Agent | Target Output | Status |
|-------|--------------|--------|
| canon-indexer | `.scratch/ANNEAL-DIGEST-CANON.md` | **FAILED** — "Prompt is too long" (264K tokens exceeded agent capacity). Must split into 3-4 sub-agents by file range (e.g., CANON-00xxx, CANON-10xxx, CANON-20xxx, CANON-30xxx). |
| clarescence-indexer | `.scratch/ANNEAL-DIGEST-CLARESCENCE.md` | CHECK |
| scaffold-indexer | `.scratch/ANNEAL-DIGEST-SCAFFOLD.md` | CHECK |
| metachar-convergence-indexer | `.scratch/ANNEAL-DIGEST-METACHAR.md` | CHECK |
| v1-gap-analyzer | `.scratch/ANNEAL-DIGEST-GAPS.md` | CHECK |

**First action**: `ls -la /Users/home/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/.scratch/ANNEAL-DIGEST-*.md && wc -l` those files. Note which are present and their sizes.

### Existing Artifacts
- `00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v1.md` — 605 lines, committed at 6eb4653. Keep as historical.
- `00-ORCHESTRATION/state/impl/.scratch/` — digest output directory (may need `mkdir -p`).

### Working Tree
- Committed at f27ca2b (Session 20 handoff).
- **WARNING**: Convergence docs were git-deleted by Ajna sync but still exist on disk:
  - `/Users/home/Desktop/syncrescendence/-INBOX/commander/syncrescendence_convergence.md` (142K)
  - `/Users/home/Desktop/syncrescendence/-INBOX/commander/syncrescendent_convergence_aligned.md` (98K)
  - They are physically present. If git shows them deleted, recover with `git checkout HEAD~1 -- <path>` or just read from disk.
- Many CONFIRM/RESULT files were moved back from 40-DONE to 00-INBOX0 by Ajna sync (inbox churn — not critical, process or ignore).

### Constellation Health
- All 4 agents HEALTHY as of session start (2026-02-17 19:32).
- Neural Bridge (MBA ↔ Mac mini) UP.
- MBA syncing every 5 minutes (Ajna commits).

---

## V. EXECUTION PLAN

### Step 0: Verify Phase 1 Digests
```bash
ls -la /Users/home/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/.scratch/ANNEAL-DIGEST-*.md
wc -l /Users/home/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/.scratch/ANNEAL-DIGEST-*.md
```

**KNOWN FAILURE**: canon-indexer failed — "Prompt is too long." 264K tokens exceeded Sonnet agent capacity. CANON must be split into 3-4 sub-agents. Use `ls 01-CANON/*.md | wc -l` to count files, then split alphabetically or by CANON-ID range. Each sub-agent produces a partial digest, then a merge agent combines them.

**Decision tree**:
- All 5 present AND each >100 lines → proceed to Step 1
- Some missing or <100 lines → re-dispatch those specific domains:
  - For CANON: agent reads `01-CANON/*.md`, extracts concepts/primitives/identity
  - For CLARESCENCE: agent reads `00-ORCHESTRATION/state/impl/clarescence/*.md`, extracts decisions/terms
  - For SCAFFOLD: agent reads `00-ORCHESTRATION/state/*.md` + `02-ENGINE/*.md` + `05-SIGMA/**/*.md`
  - For METACHAR: agent reads both metacharacterization dirs + convergence docs (WARN: CLAUDE.md trap — use specific file paths, not directory reads)
  - For GAPS: agent reads v1 + memory + intentions + IMPL map
- All 5 missing → full re-dispatch needed (previous agents may have all failed)

### Step 1: Launch Phase 2 Convergence Agent

Launch a SINGLE Sonnet 4.6 agent (model="sonnet") that:

1. Reads all 5 digest files from `.scratch/`
2. Reads `ARCH-ONTOLOGY_ANNEALMENT_v1.md` as structural scaffold
3. Reads convergence docs directly (they're ~5K lines total, well within 1M context):
   - `/Users/home/Desktop/syncrescendence/-INBOX/commander/syncrescendence_convergence.md`
   - `/Users/home/Desktop/syncrescendence/-INBOX/commander/syncrescendent_convergence_aligned.md`
4. Reads key model responses (by specific file path, NOT via directory read):
   - `/Users/home/Desktop/syncrescendence/-INBOX/commander/new_ontology_metacharacterization/claude.md`
   - `/Users/home/Desktop/syncrescendence/-INBOX/commander/new_ontology_metacharacterization/chatgpt.md`
   - `/Users/home/Desktop/syncrescendence/-INBOX/commander/new_ontology_metacharacterization_2/claude.md`
   - `/Users/home/Desktop/syncrescendence/-INBOX/commander/new_ontology_metacharacterization_2/chatgpt.md`
5. Cross-references ALL material
6. Writes `00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md`

**Prompt for the convergence agent must specify**:
- Cross-reference all 5 digests against each other
- Cite specific source files for every claim
- Exhaustive concept inventory (superset of v1's Section III)
- Identify contradictions between domains
- Preserve v1's strongest sections (Palantir synthesis, substrate architecture)
- Deepen: clarescence decisions, CANON ontological primitives, scaffold living state
- Target: 600-1000 lines

### Step 2: Opus Verification (LIGHTWEIGHT)

Read ONLY the v2 output file (~600-1000 lines). This is the ONE large read Opus makes.

Spot-checks (3-5 targeted reads, 50-100 lines each):
- Pick 2 random clarescence file names from the digest → grep for those decisions in v2
- Pick 2 random CANON concepts from the digest → verify they appear in v2's concept inventory
- Verify all 6 domains have dedicated coverage in v2

### Step 3: Commit + State Update

```bash
git add 00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
git add 00-ORCHESTRATION/state/impl/.scratch/ANNEAL-DIGEST-*.md
git commit -m "arch(ontology): unified annealment v2 — full corpus synthesis

Produced via progressive summarization: 616K tokens → 5 domain digests → 1 convergence synthesis.
Sources: 79 CANON files, 65 clarescences, full scaffold state, 8 model responses, 2 convergence docs.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

Update:
- `DYN-DEFERRED_COMMITMENTS.md`: DC-004 (Rosetta terms) and DC-012 (doc formalization) progress
- `DYN-EXECUTION_STAGING.md`: execution log entry

---

## VI. CORPUS INDEX

| Domain | Path | Files | Lines | ~Tokens |
|--------|------|-------|-------|---------|
| CANON | `01-CANON/*.md` | 79 | 66,031 | ~264K |
| ENGINE | `02-ENGINE/*.md` | many | 20,182 | ~80K |
| SIGMA | `05-SIGMA/**/*.md` | many | 4,500 | ~18K |
| Clarescence | `00-ORCHESTRATION/state/impl/clarescence/*.md` | 65 | 21,207 | ~85K |
| Scaffold state | `00-ORCHESTRATION/state/*.md` | many | 34,569 | ~138K |
| Metachar set 1 | `-INBOX/commander/new_ontology_metacharacterization/*.md` | 5 | 1,052 | ~4K |
| Metachar set 2 | `-INBOX/commander/new_ontology_metacharacterization_2/*.md` | 5 | 1,004 | ~4K |
| Convergence | `-INBOX/commander/syncrescen{dence,dent}_convergence{,_aligned}.md` | 2 | 4,955 | ~20K |
| Memory | `~/.claude/projects/-Users-home/memory/*.md` | many | 826 | ~3K |
| **TOTAL** | | | **~154K lines** | **~616K tokens** |

Key individual files:
- `ARCH-INTENTION_COMPASS.md`: 490 lines (intention vectors)
- `IMPLEMENTATION-MAP.md`: 2,294 lines (T2 tracking, 197 IMPL entries)
- `DYN-BACKLOG.md`: 183 lines (project state)
- `DYN-DEFERRED_COMMITMENTS.md`: 84 lines (unfulfilled promises)
- `ARCH-ONTOLOGY_ANNEALMENT_v1.md`: 605 lines (existing synthesis, committed)

---

## VII. ANTI-PATTERNS (SEARED — DO NOT REPEAT)

1. **DO NOT** read raw corpus files (>200 lines) into Opus context — delegate to Sonnet
2. **DO NOT** launch execution agents before the plan is Sovereign-approved
3. **DO NOT** ask "what's your directive" when the Sovereign has already stated the task
4. **DO NOT** read from directories containing CLAUDE.md files (auto-loads ~20K+ tokens into system context)
5. **DO NOT** present measurement tables as a substitute for strategy — measure once, then build
6. **DO NOT** use relative paths — always absolute from `/Users/home/Desktop/syncrescendence/`
7. **DO NOT** try to hold >10K tokens of content reads in a single Opus session
8. **DO NOT** launch N parallel agents that each try to read the full corpus — divide domains first
9. **DO NOT** assume a single Sonnet agent can handle >200K tokens of file reads — CANON at 264K tokens blew out with "Prompt is too long." Split any domain >150K tokens into 2-4 sub-agents by file range.
9. **DO NOT** rush ExitPlanMode before incorporating all Sovereign feedback
10. **DO NOT** confuse "execute first" (do things you can do) with "interrupt the briefing" (don't listen)

---

## VIII. SECRET WEAPON — SONNET 4.6 + SWARM

### Sonnet 4.6
- **1M context window** — can hold the ENTIRE 616K token corpus in a single agent
- Use `model="sonnet"` in Task tool parameter
- Cost-effective for heavy reading/summarization work
- Launch via: `Task(subagent_type="general-purpose", model="sonnet", run_in_background=true, ...)`

### Agent Teams (Swarm)
- `TeamCreate(team_name="annealment-team")` — creates team with shared task list
- `Task(team_name="annealment-team", name="agent-name", ...)` — spawns agent in team
- `TaskCreate/TaskList/TaskUpdate` — coordinate work via shared task list
- `SendMessage` — inter-agent communication
- Use for multi-phase coordinated work (Phase 1 → Phase 2 handoff)
- For simple parallel reads, regular Task tool (no team) is sufficient

### When to Use What
- **Single Sonnet agent**: one domain to read, one output to produce
- **Parallel Task agents (no team)**: independent reads that don't depend on each other
- **Team/swarm**: phases where later agents depend on earlier agents' output
- **Opus direct**: orchestration, verification, commits — NEVER raw corpus reading

---

## IX. WHAT V1 GOT RIGHT (preserve in v2)

- Section I (Palantir Reveal): 4-model convergence, 3-layer architecture (semantic/kinetic/dynamic)
- Section VI (Formal Ontology Reconception): Object types, link types, action types — solid taxonomy
- Section VII (Substrate Architecture): Layer 0-3 stack model with organ mapping
- Section IX (Universal Convergence): 10 points all models agreed on
- The "test": if deleting an app deletes your semantics, you have a workspace, not an ontology

## X. WHAT V1 MISSED (deepen in v2)

- Clarescence decisions: 65 files of decisions/terms NEVER read. V1 claims "CLARESCE^3" as source but only references the meta-level, not individual decisions.
- CANON content: 79 files of canonical knowledge NEVER traversed. V1's concept inventory draws from scaffold, not from actual CANON reads.
- Convergence docs: 5K lines only partially processed due to context blowout.
- Scaffold living state: accurate inventory of what's running vs. what's aspirational — v1 lists concepts but doesn't audit liveness.
- Exocortex deep mapping: v1 has the table but doesn't cross-reference actual API/MCP states.
- Annealment protocol execution: v1 DESCRIBES the 9-step protocol but doesn't EXECUTE any step. V2 should at minimum execute steps 1-3 (ground truth, redundancy, terminology).

---

*Produced by Commander (Opus 4.6) — Session 20 handoff, 2026-02-17*
*Next session: read this file, verify digests, execute the plan. Stay under 10K tokens.*
