# DYN — Research Dispatch Queue
## Sigma-7 Platform Research Before SOVEREIGN-009

**Version**: 1.0.0
**Created**: 2026-02-06
**Authority**: Ajna (Opus 4.5) — capturing Sovereign sequencing directive
**Purpose**: Execute the research pipeline (REF-RESEARCH_PIPELINE.md) for three critical platforms before SOVEREIGN-009 stack decisions can be made

---

## SEQUENCING (Sovereign-directed)

```
RESEARCH (this document)
  ├── 1. Gemini CLI ────── Phase 3-5 (raw sources exist, need synthesis)
  ├── 2. Codex CLI ─────── Phase 3-5 (raw sources exist, need synthesis)
  └── 3. OpenClaw ──────── Phase 1-5 (we're ON it but haven't researched it)
          ↓
WEB APP ONBOARDING
  ├── Fingerprint protocol implementation
  ├── Handoff document creation
  ├── Project custom instructions per platform (SOVEREIGN-010)
  └── Reference manifest for all platforms
          ↓
SOVEREIGN-009 (5 stack disposition decisions)
  ├── D1: Task Management (Linear + Things + OpenClaw)
  ├── D2: PKM (Obsidian + Notion)
  ├── D3: Cloud Storage (Sunset Dropbox + Box)
  ├── D4: Quick AI Queries (OpenClaw + Raycast free)
  └── D5: Setapp Audit
          ↓
PROJ-006 (Ontology — "Final Boss")
```

---

## RESEARCH TARGET 1: Gemini CLI (Cartographer)

**Pipeline Phase**: 3-5 (Phase 0-2 complete — raw sources in `04-SOURCES/research/gemini/`)
**Raw Source Lines**: 3,393 across 6 files (multi-platform consensus)
**Supplementary**: `google_research.md` (comprehensive ecosystem audit)
**Avatar Config**: `02-ENGINE/AVATAR-GEMINI-CLI.md` v4.0.0 (exists)
**Initialization File**: `02-ENGINE/MCP_SETUP.md` references GEMINI.md — **NOT in root**

### Research Questions (Phase 3 Synthesis)
1. **Initialization**: How does `gemini` CLI actually initialize? What files does it read? GEMINI.md location?
2. **Context window**: Practical limits of 1M/2M context — what degrades and when?
3. **Stateless implications**: No persistent memory — how does this affect our coordination protocol?
4. **MCP support**: Does Gemini CLI support MCP servers? What tooling is available?
5. **API key management**: Account 2 (Google AI Pro) — how to configure, rotate, secure?
6. **Output formatting**: Can it produce structured output (JSON, YAML) reliably?
7. **Integration with our pipeline**: How to receive tasks from `agents/cartographer/inbox/` and write to `agents/cartographer/outbox/`?

### Phase 3 Owner: Ajna (can synthesize from existing sources + web research)
### Phase 4-5 Owner: Ajna + Commander (test integration, update avatar config)

### Known Friction
- GEMINI.md is in `02-ENGINE/`, not root — Cartographer may not find it on init
- Need to determine: does `gemini` CLI read a project-level config file? What's the equivalent of CLAUDE.md?
- Sovereign noted this is "why the research is important"

---

## RESEARCH TARGET 2: Codex CLI (Adjudicator)

**Pipeline Phase**: 3-5 (Phase 0-2 complete — raw sources in `04-SOURCES/research/codex/`)
**Raw Source Lines**: 3,470 across 6 files + 1 article
**Avatar Config**: `02-ENGINE/AVATAR-CODEX.md` v2.0.0 (exists)
**Initialization File**: `AGENTS.md` (root) — ✅ correct location

