# CLUSTERING TASK — Adjudicator (Codex)

## Context
You are in `/Users/system/syncrescendence/corpus/`. There are ~11,712 files. We need to classify every file by its **semantic topic** — what the file is ABOUT, not what type of file it is.

## Your Assignment
You are taking files **04001 through 08000**. For each file:
1. Read the first 10-20 lines
2. Determine what SUBJECT MATTER it covers
3. Assign it a granular topic tag

## Topic Tags (use these, add new ones if needed)
### AI Platforms
- `claude-code` — About Claude Code specifically (setup, tips, features, configs)
- `openclaw` — About OpenClaw specifically (setup, skills, configs, architecture)
- `codex` — About OpenAI Codex specifically
- `gemini` — About Google Gemini specifically
- `chatgpt` — About ChatGPT specifically
- `cursor` — About Cursor IDE
- `other-ai-tool` — Other specific AI tools

### AI Concepts
- `ai-agents` — Multi-agent systems, agent architectures, agent frameworks
- `ai-coding` — AI-assisted coding, vibe coding, AI dev workflows
- `prompt-engineering` — Prompting techniques, system prompts, prompt design
- `ai-memory` — RAG, vector stores, embeddings, agent memory
- `ai-safety` — Alignment, guardrails, red teaming, AI risk
- `ai-models` — Model comparisons, benchmarks, model releases, scaling laws
- `ai-business` — AI startups, AI economics, AI market dynamics
- `mcp` — Model Context Protocol, tool use, function calling
- `ai-video` — AI video generation, VFX, visual AI
- `ai-image` — AI image generation
- `ai-general` — General AI news/commentary not fitting above

### Knowledge Domains
- `geopolitics-us-china` — US-China relations
- `geopolitics-iran` — Iran, Middle East conflicts
- `geopolitics-russia` — Russia, Ukraine
- `geopolitics-grand-strategy` — Grand strategy, world order, military theory
- `geopolitics-other` — Other geopolitical topics
- `economics-macro` — Macroeconomics, markets, monetary policy
- `economics-investing` — Investing, trading, portfolio strategy
- `economics-startups` — Startups, venture capital, entrepreneurship
- `physics-cosmology` — Universe, dark energy, quantum mechanics, astrophysics
- `biology-evolution` — Evolution, genetics, organisms
- `biology-neuroscience` — Brain, consciousness from neuroscience angle
- `philosophy-consciousness` — Consciousness, metaphysics, Vedanta, phenomenology
- `philosophy-epistemology` — Knowledge theory, truth, reasoning
- `history` — Historical topics
- `self-improvement` — Focus, discipline, learning, habits, productivity
- `content-creation` — Content strategy, personal branding, creator economy
- `design` — UI/UX, visual design, design systems
- `infrastructure` — SSH, networking, servers, DevOps, launchd
- `software-engineering` — Non-AI programming, architecture, systems design

### Syncrescendence Internal
- `sn-handoff` — Session handoffs (CC## files)
- `sn-task` — Task dispatch files
- `sn-confirm` — Confirmation receipts
- `sn-result` — Result files from agent execution
- `sn-prompt` — Prompts for triangulation
- `sn-certescence` — Clarescence/ascertescence session artifacts
- `sn-config` — Internal configs, YAML, coordination files
- `sn-script` — Operational scripts (.sh, .py)
- `sn-watchdog` — Watchdog/health monitoring artifacts
- `sn-canon` — Canon documents, ontology, principles
- `sn-rosetta` — Terminology reconciliation
- `sn-system-prompt` — Our own system prompts for constellation agents
- `sn-architecture` — Syncrescendence architecture docs
- `sn-pipeline` — Ingestion/processing pipeline docs
- `sn-atom` — Atom extraction files and JSONL atom records
- `sn-other` — Other syncrescendence operational files

## Output Format
Produce a TSV (tab-separated) file. One line per file:
```
filename[TAB]topic[TAB]secondary_topic_if_any[TAB]one_line_summary
```

Example:
```
04001.md	ai-agents	ai-coding	Thread about agent-assisted development workflows
04050.jsonl	economics-macro		Atoms about Federal Reserve policy shifts
```

## Rules
- Every file gets exactly ONE primary topic
- Secondary topic only if strongly relevant
- If a file is an atom extraction (`# Extraction:` header), tag it by what the SOURCE is about, not as "extraction"
- If a file is JSONL, read the `content` field to determine topic
- Speed over perfection — we need coverage on 4,000 files
- Write output to `/Users/system/syncrescendence/corpus/CLUSTER-MAP-ADJUDICATOR.tsv`
