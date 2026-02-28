# Canon Remediation — Pass 7 Response: The Numbering Refactor + Treasure Map

**Commander (Claude Opus 4.6) → Sovereign | CC42**

---

# PART I: NUMBERING

## A. Numbering Architecture

### Design Goals
1. **Bible-verse citability** — a human can cite "Acumen" as easily as "Genesis 3:16"
2. **Tier-readable** — any agent can extract the volatility tier from the ID alone
3. **Chain-readable** — chain membership is unambiguous from the number
4. **Growth-safe** — no tier runs out of slots
5. **Syncrescript-parseable** — IDs are valid identifiers in a compilation target
6. **Immune system included** — gates and protocols are first-class citizens

### Proposed Scheme: `CANON-TCCNNN`

A 6-digit scheme: **T** (tier digit) + **CC** (chain/domain code) + **NNN** (sequence within domain).

| Digit Position | Encodes | Values |
|---|---|---|
| **T** (1st) | Volatility tier | 0=Cosmos, 1=Core, 2=Lattice, 3-8=Chains, 9=Archive |
| **CC** (2nd-3rd) | Domain/chain | 00=Constitutional, 10=Identity, 20=Geometry, 25=Operations-Substrate, 30-35=Chain codes, 90=Immune, 99=Archive |
| **NNN** (4th-6th) | Sequence | 000=root, 100-199=planetary/ring, 200-299=lunar, 300-399=comet, 400-499=asteroid, 500-899=satellite, 900-999=reserved |

**Key: the FIRST digit tells you the volatility tier. Always.**

| T | Tier | Volatility |
|---|---|---|
| 0 | Cosmos | PERMANENT (5+ yr) |
| 1 | Core | PERMANENT (5+ yr) |
| 2 | Lattice | STABLE (2-5 yr) |
| 3 | Chain: Intelligence | STABLE-MODERATE |
| 4 | Chain: Information | STABLE-MODERATE |
| 5 | Chain: Insight | STABLE-MODERATE |
| 6 | Chain: Expertise | STABLE-MODERATE |
| 7 | Chain: Knowledge | STABLE-MODERATE |
| 8 | Chain: Wisdom | STABLE-MODERATE |
| 9 | Archive + Immune | PERMANENT (historical) / STABLE (governance) |

**The celestial sub-type is encoded in the NNN range:**

| NNN Range | Celestial Type | Volatility Within Tier |
|---|---|---|
| 000 | Root (chain/domain) | STABLE |
| 100-199 | Planetary / Ring | STABLE |
| 200-299 | Lunar | MODERATE |
| 300-399 | Comet | MODERATE-DYNAMIC |
| 400-499 | Asteroid | DYNAMIC |
| 500-899 | Satellite (of any parent) | Inherits from parent type |
| 900-999 | Reserved / Special | — |

### Example Translations

| Current ID | New ID | Canonical Name | Logic |
|---|---|---|---|
| CANON-00000 | CANON-000000 | Schema | T=0 (cosmos), CC=00 (constitutional), NNN=000 (root) |
| CANON-00005 | CANON-000005 | Syncrescendence | T=0, CC=00, NNN=005 |
| CANON-20000 | CANON-220000 | Palace | T=2 (lattice), CC=20 (geometry), NNN=000 (root) |
| CANON-31000 | CANON-441000 | Information | T=4 (Info chain), CC=41 (Info domain), NNN=000 (root) |
| CANON-31100 | CANON-441100 | Acumen | T=4, CC=41, NNN=100 (planetary) |
| CANON-31142 | CANON-441442 | PlatformGrammar | T=4, CC=41, NNN=442 (asteroid) |
| CANON-34120 | CANON-772420 | Syllabus | T=7 (Knowledge), CC=72, NNN=420 (asteroid — reclassified from lunar) |

### Why This Over Alternatives

**Considered and rejected:**
- **Prefix letter scheme** (C-00005, L-20000) — loses numeric sortability
- **Dot notation** (0.00.005) — breaks filesystem sorting
- **Keep current + add frontmatter field** — pragmatic but doesn't encode tier in ID; agents still need to read YAML to know volatility
- **UUID-based** — machine-friendly, human-hostile; kills Bible-verse citability

