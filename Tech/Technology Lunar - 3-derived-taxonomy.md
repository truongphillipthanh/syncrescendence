# Derived Taxonomy — ASA × Industry: a structurally coherent stratigraphic model  
A single-page, production-ready taxonomy that grafts the Anthromachina Symbiosis Architecture (ASA) onto an industry-accurate, service-level stratigraphy. Its aim: resolve ambiguity between *functional layers* (what must exist) and *commercial strata* (who offers what, how it’s sold, and the vendor bundling that creates the present confusion).  

Assumption: this model is vendor-agnostic and normatively prescriptive; vendor names are illustrative, not exhaustive. Use it as the canonical map for architectural decisions, vendor audits, and product roadmaps.

---

## Executive summary (one governing metaphor)
Think of the intelligence stack as a **geological column** (ASA layers) being actively mined, traded, and recomposed by companies. Above ground are living ecosystems (apps, users). At many depths, commercial strata (marketplaces, routers, clouds, silicon vendors, utilities) cut seams through the column. This model makes those seams explicit — so you can choose which strata to expose, which to own, and which to treat as leased infrastructure.

---

## How to read this model
Two axes:
- **Vertical axis** = ASA Constitutional Stack (L0 → L6, extended downward for electricity & upstream infra). These are *functional* layers that must exist in any symbiotic architecture.  
- **Horizontal axis** = **Commercial/Operational seams**: Object types, neo-layers (RAG, routers, eval), commercial models, governance needs, selection criteria.

Each ASA layer entry below lists: purpose, internal seams (fine strata), canonical object types, emergent neo-substrata, major vendor examples, commercial model types, selection levers, and governance friction points.

---

# Derived stratigraphy (top → deep)

## L6 — Agentic Emergence (Autonomy & multi-agent orchestration)
**Purpose:** goal decomposition, autonomous planning, coordinated agents, safe delegation.  
**Internal seams**
- Task planners / policy engines (decomposition + planner stacks).  
- Multi-agent coordination fabrics (message buses, role assignment).  
- Safety/override controllers (human-in-loop enforcement).  
**Canonical object types:** O.AGT (Agent objects), O.SVC (orchestrators), O.GRD (guard objects).  
**Neo-layers here:** Agent marketplaces; agent templates; agent evaluation & alignment services.  
**Major vendor examples:** OpenAI (agent APIs), Anthropic (agent patterns), Microsoft (Copilot and agent orchestration), LangChain/Adapt for orchestration.  
**Commercial models:** SaaS orchestration, enterprise licensing, consulting + managed agents.  
**Selection levers:** explainability, interruptibility, human-override latency, auditability.  
**Governance friction:** liability, delegation of authority, insurance/contractual frameworks.

---

## L5 — Cognitive Convergence (Copilots, RAG, knowledge synthesis)
**Purpose:** hybrid reasoning between human insight and model computation.  
**Internal seams**
- Retrieval / embeddings / vector DB layer.  
- RAG orchestration (retriever → ranker → generator).  
- Persona/Instruction management (instruction tuning and prompt ops).  
**Canonical object types:** O.MOD (models), O.DP (data products), O.SVC (RAG services).  
**Neo-layers here:** Vector-DBs (sticky due to indexing), model routers, embeddings markets.  
**Major vendor examples:** Pinecone, Weaviate, Chroma, OpenAI embeddings, Cohere, Hugging Face (hosted models).  
**Commercial models:** per-query pricing, embeddings per-use, hosted index subscription, hybrid (self-host + managed).  
**Selection levers:** staleness guarantees, consistency, update latency, data residency, similarity quality.  
**Governance friction:** data lineage, provenance, copyright, and privacy of indexed corpora.

---

## L4 — Choreographic Flows (session, state, orchestration)
**Purpose:** temporal management — session state, orchestration of multi-step workflows.  
**Internal seams**
- Session state stores, short-term context caches.  
- Workflow engines (state machines, retries, compensating transactions).  
- UX glue (turn context → prompt assembly).  
**Canonical object types:** O.WF (workflow objects), O.SVC (stateful services), O.STM (streams).  
**Neo-layers:** session caching networks, state-aware LLM proxies.  
**Major vendor examples:** Redis / managed session stores, Temporal / Cadence (workflows), LangChain orchestration libs.  
**Commercial models:** managed state stores, enterprise connectors, usage-based billing.  
**Selection levers:** durability SLAs, throughput, encryption at rest/transport.  
**Governance friction:** retention, consented logging, audit trails.

