---
id: ref-web_app_memory_audit
kind: reference
scope: engine
target: engine
linear: SYN-38
intention: INT-1604
version: 1.0.0
status: canonical
created: 2026-02-10
updated: 2026-02-10
---

# Web App Memory Architecture Audit
## SYN-38 | INT-1604

**Author**: memory-auditor agent (Commander delegation)
**Date**: 2026-02-10
**Status**: COMPLETE v1.0.0

---

### Executive Summary

The AI memory landscape as of February 2026 is fragmented across fundamentally incompatible architectures. Cloud platforms (Claude, ChatGPT, Gemini) each implement proprietary memory systems with varying degrees of export capability, while self-hosted infrastructure (Mem0, Graphiti, QMD) provides full data sovereignty at the cost of operational overhead. The single most important finding: **Claude's API-accessible memory tool and the self-hosted stack (Graphiti + Mem0 + QMD) are the only systems offering genuine portability** -- ChatGPT memories are consumer-only with no API access, and Gemini's memory is all-or-nothing with no selective export. The Syncrescendence project is well-positioned because its heaviest memory investments are already in portable, self-hosted infrastructure.

---

### Platform Comparison Matrix

| Platform | Memory Type | Persistence | Capacity | Export | API Access | Lock-in Risk | Syncrescendence Usage |
|----------|-------------|-------------|----------|--------|------------|--------------|----------------------|
| **Claude Code** | File-based hierarchy (CLAUDE.md) | Permanent (disk + git) | Unlimited (filesystem) | Full (git-tracked) | N/A (filesystem) | **NONE** | PRIMARY -- repo root + memory/ |
| **Claude.ai** | Memory summary + project knowledge | Cross-conversation | ~200K tokens/project | Full (data export + memory import/export) | Yes (Memory Tool beta) | **LOW** | Active -- Syncrescendence project |
| **ChatGPT** | Saved memories + project files | Cross-conversation | ~6,000 tokens (memories), 512MB/file | Partial (data export, no API) | **NO** | **HIGH** | Psyche/CTO via OpenClaw |
| **Gemini Web** | Saved Info + Gems + Personal Intelligence | Cross-conversation | 1M token context, 10 files/Gem | All-or-nothing | **NO** | **MEDIUM** | Cartographer surveys |
| **NotebookLM** | Notebook-scoped sources | Per-notebook, persistent | 1M token context, 50+ sources | Download outputs only | Limited (Discovery Engine API) | **MEDIUM** | Not active |
| **Notion** | Database-backed pages | Permanent | Unlimited (plan-dependent) | Full (API + bulk export) | Yes (full CRUD API + MCP) | **LOW** | MCP configured (not loading) |
| **Mem0** | Hybrid vector + graph + KV | Permanent (Qdrant-backed) | 44 memories (current), scalable | Full (self-hosted, Qdrant export) | Yes (REST API) | **NONE** | LIVE -- OpenClaw auto-capture |
| **Graphiti** | Temporal knowledge graph | Permanent (Neo4j-backed) | Unlimited (graph DB) | Full (Neo4j dump, Cypher export) | Yes (REST + MCP) | **NONE** | LIVE -- shared KG, 9 tools |
| **QMD** | BM25 local search index | Hourly refresh | 693 vault .md files | Full (it IS the vault) | Yes (make search) | **NONE** | LIVE -- local corpus search |

---

### Detailed Assessments

---

#### 1. Claude Code (Anthropic CLI)

**Architecture**

Claude Code implements the most sophisticated hierarchical memory system of any AI coding tool, with 8 distinct layers:

1. **User Global** (`~/.claude/CLAUDE.md`) -- account-wide preferences
2. **Organization Policy** (`/Library/Application Support/ClaudeCode/CLAUDE.md`) -- IT-managed
3. **Project Root** (`./CLAUDE.md`) -- git-tracked project context
4. **Project Rules** (`.claude/rules/*.md`) -- conditional path-based rules
5. **Project Local** (`./CLAUDE.local.md`) -- personal, gitignored
6. **Subdirectory** (nested `CLAUDE.md` files) -- on-demand loading
7. **Auto Memory** (`~/.claude/projects/<project>/memory/`) -- Claude-written notes
8. **Session** (ephemeral conversation context) -- lost on exit

