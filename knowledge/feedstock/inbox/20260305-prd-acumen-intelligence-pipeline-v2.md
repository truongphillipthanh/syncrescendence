# Product Requirements Document: Acumen Intelligence Pipeline

## 1. Product Overview

The Acumen Intelligence Pipeline is the operational engine for the Acumen IIC's Extraction mode (Mode 2), as specified in CANON-31115 and CANON-31143. It implements the IIC's "Compression Intelligence" capability — determining whether 3-hour podcasts should be bullet points, or conversely, whether 140-character posts deserve dissertation-level analysis.

The pipeline transforms raw YouTube platform signals into sovereign, context-matched intelligence artifacts. It executes variable-depth semantic extraction across 219+ curated channels, routing processed content into consumption modalities calibrated to the practitioner's cognitive state and temporal window. The system replaces algorithmic feed consumption with intentional, high-density knowledge acquisition integrated into the practitioner's existing temporal choreography (CANON-31_03 Feedcraft).

**North star after 90 days**: Every monitored platform event reaches the practitioner at the exact required compression depth (from one-sentence Logline to fully polished Transcript), delivered in the optimal modality and voice persona for the current consumption context, with an accompanying rationale explaining why this form serves this content in this moment. The practitioner has fully replaced manual YouTube platform browsing with pipeline artifacts.

**Non-goals**: The pipeline does not produce original content (Projection mode / Mode 3 is out of scope). It does not operate on platforms other than YouTube. It does not process content from unregistered channels. It does not attempt real-time processing — all generation is asynchronous overnight batch.

---

## 2. System Architecture

### Component Overview

The pipeline integrates five subsystems orchestrated by Prefect:

**Ingestion** polls the YouTube Data API and invokes Gemini 3.1 Flash for metadata-based triage, assigning each upload a routing decision, compression target, and polish level.

**Processing** executes a dual-track transformation. The **Deterministic Track** is the primary processing path, handling 60–70% of all content at zero API cost — fuzzy resolution key matching, regex-based disfluency removal, timing-based punctuation, and format templating. The **Intelligent Track** supplements the deterministic output exclusively for content requiring semantic judgment: charitable interpretation, editorial polish, synthesis paragraphs, and narrative bridging.

**Voice Synthesis** generates persona-mapped audio locally. Pocket TTS handles Scan Voice artifacts on CPU. Qwen3-TTS VoiceDesign produces Digest, Frontier, and Tutorial personas on GPU. All generation runs in overnight batch.

**Delivery** compiles processed artifacts into typed intelligence products — text briefs, audio episodes, and primary source queues — each carrying a rationale explaining why this form serves this content in this context.

**Storage** maintains the Feed Registry (institutional memory), the training corpus (sovereignty mechanism), and all processed artifacts in sovereign formats (Markdown, MP3, JSON) within the practitioner's local filesystem and Obsidian vault.

### Dual-Track Architecture

The dual-track split functionally mimics a compiler pipeline. The deterministic track executes lexical analysis and syntax-tree standardization, stripping predictable noise from the transcript. The intelligent track executes semantic evaluation, processing only the pre-cleaned data structures.

**The deterministic track always executes first for all content.** The intelligent track is invoked only when the assigned depth or polish level requires semantic judgment — specifically, content routed as Compress or Promote targeting depths of Abstract or deeper, or polish levels of Charitable or Editorial. Content routed as Headline or Skip, and all Bulletin/Institutional genre items at their default compression targets, never touch the intelligent track.

Both tracks are implemented simultaneously in Phase 1. This is not sequential — deterministic processing development runs in parallel with Gemini API integration from day one. If API quotas exhaust, the pipeline seamlessly outputs clean verbatim text via the deterministic track. This is not degraded operation; it is the intended output for Layer 1 scan artifacts.

### Maturation Trajectory

The pipeline matures through four phases with compressed timeline driven by cost pressure (paid-tier Gemini at ~$1–1.50/day is unsustainable without rapid sovereignty):

- **Phase 1 (Weeks 1–3)**: Dual-track bootstrap. Deterministic and intelligent processing implemented simultaneously. Every Gemini call logged as training data.
- **Phase 2 (Weeks 4–8)**: Local TTS stack. Voice personas operational. Private RSS podcast feed live.
- **Phase 3 (Weeks 8–12)**: First LoRA specialist trained on 500+ logged decisions. Shadow mode validation. Specialist swap on >90% agreement.
- **Phase 4 (Months 4–6)**: Full sovereignty. Gemini reserved for edge cases. Video compilation layer.

### Integration with Acumen IIC Architecture

The pipeline maps to existing canonical specifications:

| Pipeline Stage | Acumen IIC Mode | CANON Reference |
|---|---|---|
| Triage | Reconnaissance (Mode 1) | CANON-31_03 Feedcraft |
| Processing | Extraction (Mode 2) | CANON-31115 IIC Implementation |
| Delivery | Feeds Projection (Mode 3) | CANON-31143 Feed Curation |

The Daily Intelligence Cycle (CANON-31115) maps directly:
- Evening serendipitous browsing → feeds triage queue alongside automated monitoring
- Overnight processing → pipeline batch runs
- Morning intelligence brief → Dawn Brief (Layer 1 text scan)
- Morning strategic review → practitioner reviews Dawn Brief, makes overrides
- Targeted consumption → Layer 2 and Layer 3 artifacts routed to appropriate contexts