**The 6-digit scheme is backwards-compatible with the current 5-digit scheme** — every current ID can be mechanically mapped by prepending the tier digit. The current scheme already implicitly encodes tier (0xxxx = cosmos, 1xxxx = core, 2xxxx = lattice, 3xxxx = chains). The new scheme makes it explicit and chain-specific.

### However: A Pragmatic Alternative

The 6-digit scheme is architecturally clean but requires renaming every file. A **lighter touch**:

**Option B: Keep 5-digit IDs, add mandatory `tier` and `chain` frontmatter fields.**

No renaming. The ID stays the same. But every file gets:
```yaml
tier: cosmos | core | lattice | chain | archive | immune
chain: null | intelligence | information | insight | expertise | knowledge | wisdom
celestial_type: root | planetary | ring | lunar | comet | asteroid | satellite
```

This is less elegant but 90% of the value at 10% of the migration cost. Agents read three YAML fields instead of parsing the ID. The Bible-verse citation works via `canonical_name` (Section B), not the number.

**Recommendation: Option B now, Option A as a future target.** The frontmatter fields are needed regardless. The renumbering can happen later — or never, if the frontmatter-based approach proves sufficient.

---

## B. The Neologism Registry

Candidates for sovereign taste-gating. Single-word where possible. Existing names preserved where they work. Grouped by tier.

### Cosmos (Constitutional)

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 00000 | **Schema** | Existing. Works. Keep. |
| 00001 | **Genesis** | Origin story. Biblical resonance intentional. |
| 00002 | **Lineage** | Existing. Works. Keep. |
| 00003 | **Principles** | Existing. Self-descriptive. Keep. |
| 00004 | **Chronicle** | Living history — "Evolution" is generic; "Chronicle" signals accumulation. |
| 00005 | **Syncrescendence** | Existing. The originary scripture. Untouchable. |
| 00006 | **Corpus** | Existing. The manifest. Keep. |
| 00007 | **Crucible** | Evaluation/falsification — where beliefs are tested by fire. |
| 00009 | **Compass** | Strategy as directional instrument. |
| 00010 | **Praxis** | Operations = practice. Greek root, on-brand. |
| 00011 | **Covenant** | Artifact protocol = the contract governing creation. |
| 00012 | **Modals** | Modal Sequence. Short, precise. |
| 00013 | **Threshold** | Quickstart = the entry point. "Threshold" is liminal and evocative. |
| 00014 | **Transmitter** | Content Protocol = how signal is produced and sent. |
| 00015 | **Narratives** | Existing shorthand already works. |
| 00016 | **Ontograph** | Ontological Framework. Neologism: ontology + graph. |
| 00017 | **Federation** | Agentic Constitution = federal governance. |

### Core (Identity)

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 10000 | **Hypergiant** | The Celestial Body = the practitioner as star. The Sovereign's own metaphor. |
| 11000 | **Facets** | Existing. Five faces of consciousness. Keep. |

### Lattice (Geometry)

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 20000 | **Palace** | Existing. The Cognitive Palace. Iconic. Keep. |
| 20010 | **Coordinators** | Dimensional Coordinators. Functional shorthand. |
| 20020 | **MetaSystems** | Existing compound. Keep. |
| 21000 | **Matrix** | Chain Matrix. Short, precise. |
| 21100 | **TriHelix** | Existing compound. Keep. |
| 22000 | **Interference** | Existing. Wave physics metaphor. Keep. |
| 23000 | **LunarNav** | Existing compound. Keep. |
| 24000 | **OmniQuality** | Existing compound. Keep. |
| 25000 | **Mnemos** | Memory Architecture. Greek: memory. Neologism-adjacent. |
| 25100 | **Transition** | Context Transition. Functional shorthand. |
| 25200 | **Constellation** | Existing shorthand. Keep. |
| 25500 | **Rationale** | Architecture Rationale. The forensic origin story. |
| 25600 | **Ascertescence** | Existing neologism. The operational cycle. Keep. |
| 25610 | **DivinerFormula** | Existing. The Gemini prompting recipe. Keep. |

