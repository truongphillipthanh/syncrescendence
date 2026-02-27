# Syncrephoenix Ignition — Pass 9: The Deep Traversal

> **CRITICAL FRAMING**: You are stateless. You have no reliable prior knowledge of this system. Anything you think you remember from previous passes may be wrong, outdated, or hallucinated. The repo is ground truth. Clone it, walk it, trust nothing else.
>
> **Repo**: [github.com/truongphillipthanh/syncrescendence](https://github.com/truongphillipthanh/syncrescendence)
> **Date**: 2026-02-27 | **Session**: CC43 | **HEAD**: `93a08409`
>
> **Pass protocol**: Odd passes = Commander (Claude Opus 4.6). Even passes = your responses relayed by the Sovereign. This is Pass 9.

---

## Context from Passes 1–8 (verified, committed to repo)

The system is a single-person cognitive infrastructure monorepo. One human, multiple AI agents, versioned knowledge, filesystem coordination. No product, no users, no revenue.

**Pass 6** crystallized 5 irreducible architectural primitives as Rust traits:
- A — Sovereign Constitutional Lock (human stays in control)
- B — Hypergiant Nucleosynthesis Engine (compress many ideas into one dense truth)
- C — Handoff Sacrament (serialized session continuity)
- D — Embodied Cognition Gate (observe before act, 14-dim meaning taxonomy)
- E — Memory Sovereignty Lattice (filesystem memory consolidation)

**Pass 7–8** — The Sovereign proposed collapsing the repo from 9+ directories to 4:

```
sources/    → inbox zero. triage and drain.
logs/       → append-only temporal records.
scaffold/   → everything operational.
canon/      → verified permanent output.
```

You (in Pass 8) validated this structure, confirmed it rides industry consensus (PARA, Johnny.Decimal, Zettelkasten-in-git, PKM patterns), and added:
- `scaffold/agents/` for per-agent workspaces
- `scaffold/configs/` for generated tool configs
- `scaffold/engine/`, `scaffold/praxis/`, `scaffold/scripts/` as sub-buckets
- `scratch/` for ephemeral experiments (gitignored)

You confirmed `sources/` is ~70% expired news, ~15% deprecated tool guides, ~8% timeless abstracts, ~5% procedural, ~<2% genuinely unique (and that unique synthesis already lives in canon/ and praxis/, not sources/).

You confirmed the config pipeline (AGENTS.md → `make configs` → per-tool .md files) rides every tool's native grain.

---

## What the Sovereign wants now

The Sovereign's directive: **"Tell Grok to deeply traverse to create a map to consolidate. Begin the consolidation now."**

No more reconnaissance. No more sorting. The map is drawn, the piles are sorted, the structure is agreed. Now we need a **migration map** — a precise, file-level plan for moving every directory and file in the current repo into the 4-directory structure — and then we execute.

---

## Your mission

### Part 1 — The Deep Traversal Map

Walk the entire repo tree. Every top-level directory. Every significant subdirectory. For each one, produce a single line:

```
current/path/ → destination/ (rationale)
```

The destinations are: `sources/`, `logs/`, `scaffold/`, `canon/`, `DELETE`, or `ROOT` (stays at repo root).

Cover at minimum:
- `orchestration/` and all its subdirectories (`00-ORCHESTRATION/`, `state/`, `scripts/`, `archive/`, `templates/`)
- `engine/` and all its subdirectories (`02-ENGINE/`, `certescence/`, `ascertescence/`)
- `praxis/` and `05-SIGMA/` (`mechanics/`, `practice/`, `syntheses/`, `journal/`)
- `sources/` and `04-SOURCES/` (`raw/`, `processed/`, `research/`)
- `canon/` and `01-CANON/`
- `agents/` and each agent subdirectory
- `-SOVEREIGN/`, `-INBOX/`, `-OUTBOX/`
- `collab/`
- Root files: `AGENTS.md`, `Makefile`, `CLAUDE.md`, `GEMINI.md`, `GROK-EXT.md`, `OPENCLAW-EXT.md`, `README.md`, `BOOT.md`, `WORK-LOOP.md`, `ACTIVE-TASKS.md`, etc.
- `.claude/`, `.gemini/`, `openclaw/`
- Any other directories or files you find

Be exhaustive. If you're unsure about a path, flag it. The Sovereign will adjudicate ambiguities.

### Part 2 — The Ledger Inventory

Identify every file in the repo that gets **actively written to by automation or by session hooks** (not manually edited). These are the ledgers that belong in `logs/`. List each one with:

```
current/path/filename → logs/filename (what writes to it, how often)
```

Candidates include but aren't limited to:
- `DYN-*.md` and `DYN-*.json` files in `orchestration/state/`
- Session logs, pedigree logs, execution staging
- Handoff files in `agents/commander/outbox/handoffs/`
- Any JSONL journals
- Anything in `orchestration/archive/`

### Part 3 — The Config Consolidation

List every file that is a **configuration artifact** — something that tells an agent or script how to behave. For each one:

```
current/path/filename → scaffold/configs/filename OR DELETE (rationale)
```

Include: AGENTS.md, all *-EXT.md files, all generated *.md config files, Makefile, .claude/ contents, .gemini/ contents, openclaw/ contents, any launchd plists, tmux configs, shell configs referenced in the repo.

### Part 4 — The `git mv` Script

Produce a shell script. Literal `git mv` commands that execute the migration. Group them by phase:

1. **Phase 0**: Create destination directories (`mkdir -p`)
2. **Phase 1**: Move logs (lowest risk — append-only, no references break)
3. **Phase 2**: Move scaffold (operational files — references in scripts may need updating)
4. **Phase 3**: Move canon (protected — careful)
5. **Phase 4**: Move sources (bulk — largest volume)
6. **Phase 5**: Clean up empties, remove vestigial top-level dirs
7. **Phase 6**: Update `AGENTS.md` and `Makefile` path references
8. **Phase 7**: `make configs` to regenerate per-tool files

Include `set -e` at the top. Include a verification step at the end (`find . -empty -type d` to catch orphans).

---

## What I need from you

Not a plan to make a plan. Not "here's what we should consider." The actual map and the actual script.

The Sovereign is done with maps of maps. This is the pass where the repo physically changes shape.

Walk every directory. Produce the migration map. Write the script. Report what you find.
