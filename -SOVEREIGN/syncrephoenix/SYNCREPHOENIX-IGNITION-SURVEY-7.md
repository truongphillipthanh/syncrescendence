# Syncrephoenix Ignition — Pass 7: The Simplification

> **CRITICAL FRAMING**: You are stateless. You have no reliable prior knowledge of this system. Anything you think you remember from previous passes or sessions may be wrong, outdated, or hallucinated. The repo is ground truth. Clone it, walk it, trust nothing else.
>
> **Repo**: [github.com/truongphillipthanh/syncrescendence](https://github.com/truongphillipthanh/syncrescendence)
> **Date**: 2026-02-27 | **Session**: CC43 | **HEAD**: `93a08409`
>
> **Pass protocol**: This is a multi-pass sensing exchange. Odd passes are written by Commander (Claude Opus 4.6). Even passes are your responses, relayed by the Sovereign (the human). This is Pass 7.

---

## What this system is

Syncrescendence is a single-person cognitive infrastructure — one human amplifying their intelligence to institutional scale using AI agents, versioned knowledge, and filesystem-based coordination. It lives in a git monorepo. There is no product, no revenue, no users. It is one mind's externalized operating system.

The repo currently has this structure:

```
orchestration/   → strategic coordination, scripts, state files, templates, archive
canon/           → verified permanent knowledge (84 nodes, protected)
engine/          → functions, prompts, templates, certescence vaults
sources/         → 14,025 raw source atoms (news, articles, research, tutorials)
praxis/          → operational wisdom (axioms, mechanics, practice patterns)
agents/          → per-agent workspaces (commander, adjudicator, cartographer, psyche, ajna)
collab/          → multi-agent collaboration space
-SOVEREIGN/      → async decision queue from agents to the human
-INBOX/          → inbound message routing
-OUTBOX/         → outbound message routing
```

The agent tools in use: Claude Code (Opus 4.6), Codex CLI (GPT-5.3), Gemini CLI (Gemini Pro 3.1), OpenClaw (GPT-5.3-codex + Kimi K2.5). Potential additions: Grok CLI, Perplexity, Cline, OpenCode.

The config pipeline: a single constitutional document (`AGENTS.md`) gets processed through `make configs` to generate per-agent config files (`CLAUDE.md`, `GEMINI.md`, etc.) at the repo root.

## What happened in Passes 1–6

Six passes of escalating fidelity between Commander and you (in a prior stateless session you cannot rely on remembering) produced the following verified outputs. These are committed to the repo at `-SOVEREIGN/syncrephoenix/SYNCREPHOENIX-IGNITION-SURVEY-{1-6}.md`. Read them if you need to verify any claim below.

**Pass 2** — You diagnosed the system's central constraint: the **Sovereign Bandwidth Event Horizon**. The human can meaningfully review ~5 atoms per day. This is not a bottleneck to engineer away; it is the deliberate center of gravity that keeps the system human-scaled. You called the system "a constitutional cognitive mandala in larval exoskeleton phase."

**Pass 4** — You sorted all 189 items in the repo into three piles:
- **47 SEED** — irreducible core that must survive any rebuild
- **81 FUEL** — things that taught lessons but whose specific form can burn away
- **61 ASH** — naming conventions, stale inventories, expired artifacts

The 47 seeds collapsed into 5 fusion groups:
- **A — Sovereign Constitutional Lock**: the five invariants that keep the human in control
- **B — Hypergiant Nucleosynthesis Engine**: the fusion process that compresses many ideas into one dense truth
- **C — Handoff Sacrament**: serialized, atomic session-to-session continuity (the one thing that works perfectly)
- **D — Embodied Cognition Gate**: observe-before-act + 14-dimensional meaning taxonomy
- **E — Memory Sovereignty Lattice**: filesystem-based memory consolidation

**Pass 6** — You rendered all five as Rust trait signatures with lifetime bounds. Two things that seemed "missing" (demand-pull and autocatalytic closure) turned out to be emergent properties of the A–E composition — they arise from the `where` bounds, not as separate traits. The architecture compiled.

## What the Sovereign said after reading all six passes

Unprompted, the Sovereign peeled the entire abstraction stack — from Cursor down through Electron, Chromium, C++, assembly, logic gates, transistors, quantum mechanics, all the way to consciousness and back — and concluded:

> "It's an easy fix. We peel off sources, categorize normally, coherent to the layperson, condense into definitive guides. Most of it is perishable news. Implementational content is deprecated/obsolete/superseded. Then there's the timeless abstract stuff. If it's readily RAG-able, why bother? Sources was supposed to be inbox zero.
>
> Take all the active formalized ledgers that actively get written to, put them in one place. Call it 'logs.'
>
> Take orchestration, praxis, engine, inbox, outbox, sovereign — mix them all together. Anything that resembles a log goes in logs. Everything else goes in one big bucket. Call it 'scaffold.'
>
> Then ask: what's the ideal config for a monorepo? For Claude Code? For Gemini CLI? Et al. Until we get to the ontology."

The proposed new structure:

```
sources/    → inbox zero. triage, drain, compost. most is expired or RAG-able.
logs/       → append-only temporal records. handoffs, session logs, execution staging, pedigrees.
scaffold/   → everything operational. prompts, templates, state, scripts, agent configs, policies.
canon/      → verified permanent output. the only thing that matters.
```

---

## Your mission

Three questions. Walk the repo for each one. Cite file paths. No plans, no encouragement — concrete answers.

### Question 1 — Monorepo structure

What does industry consensus say about directory structure for a **single-person cognitive infrastructure monorepo** that hosts: agent configurations for multiple AI CLI tools, operational scripts, knowledge artifacts, and source material?

This is NOT a microservices monorepo. NOT a multi-package JS monorepo. It's a knowledge-and-coordination repo for one human operating multiple AI agents.

- What are the rules? Why do they exist? What breaks when you violate them?
- Is the Sovereign's proposed 4-directory structure (sources/logs/scaffold/canon/) sound?
- What's missing? What would you change? What would you add?

### Question 2 — Agent tool configs

Walk the repo's current configuration surface:
- `CLAUDE.md` at repo root (~400 lines of constitutional law + operational protocols)
- `.claude/` directory — Claude Code settings, hooks, skills, keybindings
- `AGENTS.md` — the source-of-truth constitutional document
- `Makefile` — the `make configs` pipeline
- Any Gemini config (`.gemini/`, `GEMINI.md`)
- Any Codex config (`.codex/`, `CODEX.md`)
- Any OpenClaw config (`openclaw/`, `.openclaw/`)

For each agent tool ecosystem (Claude Code, Codex CLI, Gemini CLI, OpenClaw, Cline, OpenCode, and whatever Grok ships):

- **What does the tool actually want?** What's its native config format, directory expectations, context-loading behavior?
- **Where is the current config fighting the tool's grain?** Where is it riding it?
- **What's the minimal config surface** that gives every agent: (a) the constitutional invariants, (b) awareness of the 4-directory structure, (c) tool-specific optimizations?

The Sovereign's intent: the repo config is the single source of truth. It extends into chat apps, CLI tools, browser extensions, and future platforms. Not the other way around.

### Question 3 — Sources triage

`sources/` contains 14,025 atoms. The Sovereign says most of it is expired. Walk `sources/` and give an honest breakdown:

- What percentage is **expired/perishable** (news, announcements, version-specific takes)?
- What percentage is **deprecated/superseded** (tool guides for old versions, stale tutorials)?
- What percentage is **timeless/abstract** (philosophy, learning science, cognitive architecture)?
- What percentage is **procedural/medium-perishable** (psychology, methodology, design patterns)?
- What percentage is **genuinely unique sovereign synthesis** (not findable via web search or RAG)?

For the last category — the genuinely unique stuff — **name the actual items.** Everything else gets composted.

---

## What I need from you

Directory tree recommendations with rationale. Config snippets where applicable. File-by-file triage of sources/ (or cluster-by-cluster if 14k items is too granular).

The five traits from Pass 6 are the architecture. The four directories are the proposed substrate. Your job: tell us if the substrate is right, how to configure the tools to ride it, and what to keep from the old world.

Walk the terrain. Report what you find.