As of Claude Code v2.1.33 (February 2026), subagent memory frontmatter gives each agent team member its own persistent markdown-based knowledge store.

**Capacity**

- Filesystem-bound: no inherent limits beyond disk space
- Context window: ~200K tokens per session
- Auto memory directory: currently 10 files in Syncrescendence project (`~/.claude/projects/-Users-home/memory/`)
- CLAUDE.md at repo root: 3,912 words, loaded at every session start

**Portability**: **FULL**

All memory is file-based and git-tracked. The `CLAUDE.md` hierarchy is plain Markdown -- readable by any system, portable to any platform. Auto-memory files are stored locally at `~/.claude/projects/`. No vendor lock-in whatsoever.

**Lock-in Risk**: **NONE**

Memory exists as files on disk. If Anthropic disappeared tomorrow, every byte of Claude Code memory would remain accessible as plain text files. This is the gold standard for memory portability.

**Syncrescendence Usage**

- `CLAUDE.md` at repo root: 3.0.0, constitutional rules, directory structure, protocols
- `~/.claude/projects/-Users-home/memory/MEMORY.md`: 400+ lines of strategic context
- 10 memory files covering MCP config, cockpit fixes, frontier landscape, narrative DNA, paths, projects, claudecron, emacs layer, ontology
- `.claude/rules/` directory for path-conditional context
- 6 hooks (session_log, ajna_pedigree, create_execution_log, pre_compaction, intent_compass)

---

#### 2. Claude.ai (Anthropic Web)

**Architecture**

Claude's web platform now implements persistent memory that synthesizes knowledge across conversations:

- **Memory Summary**: Auto-generated synthesis updated every 24 hours, categorized into domains (Role & Work, Current Projects, Personal Content)
- **Project Knowledge**: File uploads per project, ~200K+ tokens per file, ~100+ files
- **Project-Specific Memory**: Learned facts scoped to individual projects with zero cross-contamination
- **Cross-Thread Search**: Tool-based retrieval of past conversations (conversation_search, recent_chats)
- **Incognito Mode**: Conversations that don't appear in history or save to memory

Available on Team and Enterprise plans. Memory is optional with granular controls.

**Capacity**

- Memory summary: no published hard limit (synthesized, not itemized)
- Project knowledge: 200K+ tokens per file, ~100+ files per project
- Context window: ~200K tokens (model-dependent)
- Cross-thread search: indefinite conversation retention

**Portability**: **HIGH**

- Full data export via Settings > Privacy (includes chat history + memory)
- Memory import/export feature for migration between AI services (launched 2026)
- Memory Tool available via API (beta: context-management-2025-06-27 header)
- Works on Claude API, Amazon Bedrock, and Google Cloud Vertex AI
- Key advantage over ChatGPT: memory IS accessible via API

**Lock-in Risk**: **LOW**

Memory export is functional, API access exists, and the import/export feature explicitly enables migration. The main lock-in vector is the project knowledge files, which are standard documents that can be re-uploaded elsewhere.

**Syncrescendence Usage**

- Syncrescendence IIC project with custom instructions matching Constellation Architecture
- Project knowledge includes research documents
- Memory configured with system-wide Custom Instructions (Account 3)

---

#### 3. ChatGPT (OpenAI)

**Architecture**

ChatGPT implements a multi-layer memory system with both passive and active components:

- **Global Custom Instructions**: Account-level behavioral config
- **Saved Memories**: Auto-learned facts from conversations (passive), ~6,000 tokens capacity
- **Automatic Memory Management**: Prioritizes relevant memories, deprioritizes stale ones (new 2026)
- **Project Files**: 25-40 files (tier-dependent), 512MB per file
- **Project Memory Mode**: Toggle between Default (global + project) and Project-Only (isolated)
- **Canvas**: Persistent side-by-side document/code editor

Memory was increased 25% for Plus/Pro/Team users in early 2026.

**Capacity**

- Saved memories: ~6,000 tokens (~45-50K words equivalent after compression)
- Project files: 25-40 files, 512MB each
- Context window: 32K-128K tokens (tier-dependent)
- Thread length: unlimited (but progressive context eviction)
- "Memory full" is a frequent user complaint even after the 25% increase

