# CRUSH Phase 2 — Concept Inventory (Phase 1 Output)

**Generated**: CC62, 2026-03-01
**Scope**: All 22 corpus folders scanned — 5 via existing SUBCATEGORY-INDEX.md, 17 via subagent concept mapping
**Total corpus files**: ~5,784

---

## Macro Finding: Systematic Pipeline Misclassification

Every folder scanned shows **30-70% contamination** from bulk YouTube ingestion that routed by channel/format rather than semantic topic. Three categories of misrouted content recur everywhere:

1. **Syncrescendence operational artifacts** (TASK/CONFIRM files, scripts, session logs, CLARESCENCE passes, watchdog escalations) → should be `multi-agent-systems/`
2. **Zero-atom extraction stubs** → should be `multi-agent-systems/` per CC59 Amendment
3. **General AI news/model coverage** → scattered across folders that don't match the topic

**Implication**: Before coalescence (merging overlapping files), a reclassification pass is needed to get files into correct folders. Overlap detection across folders is unreliable when 30-60% of each folder's contents don't belong there.

---

## Per-Folder Concept Maps

### 1. ai-capability-futures (172 files) — INDEXED
- AGI timelines & predictions
- Scaling laws & trajectories
- Agent evals & capability benchmarks
- Market & investment analysis
- Democratization & open models
- Human-AI symbiosis

### 2. ai-models (556 files) — INDEXED
- Mathematical foundations
- Frontier model releases (dominant cluster, ~170 files)
- Training & scaling
- Benchmarks & evaluation
- Architecture & efficiency
- Fine-tuning & adaptation

### 3. claude-code (322 files) — INDEXED
- Core architecture
- Extended thinking & reasoning
- MCP & sub-agent integration
- Customization & skills (largest subcategory)
- Community & usage patterns
- Security & isolation

### 4. multi-agent-systems (1,755 files) — INDEXED
- External MAS research
- Syncrescendence operations (dominant — 900+ files of internal ops)
- Orchestration patterns
- MCP & protocol engineering
- Sub-agent delegation
- Architecture & frameworks

### 5. openclaw (292 files) — INDEXED
- Installation & configuration
- Memory & personality
- Phone & multi-device fleets
- Security & cost optimization
- Operational tooling
- Ecosystem & comparative analysis (largest subcategory)

### 6. ai-memory-retrieval (351 files)
- **Core (on-topic ~50-80 files)**: AI memory architectures, context engineering/RAG, persistent agent memory UX
- **Misrouted**: ~40-60 OpenClaw files (→ openclaw/), ~100-150 mixed-topic extraction atoms, ~25-40 ops artifacts
- **Cross-overlap**: PKM boundary with productivity-pkm; OpenClaw boundary with openclaw/

### 7. product-business (255 files)
- **Core**: AI market dynamics/SaaS disruption (50-70 files), enterprise AI adoption, AI business models, macro-economics
- **Misrouted**: VC investment content (→ startup-vc), OpenClaw builds (→ multi-agent-systems), quantum computing outlier, pipeline scripts
- **Cross-overlap**: startup-vc (investment), leadership-management (future-of-work)

### 8. philosophy-esoterica (235 files)
- **Core (~80-90 files)**: Consciousness/philosophy of mind (dominant, 35-45 files), philosophy of biology/evolution, cosmology/physics, integral/meta-philosophical frameworks, esotericism/sacred traditions
- **Misrouted**: ~30-50 Syncrescendence ops artifacts
- **Cross-overlap**: HIGH with meaning-civilization (civilizational-scale content), moderate with health-psychology (embodied cognition)

### 9. writing-creation (221 files)
- **Core (~80-100 files)**: Writing craft/articulation, creator economy/personal brand, AI tools for content creation
- **Misrouted**: AI model news, AI policy, philosophy, multi-agent build guides, pipeline infrastructure
- **Cross-overlap**: productivity-pkm (workflows), prompt-engineering (AI writing assistance)