The six developmental chains (CANON-31143) inform genre typing: Intelligence chain content (frontier research) demands maximum novelty density; Expertise chain content (tutorials) demands actionability; Wisdom chain content (civilizational thinking) demands meaningful integration. The Feed Registry's genre and domain_tags fields encode this chain alignment.

---

## 3. Feed Registry Specification

The Feed Registry is the pipeline's institutional memory — a living document that accumulates knowledge about each channel's patterns, vocabulary, and signal quality over time. It is not configuration; it is intelligence. Stored locally as `registry.json`.

### Channel Metadata Schema

```json
{
  "channel_id": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
  "name": "Google DeepMind",
  "genre": "Institutional",
  "cadence": "irregular",
  "default_compression": "Abstract",
  "default_polish": "clean_verbatim",
  "signal_density": "high",
  "visual_dependency": "low",
  "voice_normalization": "normalize",
  "domain_tags": ["AI", "AGI", "Research"],
  "chain_alignment": "Intelligence",
  "resolution_vocabulary": ["Demis Hassabis", "AlphaFold", "Gemini", "TPUv5e"],
  "priority_band": "Tier 1",
  "triage_hit_rate": 0.85,
  "last_processed": "2026-03-04T10:00:00Z",
  "notes": "Prioritize architecture releases. Quarterly: reassess if signal density holds."
}
```

**Field specifications:**

| Field | Type | Valid Values | Notes |
|---|---|---|---|
| `genre` | Enum | Bulletin, Deep Dive, Commentary, Tutorial, Explainer, Institutional, Frontier | May migrate during quarterly audit |
| `cadence` | Enum | daily, weekly, biweekly, monthly, irregular | Determines polling frequency |
| `default_compression` | Enum | Headline, Abstract, Précis, Synopsis, Blueprint, Treatment, Transcript | Independent of polish |
| `default_polish` | Enum | clean_verbatim, charitable, editorial | Independent of compression |
| `signal_density` | Enum | high, medium, low | Recalibrated quarterly from triage_hit_rate |
| `visual_dependency` | Enum | none, low, high | Flags content that must be watched |
| `voice_normalization` | Enum | original, normalize, flag_per_episode | Original preserves speaker voice |
| `chain_alignment` | Enum | Intelligence, Information, Insight, Expertise, Knowledge, Wisdom | Which developmental chain this channel serves |
| `priority_band` | Enum | Tier 1, Tier 2, Tier 3 | May drift based on triage_hit_rate |
| `triage_hit_rate` | Float | 0.0–1.0 | Rolling 90-day ratio of non-Skip triage decisions |

### Genre Definitions

Each genre carries defaults for compression, polish, and voice persona. These are starting positions — the triage system may override per-episode.

| Genre | Default Compression | Default Polish | Default Voice | Typical Cadence |
|---|---|---|---|---|
| Bulletin | Headline | clean_verbatim | Scan Voice | daily |
| Deep Dive | Transcript | editorial | Digest Voice (MOSS-TTS for multi-speaker) | irregular |
| Commentary | Précis | charitable | Digest Voice | weekly |
| Tutorial | Blueprint | charitable | Tutorial Voice | variable |
| Explainer | Synopsis | charitable | Digest Voice | irregular |
| Institutional | Abstract | clean_verbatim | Scan Voice | irregular |
| Frontier | Précis | editorial | Frontier Voice | irregular |

### Registry Maintenance Protocols

**Continuous (automated)**:
- `resolution_vocabulary` auto-appends proper nouns identified by Gemini during intelligent-track processing.
- `triage_hit_rate` updates after every triage decision (rolling 90-day window).
- `last_processed` updates after every processing pass.

**Quarterly audit (manual, half-day)**:
- Channels with zero triage promotions in 90 days flagged for review. Prune or reclassify.
- `signal_density` recalibrated from `triage_hit_rate`: >0.7 = high, 0.3–0.7 = medium, <0.3 = low.
- `priority_band` reconsidered: channels whose signal_density dropped from high to low are candidates for Tier demotion.
- `genre` reclassified if a channel's output pattern has shifted (e.g., a Commentary channel that now primarily publishes Tutorials).
- Voice persona assignments reviewed for habituation — refresh persona parameters if needed.

---

## 4. Ingestion Subsystem

### YouTube Data API Integration

Polling uses the `search` and `videos` endpoints. To stay within the 10,000 unit daily quota, polling follows cadence-aware backoff:

| Channel Cadence | Poll Interval |
|---|---|
| daily | Every 4 hours |
| weekly | Every 12 hours |
| biweekly / monthly | Every 24 hours |
| irregular | Every 24 hours |

Channel IDs are cached locally to avoid redundant `channels.list` calls. Upload detection uses `publishedAfter` parameter set to `last_processed` timestamp from registry.

### Triage Logic

**Inputs**: Video title, description (full text), channel genre, priority band, duration, first 60 seconds of caption text (via `captions.download`), chapter markers if present.

**Outputs**: A routing decision with rationale.

