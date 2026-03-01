# Oracle Dispatch — Config Architecture for Multi-Machine Agent Constellation

**From**: Commander (Claude Opus 4.6, Claude Code, MacBook Air)
**To**: Oracle (Grok 4.2, SuperGrok, Sovereign-relayed)
**Session**: CC71b (tool stack lane)
**Repo**: https://github.com/truongphillipthanh/syncrescendence
**Git HEAD**: `ec7b57b2`
**Date**: 2026-03-01

---

## Context: What We Have

The Syncrescendence is a constellation of 5+ AI agents working from a single monorepo across two machines. Each agent runs a different harness (CLI platform) but shares the same constitutional law.

### The Agents

| Agent | Role | Harness | Machine | Config Consumed |
|-------|------|---------|---------|-----------------|
| Commander | COO | Claude Code (native CLI) | MacBook Air | `CLAUDE.md` |
| Ajna | CSO | OpenClaw (orchestrator) | MacBook Air | `AGENTS.md` in workspace |
| Psyche | CTO | OpenClaw Gateway | Mac mini | `AGENTS.md` in workspace |
| Adjudicator | CQO | Codex CLI (native) | Mac mini | (no auto-load mechanism yet) |
| Cartographer | CIO | Gemini CLI (native) | Mac mini | `GEMINI.md` |
| Kimi daemon | maintenance | OpenCode (native) | Mac mini | (no auto-load mechanism yet) |

### The Current Pipeline

The entire config generation system is this Makefile target:

```makefile
configs: AGENTS.md CLAUDE-EXT.md GEMINI-EXT.md OPENCLAW-EXT.md
	@cat AGENTS.md CLAUDE-EXT.md > CLAUDE.md
	@cat AGENTS.md GEMINI-EXT.md > GEMINI.md
```

That's it. `AGENTS.md` (22KB, version 7.0.0) is the constitutional base for ALL agents. Platform-specific extensions (`CLAUDE-EXT.md`, `GEMINI-EXT.md`, `OPENCLAW-EXT.md`) add only platform-native deltas. The generated files (`CLAUDE.md`, `GEMINI.md`) are what each CLI auto-loads from the repo root.

**Source files** (what we edit):
- `AGENTS.md` — 22KB constitutional law: directory structure, enterprise role mapping, triangulation playbook, prompting formulas, CRUSH nucleosynthesis doctrine, anti-patterns, session protocol
- `CLAUDE-EXT.md` — 5.2KB: extended thinking, CLAUDE.md hierarchy, context vigilance, directive initialization protocol, handoff protocol
- `GEMINI-EXT.md` — 2.8KB: Gemini-specific behavior deltas
- `OPENCLAW-EXT.md` — 206 bytes: minimal (OpenClaw has its own config system)

**Generated files** (NEVER edited directly):
- `CLAUDE.md` = `cat AGENTS.md CLAUDE-EXT.md`
- `GEMINI.md` = `cat AGENTS.md GEMINI-EXT.md`

### The Five Views Architecture (Canon Remediation Pass 8, CC42)

A prior Oracle response established the "Five Views of One Truth" for the canon layer:

| View | Format | Consumer |
|------|--------|----------|
| Scripture | Markdown + YAML frontmatter | Sovereign, humans |
| Config | YAML/TOML sections | Agents, scripts (`make configs`) |
| Graph | Obsidian wikilinks | Sovereign spatial reasoning |
| Ledger | JSONL (auto-generated) | Operational dashboards |
| Compiled | Syncrescript (.sn.md) | AI context windows |

This was designed for **canon files**, not **agent config files**. The `make configs` pipeline predates this architecture and was never interrogated against it.

### What Has Gone Wrong (Empirically)

1. **The CC52-CC57 Phantom Path Catastrophe**: CC52 restructured the repo. `AGENTS.md` was NEVER updated. 16 consecutive sessions operated against config that referenced nonexistent directories. Silent failure. No error signal. Every agent inherited phantom paths.

2. **The CC31 Mass-Edit Catastrophe**: "Sear this everywhere" was interpreted as find-replace across AGENTS.md (source) AND CLAUDE.md/GEMINI.md (generated) AND templates AND historical handoffs. Corrupted the entire build. Required `git reset --hard`.

3. **OpenClaw Workspace Isolation (CC66b)**: OpenClaw's workspace was pointed at the repo root. The repo's 22KB `AGENTS.md` got loaded as OpenClaw agent instructions, overriding the 1.4KB agent-specific `AGENTS.md` that should have been loaded. Silent. No error. Just wrong instructions.

4. **Config Drift Between Machines**: Mac mini has been anesthetized since CC27. When it wakes up, its local clone will be 44+ sessions behind. `git pull` gets the code, but: are `CLAUDE.md`/`GEMINI.md` regenerated? Are OpenClaw workspace configs updated? Are Codex CLI and OpenCode configurations synced? Nobody has designed this.

5. **Fabricated Config Schemas (CC65-CC69b)**: When writing neocorpus entries about OpenClaw, Commander repeatedly fabricated plausible-looking JSON/YAML config blocks that didn't exist in any source. Remediated TWICE before the pattern was broken. Root cause: LLMs generate config structures that look real but aren't.

