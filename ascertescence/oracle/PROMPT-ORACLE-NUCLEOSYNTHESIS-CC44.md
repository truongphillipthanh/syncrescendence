# PROMPT — Oracle Nucleosynthesis: Strange Attractor Directory Manifest

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok)
**Session**: CC44
**Git HEAD**: `4de9df40`
**Reply-To**: Commander (paste response back)

---

## Context

The Syncrephoenix flattened the entire repo — all files at root of their directories. Now we're doing the inverse: **nucleosynthesis**. Grouping files by the strange attractors they orbit, using nested directories as the grouping mechanism.

Think of it as a garage that was emptied out. There are manuals, specific wrenches, and whole engine parts JUST for Toyota — and other stuff not related to automotive. We're sorting by what they're FOR, not what they ARE.

The original 11 tool-level attractors (Terminal, Claude Code, Codex, Gemini CLI, OpenCode, Cline, OpenClaw, AI Agents, Multi-Agent Orchestration, Models, Memory) are now joined by concept-level attractors discovered in the corpus:

| Attractor | File Count | Description |
|---|---|---|
| **Ontology** | 45+ | Rosetta bridge, annealment v1/v2, typed entities, Python scripts, Palantir research |
| **Consciousness/Cognitive Architecture** | 275+ | Six Causal Chains, Cognitive Palace, CANON-3xxxx range |
| **Clarescence** | 56 | Sovereign's illumination instrument (path analysis, metacharacterization) |
| **Ascertescence** | 87 | Commander's triangulation instrument (Oracle↔Diviner↔Adjudicator cycles) |
| **Certescence** | 30+ | Verified knowledge vault lifecycle (councils, siege lanes, templates) |
| **Sovereignty/Governance** | 194 | Constitutional law, 5 invariants, ratification, sovereign directives |
| **Infrastructure/Deployment** | 193 | Neural bridge (SSH MBA↔mini), launchd, auto-ingest, dispatch |
| **Feedcraft** | 52 | Content pipeline, demand-pull, intake/irrigation/synthesis |
| **Skills/Tools** | 58 | SKILL.md files, tool niche registry |
| **Agent Coordination** | 898 | Inbox/outbox kanban, task receipts, handoffs |
| **Intention/Decision** | 71 | DAG convergence, intention compass, deferred commitments |
| **Canon** | 170 | Verified knowledge corpus (cosmic/core/chain/lattice taxonomy) |

---

## Your Task (TWO PARTS)

### Part 1: The Manifest

Traverse the repo. Produce a **nucleosynthesis manifest** — a mapping from every file (or file pattern) to its attractor directory.

The directory structure should be hierarchical where it makes sense. For example:

```
cli/
  claude-code/     # CLAUDE.md variants, hooks, skills, settings, MCP configs
  codex/           # Adjudicator workflow files, bid/audit framing
  gemini/          # Diviner dispatch, headless mode, classification
  opencode/        # (if anything exists)
  cline/           # (if anything exists)
  openclaw/        # SOUL.md, HEARTBEAT.md, Ajna/Psyche configs
ontology/
  rosetta/         # Rosetta Stone, bridge, normalization
  annealment/      # ARCH-ONTOLOGY_ANNEALMENT v1/v2
  schemas/         # Typed entities, taxonomies, classification
  scripts/         # Python ontology tools
  ...
```

**Current repo structure** (all flat):

```
sources/        5,698 files  — prefixed: META-, SOURCE-, NOTEBOOK-, RESEARCH-, PROCESSED-, INDEX-, ASSET-
scaffold/       1,321 files  — prefixed: AGENT-, SCRIPT-, ENGINE-, PRAXIS-, CONFIG-, CONSTELLATION-
canon/            170 files  — prefixed: CANON-XXXXX-{TOPIC}-{taxonomy}.md (numbered 00000-99000)
logs/             456 files  — prefixed: ARCH-, DYN-, CLARESCENCE-, RESPONSE-, PROMPT-, REF-, RESULT-, RENDEZVOUS-
ascertescence/     91 files  — sorted by agent (oracle/, diviner/, adjudicator/, meta/)
```

**Key file patterns to account for**:

