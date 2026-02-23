# Live CANON Ticker: Design Specification
## Dynamic Model/Capability/Economics Tracking System

**Status**: DESIGN (awaiting Sovereign approval to implement)
**Created**: 2026-02-01
**Project**: PROJ-LIVE-CANON

---

## Problem Statement

The AI landscape changes quarterly. Frontier model releases, pricing shifts, capability expansions, and open-source proliferation outpace static documentation. MODEL-INDEX.md (last updated 2026-01-02) is already stale. CANON-30300 defines SQL schemas for model tracking but has no population or refresh mechanism.

The constellation needs a system that:
1. Tracks changes as they happen (not monthly snapshots)
2. Distinguishes what changed from what's stable
3. Is machine-parseable for automated sensing
4. Provides FIDS-style at-a-glance visibility
5. Integrates with the research pipeline for verification

---

## Architecture: Three-Layer Design

```
Layer 1: TICKER FEED (append-only changelog)
  engine/DYN-TICKER_FEED.md
  - Chronological entries: "2026-02-15: Claude 5.0 announced, 500K context"
  - Each entry: date, source, category, delta description
  - New entries appended at TOP (most recent first)
  - Never edited, only appended (audit trail)

Layer 2: CURRENT STATE (living reference)
  engine/MODEL-INDEX.md (existing, restructured)
  - The truth: what models exist NOW, their capabilities NOW, prices NOW
  - Updated whenever Layer 1 gets a new entry
  - Diffable via git (every update = commit)

Layer 3: CANON INTEGRATION (stable knowledge)
  canon/CANON-30300-TECH_STACK-comet.md (existing)
  - Updated quarterly or on significant architectural shifts
  - Reflects proven patterns, not breaking news
  - References Layer 2 for current data
```

---

## Layer 1: Ticker Feed Format

```markdown
# AI ECOSYSTEM TICKER FEED
## Chronological Change Log

### 2026-Q1

#### 2026-02-15 [MODEL] Anthropic
- Claude 5.0 announced: 500K native context, native multimodal generation
- Source: anthropic.com/blog
- Impact: IIC reassignment needed (Opus→Claude 5, Sonnet stays for speed)
- Action: Update MODEL-INDEX.md, review CANON-25200 constellation assignments

#### 2026-02-01 [PRICING] Google
- Gemini AI Ultra dropped to $200/mo (was $250)
- Source: blog.google/ai
- Impact: Account 2 economics improved
- Action: Update MODEL-INDEX.md pricing section

#### 2026-01-28 [OSS] DeepSeek
- DeepSeek-V4 released: 256K context, beats GPT-4.1 on SWE-bench
- Source: github.com/deepseek-ai
- Impact: Batch processing candidate upgrade
- Action: Evaluate for PROJ-RESEARCH pipeline
```

**Entry Schema:**
```
#### YYYY-MM-DD [CATEGORY] Provider
- Description of change
- Source: URL or reference
- Impact: Effect on constellation
- Action: Required updates
```

**Categories**: `[MODEL]`, `[PRICING]`, `[CAPABILITY]`, `[OSS]`, `[PLATFORM]`, `[TOOLING]`, `[REGULATION]`

---

## Layer 2: MODEL-INDEX.md Restructure

Evolve from current format to include:

### FIDS Status Board (new section at top)

```markdown
## FIDS — Fleet Status Board

| Platform | Status | Model | Latest | Delta |
|----------|--------|-------|--------|-------|
| Anthropic | NOMINAL | Claude 4.5 Opus | 2025-11-01 | — |
| OpenAI | NOMINAL | GPT-5.2 | 2025-09-15 | — |
| Google | NOMINAL | Gemini 3 Pro | 2025-10-01 | — |
| xAI | NOMINAL | Grok 4 | 2025-12-01 | — |
| DeepSeek | WATCH | V3.2 | 2025-11-15 | V4 imminent |

Status: NOMINAL (stable), WATCH (change expected), UPDATING (active transition),
        DEGRADED (capability regression), NEW (just released)
```

### Change from snapshot to diff-friendly format

Each model section gets a `Last Verified` date:
```markdown
### Claude 4.5 Opus
- **API**: `claude-opus-4-5-20251101`
- **Context**: 200K (1M beta)
- **Strengths**: Deep synthesis, architectural thinking, extended thinking
- **IIC**: Oracle sessions, strategic synthesis
- **Last Verified**: 2026-02-01
```

### Economics section with constellation monthly cost

```markdown
## CONSTELLATION ECONOMICS

| Account | Platform | Tier | Monthly | Function |
|---------|----------|------|---------|----------|
| A1 | Claude | Max 5x | $100 | Commander/Vizier |
| A1 | ChatGPT | Plus | $20 | Compiler/Vanguard |
| A2 | Claude | Pro | $20 | Adjudicator |
| A2 | Google AI | Pro | $20 | Cartographer/Diviner |
| A3 | Grok | SuperGrok | $30 | Oracle |
| — | — | **Total** | **$190** | — |

Last verified: 2026-02-01
```

---

## Update Protocol

### Manual Updates (current)