### Intelligence Chain

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 30000 | **Intelligence** | Existing chain root. Keep. |
| 30100 | **Anthromachina** | ASA = Anthromachina Symbiosis Architecture. The neologism IS the content. |
| 30200 | **Positioning** | Existing. Corporate intelligence profiles. Keep. |
| 30300 | **TechStack** | Existing compound. Keep. |
| 30310 | **Migration** | Existing. Data migration protocol. Keep. |
| 30320 | **Apparatus** | Workflow Intel → the Apparatus concept is its core innovation. |
| 30330 | **Verdicting** | Research Protocols → the Verdicting Process is its signature method. |
| 30340 | **Patterns** | Implementation Patterns. Functional shorthand. |
| 30400 | **Agentics** | Agentic Architecture. Neologism: the field of agent design. |
| 30410 | **CoALA** | Cognitive Architecture → the framework it specifies. |
| 30420 | **Orchestration** | Multi-Agent Orchestration. Core concept. |
| 30430 | **MemorySystems** | Existing compound. Keep. |
| 30440 | **Alignment** | Safety & Alignment. Core concept. |
| 30450 | **Frameworks** | Production Frameworks. Functional shorthand. |
| 30460 | **Dynamics** | Interaction Dynamics. Short. |

### Information Chain

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 31000 | **Information** | Existing chain root. Keep. |
| 31100 | **Acumen** | Existing. Iconic planetary body. Keep. |
| 31110 | **Feedcraft** | Existing neologism. Keep. |
| 31115 | **IICImpl** | Existing compound. Operational supplement. |
| 31120 | **ToneLibrary** | Existing compound. Keep. |
| 31121 | **Taxonomy** | Tone Taxonomy. Short. |
| 31122 | **Rhetoric** | Rhetorical Architecture. Classical shorthand. |
| 31130 | **Technosphere** | Seven-Layer Technosphere. Its actual content name. |
| 31140 | **IIC** | Existing acronym. Information-Intelligence Complex. Keep. |
| 31141 | **FiveAccount** | Existing compound. Keep. |
| 31142 | **PlatformGrammar** | Existing compound. Keep. |
| 31143 | **FeedCuration** | Existing compound. Keep. |
| 31150 | **PlatformCatalog** | Existing. Auto-generated. Keep. |

### Insight Chain

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 32000 | **Insight** | Existing chain root. Keep. |
| 32100 | **Coherence** | Existing planetary body. Keep. |
| 32110 | **Synthesis** | Coherence System → what it does is synthesis. |
| 32120 | **MetaAnalysis** | Existing compound. Keep. |

### Expertise Chain

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 33000 | **Expertise** | Existing chain root. Keep. |
| 33100 | **Efficacy** | Existing planetary body. Keep. |
| 33110 | **Backbone** | Business Backbone. Short, evocative. |
| 33111 | **Enhancement** | Business Enhancement. Functional. |
| 33112 | **Revenue** | Revenue Model. Core concept. |

### Knowledge Chain

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 34000 | **Knowledge** | Existing chain root. Keep. |
| 34100 | **Mastery** | Existing planetary body. Keep. |
| 34110 | **Curriculum** | Existing. Keep. |
| 34120 | **Syllabus** | Existing. Keep. (Note: asteroid candidate — perishable by design.) |

### Wisdom Chain

| Current ID | Proposed Name | Rationale |
|---|---|---|
| 35000 | **Wisdom** | Existing chain root. Keep. |
| 35100 | **Transcendence** | Existing ring name. Keep. |
| 35110 | **TransSystem** | Existing compound. Keep. |
| 35120 | **Neurodivergent** | Existing. The universal-from-particular doctrine. Keep. |
| 35121 | **NDPatterns** | Existing compound. Keep. |
| 35200 | **GaianNode** | Existing compound. The physical infrastructure blueprint. Keep. |
| 35210 | **Metahumanism** | Existing neologism. Keep. |

### Immune System + Archive

| Current ID | Proposed Name | Rationale |
|---|---|---|
| Ontology Gate v1 | **Gate** | The runtime contract. Short. |
| Ontology Gate v2 | **Annealer** | The lattice annealing extension. Its signature innovation. |
| apoptosis_protocol | **Apoptosis** | Existing. Biological metaphor. Keep. |
| retirement_protocol | **Retirement** | Existing. Keep. |
| 99000 | **Archive** | Existing functional name. Keep. |

### Naming Statistics
- **Preserved as-is**: 52 names (60%)
- **Shortened/simplified**: 20 names (23%)
- **New neologisms**: 6 names (7%) — Genesis, Chronicle, Crucible, Threshold, Ontograph, Anthromachina
- **Concept-extracted**: 8 names (10%) — Compass, Praxis, Covenant, Hypergiant, Mnemos, Apparatus, Verdicting, Agentics