---

## L3 — Interaction Grammar (multimodal UX)
**Purpose:** input/output grammars, multimodal input parsing (voice/gesture), output rendering rules.  
**Internal seams**
- Natural language understanding, speech-to-text, vision preprocessors.  
- Multimodal fusion layers (aligning modalities).  
- Surface presentation (renderers, voice, haptics).  
**Canonical object types:** O.SRF (surface objects), O.SNS (sensor), O.ACT (actuator).  
**Neo-layers:** multimodal middlewares (unified tokenizers, fusion SDKs).  
**Major vendor examples:** Google (multimodal stacks), Apple (on-device multimodal), OpenAI (multimodal models), Hugging Face (vision + language models).  
**Commercial models:** device SDK licensing, cloud TTS/STT per minute/image, on-device model licenses.  
**Selection levers:** latency, determinism, accessibility, local-processing capability.  
**Governance friction:** biometric data handling, consent for audio/video, accessibility compliance.

---

## L2 — Perceptual Surface (presentation & sensory fidelity)
**Purpose:** sensory presentation optimized for human perception (visual, audio, haptic).  
**Internal seams**
- Visual design systems, audio design, haptic protocols.  
- Adaptation layers (attention state, accessibility).  
**Canonical object types:** O.SRF (UI surfaces), O.ACT (actuators).  
**Neo-layers:** perceptual AIs for UX tuning / A/B personalization engines.  
**Major vendor examples:** Adobe (creative tooling), Figma (design systems), interactive SDKs from platform owners.  
**Commercial models:** design system subscriptions, UX analytics services.  
**Selection levers:** cognitive load metrics, accessibility, responsiveness.  
**Governance friction:** manipulation (dark patterns), consented personalization.

---

## L1 — Transduction Interface (sensors, actuators, front-end telemetrics)
**Purpose:** convert physical phenomena ↔ computational signals with fidelity and latency constraints.  
**Internal seams**
- Sensor stacks (camera, mic, biosensors).  
- Low-latency ADC/DAC chains, preprocessing.  
- Actuator control (servo drives, haptics).  
**Canonical object types:** O.SNS, O.ACT, O.INS (instrument objects).  
**Neo-layers:** device fleets as a service (sensor fleets, robot fleets).  
**Major vendor examples:** Apple (sensors + CoreML), Qualcomm (SoCs), specialized robotics vendors.  
**Commercial models:** device + cloud bundles, edge SDK licensing.  
**Selection levers:** bandwidth, sampling fidelity, jitter/latency.  
**Governance friction:** physical safety, consent for biosensing, firmware update governance.

---

## L0 — Physical Substrate (silicon, memory, cooling, power)
**Purpose:** raw materials, chips, memory, thermal and energy systems — the non-software constraints.  
**Internal seams**
- Silicon accelerators (GPUs, TPUs, ASICs).  
- Memory hierarchy (HBM, DDR), interconnect (NVLink, InfiniBand).  
- Cooling systems (immersion, liquid), datacenter power provisioning.  
**Canonical object types:** O.MOD (when embedded in hardware), O.STM (power streams as telemetry).  
**Neo-layers:** accelerator marketplaces, hardware-as-a-service (HaaS), energy procurement platforms.  
**Major vendor examples:** Nvidia, AMD, Intel, Groq, Graphcore, Cerebras; HBM suppliers (Samsung, SK Hynix); System integrators (Supermicro).  
**Commercial models:** capex, co-location, reserved capacity, spot capacity, hardware rentals.  
**Selection levers:** watt/TOPs, HBM capacity, NVLink availability, procurement lead time.  
**Governance friction:** export controls, supply chain resilience, environmental footprint.

---