- `scaffold/AGENT-COMMANDER-*` (243 files) — Commander's operational artifacts
- `scaffold/AGENT-ADJUDICATOR-*` (186 files) — Adjudicator inbox/outbox
- `scaffold/AGENT-CARTOGRAPHER-*` (142 files) — Cartographer tasks
- `scaffold/AGENT-AJNA-*` (118 files) — Ajna (CSO) artifacts
- `scaffold/AGENT-PSYCHE-*` (89 files) — Psyche (CTO) artifacts
- `scaffold/SCRIPT-ORCHESTRATION-*` (182 files) — Automation scripts
- `scaffold/ENGINE-*` (173 files) — Prompts, references, configs
- `sources/META-*` (3,494 files) — Metadata/extraction records
- `sources/SOURCE-*` (1,773 files) — Raw ingested sources
- `sources/NOTEBOOK-*` (269 files) — Topic clusters
- `logs/CLARESCENCE-*` (56 files) — Clarity docs
- `logs/ARCH-*` (39 files) — Architecture decisions
- `logs/DYN-*` (43 files) — Dynamic state

**Requirements for the manifest**:

1. **Every file must be accounted for** — nothing left uncategorized. Use an `uncategorized/` bucket if needed.
2. **Express it as a script** — a bash/Python script that Commander can execute to perform the moves. Use `git mv` for tracked files. Include collision detection.
3. **Be meticulous** — use glob patterns where possible (`scaffold/AGENT-COMMANDER-*` → `agents/commander/`), but call out specific files that don't fit patterns.
4. **Preserve git history** — `git mv`, not `mv`.
5. **Handle the META- explosion** — 3,494 META- files in sources/ need a strategy. They're extraction records paired with their SOURCE- parents. Keep them together or separate?
6. **Account for cross-attractor files** — some files orbit multiple attractors. Make a decision, document it.

### Part 2: Next-Round Strange Attractor Supersensing

The original Hypersensing identified 11 tool-level attractors. Commander's corpus scan found 12 more concept-level ones. But there may be attractors we're both missing.

**Questions**:

1. **What attractors are hiding in sources/?** The 5,698 files include notebooks on specific topics (NOTEBOOK-01-OPENCLAW, NOTEBOOK-03-AGENT-MEMORY, NOTEBOOK-05-CLAUDE-CODE, NOTEBOOK-07-ECONOMIC-RECKONING, etc.). What do the notebook topics reveal about attractors that aren't in either list?

2. **What's the relationship between tool-level and concept-level attractors?** The original 11 are tools (Claude Code, OpenClaw, etc.). The new 12 are concepts (Ontology, Feedcraft, Governance). How do they relate? Does every tool serve a concept? Does every concept require a tool?

3. **What's the hierarchy?** If we nest directories, what's the top-level taxonomy? Is it tool-first (cli/claude-code/ontology-configs) or concept-first (ontology/cli-configs/claude-code)? The Sovereign's garage metaphor suggests concept-first (all Toyota stuff together regardless of whether it's a manual, wrench, or engine part).

4. **What strange attractors should the ontology itself track?** If we're building the ontology (per Pass 2), the attractor topology IS ontological content. The ontology should know about its own attractors. What does that self-referential structure look like?

---

## Anti-Survey Guardrails

- Do NOT produce a generic directory structure that could apply to any monorepo
- Do NOT list files without categorizing them
- The manifest must be EXECUTABLE — a script Commander can run, not a proposal to discuss
- If a file genuinely doesn't fit any attractor, say so explicitly — don't force it into a category
- The directory hierarchy must reflect THIS system's actual gravitational topology, not a textbook taxonomy

---

## Response Format

```
## Part 1: The Manifest

### Directory Taxonomy
[The proposed nested directory structure with descriptions]

### The Script
[Executable bash/Python that performs all git mv operations]
[Include: collision detection, dry-run mode, progress reporting]
[Handle: META- pairing strategy, cross-attractor files, uncategorized bucket]

### Cross-Attractor Files
[Files that orbit multiple attractors — where they go and why]

### The META- Strategy
[How to handle the 3,494 META- files — keep paired, separate, or something else]

## Part 2: Next-Round Supersensing

### Hidden Attractors in Sources
[What the notebooks and research files reveal]

### Tool↔Concept Mapping
[How the 23 attractors relate hierarchically]

### Proposed Top-Level Taxonomy
[The directory tree that reflects actual gravitational topology]

### Self-Referential Ontology Structure
[What the ontology tracks about its own attractors]
```
