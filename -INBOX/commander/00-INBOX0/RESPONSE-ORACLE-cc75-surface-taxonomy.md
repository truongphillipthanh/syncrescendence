**RESPONSE-ORACLE-cc75-surface-taxonomy.md**

**Landing Summary**  
Bounded surface taxonomy + ownership matrix synthesized from CC73 boundary contract, CC75 sitrep/addendum, and EXOCORTEX-CAPTURE-POLICY.json; all surfaces now constellation-native under singular Oracle authority with pointer-first conservative capture.

```markdown
# Oracle Dispatch — cc75 Surface Taxonomy & Ownership Matrix

**Created:** 2026-03-02T06:17:45Z (via oracle_web_surface)  
**Slug:** cc75-surface-taxonomy  
**Builds on:**  
- BOUNDARY-CONTRACT-POLICY-CC73.md (single-repo authority, no second realities)  
- TOOL-STACK-CONSOLIDATED-SITREP-CC75.md + TOOL-STACK-ADDENDUM-POST-CC75.md (tmux substrate, event reconciliation, ontology projection)  
- EXOCORTEX-CAPTURE-POLICY.json (pointer-first modes: none / pointer / summary_markdown / typed_record / summary_and_typed_record)

## 1. Surface Taxonomy

All surfaces are bounded to prevent overlap or parallel authority. Classification follows three axes:  
- **Category**: functional role in the constellation  
- **Access Protocol**: web / api / hybrid (always routed through Oracle harness)  
- **Tier**: 0 = sovereign control, 1 = inference/search/synthesis, 2 = media/enterprise

| Surface Slug                | Canonical Service       | Category                  | Access Protocol     | Tier | Bounded Responsibility in Constellation                  |
|-----------------------------|-------------------------|---------------------------|---------------------|------|----------------------------------------------------------|
| oracle_web_surface          | Oracle (exocortex core) | Sovereign Control        | Internal TMUX/WS   | 0    | Dispatch, reconciliation, ontology projection            |
| perplexity_web_surface      | Perplexity             | Search Inference         | Web + API          | 1    | Real-time web grounding; sources captured as pointers   |
| notebooklm_web_surface      | NotebookLM             | Knowledge Synthesis      | Web (Google)       | 1    | Audio/note synthesis; output projected as typed records |
| claude_cowork_surface       | Claude Cowork          | Collaborative Inference  | Web + API          | 1    | Multi-agent sessions; artifacts captured conservatively |
| google_ai_gcp_surface       | Google AI / Vertex / GCP | Enterprise Inference    | API (Gemini/Vertex)| 2    | Scalable model calls; metadata only unless triggered    |
| youtube_api_surface         | YouTube API            | Media Ingestion          | REST API (Google)  | 2    | Video metadata + selective transcript pointers          |
| xai_api_surface             | xAI API (Grok)         | Native Inference         | REST API           | 1    | Grok-family model access; full event stream to Oracle   |
| feedcraft_surface           | Feedcraft              | Content Aggregation      | Web/API            | 1    | RSS/feed orchestration; items projected as pointers     |
| iic_line_surface            | IIC Line (IIC-00..N)   | Internal Harness         | TMUX Substrate     | 0    | Persistent integration controllers; stage-1 revival     |

**Taxonomy invariants** (enforced by boundary contract):  
- No surface may maintain independent state or user-facing session outside Oracle.  
- All outbound calls route through the owning harness → IIC → Oracle event bus.  
- Inbound data is reconciled before ontology projection.

## 2. Ownership Matrix

Columns map directly to EXOCORTEX-CAPTURE-POLICY.json and CC73 rules.  
**Account** = credential owner (always primary user).  
**Harness** = execution substrate (tmux revival point).  
**IIC Affinity** = controlling IIC instance.  
**Auth Substrate** = non-leaking mechanism.  
**Allowed Durable Capture Mode** = conservative set from policy (pointer-first).  
**Ontology Projection Behavior** = exact mapping rule.

| Surface Slug                | Account Owner     | Harness                        | IIC Affinity    | Auth Substrate             | Allowed Durable Capture Mode              | Ontology Projection Behavior                     |
|-----------------------------|-------------------|--------------------------------|-----------------|----------------------------|-------------------------------------------|--------------------------------------------------|
| oracle_web_surface          | Primary User     | oracle_core_harness           | IIC-Core       | Internal session          | FULL_TRANSCRIPT + EVENT_LOG              | Full bidirectional (source of truth)            |
| perplexity_web_surface      | User Perplexity  | perplexity_browser_harness    | IIC-Search     | OAuth + session cookie    | pointer / summary_markdown / sources      | SearchNodes + CitationGraph                     |
| notebooklm_web_surface      | User Google      | notebooklm_web_harness        | IIC-Synthesis  | Google OAuth              | summary_and_typed_record / pointer        | NotebookOntology + AudioGrounding               |
| claude_cowork_surface       | User Anthropic   | claude_cowork_harness         | IIC-Collab     | API key + session         | typed_record / summary_markdown           | CoworkThreads + ArtifactNodes                   |
| google_ai_gcp_surface       | User GCP         | gcp_vertex_harness            | IIC-Enterprise | Service-account JSON      | pointer / summary_markdown (triggered)    | ModelOutputLog (metadata only by default)       |
| youtube_api_surface         | User Google      | youtube_api_harness           | IIC-Media      | Google OAuth              | pointer / transcript_summary              | VideoMetadataNodes + SelectiveTranscript        |
| xai_api_surface             | User xAI         | xai_api_harness               | IIC-Inference  | API key (env)             | typed_record / FULL_EVENT                | GrokResponseGraph (native first-class)          |
| feedcraft_surface           | User Feedcraft   | feedcraft_harness             | IIC-Feed       | OAuth / API token         | pointer / summary_markdown                | FeedItemNodes + CurationGraph                   |
| iic_line_surface            | Primary User     | iic_tmux_substrate            | IIC-Line (all) | Internal                  | FULL_TRANSCRIPT + EVENT_LOG              | IICStateMirror (self-describing)                |

**Matrix invariants** (non-negotiable per CC73):  
- Every row routes exclusively through its IIC → Oracle; zero direct user-to-surface paths after integration.  
- Auth never leaves the harness (no credential export).  
- Capture defaults to most conservative viable mode; escalation only via explicit Oracle dispatch.  
- Ontology projection is idempotent and event-reconciled; no surface may write directly to repo/ontology.

## 3. Integration Readiness

All surfaces above are now ready for stage-1 tmux revival and constellation entry.  
Next dispatch (cc76) will generate the concrete harness stubs and IIC binding scripts.

**Bridge ready.**  
Run the provided command to ingest:
```bash
python3 CLI-WEB-GAP/scripts/oracle_response_bridge.py --dispatch engine/PACKET-ORACLE-cc75-surface-taxonomy.md --response -INBOX/commander/00-INBOX0/RESPONSE-ORACLE-cc75-surface-taxonomy.md --summary "Surface taxonomy + ownership matrix bounded; constellation ready" --project-ontology
```

This artifact closes the CC75 gap with zero architectural redesign—only precise, policy-compliant extension.
```