| Decision | Meaning | Downstream |
|---|---|---|
| Skip | Below threshold. Not worth processing. | Logged only. |
| Headline | Worth noting, not consuming. | Deterministic-only: one sentence. |
| Compress | Process at channel's default compression target. | Deterministic + intelligent (if depth/polish require). |
| Promote | Process at higher resolution than default. | Intelligent track engaged. |
| Flag-for-Primary | Must be consumed in original form. | Rationale generated. Queued for Layer 3. |

### Gemini 3.1 Flash Triage Prompt

```text
System: You are an intelligence triage engine for a personal knowledge pipeline monitoring 
YouTube channels. Your job: determine whether this upload justifies the practitioner's 
attention, and if so, at what compression depth and polish level.

Context from registry:
- Channel: {name} | Genre: {genre} | Priority: {priority_band}
- Default compression: {default_compression} | Default polish: {default_polish}
- Signal density: {signal_density}
- Domain tags: {domain_tags}
- Resolution vocabulary: {resolution_vocabulary}

Video metadata:
- Title: {title}
- Duration: {duration}
- Description: {description}
- First 60s transcript: {initial_transcript}

Output strictly valid JSON:
{
  "decision": "Skip|Headline|Compress|Promote|Flag-for-Primary",
  "target_depth": "None|Headline|Abstract|Precis|Synopsis|Blueprint|Treatment|Transcript",
  "target_polish": "clean_verbatim|charitable|editorial",
  "rationale": "One sentence: why this decision, what signal was detected or absent.",
  "primary_flag_reason": "null unless Flag-for-Primary. Why must this be consumed in original form?"
}

Decision rules:
1. Skip: Bulletin content restating existing news with no novel signal.
2. Headline: Low-signal content from medium/high-density channels worth logging.
3. Compress: Standard content processed at channel defaults.
4. Promote: Override defaults upward when a lower-tier channel hosts a Tier 1 guest, 
   covers a paradigm shift, or produces unusually deep analysis.
5. Flag-for-Primary: Content where compression destroys signal — live debates with 
   performative dynamics, hardware teardowns, visually dependent demonstrations, 
   or events where the practitioner's own judgment is required.
```

### Caption Type Detection

Query `captions.list` endpoint for the video. If any track has `"kind": "asr"`, classify as auto-generated — route through full deterministic reconstruction (punctuation insertion, resolution key, filler removal). If manual tracks exist, use them — route through light deterministic pass (resolution key only, preserve existing punctuation).

### Resolution Key Extraction

Before processing, extract the episode-level resolution key from the video description:
1. All capitalized multi-word noun phrases (names, organizations, products).
2. All @-mentions and URLs (extract handle/domain as likely proper noun).
3. Merge with channel's `resolution_vocabulary` from registry.
4. During Phase 1, Gemini's intelligent-track output is compared against the resolution key — any new proper nouns Gemini resolves that aren't in the key get auto-appended to the channel's `resolution_vocabulary`.

The extraction method should evolve. Initial implementation uses simple heuristics; as the registry matures, the accumulated vocabulary handles most resolution without per-episode extraction.

---

## 5. Processing Subsystem

### Deterministic Track

The deterministic track is the primary processing path. It executes on all content regardless of triage routing. Zero API cost. Zero model calls.

**Fuzzy Resolution Key Matching**:
Levenshtein distance matching (threshold ≥ 0.85 similarity) against the merged resolution key (channel vocabulary + episode-level extraction). Applied to every token in the transcript. Examples: `alpha fold` → `AlphaFold`, `yan la coon` → `Yann LeCun`, `anthro pick` → `Anthropic`.

**Disfluency Removal**:
Two-tier regex system:

Tier 1 — Unconditional removal (always fillers):
```regex
\b(um|uh|hm+|mhm|ah|er)\b
```

Tier 2 — Context-dependent removal (filler only when not grammatically load-bearing):
```regex
# Remove "like" when preceded by pause marker or followed by filler
(?<=[.!?]|\[silence\])\s*\blike\b
\blike\b(?=\s+(?:um|uh|you know))

# Remove "you know" when flanked by content (not as genuine question)
\byou know\b(?!\?)

# Remove "I mean" at sentence boundaries
(?<=[.!?])\s*\bI mean\b

# Remove "sort of" / "kind of" when followed by repetition of prior phrase
\b(sort|kind) of\b(?=\s+\1)

# Remove "basically" / "essentially" / "literally" when not modifying a specific claim
\b(basically|essentially|literally)\b(?=\s*[,.]|\s+(?:the|it|we|they|I))
```

Expand this list as the pipeline encounters new patterns. Target: 50–80 patterns covering 80–90% of fillers. The remaining 10–20% are edge cases for the intelligent track.

**Timing-Based Punctuation** (for auto-generated captions only):
Parse ASR timestamp deltas between caption segments:
- `delta > 800ms` → Insert `.` and capitalize next token.
- `400ms < delta ≤ 800ms` → Insert `,`.
- `delta > 1500ms` → Insert `.\n\n` (paragraph break).

Adjust thresholds after 2 weeks of data: if practitioners report over/under-punctuation, recalibrate from actual caption timing distributions.

**Format Templating**:
After cleaning, apply the genre-specific output template (see below) to structure the text into the target artifact type.

### Intelligent Track

Invoked only when the triage decision is Compress or Promote AND the target depth is Abstract or deeper OR the target polish is charitable or editorial. All other content is finalized by the deterministic track.

