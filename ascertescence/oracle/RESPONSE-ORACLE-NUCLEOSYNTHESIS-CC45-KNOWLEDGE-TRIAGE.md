### Topic→Attractor Mapping

The mappings cluster related topics into the fewest attractors possible while respecting conceptual fit—prioritizing agents/ for AI coordination themes, skills/ for practical techniques, infrastructure/ for tools and setups, ontology/ for schemas and philosophies, and knowledge/ as the general sink for uncategorized residues like career or economics. Subdirectories are introduced sparingly to maintain hierarchy without fragmentation; for instance, skills/prompting/ groups prompting workflows. Ambiguities (e.g., "framework" could lean philosophical or engineering) resolve toward praxis-oriented attractors like skills/ unless ontology/ better captures definitional aspects. This empties uncategorized/ by routing all 1,773 SOURCE files (and paired META) into these paths.

| Source Topic(s) | → Attractor Directory | Rationale |
|-----------------|-----------------------|-----------|
| ai-agents | agents/ | Direct match to agent offices and coordination; core to multi-agent systems. |
| ai-engineering, architecture, framework | skills/ai-engineering/ | Engineering practices and architectural patterns fit as practical skills; subdirectory isolates from general skills like testing. |
| context-management, memory-management | memory/ | Both involve state and recall mechanisms, aligning with DYN-* state and session logs. |
| extended-thinking | consciousness/ | Philosophical extension of cognition ties to capabilities in consciousness/. |
| claude, claude-code, anthropic | infrastructure/claude/ | Claude-specific tools and code as infrastructure configs; subdirectory for model-specific isolation. |
| automation, ai-workflow | agents/automation/ | Workflow automation as agent coordination; subdir prevents bloating root agents/. |
| api | infrastructure/api/ | API integrations as deployment and config tools. |
| gemini | infrastructure/gemini/ | Model-specific like Claude; fits infrastructure for launch and tools. |
| openai, gpt | infrastructure/openai/ | Parallel to gemini/; groups OpenAI ecosystem. |
| developer-tools, cli-tools, git | infrastructure/developer-tools/ | Broad tools for devs, including CLI and version control, as infrastructure essentials. |
| best-practices, testing | skills/best-practices/ | Praxis-oriented guidelines and testing as skill-building docs. |
| prompting | skills/prompting/ | Core prompting techniques as practical skills. |
| openclaw, clawdbot | infrastructure/openclaw/ | Custom bots and dbs as infrastructure CLI/tools. |
| philosophy, consciousness | ontology/philosophy/ | Definitional and schema work in ontology/; consciousness as philosophical reference. |
| rag | skills/rag/ | Retrieval-augmented generation as a technique in skills/. |
| vibe-coding | skills/vibe-coding/ | Aesthetic coding practices as a praxis subset. |
| research | certescence/research/ | Verification and council templates extend to research methods. |
| career | knowledge/general/ | No strong fit elsewhere; general knowledge catch-all for professional advice. |
| product-development | skills/product-development/ | Development cycles as applied skills. |
| codex | infrastructure/codex/ | Legacy OpenAI tool; fits infrastructure like APIs. |
| tutorial | feedcraft/tutorials/ | Ingestion pipelines can include tutorial scripts for onboarding. |
| economics | sovereignty/economics/ | Decision-making and directives influenced by economic motives. |
| homelab | infrastructure/homelab/ | Setup and deployment for personal labs. |

### Expiry Assessment

Set a stale threshold at sources dated before 2024-01-01, given AI's rapid pace—models like GPT-4 (2023) supersede much pre-2024 content, while 2024+ captures Grok/Claude/Gemini evolutions. For signal_tier (assuming a 1-5 scale in frontmatter, with 1 low and 5 high), mark low-value if ≤2, as this likely flags speculative or unverified atoms. Noise-prone combos include x-thread or x-article before 2025 (ephemeral discourse often outdated by model updates) and youtube-interview/panel before 2024 (speculative talks lose edge post-deployment). Move expired sources to knowledge/archive/ rather than delete, preserving reversibility for rare revivals while clearing active paths.

### META Pairing Rule

META files should follow their paired SOURCE to the same attractor directory, landing in a meta/ subdirectory (e.g., agents/meta/ alongside agents/raw/ for sources). This decentralizes for contextual proximity—extractions stay with origins for easy pairing—avoiding centralized bloat that could orphan files during queries.

### The 265 Notebooks

Merge notebooks into the same attractor directories as routed sources, dropping knowledge/ subdir prefixes if redundant (e.g., move knowledge/infrastructure/cli/claude-code/notebooks/ contents directly into infrastructure/claude/). This unifies by concept, leveraging filename topics to align with frontmatter-driven sources, preventing knowledge/ from siloing exemplars.