# YOUTUBE PROCESSING BACKLOG

**Document Type**: QUEUE (Content Processing)
**Last Updated**: 2025-12-29
**Total Channels**: 100+
**Processing Status**: Manual (automation via MCP + transcribe_youtube pending)

---

## PRIORITY TIERS

### Tier 1: Frontier Labs & Research Synthesis (Highest Priority)
Process immediately when new uploads appear. Strategic value: Frontier developments, technical depth.

- **Anthropic** - AI safety, Claude updates
- **OpenAI** - GPT developments, safety research
- **Dwarkesh Patel** - Deeply researched interviews (frontier AI leaders)
- **Scale AI** - Reliable AI systems, important decisions
- **Google for Developers** / **Google Cloud Tech** - Gemini developments, cloud AI
- **NVIDIA** / **NVIDIA Developer** - Accelerated computing, GPU developments
- **Latent Space** - AI engineers community (90K+), models/tools/ideas
- **Extropic** - Thermodynamic computing (cutting-edge substrate)

### Tier 2: Technical Deep-Dives (High Priority)
Process within 7 days. Technical expertise, implementation guidance.

- **Fireship** - High-intensity code tutorials
- **Theo - t3.gg** - Full stack TypeScript
- **ThePrimeTime** - Stream highlights, dev perspectives
- **Two Minute Papers** - Research paper summaries
- **AI Bites** - AI concepts, research papers (clear explanations)
- **Anton Petrov** - Science/math explanations via simulations
- **Marina Wyss** - ML/AI career guidance (Twitch/Amazon scientist)
- **LangChain** - Agent building with LangChain
- **KodeKloud** - DevOps, cloud comprehension
- **freeCodeCamp.org** - Programming education

### Tier 3: Commentary & Analysis (Medium Priority)
Process within 30 days. Market analysis, strategic perspectives.

- **All-In Podcast** - Chamath, Calacanis, Sacks, Friedberg (economic/tech/political)
- **a16z** - VC perspectives, technology trends
- **Matthew Berman** - AI news, open source, LLMs
- **Wes Roth** - AI news, optimism-focused
- **Matt Wolfe** - AI capabilities exploration
- **The AI Daily Brief** - Daily AI news summaries
- **AI News & Strategy Daily | Nate B Jones** - AI strategy for builders/execs
- **Discover AI** - Scientific frontiers of AI
- **David Shapiro** - AI philosophy ("liberate humanity from drudgery")
- **Wes and Dylan** - AI/robotics/biotech expert interviews
- **Curt Jaimungal** - Theoretical physics, consciousness, AI, God (technical)
- **What the AI?!** - Weekly AI guide (business/finance focus)

### Tier 4: Background/Ambient (Low Priority)
Process as time allows. General tech news, ambient content.

- **Bloomberg Technology** / **Bloomberg Television** - Tech news, market analysis
- **CNBC** / **CNBC Television** - Financial news, market analysis
- **WIRED** - "Where tomorrow is realized"
- **Big Think** - Philosophy, culture, human mind
- **Y Combinator** / **YC Root Access** - Startup advice, founder stories
- **Notion** - Product updates
- **ARK Invest** - Disruptive innovation focus
- **Digital Trends** - Technology news (simply/clearly)
- **Cheddar** - Financial news, tech coverage

### Tier 5: Specialized/Niche (Selective Processing)
Process only when specific topic relevant.

- **ARC Prize** - $1M+ AGI benchmark competition
- **Asianometry** - Business/economics/history essays
- **Quanta Magazine** - Breakthroughs in science/math
- **Institute for Advanced Study** - Theoretical research
- **IBM Technology** - AI, automation, cybersecurity, data science
- **Databricks** - Data and AI company updates
- **Tiago Forte** - Building a Second Brain methodology
- **Linking Your Thinking** - Personal Knowledge Management (Nick Milo)
- **HealthyGamerGG** - Dr. K content (mental health, gaming)
- **SleepWise** - Thoughtful sleep content