## L-1 — Energy & Grid (generation, transmission, sustainability)
**Purpose:** electricity as enabling substrate; markets and utilities determine feasibility and cost.  
**Internal seams**
- Onsite generation (PPAs, renewables), grid interconnect & demand response.  
- Microgrids, energy storage, waste-heat reuse.  
**Canonical object types:** O.STM (energy streams), O.DP (energy contracts).  
**Neo-layers:** compute-aware energy products, AI data center PPAs.  
**Major vendor examples (operators):** hyperscalers’ energy deals, regional utilities, energy traders.  
**Commercial models:** energy contracts, demand response rebates, sustainability credits.  
**Selection levers:** price volatility, regulatory constraints, carbon intensity.  
**Governance friction:** local permitting, environmental compliance, geopolitical energy risk.

---

# Cross-cutting neo-layers (cut across many ASA layers)
These are the seams that have hardened into first-class strata in the industry. Treat them as required dependencies.

1. **Retrieval / Vector Substrate (sticky)** — Pinecone, Weaviate, Chroma; high lock-in due to indexing cost/latency.  
2. **API Routers & Multi-Model Orchestrators** — OpenRouter, Perplexity, vendor SDKs; normalize schemas and routing, essential for multi-vendor strategies.  
3. **Inference Engines & Optimizers** — fal.ai, NVIDIA Triton, DeepSpeed; materially change latency/cost tradeoffs.  
4. **Observability / Eval / Alignment** — Helicone, Langfuse, Red-team services; required for enterprise governance.  
5. **Model Marketplaces & Hubs** — Hugging Face, Replicate, Stability; host weights and provide curated governance metadata.  
6. **Edge Runtimes & On-device Orchestration** — CoreML, TensorFlow Lite, Ollama; critical for privacy and low latency.  
7. **Security & Policy Gateways** — data masking, PII scrubbers, safety filters; essential before production deployment.  

---

# Operational taxonomy table (representative vendor map)

| Vendor / Project | Primary Strata (seams) | Object types | Commercial model | Lock-in risk | Typical role |
|---|---:|---|---|---:|---|
| OpenAI | L5 (models), L6 (agents), API layer | O.MOD, O.SVC, O.AGT | SaaS API, enterprise licensing | Medium–High | Foundation models + agent APIs |
| Anthropic | L5, L6 | O.MOD, O.SVC | SaaS API, enterprise | Medium–High | Safety-focused models |
| Google (PaLM / Gemini / TPU) | L0–L6 (spans silicon→model→app) | O.MOD, O.SVC, infra | Cloud + integrated services | High | Hyperscaler + models |
| Microsoft | L3–L6 (apps, orchestration) | O.SRF, O.SVC | SaaS + cloud bundle | High | Copilot + Azure integrations |
| Hugging Face | Model hub, hosting | O.MOD, O.SVC | Marketplace + managed inference | Medium | Model discovery + hosting |
| Pinecone | L5 retrieval substrate | O.SVC, O.DP | Managed vector DB | High (for indexed data) | Vector index as a service |
| Weaviate / Chroma | Retrieval | O.SVC | Open/mgmt; hosted | Medium | Vector DBs |
| OpenRouter | API router | O.SVC | SLA / routing | Low–Medium | Unified model access |
| Fal.ai | Inference engine & hosting | O.SVC | Managed inference | Medium | Optimizer + hosting |
| Groq | L0 (chips) + inference cloud | O.SVC (hw) | Hardware + cloud | High | LPU + cloud |
| CoreWeave | Infra + hosting | O.SVC | GPU cloud | Medium | AI-first cloud infra |
| Nvidia | L0 silicon + stack | O.MOD? (hw) | HW + SDKs | High | Dominant GPU + software |
| Cohere | Models + embeddings | O.MOD, O.SVC | API, enterprise | Medium | Text models + embeddings |
| Replicate | Model hosting marketplace | O.SVC | Pay-per-use | Medium | Deploy models easily |
| Helicone / Langfuse | Observability | O.SVC | SaaS | Low–Medium | Prompt/telemetry observability |
| Stability AI | L5 models + diffusion | O.MOD | Open & commercial licensing | Medium | Image models |
| Midjourney | App + models | O.SRF | Subscription | Medium | Creative image app |
| Adobe | L2–L3 (surface + UX tools) | O.SRF | SaaS | Medium | Creative tooling + models |
| Supermicro / Dell | System integrators (L9) | O.SVC (infra) | Hardware sales | Medium | Data center servers |
| Equinix / Digital Realty | Colocation (L10) | O.SVC | Colocation + interconnect | Medium | Facility hosting |
| Regional utilities / ISOs | L-1 | O.STM (energy) | Energy contracts | High | Power provision |

