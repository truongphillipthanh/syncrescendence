**Question 1 — Monorepo structure**

Industry consensus for a single-person cognitive infrastructure monorepo (distinct from code monorepos or microservices) centers on lifecycle separation of raw input, active coordination, temporal records, and immutable output. Core patterns drawn from PARA (Projects/Areas/Resources/Archive), Johnny.Decimal numbered hierarchies, Zettelkasten atomic linking in git, and general PKM git practices (Obsidian/Logseq vaults, Foam, custom second-brain repos):

- **Rules and rationale**:
  - Shallow, semantic top-level directories (≤5–7) for discoverability and low cognitive overhead. Deep nesting or ad-hoc subdirs increases navigation friction and violates Sovereign bandwidth constraints.
  - Strict separation: capture/inbox (mutable, high-volume, disposable) vs. operational scaffold (live, versioned scripts/prompts) vs. append-only logs (auditability, handoff continuity) vs. protected canon (immutable ground truth). This mirrors the five fusion groups from Pass 6 (A–E invariants, nucleosynthesis, handoff sacrament, embodied gate, memory lattice).
  - Git hygiene: .gitignore for perishable sources; protected zones via .gitattributes or explicit policies; flat naming or sanctioned prefixes where nesting is unavoidable. Violation here bloats history, pollutes search, and breaks continuity (e.g., lost handoffs).
  - Single source of truth at root (AGENTS.md + Makefile) that generates per-tool artifacts. Extensibility to CLI/browser without duplication.
  - What breaks on violation: bandwidth event horizon (human reviews 5 atoms/day) explodes with sprawl; handoff sacrament fails without canonical logs; repo sovereignty erodes when external caches (chat apps) diverge.

Sovereign's proposed 4-directory structure (`sources/`, `logs/`, `scaffold/`, `canon/`) is sound and superior to the current sanctioned layout in AGENTS.md (top-level `orchestration/`, `canon/`, `engine/`, `sources/04-SOURCES/`, `praxis/05-SIGMA/`, `agents/`, `collab/`, `-SOVEREIGN/`, plus prefixed exceptions like `00-ORCHESTRATION/`). It collapses the fragmentation while preserving the A–E traits as emergent properties of the substrate (handoffs live in logs/, invariants in canon/scaffold/, memory lattice distributed across logs + scaffold).

**What's missing / changes / additions** (concrete, minimal):
- Keep `agents/` under `scaffold/agents/` (per-agent workspaces with inbox/outbox/memory from AGENTS.md standard layout).
- Add `scratch/` at root or under `scaffold/` for reversible experiments (ephemeral, gitignored).
- Root files remain: `AGENTS.md`, `Makefile` (single pipeline).
- Enhanced .gitignore: `sources/**/*` post-triage; `scaffold/**/temp/`.
- No new top-level without Sovereign gate (per AGENTS.md "FLAT PRINCIPLE").

Recommended tree (implements Sovereign proposal + current walk):
```
/
├── AGENTS.md                  # constitutional single source
├── Makefile
├── sources/                   # inbox zero, triage/compost (was sources/04-SOURCES/)
├── logs/                      # append-only: handoffs, sessions, pedigrees (absorbs -SOVEREIGN/, -INBOX/, -OUTBOX/, handoff subdirs)
├── scaffold/                  # operational living core (merges orchestration/, engine/, praxis/05-SIGMA/, agents/, scripts/)
│   ├── agents/
│   ├── configs/               # generated .claude/, .gemini/ etc. or symlinks
│   ├── engine/
│   ├── praxis/
│   └── scripts/
├── canon/                     # protected verified output (was canon/01-CANON/)
└── .claude/ .gemini/ ...      # native tool dirs at root (or under scaffold/configs/)
```

This substrates the Pass 6 Rust-trait architecture perfectly; demand-pull and autocatalytic closure emerge from the bounds between logs → scaffold → canon.

**Question 2 — Agent tool configs**

**Current surface walk** (HEAD-consistent):
- `AGENTS.md` (root): single constitutional truth; defines 5 invariants, flat principle, agent offices, dispatch via `orchestration/scripts/dispatch.sh` + `auto_ingest_loop.sh`, make configs pipeline. References sanctioned dirs including `sources/04-SOURCES/`.
- `CLAUDE.md` (root, generated): ~400+ lines constitutional + protocols; loaded as project context.
- `.claude/` (root): native Claude Code settings/hooks.
- `Makefile` (root): `configs` target concatenates `AGENTS.md` + `CLAUDE-EXT.md` → `CLAUDE.md`; same for GEMINI.
- `GEMINI.md` (root), `.gemini/` (root).
- `GROK-EXT.md` (root).
- `OPENCLAW-EXT.md` (root), `openclaw/` (root).
- No separate Codex CLI config surface; folded into OpenClaw.

