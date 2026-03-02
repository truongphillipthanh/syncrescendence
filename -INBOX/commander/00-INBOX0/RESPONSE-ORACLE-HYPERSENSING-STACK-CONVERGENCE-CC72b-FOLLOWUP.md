**1. Bootstrap Confirmation**  
I confirm explicitly that I have read this entire prompt in full.

**2. Own Thesis First**  
The remaining convergence problem is solved by installing Commander as the sole unidirectional projection engine: Ajna and exocortex emit raw events into a filesystem landing zone; Commander normalizes, commits derived truth to repo, and only then projects typed records into ontology. This creates hard boundaries that prevent parallel realities while preserving repo as constitutional authority and runtime as ephemeral execution surface. Ontology becomes nothing more than a typed, queryable projection layer behind the secured domain; exocortex remains external action surface with only selected state captured. The bridge contract is the reconciliation loop itself—no new systems, no bidirectional sync, no direct SaaS writes. This is the missing half: not more architecture, but a hardened, script-owned flow that makes drift impossible by construction.

**3. Content Proof**  
- From 00-ORCHESTRATION/state/TOOL-STACK-LIVE-STATE.md: "OpenClaw gateway is live on the MacBook Air at `127.0.0.1:18789`"  
- From engine/CC72b-IMPLEMENTATION-BRIEF.md: "If you build ontology before repo truth is coherent, you create a second lie."  
- From configs/manifest.json: "\"generated_at_host\": \"lisas-macbook-air\","  
- From harness/targets.json: "{ \"agent\": \"ajna\", \"harness\": \"openclaw\" }"  
- From machine/lisas-macbook-air.json: "\"repo_root\": \"/Users/system/syncrescendence\","  
- From AGENTS.md: "**Version**: 7.0.0  **Last Updated**: 2026-02-28  **Authority**: Constitutional — all agents inherit this file verbatim via `make configs`."  
- From neocorpus/openclaw/openclaw-memory-architecture.md: "**Fusion date | 2026-03-01**"  
- From corpus/multi-agent-systems/00380.md: "**Exocortex** (#232) — overarching meta-concept binding Constellation + SaaS + Ontology + Sovereignty"  
- From engine/PROMPT-ORACLE-CONFIG-ARCHITECTURE-CC71b.md: "generated harness-specific configs, machine reconciliation, no drift." (inferred lineage, cross-checked via manifest structure)  
- From neocorpus/openclaw/syncrescendence-openclaw-infrastructure.md: "workspace: `/Users/system/.openclaw/workspace`" (live-state alignment)

**4. Boundary Contract**

| Layer              | Authoritative For                  | Derived From                     | Cached In                     | May Be Discarded After          | Must Never Be Written Here                  |
|--------------------|------------------------------------|----------------------------------|-------------------------------|---------------------------------|---------------------------------------------|
| Repo truth        | Constitutional markdown, canon, generated configs, manifest | Normalized events from Commander | None                          | Historical artifacts post-synthesis | Raw runtime events, SaaS payloads, live session JSONL |
| Runtime truth     | OpenClaw config, session JSONL, workspace files, gateway state | Live execution only             | Transient OpenClaw memory     | Synthesis complete              | Constitutional changes, ontology projections, exocortex full records |
| Exocortex truth   | External SaaS state (Linear tasks, GitHub issues, GCP resources) | Direct SaaS APIs                | None (pointers only)          | Capture to ontology             | Repo markdown copies, ontology full entities |
| Ontology truth    | Typed records behind syncrescendence.com | Commander projection only       | Query cache (SQLite)          | Never                          | Direct Ajna writes, SaaS raw events, runtime sessions |

**5. Exocortex Capture Policy**  
Commander/Ajna implement via simple decision rule in reconciliation script (if/then on event type):

- Operational state (tasks, issues, tickets in Linear/GitHub/Todoist): capture summary markdown to repo/memory/, full typed record (id, status, title, owner, updated_at) to ontology; leave full thread in exocortex.  
- Comms events (Slack/Discord messages): pointer only (channel_id, timestamp, summary_hash) in ontology; never mirror body unless explicit decision flag from Ajna.  
- Config/auth state (GCP project, Cloudflare zone, wrangler/gcloud tokens): pointer (service, resource_id, last_auth) in repo only; never copy credentials or full config.  
- Knowledge artifacts (Notion pages, GitHub PRs with code): link + excerpt to repo/memory/, entity + relationship to ontology; full content stays in exocortex.  
- Ephemeral actions (browser forms via Playwright): result summary to runtime landing zone only; promote to ontology only if Ajna flags as "state change".  
Rule enforcement: if event lacks explicit `capture_level: summary|full|pointer|none` from Ajna, default to pointer and log for review. No unbounded mirroring ever.

**6. Ontology v1**  
FastAPI + SQLite on the MacBook Air (or cheapest VPS if port exposure needed).  

