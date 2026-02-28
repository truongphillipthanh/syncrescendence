# Canon Remediation — Pass 7: The Numbering Refactor + Treasure Map

**Sovereign → Commander (Claude Opus 4.6)**
**Context: CC42 Canon Sensing complete. Passes 5-6 should be complete before running this pass.**

---

## Standing Context

Same as Pass 5. Additional framing:

The current 5-digit scheme (CANON-NNNNN) was inspired by Bible verse citation: precise enough to cite any fragment, flat enough to sort in a file manager. The Sovereign originally planned for each cosmos piece to receive a singular neologistic name — a heuristic shorthand (the Rosetta Stone is the ad-hoc attempt at this). The scheme should serve both machine traversal (flat, sortable) and human conversation (memorable names).

The backlog is not debt — it's treasure. The massive accumulation of content (14,025 atoms in sources, 606 sovereign_review, 86 canon files with ~30% self-declared `partial`) represents unrealized value, not technical debt. The throughput problem was organizational incoherence making content unreachable — not the content itself being worthless. Now that we're establishing coherence (canon remediation here, scaffold decruft in parallel), the question becomes: what treasure is buried, and what's the extraction plan?

---

## Objective

Two concerns combined in one pass: (1) propose a numbering scheme that serves the formalized cosmology, and (2) map the treasure — what's valuable in the accumulated content.

## Instructions

Read Passes 5 and 6 responses. Then:

### Part I: Numbering

**A. Numbering Architecture.** Propose a revised scheme. Consider:
- Maintaining Bible-verse citability (CANON-31100 → "Acumen" just as Genesis 3:16 → "the fall")
- Encoding the volatility tier in the number itself (so any agent can read the tier from the ID)
- Accommodating whatever Intelligence decomposition Pass 5 proposed (adapt to its recommendation, noting if multiple options were presented)
- Making chain membership unambiguous from the number alone
- Handling the non-CANON files (apoptosis_protocol, retirement_protocol, Ontology Gates) — they need to be first-class citizens with proper IDs
- Supporting the eventual Syncrescript compilation target (IDs must be parseable)
- Growth: the numbering scheme must not run out of slots as new chains elaborate

**B. The Neologism Registry.** For every file, propose a singular canonical name — the human-readable shorthand. These are CANDIDATES for sovereign taste-gating (you propose, the Sovereign approves). Guidelines: ideally a single word, ideally on-brand, ideally a neologism when no existing word suffices. The Rosetta Stone's existing entries are prior art — preserve what works, replace what doesn't.

**C. Migration Path.** How do we get from the current numbering to the new one without breaking every wikilink, every `depends_on` reference, every cross-reference section? Produce a migration spec: what renames, what redirects, what gets batch-updated. Account for the `sn/` directory (85 compressed copies that also use the current IDs).

**D. The Frontmatter Standard.** Define the canonical YAML frontmatter schema that every file must have. Resolve the current inconsistencies:
- `depends_on` should mean ONE thing (propose: split into `requires`, `siblings`, `synthesizes`)
- `operational_status` must be mandatory (no more missing fields)
- Version numbers: pick one source of truth (YAML or body), kill the other
- `parent` field: reconcile with `depends_on` — are they different relationships?
- Add: `volatility_tier`, `refresh_cadence`, `canonical_name` (the neologism)

### Part II: Treasure Map

**E. The Incomplete Inventory.** Every canon file with `operational_status: partial` or `theoretical` or missing — list them with a specific assessment:
- What's actually missing? (e.g., CANON-33111 has a literal `[SECTION III TO BE WRITTEN]`)
- Is the missing content critical or optional?
- Can an agent draft it, or does it require sovereign taste-gating?
- Estimated effort: trivial (metadata fix), moderate (section completion), heavy (full rewrite)

**F. The Promotion Candidates.** From the existing sources/sovereign_review backlog (606 atoms) and from the sensing findings themselves — what content SHOULD be in canon but isn't? The corpus manifest (00006) is 15 files behind. The cost figures contradict across 3 files. Three chain root H1 headings use stale names. Five files lack frontmatter. This is the punchlist.

**G. The Demotion Candidates.** Which current canon files should be reclassified? The sensing found:
- Five 304xx "textbook chapters" created in one day, never updated, all theoretical
- CANON-34120 (Syllabus) is perishable by design
- CANON-31150 (Platform Catalog) is auto-generated
- CANON-33111 has an unwritten section
Should these be demoted to a "draft" or "reference" status? Should auto-generated files have a different canon status? These are PROPOSALS for sovereign decision — present options, don't decree.

**H. The Cross-Reference Repair Plan.** Every broken link, every stale reference, every contradicting figure — produce the definitive fix list. Include the CANON-00008 ghost reference in 00007, the 3 stale chain names, the 3 contradicting cost figures, the 5 frontmatter-free files.

**I. Connection to the Scaffold Decruft.** The parallel session is cleaning the scaffold (engine/orchestration). What canon changes would unblock scaffold improvements? What scaffold capabilities (once decrusted) would enable canon maintenance that's currently impossible? Map the dependencies between the two efforts so neither blocks the other unnecessarily.

Write response to `~/Desktop/RESPONSE-CANON-REMEDIATION-PASS7.md`

---

*Prompt generated by Commander (Claude Opus 4.6), CC42 Canon Remediation.*
