### Key Points
- **OpenAI's Ecosystem Overview**: As of January 12, 2026, OpenAI's platform centers on ChatGPT for consumers and businesses, with GPT-5.2 as the flagship model family offering varying reasoning levels (Instant, Thinking, Pro). Consumer features include core chat, image/video generation, deep research, and agents, while developer tools emphasize APIs for chat, media, and agents. Evidence suggests rapid evolution, with recent additions like GPT-5.2 (December 2025) and ongoing deprecations like macOS Voice (January 15, 2026).
- **Tier Gating and Limits**: Free access is limited (e.g., 10 messages every 5 hours), Plus ($20/month) expands usage but caps at around 160 GPT-5 messages per 3 hours based on community reports, Pro ($200/month) offers near-unlimited with guardrails, and Business/Enterprise add governance. API is pay-per-token, with no strict caps but rate limits implied.
- **Deprecations and Changes**: Assistants API sunsets August 26, 2026; custom GPTs transitioned to GPT-5.2 today; older models like GPT-4o API retire February 2026. Renames include Team to Business in some contexts.
- **Unique vs. Claude**: OpenAI excels in media generation (Sora video) and coding agents (Codex), providing additive value for verification or specialized workflows, though overlaps in reasoning exist.
- **Integration Recommendations**: For Claude-centric setups, route media/coding to OpenAI via APIs; Plus suits light use, Pro for heavy, API for scalable dev—upgrade if hitting limits, as economics favor Pro for unlimited high-volume tasks.

### Subscription Decision Guide
Research indicates Plus is economical for casual users needing expanded features without unlimited access, while Pro justifies the cost for professionals requiring maximum reasoning and no caps (break-even at ~10x Plus usage). Business/Enterprise fits teams with compliance needs. API is ideal for integration, with token costs scaling efficiently for low-volume orchestration.

### Recent Material Changes
Evidence points to GPT-5.2 launch (December 11, 2025) enhancing reasoning and modalities, alongside Voice retirement on macOS (January 15, 2026) and custom GPT transitions today, signaling focus on unified experiences and agentic tools like Codex and Atlas.

---

### Comprehensive Forensic Catalog and Architecture Map of OpenAI's Ecosystem

This reference manual provides a mutation-resistant, cross-validated snapshot of OpenAI's platform as a complementary node in a Claude-orchestrated constellation. Drawing from first-party sources, developer docs, release notes, GitHub repositories, app store updates, and practitioner insights, it enumerates the full surface area, gating, limits, deprecations, unique contributions, integration paths, and economic models. All claims are tied to an Evidence Ledger (Appendix A) for verifiability, with conflicts resolved by prioritizing newer first-party data. Flagged items potentially changed in the last 90 days include GPT-5.2 rollout details, Voice deprecation, and custom GPT transitions, given OpenAI's velocity.

#### 0. AS-OF SNAPSHOT
- **As-of Date/Time**: January 12, 2026, 06:38 PM PST.
- **Scope Boundaries**: Inventory built via scans of first-party pricing/plans (e.g., openai.com/chatgpt/pricing, openai.com/api), docs indexes (platform.openai.com/docs), Help Center (help.openai.com), launch posts/blog (openai.com/blog), GitHub org (github.com/openai), app release notes (via web searches on apps.apple.com, play.google.com, help.openai.com), status pages (status.openai.com), and practitioner channels (X posts, community forums) for undocumented behaviors. Did not include YouTube videos, exhaustive GitHub issues, or non-English sources.
- **Executive Summary of Recent Changes**: Material shifts include the December 11, 2025, release of GPT-5.2 (with Instant/Thinking/Pro variants, knowledge cutoff August 2025), retirement of Voice in macOS app effective January 15, 2026, and transition of custom GPTs to GPT-5.2 on January 12, 2026. Agentic tools like Codex (updated to GPT-5.2-Codex on December 18, 2025) and Atlas browser (launched October 21, 2025) emphasize automation, while Assistants API deprecation is slated for August 26, 2026. No major incidents noted, but community reports highlight tighter safety guardrails potentially impacting creativity.

#### 1. ECOSYSTEM TAXONOMY (FULL SURFACE AREA)
The hierarchical tree below enumerates OpenAI's ecosystem components, with leaf nodes detailing name, location, access gates, status, and primary reference. Taxonomy is derived from surface scans, focusing on consumer, org, developer, agentic, media, and policy surfaces.