### 10. vibe-coding (220 files)
- **Core (~100-130 files)**: Vibe coding critique/methodology, AI coding tool ecosystem, developer workflow patterns, career positioning, builder platforms
- **Misrouted**: ~60-80 zero-atom extraction stubs, ~40-50 pipeline .jsonl/.py artifacts, esoterica/astronomy/food science outliers
- **Cross-overlap**: claude-code (CC-specific content), product-business (economic framing)

### 11. meaning-civilization (211 files)
- **Core**: Syncrescendence CANON framework (36 files), AI capabilities/industry (~40-50), post-labor economics, civilizational transition/Big Cycle, game theory/Moloch, meaning crisis, abundance vs collapse
- **Misrouted**: ~10-15 geopolitics files, ~5-8 esoteric files, ~10-15 ops artifacts, ~15-20 AI tools/PKM files
- **Cross-overlap**: HIGH with geopolitics-grand-strategy and philosophy-esoterica

### 12. design-taste (193 files)
- **Core (~40-65 files)**: Taste as cultivable capacity (Paul Graham), designer-in-the-AI-era role transformation, AI-assisted design workflows
- **Misrouted**: ~50-70 AI industry news, ~10-20 startup/founder interviews, ~10-20 ops artifacts, consciousness/biology content
- **Cross-overlap**: vibe-coding (Direct Design), product-business (enterprise design)

### 13. productivity-pkm (191 files)
- **Core**: Personal agency/generalist mind, AI-augmented workflows, PKM methodologies (Zettelkasten/PARA), Claude Code workflow mastery, AI adoption strategy
- **Misrouted**: ~8-10 pipeline scripts (→ multi-agent-systems), enterprise SaaS disruption files (→ product-business)
- **Cross-overlap**: ai-memory-retrieval (PKM/memory boundary), writing-creation (content workflows)

### 14. health-psychology (176 files)
- **Core (~70-85 files)**: Neuroscience/cognitive science (25-30), mental health/ADHD/emotional regulation (10-15), longevity/biohacking (10-15), psychology of success
- **Misrouted**: ~25 watchdog escalation logs (11279-11306), ~20-25 AI productivity files (→ productivity-pkm), ~15-20 AI industry news
- **Cross-overlap**: philosophy-esoterica (consciousness), ai-memory-retrieval (brain-as-system)

### 15. geopolitics-grand-strategy (152 files)
- **Most severely misclassified folder (60-70% misrouted)**
- **Core (~30 files)**: US-China AI competition/chip controls, defense tech/military AI, corporate-state national security
- **Misrouted**: ~17 Syncrescendence ops artifacts, ~10-15 zero-atom stubs, ~20-30 YouTube metadata stubs on unrelated topics, meaning-economy content
- **Cross-overlap**: ai-safety (AI governance), meaning-civilization (civilizational transition)

### 16. ai-video-vfx (123 files)
- **Core (~25-30 files)**: AI video generation models (Pika, Kling, Runway, Sora, Veo), transmedia/VFX futures (John Gaeta)
- **Misrouted**: ~25-30 AI news roundups, ~15-20 agentic coding/vibe-coding files, ~10-12 corpus infrastructure indexes, ~15-20 philosophy/consciousness/transportation files
- **Cross-overlap**: ai-models (model coverage), vibe-coding (agent-augmented dev)

### 17. infrastructure (96 files)
- **Core**: Semiconductor/datacenter hardware, energy/novel computing, developer tooling
- **Misrouted**: Syncrescendence internal system infrastructure (canon files, orchestration schemas)
- **Cross-overlap**: claude-code (dev tooling), multi-agent-systems (system docs)

### 18. ai-safety (89 files)
- **Core**: AI existential risk/alignment theory, capability frontier analysis, governance/policy
- **Misrouted**: CLARESCENCE passes, canon reviews, system audits
- **Cross-overlap**: ai-capability-futures (VERY porous boundary), philosophy-esoterica (consciousness/emergence)

### 19. startup-vc (80 files)
- **Most coherent small folder**: AI-era disruption/founder playbook, VC strategy/investor frameworks, company building, startup ecosystem geography
- **Cross-overlap**: product-business (AI tooling, founder playbook), leadership-management (org design)

