# Pool A Research Census Report

**Generated:** 2026-02-21
**Source directory:** `/Users/system/Desktop/research/`
**pool_origin:** `pool_a_research`

---

## Summary

| Metric | Value |
|--------|-------|
| Total files inventoried | 450 |
| .md files | 448 |
| Non-.md files (excluded from CSV rows) | 2 (see Anomalies) |
| Files with frontmatter | 438 |
| Files missing frontmatter | 12 |
| Files with URL field | 438 |
| Files missing URL | 12 |
| Date range | 2002-02-01 — 2026-02-21 |

---

## Breakdown by Platform

| Platform | Count |
|----------|-------|
| x | 428 |
| website | 11 |
| internal | 10 |
| aihero | 1 |
| **Total** | **450** |

Notes:
- `x` = Twitter/X posts (articles and threads)
- `website` = web articles/pages (includes `undated-website-*` files)
- `internal` = PROMPT-AGENT and RESPONSE-AGENT files (internal research/prompt artifacts)
- `aihero` = aihero platform capture

---

## Breakdown by Format

| Format | Count |
|--------|-------|
| article | 315 |
| thread | 124 |
| research | 11 |
| **Total** | **450** |

Notes:
- `article` = `x_article` filename pattern + `website` single-segment files
- `thread` = `x_thread` filename pattern
- `research` = PROMPT/RESPONSE pairs + `aihero` file (internal research artifacts)

---

## Date Range

- **Earliest:** 20020201 (2002-02-01) — Paul Graham "Taste for Makers" (retroactively dated)
- **Latest:** 20260221 (2026-02-21)
- **Undated files:** 4 (`undated-website-*` prefix)
- **Most content concentrated in:** 2026-01 through 2026-02 (bulk capture window)

---

## Files Missing Frontmatter (12)

These files have no YAML frontmatter block (`---`). They also all lack a `url` field as a consequence.

| Filename | Notes |
|----------|-------|
| `20260130-x_article-the_engineering_behind_clawdbot-@hesamation.jpeg` | Binary image file — not a markdown document |
| `20260220-x_thread-between_gemini_31_and_claude_46-@bilawalsidhu.md` | Missing frontmatter |
| `PROMPT-AUGUR-20260203-openclaw_deep_research.md` | Internal prompt artifact — no frontmatter expected |
| `PROMPT-DIVINER-20260203-openclaw_deep_research.md` | Internal prompt artifact |
| `PROMPT-ORACLE-20260203-openclaw_deep_research.md` | Internal prompt artifact |
| `PROMPT-VANGUARD-20260203-openclaw_deep_research.md` | Internal prompt artifact |
| `PROMPT-VIZIER-20260203-openclaw_deep_research.md` | Internal prompt artifact |
| `RESPONSE-AUGUR-20260203-openclaw_deep_research.md` | Internal response artifact — no frontmatter expected |
| `RESPONSE-DIVINER-20260203-openclaw_deep_research.md` | Internal response artifact |
| `RESPONSE-ORACLE-20260203-openclaw_deep_research.md` | Internal response artifact |
| `RESPONSE-VANGUARD-20260203-openclaw_deep_research.md` | Internal response artifact |
| `RESPONSE-VIZIER-20260203-openclaw_deep_research.md` | Internal response artifact |

Of the 12 missing frontmatter, **10 are PROMPT/RESPONSE internal files** (expected behavior — not web captures), **1 is a `.jpeg` binary**, and **1 is a genuine gap** (`@bilawalsidhu` thread).

---

## Files Missing URL (12)

Identical set to missing-frontmatter files above. All 438 files with frontmatter contain a `url:` field. No partial-frontmatter cases (where frontmatter exists but url is absent) were found.

---

## Anomalies

### Non-.md Files (2)

| Filename | Type | Notes |
|----------|------|-------|
| `.DS_Store` | macOS metadata | Finder artifact — should be in `.gitignore` |
| `20260130-x_article-the_engineering_behind_clawdbot-@hesamation.jpeg` | JPEG image | Embedded image file saved alongside its companion `.md` file of the same stem. The `.md` version of this file also exists in the directory. |

### Unusual Naming Patterns (14)

**PROMPT/RESPONSE pairs (10 files):** Follow the pattern `{PROMPT|RESPONSE}-{AGENT}-{DATE}-{slug}.md` rather than the standard `{DATE}-{platform}-{title}-{creator}.md` convention. These are internal Constellation research artifacts (five agents: AUGUR, DIVINER, ORACLE, VANGUARD, VIZIER), all dated 20260203, all concerning `openclaw_deep_research`. Classified as platform=`internal`, format=`research`.

**Undated website files (4 files):** Prefixed with `undated-` rather than a YYYYMMDD date. Content is undatable web documentation:
- `undated-website-agents_md_simple_open_format_guiding--agents.md`
- `undated-website-solverforge-huggingface.md`
- `undated-website-soul_md_what_makes_an_ai_itself--soul.md`
- `undated-website-voicebox_open_source_voice_cloning_powered--voicebox.md`

**Double-dash separator in undated filenames:** Three of the four undated files use `--` before the creator/source token (e.g., `--agents`, `--soul`, `--voicebox`), suggesting an intentional disambiguation separator when the creator slug is derived from the page rather than a person handle.

**Retroactively dated outlier:** `20020201-website-taste_for_makers-paulgraham.md` is dated 2002-02-01, over 24 years before the next-oldest file. This is the publication date of the Paul Graham essay, not a capture date.

**Far-past outlier:** `20250612-website-dont-build-multi-agents-cognition.md` is dated 2025-06-12, predating the main 2026 capture window by ~7 months.

---

## Data Quality Assessment

- **438/450 (97.3%)** files have complete frontmatter with URL — strong overall quality.
- **10/12 missing frontmatter** cases are intentional internal artifacts, not data gaps.
- **1 genuine gap:** `20260220-x_thread-between_gemini_31_and_claude_46-@bilawalsidhu.md` should have frontmatter added.
- **1 binary file** (`.jpeg`) present in source directory — may want to move to an `assets/` subfolder.
- **1 `.DS_Store`** file — should be gitignored at the research directory level.