**Portability**: **LOW**

- Data export exists (Settings > Data Controls > Export) but produces a bulk dump, not structured memory
- **NO API access to saved memories** -- this is consumer-app only
- No programmatic way to read, write, or migrate individual memories
- Project files can be re-downloaded but project configuration is not portable
- Canvas content persists but has no export mechanism beyond copy-paste

**Lock-in Risk**: **HIGH**

The lack of API access to memories is the critical lock-in vector. You cannot script memory migration. The data export is a compliance feature (GDPR), not a portability feature. Any investment in ChatGPT's memory system is effectively trapped in OpenAI's ecosystem.

**Syncrescendence Usage**

- Psyche (CTO) operates via OpenClaw with GPT-5.3-codex -- but OpenClaw bypasses ChatGPT's native memory entirely
- ChatGPT Projects not configured for Syncrescendence compiler role (checklist item pending)
- Memory regression in GPT-5.x within Projects reported by users -- explicit specs required

---

#### 4. Gemini (Google Web + CLI)

**Architecture**

Gemini's memory operates through Google ecosystem integration:

- **Saved Info**: Explicit "Remember X" facts, global scope, web-only management
- **Personal Intelligence**: Context from Gmail, Drive, Photos, Search, YouTube (beta, US-only)
- **Past Chat Personalization**: Learns from conversation history (not available in EEA/UK)
- **Gems**: Custom personas with instructions + up to 10 knowledge files (can link live Google Drive files)
- **1M Token Context**: Largest context window in the industry (Gemini 3 Pro)
- **NotebookLM Integration**: Attach 50+ source notebooks with zero-hallucination grounding

**Capacity**

- Saved Info: no published limit (explicit fact storage)
- Gems: 10 files each, leveraging 1M token context window
- Context window: 1M tokens (~750K words)
- NotebookLM: 1M token context, 50+ sources per notebook, 6x conversation memory (2026 upgrade)
- Thread length: effectively unlimited

**Portability**: **LOW-MEDIUM**

- Saved Info: viewable/editable at gemini.google.com/saved-info but no bulk export API
- Memory management is "all-or-nothing" -- selective deletion promised for 2026 but not available
- Gems cannot self-update files (security restriction) -- user must manually re-upload
- Google Drive file linking is a strength (live documents) but creates Google ecosystem dependency
- NotebookLM outputs downloadable (podcasts, videos) but notebook structure is not portable
- No API for memory management equivalent to Claude's Memory Tool

**Lock-in Risk**: **MEDIUM**

The Google ecosystem integration is both strength and chain. Personal Intelligence creates deep dependency on Google services. Gems are portable in concept (instructions + files) but not in practice (no export API). The 1M context window reduces the NEED for persistent memory (you can stuff more in per session) which partially mitigates lock-in.

**Syncrescendence Usage**

- Cartographer (CIO) role via Gemini CLI -- stateless, no memory dependency
- Gemini CLI is fully stateless by design (each invocation independent, 1M context per call)
- No Gems configured for Syncrescendence
- Gemini MCP server configured (pending restart) for corpus sensing
- Google AI API key stored at `~/.syncrescendence/.env`

---

#### 5. Self-Hosted Stack: Mem0 + Graphiti + QMD

##### 5a. Mem0 (Qdrant-backed)

**Architecture**

Mem0 is a universal memory layer employing hybrid datastore architecture:

- **Vector Store** (Qdrant): Semantic similarity search over memories
- **Graph Store**: Relationship understanding between entities
- **Key-Value Store**: Quick access to structured data
- Auto-capture + auto-recall on every OpenClaw conversation
- Model-agnostic: works with OpenAI, Anthropic, Ollama, or custom models

**Current State** (LIVE)

- Qdrant container: Up 32 hours, healthy
- Collections: `memories` (44 points, 1536-dim cosine embeddings), `memory_migrations`
- Embedding model: OpenAI text-embedding-ada-002 (1536 dimensions)
- Port: 6333 (HTTP), 6334 (gRPC)

**Portability**: **FULL**

- Self-hosted: all data on local disk
- Qdrant supports snapshot export, collection cloning, and API-based bulk read
- Mem0 is open-source (MIT license, v1.0.0, $24M Series A)
- Can switch vector backend (Qdrant, Chroma, Pinecone, Milvus, Weaviate)
- Mem0 explicitly positioning memory as portable infrastructure (like contacts)