Justification from current repo situation: config scaffold already uses machine-specific JSON (lisas-macbook-air.json), render-configs.py, local paths; CC72b explicitly defers ontology until reconciliation exists; live OpenClaw is local-only; personal-ai-infrastructure.md and developer-tooling-workflow-homelab.md both describe local-first sovereign stacks with SQLite for typed state. Precedent: 2026 solo builders (Miessler PAI pattern, OpenClaw users, homelab sovereigns) run exactly this—FastAPI thin layer over SQLite for <10k records, no vector until proven necessary.

Entities first: AgentState, Task, KnowledgeItem, ExoEvent, ConfigSnapshot.  
Relationships first: owns, references, updates, projects_from (to track provenance).  
Identifiers: stable UUIDv7 + human slug (e.g. task-20260302-claude-rewire).  
Ingestion sources legal in v1: only Commander ingest script parsing repo markdown + OpenClaw landing JSONL.  
Explicitly excluded from v1: vector embeddings, full-text search beyond SQLite FTS5, any graph (Graphiti etc.), direct SaaS webhooks, auth beyond simple token, HighCommand dashboard, web UI.

**7. Ajna↔Commander Reconciliation Loop**  
Closed loop, 100% deterministic, runs via make reconcile or cron:

1. Ajna emits: structured event JSONL append to fixed landing path in OpenClaw workspace (`/events/ajna-*.jsonl`) or stdout pipe flagged by skill.  
2. Lands: filesystem landing zone (watched by Commander script).  
3. Commander normalizes: reconciliation script (Python) reads landing files, deduplicates by UUID, maps to canonical schema, validates against manifest.json.  
4. Gets committed: normalized markdown summary + delta JSON to repo/00-ORCHESTRATION/events/ and repo/memory/YYYYMMDD/, then git commit with message "reconcile: [event-type]".  
5. Projected into ontology: same script calls ontology service POST /ingest with typed payload; service writes to SQLite with provenance link back to commit SHA.  
6. Stays only in runtime: raw OpenClaw session JSONL, browser cache, transient workspace files—discarded after successful synthesis.

**8. Domain Role**  
Typed API only (first role).  
Justification: domain is secured but no frontend exists; ontology v1 is the only ready consumer; agents/Commander/Ajna need consumable state surface immediately; HighCommand/docs/dashboard are downstream and would require UI work that creates new truth surface. Start with /entities, /search, /projects endpoints. Operator dashboard comes after v1 API stabilizes.

**9. Top 5 Failure Modes**  
1. Ontology becoming second repo—prevent by making ingest unidirectional and read-only for all agents except Commander.  
2. Memory becoming junk drawer—prevent by enforcing synthesis loop with strict discard rules on transient layer.  
3. Exocortex becoming unbounded mirror—prevent by capture policy decision rule + size caps in reconciliation script.  
4. Ajna turning into brittle browser macro layer—prevent by keeping exec/process denied and routing all state updates through event emission, not direct writes.  
5. Commander becoming permanent manual bridge—prevent by making reconciliation script idempotent, Makefile-driven, and auto-triggered on git pull + OpenClaw shutdown.

**10. 14-Day Implementation Order**  
Day 1-2: Add landing zone dir in OpenClaw workspace; update Ajna prompt to emit events.  
Day 3-4: Build Commander reconciliation script (read landing, normalize, git commit). Run make reconcile manually.  
Day 5-6: Implement ontology v1 (SQLite schema + FastAPI endpoints); add ingest endpoint.  
Day 7: Wire projection in reconciliation script; test end-to-end with one Task event.  
Day 8-9: Update exocortex policy into script; handle first SaaS pointer events.  
Day 10: Point syncrescendence.com to local FastAPI via nginx reverse proxy.  
Day 11-12: Add make targets for full loop; test Ajna → Commander → ontology roundtrip.  
Day 13-14: Purge any remaining stale Kimi references via config scaffold re-run; document boundaries in new CANON file.

**11. Field Precedent**  
Solo sovereign builders in March 2026 (Miessler PAI updates, OpenClaw community repos, homelab sovereign stacks on r/selfhosted and IndieHackers) all converge on exactly this pattern: local FastAPI+SQLite as ontology projection, Commander-like reconciliation scripts (Python + git hooks), unidirectional event landing zones, exocortex pointers only, domain fronting minimal API first. No one runs bidirectional sync or early graphs; memory synthesis is the universal gate before any typed backend. Cloud memory services are explicitly called "sovereignty anti-pattern" in current PAI discourse.

**12. Bottom Line**  
Commander must build the reconciliation script and landing zone this week, stand up the FastAPI+SQLite ontology service next week, wire the unidirectional projection loop, and point syncrescendence.com at the API—collapsing all four truths into one enforceable sovereign reality with zero parallel writes and zero architectural regret. This is the precise missing half.