### 20. leadership-management (50 files)
- **Weakest folder — highest misclassification rate**
- **Core (~15-20 files)**: Organizational design, career development, leadership philosophy
- **Misrouted**: AI model releases, CS education, political commentary, Tesla operations
- **Cross-overlap**: startup-vc (remote work, org design), product-business (AI career disruption)

### 21. prompt-engineering (43 files)
- **Most coherent small folder**: Prompting philosophy/mental models, API-level techniques, agentic orchestration, workflow automation
- **Cross-overlap**: claude-code (API techniques, subagents), multi-agent-systems (orchestration), writing-creation (content automation)

### 22. ai-biotech (10 files)
- **Thin but legitimate**: Brain-computer interfaces, AI-accelerated drug discovery, biotech as AI-adjacent sector
- **Cross-overlap**: health-psychology (therapeutic BCIs), ai-capability-futures (AlphaFold/DeepMind)

---

## Species C Overlap Candidates (Cross-Folder Conceptual Overlap)

These are concepts that appear independently in 3+ folders at comparable depth — the targets for coalescence:

### 1. Post-Labor Economics / AI and Work
**Folders**: meaning-civilization, product-business, geopolitics-grand-strategy, productivity-pkm, writing-creation, health-psychology, leadership-management
**Signal**: K-shaped economy, knowledge worker displacement, post-scarcity futures, career positioning

### 2. Consciousness / Philosophy of Mind
**Folders**: philosophy-esoterica, meaning-civilization, health-psychology, ai-safety
**Signal**: Hard problem, idealism, IIT, panpsychism, brain-as-computation debate

### 3. AI Tool Ecosystem / Vibe Coding / AI-Assisted Development
**Folders**: vibe-coding, design-taste, claude-code, productivity-pkm, product-business, writing-creation
**Signal**: Cursor, Claude Code, Lovable, Bolt; vibe coding critique; AI-native workflows

### 4. Creator Economy / Personal Brand / Content Creation
**Folders**: writing-creation, productivity-pkm, product-business, design-taste
**Signal**: Dan Koe, newsletter growth, audience-first, one-person business

### 5. Civilizational Transition / Abundance vs Collapse
**Folders**: meaning-civilization, geopolitics-grand-strategy, philosophy-esoterica
**Signal**: Dalio Big Cycle, Fourth Turning, Diamandis abundance thesis, post-1945 order collapse

### 6. OpenClaw Architecture and Usage
**Folders**: openclaw, ai-memory-retrieval, health-psychology, vibe-coding, product-business
**Signal**: ClawdBot architecture, skills system, memory degradation, multi-agent management

### 7. AI Governance / Safety Policy
**Folders**: ai-safety, geopolitics-grand-strategy, meaning-civilization, ai-capability-futures
**Signal**: Chip controls, WEF debates, Amodei's "Adolescence of Technology", lab strategy

### 8. PKM / Knowledge Architecture / Second Brain
**Folders**: productivity-pkm, ai-memory-retrieval, health-psychology, writing-creation
**Signal**: Zettelkasten, PARA, agentic note-taking, Obsidian, vault design

---

## Recommended Next Steps

### Phase 1.5: Reclassification Pass (NEW — discovered during Phase 1)
Before overlap nomination, the corpus needs a targeted reclassification:
1. **Operational artifacts audit**: Sweep all 22 folders for TASK/CONFIRM/RESULT directives, zero-atom stubs, pipeline scripts, watchdog logs, CLARESCENCE passes → route to multi-agent-systems/
2. **Worst offenders first**: geopolitics-grand-strategy (60-70% misrouted), leadership-management (highest noise), health-psychology (watchdog block)
3. This is Species B work (janitorial) but it's prerequisite for reliable Species C detection

### Phase 2: Overlap Nomination (Oracle)
Stage Oracle prompt with this concept inventory. Task: identify specific file clusters of 3+ files covering the same concept at comparable depth, with content proof.

### Phase 3: Overlap Verification (Adjudicator)
Binary verdict per cluster: REDUNDANT or COMPLEMENTARY.

### Phase 4: Coalescence Pilot (Commander)
Attempt unification on verified candidates. Compare to originals.