**Lock-in Risk**: **NONE**

Everything runs locally in Docker. Data is in Qdrant snapshots. Code is open-source. If Mem0 the company disappears, the open-source fork continues.

##### 5b. Graphiti (Neo4j-backed)

**Architecture**

Graphiti is a temporal knowledge graph engine by Zep AI:

- **Bi-temporal model**: tracks when events occurred AND when they were ingested
- **Incremental updates**: no batch recomputation needed
- **Entity/relationship/community** graph structure
- Validity intervals on every edge (temporal awareness)
- Supports Neo4j, Amazon Neptune, FalkorDB, Kuzu backends

**Current State** (LIVE)

- Neo4j 5.26.0 Community: Up 32 hours, healthy, port 7474 (HTTP) + 7687 (Bolt)
- Graphiti API: Up 32 hours, healthy, port 8001
- MCP server: 9 tools available via Claude Code
- All three containers running in Docker

**Portability**: **FULL**

- Neo4j supports full database dumps (`neo4j-admin dump`)
- Cypher queries can export any subgraph as CSV/JSON
- Multiple backend support (Neo4j, Neptune, FalkorDB, Kuzu)
- Open-source (MIT license)
- MCP server enables any MCP-compatible client to access the graph

**Lock-in Risk**: **NONE**

Self-hosted, open-source, standard graph database. The knowledge graph IS the portable artifact.

##### 5c. QMD (BM25 Local Search)

**Architecture**

QMD provides BM25 keyword search over the vault's 693 Markdown files:

- Hourly refresh via launchd (`run_qmd_update.sh`)
- Accessible via `make search Q="query"`
- No external dependencies beyond the vault files themselves

**Current State** (LIVE)

- Refresh: hourly via launchd agent
- Corpus: 693 .md files in the vault
- Interface: make target

**Portability**: **FULL**

The index IS the vault. QMD is a view over existing files, not a separate data store.

**Lock-in Risk**: **NONE**

---

#### 6. Notion

**Architecture**

Notion 3.0 (September 2025) introduced AI Agents with a state-of-the-art memory system built on Notion's own infrastructure:

- **Pages and Databases**: Core storage primitives with full version history
- **AI Agent Memory**: Uses Notion pages/databases as persistent context
- **Agent Instructions**: Dedicated instruction pages per agent (style, references, filing rules)
- **Multi-Model**: GPT-5.2, Claude Opus 4.5, Gemini 3 (switchable, context persists across model changes)
- **MCP Server**: Official Notion MCP for full CRUD operations on pages, blocks, and databases
- **Calendar Integration**: Google + Notion Calendar search

**Capacity**

- Storage: unlimited pages/databases (plan-dependent)
- AI Agent: 20+ minutes of multi-step actions per invocation
- File uploads: varies by plan
- API: full CRUD, 3 requests/second rate limit

**Portability**: **HIGH**

- Full API access (REST + MCP): read, create, update, delete pages/blocks/databases
- Bulk export: Markdown, CSV, HTML
- MCP server enables any AI tool to interact with Notion workspace
- Version history preserves all changes
- Database → CSV export for structured data

**Lock-in Risk**: **LOW**

Notion's API is comprehensive and the MCP server is official. Data can be extracted in standard formats. The main risk is that Notion's rich block types (toggles, callouts, synced blocks) don't map perfectly to plain Markdown, causing some formatting loss on export.

**Syncrescendence Usage**

- MCP server configured in `~/.claude.json` (global scope) but currently **NOT LOADING**
- Notion workspace exists but not actively integrated into the agent constellation
- Potential role: persistent structured knowledge base accessible by all agents via MCP

---

### Portability Strategy

#### Data Trapped in Each Platform

