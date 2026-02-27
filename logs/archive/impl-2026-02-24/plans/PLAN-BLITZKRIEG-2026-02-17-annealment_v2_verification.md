# BLITZKRIEG PLAN — Annealment v2 Verification & Gap Patching
## Issued: 2026-02-17 | Task: TASK-20260217-annealment_v2_verification_reinit
## Authority: Sovereign Session 20 | Agent: Commander (Opus, MBA)

---

### Objective
Verify that `ARCH-ONTOLOGY_ANNEALMENT_v2.md` (765 lines, commit `bb0446d`) faithfully
synthesizes all 9 digest sources and raw metacharacterization inbox sources; patch any
gaps discovered; enforce 800-line ceiling on the final document.

---

### Constraints
- **Context**: Opus orchestrator — <10K token content budget. NO raw corpus reads.
- **Per-agent budget**: Max 3,000 lines across all reads (Sonnet subagents).
- **v2 ceiling**: 800 lines. If patches push past 800, compress elsewhere first.
- **wc -l before every Read** — >500 lines → delegate to Sonnet.
- **Dependencies**: No cross-lane dependencies. All 6 lanes run in parallel.
- **DC-004**: ~25 Rosetta Stone terms deferred — separate task, not in scope here.

---

### Pre-Exploration Findings (Commander — completed before plan)

| Finding | Detail |
|---------|--------|
| v2 line count | 765 lines ✓ — within 800-line ceiling |
| All 9 digests present | Confirmed at impl/.scratch/ and clarescence/.scratch/ |
| Canon count | **RESOLVED**: 79 unique non-sn files. Digests claimed 92 = overcounted 13 sn/ mirrors. No unique files were missed. |
| Metachar raw | metachar_1 = 1,040 lines; metachar_2 = 988 lines — within agent budget with v2 |
| DC-004 status | OPEN, target 2026-02-18 — not addressable in this session |
| Deferred commitments | No OPEN items blocking this verification task |

**Canon count resolution**: 79 non-sn files + 81 sn/ mirrors = 160 total. Digests
processed 79 unique + 13 sn/ mirrors (accidentally) = 92 claimed. The 68 "unaccounted"
from the TASK briefing are the remaining 81-13=68 sn/ mirrors the digests correctly
skipped. **No unique CANON files were missed by the digest agents.**

---

### Success Criteria
- [ ] Coverage reports produced for all 9 digests vs v2 (Lanes A–D)
- [ ] Metachar raw vs v2 coverage checked for both prompt rounds (Lanes E–F)
- [ ] Canon 92-vs-79 discrepancy documented and closed
- [ ] ANNEAL-V2-PATCHES.md produced at `impl/.scratch/` (even if empty = all clear)
- [ ] Patches applied to v2 if warranted, line count verified ≤800
- [ ] Commit produced if v2 modified

---

### Lanes (all parallel — no sync dependencies)

| Lane | Agent | Reads | Line Budget | Output File |
|------|-------|-------|-------------|-------------|
| A | Sonnet subagent | v2(765) + CANON-0X(319) + CANON-1X2X(307) | 1,391 | VERIFY-A-canon_0x_1x2x.md |
| B | Sonnet subagent | v2(765) + CANON-30(209) + CANON-31(236) + CANON-32-35(387) | 1,597 | VERIFY-B-canon_30_31_32.md |
| C | Sonnet subagent | v2(765) + GAPS(412) + METACHAR-digest(307) + SCAFFOLD(381) | 1,865 | VERIFY-C-gaps_metachar_scaffold.md |
| D | Sonnet subagent | v2(765) + CLARESCENCE(581) | 1,346 | VERIFY-D-clarescence.md |
| E | Sonnet subagent | v2(765) + METACHAR-digest(307) + metachar_1 raw(1,040) | 2,112 | VERIFY-E-metachar_raw_1.md |
| F | Sonnet subagent | v2(765) + METACHAR-digest(307) + metachar_2 raw(988) | 2,060 | VERIFY-F-metachar_raw_2.md |

All output files at: `orchestration/state/impl/.scratch/`

---

### Lane Prompts

#### LANE A — Canon 0x + 1x2x vs v2

```
You are a verification agent for the Syncrescendence corpus.

TASK: Cross-reference ARCH-ONTOLOGY_ANNEALMENT_v2.md against two canon digests.
For each major concept, theme, or entity in the digests, check if it appears in v2.
Produce a concise coverage checklist.

READ THESE FILES IN ORDER:
1. orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
2. orchestration/state/impl/.scratch/ANNEAL-DIGEST-CANON-0X.md
3. orchestration/state/impl/.scratch/ANNEAL-DIGEST-CANON-1X2X.md

OUTPUT FORMAT (write to orchestration/state/impl/.scratch/VERIFY-A-canon_0x_1x2x.md):
# VERIFY-A: Canon 0x + 1x2x Coverage vs v2
## COVERED (in v2) — list concept + v2 section
## MISSING (in digest but absent from v2) — list concept + which digest
## PARTIAL (mentioned but underrepresented) — list concept + gap description
## VERDICT: PASS / GAPS-FOUND / CRITICAL-GAPS
Keep output under 150 lines. Be specific — name files, sections, concepts.
```

