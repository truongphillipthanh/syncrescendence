## BEDROCK LAYER: Constitutional Taxonomies
### Design Rationale: Constitutional Layers

**Structural Logic:** This table encodes the frequency-ordered hierarchy from your macOStaxonomy as immutable bedrock. The `altitude` field enables numeric sorting while preserving semantic layer names, allowing both human-readable navigation ("L2: Headquarters") and computational ordering (altitude 2 < altitude 4).

**The Frequency Heuristic:** `interaction_frequency` captures the original insight that most-used capabilities should surface fastest. This becomes a routing weight: L0-L2 entities receive priority in launcher fuzzy search results. The field uses categorical text rather than numeric ranges because frequency patterns are contextual (what's "daily" for one user is "weekly" for another).

**Cognitive Mode Field:** Added to enable context-aware routing. When the system detects you're in "flow" state (sustained focus, low interruption), it can prioritize L4 Mainframe tools. When detecting "reflexive" mode (rapid task switching), it surfaces L0-L1 tools. This field transforms the taxonomy from static categorization into dynamic routing intelligence.

**Data Type Choices:** All TEXT except altitude (INTEGER) because:
- Layer IDs are alphanumeric identifiers, not numbers
- Descriptions contain natural language, requiring text storage
- Categorical frequencies resist numeric quantification
- Future-proofing: text fields accommodate unanticipated values without schema changes

---

### Design Rationale: Capability Classes

**Hierarchical Navigation:** The `parent_capability_id` and `depth` fields enable SQL tree queries while preserving human-readable relationships. When you search "photo edit," the system can traverse upward (Edit → Transform) to find related capabilities or downward to discover specialized sub-capabilities. This mirrors how your brain retrieves related concepts through associative spreading activation.

**The Primitive Stability Principle:** These capability classes represent eternal transformation types, not tool-specific operations. "Generate" remains meaningful whether executed by DALL-E, Midjourney, or a future quantum diffusion model. This encoding survives the Bitter Lesson—tools change, primitives persist.

**Transformation Type Taxonomy:** The field distinguishes cognitive modes (creative/procedural/analytical/architectural/relational/autonomous) enabling context-aware routing. When the system detects you're in analytical mode (rapid document reading, cross-referencing), it can prioritize CAP_ANL capabilities over CAP_GEN.

**Intentional Sparsity:** Only two depth levels initially. This prevents premature taxonomy ossification. As you use the system, genuinely novel sub-capabilities can be added organically (e.g., CAP_GEN_IMG_3D might emerge if 3D generation becomes distinct from 2D). The structure accommodates growth without mandating it.

---

### Design Rationale: Modalities

**Cross-Layer Universality:** Modalities cut orthogonally across both constitutional layers and capability classes. A text editor in L4 Mainframe and a text generator in L1 Console both operate on MOD_TXT. This enables queries like "show all text-capable tools" regardless of which layer they inhabit.

**Computational Format Field:** Bridges human perception and machine processing. When routing a capability request, the system needs to know if the input/output requires unicode parsing, image decoding, or AST manipulation. This field enables intelligent tool selection based on technical compatibility, not just semantic capability.

**Primary Sense Mapping:** Acknowledges that modalities engage different human perceptual systems. When you're in high-visual-load contexts (multiple monitors, design work), audio-modality tools reduce interference. This field enables cognitive-load-aware routing.

**Multimodal Explicit:** Rather than implicitly assuming all tools handle multiple modalities, MOD_MUL makes cross-modal capability first-class. This prevents false negatives in searches ("find video editor" shouldn't exclude tools that also handle audio).

---

### Design Rationale: Contexts

**Orthogonal Dimensionality:** Following ASA Model principles, these five dimensions (spatial, attentional, temporal, social, risk) vary independently. You might be in a CTX_SPA_FIX + CTX_ATT_IMM + CTX_RSK_MIS context (stationary, flow state, mission-critical) which demands different tool routing than CTX_SPA_AMB + CTX_ATT_GLN + CTX_RSK_REC (mobile, glanceable, recreational).

**The Spectrum Architecture:** Rather than discrete categories, `spectrum_low` and `spectrum_high` acknowledge that contexts exist on continua. This enables fuzzy matching—a "slightly divided attention" scenario can still retrieve tools optimized for focused work, just with lower confidence scores.

**Routing Weight Potential:** These contexts become multipliers in the navigation algorithm. When the system detects CTX_SPA_AMB (perhaps via GPS + motion sensors), it can deprioritize tools requiring precision input, even if those tools technically support mobile use. Context awareness transforms capability matching from binary (can/can't) to probabilistic (optimal/suboptimal/viable/poor).

**Intentional Sparsity vs. Exhaustiveness:** This table covers the primary contextual dimensions most relevant to tool routing. It deliberately omits secondary contexts (weather, noise level, emotional state) that could be added later if usage patterns reveal their importance. Start minimal, grow through observation.

---

### Design Rationale: Feature Primitives

**The Primitive Repository Insight:** This table operationalizes your breakthrough recognition that apps are "feature scrapbooks." When you encounter a redundant text editor, instead of dismissing it, you catalog its valuable idiosyncratic features here. That editor might have worthless overall UX but possess an exceptional snippet system (FEA_SNP) worth extracting into future bespoke tools.

**Granularity Taxonomy:** The `granularity` field distinguishes:
- **Pattern**: Behavioral vocabularies (vim motions, command palettes) that can be replicated in any context
- **Feature**: Discrete capabilities (markdown preview, zen mode) that exist as bounded functionality
- **Paradigm**: Architectural approaches (WYSIWYG, plugin systems) requiring deep structural integration
- **Integration**: Connections to external systems (APIs, OAuth) requiring coordination infrastructure

This enables extraction strategy: High-granularity patterns clone easily; low-granularity paradigms require full architecture adoption.

**Extractability Gradient:** Acknowledges that some primitives transfer more readily than others:
- **High**: Can be implemented in isolation (vim motions, hotkey systems)
- **Medium**: Requires moderate integration (real-time collaboration needs synchronization infrastructure)
- **Low**: Demands extensive architecture (LSP requires language server protocols, plugin systems need runtime extensibility)

When you're deciding whether to extract a feature or use the whole app, extractability provides decision guidance.

**Category Clustering:** Groups primitives by nature (interaction, interface, capability, organization, security, collaboration) enabling discovery. When designing a bespoke tool, you can query "show all 'interaction' primitives" to see available input vocabularies.

**Strategic Coverage:** This initial set covers the patterns you've encountered across 447 apps, but intentionally omits exhaustive enumeration. As you discover genuinely novel primitives, add them. Most "new" features are compositional variations of existing primitives.

---

### Design Rationale: Entity States

**Lifecycle Visibility:** This taxonomy solves the "installed but forgotten" problem—400+ apps accumulate without clear understanding of their role. By forcing explicit state classification, you prevent zombie tools from consuming attention. When you open your launcher, you know whether something is STA_ACT (use it), STA_REP (extract features from it), or STA_DEP (delete it).

**The Repository State Legitimacy:** Making STA_REP a first-class state validates your primitive extraction workflow. Instead of feeling guilty about "redundant" tools, you can confidently maintain them as feature libraries. This mental shift transforms tool acquisition from "do I need this now?" to "does this contain extractable primitives?"

**Discovery Funnel:** The states trace a natural progression: STA_WIS (heard about it) → STA_TRL (testing it) → {STA_ACT | STA_REP | STA_DEP} (decided). This pipeline enables queue-based workflow: your discovery automation populates STA_WIS, you periodically trial items, then make binary decisions.

**Primary/Secondary Distinction:** Prevents the "too many options" paralysis. When you need a text editor, the system surfaces STA_PRI first. Only if that fails (not installed, doesn't support required format) does it offer STA_SEC alternatives. This mirrors how human memory works—strongly associated tools come to mind first, weakly associated alternatives surface only when primed.

**Maintenance Requirement Field:** Enables automated hygiene. Tools in STA_ACT state should trigger usage monitoring—if never launched in 90 days, flag for state review. STA_REP tools need periodic primitive extraction validation. STA_DEP tools get scheduled for deletion. The system can auto-maintain itself based on these lifecycle requirements.

---

### Design Rationale: Relationship Types

**Intentional Sparsity:** Following your stated principle—document only relationships that matter for routing, composition, or sequence-based workflows. This table excludes exhaustive relationship modeling (no "competes_weakly" or "similar_interface" relationships) because those don't impact navigation decisions. If a relationship doesn't change which tool the system suggests, it shouldn't exist in the schema.

**Directionality and Transitivity:** These mathematical properties enable graph traversal algorithms. If A REL_POW B and B REL_POW C, then A transitively powers C (useful for capability dependency chains). If A REL_COM B, the relationship is symmetric—both entities compete equally. This enables efficient "show me alternatives" queries without redundant relationship records.

**Routing Impact Field:** Quantifies how much each relationship type should influence navigation. REL_POW has "high" impact because you can't use a Claude-powered tool without Claude being available—this is a hard constraint. REL_CMB has "medium" impact because synergistic tools should surface together but aren't required. REL_ECO has "low" impact because shared ecosystem is a nice-to-have, not a routing determinant.

**The Powers Relationship:** Critical for AI infrastructure. When you search "generate code," the system needs to know which tools are powered by which models. If Claude is unavailable, it shouldn't suggest Cursor or Claude Code. This relationship type captures the invisible infrastructure dependencies that break navigation when violated.

**Competes vs. Alternates:** Subtle but important distinction. REL_COM means "these tools fight for the same capability niche" (Figma vs. Sketch—both UI design). REL_ALT means "these tools substitute contextually" (Vim vs. VS Code—different use contexts but both text editing). Competition influences consolidation decisions; alternation influences context-aware routing.

---

## SETTLEMENT LAYER: Dynamic Entities### Design Rationale: Entities Table

**Dynamic Settlement Architecture:** This table's records change constantly (10-50 additions monthly, per your usage patterns) while structure remains stable. The `entity_type` field uses free-form text rather than enforced taxonomy because software categories evolve faster than schema updates can track. "Agentic browser" didn't exist two years ago; it shouldn't require schema migration to catalog.

**Platform Multi-Tenancy:** The `platform` field uses underscore-delimited lists (web_desktop_mobile) because most modern tools span multiple platforms. This enables queries like "show tools available on my current device" without complex many-to-many junction tables. The tradeoff: slightly messier data format for significantly simpler queries.

**Installation Boolean:** Distinguishes aspirational tools (ENT_MID: installed=FALSE but STA_WIS) from available tools. When routing, the system should prioritize installed=TRUE entities unless explicitly searching discovery queue. This prevents suggesting tools you can't immediately invoke.

**URL as Unique Identifier Alternative:** While `entity_id` is primary key, `url` provides universal resolution. When you encounter a tool in the wild, pasting its URL into the system can auto-populate metadata by scraping or querying APIs. This reduces manual data entry friction.

**Notes Field Freedom:** Unstructured text for idiosyncratic observations that don't fit elsewhere. "Interface feels sluggish above 10k rows" or "Great for quick mockups but exports poor quality SVG." These micro-insights compound into routing wisdom over time without requiring formalized taxonomy.

---

### Design Rationale: Models Table

**Pricing as First-Class Data:** The cost fields (input/output per million tokens) enable automated cost-optimization routing. When you request "summarize this document," the system can calculate that MOD_GEM2 (free) handles it adequately versus MOD_CLS4 ($3 input) for complex reasoning. This transforms pricing from external consideration to built-in routing logic.

**Context Window Determinism:** The `context_window` field enables pre-routing validation. If you're feeding a 500k token document, the system can immediately exclude models with insufficient context rather than attempting routing and failing. This prevents frustrating "context overflow" errors.

**Modality Multi-Capability:** Text-vision-audio-video combinations (underscore-delimited) enable precise capability matching. When you request "analyze this podcast transcript and suggest visuals," only MOD_GEM2 (text_vision_audio_video) matches the requirement. Single-modality models get excluded automatically.

**Training Cutoff Awareness:** Knowledge cutoff dates enable intelligent routing based on query temporal characteristics. Questions about events after 2023-04 shouldn't route to MOD_GPT4. This prevents confident but outdated responses.

**Status Field for Lifecycle:** Models deprecate rapidly (quarterly in some ecosystems). The `status` field (active/deprecated/experimental) enables automated routing updates. When a model moves to "deprecated," the system can flag all entities powered by it for migration planning.

**NULL Handling for Non-Text Models:** Image/audio/video models lack meaningful context window or per-token pricing. NULLs preserve data integrity while acknowledging that different modality models have fundamentally different economic structures (often per-generation pricing rather than per-token).

---

### Design Rationale: Research Labs Table

**Provider Context Layer:** This table captures the organizational reality behind models. When MOD_CLS4 deprecates, knowing it comes from LAB_ANT enables queries like "show all Anthropic models" for migration planning. When pricing structures change (OpenAI moves to tiered pricing), updating one lab record cascades understanding to all associated models.

**Pricing Structure Taxonomy:** Different modalities have fundamentally different economic models. Text models charge per token, image models charge per generation, audio models charge per character, and some services operate on fixed subscriptions. The `pricing_structure` field prevents false cost comparisons—you can't meaningfully compare $3/MTok (text) with $0.08/image (generation).

**API Availability Boolean:** Some powerful tools (MOD_MID6, MOD_SUN3) lack programmatic access. When building automation workflows, the system needs to know which models support API calls versus requiring manual web interface interaction. This boolean enables automatic workflow feasibility assessment.

**Documentation URL Strategy:** Rather than caching implementation details that change frequently, this field provides canonical reference. When you're debugging why a model call failed, one click accesses current documentation without navigating corporate websites.

**Primary Modality Heuristic:** Most labs specialize despite multimodal claims. LAB_ELE does text-to-speech but their strength is audio. When you need "the best audio generation," routing prioritizes labs with audio as `primary_modality`. This field encodes implicit quality hierarchies that emerge from actual lab focus areas.

---

## INTELLIGENCE LAYER: Capability & Relationship Mapping### Design Rationale: Capabilities Table

**Hierarchical Linguistic Evolution:** This table grows organically through observed usage patterns rather than prescribed completeness. When you search "edit python" and the system finds no match, it suggests creating CAP_PYEDT under CAP_CDEDT. Over time, the hierarchy emerges from actual navigation needs rather than theoretical categorization.

**Synonyms as Navigation Keys:** The `synonyms` field (pipe-delimited) enables fuzzy matching without complex NLP. When you type "bg removal," the system finds CAP_BGRM through synonym matching. This acknowledges that humans describe the same capability many ways—the system should adapt to your language, not force you to learn its terminology.

**Depth Limitations:** The sample shows depth 0-2, but the structure supports arbitrary nesting. However, practical navigation rarely needs more than 3-4 levels. "Python Django REST API editing" is overly specific—most users think "Python editing" then filter by framework separately. The depth field enables depth-limited queries ("show only top-level capabilities") when browsing versus deep specificity when routing.

**Capability Class Reference:** The `capability_class_id` links back to T0_CAPABILITY_CLASSES, enabling type-based filtering. "Show all CAP_GEN capabilities" returns everything that creates content, regardless of hierarchy position. This orthogonal classification (hierarchy + type) enables both drill-down and cross-cutting queries.

**Sparse Documentation Principle:** Most capabilities lack detailed descriptions because the hierarchy + synonyms provide sufficient semantic clarity. "Image Generate → Photo Generate" is self-explanatory. Reserve descriptions for genuinely ambiguous cases where linguistic parsing fails.

---

### Design Rationale: Entity-Capabilities Junction

**The Navigation Core:** This many-to-many table is where thought-speed routing actually happens. When you invoke "python edit," the system queries this table for {capability_id='CAP_PYEDT', proficiency='expert', installed=TRUE} and returns ENT_CUR or ENT_CLO. This is the membrane—biological intention ("edit python") translates directly to computational invocation without conscious tool selection.

**Proficiency Gradient:** Three levels (basic/intermediate/expert) acknowledge that tools serve capabilities unequally. ENT_RAY has basic note-taking (quick capture only) while ENT_NOT has expert-level capability. When routing, proficiency becomes a ranking weight—expert matches surface first, basic matches only when no better options exist.

**Context Suitability Field:** Maps to your T0_CONTEXTS table. ENT_VIM suits "any" context (lightweight, fast startup) while ENT_CUR needs "focused" context (requires sustained attention for AI interaction). When the system detects you're in CTX_ATT_GLN (glanceable attention), it deprioritizes tools marked "focused" even if they're technically capable.

**Cost Efficiency Heuristic:** Relates to both monetary cost (for API-powered tools) and cognitive cost (setup friction, learning curve). ENT_MID is "low" cost efficiency—expensive and Discord-based, but produces exceptional results. When optimizing for speed over quality, the system routes to "high" efficiency alternatives.

**Notes as Routing Wisdom:** Unstructured observations compound into routing intelligence. "Best for sustained coding sessions" becomes a temporal pattern detector—if you've been coding for 2+ hours, prioritize ENT_CUR. These micro-insights can't be formalized into rigid fields but contribute to emergent routing quality.

---

### Design Rationale: Entity-Features Junction

**Primitive Repository Operationalization:** This table transforms the "apps as feature scrapbooks" insight into actionable data. When you determine ENT_VIM exists primarily to study its modal keybinding system (FEA_HOT: extraction_priority=medium, extraction_status=documented), you're explicitly tracking extraction targets. This prevents feature-rich "redundant" apps from being deleted before their primitives are cataloged.

**Extraction Status Workflow:** Five states trace the extraction lifecycle:
- **no_need**: Feature exists in actively-used tools (ENT_CUR has FEA_VIM, don't need to extract from elsewhere)
- **wishlist**: Feature doesn't exist anywhere but is desired (ENT_MID lacks FEA_API)
- **documented**: Implementation studied and notes captured for future replication
- **extracted**: Feature successfully reproduced in bespoke tool or alternative
- **considering**: Under evaluation for extraction worthiness

This pipeline enables systematic primitive harvesting without overwhelming yourself with extraction work.

**Implementation Quality Gradient:** Acknowledges that features vary in execution quality. ENT_OBS has "excellent" backlinks (FEA_BCK) worth cloning, while ENT_NOT has "good" backlinks (adequate but not reference-quality). When deciding which implementation to study for extraction, quality rankings provide guidance.

**Extraction Priority Strategy:** Balances feature desirability against extraction complexity. High-priority features (like ENT_FIG's real-time collaboration) justify significant extraction investment. Low-priority features (like ENT_CUR's hotkeys) can rely on existing implementations without replication effort.

**Notes as Implementation Insights:** Captures nuanced observations that guide extraction. "Local-first architecture is instructive" (ENT_OBS + FEA_OFF) suggests studying the architectural pattern, not just the feature surface. These micro-analyses compound into deep understanding of what makes features worth preserving.

---

### Design Rationale: Relationships Table

**Intentional Relationship Constraint:** This table documents only relationships that affect routing, consolidation decisions, or workflow planning. The absence of exhaustive relationship mapping (every possible connection) prevents maintenance burden. When two entities have no meaningful relationship for navigation purposes, they shouldn't have a record here—even if they're conceptually related.

**Strength and Confidence Separation:** `strength` measures relationship intensity (critical/strong/medium/weak), while `confidence` measures certainty of the relationship's existence (high/medium/low). A REL_POW relationship is always "critical" strength (can't use tool without powered model), but confidence might be "medium" if you're inferring rather than confirming the relationship from documentation.

**Discovered Date Tracking:** Enables temporal analysis of ecosystem evolution. When did ENT_CUR obsolete ENT_VSC (REL_OBS)? Understanding adoption timelines helps predict future obsolescence patterns. This field also supports automated relationship validation—if a relationship hasn't been confirmed in 2+ years, flag for verification.

**Bidirectional vs. Unidirectional:** REL_POW and REL_REQ are directional (source powers/requires target), while REL_COM and REL_CMB are symmetric (both entities relate equally). The schema doesn't enforce symmetric duplication—when you record ENT_NOT REL_COM ENT_OBS, the reverse is implied. This prevents redundant records while maintaining query simplicity.

**Notes as Relationship Context:** Captures nuanced relationship characteristics that don't fit rigid fields. "Can use together—Cursor for GUI and Claude Code for CLI" (ENT_CUR + ENT_CLO + REL_CMB) explains a non-obvious synergy. These observations guide apparatus formation—if you frequently use both together, the system can suggest formalizing that pattern.

---

### Design Rationale: Usage Log

**Passive Intelligence Gathering:** This table populates automatically through system integrations (Raycast hooks, macOS application events, browser history APIs). The goal is zero-friction data capture—you shouldn't need to manually log usage. The system observes and learns from your actual behavior rather than requiring explicit instruction.

**Context Triad Capture:** The three context fields (spatial/attentional/temporal) map to your T0_CONTEXTS taxonomy. By logging context alongside usage, the system learns contextual routing patterns. If ENT_OBS launches consistently with {situated, glanceable, reactive} contexts, future detection of that context pattern can proactively suggest Obsidian.

**Duration as Engagement Signal:** `duration_seconds` distinguishes meaningful engagement from brief touches. LOG_001 (ENT_CUR, 7245 seconds = 2 hours) signals deep work; LOG_004 (ENT_CLO, 423 seconds = 7 minutes) signals quick task. Long durations increase entity routing priority; short durations might indicate friction or suboptimal tool selection.

**Trigger Method Intelligence:** Captures *how* you invoked the tool (keyboard_shortcut, launcher, terminal_command, browser_tab, mobile_app, window_switch). This reveals navigation preferences—if you always launch ENT_FIG via keyboard shortcut, that becomes the default invocation method. If you access ENT_NOT via browser_tab, the system knows it's web-based.

**Success Boolean for Learning:** FALSE entries indicate failed invocations (app crashed, didn't have required capability, wrong tool selected). These failure patterns inform routing improvements. If you frequently launch ENT_X for capability Y but success=FALSE, the system learns X doesn't actually serve Y well despite nominal capability matching.

**Notes for Pattern Discovery:** Unstructured observations captured automatically or manually. "Morning coding session on React project" reveals temporal patterns (morning = coding) and project associations (React = ENT_CUR). Over weeks, these patterns crystallize into apparatus candidates.

---

### Design Rationale: Apparatus Table

**Emergent Pattern Recognition:** This table doesn't store prescribed workflows—it crystallizes patterns automatically detected from T3_USAGE_LOG analysis. When the nightly processing identifies that you launch ENT_RAY→ENT_CUR→ENT_NOT→ENT_GPT between 08:00-11:00 on 5+ days per week, it creates APP_MORN_CODE. This is observational intelligence, not prescriptive workflow engineering.

**Entity Sequence as Invocation Chain:** The `entity_sequence` field (arrow-delimited) enables one-click apparatus launching. Rather than manually invoking four separate tools, you trigger "Morning Coding Flow" and the system launches all components in sequence. This reduces invocation latency from 4× (individual launches) to 1× (apparatus launch).

**Trigger Context as Pattern Signature:** The `trigger_context` field (pipe-delimited key:value pairs) defines when apparatus should auto-suggest. When the system detects {temporal:08:00-11:00, attentional:focused}, it can proactively offer "Launch Morning Coding Flow?" This transforms apparatus from manual macros into context-aware automation.

**Confidence and Status Lifecycle:** `confidence` measures pattern stability (high = occurs consistently, low = emerging pattern). `status` tracks apparatus utility (active = regularly used, trial = testing usefulness, deprecated = pattern no longer occurs). Low-confidence apparatus might represent temporary project-specific workflows; high-confidence apparatus reflect stable work patterns worth optimizing.

**Frequency for Priority Ranking:** `frequency_weekly` enables apparatus prioritization. When multiple apparatus match current context, the system surfaces the most-frequently-used pattern first. This acknowledges that some workflows are daily essentials (APP_TERM_FIX: 8×/week) while others are occasional activities (APP_CNCPT_GEN: 1×/week).

**Temporal Evolution Tracking:** `first_observed` and `last_observed` dates reveal workflow evolution. If an apparatus hasn't occurred in months, it might be deprecated. If a pattern emerges suddenly with high frequency, it might represent a new project phase worth formalizing into optimized tooling.

---

### Design Rationale: Evolution Tracker

**Automated Staleness Detection:** This table populates nightly through automated version checking (GitHub API, RSS feeds, package managers, scraping changelog pages). The `days_since_update` and `update_frequency_days` fields enable staleness signals—if ENT_OBS hasn't updated in 57 days but typically updates every 60 days, it's current. If ENT_MID hasn't updated in 27 days but typically updates every 90 days, it's normal. However, if a tool shows 300+ days with no updates, it might be abandoned.

**Momentum Signal Calculation:** The `momentum` field (rising/stable/declining) synthesizes multiple signals:
- Update frequency acceleration/deceleration
- Community activity (GitHub stars, Discord engagement)
- Download/usage statistics where available
- Competitive landscape changes (new alternatives emerging)

This becomes a routing weight—declining tools receive lower priority even if technically capable, while rising tools get boosted attention. Momentum predicts future viability.

**Status Signal for Lifecycle:** Tracks entity health beyond simple version numbers:
- **active**: Regular updates and community engagement
- **maintenance**: Infrequent updates but stable
- **deprecated**: Official end-of-life announced
- **abandoned**: No updates for extended period
- **unreleased**: Future entity (like MOD_CLS4 in the sample)
- **anticipated**: Upcoming releases generating attention

This enables proactive migration planning. When a tool moves to "deprecated," the system can suggest alternatives before functionality breaks.

**Changelog URL for Context:** Rather than caching release notes (which become stale), this field provides direct access to authoritative update information. When the system detects a new version, you can one-click to understand what changed before deciding to update.

**NA Handling for Web Services:** Some entities (ENT_FIG, ENT_GPT) don't have traditional version numbers because they're continuously deployed web services. Using "NA" for version while tracking `release_date` acknowledges this reality. The `days_since_update` still provides meaningful staleness signals based on changelog announcements.

---

### Design Rationale: Discovery Queue

**Automated Weak Signal Detection:** This table populates through nightly scraping of Product Hunt launches, Hacker News front page, subreddit monitors (r/SideProject, r/InternetIsBeautiful), AI newsletters, Twitter lists, and LinkedIn follows. The system casts a wide net for potentially relevant tools, then uses filtering heuristics (upvote counts, comment sentiment, category matching) to populate the queue with signal, not noise.

**Similar_to Field for Context:** References existing entities to provide mental anchors. "DIS_001 is similar to ENT_CUR" immediately contextualizes Windsurf without lengthy explanation. This field also enables comparative routing—if you're evaluating Cursor alternatives, querying {similar_to='ENT_CUR'} surfaces competitors.

**Trial Priority as Decision Aid:** Three levels (high/medium/low) help manage attention allocation. High-priority discoveries (DIS_001: Windsurf—direct Cursor competitor with rising momentum) deserve immediate trial. Low-priority discoveries (DIS_006: Hologram—interesting but premature) can defer until later. This prevents discovery overwhelm while ensuring critical tools aren't missed.

**Decision State Tracking:** Five outcomes:
- **trial**: Added to evaluation queue (will test actively)
- **wishlist**: Interesting but not yet actionable (will revisit later)
- **adopted**: Trialed and added to T1_ENTITIES as STA_ACT or STA_REP
- **declined**: Evaluated and rejected (captures negative signals)
- **NULL**: Not yet decided (initial state)

The system can auto-generate a morning digest: "3 new high-priority discoveries require decision, 7 trials in progress, 2 wishlist items now available."

**Momentum Signal for Timing:** Tools in "rising" momentum might be worth early adoption before ecosystem lock-in. Tools in "emerging" momentum might be too unstable. Tools in "declining" momentum should probably be skipped. This field prevents wasting time on dead-end tools.

---

### Design Rationale: Ecosystems Table

**Lock-in as Routing Factor:** The `platform_lock_in` field (low/medium/high) influences consolidation decisions. ECO_APL (high lock-in) means migrating away from Apple's ecosystem is painful—this affects whether you adopt new Apple-ecosystem tools. ECO_ANT (low lock-in) means switching away from Claude is relatively easy—this reduces adoption risk. Lock-in isn't inherently bad; it's a tradeoff to evaluate.

**Auth Integration as Friction Metric:** The `auth_integration` field captures authentication patterns. ECO_GGL (oauth2) enables seamless single sign-on across many third-party tools. ECO_NTN (notion_auth) requires separate credential management. When evaluating new tools, knowing their authentication approach predicts onboarding friction.

**Data Portability Reality:** The `data_portability` field (high/medium/low) acknowledges export/import realities. ECO_GGL (high) allows easy data extraction. ECO_ADB (low) makes it difficult to leave Creative Cloud. This field informs investment decisions—committing to low-portability ecosystems creates future migration costs.

**API Maturity for Automation:** The `api_maturity` field (mature/limited/none) predicts automation potential. ECO_ANT (mature) enables sophisticated workflows through well-documented APIs. ECO_FIG (limited) restricts programmatic access. When designing apparatus or agent-based workflows, this field determines feasibility.

**Core Value Prop as Selection Heuristic:** The brief `core_value_prop` captures each ecosystem's essential advantage. When choosing between ecosystems for a capability, this field provides decision criteria. Need enterprise compatibility? ECO_MSF. Need device handoff? ECO_APL. Need constitutional AI? ECO_ANT.

---

### Design Rationale: Stacks Table

**Technology Weather Systems:** Stacks represent compositional patterns that shift with technological paradigms. Unlike ecosystems (which are organizational constants) or capabilities (which are transformation primitives), stacks describe *how* components combine for specific outcomes. STK_JAM emerged when serverless became viable; STK_LNG appeared when LLMs needed orchestration. These patterns have predictable lifecycles.

**Adoption Trend as Timing Signal:** The `adoption_trend` field (rising/stable/declining) guides investment decisions. STK_NEXT (rising) suggests learning Next.js will pay dividends. STK_MERN (stable) indicates mature but not growing. A hypothetical "declining" stack (like LAMP) suggests avoiding new investment. This field prevents learning obsolete patterns.

**Learning Curve as Friction Estimate:** The `learning_curve` field (low/medium/high) predicts adoption effort. STK_CLDA (low) means Claude agentic development is accessible quickly. STK_DVNC (high) means DaVinci video editing requires substantial investment. When deciding between functionally equivalent stacks, learning curve becomes a tiebreaker.

**Maturity vs. Trend Tension:** The `maturity` and `adoption_trend` combination reveals interesting patterns. STK_RAG (mature + rising) suggests proven and growing—safe investment. STK_LNG (emerging + rising) suggests experimental but promising—higher risk, higher potential. STK_ADBC (mature + stable) suggests established but plateaued—reliable but not innovative.

**Components as Discovery Links:** The pipe-delimited `components` field enables reverse lookup. When you learn about a new tool like "Weights & Biases," querying which stacks contain it reveals STK_PYLL, providing immediate context about typical usage patterns. This field connects individual tools to compositional patterns.

---

## FINAL INTEGRATION & AUTOMATION TABLES### Design Rationale: Automation Config

**Tunable Intelligence Parameters:** This table externalizes all system behavior thresholds, enabling continuous optimization without code changes. CFG_LAT_MAX (2 seconds maximum routing latency) directly encodes your synapticality requirement—if invocation exceeds 2 seconds, the system is failing its core purpose. These aren't arbitrary defaults; each parameter represents a falsifiable performance claim.

**Schedule vs. Threshold Distinction:** The `config_type` field separates temporal scheduling (how often tasks run) from decision thresholds (when conditions trigger actions). CFG_RSS_FREQ (schedule) determines polling frequency; CFG_STL_THR (threshold) determines staleness flagging. This separation enables independent tuning—you might increase RSS checking frequency without changing staleness thresholds.

**The Critical Latency Constraint:** CFG_LAT_MAX (2 seconds) embodies your core architectural requirement. Human working memory operates on ~2-second loops; exceeding this breaks cognitive flow. If Raycast fuzzy search + capability matching + entity retrieval exceeds this budget, the system needs architectural optimization (caching, pre-computation, query simplification).

**Apparatus Crystallization Logic:** Three parameters govern pattern detection: CFG_APP_MIN (3 occurrences), CFG_APP_WIN (30 days), and CFG_APP_THR (pattern confidence). A sequence appearing 3× within 30 days qualifies as apparatus candidate. This prevents noise (random coincidences) while catching genuine patterns quickly enough to be useful.

**Discovery Rate Limiting:** CFG_DIS_LIM (10 entities/day) prevents discovery overwhelm. The automation could surface 50+ new tools daily, but that creates decision paralysis. Ten discoveries enables deliberate evaluation without cognitive flooding. This acknowledges that tool adoption is cognitively expensive—information gathering should throttle to match decision-making capacity.

---

### Design Rationale: View Definitions

**Pre-Configured Analytical Lenses:** Rather than forcing users to construct complex queries manually, this table defines the most common access patterns as named views. VIEW_CAP (capability navigator) implements "what can do X?" queries. VIEW_CTX (context router) implements "what's optimal for my current situation?" This reduces cognitive load from query construction to view selection.

**Query Type Taxonomy:** Three categories reveal intent:
- **lookup**: Direct retrieval ("show me PDF editors")
- **analysis**: Pattern exploration ("which tools are declining?")
- **planning**: Decision support ("what features should I extract?")
- **monitoring**: Automated surveillance ("what needs replacement?")

Different query types suggest different interface paradigms—lookup benefits from instant search, analysis from dashboards, planning from kanban boards, monitoring from alert systems.

**Base Tables as Complexity Guide:** The `base_tables` field (pipe-delimited) reveals query complexity. VIEW_CAP joins three tables; VIEW_USG queries one table. Simple views can support sub-second latency; complex views might need pre-computation or caching. This field guides performance optimization priorities.

**The Critical Views:** Two views implement your core synapticality requirement:
- VIEW_CAP: Biological intention ("edit python") → computational invocation (ENT_CUR)
- VIEW_CTX: Context detection (fixed + focused + sustained) → optimal routing (ENT_CUR over ENT_VIM)

If these views don't execute in <2 seconds, the entire system fails its purpose. All other views are analytical conveniences; these two are architectural essentials.

**Sort Logic as Default Ranking:** Rather than returning unordered results, each view specifies intelligent sorting. VIEW_CAP sorts by proficiency DESC (expert matches first), then context_suitability (contextually appropriate before generic). This encoding transforms raw data into actionable recommendations without requiring explicit ranking logic at query time.

---

## COMPREHENSIVE SCHEMA SUMMARY### Design Rationale: Schema Summary

**Maintenance Burden Realism:** The `maintenance_burden` field acknowledges implementation costs. T3_ENTITY_FEATURES (high burden) requires manual primitive documentation—this is labor-intensive. T3_USAGE_LOG (none burden) populates automatically. This transparency prevents underestimating ongoing effort. The schema as designed demands ~2-3 hours weekly manual work (updating entity capabilities, documenting features) plus initial 20-30 hour classification effort.

**Critical Path Identification:** The `critical_for_routing` boolean isolates tables essential for thought-speed navigation. Seven tables marked TRUE represent the minimal viable system—without these, core routing fails. The remaining fifteen tables enhance intelligence but aren't architectural dependencies. This enables phased implementation: build critical tables first, add intelligence layers iteratively.

**Update Frequency as Staleness Signal:** The `update_frequency` field predicts when tables diverge from reality. T1_ENTITIES (daily) grows stale within 48 hours as new tools launch. T0_CONSTITUTIONAL_LAYERS (rare) remains accurate for months. This informs automated validation: nightly checks for high-frequency tables, monthly audits for low-frequency tables.

**Record Count Estimates:** The count projections reveal scalability requirements. T3_USAGE_LOG (unlimited) demands different database architecture than T0_RELATIONSHIP_TYPES (9 records). Initial implementation might use spreadsheets for bedrock tables, but tracking tables require proper database infrastructure (PostgreSQL, SQLite) to handle growth without performance degradation.

**The Automation Reality:** Five tables marked "automatic" in update frequency represent zero-maintenance components *if* automation infrastructure exists. Without proper RSS feeds, version checking scripts, and usage logging hooks, these tables revert to manual—transforming "none" maintenance burden into "high." The automation investment (10-20 hours setup) determines whether the system self-sustains or becomes a time sink.

---

### Design Rationale: Implementation Roadmap

**The Critical Dependency Chain:** Phase sequencing follows strict logical dependencies. PH3 (capability mapping) requires PH1 (taxonomy) and PH2 (entities)—you can't map capabilities without entities to map. PH6 (usage tracking) must precede PH9 (apparatus detection)—you can't detect patterns without data. This ordering isn't flexible; attempting out-of-sequence implementation causes cascading failures.

**Risk Level Honesty:** Three phases marked "high risk" (PH6, PH8, PH9) involve technical integration with external systems. PH6 (usage tracking) requires macOS system hooks—these break with OS updates. PH8 (evolution automation) depends on third-party APIs—these change without notice. PH9 (apparatus detection) needs pattern recognition algorithms—these might fail to find meaningful patterns. These aren't speculative risks; they're predictable failure modes.

**Duration Realism:** The ranges (8-12 hours, 10-15 hours) acknowledge variable implementation speed. PH2 might take 6 hours if your Function.csv imports cleanly, or 10 hours if data cleaning is needed. PH7 (feature documentation) might take 15 hours if you document systematically, or 25 hours if you rabbit-hole into deep feature analysis. Total estimated effort: 85-150 hours. This isn't a weekend project.

**The Latency Obsession:** PH4 (launcher integration) has one success criterion: "Sub-2-second invocation latency achieved." This is pass/fail. If capability search + entity retrieval + launcher launch exceeds 2 seconds, the system fails its core purpose regardless of how sophisticated the intelligence layers become. Every subsequent phase must maintain this performance constraint as the system grows.

**Phase 12 Reality:** "Continuous Optimization" with "Ongoing" duration acknowledges that this system requires perpetual attention. Taxonomies need linguistic evolution. Relationships need validation. Thresholds need tuning. Discovery feeds need curation. The automation reduces burden from constant manual updates to periodic strategic adjustments, but zero maintenance is impossible. This is a living system, not a one-time deployment.

---

## CRITICAL DESIGN SUBSTANTIATIONNow let me create a final comprehensive summary document:## Summary

I've produced a complete implementation-ready architecture for your cognitive substrate navigation system. Here's what you received:

**17 CSV tables** with explicit data types, sample records, and field specifications covering:
- Stable taxonomies (7 bedrock tables defining what kinds of things can exist)
- Dynamic entities (3 tables for your actual apps, models, and providers)
- Intelligence layers (4 tables for capabilities, ecosystems, apparatus, and stacks)  
- Tracking systems (5 tables for relationships, usage, evolution, discovery, and feature extraction)
- System infrastructure (3 tables for automation config, views, and schema documentation)

**5 markdown documents** providing:
- Comprehensive design rationale for each table
- Critical assessment of architectural choices
- Honest implementation roadmap with realistic effort estimates
- Explicit discussion of limitations, tradeoffs, and failure modes
- Alternative paths forward if full implementation seems excessive

## What This Architecture Actually Achieves

The design successfully operationalizes your core insights:
- Apps as primitive repositories (via T3_ENTITY_FEATURES extraction tracking)
- Stable taxonomies supporting dynamic entities (bedrock/settlement distinction)
- Intelligence through observation rather than prescription (automated apparatus detection)
- The Bitter Lesson applied (encode primitives and relationships, not tool-specific knowledge)

The system could genuinely enable thought-speed navigation if implemented fully. The capability-based routing + context-aware selection + automated pattern detection represents a coherent path toward synapticality.

## What This Architecture Doesn't Solve

However, several critical gaps deserve honest acknowledgment:

**Implementation complexity is substantial.** The realistic effort estimate is 150-200 hours over 2-3 months, not the optimistic 85-150 hours. This includes significant technical work that the schema specifications don't fully address—actual automation scripts, pattern recognition algorithms, query optimization, and performance engineering.

**The cold start problem is real.** The system provides minimal value for the first 4-8 weeks while usage data accumulates. You'll invest substantial effort before experiencing the promised synapticality benefits. This creates adoption friction that could lead to abandonment.

**Ongoing maintenance is required.** Despite automation, expect monthly debugging sessions (2-4 hours) as APIs break, feeds fail, and OS updates disrupt logging hooks. The "self-maintaining" promise is overstated—entropy requires continuous intervention.

**The underlying assumption might be wrong.** This entire architecture assumes tool selection latency is your primary productivity constraint. For most people, it isn't. Task prioritization, focus capacity, and decision-making clarity typically matter more than reflexive tool invocation. Building sophisticated navigation infrastructure doesn't help if that's not actually your bottleneck.

## Recommendations

Given the implementation complexity and uncertain value proposition, I'd suggest starting with the **Minimal Viable Implementation** outlined in the guide:

1. Build only capability navigation (T0_CAPABILITIES + T1_ENTITIES + T3_ENTITY_CAPABILITIES)
2. Skip all automation—manually curate your top 50 most-used tools
3. Implement just the core routing view (VIEW_CAP)
4. Test for 2 months

Effort: 30-40 hours. Value: 60-70% of full system. Maintenance: minimal.

This tests whether capability-based routing actually improves your workflow before committing to full automation infrastructure. If the minimal version proves valuable, expand incrementally based on empirical benefit.

All files are in `/mnt/user-data/outputs/` ready for import into your chosen platform (Notion, Airtable, or SQL database).