| Platform | What's Trapped | Severity | Migration Difficulty |
|----------|---------------|----------|---------------------|
| **ChatGPT Memories** | ~6,000 tokens of learned facts, no API access | HIGH | Manual copy-paste only |
| **ChatGPT Canvas** | Iterative document/code state | MEDIUM | Copy-paste |
| **Gemini Saved Info** | Personal facts/preferences | MEDIUM | Manual transcription |
| **Gemini Personal Intelligence** | Cross-service context graph | HIGH | Not exportable at all |
| **NotebookLM Notebooks** | Source organization + AI notes | MEDIUM | Sources re-uploadable, notes lost |
| **Claude.ai Project Knowledge** | Uploaded files | LOW | Files are standard documents |
| **Claude.ai Memory Summary** | Synthesized cross-conversation knowledge | LOW | Exportable + API access |

#### Migration Paths Between Platforms

1. **Claude.ai <-> Claude Code**: Natural bridge. Claude.ai memory export can be placed into CLAUDE.md or memory/ files. Claude Code session insights can be uploaded as project knowledge.

2. **ChatGPT -> Claude**: Manual only. Export ChatGPT data, extract memories from JSON dump, reformat as Claude project knowledge or CLAUDE.md entries. No automation possible due to ChatGPT API gap.

3. **Any Platform -> Graphiti**: Feed conversation exports or memory dumps into Graphiti as episodes. The temporal knowledge graph will extract entities and relationships automatically.

4. **Any Platform -> Mem0**: Use Mem0 API to store extracted facts. Mem0's auto-capture works for OpenClaw conversations; other platforms require manual bridging.

5. **Vault (QMD) -> Any Platform**: The vault IS the universal format. Any platform can ingest Markdown files.

6. **Notion <-> Everything**: Notion's API + MCP makes it the best hub for structured data exchange. Create a Notion database as a memory ledger, sync via MCP.

#### Recommended Backup Strategy

```
TIER 1 (Ground Truth): Git Repository + Vault Files
  └── CLAUDE.md hierarchy, memory/ directory, all .md files
  └── Backed up via git (remote), Time Machine (local)
  └── QMD indexes this automatically

TIER 2 (Sovereign Infrastructure): Docker Volumes
  └── Neo4j data (Graphiti knowledge graph)
  └── Qdrant data (Mem0 vector memories)
  └── Backup: docker volume snapshots, neo4j-admin dump, qdrant snapshots

TIER 3 (Cloud Platform Exports): Scheduled Pulls
  └── Claude.ai: quarterly data export + memory export
  └── ChatGPT: quarterly data export (Settings > Data Controls)
  └── Notion: API-driven database exports (automatable via n8n)

TIER 4 (Disposable/Ephemeral): No Backup Needed
  └── Gemini CLI sessions (stateless by design)
  └── Perplexity threads (research-only, no persistent state)
  └── Grok conversations (no customization layer)
```

---

### Recommendations

#### 1. Memory Investment Priority

| Priority | Platform | Strategy | Rationale |
|----------|----------|----------|-----------|
| **P0 INVEST** | Claude Code (CLAUDE.md + memory/) | Maximum investment | Full portability, git-tracked, zero lock-in, loaded every session |
| **P0 INVEST** | Graphiti (Neo4j) | Maximum investment | Self-hosted KG, temporal awareness, MCP-accessible, multi-backend |
| **P1 INVEST** | Mem0 (Qdrant) | Grow incrementally | Auto-capture for OpenClaw, 44 memories and growing, fully portable |
| **P1 INVEST** | Claude.ai Projects | Moderate investment | Good portability, API access, project isolation |
| **P2 EVALUATE** | Notion (MCP) | Fix MCP loading, then evaluate | Excellent API, but currently not operational |
| **P3 KEEP EPHEMERAL** | ChatGPT | Do not invest in native memory | No API, high lock-in; Psyche uses OpenClaw (bypasses ChatGPT memory) |
| **P3 KEEP EPHEMERAL** | Gemini Web | Minimal Saved Info only | Stateless CLI is the primary interface; Gems add little for our workflow |
| **P4 IGNORE** | NotebookLM, Perplexity, Grok | Zero memory investment | No persistent memory worth capturing |

#### 2. Data Sovereignty Strategy