1. Sovereign or Commander encounters new model/pricing information
2. Add entry to DYN-TICKER_FEED.md (append at top)
3. Update MODEL-INDEX.md corresponding section
4. Commit: `chore(ticker): [CATEGORY] Provider — description`

### Automated Sensing (target)

```
Trigger: Weekly cron OR Sovereign directive
Agent: Cartographer (Gemini CLI) — 1M context surveys web
Script: orchestration/scripts/ticker_sense.sh

Flow:
  1. Gemini CLI queries for recent AI announcements (past 7 days)
  2. Output: structured JSON of detected changes
  3. Script parses JSON, formats ticker entries
  4. Writes to DYN-TICKER_FEED.md
  5. Commander reviews + applies to MODEL-INDEX.md
  6. Commit

Verification:
  - Perplexity (Augur) cross-checks claims against official sources
  - No ticker entry without source URL
  - MODEL-INDEX.md changes require human review
```

### Event-Driven Updates

```
Trigger: Major model release (detected via Grok X sensing or news)
Agent: Oracle (Grok) detects via X firehose
Flow:
  1. Grok surfaces model release chatter
  2. Sovereign dispatches via -INBOX: "Evaluate [model] for constellation"
  3. Cartographer surveys official docs (1M context ingest)
  4. Adjudicator runs benchmark comparison (if code-relevant)
  5. Commander updates ticker + MODEL-INDEX.md
  6. If architectural impact → propose CANON-30300 update
```

---

## Tracking Domains

### Domain 1: Frontier Models (quarterly cadence)
- New model releases from major labs
- Context window changes
- Capability additions (vision, audio, code, reasoning)
- Benchmark results (SWE-bench, MMLU, GPQA, etc.)

### Domain 2: Platform Features (monthly cadence)
- New platform features (Projects, Canvas, Gems, etc.)
- CLI tool updates (Claude Code, Codex, Gemini CLI versions)
- MCP ecosystem changes
- API changes (new endpoints, deprecations)

### Domain 3: Economics (quarterly cadence)
- Subscription pricing changes
- API pricing changes
- New tier introductions
- Constellation cost impact

### Domain 4: Open Source (monthly cadence)
- Notable OSS model releases (DeepSeek, Qwen, Llama, Mistral)
- OSS tool releases relevant to constellation
- License changes

### Domain 5: Capability Frontiers (quarterly cadence)
- Visual AI (image/video/3D generation)
- Audio AI (music, voice, TTS quality)
- Simulation/world models
- Agentic capability shifts
- Scholarly/academic tool releases

### Domain 6: Regulatory/Ecosystem (as-needed)
- AI regulation changes affecting operations
- Platform policy changes
- Significant acquisitions or shutdowns

---

## Integration with Existing Infrastructure

### DEF Variable System
When MODEL-INDEX.md is restructured, key values become DEF-referenced:
```
DEF ConstellationCost:
  monthly_total: 190
  a1_claude: 100
  a1_chatgpt: 20
  a2_claude: 20
  a2_google: 20
  a3_grok: 30
  currency: USD
  last_verified: 2026-02-01
end
```

### Research Pipeline
Ticker sensing becomes Phase 0 of the research pipeline:
```
Phase 0: Sense (Gemini CLI weekly scan → ticker entries)
Phase 1: Triangulate (multi-platform verification of claims)
Phase 2: Evaluate (benchmark + capability assessment)
Phase 3: Integrate (MODEL-INDEX.md + CANON-30300 if architectural)
```

### COCKPIT.md
Add ticker status widget to COCKPIT when FIDS dashboard is built.

---

## Implementation Phases

### Phase A: Ticker Feed File
- Create `engine/DYN-TICKER_FEED.md` with initial entries
- Backfill major changes since MODEL-INDEX.md was last updated (2026-01-02)
- Establish entry format and commit convention

### Phase B: MODEL-INDEX.md Restructure
- Add FIDS status board at top
- Add `Last Verified` dates to each section
- Add constellation economics summary
- Update all stale data to current (2026-02-01)

### Phase C: Automation Script
- Create `ticker_sense.sh` for Gemini CLI weekly sensing
- Create `ticker_apply.sh` for formatting and applying updates
- Add to dispatch system for Cartographer

### Phase D: DEF Integration
- Add ConstellationCost and ModelVersions DEF blocks
- Wire into sn_expand.py for SN document references

---

## Success Criteria

- MODEL-INDEX.md is never more than 2 weeks stale
- Every model/pricing change has a ticker feed entry with source
- Constellation economics are current within 1 billing cycle
- Any agent can query current model state via file read
- Git history shows clear change trail (when things changed and why)

---

## Cross-References

- `engine/MODEL-INDEX.md` — Current model registry (to be restructured)
- `canon/CANON-30300-TECH_STACK-comet.md` — Canonical tech stack (SQL schemas)
- `engine/REF-STACK_TELEOLOGY.md` — Stack teleology (FIDS aspiration, line 335)
- `praxis/MEMORY-AJNA-THREAD-EXTRACTION.md` — FIDS concept origin (line 111)
- `canon/CANON-25200-CONSTELLATION_ARCH-lattice.md` — Constellation architecture
- `orchestration/state/REF-DESKTOP_CAPTURE_INVENTORY.md` — Original ticker directive (line 229)