#### LANE B — Canon 30+31+32-35 vs v2

```
You are a verification agent for the Syncrescendence corpus.

TASK: Cross-reference ARCH-ONTOLOGY_ANNEALMENT_v2.md against three canon digests.
For each major concept in the digests, check if it appears in v2.

READ THESE FILES IN ORDER:
1. orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
2. orchestration/state/impl/.scratch/ANNEAL-DIGEST-CANON-30.md
3. orchestration/state/impl/.scratch/ANNEAL-DIGEST-CANON-31.md
4. orchestration/state/impl/.scratch/ANNEAL-DIGEST-CANON-32-35.md

OUTPUT FORMAT (write to orchestration/state/impl/.scratch/VERIFY-B-canon_30_31_32.md):
# VERIFY-B: Canon 30/31/32-35 Coverage vs v2
## COVERED — concept + v2 section
## MISSING — concept + which digest
## PARTIAL — concept + gap description
## VERDICT: PASS / GAPS-FOUND / CRITICAL-GAPS
Under 150 lines. Name files and sections explicitly.
```

#### LANE C — GAPS + METACHAR-digest + SCAFFOLD vs v2

```
You are a verification agent for the Syncrescendence corpus.

TASK: Cross-reference ARCH-ONTOLOGY_ANNEALMENT_v2.md against three digests covering
gaps analysis, metacharacterization, and scaffold state.

READ THESE FILES IN ORDER:
1. orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
2. orchestration/state/impl/.scratch/ANNEAL-DIGEST-GAPS.md
3. orchestration/state/impl/.scratch/ANNEAL-DIGEST-METACHAR.md
4. orchestration/state/impl/.scratch/ANNEAL-DIGEST-SCAFFOLD.md

OUTPUT FORMAT (write to orchestration/state/impl/.scratch/VERIFY-C-gaps_metachar_scaffold.md):
# VERIFY-C: Gaps + Metachar-Digest + Scaffold Coverage vs v2
## COVERED — concept + v2 section
## MISSING — concept + which digest
## PARTIAL — concept + gap description
## VERDICT: PASS / GAPS-FOUND / CRITICAL-GAPS
Under 150 lines. Name files and sections explicitly.
```

#### LANE D — Clarescence vs v2

```
You are a verification agent for the Syncrescendence corpus.

TASK: Cross-reference ARCH-ONTOLOGY_ANNEALMENT_v2.md against the Clarescence digest.
Focus especially on: recurring themes, resolved tensions, persistent gaps, and any
lens-specific findings that should appear in v2 Section 6 (Clarescence Synthesis).

READ THESE FILES IN ORDER:
1. orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
2. orchestration/state/impl/clarescence/.scratch/ANNEAL-DIGEST-CLARESCENCE.md

OUTPUT FORMAT (write to orchestration/state/impl/.scratch/VERIFY-D-clarescence.md):
# VERIFY-D: Clarescence Coverage vs v2
## COVERED — theme/tension/gap + v2 section
## MISSING — theme/tension/gap not in v2
## PARTIAL — underrepresented items
## VERDICT: PASS / GAPS-FOUND / CRITICAL-GAPS
Under 150 lines. Name files and sections explicitly.
```

#### LANE E — Metachar Raw Round 1 vs v2 (HIGH RISK — context distance)

```
You are a verification agent for the Syncrescendence corpus.

CONTEXT: The Unified Annealment v2 convergence agent was rate-limited and may have lost
fidelity on metacharacterization raw files read early in its context. Your job is to
compare the RAW LLM responses from round 1 against (a) the existing METACHAR digest
and (b) v2 directly, to identify any concepts that were captured in raw responses but
missing from v2.

KEY CONCEPTS TO WATCH FOR (per session briefing):
- Palantir ontology primitives (objects, properties, actions, links, media)
- Sovereign stack architecture
- Prosumer analogues
- Shackle-vs-organ framing
- Any novel ontological framing not in the METACHAR digest

READ THESE FILES IN ORDER:
1. orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
2. orchestration/state/impl/.scratch/ANNEAL-DIGEST-METACHAR.md
3. -INBOX/commander/new_ontology_metacharacterization/claude.md
4. -INBOX/commander/new_ontology_metacharacterization/chatgpt.md
5. -INBOX/commander/new_ontology_metacharacterization/gemini.md
6. -INBOX/commander/new_ontology_metacharacterization/grok.md

OUTPUT FORMAT (write to orchestration/state/impl/.scratch/VERIFY-E-metachar_raw_1.md):
# VERIFY-E: Metachar Raw Round 1 vs v2
## IN DIGEST + IN v2 — confirmed captured
## IN RAW but NOT IN DIGEST — things the digest missed from round 1
## IN RAW but NOT IN v2 — things v2 missed (list verbatim concept + raw source file)
## PARTIAL IN v2 — mentioned but surface-level only
## VERDICT: PASS / GAPS-FOUND / CRITICAL-GAPS
Under 200 lines. Quote raw source text for any MISSING items — evidence for patching.
```