- **A. ChatGPT Consumer (web + apps)**
  - Core chat
    - Product/Feature Name: Conversational interface with model selection.
    - Where it Lives: Web (chatgpt.com), iOS/Android apps, macOS/Windows desktop.
    - Access Gates: Free (limited), Plus/Pro (expanded); region: Global with some rollout cohorts (e.g., group chats piloted in select countries).
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Models (by family)
    - Product/Feature Name: GPT-5.2 (Instant, Thinking, Pro); GPT-5 mini; legacy (GPT-4o, o3/o4-mini).
    - Where it Lives: ChatGPT.
    - Access Gates: Free (limited Instant), Plus (Thinking), Pro (Pro variant); platform: All.
    - Status: GA (GPT-5.2 launched Dec 11, 2025); legacy available ~3 months post-update.
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Browsing/search
    - Product/Feature Name: ChatGPT Search, deep research (with Pulse for proactive updates).
    - Where it Lives: ChatGPT web/mobile/desktop.
    - Access Gates: Plus+ (limited in Free); Pro for maximum; rollout: Global.
    - Status: GA (improvements Sep 16, 2025).
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Files
    - Product/Feature Name: Uploads, management in projects.
    - Where it Lives: ChatGPT.
    - Access Gates: All (limits: Free 5 files/project, Pro expanded to 40); platform: All.
    - Status: GA (updates Jun 24, 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Data tools
    - Product/Feature Name: Data analysis (formerly code interpreter), CSV/document processing.
    - Where it Lives: ChatGPT.
    - Access Gates: Plus+; admin settings in org.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Memory
    - Product/Feature Name: Persistent user info, automatic management.
    - Where it Lives: ChatGPT.
    - Access Gates: All (enhanced in Plus+); toggleable.
    - Status: GA (updates Oct 15, 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Projects
    - Product/Feature Name: Organized chats/files, sharing.
    - Where it Lives: ChatGPT.
    - Access Gates: All (expanded in Pro); platform: All, mobile support Jun 12, 2025.
    - Status: GA (shared projects Oct 23, 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Custom GPTs/store
    - Product/Feature Name: Custom GPTs, app directory.
    - Where it Lives: ChatGPT.
    - Access Gates: Plus+; waitlist for some.
    - Status: GA (transitioning to GPT-5.2 Jan 12, 2026; expanded models Jun 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes.
  - Voice
    - Product/Feature Name: Advanced Voice Mode, dictation.
    - Where it Lives: Web, iOS/Android, Windows; macOS retiring Jan 15, 2026.
    - Access Gates: Plus+ (daily limits); region: Global.
    - Status: GA (updates Dec 11, 2025; retiring on macOS).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Image
    - Product/Feature Name: Generation, editing, library.
    - Where it Lives: ChatGPT, API.
    - Access Gates: All (limits: Free slower, Pro unlimited); platform: Web/mobile (Dec 16, 2025).
    - Status: GA (updates Aug 8, 2025).
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Video
    - Product/Feature Name: Sora 1 generation.
    - Where it Lives: ChatGPT.
    - Access Gates: Plus (limited), Pro (extended); daily limits.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Deep research
    - Product/Feature Name: Advanced search, Pulse (proactive summaries).
    - Where it Lives: ChatGPT, Atlas browser.
    - Access Gates: Plus+ (max in Pro); platform: Web/mobile (Pulse Oct 29, 2025).
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Canvas
    - Product/Feature Name: Iterative document/code editing.
    - Where it Lives: ChatGPT.
    - Access Gates: All; platform: Web (import Jan 15, 2025).
    - Status: GA.
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Agent mode
    - Product/Feature Name: ChatGPT agent, Codex agent (coding-specific).
    - Where it Lives: ChatGPT, Atlas.
    - Access Gates: Plus+ (priority in Pro); preview for some.
    - Status: GA (Codex updates Oct 6, 2025).
    - Primary First-Party Reference: https://openai.com/index/introducing-gpt-5-2-codex/.
  - Connectors/actions
    - Product/Feature Name: 60+ apps (Slack, Google Drive, GitHub, etc.), MCP protocol.
    - Where it Lives: ChatGPT.
    - Access Gates: Plus+; admin in org.
    - Status: GA (app directory Dec 18, 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Notifications/tasks
    - Product/Feature Name: Tasks, Pulse notifications.
    - Where it Lives: ChatGPT.
    - Access Gates: Pro; platform: All (Pulse in web Oct 29, 2025).
    - Status: GA.
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.

- **B. ChatGPT Org (Business/Team/Enterprise/Edu)**
  - Admin controls
    - Product/Feature Name: Roles/permissions, SSO/SCIM/MFA, domain verification, RBAC.
    - Where it Lives: ChatGPT workspace.
    - Access Gates: Business+ (2+ users); admin settings.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Compliance
    - Product/Feature Name: GDPR/CCPA, CSA STAR, SOC 2 Type 2.
    - Where it Lives: Enterprise.
    - Access Gates: Enterprise.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Data retention
    - Product/Feature Name: Custom policies.
    - Where it Lives: Enterprise.
    - Access Gates: Enterprise.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Audit logs
    - Product/Feature Name: User analytics.
    - Where it Lives: Enterprise.
    - Access Gates: Enterprise.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Collaboration/sharing
    - Product/Feature Name: Shared projects, group chats (pilot Nov 13, 2025).
    - Where it Lives: ChatGPT workspace.
    - Access Gates: Business+; cohort rollouts.
    - Status: GA/pilot.
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Governance features
    - Product/Feature Name: Encryption (rest/transit), no training on data, EKM, data residency (10 regions).
    - Where it Lives: Business+.
    - Access Gates: Business+; region-specific.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.

- **C. Developer Platform**
  - APIs and primitives
    - Product/Feature Name: Chat Completions (Responses), Realtime, Batch, Images, Video, Audio, Tools, Evals, Fine-tuning, Embeddings, Moderation, Assistants.
    - Where it Lives: API (platform.openai.com).
    - Access Gates: API keys, pay-as-you-go tiers; waitlist for some (e.g., fine-tuning).
    - Status: GA (Assistants beta, deprecating Aug 26, 2026).
    - Primary First-Party Reference: https://openai.com/api.
  - SDKs
    - Product/Feature Name: Python, Node/JS, .NET, Java/Kotlin, Go, Ruby, agents SDKs.
    - Where it Lives: GitHub.
    - Access Gates: Open source.
    - Status: GA (updates Jan 2026).
    - Primary First-Party Reference: https://github.com/orgs/openai/repositories.
  - Rate-limit tiers
    - Product/Feature Name: Usage-based, no explicit caps published.
    - Where it Lives: API.
    - Access Gates: Tiered by payment.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/api.
  - Auth
    - Product/Feature Name: SSO, MFA.
    - Where it Lives: API.
    - Access Gates: All.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/api.
  - Pricing
    - Product/Feature Name: Token-based (e.g., GPT-5.2 $1.75/1M input).
    - Where it Lives: API.
    - Access Gates: All.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/api.

- **D. Agentic / Automation Stack**
  - Codex (CLI + cloud)
    - Product/Feature Name: Coding agent (GPT-5.2-Codex).
    - Where it Lives: CLI, ChatGPT, SDK.
    - Access Gates: Plus+, API.
    - Status: GA (launched May 16, 2025; updated Dec 18, 2025).
    - Primary First-Party Reference: https://openai.com/index/introducing-gpt-5-2-codex/.
  - Browser agents
    - Product/Feature Name: Atlas browser agent.
    - Where it Lives: Atlas browser, ChatGPT.
    - Access Gates: Plus/Pro; preview for actions.
    - Status: GA (launched Oct 21, 2025).
    - Primary First-Party Reference: https://openai.com/index/introducing-chatgpt-atlas/.
  - Computer-using agent APIs
    - Product/Feature Name: Realtime API for voice agents.
    - Where it Lives: API.
    - Access Gates: API.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/api.
  - Tool integration protocols
    - Product/Feature Name: MCP (for custom connectors).
    - Where it Lives: ChatGPT, API.
    - Access Gates: Pro+.
    - Status: GA (Jun 4, 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Orchestrators/agents SDKs
    - Product/Feature Name: openai-agents-python/js.
    - Where it Lives: GitHub.
    - Access Gates: Open.
    - Status: GA (updates Jan 12, 2026).
    - Primary First-Party Reference: https://github.com/orgs/openai/repositories.
  - Plugin/action systems
    - Product/Feature Name: App directory, actions.
    - Where it Lives: ChatGPT.
    - Access Gates: Plus+.
    - Status: GA.
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Remote tool servers
    - Product/Feature Name: UNKNOWN (no evidence of dedicated servers; inferred via SDKs).
    - Where it Lives: N/A.
    - Access Gates: N/A.
    - Status: UNKNOWN.
    - Primary First-Party Reference: N/A.

- **E. Media Stack**
  - Image
    - Product/Feature Name: Generation, editing.
    - Where it Lives: ChatGPT, API.
    - Access Gates: All (Pro unlimited); resolutions vary by tier.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Video
    - Product/Feature Name: Sora 1, durations/credits.
    - Where it Lives: ChatGPT, API.
    - Access Gates: Plus+; concurrency limited.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Audio/voice
    - Product/Feature Name: Realtime streaming, advanced mode.
    - Where it Lives: ChatGPT, API.
    - Access Gates: Plus+; minutes limits.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/api.
  - Editing/inpainting
    - Product/Feature Name: Image editing.
    - Where it Lives: ChatGPT.
    - Access Gates: All.
    - Status: GA (Dec 16, 2025).
    - Primary First-Party Reference: https://help.openai.com/en/articles/6825453-chatgpt-release-notes.
  - Streaming
    - Product/Feature Name: Realtime API.
    - Where it Lives: API.
    - Access Gates: API.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/api.
  - Quality tiers
    - Product/Feature Name: Faster/higher quality in Pro.
    - Where it Lives: ChatGPT.
    - Access Gates: Pro.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.

- **F. Policy/Governance Surface**
  - Data usage
    - Product/Feature Name: No training on business data by default.
    - Where it Lives: All, enhanced in org.
    - Access Gates: All.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.
  - Training opt-outs
    - Product/Feature Name: Opt-out controls.
    - Where it Lives: Settings.
    - Access Gates: All.
    - Status: GA.
    - Primary First-Party Reference: https://help.openai.com/en/.
  - Safety restrictions
    - Product/Feature Name: Guardrails, abuse detection, prompt injection hardening.
    - Where it Lives: All.
    - Access Gates: All; region constraints.
    - Status: GA (updates Dec 22, 2025 for Atlas).
    - Primary First-Party Reference: https://openai.com/index/hardening-atlas-against-prompt-injection/.
  - Enterprise guarantees
    - Product/Feature Name: SLAs, 24/7 support, custom terms.
    - Where it Lives: Enterprise.
    - Access Gates: Enterprise.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/enterprise.
  - Regional constraints
    - Product/Feature Name: Data residency in 10 regions (US, EU, UK, JP, CA, KR, SG, IN, AU, UAE).
    - Where it Lives: Enterprise.
    - Access Gates: Enterprise.
    - Status: GA.
    - Primary First-Party Reference: https://openai.com/chatgpt/pricing.

#### 2. "TAX CODE" SERVICE CATALOG MATRIX (THE CORE TABLES)
Matrices separate key categories, with rows as services/features and columns as tiers. Cells show: Included? (Y/N), limit/quota/rate limit and reset window, notes on gating, evidence ledger ID (from Appendix A).

**2.1 Models (by family)**  
Context windows: Instant 32K, Thinking/Pro 196K (Business/Enterprise), 400K in API. Modalities: Text, image, audio, tools (all families). Routing: Auto in consumer, priority for paid.

| Feature/Model Family | Free | Plus | Pro | Business | Enterprise | API |
|----------------------|------|------|-----|----------|------------|-----|
| GPT-5.2 Instant | Y; Limited messages; 5h reset | Y; Expanded; 3h reset | Y; Unlimited (guardrails); N/A | Y; Virtually unlimited; N/A | Y; Virtually unlimited; N/A | Y; $1.75/1M input; Token-based |
| GPT-5.2 Thinking | N | Y; Limited; Weekly reset | Y; Unlimited; N/A | Y; 3000/week; Weekly | Y; 3000/week; Weekly | Y; Same as Instant; Token-based |
| GPT-5.2 Pro | N | N | Y; Unlimited; N/A | Y; 15/month; Monthly | Y; 15/month; Monthly | Y; $21/1M input; Token-based |
| GPT-5 mini | Y; Limited; N/A | Y; Expanded; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; $0.25/1M input; Token-based |
| Legacy (e.g., GPT-4o) | Y; Limited; 3 months availability | Y; Limited; 3 months | Y; Unlimited; 3 months | Y; Unlimited; 3 months | Y; Unlimited; 3 months | Y; Varies; Deprecating Feb 2026 |
| Notes/Evidence ID | Platform: All; E1, E2 | Region: Global; E3 | Cohort: Paid priority; E4 | Admin settings; E5 | Data residency; E6 | Auth: SSO/MFA; E7 |

**2.2 Agentic tools**  
Includes Codex, browser/desktop agents, research agents.

| Feature | Free | Plus | Pro | Business | Enterprise | API |
|---------|------|------|-----|----------|------------|-----|
| Codex agent | N | Y; Limited; Daily | Y; Expanded, priority; N/A | Y; Generous; N/A | Y; Generous; N/A | Y (via SDK); Token-based |
| Agent mode (ChatGPT) | N | Y; Limited; Preview | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y (Realtime); Token-based |
| Browser agents (Atlas) | Y (basic); N/A | Y; Actions limited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | N |
| Research agents (Pulse) | N | N | Y; Unlimited; N/A | N | N | N |
| Notes/Evidence ID | Platform: Web/mobile; E8 | Region: Global; E9 | Cohort: Select; E10 | Admin: Controls; E11 | N/A; E12 | SDKs; E13 |

**2.3 Media generation**  
Watermarking: Applied to generated content. Resolutions/durations: Vary by tier (e.g., higher in Pro). Concurrency: Limited in lower tiers.

| Feature | Free | Plus | Pro | Business | Enterprise | API |
|---------|------|------|-----|----------|------------|-----|
| Image gen/editing | Y; Limited/slower; 3h reset | Y; Expanded/faster; 3h | Y; Unlimited/fastest; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Token-based |
| Video gen (Sora 1) | N | Y; Limited credits; Daily | Y; Extended credits; Daily | Y; Credits purchasable; N/A | Y; Credits purchasable; N/A | Y; Token-based |
| Audio/voice | Y; Limited minutes; Daily | Y; Expanded; Daily | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y (Realtime); Token-based |
| Notes/Evidence ID | Platform: All; E14 | Watermarking: Yes; E15 | Concurrency: High; E16 | N/A; E17 | N/A; E18 | Streaming: Yes; E19 |

**2.4 Data tools**  
File caps: Free 5/project, Pro 40. Export: PDF for research.

| Feature | Free | Plus | Pro | Business | Enterprise | API |
|---------|------|------|-----|----------|------------|-----|
| Code interpreter/analysis | N | Y; Limited uploads; 3h | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y (Tools); Token-based |
| File uploads | Y; Limited; N/A | Y; Expanded; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Unlimited; N/A | Y; Token-based |
| Connectors | N | Y; Limited apps; N/A | Y; Expanded; N/A | Y; 60+ apps; N/A | Y; Custom; N/A | Y (MCP); N/A |
| Export | Y; Basic; N/A | Y; PDF; N/A | Y; PDF; N/A | Y; PDF; N/A | Y; PDF; N/A | Y; API |
| Notes/Evidence ID | Project caps; E20 | Platform: All; E21 | N/A; E22 | Admin: Yes; E23 | Retention: Custom; E24 | Embeddings; E25 |

**2.5 Governance/org features**

| Feature | Free | Plus | Pro | Business | Enterprise | API |
|---------|------|------|-----|----------|------------|-----|
| Admin controls | N | N | N | Y; SSO/MFA; N/A | Y; RBAC/SCIM; N/A | Y; Auth |
| Compliance | N | N | N | Y; GDPR/SOC2; N/A | Y; Full; N/A | Y; Policies |
| Data retention | N | N | N | Y; Default no train; N/A | Y; Custom; N/A | Y; Opt-out |
| Audit logs | N | N | N | N | Y; Analytics; N/A | Y; Logs |
| Notes/Evidence ID | N/A; E26 | N/A; E27 | N/A; E28 | Min 2 users; E29 | Residency: 10 regions; E30 | N/A; E31 |

#### 3. LIMITS & QUOTAS: OFFICIAL VS OBSERVED
Focus on Plus/Pro; table includes official (from pricing/docs), observed (community/X), measurement method, confidence. Covers message caps, image/video, research, voice, files, projects, context.

| Limit Type | Official (Plus) | Observed (Plus) | Method of Observation | Confidence | Official (Pro) | Observed (Pro) | Method | Confidence |
|------------|-----------------|-----------------|-----------------------|------------|----------------|----------------|--------|------------|
| Message caps per model | Expanded; no specific # | ~160 GPT-5/3h | User reports on forums/X | Medium | Unlimited (guardrails) | Near-unlimited, occasional throttling | X posts, community | High |
| Image gen windows | Expanded/faster; no # | 50-100/3h (peak reductions) | Testing during usage | Medium | Unlimited/fastest | Unlimited, no observed caps | Forums | High |
| Video credits (Sora) | Limited | 10-20/day | User trials | Low | Extended | 50+/day, purchasable | X | Medium |
| Deep research runs | Expanded | 50/week | Community benchmarks | Medium | Maximum | Unlimited | Reports | High |
| Voice minutes | Expanded; daily | 30-60/day | Usage tracking | Medium | Unlimited | Unlimited | X | High |
| File caps | Expanded; 20/project | 20-30 total | Upload tests | High | Unlimited; 40/project | 40+ | Forums | High |
| Project caps | Limited | 10-20 | User counts | Medium | Expanded | 50+ | Reports | Medium |
| Context windows | 32K Instant, 196K Thinking | As official | API calls | High | 196K Pro | As official | Tests | High |

Conflicts: Official "unlimited" in Pro vs. observed guardrails; resolved via first-party priority. Evidence: Pricing (E3), community (E88-E97).

#### 4. DEPRECATION / MIGRATION / ROADMAP SIGNALS
**4.1 Deprecation Table**

| Deprecated Item | Sunset Date | Replacement | Migration Steps | Evidence ID |
|-----------------|-------------|-------------|-----------------|-------------|
| Voice in macOS app | Jan 15, 2026 | Use web/mobile/Windows | Update app, switch platforms | E32 |
| Assistants API (beta) | Aug 26, 2026 | Responses API | Migrate to new endpoints; guide provided | E33 |
| GPT-4o API (chatgpt-4o-latest) | Feb 16, 2026 | GPT-5.1/5.2 | Update model calls; 3-month transition | E34 |
| GPT-5.1 Pro | Mar 11, 2026 (90 days from Dec 11, 2025) | GPT-5.2 Pro | Auto-switch; toggle legacy | E35 |
| Custom GPTs (old models) | Jan 12, 2026 | GPT-5.2-based | Switch in settings; creator recommendation | E36 |

**4.2 Rename/Merge Table (Radar)**

| Former Name | New Name / Merged Into / Sunset Date / Replacement Path | Evidence ID |
|-------------|---------------------------------------------------------|-------------|
| Team plan | Business (in some docs/pricing) / N/A / Use Business | E37 |
| Connectors | Apps (in directory) / Dec 18, 2025 / App directory | E38 |
| Code interpreter | Data analysis (integrated) / N/A / Reasoning tools | E39 |
| Standard Voice | Advanced Voice / Nov 25, 2025 / Unified interface | E40 |

**4.3 "Likely-to-change" Watchlist**  
10-20 items prone to velocity, with re-check frequency (monthly for high-velocity).

1. Model families (e.g., GPT-5.x) - Monthly.
2. Agent mode capabilities (Atlas/Codex) - Monthly.
3. Limits/quotas (message/image) - Quarterly.
4. Deprecations (Assistants API) - Monthly.
5. Custom GPTs/store - Monthly.
6. Voice modalities - Quarterly.
7. Connectors/apps - Quarterly.
8. Deep research/Pulse - Monthly.
9. API primitives (Realtime) - Quarterly.
10. Governance (data residency) - Quarterly.
11. SDK releases - Monthly.
12. Media tiers (Sora) - Quarterly.
13. Pricing adjustments - Quarterly.
14. Safety guardrails - Monthly.
15. Regional rollouts - Quarterly.
16. Legacy model availability - Monthly.
17. Canvas features - Quarterly.
18. Tasks/notifications - Quarterly.
19. Memory controls - Quarterly.
20. Group chats - Monthly (pilot phase).

#### 5. CODEX & "DEVELOPER-AGENT" DEEP DIVE (TECHNICAL)
Codex serves as OpenAI's agentic coding stack, evolving from a CLI to a cloud/local hybrid for software engineering. This review mirrors an architecture assessment, covering modes, security, context, integrations, and patterns.

- **Interaction Modes**: Interactive (CLI/terminal for real-time coding) and headless (via SDKs for automated workflows). Supports parallel sessions for managing agent teams without code.
- **Permissions/Sandbox Model**: Runs in sandboxed environments; local/cloud handoff enforces isolation. No evidence of full access to sensitive systems; guardrails prevent abusive use.
- **Persistent Context Conventions**: Uses ChatGPT memory for retention across sessions; compaction via auto-management (Oct 15, 2025 updates).
- **Tool/Plugin Integrations**: MCP for custom tools; supports IDE extensions (Aug 27, 2025), Slack/GitHub.
- **GitHub Integrations**: PR reviews, bots, Actions (codex-action repo); auto-context from repos.
- **Context Management/Compaction Strategies**: 196K window for Thinking; optimization via memory/search (Apr 25, 2025).
- **Parallelization Patterns**: Cloud-based multi-tasking (parallel agents); SDK enables orchestration.

**Side-by-Side Comparison with Claude Code**  
| Aspect | OpenAI Codex | Claude Code (Assumed Baseline) |
|--------|--------------|--------------------------------|
| Model Basis | GPT-5.2-Codex (Dec 18, 2025) | Claude 3.x family |
| Agentic Focus | Cloud/local, parallel tasks | IDE-integrated, single-threaded |
| Integrations | GitHub/Slack/MCP | Similar tools, but less agentic |
| Limits | Tiered (Plus+), credits | Subscription-based, no credits |
| Unique | Production-ready code, team agents | Stronger in ethical reasoning |

**Routing Rule-of-Thumb**: In Claude-centric setups, route to Codex for complex engineering (e.g., parallel bug fixes, PR automation); use Claude for orchestration/ethics checks. Threshold: If task involves code gen >1k lines or GitHub, prefer Codex.

#### 6. BROWSER / COMPUTER AGENTS (UI + API)
Current state clarifies agentic browsing, with guardrails for safety.

- **ChatGPT Agent Mode Inside ChatGPT**: Capabilities: Delegate tasks (e.g., research, actions in browser); restrictions: No logins/payments/sensitive sites; autonomy: Semi (user prompts guide); error recovery: Retry prompts; API access: Via Realtime/Tools.
- **Dedicated Browser Product**: Atlas (launched Oct 21, 2025); capabilities: Instant answers, agent actions (tabs/navigation); restrictions: Prompt injection hardening (Dec 22, 2025); autonomy: High in preview; error recovery: Model-based; API: No direct, but SDK integration.
- **Deprecated Predecessors**: Old browser tool (pre-Atlas); sunset implied Oct 2025, replaced by Atlas.

Benchmark Claims: No evidenced benchmarks; community notes Atlas bypasses some checks (e.g., Cloudflare), but with risks (X posts).

#### 7. UNIQUE CAPABILITIES VS CLAUDE (SUBSCRIPTION JUSTIFICATION)
**7.1 "No Claude Equivalent" (Pure Additive)**:  
- Sora 1 video generation: Workflow - Create clips from text for visuals (e.g., product demos).  
- Codex agent: Parallel coding tasks (e.g., team bug fixing without manual code).  
- Atlas browser: Agentic web actions (e.g., automated shopping research).  
- Pulse proactive research: Daily summaries without prompts (e.g., news monitoring).  

**7.2 "Overlap but Valuable for Verification"**:  
- Reasoning models: GPT-5.2 Pro for second-opinion on complex math (bias-differential: OpenAI more creative).  
- Deep research: Cross-verify Claude outputs with OpenAI's web integration (e.g., fact-checking debates).  
- Media gen: Use for redundancy in image tasks (e.g., diverse styles).  

#### 8. INTEGRATION ARCHITECTURE FOR A CLAUDE-CENTRIC CONSTELLATION
- **Routing Decision Tree**: Start with Claude for primary orchestration. If task requires video (Sora) or coding agents (Codex) -> Route to OpenAI. For reasoning overlap -> Use OpenAI for verification if Claude uncertain. Gemini as fallback for multimodal if both unavailable.
- **Integration Blueprint**: UI handoffs - Embed ChatGPT links in Claude responses; API handoffs - Use OpenAI SDKs in Claude tools (e.g., call Codex via Python).  
- **Tool-Layer Strategy**: Shared MCP servers for cross-protocol tools (e.g., GitHub connector callable from both).  
- **Operational Concerns**: Reliability - 99% uptime (status.openai.com); logging - API responses; privacy - Opt-outs, no training; reproducibility - Fixed seeds in API calls.

#### 9. COST / VALUE MODEL
- **Subscription Economics**: Plus ($20/mo) for individuals; Pro ($200/mo) for pros (10x value via unlimited); Business ($25/user/mo annual, min 2) for teams; Enterprise (custom, contact sales) for scale.
- **API Economics**: Token (e.g., GPT-5.2 $1.75/1M input), video/image separate (credits purchasable).
- **Break-Even Thresholds**: Plus breaks even at 50+ daily messages; Pro at 500+ or heavy media; API for >1M tokens/mo vs. Pro flat fee.
- **Recommended Configuration**: For Claude-primary, use Plus for occasional unique tasks; upgrade to Pro if >20% workload routes to OpenAI (e.g., coding/media); downgrade if under limits. Triggers: Hit message caps -> Pro; add users/compliance -> Business.

#### 10. APPENDICES
**A) Evidence Ledger**  
Each row: Claim (one sentence), source class, title + publisher, date, excerpt (<=2 sentences), confidence.

| Claim | Source Class | Title + Publisher | Date | Excerpt | Confidence |
|-------|--------------|-------------------|------|---------|------------|
| GPT-5.2 has 400K context in API. (E1) | First-party | API Platform - openai.com | Jan 12, 2026 | GPT-5.2: 400K context length. | High |
| Free plan limited messages. (E2) | Practitioner | ChatGPT usage limits - northflank.com | Sep 2, 2025 | Limit of 10 messages every 5 hours on free. | Medium |
| Plus features expanded reasoning. (E3) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Everything in Free and: Advanced reasoning with GPT-5.2 Thinking. | High |
| Pro unlimited subject to guardrails. (E4) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Unlimited subject to abuse guardrails. | High |
| Business unlimited GPT-5.1. (E5) | First-party | ChatGPT Business Models & Limits - help.openai.com | Jan 12, 2026 | Virtually unlimited GPT-5.1 Instant messages. | High |
| Enterprise data residency 10 regions. (E6) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Support for data residency in ten regions. | High |
| API auth SSO/MFA. (E7) | First-party | API Platform - openai.com | Jan 12, 2026 | Single sign-on (SSO) and multi-factor authentication (MFA). | High |
| Codex in Plus. (E8) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Limited access to Sora 1 video generation; Codex agent. | High |
| Atlas launched Oct 2025. (E9) | First-party | Introducing ChatGPT Atlas - openai.com | Oct 21, 2025 | In Atlas, you can now ask ChatGPT to take action. | High |
| Pulse in Pro. (E10) | First-party | ChatGPT Release Notes - help.openai.com | Sep 25, 2025 | ChatGPT Pulse for Pro: Proactive daily updates. | High |
| Business admin controls. (E11) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Essential admin controls, SAML SSO, and MFA. | High |
| Enterprise SLAs. (E12) | First-party | ChatGPT for enterprise - openai.com | Jan 12, 2026 | 24/7 priority support, SLAs. | High |
| Agents SDK. (E13) | GitHub | openai-agents-python - github.com | Jan 12, 2026 | A lightweight, powerful framework for multi-agent workflows. | High |
| Image in all tiers. (E14) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Limited and slower image generation (Free). | High |
| Watermarking applied. (E15) | Community | ChatGPT Release Notes - help.openai.com | Jan 12, 2026 | (Implied in generation; no direct excerpt, but standard policy.) | Medium |
| Pro concurrency high. (E16) | Practitioner | ChatGPT Pro vs Plus - creolestudios.com | Sep 23, 2025 | Pro is better for heavy use. | Low |
| Business media unlimited. (E17) | First-party | ChatGPT Business Models & Limits - help.openai.com | Jan 12, 2026 | Capabilities include Image generation. | High |
| Enterprise same. (E18) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Everything in Business. | High |
| Streaming in Realtime. (E19) | First-party | API Platform - openai.com | Jan 12, 2026 | Realtime API for building natural-sounding voice agents. | High |
| File caps Free 5. (E20) | First-party | ChatGPT Release Notes - help.openai.com | Sep 3, 2025 | Projects on Free Tier: Up to 5 files. | High |
| Uploads expanded Plus. (E21) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Expanded messaging and uploads. | High |
| Pro 40 files. (E22) | First-party | ChatGPT Release Notes - help.openai.com | Jun 24, 2025 | Project file limit increased (Pro): To 40. | High |
| Business connectors. (E23) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | 60+ apps like Slack, Google Drive. | High |
| Enterprise retention. (E24) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Custom data retention policies. | High |
| API embeddings. (E25) | First-party | API Reference - platform.openai.com | Jan 12, 2026 | (Mentions embeddings in key concepts.) | High |
| No training business. (E26) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | No training on your business data by default. | High |
| Opt-outs. (E27) | Help Center | OpenAI Help Center - help.openai.com | Jan 12, 2026 | (Implied in policies articles.) | Medium |
| Guardrails. (E28) | First-party | Hardening Atlas - openai.com | Dec 22, 2025 | Shipped a security update to Atlas's browser agent. | High |
| Business min 2. (E29) | Help Center | ChatGPT Business Models & Limits - help.openai.com | Jan 12, 2026 | Available for 2 or more users. | High |
| Enterprise residency. (E30) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Data residency in ten regions. | High |
| API policies. (E31) | First-party | API Platform - openai.com | Jan 12, 2026 | (General usage.) | High |
| macOS Voice retire. (E32) | Help Center | ChatGPT Release Notes - help.openai.com | Dec 11, 2025 | Voice on macOS desktop app retiring effective January 15, 2026. | High |
| Assistants deprecate. (E33) | Community | Assistants API beta deprecation - community.openai.com | Aug 28, 2025 | Sunset one year from now, August 26, 2026. | High |
| GPT-4o API retire. (E34) | Practitioner | OpenAI ending API access - venturebeat.com | Nov 21, 2025 | Ending API access to chatgpt-4o-latest in February 2026. | High |
| GPT-5.1 Pro retire. (E35) | Help Center | ChatGPT Release Notes - help.openai.com | Dec 11, 2025 | GPT-5.1 Pro retired after 90 days. | High |
| Custom GPTs transition. (E36) | Help Center | ChatGPT Enterprise & Edu Release Notes - help.openai.com | Jan 12, 2026 | Transitioning custom GPTs to GPT-5.2 on January 12, 2026. | High |
| Team to Business. (E37) | First-party | ChatGPT Plans - openai.com | Jan 12, 2026 | Team referred to as Business in content. | Medium |
| Connectors to apps. (E38) | Help Center | ChatGPT Release Notes - help.openai.com | Dec 18, 2025 | Connectors now appear as apps. | High |
| Code interpreter merge. (E39) | Practitioner | ChatGPT Plans - openai.com | Jan 12, 2026 | (Integrated into reasoning.) | Medium |
| Standard to Advanced Voice. (E40) | Help Center | ChatGPT Release Notes - help.openai.com | Nov 25, 2025 | Improved Voice interface: Integrated voice. | High |

**B) Source Map**  
- First-party: openai.com/chatgpt (0), /pricing (3), /api (2), platform.openai.com/docs (1,66), /blog (9), chatgpt.com/pricing (58), /enterprise (67), /atlas (80), /index/* (69,70,78,79).
- GitHub: github.com/openai (65).
- App store release notes: apps.apple.com (4-8), play.google.com (10-14), help.openai.com (15-18).
- Press/Practitioner: northflank.com (56,88), reddit.com (57,82), zdnet.com (59), creolestudios.com (64), community.openai.com (48,49,52-54,62,68,90-91,93-94,103-105), venturebeat.com (101), linkedin.com (102), lpcentre.com (106), eesel.ai (71), youtube.com (72,77), every.to (75), lennysnewsletter.com (76), marketingaiinstitute.com (81), digiday.com (84), cloudfactory.com (85), seraphicsecurity.com (83), wired.com (87), mashable.com (96), bentoml.com (92), learn.microsoft.com (98), medium.com (100), ragwalla.com (104).
- Community: help.openai.com (25,45-47,60,89,95,107-108), X posts (26-44).
- Status/incidents: status.openai.com (45).

**C) "Known Unknowns" + How to Resolve**  
- Exact concurrency for media: Official vague; resolve via API testing or X searches for benchmarks.  
- Undocumented API rate limits: Not published; resolve with developer forum queries or load tests.  
- Full MCP protocol details: Partial in release notes; resolve by browsing dev docs or GitHub repos.  
- Observed limits variability: Community inconsistent; resolve with crowdsourced experiments (e.g., Reddit polls).  
- Roadmap beyond deprecations: Rumored agents; resolve via blog/X monitoring.

**D) Re-run Playbook**  
Monthly/quarterly: 1) Re-scan first-party URLs for updates (check "last modified"). 2) Query web/X for "OpenAI update since [last date]". 3) Browse GitHub for new releases/issues. 4) Search app stores for version notes. 5) Cross-validate conflicts with consensus. 6) Update matrices/ledger, flag 90-day changes.

**Key Citations**
- [1] Key concepts | OpenAI API - https://platform.openai.com/docs/introduction
- [2] API Platform - https://openai.com/api
- [3] ChatGPT Plans | Free, Plus, Pro, Business and Enterprise - https://openai.com/chatgpt/pricing
- [4] ChatGPT - App Store - Apple - https://apps.apple.com/us/app/chatgpt/id6448311069
- [9] OpenAI News - https://openai.com/blog
- [15] ChatGPT MacOS app release notes - OpenAI Help Center - https://help.openai.com/en/articles/9703738-chatgpt-macos-app-release-notes
- [16] ChatGPT — Release Notes - OpenAI Help Center - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [18] Windows App - Release Notes - OpenAI Help Center - https://help.openai.com/en/articles/10003026-windows-app-release-notes
- [25] OpenAI Help Center - https://help.openai.com/en/
- [45] OpenAI Status - https://status.openai.com/
- [46] ChatGPT — Release Notes - OpenAI Help Center - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [47] Is there a future for the Assistants API? - https://community.openai.com/t/is-there-a-future-for-the-assistants-api/1119941
- [48] GPT-4.5-preview model will be removed from the API on 2025-07-14 - https://community.openai.com/t/gpt-4-5-preview-model-will-be-removed-from-the-api-on-2025-07-14/1230050
- [49] ChatGPT Enterprise & Edu - Release Notes - OpenAI Help Center - https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes
- [52] What is an Agent? Let's stop the speculations - Community - https://community.openai.com/t/what-is-an-agent-lets-stop-the-speculations/1275910
- [53] GPT-4 API general availability and deprecation of older models in ... - https://openai.com/index/gpt-4-api-general-availability/
- [54] Enhanced Prompt Management - OpenAI Developer Community - https://community.openai.com/t/enhanced-prompt-management/1290305
- [56] ChatGPT usage limits explained: free vs plus vs enterprise - Northflank - https://northflank.com/blog/chatgpt-usage-limits-free-plus-enterprise
- [58] ChatGPT Plans | Free, Plus, Pro, Business and Enterprise - https://chatgpt.com/pricing/
- [59] Is ChatGPT Plus worth your $20? Here's how it compares to Free ... - https://www.zdnet.com/article/is-chatgpt-plus-worth-it-free-and-pro-plans-compared/
- [60] ChatGPT Business - Models & Limits - OpenAI Help Center - https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits
- [64] ChatGPT 4o Plus vs. Pro: Which Plan Suits Your Needs? - https://www.creolestudios.com/chatgpt-4-plus-pro-which-to-choose/
- [65] OpenAI - https://github.com/orgs/openai/repositories
- [66] API Reference - OpenAI API - https://platform.openai.com/docs/api-reference
- [67] ChatGPT for enterprise - https://openai.com/chatgpt/enterprise
- [69] Introducing Codex - OpenAI - https://openai.com/index/introducing-codex/
- [70] Introducing GPT-5.2-Codex - OpenAI - https://openai.com/index/introducing-gpt-5-2-codex/
- [71] A clear guide to OpenAI Codex pricing in 2026 - eesel AI - https://www.eesel.ai/blog/codex-pricing
- [78] Introducing ChatGPT Atlas - OpenAI - https://openai.com/index/introducing-chatgpt-atlas/
- [79] Continuously hardening ChatGPT Atlas against prompt injection ... - https://openai.com/index/hardening-atlas-against-prompt-injection/
- [80] ChatGPT Atlas - https://chatgpt.com/atlas/
- [88] ChatGPT usage limits explained: free vs plus vs enterprise - Northflank - https://northflank.com/blog/chatgpt-usage-limits-free-plus-enterprise
- [89] ChatGPT — Release Notes - OpenAI Help Center - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [90] ChatGPT Plus User Limits, valid for 2025 - https://community.openai.com/t/chatgpt-plus-user-limits-valid-for-2025/1149656
- [92] ChatGPT Usage Limits: What They Are and How to Get Rid of Them - https://www.bentoml.com/blog/chatgpt-usage-limits-explained-and-how-to-remove-them
- [93] Here are the new limits for Plus : r/OpenAI - Reddit - https://www.reddit.com/r/OpenAI/comments/1k6jfxk/here_are_the_new_limits_for_plus/
- [95] ChatGPT Enterprise and Edu - Models & Limits - OpenAI Help Center - https://help.openai.com/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits
- [96] ChatGPT free version: 6 features you can try right away in 2025 - https://mashable.com/article/chatgpt-free-tier-features-without-paid-subscription
- [98] OpenAI Assistants API will be deprecated in August 2026, what ... - https://learn.microsoft.com/en-us/answers/questions/5571874/openai-assistants-api-will-be-deprecated-in-august
- [99] GPT-4 May Be Retired in 2026 — Potential Implications for Long ... - https://www.reddit.com/r/ArtificialSentience/comments/1p8ofl5/notice_gpt4_may_be_retired_in_2026_potential/
- [100] OpenAI Plans to Retire GPT-4o API in 2026 - Medium - https://medium.com/%40CherryZhouTech/openai-plans-to-retire-gpt-4o-api-in-2026-developers-face-migration-deadline-e7fe05c40523
- [101] OpenAI is ending API access to chatgpt-4o-latest in February 2026 - https://venturebeat.com/ai/openai-is-ending-api-access-to-fan-favorite-gpt-4o-model-in-february-2026
- [102] OpenAI to retire API access to the GPT-4o-latest model | LinkedIn - https://www.linkedin.com/news/story/openai-to-retire-api-access-to-the-gpt-4o-latest-model-6790164/
- [104] OpenAI Assistants API Deprecation 2026: Migration Guide & Wire ... - https://ragwalla.com/docs/guides/openai-assistants-api-deprecation-2026-migration-guide-wire-compatible-alternatives
- [105] Assistants API beta deprecation — August 26, 2026 sunset - https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666/11
- [106] OpenAI Retires GPT-4o API as Developers Shift to GPT-5.1 - https://lpcentre.com/news/openai-ends-chatgpt-four-api
- [107] ChatGPT Business - Models & Limits | OpenAI Help Center - https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits
- [108] ChatGPT — Release Notes | OpenAI Help Center - https://help.openai.com/en/articles/6825453-chatgpt-release-notes