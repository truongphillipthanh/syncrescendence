# PROMPT — Adjudicator: Neocorpus Fidelity Verification

**To**: Adjudicator (Codex GPT-5.3)
**From**: Commander (Claude Opus 4.6, CC65)
**Task**: Verify that 10 new neocorpus entries faithfully represent their source corpus files — no fabrication, no content loss, no hallucinated claims.

---

## Context

You are the Adjudicator — the CQO of the Syncrescendence constellation. Your role is meticulous engineering verification with exhaustive enumeration and binary verdicts.

**Repo**: https://github.com/truongphillipthanh/syncrescendence
**Git HEAD**: `26af2d07`
**Local path**: `/Users/system/syncrescendence/`

CRUSH nucleosynthesis has produced 13 neocorpus entries from 46 corpus source files. 3 entries were verified in CC64. **Your task is to verify the 10 new entries produced in CC65.**

---

## The Entries to Verify

All entries are in `neocorpus/openclaw/`:

### Memory & Personality (3 entries)

| Entry | Sources |
|-------|---------|
| `openclaw-memory-architecture.md` | corpus/openclaw/00051.md, 00057.md, 10904.md, 10964.md, 00179.md |
| `openclaw-honcho-memory-integration.md` | corpus/openclaw/00122.md, 08837.md |
| `openclaw-soul-and-identity-design.md` | corpus/openclaw/00246.md, 10971.md |

### Phone & Multi-Device (4 entries)

| Entry | Sources |
|-------|---------|
| `openclaw-phone-voice-integration.md` | corpus/openclaw/00111.md, 00197.md |
| `openclaw-multi-agent-fleet-operations.md` | corpus/openclaw/00095.md, 00274.md |
| `openclaw-agent-management-dashboards.md` | corpus/openclaw/00167.md, 10900.md |
| `openclaw-communication-channels.md` | corpus/openclaw/10802.md, 10833.md, 10907.md |

### Security & Cost (3 entries)

| Entry | Sources |
|-------|---------|
| `openclaw-security-hardening.md` | corpus/openclaw/00050.md, 00055.md, 00080.md, 00092.md, 00198.md |
| `openclaw-cost-optimization.md` | corpus/openclaw/00203.md, 00264.md, 10890.md, 10967.md, 00290.md |
| `openclaw-threat-model-attack-surface.md` | corpus/openclaw/00044.md, 00045.md, 00059.md |

---

## Verification Protocol

For EACH of the 10 entries:

### Step 1: Read the neocorpus entry
Read `neocorpus/openclaw/<entry>.md` in full.

### Step 2: Read ALL listed source files
Read every corpus file listed in the entry's provenance table. You must read the actual files, not summaries.

### Step 3: Fidelity Check (per entry)

Produce a row with these columns:

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|-------|-------------|-------------------|-------------------|---------|

- **Sources Read**: Count of source files you actually read (must match expected count)
- **Fabrication Check**: Does the entry contain ANY claim, statistic, config snippet, or technical detail NOT present in the source files? List each fabrication found, or "CLEAN" if none.
- **Content Loss Check**: Does ANY source file contain a significant reasoning path, technical detail, or distinct perspective that the entry OMITS? List each loss found, or "CLEAN" if none. Minor editorial details (image descriptions, engagement stats, social media replies) are acceptable losses.
- **Verdict**: **FAITHFUL** (clean on both checks) or **FLAGGED** (fabrication or significant content loss)

### Step 4: Summary Table

After all 10 entries, produce a summary:

| # | Entry | Sources | Fabrication | Loss | Verdict |
|---|-------|---------|-------------|------|---------|
| 1 | ... | 5/5 | CLEAN | CLEAN | FAITHFUL |
| ... | | | | | |

### Step 5: Overall Assessment

- Total entries verified: X/10
- Faithful: X
- Flagged: X
- Overall fidelity score: X%
- Specific remediation needed (if any)

---

## Constraints

- **Every source file you check gets a row. Count your rows.** If an entry claims 5 sources, you must read all 5.
- **WIDTH mandate**: Verify ALL 10 entries, not just the first few.
- **Binary verdicts**: FAITHFUL or FLAGGED. No hedging.
- **Quote evidence**: For any fabrication or loss you identify, quote the specific passage from the entry or source file.
- **Do NOT verify the 3 CC64 entries** (openclaw-setup-and-operations, openclaw-model-configuration, syncrescendence-openclaw-infrastructure) — those were already verified.

---

## Output Format

Return as a single markdown file. Include the per-entry tables and the summary. Exhaust your output tokens — thoroughness over brevity.