**When Gemini 3.1 Pro is invoked:**
- Charitable interpretation and editorial polish (the Wispr Flow–style LLM pass on pre-cleaned text)
- Synthesis paragraphs for the Dawn Brief (positioning items within practitioner's frameworks)
- Narrative bridging for bespoke podcast episodes (connecting disparate items into coherent segments)
- Cross-domain pattern detection (what themes emerged across channels today?)

**When the intelligent track is NOT invoked:**
- All Headlines (deterministic-only: one sentence from title + description)
- All Bulletin and Institutional content at default clean_verbatim polish
- All resolution key application, filler removal, punctuation insertion
- All format templating

### The Polish Spectrum

Polish level is chosen independently of compression depth. A Transcript may remain clean verbatim while a Précis is inherently charitable by construction. The two axes are orthogonal:

| | Clean Verbatim | Charitable | Editorial |
|---|---|---|---|
| **Headline** | Deterministic only | N/A (too short) | N/A (too short) |
| **Abstract** | Deterministic only | Gemini resolves ambiguity | N/A (rarely needed) |
| **Précis** | Possible but unusual | Default for most genres | Frontier/Deep Dive |
| **Synopsis** | Possible for Tutorial | Default | Deep Dive |
| **Transcript** | Layer 1 reference use | Standard for most | Dwarkesh-grade |

**Clean Verbatim**: The deterministic track's output. Fillers removed, punctuation inserted, names resolved. Zero LLM intervention. This is the intended output for all Layer 1 scan artifacts and is fully sufficient for triage briefs and rapid skimming.

**Charitable Interpretation**: The intelligent track resolves pronoun ambiguity, completes fragmented sentences, smooths grammatical irregularities that result from thinking aloud. The speaker's vocabulary, rhetorical patterns, and characteristic phrasing are preserved. Self-corrections are kept when they reveal thinking process, collapsed when they're pure verbal repair.

**Editorial Polish**: The intelligent track restructures for maximal logical flow, elevates prose to publication standard. Sentence fragments become sentences. Rambling is tightened. The speaker's ideas, arguments, and personality are fully preserved, but the prose reads as if written. Reserved for Tier 1 Deep Dive and Frontier content that will be revisited as standalone artifacts.

### Genre-Specific Processing Templates

Each template instructs the model (or structures the deterministic output) to produce the *structurally correct* artifact type — not a generic summary with the right label.

**Bulletin → Headline (Logline)**:
```
Produce a single sentence fusing subject, development, and stakes. 
Format: [Who/What] [did/announced/released] [what], [implication].
Example: "Cerebras filed for IPO, signaling wafer-scale compute entering public markets."
```

**Institutional → Abstract (IMRaD-adjacent)**:
```
Structure as three components:
1. Claim: What is being announced or presented? (1-2 sentences)
2. Evidence: What specifications, data, or demonstrations support it? (1-2 sentences)  
3. Implication: What does this mean for the practitioner's domains? (1 sentence)
Preserve technical precision. Strip corporate framing and marketing language.
```

**Commentary → Précis (rhetorical structure preservation)**:
```
Produce a Précis that preserves the speaker's exact rhetorical structure and logical 
progression while condensing length. The output must reflect:
1. How the argument opens (the speaker's chosen entry point)
2. The logical sequence of evidence and reasoning (in the speaker's order, not reorganized)
3. The conclusion the speaker reaches and why they believe it follows
4. What distinguishes this framing from consensus (the novel contribution)
Do NOT restructure the argument into a "better" logical order. The rhetorical sequence 
is itself information about how the speaker thinks.
```

**Tutorial → Blueprint (actionable specification)**:
```
Extract a dimensioned, actionable specification:
1. Prerequisites: What must be installed, configured, or understood before starting.
2. Steps: Numbered sequence with exact commands, configurations, and parameters.
3. Gotchas: Failure modes the speaker warns about or implies.
4. Outcome: What the completed implementation looks like.
Strip motivation and encouragement. This artifact must be executable without watching.
```

**Explainer → Synopsis (pedagogical structure)**:
```
Reconstruct the pedagogical architecture in the speaker's exact order of introduction:
1. Core Concept: What is being explained.
2. Intuition: The analogy, metaphor, or visualization used to build initial understanding.
3. Formal Treatment: The precise mechanism, math, or technical detail.
4. Connections: How this concept relates to adjacent ideas the speaker references.
Preserve the order of conceptual introduction — the pedagogy IS the content.
```

**Deep Dive → Transcript (multi-voice, editorially polished)**:
```
Produce a complete faithful rendering of the conversation. Preserve:
- Each speaker's distinctive vocabulary, sentence structure, and rhetorical patterns
- Disagreements, tensions, and collaborative idea development
- Self-corrections that reveal thinking process
- Substantive tangents and exploratory threads
Apply editorial polish: elevate to written-essay standard while maintaining each 
speaker's recognizable voice. Use em-dashes for interruptions. Bold speaker names.
The output must be a standalone readable artifact of independent literary value.
```

**Frontier → Précis (synthesis-oriented)**:
```
Produce a Précis preserving the speaker's conceptual architecture:
1. The framework being proposed or explored (axioms, definitions, scope)
2. The reasoning chain (how conclusions follow from premises)
3. Implications the speaker draws or implies
4. Synthesis note: How this connects to existing frameworks in the practitioner's 
   knowledge base (reference domain_tags from registry for relevant connections).
```

---

## 6. Voice Synthesis Subsystem

### Voice Personas as Cognitive Affordances

Voice personas are not aesthetic preferences or TTS configuration details. They are functional information architecture — the auditory equivalent of the genre tag in the registry. Each persona primes a specific cognitive processing mode in the practitioner:

- **Scan Voice** primes tactical-awareness mode: rapid pattern recognition, triage-level attention.
- **Digest Voice** primes sustained informational absorption: analytical engagement, moderate depth.
- **Frontier Voice** shifts the practitioner into contemplative processing: associative thinking, paradigm-level reflection.
- **Tutorial Voice** activates instructional tracking: sequential attention, implementation focus.

Voice selection is driven by the intersection of content genre and consumption context, not by channel. The same channel's content may arrive in Scan Voice when it appears in the Dawn Brief and Digest Voice when expanded into the evening podcast.

The personas must be sufficiently distinct that the cognitive cueing effect persists over months of daily use. Quarterly review: if the practitioner reports habituation (no longer registering the voice-switch signal), refresh persona parameters to restore differentiation.

### Model Selection Matrix

| Model | Persona | Hardware | Use Case |
|---|---|---|---|
| Pocket TTS (Kyutai, 100M) | Scan Voice | CPU-only, any M1+ Mac | Rapid generation for short scan items. Sub-12s per clip. |
| Qwen3-TTS VoiceDesign | Digest, Frontier, Tutorial | GPU (RTX 4060) or M2+ with MLX | Rich prosody for sustained 20–90 min narration. |
| Kokoro 82M | Any (fallback) | CPU-only | Continuous delivery if Qwen3 environment fails. |
| MOSS-TTS | Multi-speaker Deep Dive | GPU | Discrete speaker separation for dialogue preservation. |

### VoiceDesign Persona Prompts

```
Scan Voice:
"Clear, brisk pacing, slightly clipped enunciation. Low affective coloring, precise 
articulation. 160 words per minute. Flat intonation indicating operational awareness. 
Short inter-segment pauses (200ms). No warmth — this is status reporting."

Digest Voice:
"Warm, measured pacing. Moderate resonance, slight chest quality. 130 words per minute. 
Authoritative but inviting. 400 millisecond inter-segment breaths. The listener should 
feel they are being briefed by a thoughtful analyst, not read to by a machine."

Frontier Voice:
"Deep register, slow and deliberate cadence. Contemplative spacing with 600ms+ pauses 
at paragraph breaks. 110 words per minute. Extended silences between segments to allow 
conceptual absorption. The voice invites dwelling, not scanning."

Tutorial Voice:
"Precise, patient, gently upbeat. Slight upward inflection at the end of instructional 
steps (signaling 'here comes the next one'). 140 words per minute. Clear enunciation of 
technical terms. The voice of a skilled teacher who assumes competence."
```

These prompts are saved as versioned artifacts in the registry directory. Adjust after Phase 2 testing — the first versions are starting points, not final.

### Audio Generation Pipeline

1. Split text artifacts at paragraph boundaries. Each chunk processes independently to eliminate prosody drift.
2. Prepend the persona prompt to each chunk for consistent voice seeding.
3. Generate `.wav` files per chunk via the assigned TTS model.
4. Concatenate with pydub. Insert 500ms silence between semantic sections, 200ms between paragraphs within a section.
5. Apply -14 LUFS loudness normalization.
6. Export to 128 kbps MP3 (spoken-word optimal quality-to-size).
7. Estimated generation time: 30–60 minutes of audio in 1–3 hours on M2+ Mac or RTX 4060.

---

## 7. Delivery Subsystem

### Consumption Space Navigation

Effective intelligence consumption is phenomenological — it depends on the practitioner's cognitive state, the sensory modality, the compression depth, and the temporal context. The delivery system navigates a four-dimensional consumption space:

**Depth** × **Polish** × **Modality** × **Context**

Every routing decision evaluates all four dimensions before selecting a playlist and artifact form. The named playlists below encode specific positions in this space — they are defaults, not constraints. The practitioner can override any routing decision.

### The Three Consumption Layers

| Layer | Purpose | Cognitive Demand | Depth Range | Polish Range | Modalities |
|---|---|---|---|---|---|
| **Scan** | Peripheral awareness. What happened? | Low. Pattern recognition. | Headline – Abstract | Clean Verbatim | Text, Audio (Scan Voice) |
| **Digest** | Substantive understanding. | Medium. Sustained attention. | Précis – Synopsis | Charitable – Editorial | Text, Audio (Digest/Frontier Voice) |
| **Primary** | Unmediated engagement. | High. Full attention. | Treatment – Transcript – Original | Editorial or Original | Text, Audio (Original), Video (Original) |

### Named Playlists

| Playlist | Layer | Modality | Context | Voice | Cadence |
|---|---|---|---|---|---|
| Dawn Brief | Scan | Text | Morning sharp focus (6–8 AM) | N/A | Daily |
| Commute Current | Scan | Audio | Commute/transition (8–9 AM) | Scan Voice | Daily |
| Midday Tactical | Primary | Text | Focused work (as needed) | N/A | As needed |
| Afternoon Ambient | Digest | Audio | Afternoon transition / exercise | Digest Voice | 3–4x weekly |
| Evening Synthesis | Digest | Audio | Evening walk / wind-down (9–10:30 PM) | Frontier Voice for frontier content, Digest Voice otherwise | Daily |
| Weekend Deep | Primary | Text + Video | Saturday deep synthesis (4–6 hours) | N/A (original sources) | Weekly |

### Dawn Brief Format

```markdown
# Dawn Brief | {DATE}

## Synthesis Alert
{Cross-domain pattern detected across {Channel A} and {Channel B} regarding {Topic}.}
{Why this matters: one sentence connecting the pattern to the practitioner's active projects or chain development.}

## Tactical Awareness (Promoted)
**[{Channel Name}] {Headline}**
{Abstract paragraph.}
*Why promoted: {Triage rationale from Gemini.}*
*Suggested consumption: {Layer recommendation + modality + context.}*

## Peripheral Radar (Compressed)
- **[{Channel Name}]** {Headline}
- **[{Channel Name}]** {Headline}
- **[{Channel Name}]** {Headline}

## Primary Source Flags
- **[{Channel Name}]** {Title}
  *Why this cannot be compressed: {primary_flag_reason from triage.}*
  *What to pay attention to: {Logline + connection to existing knowledge.}*
  *Suggested context: {When and how to consume — e.g., "Weekend Deep, watch in full, visual dependency high."}*

## Pipeline Health
{N} ingested / {N} compressed / {N} promoted / {N} flagged. {N} min audio generated.
```

### Bespoke Podcast Episode Structure

The bespoke podcast is not a flat TTS rendering of text articles. It is a structured audio briefing designed to feel like being briefed by a thoughtful intelligence analyst.

**Episode structure (Afternoon Ambient / Evening Synthesis)**:

1. **Opening** (Digest Voice): The single most important development of the day and a one-sentence statement of why it matters to the practitioner. Duration: 60–90 seconds.

2. **Thematic Segments** (3–4 per episode): Items grouped by domain or conceptual connection, not by source channel. Each segment:
   - Segment intro: "The theme connecting these items is {theme}."
   - Content items delivered sequentially.
   - Voice persona matches content type within the segment (Frontier Voice for civilizational items, Digest Voice for analytical items, Tutorial Voice for implementation items).

3. **Transitions between segments**: Explicit bridging statements generated by the intelligent track: "This connects to {previous segment's theme} because {connection}." or "A counterpoint to that comes from {Channel}, which argues {contrasting position}."

4. **Closing synthesis** (Digest Voice): What patterns emerged today that weren't visible yesterday? One paragraph. Duration: 60–90 seconds.

5. **Rationale coda** (Scan Voice, brief): "This episode was routed to Evening Synthesis because {reason — e.g., 'the frontier content benefits from your evening associative processing state'}."

### Private RSS Feed Specification

A static Python script (`compile_feed.py`) parses the local audio output directory and generates `podcast.xml` (RSS 2.0). Hosted on GitHub Pages. Updated by GitHub Actions after each `flow_compile_delivery` run.

- **File naming**: `YYYYMMDD-{Playlist}.mp3` (e.g., `20260304-EveningSynthesis.mp3`)
- **Format**: 128 kbps MP3 (spoken-word optimal)
- **Storage**: ~200 MB/month. Trivially free on GitHub Pages.
- **Multiple feeds**: One RSS feed per playlist (Dawn Brief audio scan, Afternoon Ambient, Evening Synthesis). Practitioner subscribes to each in their podcast app as separate "shows."

### Graceful Degradation

| Failure | Behavior | Practitioner Experience |
|---|---|---|
| Gemini quota exhausted | Deterministic track completes all processing at clean_verbatim. Intelligent track items queued for next day. | Dawn Brief arrives on time with slightly less polished content. No loss of coverage. |
| Qwen3-TTS fails | All audio routes to Pocket TTS (reduced prosodic richness). | Podcast episodes arrive on time in Scan Voice only. Functional but less differentiated. |
| Pocket TTS fails | Audio generation skipped entirely. | Text-only delivery. Dawn Brief and Reading Digest arrive normally. |
| YouTube API quota | Cache serves last-known channel state. New uploads detected on next polling cycle. | Brief may be 4–12 hours stale on some channels. Acceptable. |
| Full pipeline stall | Prefect partial flow outputs whatever completed. | Practitioner receives partial brief with health alert explaining what's missing and why. |

---

## 8. Orchestration

### Prefect Flow Specification

Prefect manages the state graph with native retries, dead-letter handling, and partial flow behavior. Every task uses `.with_options(on_failure=continue_downstream)` to ensure partial output rather than full failure.

### Scheduling

Cron expressions are starting defaults. Adjust based on actual hardware performance — the requirement is that all processing completes before 06:00 AM, not that it starts at exactly these times.

| Cron | Flow | Description |
|---|---|---|
| `0 */4 * * *` | `flow_ingest_triage` | Poll YouTube API, execute Gemini Flash triage, populate processing queue (SQLite). |
| `30 0 * * *` | `flow_process_deterministic` | Execute regex cleaning, resolution key matching, punctuation insertion, format templating on all queued items. |
| `30 1 * * *` | `flow_process_intelligent` | Execute Gemini Pro polish/synthesis on items requiring intelligent track. Skip if quota exhausted. |
| `30 2 * * *` | `flow_synthesize_audio` | Batch TTS generation. Pocket TTS for Scan items, Qwen3 for Digest/Frontier/Tutorial. |
| `0 4 * * *` | `flow_compile_delivery` | Generate Dawn Brief markdown. Compile podcast episodes. Update RSS feeds. Push to Obsidian vault. |
| `30 5 * * *` | `flow_health_report` | Summarize pipeline status. Push to Telegram/Discord. |

### Monitoring

- **Telegram/Discord webhook**: Critical alerts on `youtube_quota_exhaustion`, `gemini_quota_exhaustion`, `tts_hardware_failure`, `disk_space_critical`.
- **Morning health report** (05:30 AM): `[Pipeline Status] {N} ingested / {N} compressed / {N} promoted / {N} flagged. {N} min audio generated. {N} intelligent-track items skipped (quota). Training corpus: {N} total logged pairs.`
- **Weekly summary**: Triage accuracy review (did the practitioner agree with routing decisions?), specialist model training corpus size, API cost for the week.

### Retry Policies

| Task | Retries | Backoff | Dead Letter |
|---|---|---|---|
| YouTube API poll | 3 | Exponential (30s, 60s, 120s) | Skip channel, continue others |
| Gemini Flash triage | 2 | 60s | Route to default Compress |
| Gemini Pro processing | 1 | 120s | Output deterministic clean_verbatim |
| TTS generation | 2 | 30s | Skip audio, deliver text-only |

---

## 9. Specialist Model Training

The specialist model is not a nice-to-have. It is the economic mechanism that makes the pipeline viable at steady state. Without it, API costs accumulate to ~$35–45/month. With it, costs approach zero.

### Logging Specification

From Day 1, every Gemini execution appends to `training_corpus.jsonl`:

```json
{
  "timestamp": "2026-03-04T02:15:00Z",
  "task_type": "triage|polish|synthesis|bridge",
  "model": "gemini-3.1-flash|gemini-3.1-pro",
  "input": {
    "instruction": "Full system prompt used",
    "context": "All input data provided to the model"
  },
  "output": "Complete model response",
  "metadata": {
    "channel_id": "UC...",
    "genre": "Commentary",
    "video_id": "...",
    "processing_time_ms": 3400
  }
}
```

This schema must capture enough context to reproduce the model's decision from the logged data alone. If a training example requires external lookups to make sense, the logging is insufficient.

### Training Trigger

First LoRA training executes when `training_corpus.jsonl` contains ≥ 500 items with `task_type: "triage"`. At ~20 triage decisions/day, this threshold is reached at approximately Week 3.

### Distillation Protocol

1. **Phase 1 (Weeks 1–3)**: Gemini Flash handles all triage. Every call logged.
2. **Week 3**: Train QLoRA adapter on Qwen2.5-1.5B or Phi-4-mini using the logged corpus. Training completes in hours on M2+ Mac or RTX 4060 via Unsloth.
3. **Shadow mode**: Deploy specialist alongside Gemini Flash. Both process every triage input. Compare `decision` key via string match.
4. **Agreement tracking**: Rolling window of 100 consecutive items. Log agreement rate.
5. **Swap criteria**: When agreement exceeds 90% over 100 consecutive items, specialist becomes primary for routine triage (Skip, Headline, Compress decisions). Gemini Flash reserved for Promote and Flag-for-Primary logic paths.
6. **Continuous updates**: Maintain a 1,000-item replay buffer. Train new LoRA adapter monthly on the latest 1,000 items + replay buffer. This keeps the specialist current as channels evolve and practitioner interests shift.

### Base Model Selection

Qwen2.5-1.5B or Phi-4-mini. Selection criteria: superior JSON schema adherence on consumer hardware, fast QLoRA convergence on small corpora (<5K examples), and inference latency under 500ms for triage decisions. Benchmark both during Phase 1 on the first 100 logged items; choose whichever achieves higher agreement.

---

## 10. Implementation Roadmap

### Phase 1: Dual-Track Bootstrap (Weeks 1–3)

**Entry criteria**: M2+ Mac or RTX 4060 available. Google AI Pro subscription ($20/mo) active. GitHub account for RSS hosting.

**Deliverables**:
- `registry.json` populated with all 219 channels (genre, cadence, defaults).
- YouTube Data API polling via Prefect cron.
- Gemini 3.1 Flash triage operational.
- Deterministic processing track (filler removal, punctuation, resolution keys, templating) operational in parallel.
- Gemini 3.1 Pro intelligent track for Compress/Promote items.
- Dawn Brief markdown delivered to Obsidian vault by 06:00 AM.
- `training_corpus.jsonl` logging every Gemini call.
- Telegram/Discord health alerts operational.

**Exit criteria**: Dawn Brief delivered 100% of mornings for 7 consecutive days. Training corpus exceeds 200 items.

### Phase 2: Local Audio Layer (Weeks 4–8)

**Entry criteria**: Phase 1 exit criteria met. Pocket TTS and Qwen3-TTS tested locally.

**Deliverables**:
- Pocket TTS generating Scan Voice audio.
- Qwen3-TTS generating Digest, Frontier, Tutorial persona audio.
- Chunking + concatenation + normalization pipeline.
- GitHub Pages RSS feed for Commute Current and Evening Synthesis playlists.
- VoiceDesign prompts tuned against generated output (iterate at least 3 revisions per persona).

**Exit criteria**: Audio episodes delivered for 14 consecutive days. Practitioner confirms voice personas are perceptibly distinct and the cognitive cueing effect is present.

### Phase 3: Sovereign Specialist Swap (Weeks 8–12)

**Entry criteria**: Training corpus exceeds 500 triage items. Phase 2 audio delivery stable.

**Deliverables**:
- QLoRA fine-tuned specialist model on logged triage decisions.
- Shadow mode running: specialist + Gemini Flash in parallel.
- Agreement tracking dashboard (can be a simple log).
- Specialist swapped to primary upon >90% agreement over 100 items.
- Gemini Flash reserved for Promote/Flag-for-Primary paths.
- MOSS-TTS integration for multi-speaker Deep Dive transcripts (if hardware supports).

**Exit criteria**: Specialist handling >80% of daily triage volume. Weekly API cost below $5.

### Phase 4: Full Sovereignty (Months 4–6)

**Entry criteria**: Phase 3 specialist stable for 30 days.

**Deliverables**:
- Gemini Pro reserved for genuine edge cases only.
- ffmpeg pipeline for Layer 1 video trailer compilation using Gemini-identified timestamp markers.
- Full quarterly audit cycle completed (registry pruning, signal density recalibration, persona refresh).
- Continuous LoRA update cycle operational (monthly retrain on latest 1K items + replay buffer).

**Exit criteria**: Total monthly operating cost below $5. 100% of Layer 1 and Layer 2 artifacts generated locally.

---

## 11. Cost Model

| Phase | Gemini API | TTS | Hosting | Storage | Total Monthly |
|---|---|---|---|---|---|
| Bootstrap (Weeks 1–3) | Google AI Pro $20/mo | $0 (none yet) | $0 | $0 | ~$20 |
| Audio Layer (Weeks 4–8) | Google AI Pro $20/mo | $0 (local) | $0 (GitHub Pages) | $0 (<1 GB) | ~$20 |
| Specialist Swap (Weeks 8–12) | ~$5–10/mo (reduced calls) | $0 (local) | $0 | $0 | ~$5–10 |
| Full Sovereignty (Month 4+) | <$2/mo (edge cases) | $0 (local) | $0 | $0 | ~$2 |

**Hardware capital** (one-time, sunk cost): M2+ Mac or PC with RTX 4060. Both support TTS batch generation and LoRA fine-tuning.

---

## 12. Risk Register

| Risk | Category | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Gemini quota exhaustion | Technical | High (Phase 1) | Medium | Deterministic track ensures Dawn Brief delivery. Accelerate specialist. |
| TTS prosody drift in long segments | Technical | Medium | Low | Strict paragraph-level chunking + consistent prompt seeding per chunk. |
| Specialist overfitting to early channels | Technical | Medium | Medium | Replay buffer + monthly retrain. Monitor agreement on new channels. |
| Gemini 3.1 model retirement | Strategic | Certain (eventually) | Low | Phase 3 specialist insulates core pipeline. Only edge-case path affected. |
| Pipeline stall (Prefect failure) | Operational | Low | High | `.with_options(on_failure=continue_downstream)` on all tasks. Partial output > no output. |
| Voice persona habituation | Strategic | Medium | Low | Quarterly persona parameter refresh. Maintain maximum distinctiveness. |
| YouTube API changes | Strategic | Low | High | Channel ID cache reduces API dependence. yt-dlp fallback for data extraction. |
| Student budget exceeded | Operational | Medium (Phase 1) | High | Cost ceiling: $25/mo. If exceeded, freeze intelligent track, run deterministic-only until specialist is ready. |

---

## 13. Success Metrics

### 30-Day Checkpoint
- Dawn Brief delivered to Obsidian 100% of mornings by 06:00 AM.
- 100% of Tier 1 and Tier 2 uploads processed within 24 hours.
- Training corpus exceeds 500 validated triage items.
- Practitioner reports: pipeline artifacts are replacing >50% of manual YouTube browsing.

### 90-Day Checkpoint
- Specialist model agreement rate exceeds 90% against Gemini Flash baseline.
- Weekly API cost below $5.
- Audio podcast episodes delivered for 60+ consecutive days.
- Practitioner confirms: voice personas produce distinct cognitive cueing effect.
- Practitioner confirms: total replacement of manual YouTube platform browsing.
- Cross-domain synthesis alerts (Dawn Brief Section 1) have surfaced at least 3 non-obvious connections the practitioner would not have detected manually.

### 180-Day Checkpoint
- Total monthly operating cost below $5.
- 100% of Layer 1 and Layer 2 artifacts generated via sovereign local compute.
- Time-to-insight: sub-12-hour latency between a platform upload and practitioner contextual awareness.
- Feed Registry has completed at least one full quarterly audit cycle with measurable signal density recalibration.
- The pipeline's institutional knowledge (registry vocabulary, specialist model, persona prompts) demonstrably improves processing quality compared to Month 1 baseline.
