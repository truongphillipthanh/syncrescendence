# PROMPT — Oracle Nucleosynthesis Pass 2: Higher Fidelity Manifest

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok)
**Session**: CC44
**Git HEAD**: `8e88c69d`
**Reply-To**: Commander (paste response back)

---

## What Pass 1 Got Right

- Concept-first hierarchy (Sovereign's garage metaphor) — correct
- Max depth 3 — correct
- 3 hidden attractors (Verticalization, Expression, Field) mapping to Phases 8/9/10 — good
- Self-referential ontology structure — good
- META-/SOURCE- pairing strategy — directionally right

## What Pass 1 Got Wrong

The directory taxonomy is sound. The **script is not executable**. Here are the specific errors Commander found when validating against the actual corpus:

### Error 1: ENGINE- files are not all ontology
`scaffold/ENGINE-*` (173 files) breaks down as:
- `ENGINE-REF-*` (35) — references for many attractors (Audizer, Fleet, Rosetta, Stack Teleology, etc.)
- `ENGINE-PROMPT-*` (35) — prompts for Oracle, Diviner, Adjudicator, not ontology
- `ENGINE-FUNC-*` (28) — functions/code for many subsystems
- `ENGINE-DYN-*` (20) — dynamic state files
- `ENGINE-CERTESCENCE-*` (15) — certescence vault (councils, templates, siege)
- `ENGINE-AVATAR-*` (8) — agent avatar/identity files
- `ENGINE-QUEUE-*` (7) — processing queues
- `ENGINE-IIC-*` (6) — Integration/coherence configs
- Others: CAP (5), TOOL (4), TEMPLATE (3), PROTO (2), SURVEY (2), WF (1), MODEL (1)

Routing all 173 to `ontology/scripts/` is wrong. Each subtype serves a different attractor.

### Error 2: ARCH- files are not all ontology
`logs/ARCH-*` (39 files) include memory architecture, skill registry, lock hierarchy, design decisions, tool niche registry — only ~4 are ontology-related (ARCH-ONTOLOGY_ANNEALMENT v1/v2, ARCH-ROSETTA_ONTOLOGY_BRIDGE, ARCH-ROSETTA_NORMALIZATION_AUDIT).

### Error 3: SCRIPT-ORCHESTRATION- files are not all agent coordination
`scaffold/SCRIPT-ORCHESTRATION-*` (176 files) include ontology tools (build_ontology_db.py, ontology_maintain.py), pipeline tools (protease_promote.py, atom_cluster.py), session management (session_state_brief.py), launchd plists, and more. They serve many attractors.

### Error 4: `scaffold/*CLAUDE*` glob doesn't match
Files are prefixed `AGENT-COMMANDER-*`, not `*CLAUDE*`. Same for `*CODEX*`, `*GEMINI*`, `*OPENCLAW*`. The glob patterns need to match actual prefixes or search file CONTENT for tool references.

### Error 5: Missing prefix groups entirely
**Scaffold** (not handled): PRAXIS- (34), CONFIG- (5), CONSTELLATION- (7), COLLAB- (11), TEMPLATE- (2), plus singletons (PORTAL, FLEET, DEPLOYMENT, CONTINUOUS, BOOT.md, OPENCLAW, INTER, WORK)

**Sources** (not handled): PROCESSED- (42), INDEX- (8), ASSET- (6), REF- (3), plus singletons (TRANSCRIPT_RECONCILIATION.md, FRONTMATTER_TEMPLATE.md, DYN, index.md, README.md)

**Logs** (not handled): RESPONSE- (50), PROMPT- (25), REF- (23), RESULT- (21), RENDEZVOUS- (11), CLARESCE- (11), ANNEAL- (9), DEC- (8), QUEUE- (7), GATE- (7), DISPATCH- (7), VERIFY- (6), RUNLOGS- (6), RESEARCH- (6), MODEL- (6), SOVEREIGN- (5), PRAC- (5), plus others

### Error 6: Existing directories not handled
The repo currently has these top-level dirs that would conflict: `engine/`, `orchestration/`, `memory/`. The script doesn't account for merging or renaming these.

### Error 7: Notebook topic coverage
14 distinct notebook topics exist. The case statement handles ~3. Here are all of them:
```
AGENT-MEMORY-SYSTEMS
AGENT-SECURITY-HARDENING
AGENTIC-NOTETAKING-KNOWLEDGE-VAULTS
AI-ENGINEERING-ROADMAPS-ARCHITECTURE
CLAUDE-CODE-COWORK-POWER-PATTERNS
DESIGN-IN-AI-ERA
ECONOMIC-RECKONING-SAAS-LABOR-SOCIETY
HOMELAB-INFRASTRUCTURE
MULTI-AGENT-ORCHESTRATION-SWARMS
OPENCLAW-ARCHITECTURE-SETUP
OPENCLAW-DEEP-RESEARCH-CONSTELLATION (6 prompt + 5 response files)
PHILOSOPHICAL-WILDCARDS-CULTURAL-COMMENTARY
PROMPT-ENGINEERING-SKILLS-CRAFT
VIBE-CODING-SOFTWARE-ABUNDANCE
```

Each needs an explicit attractor mapping.

---

## What We Need From Pass 2

### 1. Complete prefix→attractor routing table

For EVERY prefix in EVERY directory, specify which attractor directory it routes to. Format:

```
scaffold/AGENT-COMMANDER-*         → agents/commander/
scaffold/AGENT-ADJUDICATOR-*      → agents/adjudicator/
scaffold/ENGINE-REF-*              → {attractor based on content — specify each}
scaffold/ENGINE-PROMPT-ORACLE-*    → ascertescence/oracle/
scaffold/ENGINE-PROMPT-DIVINER-*   → ascertescence/diviner/
scaffold/ENGINE-CERTESCENCE-*      → certescence/
scaffold/SCRIPT-ORCHESTRATION-ontology_* → ontology/scripts/
scaffold/SCRIPT-ORCHESTRATION-protease_* → feedcraft/scripts/
...
logs/ARCH-ONTOLOGY_*               → ontology/annealment/
logs/ARCH-MEMORY_*                 → memory/
logs/ARCH-SKILL_*                  → skills/
logs/ARCH-LOCK_*                   → infrastructure/
logs/RESPONSE-ORACLE-*             → ascertescence/oracle/
logs/RESPONSE-DIVINER-*            → ascertescence/diviner/
logs/RESPONSE-ADJUDICATOR-*        → ascertescence/adjudicator/
...
```

Be exhaustive. Every prefix group accounted for.

### 2. Notebook topic→attractor mapping

For each of the 14 notebook topics, which attractor do they orbit?

### 3. ENGINE- subtype routing

For each ENGINE- subtype (REF, PROMPT, FUNC, DYN, CERTESCENCE, AVATAR, QUEUE, IIC, CAP, TOOL, TEMPLATE, PROTO, SURVEY, WF, MODEL), where does it go? Some will need per-file routing (e.g., ENGINE-REF-AUDIZER goes to skills/, ENGINE-REF-ROSETTA goes to ontology/).

### 4. The SOURCE-/META- pairing mechanism

Pass 1 used numeric ID extraction. What's the actual pairing pattern? Show 5 real examples of SOURCE- → META- pairs from the corpus to validate the mechanism.

### 5. Conflict resolution for existing directories

`engine/`, `orchestration/`, `memory/` already exist. What happens to their contents? Merge into new taxonomy? Rename first?

### 6. Updated executable script

Incorporating all corrections above. Must handle every file in the repo. The script should be Python (not bash) — the prefix routing logic needs data structures, not case statements.

---

## Anti-Glaze Guardrails

- If a prefix group has <10 files and you're unsure where it goes, say "UNCATEGORIZED — needs manual review" rather than guessing
- The routing table must be COMPLETE — if Commander runs the script and finds orphaned files, the manifest failed
- Test your logic against the actual prefix counts given above — they must sum correctly

---

## Response Format

```
## Prefix→Attractor Routing Table
[Complete table for scaffold/, sources/, logs/, canon/]

## Notebook Topic Mapping
[14 topics → attractors]

## ENGINE- Subtype Routing
[Per-subtype, with specific file callouts where needed]

## SOURCE-/META- Pairing Examples
[5 real pairs from corpus]

## Existing Directory Resolution
[engine/, orchestration/, memory/ handling]

## The Script (Python)
[Complete, executable, handles every file]
```
