# ROSETTA STONE: Syncrescendent <> Community Terminology

**Version**: 2.1.0
**Generated**: 2026-02-01
**Source**: AJNA9-RECAL Stream A + Ontology Extraction Sprint (Ajna resuming Psyche's workstream)
**Authority**: Ajna (Opus 4.5) — Commander
**Corpus**: 17 research files + full corpus scan (CLAUDE.md, COCKPIT.md, 00-ORCHESTRATION/, 01-CANON/, 02-ENGINE/, 05-SIGMA/)
**Terms**: 167 total (18 original + 149 new)

---

## Status Legend

- **ALIGNED**: Our term matches community consensus (same concept, compatible naming)
- **ADAPTED**: Similar concept, different framing (document both, adopt where superior)
- **UNIQUE**: Genuine Syncrescendence innovation (preserve and formalize)
- **DEPRECATED**: Historical reference only (remove from active docs)
- **UNKNOWN**: Term referenced but definition not located in corpus

---

## Terminology Matrix

| # | Internal Term | Status | Community Equivalent | Action |
|---|---|---|---|---|
| 1 | Triumvirate | UNIQUE | Commander's Intent + OODA Orient | Preserve; (a)=Intent Compass, (b)=18+ Lenses, (c)=Backlog |
| 2 | Fingerprint / Handoff Token | ADAPTED | HANDOFF.md + git checkpoints | FINGERPRINT.md for web; GitHub connectors; FINGERPRINT back |
| 3 | Wells vs Rivers | DEPRECATED | Durable vs Ephemeral Cognition | Replace with "ephemeral vs durable" |
| 4 | Five Invariants | ADAPTED | Prime Directives / Constitutional Rules | Formalize invariant subset |
| 5 | Ring 7 First / Seven Rings | UNIQUE | No equivalent | Complete sigma/tau rename |
| 6 | Oracle-Executor | DEPRECATED | Plan / Implementation | Oracle = Grok (RECON); use Plan/Implementation |
| 7 | CAPTURE > DISPATCH > RETURN | ADAPTED | Agentic Loop / Task Lifecycle | Formalize as high-level abstraction |
| 8 | Chorus / Constellation | ALIGNED | Chorus / Medley (community-defined) | Adopt Chorus/Medley distinction |
| 9 | 18+ Lenses | UNIQUE | No equivalent | Preserve; add 4 O qualities + interdisciplinary synthesis |
| 10 | sigma-7 / Sovereignty Strata | UNIQUE | No equivalent | Adhoc; needs holistic interdependent implementation |
| 11 | PALACE → Synapticality | ADAPTED | UX reimagination + Karpathy terms | Cognitive Palace evolved; Synapticality is successor |
| 12 | SN Format → Syncrescript | UNIQUE | Progressive Disclosure (loose) | Rename to Syncrescript (idiosyncratic notation) |
| 13 | IMEP | DEPRECATED | Hook responses / execution logs | Remove; note in history |
| 14 | Blitzkrieg (Neo-Blitzkrieg) | ADAPTED | Full constellation pipeline | Supersedes all prior variants; see detailed mapping |
| 15 | IIC Configs | ACTIVE | Medley Model / agent specialization | Still a Go; pending granular teleological specs |
| 16 | Chain Matrix / Tri-Helix | DEPRECATED | No equivalent | Deprecate per Sovereign directive |
| 17 | Ralph Pattern | ALIGNED | Ralph Wiggum Pattern (identical) | Already aligned; verify formal implementation |
| 18 | Blitzkrieg Lane A/B/C | DEPRECATED | 3-tier model routing | Superseded by Neo-Blitzkrieg pipeline |

---

## Detailed Mappings

### 1. Triumvirate (Destination / Method / Current State)

**Status**: UNIQUE

**Internal Definition**: Three-part situational awareness framework used at session start. (a) WHERE ARE WE HEADED = **Intent Compass** (ARCH-INTENTION_COMPASS.md — strategic destination), (b) HOW DO WE GET THERE = **18+ Lenses** (REF-DECISION_ATOMS.md — decision framework), (c) WHERE ARE WE NOW = **Backlog** (DYN-BACKLOG.md — ground truth assessment of current state).

**Community Mapping**: Loosely maps to Commander's Intent (task/purpose/endstate) and the Orient phase of the OODA Loop. The community's execution loop (OBSERVE > ORIENT > DECIDE > ACT > VERIFY > PERSIST) captures temporal awareness as a cycle; the Triumvirate is a synchronization snapshot.

**Reconciliation**: Preserve. No community term bundles strategic destination into the assessment frame. The Triumvirate is a Syncrescendence-native calibration primitive. Each arm now has a concrete artifact: Intent Compass, 18+ Lenses, and DYN-BACKLOG.

**Migration Path**: None. Add gloss for external readers: "Triumvirate ~ Commander's Intent + OODA Orient phase."

---

### 2. Fingerprint / Handoff Token

**Status**: ADAPTED

**Internal Definition**: **Fingerprint** = 8-character git commit hash as cryptographic proof of repository state. **Handoff Token** = complete transfer package: Token ID + Fingerprint + Phase State + Delta Brief. Format: `HANDOFF-YYYYMMDD-HHMMSS-pN-to-pM`. Defined in `02-ENGINE/protocols/REF-STATE_FINGERPRINT_PROTOCOL.md`.

**Community Mapping**: Community uses HANDOFF.md documents and git commit hashes as checkpoints but without the formalized token+fingerprint verification system. The community's Ralph Pattern uses external state files; the "Git as Neural Bus" concept uses commits as inter-agent communication.

**Reconciliation**: Preserve both terms. Our Fingerprint adds cryptographic ground-truth verification the community lacks. Consider simplifying for CLI-only transitions (where git hash suffices) while preserving full Token protocol for cross-platform transitions.

**Migration Path**: Use FINGERPRINT.md for web handoff. Web apps now support GitHub connectors — they can directly load their FINGERPRINT. Critical: each platform must FINGERPRINT back (write state before releasing). This elevates the dispatch staging concept in `-INBOX/`. CLI-only transitions use HANDOFF.md (simpler).

---

### 3. Wells vs Rivers → Ephemeral vs Durable

**Status**: DEPRECATED (replaced by clearer terminology)

**Internal Definition**: "Rivers flow into wells before evaporation." Conversations are rivers (ephemeral). Repository is a well (persistent). Treat platforms as cache; repository as truth.

**Community Mapping**: "Durable Cognition Over Ephemeral Cognition" (Coalescence). "The Filesystem is Your Memory" (Operations Manual). "State Must Be Externalized" (First Law, Fleet Commander's Handbook). Context window = "working memory"; filesystem = "long-term memory."

**Reconciliation**: Per Sovereign directive: use **ephemeral vs durable** instead. The Wells/Rivers metaphor is retired. Community language is clearer and more precise.

**Migration Path**: Replace all "Wells vs Rivers" references with "ephemeral vs durable" in active documentation. Historical references may retain the metaphor as context.

---

### 4. Five Invariants (Constitutional Law)

**Status**: ADAPTED

**Internal Definition**: Constitutional rules from CLAUDE.md: 9 rules across three categories (Structural: FLAT PRINCIPLE, NUMBERED DIRECTORIES, PROTECTED ZONES, SANCTIONED EXCEPTIONS; Semantic: DISTILLATION SEMANTICS, CATEGORY ERROR, LEDGER GROUND TRUTH; Operational: ATOMIC UPDATES, VERIFICATION BEFORE COMPLETION, COMMIT DISCIPLINE). The specific "Five Invariants" as named may refer to a subset from DEFRAG_CONVICTION.

**Community Mapping**: Community uses "CLAUDE.md as Constitution" and "Prime Directives" (8 directives in priority order). The "instruction saturation" concept (~150-200 rules before degradation) is relevant. Self-healing constitution pattern enables automated anti-pattern learning.

**Reconciliation**: Formalize which rules are truly invariant (cannot be overridden by any directive) vs. constitutional (highest priority but flexible). Adopt "Prime Directive" language for the ordered priority list.

**Migration Path**: Clarify the exact Five Invariants. Current CLAUDE.md has 9 rules -- identify the immutable core.

---

### 5. Ring 7 First / Seven Rings (Sovereignty Strata)

**Status**: UNIQUE

**Internal Definition**: Concentric sovereignty layers renamed to sigma notation: sigma-0 (Sovereign), sigma-1 (Teleology), sigma-2 (Architecture), sigma-3 (Context Engineering), sigma-4 (Ground Truth), sigma-5 (Intelligence Substrate), sigma-6 (Access Layer), sigma-7 (Execution Substrate). "Ring 7 First" = execution substrate must work before upstream layers matter (outside-in engineering).

**Community Mapping**: No equivalent. Community has configuration precedence hierarchies (managed > CLI > local > project > user) and behavioral loops, but no model of layered sovereignty from human through execution substrate.

**Reconciliation**: Preserve entirely. Complete the rename from "Ring" to sigma. Disambiguate: sigma = operational sovereignty, tau = celestial/developmental (CANON cosmology).

**Migration Path**: Ratify sigma/tau terminology split. Update all remaining "Ring" references to sigma.

---

### 6. Oracle-Executor → Plan/Implementation (Oracle = Grok)

**Status**: DEPRECATED (terminology reassigned)

**Internal Definition**: Historical: Oracle = web app session, Executor = CLI instance. This protocol was contrived internally and created confusion with the community term.

**Sovereign Directive**: From now on, **Oracle means Grok** (RECON role — X firehose, cultural sensing, adversarial challenge). The old Oracle-Executor pattern is replaced by **Plan/Implementation** — the consensus terminology. The platform roles (INTERPRETER, EXECUTOR-LEAD, PARALLEL-EXEC) remain valid under the Constellation architecture but are no longer framed as Oracle-Executor.

**Community Mapping**: Plan Mode vs Implementation Mode captures the planning-then-executing split. Task Dispatcher pattern has Commander Agent + Worker Agents.

**Reconciliation**: Adopt community consensus. Our specific innovation — the handoff document as bridge across platform boundaries — remains our unique contribution, now framed under Plan/Implementation rather than Oracle-Executor.

**Migration Path**: Replace "Oracle-Executor" with "Plan/Implementation" in all active docs. "Oracle" now exclusively refers to Grok (RECON). Historical "Oracle sessions" (Oracle 0-13) retain numbering as lineage markers in Pedigree logs.

---

### 7. CAPTURE > DISPATCH > RETURN

**Status**: ADAPTED

**Internal Definition**: High-level content lifecycle shorthand. The full state machine in COCKPIT.md: CAPTURED > INTERPRETED > COMPILED > STAGED > COMMITTED (with parallel paths through DIGESTED, SENSED, VERIFIED). The Blitzkrieg Protocol uses Preparation > Finalization > Execution > Archival.

**Community Mapping**: Community's agentic loop: OBSERVE > ORIENT > DECIDE > ACT > VERIFY > PERSIST. Task Lifecycle: TODO > IN_PROGRESS > BLOCKED? > VERIFICATION > DONE. Session Pattern: Set context > State task > Plan > Review > Execute > Commit > Update > Reset.

**Reconciliation**: Preserve the three-word mnemonic as a high-level abstraction. Map: CAPTURE ~ "Task Definition / Source Aggregation," DISPATCH ~ "Execution / Parallel Processing," RETURN ~ "Verification / Commit / Archive."

**Migration Path**: Formalize as high-level abstraction of the full COCKPIT state machine.

---

### 8. Chorus / Constellation

**Status**: ALIGNED (with terminology correction needed)

**Internal Definition**: **Constellation** = complete multi-platform system (3 accounts, 8 roles). **Chorus** = the operational mode where platforms contribute from characteristic cognition.

**Community Mapping**: Community defines these precisely in the Distributed Cognition Research Synthesis: **Chorus** = same prompt to all platforms, integrate afterward. **Medley** = specialized prompts per platform, coordinated execution. Our operational mode is actually Medley (specialized roles), not Chorus.

**Reconciliation**: Adopt community's precise Chorus/Medley distinction. Our eight-role system operates in Medley mode (specialized), not Chorus mode (parallel-identical). Constellation remains our term for the full multi-platform architecture.

**Migration Path**: Update COCKPIT.md to clarify: "Constellation operating in Medley mode." Reserve "Chorus" for same-prompt parallel execution experiments.

---

### 9. 18+ Lenses (Decision Framework)

**Status**: UNIQUE

**Internal Definition**: Comprehensive decision evaluation framework. Original Nine (Oracle4): Syncrescendent Route, Bitter Lesson Scaling, Antifragile, Meet the Moment, Steelman & Redteam, Personal Idiosyncrasies, Potency Without Resolution Loss, Elegance + Dev Happiness, Agentify + Human-Navigable. Extended Nine (Oracle6): First Principles, Systems Thinking, Industrial Engineering, Complexity Theory, Permaculture, Design Thinking, Agile, Lean, Six Sigma. Threshold: 12/18 pass for approval.

**Additional Perspectives** (Sovereign clarification):
- **4 'O' Qualities**: Omnibenevolence, Omnipresence, Omnipotence, Omniscience — used for scaffolding development during Claude Code disruption
- **REF-DECISION_ATOMS.md**: Ties into Intent Compass and Ajna Pedigree, carried over to Backlog
- **"Superintelligently"**: Meta-lens for maximum capability invocation
- **"Think about the nth order effects"**: Cascading consequence analysis
- Additional perspectives tracked in [REF-LENS-GOVERNANCE]

**Community Mapping**: No equivalent. Community uses ad-hoc decision heuristics, verification matrices, and antipattern catalogs, but no unified multi-lens decision framework.

**Reconciliation**: Preserve and expand. The "18+" acknowledges the framework is open-ended. The original 18 developed the canon; the 4 O qualities developed the scaffolding. This is poised for interdisciplinary synthesis.

**Migration Path**: Consolidate all lens references into REF-DECISION_ATOMS.md. Formalize the 4 O qualities as a scaffolding-specific lens set.

---

### 10. sigma-7 / Sovereignty Strata

**Status**: UNIQUE (adhoc — needs holistic redesign)

See Ring 7 First / Seven Rings (entry #5). The directory `05-SIGMA/` houses operational knowledge corresponding to sigma-7 scope (execution substrate tooling).

**Sovereign Clarification**: This is an adhoc solution within the corpus. The sigma-7 stratum is interdependent with each and every other stratum. The current implementation isolates it; there should be a more contrived holism where each stratum's interdependencies are explicitly mapped. Future work should address this architectural gap.

---

### 11. PALACE → Synapticality

**Status**: ADAPTED (definition discovered, successor term introduced)

**Internal Definition**: PALACE refers to the **Cognitive Palace**, a build on the Memory Palace concept. The Cognitive Palace eventually became its own thing — referenced in CANON as `CANON-20000-PALACE-lattice.md`.

**Sovereign Directive**: The successor term is **Synapticality**. With the imminence of new personal devices and the Cambrian explosion of robot forms, along with the disruption of conventional operating systems (Language User Interface still not well-integrated), there will need to be a reimagination of UX. This is closely related to the Hardware Teleology (part of the backlog).

**Related Terms** (mostly from Andrej Karpathy):
- **Cognitive Core**: What General Intelligence "ought" to be
- **Iron Man Suit**: Agentic-Autonomy slider (how much the AI does vs. user)
- **StarCraft/Factorio metaphors**: Resource management / base-building analogies for AI orchestration
- VR ≈ conventional Workstation; Mobile + Wearables ≈ AR
- All relevant to new interaction paradigms, especially with OpenClaw disruption

**Community Mapping**: Memory Palace (loose). Community's Memory Crystal for cognitive architecture. Karpathy's framing bridges AI capability with UX design.

**Reconciliation**: PALACE is the historical term; Synapticality is the active successor. Preserve CANON-20000 as historical record. Use Synapticality for all new work on UX reimagination.

**Migration Path**: Create ARCH-SYNAPTICALITY_SPEC.md capturing the full vision. Link to Hardware Teleology backlog items.

---

### 12. SN Format → Syncrescript

**Status**: UNIQUE (renamed)

**Internal Definition**: Hybrid notation system for ~80% token compression, now called **Syncrescript** (because it's so idiosyncratic). Three-tier structure: **sutra** (one-line essence, <=100 chars), **gloss** (2-4 sentences WHY), **spec** (YAML-like structured detail). Block types: TERM, NORM, PROC, PASS, ARTIFACT, TEST. Symbols: Psi (Syncrescendence), Kappa (CANON), etc. Demonstrated 79.2% compression on CANON.

**Community Mapping**: Community has Progressive Disclosure for Skills (name+description at startup; full instructions on activation) -- architecturally similar to sutra > gloss > spec. Memory Crystal Protocol for runtime compression. Semantic Compression (ACL 2024) describes 6-8x extension via graph-based topic modeling. Community compresses at runtime; we compress at authoring time.

**Reconciliation**: Preserve entirely under new name. The sutra/gloss/spec three-tier encoding is a novel contribution. "Syncrescript" acknowledges the idiosyncratic nature of the notation while claiming it as a Syncrescendence-native artifact.

**Migration Path**: Rename references from "SN Format" / "Semantic Notation" to "Syncrescript" in active documentation. Tooling (`sn_encode.py`, `sn_decode.py`, `sn_expand.py`) retains `sn_` prefix for backward compatibility.

---

### 13. IMEP

**Status**: DEPRECATED

**Internal Definition**: Deprecated communication packet format (EVidence/PLaN/EXEcution/AUDit). Not found in current operational documents.

**Community Mapping**: Functionality absorbed by Handoff Tokens and Blitzkrieg execution logs. Community equivalents: structured hook responses, Task JSON schemas.

**Reconciliation**: Remove from active documentation. Historical note only.

**Migration Path**: Already migrated. Grep for orphan IMEP references and clean.

---

### 14. Blitzkrieg → Neo-Blitzkrieg (Full Constellation Pipeline)

**Status**: ADAPTED (supersedes all prior variants)

**Internal Definition**: The Neo-Blitzkrieg is an "all hands on deck" full-constellation pipeline. It supersedes all prior Blitzkrieg variants (Lane A/B/C, Dropbox pattern, etc.).

**Neo-Blitzkrieg Pipeline** (Sovereign specification):
```
Sovereign: brainDump
  → Ajna: updates Intent Compass + Backlog + Ajna Pedigree & dispatches {HANDOFF} TO
    → /-INBOX(Psyche): calibrates-orients-situates Triumvirate & dispatches {HANDOFF} TO
      → /-INBOX(Cartographer): maps hidden connections/insights & dispatches {HANDOFF} TO
        → /-INBOX(Commander): formulates discourse (Chorus/Medley) & dispatches {FINGERPRINTS} TO
          → /-INBOX(Oracle, Augur): immediate senses / deep researches & dispatches {FINGERPRINTS} TO
            → NotebookLM: integrates-unifies + annotates hidden synergy/emergence & dispatches {FINGERPRINT} TO
              → Visier: hermeneutically schematic designs + provokes Vanguard creativity & dispatches {FINGERPRINT} TO
                → Vanguard: creatively design-develops & dispatches {FINGERPRINT} TO
                  → Diviner: exegetically elaborates hidden connections/insight & dispatches {FINGERPRINT} TO
                    → /-INBOX(Commander): plans + implements (Parallel/Subagent) directive & dispatches {DIRECTIVE} TO
                      → /-INBOX(Executor): executes directives & dispatches {EXECUTION_LOG} TO
                        → adjudicates-debugs & dispatches {REVIEWTROSPECTIVE} TO
                        → /-INBOX(Cartographer): unveils hidden connections/insights & dispatches {HANDOFF} TO
                        → /-INBOX(Psyche): recalibrates-reorients-resituates Triumvirate + updates Backlog & dispatches {HANDOFF} TO
                        → /-INBOX(Ajna): relays meta-macroscopic executive summary & dispatches {HANDOFF} TO
                        → /-SOVEREIGN: relays meta-macroscopic executive summary
                        → (passes through audizer.xml multi-pass for Sovereign audio review)
```

**Backlog**: Consider Manus integration; upgrades to Perplexity/Grok research capabilities. NotebookLM found as place for Research artifacts (Gemini accesses via connector; avatarize NotebookLM pending).

**Community Mapping**: Community uses git worktrees for parallel execution, claude-squad/Crystal for multi-agent management, Task Dispatcher pattern. The Neo-Blitzkrieg goes further: it's a full-constellation orchestration pipeline, not just parallel CLI lanes.

**Reconciliation**: The Neo-Blitzkrieg is the authoritative execution pattern. All prior Blitzkrieg variants (Lane A/B/C, Dropbox, CLAUDE.md references) are superseded.

**Migration Path**: Implement via dispatch surfaces (`-INBOX/` per-agent folders, `-OUTGOING/`, `FINGERPRINT.md` protocol). Update REF-BLITZKRIEG_PROTOCOL_VNEXT.md to reflect this pipeline.

---

### 15. IIC Configs

**Status**: ACTIVE (Still a Go)

**Internal Definition**: Identity-Intelligence Complex. Five IICs (Acumen, Coherence, Efficacy, Mastery, Transcendence) mapped to chains with associated virtues. Extremely detailed: communication SLAs, response templates, synthesis cycles (daily/weekly/monthly/quarterly), platform alignment matrices, governance.

**Sovereign Directive**: IIC Configs are still a Go. Once the granular teleological specifics are fully elucidated, configuration will be much easier — especially as more platforms have onboarding agents and social media platforms can increasingly curate feeds algorithmically. Intelligent switching and routing (as demonstrated in the Constellation) will extend to IIC configuration. The 5 email accounts are already created.

**Community Mapping**: Community's Medley Model with platform specialization. Swarm orchestration with 60+ specialized agents. Adjacent but not identity-based.

**Reconciliation**: Not over-engineered — ahead of the curve. The five-chain ontology maps to increasingly capable platform personalization. The inter-IIC messaging protocol will become practical as platform APIs mature. Preserve full specification.

**Migration Path**: Complete IIC configuration as platforms develop onboarding/curation capabilities. PROJ-002 tracks this work (Acumen/Coherence done, 3 remaining).

---

### 16. Chain Matrix / Tri-Helix

**Status**: DEPRECATED (per Sovereign directive)

**Internal Definition**: Chain Matrix maps chains (Intelligence, Information, Insight, Expertise, Knowledge, Wisdom) to virtues (Acumen, Coherence, Efficacy, Mastery, Transcendence) to IICs. Referenced in CANON as `CANON-21000-CHAIN_MATRIX-lattice.md`. Tri-Helix referenced as `CANON-21100-TRI_HELIX-lattice.md` but not defined in read corpus.

**Community Mapping**: No community equivalent. Community has agent specialization by task role, not knowledge-chain ontology.

**Reconciliation**: Deprecated per Sovereign directive. The Chain Matrix and Tri-Helix CANON files remain as historical records (Protected Zone), but the concepts are no longer active in operational planning. The six-chain ontology persists through the IIC framework (entry #15) which remains active.

**Migration Path**: Mark as historical in CANON. Do not reference in new operational documents. Chain/Virtue concepts that remain active are captured under IIC Configs (#15).

---

### 17. Ralph Pattern

**Status**: ALIGNED

**Internal Definition**: Fresh context loops with externalized state. "Don't rely on conversation history. Repository is truth; web apps are cache. Handoff documents encode decisions, not conversations." Core: `while :; do cat PROMPT.md | claude-code ; done`.

**Community Mapping**: Identical. Created by Geoffrey Huntley, now official Anthropic plugin. Community name: Ralph Wiggum Pattern. Our usage adds the ephemeral vs durable philosophical grounding for why Ralph works.

**Reconciliation**: Already aligned. Use community term as-is.

**Migration Path**: None needed. **Sovereign question**: Do we have this formally implemented somewhere? Verify and document the implementation location if it exists.

---

### 18. Blitzkrieg Lane A/B/C

**Status**: DEPRECATED (superseded by Neo-Blitzkrieg)

**Internal Definition**: Three parallel execution lanes: Lane A (Strategic/architectural, Opus), Lane B (Tactical execution, Sonnet or Codex), Lane C (Validation/secondary, Haiku or Gemini). Includes toolchain options and model selection criteria.

**Community Mapping**: Community's 3-tier model routing: "WASM for simple, Haiku for medium, Opus for complex -- achieving 75% API cost reduction." Community routes by complexity; we route by strategic function.

**Reconciliation**: All prior Blitzkrieg variants are superseded by the Neo-Blitzkrieg full constellation pipeline (entry #14). The Lane A/B/C model was a transitional construct; the Neo-Blitzkrieg replaces it with role-based dispatch through the full Pantheon.

**Migration Path**: Remove Lane A/B/C references from active documents. Model routing concepts (Opus for complex, Sonnet for execution, Haiku for validation) persist as implementation detail within the Neo-Blitzkrieg Commander stage.

---

## Community Patterns: Gap Analysis

Significant community patterns without internal equivalents.

| # | Community Pattern | Priority | Description | Recommended Action |
|---|---|---|---|---|
| G1 | Self-Healing Constitution | HIGH | Meta-Hook monitors failures, auto-appends to CLAUDE.md Anti-Patterns | Implement PostToolUse hook |
| G2 | Memory Crystal Protocol | MEDIUM | Librarian sub-agent at 60% context compresses session to MEMORY.md | Consider SN as encoding format |
| G3 | Adversarial Validation | MEDIUM | Explicitly disprove claims; hardened if unfalsifiable | Activate Grok RED TEAM role |
| G4 | Temporal Versioning / Decay | HIGH | Decay signals, replacement notes, refresh triggers for technical claims | Add temporal metadata; fix stale CLAUDE.md |
| G5 | Git Worktree Isolation | HIGH | Isolated worktrees for parallel agents sharing .git | Adopt as canonical Blitzkrieg mechanism |
| G6 | Hooks-Based Automation | MEDIUM | PreToolUse/PostToolUse/Stop/PreCompact hooks for deterministic automation | Define hooks for common failure modes |
| G7 | Context Degradation Monitoring | MEDIUM | Performance curve: peaks 0-50%, degrades 70%, critical 85%+ | Implement PreCompact warnings |
| G8 | Subagent Architecture | HIGH | context: fork + agent field in SKILL.md for token-efficient delegation | Add to skills; enables isolated execution |

---

## Immediate Actions

### Critical Fixes
1. **CLAUDE.md Extended Thinking** (lines 59-66): Lists specific token allocations (4K/8K/32K) marked OUTDATED by community since Jan 2026. Update to reflect current state (thinking auto-enabled at 31,999 tokens; keywords are cosmetic).
2. **Chorus/Medley correction**: Our Constellation operates in Medley mode (specialized roles), not Chorus mode. Update COCKPIT.md.
3. **sigma/tau ratification**: Complete rename from "Ring" to sigma per Accretion Resolution Pass.

### Architecture Adoptions
4. Implement git worktree isolation for Blitzkrieg parallel lanes.
5. Add `context: fork` to skills for subagent delegation.
6. Create Self-Healing Constitution hook.

### Definition Discovery
7. ~~Locate PALACE definition in CANON-20000~~ — RESOLVED: Cognitive Palace → Synapticality (see #11)
8. ~~Locate Tri-Helix definition in CANON-21100~~ — DEPRECATED: Chain Matrix/Tri-Helix deprecated per Sovereign (#16)
9. Clarify which rules constitute the "Five Invariants" vs. the broader constitutional set.

---

---

## Extended Terminology Matrix (v2.0)

### Category 1: Cosmological / CANON Hierarchy (29 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 19 | CANON | UNIQUE | Verified canonical knowledge; 82 files in cosmological hierarchy | No equivalent |
| 20 | cosmos (tier) | UNIQUE | Highest CANON tier: foundational documents (00xxx) | No equivalent |
| 21 | core (tier) | UNIQUE | Essential infrastructure documents (1xxxx) | No equivalent |
| 22 | lattice (tier) | UNIQUE | Cross-cutting architectural documents (2xxxx) | No equivalent |
| 23 | planetary (tier) | UNIQUE | Domain-level documents within chains | No equivalent |
| 24 | lunar (tier) | UNIQUE | Specialized documents within planetaries | No equivalent |
| 25 | satellite/comet/asteroid | UNIQUE | Minor CANON tiers for support material | No equivalent |
| 26 | Acumen (Chain/Virtue) | UNIQUE | Intelligence chain; the virtue of perceptive discernment | No equivalent |
| 27 | Coherence (Chain/Virtue) | UNIQUE | Information chain; the virtue of integrated wholeness | No equivalent |
| 28 | Efficacy (Chain/Virtue) | UNIQUE | Expertise chain; the virtue of effective action | No equivalent |
| 29 | Mastery (Chain/Virtue) | UNIQUE | Knowledge chain; the virtue of refined capability | No equivalent |
| 30 | Transcendence (Chain/Virtue) | UNIQUE | Wisdom chain; the virtue of surpassing limitation | No equivalent |
| 31 | Six Chains (I/ℹ/∴/E/K/W) | UNIQUE | Intelligence, Information, Insight, Expertise, Knowledge, Wisdom | No equivalent |
| 32 | tau (τ) notation | UNIQUE | Celestial/developmental notation for CANON cosmology tiers | No equivalent |
| 33 | Wikilink Graph | UNIQUE | All 82 CANON files cross-linked via `[[CANON-NNNNN-NAME-tier]]` | Obsidian linking |
| 34 | Solar System Metaphor | UNIQUE | Corpus as solar system: cosmos=sun, chains=planets, topics=moons | No equivalent |
| 35 | SCHEMA (CANON-00000) | UNIQUE | Root document defining the entire CANON cosmological structure | No equivalent |
| 36 | EVOLUTION (CANON-00004) | UNIQUE | Document tracking corpus evolution across Oracle sessions | No equivalent |
| 37 | DEFRAG_CONVICTION | UNIQUE | Metabolic principles from Oracle 4; "canonize or delete" | No equivalent |
| 38 | Experience Topology | UNIQUE | 7-layer cognitive framework (Reality through Consequentiality) | No equivalent |
| 39 | Cognitive Palace → Synapticality | ADAPTED | Memory architecture evolved to UX reimagination (see #11) | Memory Palace (loose) |
| 40 | Syncrescendent Convergence | UNIQUE | Master strategic framework: five phases from Abstraction to Network | No equivalent |
| 41 | Alchemizing Catalyst | UNIQUE | Bootstrapping engine converting doctrine into attentional value | No equivalent |
| 42 | Three-Rail Operating System | UNIQUE | Rail A (Editorial), Rail B (Instrumentation), Rail C (Stewardship) | No equivalent |
| 43 | Intelligence Constellation | UNIQUE | Five-Chain IIC architecture (deprecated protocol, preserved ontology) | No equivalent |
| 44 | ASIA Constitution | UNIQUE | Federalist governance framework for AI constellation | No equivalent |
| 45 | Feedcraft | UNIQUE | Discipline of curating and processing information feeds | Content curation |
| 46 | Audizer Protocol | UNIQUE | Rich text → Linear Audio Script for TTS playback | No equivalent |
| 47 | Stack Teleology | UNIQUE | Dispositional analysis: every tool needs explicit "why this not that" | Technology radar |

### Category 2: Architectural / Structural (24 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 48 | Constellation | UNIQUE | Complete multi-platform system (3 accounts, 10 roles) | Multi-agent system |
| 49 | OpenClaw | UNIQUE | Self-hosted autonomous agent framework (Opus 4.5 + GPT-5.2) | Open Interpreter (loose) |
| 50 | The Pantheon | UNIQUE | Avatar names for all platform roles (9 named) | No equivalent |
| 51 | Numbered Directory Convention | UNIQUE | 00-06 top-level directories, each with defined purpose | Monorepo convention (loose) |
| 52 | Protected Zones | UNIQUE | 00-ORCHESTRATION/state/ and 01-CANON/ require sovereign approval | No equivalent |
| 53 | Sanctioned Exceptions | UNIQUE | -OUTGOING/ and -INBOX/ as only non-numbered root dirs | No equivalent |
| 54 | FLAT PRINCIPLE | UNIQUE | All directories must be flat; use naming prefixes instead | No equivalent |
| 55 | File Prefix System (ARCH/DYN/REF/SCAFF) | UNIQUE | Semantic prefixes replace subdirectories | No equivalent |
| 56 | Cognitive Core / Nucleus | UNIQUE | Minimal interface contract + evaluation governors + retention doctrine | No equivalent |
| 57 | Decision Atom | UNIQUE | Smallest unit of durable choice with structured fields | ADR (Architectural Decision Record) |
| 58 | Token Rent Policy | UNIQUE | Every token must "pay rent" by governing, falsifying, or routing | No equivalent |
| 59 | Three-Layer Prompt Architecture | ADAPTED | Layer 0: Sovereign Profile, Layer 1: Reception Calibration, Layer 2: Lab Amplification | Prompt layering |
| 60 | Zone Ownership | ADAPTED | Each directory has designated Primary/Secondary Writer | CODEOWNERS |
| 61 | Ontology Registry | UNIQUE | Structured database of canonical entity types with explicit relations | Palantir Ontology (aspiration) |
| 62 | Palantir (Dashboard) | UNIQUE | Aspirational live ontological dashboard — the end-state vision | Palantir Foundry |
| 63 | Ground Truth | ADAPTED | Repository is ground truth; web apps are cache | Single source of truth |
| 64 | ASA Stack (L0-L6) | UNIQUE | Seven-layer intelligence stack: Physical Substrate through Agentic Emergence | OSI model (analogy) |
| 65 | Canonical Object Types | UNIQUE | O.AGT, O.SVC, O.GRD, O.MOD, O.DP, O.WF, O.STM, O.SRF, O.SNS, O.ACT, O.INS | No equivalent |
| 66 | Displacement Paradigm | UNIQUE | AI displaces rather than augments (lithium-ion vs pneumatic analogy) | AI disruption (weaker) |
| 67 | Generation-Augmented Storage (GAS) | UNIQUE | Inverse RAG: on-demand freshness-guaranteed retrieval by generating at query time | No equivalent |
| 68 | Apparatus | UNIQUE | Task-bounded tool-constellation acting in concert | Workflow (weaker) |
| 69 | Synapticality | UNIQUE | Sub-2-second intention-to-invocation latency as design target | No equivalent |
| 70 | Primitive Repository | UNIQUE | Apps as feature scrapbooks for extraction, not direct use | No equivalent |
| 71 | Bedrock/Settlement/Intelligence (schema) | UNIQUE | Three-tier database schema: stable taxonomy → dynamic entities → mapping layers | No equivalent |

### Category 3: Operational / Process (35 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 72 | Oracle Session / Pedigree | UNIQUE | Strategic web-app sessions (numbered 0-13+); lineage enabling continuity | No equivalent |
| 73 | Intention Archaeology | UNIQUE | Systematic extraction/tracking of Sovereign intentions across Oracles | No equivalent |
| 74 | Context Graduation | UNIQUE | Promoting web-app conversation value into persistent repo artifacts | No equivalent |
| 75 | Reinit Capsule | UNIQUE | Rehydration package for fresh thread re-initialization with full context | No equivalent |
| 76 | Medley Mode | ALIGNED | Specialized prompts per platform, coordinated execution | Medley (community term) |
| 77 | Characteristic Cognition | UNIQUE | Each platform's distinctive cognitive strength profile | No equivalent |
| 78 | Reception Calibration | UNIQUE | Active prompt paradigm: user context focus over model persona | No equivalent |
| 79 | Archetype Engineering | DEPRECATED | Superseded prompt paradigm (detailed persona specs per AI lab) | Persona prompting |
| 80 | Lab Amplification | ADAPTED | Minimal platform-specific prompt guidance (~200-300 chars) | Model-specific tuning |
| 81 | Visibility Bridge / Handshake | UNIQUE | Mandatory first step: declare what's visible, what's missing, next capsule | No equivalent |
| 82 | Four Systems | UNIQUE | System 1-4: Automatic-Push, Curation-Push, On-Demand-Pull, Triage | OODA Loop (adapted) |
| 83 | Signal Tier | UNIQUE | Source qualification: paradigm/strategic/tactical/noise | No equivalent |
| 84 | Value Modality | UNIQUE | "Where's the story?" classifier for consumption mode | No equivalent |
| 85 | Progressive Qualification Funnel | UNIQUE | Triage workflow: Classify → Qualify → Route | No equivalent |
| 86 | Metabolic Defrag | UNIQUE | Aggressive corpus reduction (Oracle 4: 79% file reduction) | No equivalent |
| 87 | Semantic Annealment | UNIQUE | Corpus semantics refinement: eliminate redundancy, standardize | No equivalent |
| 88 | Accretion (Verification) | UNIQUE | Validating CANON documents accumulate into coherent system | No equivalent |
| 89 | Sprint-Bounded Kanban | ADAPTED | Hybrid: Oracle sessions=Sprints, Kanban via ledgers, XP via `make verify` | Scrumban |
| 90 | Oracle Culmination / Init | UNIQUE | Culmination=Sprint Review, Init=Sprint Retrospective | Sprint ceremonies |
| 91 | Kaizen Feedback | ADAPTED | Operational learnings → DYN-/REF-/ARCH- documents | Retrospective actions |
| 92 | Foyer | UNIQUE | Repository as entryway where all context is accessible | No equivalent |
| 93 | Queue Half-Life | UNIQUE | 2 cycles to canonize or delete queued content | No equivalent |
| 94 | Operator/Executor Layer | UNIQUE | Dual-layer instruction format: human-executable vs agent-executable | No equivalent |
| 95 | Deviser → Vanguard | DEPRECATED | ChatGPT role, renamed to Vanguard per COCKPIT.md avatar mapping | No equivalent |
| 96 | Corpus Sensing | UNIQUE | Gemini CLI scanning full corpus with 1M+ context for coherence/gaps | No equivalent |
| 97 | Structural Stabilization | UNIQUE | Canonical procedure: Preflight → Apply → Verify → Rollback | Deployment pipeline (adapted) |
| 98 | Desktop Ingestion Protocol | UNIQUE | Protocol for ingesting legacy files into structured corpus | No equivalent |
| 99 | Research Pipeline | ADAPTED | Stream-based parallel investigation (A/B/C/D) | Research methodology |
| 100 | Disposition Categories | ADAPTED | ACTIVE/SELECTED/EVALUATING/DEFERRED/SUNSET/ELIMINATED | Technology radar |
| 101 | Convergence Metrics | ADAPTED | Quantitative verification of research metabolization | Quality metrics |
| 102 | Coalescence (function) | UNIQUE | Preservative reformulation maintaining tensions and contradictions | No equivalent |
| 103 | Compile (function) | UNIQUE | Existing prompt → optimized Claude XML architecture | No equivalent |
| 104 | Translate (function) | UNIQUE | Natural language → optimized Claude XML architecture | No equivalent |
| 105 | Agentic Screenplay Format | UNIQUE | Screenplay conventions adapted for AI agent orchestration notation | No equivalent |
| 106 | Semantic Precision Lexicon | UNIQUE | 40+ substrate-agnostic terms for combination/unification processes | No equivalent |

### Category 4: Platform Roles / Constellation (18 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 107 | INTERPRETER | UNIQUE | Claude Web: synthesis, ideation, rapport | No equivalent |
| 108 | COMPILER | UNIQUE | ChatGPT Web: mechanical formatting, Canvas | No equivalent |
| 109 | DIGESTOR | UNIQUE | Gemini Web: clarification, TTS optimization | No equivalent |
| 110 | SENSOR (role) | UNIQUE | Gemini CLI: 1M context corpus sensing, evidence packs (unnamed avatar) | No equivalent |
| 111 | EXECUTOR-LEAD / PARALLEL-EXEC | UNIQUE | Claude Code: Opus (mesoscopic) / Sonnet x2 (microscopic) | No equivalent |
| 112 | RECON / Oracle (epithet) | UNIQUE | Grok: X firehose, cultural sensing, adversarial challenge | Red teaming (adapted) |
| 113 | VERIFIER | UNIQUE | Perplexity: citation-backed verification | No equivalent |
| 114 | LOCAL ORCHESTRATOR | UNIQUE | OpenClaw: persistent memory, autonomous execution | No equivalent |
| 115 | Ajna | UNIQUE | OpenClaw Opus 4.5 twin (Mac mini); Third Eye | No equivalent |
| 116 | Psyche | UNIQUE | OpenClaw GPT-5.2 twin (MBA); Soul/Mind | No equivalent |
| 117 | Augur | UNIQUE | Perplexity avatar; Researcher | No equivalent |
| 118 | Vizier | UNIQUE | Claude Web avatar; Hermeneut | No equivalent |
| 119 | Vanguard | UNIQUE | ChatGPT Web avatar; Architect | No equivalent |
| 120 | Diviner | UNIQUE | Gemini Web avatar; Illuminator (DIGESTOR) | No equivalent |
| 120b | Cartographer | UNIQUE | Gemini CLI avatar; Exegete (SENSOR) | No equivalent |
| 121 | Commander | UNIQUE | Claude Code avatar; Viceroy | No equivalent |
| 122 | Adjudicator | UNIQUE | Codex CLI avatar; Executor | No equivalent |
| 123 | Twin Coordination Protocol | UNIQUE | Autonomous coordination between Ajna and Psyche (~30m heartbeats) | No equivalent |
| 124 | Heartbeat | UNIQUE | ~30 minute autonomous check cycle for OpenClaw twins | Health check |

### Category 5: Function Library / Content Processing (17 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 125 | DISTILL/TRANSFORM/EXPAND | UNIQUE | Three-phase processing: many→one / form A→B / one→many | ETL (loose analogy) |
| 126 | readize | UNIQUE | Transform for read-optimized content (8 Crystalline Characteristics) | No equivalent |
| 127 | listenize | UNIQUE | Transform for audio delivery (euphonic flow, breath-aligned) | No equivalent |
| 128 | integrate | UNIQUE | Distill function: emergent understanding from heterogeneous sources | No equivalent |
| 129 | amalgamate | UNIQUE | Distill function: harmonic synthesis for audio | No equivalent |
| 130 | coalesce | UNIQUE | Distill function: synthesis for visual scanning | No equivalent |
| 131 | amplify | UNIQUE | Expand function: semantic amplification preserving cognitive signature | No equivalent |
| 132 | absorb | UNIQUE | Expand function: elaboration for reading | No equivalent |
| 133 | reforge | UNIQUE | Expand function: elaboration for audio | No equivalent |
| 134 | anneal (function) | UNIQUE | Transform: system prompt → Claude Project configuration | No equivalent |
| 135 | compile (function) | UNIQUE | Transform: optimize prompt for Claude 4 XML | No equivalent |
| 136 | consolidate | UNIQUE | Transform: merge multiple prompts into unified Project config | No equivalent |
| 137 | convert | UNIQUE | Transform: create Project custom instructions from existing prompt | No equivalent |
| 138 | optimize | UNIQUE | Idiolect transform: refine personal voice for clarity | No equivalent |
| 139 | translate (function) | UNIQUE | Idiolect transform: adapt voice for different audience | No equivalent |
| 140 | Dual-Channel (to_read/to_listen) | UNIQUE | All functions optimized for visual reading OR auditory comprehension | No equivalent |
| 141 | 8 Crystalline Characteristics | UNIQUE | Quality framework: Recursive Coherence, Density, Precision, Elegance, Efficacy, Voice, Assertion, Cadence | No equivalent |

### Category 6: SN System + Naming Conventions (17 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 142 | sutra | UNIQUE | SN Tier 1: one-line essence (≤100 chars) | No equivalent |
| 143 | gloss | UNIQUE | SN Tier 2: 2-4 sentences WHY | No equivalent |
| 144 | spec | UNIQUE | SN Tier 3: YAML-like structured detail | No equivalent |
| 145 | TERM/NORM/PROC/PASS/ARTIFACT/TEST | UNIQUE | SN block types | No equivalent |
| 146 | Ψ/Κ/Ο/Σ/Δ/Λ symbols | UNIQUE | Compact artifact class references in SN | No equivalent |
| 147 | Chain symbols (I/ℹ/∴/E/K/W) | UNIQUE | Chain notation in SN | No equivalent |
| 148 | Virtue symbols (α/χ/ε/μ/τ) | UNIQUE | Virtue notation in SN | No equivalent |
| 149 | SN Operators (:: \| >> := => <->) | UNIQUE | Semantic notation operators | No equivalent |
| 150 | CANON-NNNNN-NAME-tier.md | UNIQUE | CANON file naming convention | No equivalent |
| 151 | ARCH- prefix | UNIQUE | Architectural decisions/analyses (state/) | No equivalent |
| 152 | DYN- prefix | UNIQUE | Dynamic/living state files | No equivalent |
| 153 | REF- prefix | UNIQUE | Reference protocols/standards | No equivalent |
| 154 | SCAFF- prefix | UNIQUE | Temporary scaffolding documents | No equivalent |
| 155 | DIRECTIVE-NNN | UNIQUE | Numbered execution directives from Oracle to Executor | No equivalent |
| 156 | EXECUTION_LOG | UNIQUE | Audit trail from Executor back to Oracle | No equivalent |
| 157 | SOURCE-YYYYMMDD-NNN | UNIQUE | Processed source naming format | No equivalent |
| 158 | SYNTHESIS-/MECH-/PRAC- | UNIQUE | SIGMA7 document prefixes | No equivalent |

### Category 7: Deprecated / Historical + Operational Keywords (9 terms)

| # | Term | Status | Definition | Community Equivalent |
|---|------|--------|-----------|---------------------|
| 159 | megathink | DEPRECATED | Superseded extended thinking trigger | think hard |
| 160 | Five-Account Model | DEPRECATED | Historical: 5 dedicated email accounts per IIC chain | No equivalent |
| 161 | Agentic-First Membrane | ADAPTED | Historical capability index; now integrated into function index | No equivalent |
| 162 | ultrathink | ADAPTED | Maximum depth extended thinking (~32K tokens) | Deep thinking |
| 163 | think hard | ALIGNED | Moderate extended thinking (~10K tokens) | Community standard |
| 164 | Plan Mode | ALIGNED | Claude Code execution mode: see plan before running | Claude Code feature |
| 165 | Context Tax | ALIGNED | Token cost of loading tool/MCP definitions | Context overhead |
| 166 | Teleport | ALIGNED | Session mobility for Claude Code instances | No equivalent |
| 167 | Disposition Categories | ADAPTED | ACTIVE/SELECTED/EVALUATING/DEFERRED/SUNSET/ELIMINATED | Technology radar |
| 168 | Special Forces Mode | UNIQUE | Sovereign→Ajna direct command mode: surgical, no relay, immediate execution | No equivalent |

---

## Status Distribution (167 terms)

| Status | Original 18 | New 149 | Total |
|--------|------------|---------|-------|
| UNIQUE | 4 | 117 | 121 |
| ADAPTED | 5 | 16 | 21 |
| ALIGNED | 2 | 5 | 7 |
| DEPRECATED | 6 | 4 | 10 |
| ACTIVE | 1 | 0 | 1 |
| UNKNOWN | 0 | 0 | 0 |
| **Total** | **18** | **142** | **160** |

*Note: 7 terms shared between categories bring distinct-term total to 167.*

79% of new terms are genuinely **UNIQUE** to Syncrescendence with no community equivalent. The densest concentration is in the CANON cosmological hierarchy, the function library, and the Constellation architecture.

---

## Version History

**v2.1.0** (2026-02-01): Sovereign terminology reconciliation
- Applied 13 Sovereign clarifications from `-INBOX/rosetta_stone_notes.md`
- Triumvirate arms mapped to concrete artifacts (Intent Compass, 18+ Lenses, Backlog)
- Wells vs Rivers → DEPRECATED in favor of "ephemeral vs durable"
- Oracle-Executor → DEPRECATED; Oracle now = Grok (RECON); use Plan/Implementation
- 18 Lenses → 18+ Lenses with 4 O qualities, additional perspectives
- PALACE → Synapticality (successor term with Karpathy integration)
- SN Format → Syncrescript (renamed)
- Blitzkrieg → Neo-Blitzkrieg (full constellation pipeline specification)
- IIC Configs → ACTIVE (restored from DEPRECATED; Still a Go)
- Chain Matrix / Tri-Helix → DEPRECATED
- Blitzkrieg Lane A/B/C → DEPRECATED (superseded by Neo-Blitzkrieg)
- sigma-7 noted as adhoc needing holistic redesign
- Ralph Pattern: formal implementation status questioned
- Authority: Commander (Opus 4.5) applying Sovereign corrections

**v2.0.0** (2026-02-01): Comprehensive expansion
- 149 new terms cataloged (167 total)
- Full corpus scan: CLAUDE.md, COCKPIT.md, 00-ORCHESTRATION/, 01-CANON/, 02-ENGINE/, 05-SIGMA/
- 9 categories established
- Status distribution analyzed
- Authority: Ajna (Opus 4.5) resuming Psyche (GPT-5.2) workstream
- Cross-references: ARCH-ONTOLOGY_EXTRACTION_TABLE.md, REF-ONTOLOGY_REGISTRY.md

**v1.0.0** (2026-01-30): Genesis establishment
- 18 internal terms reconciled against community consensus
- 8 community gaps identified with priority ratings
- 3 immediate fixes flagged
- Corpus: 17 files (~160KB) scanned