---

## PROCESSING PROTOCOL

### 1. Monitor
- Check subscription feed for new uploads
- RSS feed integration (future automation)
- Manual check: Daily for Tier 1, Weekly for Tier 2-3

### 2. Qualify (Signal vs Noise)
**Process if**:
- Frontier lab announcement (model release, API update, research paper)
- Technical deep-dive (implementation tutorial, architecture explanation)
- Strategic analysis (market shifts, competitive landscape)
- Expert interview (frontier researchers, industry leaders)

**Skip if**:
- Generic news recap (no unique insight)
- Promotional content (product marketing without substance)
- Duplicate content (same topic covered better elsewhere)

### 3. Transcribe
**Function**: `transcribe_youtube`
**Input**: YouTube URL
**Output**: Cleaned transcript with:
- Filler words removed
- Speaker attribution (if interview)
- Timestamps for key sections
- Technical terms preserved

### 4. Synthesize
**Route based on content type**:

**Frontier Development** → Apply `digest` function
- Extract key announcements, technical specifications, strategic implications
- Compare to existing knowledge (OPERATIONAL/AI_ECOSYSTEM_SURVEY.md)
- Flag for OPERATIONAL update if affects current tooling/models

**Technical Tutorial** → Apply `integrate` function
- Extract implementation patterns, code examples, best practices
- Route to function library if metaprompt-relevant
- Archive to REFERENCE if stable technique

**Strategic Analysis** → Apply `offload` or `primer` function
- `offload` if torrential insights requiring unpacking
- `primer` if introducing unfamiliar topic requiring orientation

### 5. Route
**OPERATIONAL** (if affects living documents):
- CLI tool updates → AI_ECOSYSTEM_SURVEY.md refresh
- Model releases → AI_ECOSYSTEM_SURVEY.md refresh
- Pricing changes → AI_ECOSYSTEM_SURVEY.md refresh

**REFERENCE** (if stable insight):
- Technical explanations (foundational concepts)
- Historical context (how we got here)
- Methodology archives (research approaches)

**QUEUE → DELETE** (if low signal):
- Content qualified but not processed → Mark as "qualified/skipped" with brief note

### 6. Archive
Mark video as processed in backlog:
```markdown
- [x] **Channel Name** - Video Title (YYYY-MM-DD)
  - Route: OPERATIONAL/REFERENCE/Skipped
  - Integration: [Document updated or reference created]
  - Notes: [Brief synthesis or skip rationale]
```

---

## CURRENT BACKLOG

**Status**: No active processing queue (manual workflow not yet established)

**Next Action**: Identify 1-2 Tier 1 videos for pilot processing to validate workflow before scaling.

**Automation Potential**: MCP server monitoring RSS feeds, triggering `transcribe_youtube`, routing via content qualification, updating OPERATIONAL documents on refresh cycles.

---

## PROCESSED LOG

_None yet. First entries will be added after pilot processing._

---

## NOTES

**Content Processing Bottleneck**: 100+ channels at varied upload frequencies = significant manual processing burden. This queue infrastructure establishes workflow even before automation.

**Tier Assignment Rationale**:
- **Tier 1**: Direct impact on frontier AI capabilities/strategy
- **Tier 2**: Implementation knowledge for building with AI
- **Tier 3**: Strategic context, market understanding
- **Tier 4**: Background awareness, ambient learning
- **Tier 5**: Niche expertise, selective utility

**MCP Integration Vision**: RSS feed monitor → Qualify (AI assessment of title/description) → Transcribe → Synthesize → Route → Update OPERATIONAL → Notify human for approval

**Human-in-Loop**: All tier movements (QUEUE → OPERATIONAL → REFERENCE) require human approval. Automation proposes, Principal authorizes.

---

**END YOUTUBE PROCESSING BACKLOG**