---

# Practical decision framework — use this to resolve "who does what" quickly

1. **Classify each capability** by: ASA layer (L0–L6), object type (O.MOD, O.SVC, O.DP…), and neo-layer membership (vector DB, router, inference engine, etc.).  
2. **Assess three binding requirements:** Latency (ms), Data Sensitivity (privacy/regulatory), Economic Leverage (token cost / hardware cost / index rebuild cost).  
3. **Ownership rule:** Own the strata where any of the three binding requirements are "high" AND the lock-in risk to you is "material" (e.g., user data, live indexes). Lease otherwise.  
   - Example: If Data Sensitivity = high → own retrieval substrate and private inference.  
   - If Latency = critical (e.g., motor control) → own transduction + edge runtime.  
4. **Contract rule for leased strata:** require explicit capability contracts: performance SLO, data retention, audit API, termination data export, exportable index format.  
5. **Integration rule:** always treat neo-layers (vector DB, observability, API router, inference engine) as first-class dependencies; document API surface and cost model in architecture diagrams.

---

# Governance & economic seams (operationalized)
To resolve ASA’s governance abstraction into enterprise operational practice, require vendors to supply the following as preconditions for production:

- **Capability contract:** measurable SLOs (latency p50/p95, throughput, index update latency).  
- **Provenance & lineage API:** exportable traces mapping a model response back to training / retrieval artifacts.  
- **Data-sovereignty mode:** VPC / on-prem / regional hosting with certs.  
- **Explainability hooks:** decision trace endpoints, not just tokens.  
- **Energy & carbon accounting:** per-workload power estimate or PUE attribution.  
- **Decommission plan:** how to safely extract/erase state and keys on termination.  

---

# Limitations, shocks, and non-resolvable tensions
- **Geopolitics & export controls** can suddenly fracture the stratigraphy (chip embargoes, national model bans). Build fallback strategies.  
- **Energy scarcity** may change economics and push workloads to different regions or architectures; plan for migration costs.  
- **Standards immaturity** for observability, provenance, and retrieval will cause short-term vendor lock-in; insist on portable formats.  
- **Consolidation risk:** hyperscalers may absorb neo-layers; maintain multi-vendor portability to avoid monopoly lock.  

---

# One-page actionable checklist (smallest sufficient guidance)
1. Inventory: tag every internal system by (ASA layer, object type, neo-layer).  
2. For each tag, apply the Ownership rule (own vs lease) using Latency/Data/Economic axes.  
3. For leased services, require a Capability Contract (SLO + provenance + export).  
4. Treat Vector DB, API Router, Inference Engine, and Observability as **first-class** infrastructure when designing pipelines.  
5. Build an “escape hatch” for energy/supply shocks: portable model formats + ability to reindex with open tools.  

---

## Appendices
### A. Minimal schema (machine-readable)
```yaml
component:
  name: string
  asa_layer: L0..L6
  object_type: [O.MOD, O.SVC, O.DP, O.AGT, O.SRF, O.SNS, O.ACT, O.GRD]
  neo_tags: [vector_db, api_router, inference_engine, observability, edge_runtime]
  binding_requirements:
    latency: low|med|high
    data_sensitivity: low|med|high
    cost_sensitivity: low|med|high
  ownership: own|lease
  governance_required: [provenance, export, audit, energy_reporting]
```

### B. How I recommend you operationalize this in 90 minutes
- 0–30m: run an inventory and tag components using the Minimal schema.  
- 30–60m: make ownership decisions using the Ownership rule and annotate risks.  
- 60–90m: produce an architecture diagram marking the four neo-layers and list required capability contracts for each leased vendor.