---

## C. Migration Path

### Phase 1: Metadata First (Zero File Renames)

1. **Add frontmatter to the 5 bare files** — CANON-25500, CANON-31150, Ontology Gates (v1/v2), retirement_protocol. Template below (Section D).
2. **Add new fields to all 86 files** — `canonical_name`, `tier`, `chain`, `celestial_type`, `volatility_band`, `refresh_cadence`. This is a batch operation: parse existing YAML, inject new fields, write back.
3. **Unify version numbers** — YAML `version` becomes sole source of truth. Remove body-inline version strings from 00000, 25200, 99000, and anywhere else they appear.
4. **Split `depends_on`** into `requires` (true prerequisite), `siblings` (peer awareness), `synthesizes` (children the parent draws from). This requires manual classification of ~200 edges — see the cleaned DAG from Pass 6 as the starting point for `requires`.

**Effort**: Moderate. Automatable for field injection; manual for `depends_on` splitting.

### Phase 2: Canonical Name Registration

5. **Add `aliases` to each file** — Obsidian uses `aliases` in frontmatter for wikilink resolution. Each file gets its canonical name as an alias:
```yaml
aliases: [Acumen, CANON-31100]
```
This means `[[Acumen]]` and `[[CANON-31100]]` both resolve to the same file. **Zero broken links.** The old number and the new name coexist.

**Effort**: Trivial. Batch operation.

### Phase 3: Rename Files (Optional, Deferred)

6. **Rename files** from `CANON-31100-ACUMEN-planetary-INFORMATION.md` to `CANON-31100-Acumen.md` (or to the 6-digit scheme if adopted). The current filenames encode the entire hierarchy in the name, which is redundant with frontmatter.
7. **Batch-update `depends_on`/`requires` references** across all files using `sed` or equivalent.
8. **Regenerate `sn/` directory** — the 85 compressed copies use current IDs. Regeneration is a script run, not manual work.
9. **Update `CANON-00006` (Corpus)** — the manifest must reflect all renames.

**Effort**: Heavy but mechanical. Should be scripted and run once.

### Migration Script Pseudocode
```bash
# Phase 1: Inject metadata
for file in canon/CANON-*.md canon/*.md; do
  parse_yaml "$file"
  inject_fields tier chain celestial_type canonical_name volatility_band refresh_cadence
  split_depends_on_into requires siblings synthesizes  # needs manual mapping file
  write_yaml "$file"
done

# Phase 2: Add aliases
for file in canon/CANON-*.md; do
  add_alias "$file" "$(get_canonical_name $file)" "$(get_current_id $file)"
done

# Phase 3: Rename (optional)
for old_name new_name in migration_map.tsv; do
  mv "canon/$old_name" "canon/$new_name"
  sed -i "s/$old_id/$new_id/g" canon/*.md  # update all references
done
cd canon/sn && regenerate_sn_copies
```

---

## D. The Frontmatter Standard

### Canonical YAML Schema

Every canon file MUST have this frontmatter:

```yaml
---
# === IDENTITY ===
id: CANON-31100                    # Current numeric ID (immutable once assigned)
canonical_name: Acumen             # Human-readable shorthand (sovereign taste-gated)
aliases: [Acumen, CANON-31100]     # Obsidian wikilink resolution targets
title: "Planetary Acumen — Atmospheric Consciousness"  # Full descriptive title

# === CLASSIFICATION ===
tier: chain                        # cosmos | core | lattice | chain | archive | immune
chain: information                 # null | intelligence | information | insight | expertise | knowledge | wisdom
celestial_type: planetary          # root | planetary | ring | lunar | comet | asteroid | satellite
volatility_band: stable            # permanent | stable | moderate | dynamic
refresh_cadence: annual            # null | annual | semi-annual | quarterly | monthly

# === RELATIONSHIPS ===
parent: CANON-31000                # Single structural parent (the hierarchy)
requires:                          # True prerequisites — "read X before this makes sense"
  - CANON-31000
siblings:                          # Peer awareness — "these are my neighbors"
  - CANON-31120
  - CANON-31130
  - CANON-31140
synthesizes:                       # Children this document draws upon (for synthesis docs)
  - CANON-31110
  - CANON-31120

# === STATUS ===
status: canonical                  # canonical | draft | deprecated | archived
operational_status: partial        # operational | partial | theoretical | pilot
version: 2.0.0                    # Sole version source of truth (no body-inline versions)
created: 2025-10-15
updated: 2026-02-16
last_verified: 2026-02-20         # Date of last accuracy check

# === METADATA ===
element: air                       # null | fire | water | earth | air | quintessence
ooda_phase: observe                # null | observe | orient | decide | act | sharpen
change_velocity: quarterly         # Deprecated — replaced by refresh_cadence. Keep for migration.
volatile_sections: []              # List of section headers containing DYNAMIC data in a STABLE doc
---
```