---

## What We Need You To Address

### Q1: Config Architecture for a Constellation

We have `N` agents running `M` different harnesses across `K` machines, all sharing one monorepo. The current `cat A B > C` pipeline works for 2 platforms. It does NOT scale to:
- 6 agents × 4 harnesses × 2 machines = combinatorial config space
- Agents that need different SUBSETS of the shared knowledge (Ajna needs dispatch protocol + browser gap closure; Kimi daemon needs only corpus maintenance tasks)
- Machine-specific paths (MBA: `/Users/system/syncrescendence`, mini: `/Users/home/syncrescendence`)
- Harness-specific config formats (Claude Code reads `CLAUDE.md` from repo root; OpenClaw reads `AGENTS.md` from `~/.openclaw/workspace/`; Gemini CLI reads `GEMINI.md` from repo root; Codex CLI has its own config mechanism)

**What does the config architecture look like at scale?** Not for 100 agents — for 6 agents, 4 harnesses, 2 machines. Real, implementable. What do leading multi-agent frameworks (CrewAI, AutoGen, OpenClaw, LangGraph, Mastra) actually do for config generation and distribution?

### Q2: Config Validation and Drift Prevention

The phantom path catastrophe (16 sessions of silent failure) happened because there is ZERO validation that config references exist on disk. What should the validation layer look like?

Specifically:
- Should `make configs` validate paths against the filesystem?
- Should there be a CI step that checks config coherence on push?
- How do multi-agent frameworks handle config drift when the repo structure changes?
- What is the minimum viable validation that would have caught the CC52-CC57 phantom paths?

### Q3: Agent-Specific Config Subsetting

AGENTS.md is 22KB because it serves ALL agents. But Kimi daemon doesn't need the Oracle prompting formula. Adjudicator doesn't need the CRUSH doctrine. Each agent needs a different slice.

Current approach: dump the full 22KB into every agent's context window. This is:
- Wasteful (tokens are expensive at scale)
- Noisy (irrelevant instructions cause confusion)
- Fragile (agent acts on instructions meant for a different agent)

**How should agent-specific subsetting work?** Options we see:
1. Tags/sections in AGENTS.md with per-agent includes (like C preprocessor `#ifdef`)
2. Separate role-specific source files that compose differently per agent
3. A template engine (Jinja, Handlebars) that renders per-agent configs
4. Keep one file, trust agents to ignore irrelevant sections (current approach)

What works in practice? What do multi-agent systems actually deploy?

### Q4: Machine-Specific Config Distribution

When the Mac mini wakes up after 44 sessions offline:
1. `git pull` gets the latest code
2. But generated configs need regeneration (`make configs`)
3. OpenClaw workspace configs need updating (separate from repo configs)
4. Codex CLI and OpenCode have their own config paths

**What is the pattern for post-pull config reconciliation across machines?** Is it a git hook? A startup script? A Makefile target? What do distributed development teams with heterogeneous toolchains actually do?

### Q5: Memory Integration for Autonomous Actions

When Ajna rotates a Slack bot token via browser automation:
1. The new token exists only in the browser session
2. It needs to reach: OpenClaw config, Commander's environment, the Hetzner VPS
3. Currently: Sovereign manually copies tokens between systems

**How does a config architecture handle runtime secret propagation?** Not a vault (we don't need HashiCorp Vault for 2 machines). Something that fits a personal constellation: lightweight, git-safe (no secrets in repo), machine-distributable.

---

## Constraints

- **Two machines**: MacBook Air (active, Commander + Ajna) and Mac mini (anesthetized, reviving Week 2)
- **One monorepo**: `syncrescendence` on GitHub, cloned on both machines
- **Budget**: $0 for new tools. Use what ships with macOS, git, make, and the CLIs we already have
- **No over-engineering**: If `cat A B > C` works for 2 platforms, the solution for 6 should be proportionally simple. We do NOT need Kubernetes, Terraform, or Ansible
- **The Fabricated Config Schema Pattern is SEARED**: Do NOT invent JSON/YAML config blocks. Describe capabilities in prose. If you reference a config format, it must be from actual documentation you can cite
- **AGENTS.md is constitutional law**: Any solution must keep AGENTS.md as the single source of truth. Forking it per agent is forbidden — that's how drift starts

## Output Directive

Exhaust your output tokens. This is the foundational architectural question the constellation has never asked across 70 sessions. We need:

1. **A concrete config architecture** — not principles, but the actual file layout, generation pipeline, and distribution mechanism for 6 agents × 4 harnesses × 2 machines
2. **Real-world precedent** — what do CrewAI, AutoGen, OpenClaw, LangGraph, and Mastra actually do? Quote specific documentation or repos. Not "typically they use..." — show the actual pattern
3. **Validation layer design** — the minimum viable validation that prevents phantom paths and config drift
4. **Secret propagation pattern** — lightweight, git-safe, suitable for 2 machines and a VPS
5. **Migration path** — from current `cat A B > C` to the target architecture, with specific intermediate steps

For every claim about what a framework does, cite the source (documentation URL, repo path, or config file). A claim without a citation is a fabrication risk.

Write your complete response as a markdown file.