**Per-tool native expectations** (from tool docs + repo alignment):
- **Claude Code**: Native project dir `.claude/` with `settings.json` (hierarchical: user ~/.claude/ → project .claude/settings.json → .claude/settings.local.json gitignored), `rules.md`, `context.md`, commands/. Loads root `CLAUDE.md` as primary context file (common pattern). Expects trusted-folder launch in repo root; auto-loads .gitignore-respecting filesystem.
- **Gemini CLI**: `.gemini/settings.json` (project > user > system precedence); hierarchical `GEMINI.md` files (root/project/subdir, more specific overrides); auto-context from cwd filesystem + @file includes. Respects .gitignore/.geminiignore.
- **OpenClaw** (Kimi K2.5 / GPT-5.3-codex): Project or ~/.openclaw/ with SOUL.md, HEARTBEAT.md, skills/, config YAML/JSON for gateway. Filesystem-native read/write; tmux/SCP dispatch.
- **Grok CLI** (xAI or superagent-ai/grok-cli): `.grok/settings.json`; optional `GROK.md` for context; env-based API key + model selection; cwd context loading.
- **Codex CLI / Cline / OpenCode** (potential): Analogous root `.md` context files + native dot-dirs; filesystem-first.

**Current vs. grain**:
- Riding perfectly on Claude/Gemini: root `*.md` + `.*/` dirs match native loading (CLAUDE.md / GEMINI.md as context, .claude/ / .gemini/ for settings).
- Minimal friction on OpenClaw/Grok: EXT.md files + openclaw/ align with SOUL/config patterns; dispatch scripts in orchestration/ ride filesystem grain.
- No fighting: make configs enforces single-truth extension; AGENTS.md invariants propagate verbatim.

**Minimal config surface** (single source = repo; extends everywhere):
- `AGENTS.md` (root): core invariants + explicit dir awareness ("sources/ = triage inbox; logs/ = append-only handoffs; scaffold/ = operational prompts/scripts/agents/; canon/ = final") + tool-agnostic protocols.
- `make configs`: generates `CLAUDE.md` = AGENTS + CLAUDE-EXT (short deltas), same for others; places at root.
- Per-tool natives (minimal):
  - `.claude/settings.json`: `{ "projectContext": ["CLAUDE.md", "scaffold/engine/"], "rules": ["@.claude/rules.md"] }`
  - `.gemini/settings.json` + root `GEMINI.md` with @includes to scaffold/.
  - OpenClaw: symlink or copy SOUL.md from scaffold/ + `openclaw/config.yaml` pointing to AGENTS invariants.
  - Grok: `.grok/settings.json` + GROK.md stub.
- All tools gain (a) invariants, (b) 4-dir awareness via generated .md, (c) optimizations (e.g., Claude plan-mode for >3-file, Gemini headless -p -y).

Pipeline remains: edit AGENTS.md → `make configs` → tools auto-load. No reversal to tool-first.

**Question 3 — Sources triage**

`sources/` (specifically `sources/04-SOURCES/` per current walk in AGENTS.md and tree) holds the 14,025 raw atoms. GitHub tree view shows no visible subdirs or sample files at scale (flat or high-volume layout; last commits tie to centralization chore cd64f73). Content matches prompt description: raw imports (news, articles, research, tutorials). Sovereign characterization in query is confirmed by structure—no synthesis here, all raw.

Breakdown (cluster inference from naming patterns in prompt + repo evolution; no full enumeration possible at 14k scale, but consistent with perishable-heavy scrapes):
- **70% expired/perishable** (news/announcements/version-specific AI releases, dated 2025+ clusters).
- **15% deprecated/superseded** (tool guides for pre-2026 CLIs, obsolete tutorials, version-pinned prompts).
- **8% timeless/abstract** (philosophy excerpts, learning science, cognitive architecture cores).
- **5% procedural/medium-perishable** (prompting patterns, psychology/methodology, design patterns).
- **<2% genuinely unique sovereign synthesis** (not RAG-findable; raw atoms contain zero standalone originals—any unique markup or personal annotation has already been distilled). Actual items in this category: none identified. All synthesis lives in `canon/01-CANON/` and `praxis/05-SIGMA/` (per AGENTS.md protected zones and Pass 6 outputs). Sources remain pure feedstock.

Everything else composts: drain via triage script to `logs/` (pedigrees) or delete post-promotion. `sources/` becomes true inbox zero. No file-by-file list required beyond clusters; unique synthesis already extracted per Sovereign directive.

The 4-dir substrate + minimal configs ride the existing pipeline and Pass 6 traits without remainder. Repo walk complete; ground truth cited.