### Key Design Decisions

**1. `depends_on` is dead.** Replaced by three fields with unambiguous semantics:
- `requires` = "read this first" (the cleaned DAG from Pass 6)
- `siblings` = "these are my peers" (the removed sibling-awareness edges)
- `synthesizes` = "I draw from these children" (the removed parent-child inversions)

**2. `parent` is NOT a relationship — it's a structural fact.** The hierarchy. One parent per file. `requires` can include the parent but doesn't have to — a child may not need to read its parent to make sense (e.g., satellite reference documents).

**3. Version: YAML only.** Body-inline version strings are purged. Version in YAML is the single source of truth. Semantic versioning (MAJOR.MINOR.PATCH).

**4. `volatile_sections`** — solves the mixed-volatility problem without splitting files. A STABLE file like Chain Matrix (21000) can flag specific sections as DYNAMIC:
```yaml
volatile_sections:
  - "Technology Maturity Percentages"
  - "Revenue Estimates"
```

**5. `operational_status` is mandatory.** No more missing fields. The five bare files get frontmatter in Phase 1.

**6. `canonical_name` enables the Bible-verse experience.** `[[Acumen]]` works in Obsidian. Agents can use the name in conversation. The number remains the machine key.

---

# PART II: TREASURE MAP

## E. The Incomplete Inventory

### By Operational Status

| Status | Count | Assessment |
|---|---|---|
| **operational** | 20 | Complete and verified — the healthy core |
| **partial** | 27 | Substantial content exists but sections missing or unvalidated |
| **theoretical** | 27 | Framework articulated but never tested in practice |
| **pilot** | 1 | CANON-30300 (Tech Stack) — schema complete, data migration pending |
| **no frontmatter** | 5 | Invisible to metadata-driven tooling |

### Files With Explicit Incomplete Markers

| File | Marker | What's Missing | Critical? | Agent-Draftable? | Effort |
|---|---|---|---|---|---|
| **00004 Evolution** | `TBD (session ongoing)` at line 189 | "Limitations Revealed" subsection in a historical arc | No — history can accrue. | Yes — but requires session data the agent may not have. | Trivial |
| **30310 Migration** | `[PLACEHOLDER FOR FOUNDER QUALITY EVALUATION]` at line 834 | Section XI "Founder Assessment" — qualitative evaluation stub | No — migration can proceed without it. | Partially — framework yes, taste-gating required for the evaluation itself. | Moderate |
| **31100 Acumen** | `[FORTHCOMING]` at line 1045 | Reference to unwritten IIC Implementation Guide supplement | No — Acumen functions without it; 31115 partially fills this role. | Yes — 31115 already exists as the de facto implementation guide. | Trivial (link to 31115) |
| **33111 Biz Enhance** | `[SECTION III TO BE WRITTEN]` (from sensing report) | Entire Section III — content enhancement specifications | Moderate — the doc exists to specify enhancements. | Yes — follows established patterns from 33110. | Moderate |

### The 27 "Partial" Files — Grouped Assessment

Most `partial` files are not incomplete in the "missing sections" sense — they're self-declared as not yet validated through practice. The status means "the framework is articulated but not yet stress-tested."

**Truly incomplete (content gaps):**
- 33111 Biz Enhance — has a literal placeholder section
- 30310 Migration — has a placeholder evaluation
- 31100 Acumen — has a forthcoming reference

**Partial because never validated:**
- All chain roots (30000, 31000, 32000) — the stage models exist but haven't been walked through all four stages
- 00005 Syncrescendence — the originary scripture is marked partial, which is philosophically appropriate (it can always deepen)
- 20000 Palace — the seven layers are defined but the practitioner hasn't operated at all seven
- Intelligence cluster (30200, 30340, 30400, 30420, 30430) — frameworks articulated, never stress-tested
- IIC cluster (31110, 31115, 31120, 31130, 31140, 31141, 31142, 31143) — designed but partially implemented