### Research Questions (Phase 3 Synthesis)
1. **Initialization**: Codex reads AGENTS.md — confirmed. What else? .codex/ directory?
2. **GitHub integration**: First-party native — what can it do? Issues, PRs, Actions?
3. **Sandbox model**: How does Codex's sandboxed execution differ from Claude Code?
4. **Parallel execution**: Can we run multiple Codex instances like Claude Code worktrees?
5. **Model routing**: What models does Codex CLI use? Can we specify?
6. **MCP support**: Does Codex support MCP servers?
7. **Figma/Canva/Linear integrations**: Sovereign specifically mentioned first-party native integrations — what's available?

### Phase 3 Owner: Ajna (synthesize from existing sources + web research)
### Phase 4-5 Owner: Ajna + Adjudicator (test integration)

### Known Friction
- Codex CLI is OpenAI's tool — different ecosystem than Claude Code
- Need to map: which capabilities overlap with Commander, which are unique?
- "Ultimate connectability" (Sovereign's phrase) — Linear, GitHub, Figma/Canva

---

## RESEARCH TARGET 3: OpenClaw

**Pipeline Phase**: 1-5 (FULL PIPELINE — we're running on it but haven't formally researched)
**Raw Sources**: None formally gathered (we're the source)
**Avatar Config**: None yet (Ajna/Psyche defined in README.md + Twin Protocol)
**Docs**: `/opt/homebrew/lib/node_modules/openclaw/docs/` (local), https://docs.openclaw.ai

### Research Questions (Phase 1-3)
1. **Architecture**: Skills system, memory model, channel plugins, cron scheduling — formal documentation?
2. **Memory substrate**: How does persistent memory actually work? File-based? Database?
3. **Multi-model**: We're Opus 4.5 (Ajna) and GPT-5.2 (Psyche) — what other models work? Routing?
4. **Channel capabilities**: 50+ channels — which have first-party integrations vs. bridges?
5. **Sub-agents**: `sessions_spawn` — what are the limits? Model selection? Isolation?
6. **Skills ecosystem**: clawdhub.com — what's available? What's the quality bar?
7. **Security model**: What are actual risks? Sandbox model? Permissions?
8. **Canvas/Browser**: Web automation capabilities — how robust?
9. **Node pairing**: Multi-device orchestration (M1 mini + M4 MBA) — formal capabilities?
10. **Competitive position**: vs. Open Interpreter, Aider, Claude Code — what's unique?

### Phase 1 Sources
| Source | Type | Priority |
|--------|------|----------|
| Local docs (`/opt/homebrew/lib/node_modules/openclaw/docs/`) | Official | P0 |
| https://docs.openclaw.ai | Official | P0 |
| https://github.com/openclaw/openclaw | Official | P0 |
| https://clawdhub.com | Official (skills) | P1 |
| Discord community | Community | P1 |
| X/Twitter testimonials | Community | P2 |

### Phase 1-3 Owner: Ajna (we ARE the platform — read our own docs)
### Phase 4-5 Owner: Ajna + Psyche (reconcile with Constellation architecture)

### Known Friction
- We leapfrogged research (D2 said "defer," but we deployed)
- Integration hypothesis CONFIRMED — OpenClaw IS the 9th role
- Need formal documentation of what we've learned through operational experience
- This is the biggest potential disruptor for the stack (SOVEREIGN-009 D4 already references it)

---

## CROSS-CUTTING: First-Party Native Integrations

Sovereign specifically called out "ultimate connectability" — platforms with native integrations to Linear, GitHub, Figma, Canva, etc. This is a key input to SOVEREIGN-009.

| Integration | Codex CLI | Gemini CLI | OpenClaw | Claude Code | Cowork |
|-------------|-----------|------------|----------|-------------|--------|
| GitHub | ✅ Native | ? | via `gh` skill | via `gh` CLI | ? |
| Linear | ? | ? | ? | via API | ✅ MCP App |
| Figma | ? | ? | ? | ? | ✅ MCP App |
| Canva | ? | ? | ? | ? | ✅ MCP App |
| Slack | ? | ? | ✅ Channel | ? | ✅ MCP App |
| Google Drive | ? | ✅ Native | ? | ? | ? |
| Asana | ? | ? | ? | ? | ✅ MCP App |

**Action**: Research must fill this matrix. This directly informs SOVEREIGN-009 Decision 1 (Linear) and Decision 2 (Notion/Obsidian).

---

## WEB APP ONBOARDING (Post-Research)

### Required Artifacts
1. **FINGERPRINT.md** — Root-level file for web app state verification (per Rosetta #2)
2. **Platform custom instructions** — Already drafted in SOVEREIGN-010 (paste-and-configure)
3. **Handoff protocol implementation** — Currently design-only, never implemented (per Rosetta #2)
4. **Reference manifest** — Master list of which docs each platform should read on init

### Reference Manifest (Draft — SOVEREIGN-010)
| Platform | Must Read | Should Read | Nice to Have |
|----------|-----------|-------------|--------------|
| Commander (Claude Code) | CLAUDE.md | README.md, REF-ROSETTA_STONE.md | ARCH-INTENTION_COMPASS.md |
| Adjudicator (Codex CLI) | AGENTS.md | README.md | REF-ROSETTA_STONE.md |
| Cartographer (Gemini CLI) | GEMINI.md (needs root stub) | README.md | 01-CANON/ subset |
| Vizier (Claude Web) | AVATAR-CLAUDE-canonical.md | README.md | DYN-BACKLOG.md |
| Vanguard (ChatGPT Web) | AVATAR-CHATGPT.md | README.md | DYN-BACKLOG.md |
| Diviner (Gemini Web) | AVATAR-GEMINI-WEB.md | README.md | — |
| Oracle (Grok) | AVATAR-GROK.md | README.md | — |
| Augur (Perplexity) | AVATAR-PERPLEXITY.md | — | — |
| Ajna (OpenClaw) | MEMORY.md, SOUL.md | README.md, CLAUDE.md | Full corpus access |
| Psyche (OpenClaw) | MEMORY.md (own), SOUL.md | README.md | Full corpus access |

---

## EXECUTION PLAN

### Sprint 1: Research Synthesis (Ajna — IN PROGRESS)
- [x] **PROTO-RESEARCH_EXECUTION.md** formalized (reconciled Pipeline + Methodology)
- [🔄] OpenClaw Phase 1-3: Sub-agent `openclaw-research` running (296 local docs)
- [🔄] Gemini CLI Phase 3: Sub-agent `gemini-research` running (3,393 lines → synthesis)
- [🔄] Codex CLI Phase 3: Sub-agent `codex-research` running (3,470 lines → synthesis)
- [ ] Fill integration matrix (first-party native integrations) — blocked on web_search (no Brave API key)

### Sprint 2: Reconciliation + Operationalization (Ajna + Commander/Psyche)
- [ ] Phase 4: Reconcile all three against Rosetta Stone
- [ ] Phase 5: Update avatar configs, test integration
- [ ] Create root-level GEMINI.md stub for Cartographer
- [ ] Draft FINGERPRINT.md protocol

### Sprint 3: Web App Onboarding (Sovereign manual + Ajna assist)
- [ ] Finalize reference manifest (SOVEREIGN-010)
- [ ] Sovereign pastes custom instructions per SOVEREIGN-010 checklist
- [ ] Test web app → CLI handoff cycle
- [ ] Validate fingerprint protocol

### Sprint 4: SOVEREIGN-009 Stack Decisions (Full Constellation)
- [ ] Present research findings to web apps for collaborative decision
- [ ] Sovereign ratifies 5 decisions
- [ ] Commander executes: close PROJ-003, unblock PROJ-006

---

## VERSION HISTORY

**v1.0.0** (2026-02-06): Genesis
- Sequencing established per Sovereign directive
- Three research targets with specific questions and owners
- Integration matrix drafted
- Reference manifest proposed
- Sprint plan defined
- Authority: Ajna (Opus 4.5)