#### LANE F — Metachar Raw Round 2 vs v2 (HIGH RISK — context distance)

```
You are a verification agent for the Syncrescendence corpus.

CONTEXT: Same as Lane E but for round 2 of the metacharacterization exercise. Round 2
used a different prompt framing and may contain distinct conceptual material.

KEY CONCEPTS TO WATCH FOR:
- Any evolution or refinement of Palantir-style ontology framing
- Shackle-vs-organ / prosumer / sovereign stack (did round 2 deepen these?)
- Any entirely NEW ontological primitives not in round 1 or the digest

READ THESE FILES IN ORDER:
1. orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md
2. orchestration/state/impl/.scratch/ANNEAL-DIGEST-METACHAR.md
3. -INBOX/commander/new_ontology_metacharacterization_2/claude.md
4. -INBOX/commander/new_ontology_metacharacterization_2/chatgpt.md
5. -INBOX/commander/new_ontology_metacharacterization_2/gemini.md
6. -INBOX/commander/new_ontology_metacharacterization_2/grok.md

OUTPUT FORMAT (write to orchestration/state/impl/.scratch/VERIFY-F-metachar_raw_2.md):
# VERIFY-F: Metachar Raw Round 2 vs v2
## IN DIGEST + IN v2 — confirmed captured
## IN RAW but NOT IN DIGEST — things the digest missed from round 2
## IN RAW but NOT IN v2 — things v2 missed (list verbatim concept + raw source file)
## PARTIAL IN v2 — mentioned but surface-level only
## VERDICT: PASS / GAPS-FOUND / CRITICAL-GAPS
Under 200 lines. Quote raw source text for any MISSING items.
```

---

### Sync Point: Commander Synthesis (after all 6 lanes complete)

Commander reads all 6 VERIFY-*.md outputs (targeting <100 lines each = ~600 lines total,
within Opus budget) and produces:

**`orchestration/state/impl/.scratch/ANNEAL-V2-PATCHES.md`**

Format:
```markdown
# ANNEAL-V2 PATCHES — 2026-02-17
## Summary verdict: PASS | GAPS | CRITICAL
## Patches required: N

### PATCH-001
- Section: [v2 section name]
- Location: [line range or "after [heading]"]
- Gap: [what's missing]
- Content to add: [specific text]
- Source: [VERIFY-X file + original source]
```

If no patches needed: file contains `## Summary verdict: PASS — v2 is complete.`

If patches needed:
- Apply to v2 in-context (small patches = <50 lines added)
- After patches: `wc -l` v2 — must be ≤800 lines
- If would exceed 800: identify compressible sections in v2 first, then apply
- Commit: `fix(anneal): v2 verification patches — [1-line description]`

---

### Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Lanes E/F find major metachar concepts missing from v2 | High | Patches ready; compress v2 Section 8 (Delta, ~60 lines) if ceiling pressure |
| Coverage reports conflict each other | Medium | Commander reconciles — trust VERIFY-E/F over VERIFY-C (raw > digest) |
| Canon count still unclear | Low | RESOLVED by exploration: 79 unique files, 92 = overcount of 13 sn/ mirrors |
| v2 Section 3 (Palantir reconception) underspecified | Medium | Lanes E/F specifically watch for Palantir primitive depth |
| Rate limit on parallel Sonnet dispatch | Low | 6 agents, stagger 30s if needed; each is independent |

---

### Known Issues Acknowledged (Not Blocking)

- **Risk #4 (CLARESCENCE digest path)**: `impl/clarescence/.scratch/` vs `impl/.scratch/` — NOT fixing this session. Convergence agent already used it from its actual location. Move only if future ops require it.
- **Risk #5 (DC-004 Rosetta Stone)**: ~25 unformalized terms — separate DC-004 task, target 2026-02-18. Not in scope.
- **SOVEREIGN ALERT storm**: 100+ ALERT files in `-SOVEREIGN/` from watchdog/orchestrator incidents. Not related to this task — defer cleanup.

---

### Execution Sequence

1. **NOW**: Dispatch all 6 Sonnet agents in parallel (Task tool, subagent_type=general-purpose)
2. **After all 6 return**: Commander reads VERIFY-A through VERIFY-F
3. **Commander writes**: ANNEAL-V2-PATCHES.md
4. **If patches**: Apply → wc -l check → commit
5. **Completion**: Update TASK file status to DONE, execution log entry, mark DC-004 as noted

---

*PLAN-BLITZKRIEG-2026-02-17-annealment_v2_verification.md*
*Commander (Opus) | MBA | 2026-02-17*