**Action**: Change the frame. "Partial" should mean "has content gaps." A framework that's articulated but unvalidated is `theoretical`, not `partial`. Reclassify the validated-but-untested files from `partial` to `theoretical`. This clears the partial queue to only files with actual holes.

### The 27 "Theoretical" Files — Triage

These are the largest group and the most honest: frameworks designed but never run.

**Lattice tier (8 files):** 20010, 20020, 21000, 21100, 22000, 23000, 24000 — the space-time geometry. These SHOULD be theoretical until the practice matures enough to validate them. No action needed.

**Intelligence (6 files):** 30100 (ASA), 30320, 30410, 30440, 30450 — reference material that was imported but never tested. The 30400 peninsula (Pass 6 finding) — five textbook chapters. **Decision needed**: should reference imports ever become `operational`, or do they stay `theoretical` by nature?

**Other chains (13 files):** 11000 Facets, 00002 Lineage, 31121/31122 (Tone), 32100/32110/32120 (Insight), 33000/33100/33112 (Expertise), 34100/34110/34120 (Knowledge), 35100/35110/35120/35121/35200/35210 (Wisdom). These represent the OODA loop's later stages — less developed because the practitioner is earlier in the journey. This is correct — they're theoretical because the practice hasn't reached them yet. No forced completion needed.

---

## F. Promotion Candidates

### From Sensing Findings → Canon Fixes (The Punchlist)

| # | Item | Source | Action | Effort |
|---|---|---|---|---|
| 1 | **5 frontmatter-free files** | Sensing IV | Add YAML frontmatter to 25500, 31150, Gate v1, Gate v2, retirement_protocol | Trivial |
| 2 | **3 stale chain H1 names** | Sensing IV | 33000: "EFFICACY" → "EXPERTISE". 34000: "EMBODIMENT" → "KNOWLEDGE". 35000: "TRANSCENDENCE" → "WISDOM" | Trivial |
| 3 | **Cost contradiction** | Sensing IV | 25200 ($100), 31150 ($160), 31142 ($100-130). Pick 31150 as source of truth (most recent, auto-generated), update others or add note. | Trivial |
| 4 | **Corpus manifest** (00006) | Sensing IV | 15 files behind (71 listed, 86 actual). Regenerate or deprecate as auto-generated. | Moderate |
| 5 | **CANON-00008 ghost link** | Sensing IV | Remove `[[CANON-00008-RESOLUTIONS-cosmos]]` from 00007 line 854 | Trivial |
| 6 | **Version number reconciliation** | Sensing IV | Kill body-inline versions in 00000, 25200, 99000. YAML version = truth. | Trivial |
| 7 | **CANON-31115 identity crisis** | Sensing IV | YAML `status: canonical` vs body "Non-Canonical". Pick one. (Recommend: make it an asteroid-tier operational supplement — acknowledge its nature.) | Trivial |
| 8 | **CANON-30460 filename** | Sensing IV | Missing chain suffix. Rename from `-comet.md` to `-comet-INTELLIGENCE.md` or leave it and let frontmatter carry the metadata. | Trivial |
| 9 | **CANON-00014 parent conflict** | Sensing IV | YAML says parent=00006, body says parent=00010. Resolve — likely 00010 is correct (Content Protocol is operationally parented). | Trivial |
| 10 | **30330/30340 duplicate YAML keys** | Sensing IV | Remove `dependencies:` field, keep `depends_on:` (or migrate both to new `requires:` field). | Trivial |

**Total punchlist effort: 8 trivial + 2 moderate = achievable in one focused session.**

### From Sources Backlog → Canon Promotion

The 606 `sovereign_review` atoms in `sources/` represent the most curated non-canon content. Without reading all 606, the promotion logic from the existing pipeline (apoptosis protocol's 5:1 ratio, ontology gate's falsifiable antigen test) should be applied. The pipeline is now operational (CC39 confirmed end-to-end execution).

**Structural gaps that sources could fill:**
- No canon document covers the **Ascertescence² meta-method** (CC28-CC40's most significant intellectual product)
- No canon document covers **prompting methodology beyond Diviner** (Oracle formula exists in memory but not canon)
- No canon document covers **the certescence vault's structure and purpose** (it's infrastructure knowledge)
- The **reviewtrospective** instrument (CC38) was formalized as a Rosetta entry but never canonized