**Principle**: The repository is ground truth; web apps are cache (Invariant #5).

- **All durable knowledge** lives in the git repo as Markdown files
- **Graphiti** serves as the relational layer -- entities, relationships, temporal context that Markdown cannot capture
- **Mem0** serves as the conversational layer -- auto-captured facts from agent interactions
- **QMD** serves as the search layer -- BM25 over the vault for fast retrieval
- **Cloud platforms** are execution environments, not storage. Their memory features are convenience, not infrastructure.

**Anti-pattern**: Investing in ChatGPT or Gemini memory as if it were durable infrastructure. These platforms can change memory features, capacity, or access at any time without notice.

#### 3. Backup Automation Opportunities

| Automation | Mechanism | Priority | Status |
|------------|-----------|----------|--------|
| Neo4j daily dump | launchd + `neo4j-admin dump` | P1 | NOT STARTED |
| Qdrant snapshot | launchd + Qdrant snapshot API | P1 | NOT STARTED |
| Claude.ai memory export | Manual quarterly (no automation API yet) | P2 | NOT STARTED |
| ChatGPT data export | Manual quarterly (no automation possible) | P3 | NOT STARTED |
| Notion database sync | n8n webhook + Notion API | P2 | BLOCKED (MCP not loading) |
| Vault git backup | Already operational (git push) | P0 | DONE |

#### 4. Specific Next Actions

1. **Fix Notion MCP loading** -- resolve the `NOT LOADING` status to unlock Notion as a structured memory hub
2. **Create Neo4j backup script** -- add `neo4j-admin dump` to launchd with daily schedule
3. **Create Qdrant snapshot script** -- add snapshot API call to launchd with daily schedule
4. **Expand Mem0 integration** -- currently 44 memories; configure auto-capture thresholds and relevance scoring
5. **Do NOT configure ChatGPT Projects** for Syncrescendence -- the memory regression + no API makes it a dead end. Psyche should continue using OpenClaw which bypasses ChatGPT's native memory entirely.
6. **Evaluate Claude.ai Memory Tool API** -- the beta memory tool could enable automated sync between Claude.ai conversations and the vault

---

### Cross-References

| Document | Path | Relationship |
|----------|------|-------------|
| CANON-30430 Memory Systems | `01-CANON/CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md` | Theoretical foundation (taxonomy, architectures, vector DBs) |
| Memory Architecture Matrix | `02-ENGINE/REF-MEMORY_ARCHITECTURE_MATRIX.md` | IIC platform-specific memory layers (predecessor to this audit) |
| Constellation Agent Loops | `00-ORCHESTRATION/state/ARCH-CONSTELLATION_AGENT_LOOPS.md` | Agent loop memory dependencies |
| MCP Configuration | `~/.claude/projects/-Users-home/memory/mcp-configuration.md` | MCP server status for memory-related tools |
| Automation Master Plan | `00-ORCHESTRATION/state/ARCH-AUTOMATION_MASTER_PLAN.md` | Backup automation context |
| Stack Teleology | `02-ENGINE/REF-STACK_TELEOLOGY.md` | Technology stack decisions |
| SaaS Integration | `02-ENGINE/REF-SAAS_INTEGRATION_ARCHITECTURE.md` | Platform integration architecture |

---

### Operational Infrastructure Status (Snapshot 2026-02-10)

```
SERVICE          CONTAINER    STATUS        PORT        UPTIME
Neo4j 5.26.0     neo4j       healthy       7474/7687   32h
Graphiti API     graphiti     healthy       8001        32h
Qdrant           qdrant      healthy       6333/6334   32h
Chroma           (script)    configured    8765        launchd
QMD              (script)    hourly        N/A         launchd
Watchdog         (script)    5min          N/A         launchd
Corpus Health    (script)    6h            N/A         launchd
```

**Memory Inventory**:
- Qdrant `memories` collection: 44 points (1536-dim, cosine)
- Qdrant `memory_migrations` collection: present
- Neo4j: community edition, graph data (size not audited)
- Vault: 693 .md files indexed by QMD
- Claude Code auto-memory: 10 files in project memory directory

---

### Version History

**v1.0.0** (2026-02-10): Initial comprehensive audit
- All 6 platform categories assessed (Claude Code, Claude.ai, ChatGPT, Gemini, Self-hosted, Notion)
- Portability matrix, lock-in risk ratings, and backup strategy defined
- Self-hosted infrastructure live status verified (Graphiti, Qdrant, Neo4j all healthy)
- Supersedes and extends REF-MEMORY_ARCHITECTURE_MATRIX.md (January 2026) with portability focus