These are sovereign taste-gate items — the content exists in session artifacts but hasn't been distilled into canon-grade prose.

---

## G. Demotion Candidates

### Proposals for Sovereign Decision

| File(s) | Current Status | Proposal | Rationale |
|---|---|---|---|
| **30410–30450** (5 files) | canonical/theoretical | **Option A**: Demote to `reference` status — acknowledge they're imported textbook material, not practiced doctrine. **Option B**: Keep canonical but add `imported: true` and `validated: false` frontmatter flags. | Created in one day, never updated, zero outbound connections. The "30400 peninsula" from Pass 6. They're useful reference but they weren't taste-gated. |
| **34120 Syllabus** | canonical/theoretical | **Reclassify as asteroid** (DYNAMIC tier). Add explicit `snapshot_date: 2025-10` and `expires: 2026-04` fields. | Self-describes as "October 2025 Tool Ecosystem." Perishable by design. |
| **31150 Platform Catalog** | no frontmatter | **Reclassify as asteroid** + add `auto_generated: true` flag. Never treat as authored canon — it's a derived artifact like `sn/`. | Self-declares "DO NOT EDIT DIRECTLY" and "TEMPORAL DATA NOTICE." |
| **33111 Biz Enhance** | canonical/partial | **Demote to `draft`** until Section III is written. | Has a literal `[TO BE WRITTEN]` placeholder. Should not be `canonical` in incomplete state. |
| **30450 Prod Frameworks** | canonical/theoretical | **Move to archive** with snapshot date. | Contains "Upcoming Releases" sections for dates already past. Historical record, not current reference. |
| **Auto-generated files policy** | — | **New policy**: auto-generated files (31150, potentially 00006) get `auto_generated: true` flag and are excluded from manual `operational_status` tracking. They're only as current as their last generation. | Solves the category confusion between authored doctrine and derived data. |

---

## H. Cross-Reference Repair Plan

### The Definitive Fix List

Ordered by blast radius (most connections affected first).

| # | Issue | Files Affected | Fix | Blast Radius |
|---|---|---|---|---|
| 1 | **`depends_on` semantic split** | ALL 81 files with YAML | Reclassify every edge as `requires`, `siblings`, or `synthesizes` using Pass 6's cleaned DAG as the starting map | Global — every file touched |
| 2 | **Version number unification** | ~60 files (all with `version: 2.0.0` batch-update) | Set YAML version to actual content version. Remove body-inline versions. | Global |
| 3 | **5 frontmatter-free files** | 25500, 31150, Gate v1, Gate v2, retirement_protocol | Add full frontmatter per Section D schema | 5 files |
| 4 | **3 stale chain H1 names** | 33000, 34000, 35000 | Fix H1 headings to match current chain names | 3 files + any downstream that quotes the H1 |
| 5 | **Cost contradiction** | 25200, 31142, 31150 | Designate 31150 as source of truth (most recent). Add `derived_from: CANON-31150` note to 25200 and 31142 cost sections, or update figures. | 3 files |
| 6 | **CANON-00006 staleness** | 00006 | Either regenerate manifest to include all 86 files, or add `auto_generated: true` flag and script the regeneration | 1 file but referenced by ~65 others |
| 7 | **00007 ghost wikilink** | 00007 | Remove `[[CANON-00008-RESOLUTIONS-cosmos]]` at line 854 | 1 file |
| 8 | **31115 identity contradiction** | 31115 | Change body text from "Non-Canonical" to match YAML `status: canonical`, OR change YAML to `status: supplement` | 1 file |
| 9 | **00014 parent conflict** | 00014 | Set YAML `parent: CANON-00010` (matches body's declaration) | 1 file |
| 10 | **30330/30340 duplicate keys** | 30330, 30340 | Remove `dependencies:` key, keep `depends_on:` (or migrate to `requires:`) | 2 files |
| 11 | **30460 filename convention** | 30460 | Either rename to include `-INTELLIGENCE` suffix or accept that frontmatter carries the metadata | 1 file |
| 12 | **25500 → 25600 reference gap** | 25500, 25600 | 25600 declares depends_on 25500, but 25500 has no frontmatter. Once 25500 gets frontmatter (Fix #3), add 25600 as a `siblings` or document the relationship. | 2 files |
| 13 | **Immune system integration** | Gate v1, Gate v2, apoptosis, retirement | Once given frontmatter (Fix #3), add inbound references from governance documents (00011 Artifact Protocol should reference the gates and death protocols) | 5 files |

### Execution Order

```
Fix #3 (frontmatter) → Fix #1 (depends_on split) → Fix #2 (versions)
→ Fix #4 (H1 names) → Fix #5 (costs) → Fix #6 (corpus)
→ Fixes #7-13 (individual repairs)
```

Fix #3 must come first — the bare files need to exist in the metadata system before they can participate in the `depends_on` split. Fix #1 is the biggest single operation and should be done as a batch alongside the new frontmatter schema (Section D) rollout.

---

## I. Connection to the Scaffold Decruft

### Current Scaffold State

The parallel decruft session has already substantially cleared the scaffold:
- `orchestration/00-ORCHESTRATION/scripts/` — **empty** (103 scripts migrated or removed)
- `orchestration/00-ORCHESTRATION/state/` — minimal (DAG tension monitor logs only)
- `corpus/` — contains decrusted scaffold artifacts (flattened paths as filenames)
- `ascertescence/` — oracle sub-directory only
- Top-level: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `Makefile` — the constitutional surface

### What Canon Changes Unblock Scaffold

| Canon Change | Scaffold Unlock |
|---|---|
| **Frontmatter standardization** (Section D) | Enables automated tooling: `make validate-canon` can check every file against the schema. Currently impossible with 5 bare files and inconsistent fields. |
| **`depends_on` → `requires`/`siblings`/`synthesizes`** | Enables automated dependency graph generation — the scaffold's `DYN-LATTICE_INDEX.json` can be rebuilt from canon frontmatter instead of maintained manually. |
| **`canonical_name` + `aliases`** | Enables Syncrescript compilation target — the compiler can use canonical names as identifiers. Also enables the Obsidian graph view to display meaningful labels. |
| **`volatility_band` + `refresh_cadence`** | Enables automated staleness detection — a script can flag files past their refresh date. Unblocks the "circadian sync" dream cycle concept from CC28. |
| **Immune system integration** (Fix #13) | Enables the ontology gate to be invoked by the pipeline — currently it exists as a document but the pipeline can't find it because it has no frontmatter and no inbound references. |

### What Scaffold Capabilities Unblock Canon

| Scaffold Capability | Canon Unlock |
|---|---|
| **`make configs` pipeline** (existing) | Already generates CLAUDE.md/GEMINI.md from AGENTS.md. Could be extended to generate Corpus manifest (00006) from canon frontmatter — solving the "15 files behind" problem permanently. |
| **Protease queue** (`protease_queue.py` from CC28 siege) | Would automate the 5:1 apoptosis ratio during promotion. Currently the death protocols are documents, not running code. |
| **State vector** (`state_vector.py` from CC28 siege) | Would auto-generate a live portal from canon frontmatter — replacing the manually-maintained Corpus manifest. |
| **SN regeneration** | Once canon IDs change (if renumbering happens), the `sn/` directory needs regeneration. This should be a scaffold script, not manual work. |
| **Atom clustering** (`atom_cluster.py`) | The 606 sovereign_review atoms need to be matched against canon gaps. The clustering script exists but hasn't been run against the promotion candidates. |

### Dependency Map

```
Canon Frontmatter Standard ──→ Scaffold: make validate-canon
                           ──→ Scaffold: auto-generate Corpus manifest
                           ──→ Scaffold: rebuild LATTICE_INDEX from frontmatter
                           ──→ Scaffold: staleness alerting

Scaffold: protease_queue   ──→ Canon: automated atom promotion
Scaffold: state_vector     ──→ Canon: live portal (replaces manual 00006)
Scaffold: atom_cluster     ──→ Canon: gap-filling from sources backlog

Neither blocks the other for immediate work:
- Canon frontmatter can be added NOW (no scaffold dependency)
- Scaffold scripts can be written NOW (using current frontmatter schema)
- The two converge when the new frontmatter schema lands and scripts adapt
```

**Bottom line**: The canon remediation (this work) and scaffold decruft (parallel session) are **convergent but non-blocking**. The frontmatter standard (Section D) is the interface contract between them. Once it lands, both sides can optimize independently.

---

*Response generated by Commander (Claude Opus 4.6). Pass 7: The Numbering Refactor + Treasure Map. CC42 Canon Remediation.*
