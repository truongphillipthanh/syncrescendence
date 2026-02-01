As-of snapshot: A full, rigorously cross-validated "tax code" of the OpenAI ecosystem that meets your spec cannot be completed in one pass within the interaction and tool-call limits, but a representative, decision-usable subset can be mapped now, with explicit "known unknowns" and a re-run playbook to extend it.

## 0) As-of snapshot

- **As-of datetime**: 2026-01-12, ~16:40 PST.  
- **Scope checked so far**:  
  - ChatGPT global release notes (web) and macOS / Windows release notes for app feature drift.
  - OpenAI Help Center for admin/security/compliance and app governance (Enterprise/Edu/Business).
  - OpenAI GitHub org / ecosystem for Apps SDK + MCP usage.
  - Representative practitioner/community references for MCP / Codex integration and enterprise usage in regulated sectors.

- **Not yet scanned (explicitly out-of-scope for this first cut)**:  
  - Full pricing tables (ChatGPT & API) and model spec sheets.  
  - Full OpenAI docs index (developer.openai.com) and changelog.  
  - Full GitHub org, all Help Center articles, iOS/Android store release notes, and status/incidents.  

- **Recent material changes surfaced in this pass** (last ~90–120 days, likely to matter):  
  - Retirement of **Voice on the macOS ChatGPT desktop app** effective 2026‑01‑15, with voice consolidated into web, iOS, Android, and Windows clients.
  - Expansion of **role-based app governance, apps & connectors, and custom MCP-based apps** management for Enterprise/Edu (including RBAC-based app assignment, Compliance API coverage of app conversations, and OpenAI Compliance Logs integration).
  - Publicly documented, production-style **Apps SDK + MCP** integration examples for OpenAI tools, exposing how MCP is intended to be used as the standard tool/connector protocol in the OpenAI "apps" layer.
  - Active ecosystem work around **MCP servers that front OpenAI vector stores** and **Codex integrations via MCP**, indicating that the Model Context Protocol is the preferred abstraction for OpenAI-side tool integration even when Claude is the orchestrator.

The rest of this answer focuses on what can be supported from the sources above (plus a small "known unknowns" & re-run plan), rather than the full 10-part spec you outlined.

***

## 1) Ecosystem taxonomy (partial, evidence-backed slice)

This is a **partial taxonomy** covering areas where there is direct evidence in the scanned sources. Many leaves you requested remain UNKNOWN here and are explicitly marked so you can extend later.

### A. ChatGPT consumer apps (web + desktop)

**Core chat & models (surface evidence only)**  
- **ChatGPT web app – core chat**  
  - Lives: chatgpt.com (web).  
  - Gates: Not fully enumerated in current sources; release notes show feature toggles for models and experiences (e.g., voice).
  - Status: GA.  
  - Primary reference: ChatGPT — Release Notes.

- **ChatGPT macOS desktop app**  
  - Lives: macOS native app; release notes in OpenAI Help Center.
  - Gates: Plus and Teams noted for certain "Work with Apps" features (reading content from coding apps).
  - Status: GA; **Voice retiring on macOS app** effective 2026‑01‑15.
  - Primary reference: ChatGPT macOS app release notes; ChatGPT Release Notes.

- **ChatGPT Windows desktop app**  
  - Lives: Windows native desktop client.
  - Gates: Not fully enumerated; release notes emphasize installation mechanisms (e.g., winget) rather than tier gating.
  - Status: GA.  
  - Primary reference: Windows App – Release Notes.

**Selected desktop features with explicit evidence**  
- **Companion window (macOS)** – side-by-side persistent ChatGPT window with global shortcut (Option+Space).
  - Lives: macOS app.  
  - Gates: Not tier-labeled in notes (UNKNOWN).  
  - Status: GA as of 2024‑08‑06.
  - Ref: macOS release notes.

- **Projects & Tasks support in macOS app UI**  
  - "Added support for Tasks. Added support for working in Projects. (For now, you'll still have to create them first on web.)"
  - Lives: macOS app + web for project creation.
  - Gates: Not tier-specified in release notes (UNKNOWN).  
  - Status: GA in macOS app as of 2025‑01‑15.

- **Work with Apps (reading from coding apps)**  
  - "ChatGPT can now read content from your coding apps… This early beta is available to Plus and Teams users."
  - Lives: macOS app.  
  - Gates: Plus and Teams, early beta.
  - Status: Beta.  
  - Primary ref: macOS release notes, 2024‑11‑14.

- **Voice experience on macOS app**  
  - "We're retiring the Voice experience in the ChatGPT macOS app on January 15, 2026… feature will be available on chatgpt.com, iOS, Android, and the Windows app."
  - Lives: macOS app (until 2026‑01‑15), then removed; still in web, mobile, Windows.
  - Gates: Not tier-specified in the notes (UNKNOWN).  
  - Status: Deprecated on macOS (retiring date fixed).

**Unknown consumer features (not evidenced in this pass)**  
- Deep research, canvas beyond the small macOS mention, agent mode, notifications/tasks across all platforms, projects as a product, custom GPTs/store, browsing/search model matrix, etc. = **UNKNOWN** in this pass.

***

### B. ChatGPT org (Business / Enterprise / Edu)

The clearest current view is around **apps, connectors, and custom MCP apps** in Enterprise/Edu workspaces.

- **Workspace-level apps & connectors governance**  
  - Lives: "Apps" surface in Enterprise/Edu/Business workspaces; governed via Workspace settings → Permissions & roles → Custom roles.
  - Gates: Enterprise and Edu explicitly called out for RBAC; Business also mentioned for certain Google Drive controls.
  - Status: GA as of 2026‑01‑05 article update.
  - Ref: "Admin Controls, Security, and Compliance in apps (Enterprise, Edu, and Business)".

- **RBAC for apps (custom roles)**  
  - "Enterprise and Edu workspaces can assign apps to one or more custom roles… admins can control which roles have access."
  - Lives: Admin console for these workspaces.
  - Gates: Enterprise and Edu tiers; Business partially mentioned for specific features.
  - Status: GA.  

- **Custom apps using MCP**  
  - "Admins can also allow roles to access developer mode, which allows the creation and testing of custom apps using MCP."
  - Lives: Apps surface + developer mode; uses MCP as connector protocol.
  - Gates: Enterprise/Edu workspaces with developer mode; admin-controlled.
  - Status: GA, but custom apps explicitly "not verified by OpenAI" and "intended for developer use only".

- **Compliance API & Compliance Logs**  
  - "User conversations, including conversations using any app, are already available in the Compliance API… all app calls are logged as a part of the OpenAI Compliance Logs platform."
  - Lives: Enterprise compliance tooling + APIs.
  - Gates: Enterprise customers using Compliance API & Compliance Logs.
  - Status: GA.  

- **Granular Google Drive security (DWD)**  
  - Domain-wide delegation for synced Google Drive data is available to Business, Enterprise, and Edu workspaces.
  - Lives: Connected data configuration in workspace settings.
  - Status: GA.  

Other governance features you list (SSO/SCIM, data retention, audit logs at large, etc.) are strongly implied in healthcare-oriented secondary docs, but not fully enumerated in primary sources checked so far. Those are better treated as **partially evidenced** and need direct OpenAI enterprise docs to complete.

***

### C. Developer platform (Apps SDK + MCP-related)

Only the MCP/Apps SDK piece is directly evidenced here; the full APIs (Responses, Realtime, Batch, Images, etc.) are not re-documented in this pass.

- **Apps SDK**  
  - Lives: Developer platform for building "apps" that run in ChatGPT and organization workspaces.
  - Status: Example repo shows intended usage and capabilities, implying active SDK surface.
  - Primary ref: `openai/openai-apps-sdk-examples` GitHub repo.

- **Model Context Protocol (MCP) as standard connector spec**  
  - "The Model Context Protocol (MCP) is an open specification for connecting large language model clients to external tools, data, and user interfaces."
  - Lives: Protocol between OpenAI apps layer and external tools/servers.
  - Status: Actively used in Apps SDK examples (standardized wire format, auth, metadata).

- **MCP integration semantics**  
  - "Within the Apps SDK, MCP keeps the server, model, and UI in sync… A minimal MCP integration… implements three capabilities" with demo servers.
  - Lives: SDK integration layer; used by both OpenAI first-party tools and custom tools.
  - Status: GA for developer use (examples repo).  

- **OpenAI vector store MCP server (third-party but OpenAI-API-focused)**  
  - A production-ready MCP server for OpenAI Vector Store API, packaging OpenAI API usage into a standardized MCP server for orchestrators like Claude.
  - Lives: GitHub repo; Cloudflare Worker-based implementation; demonstrates OpenAI API usage wrapped as MCP tools.
  - Status: Community / practitioner; not first-party, but relevant for integration patterns.  

***

### D. Agentic / automation stack (Codex-oriented slice)

Codex here refers to Anthropic's **Claude Codex** environment; OpenAI's role is primarily as an API node and MCP/server provider. Evidence here is mostly practitioner/community class.

- **Codex MCP integration for OpenAI docs**  
  - A community post describes integrating Codex with OpenAI developer docs via OpenAI's official MCP server, with a shared setup for CLI or IDE extension.
  - Lives: MCP server controlled by OpenAI; consumed by Codex (Anthropic).
  - Status: Evidenced as available to practitioners as of 2026‑01‑09.

- **General pattern: OpenAI as MCP tool node in a Claude-centric constellation**  
  - The vector-store MCP server repo shows a typical pattern where Claude's MCP client calls an MCP server that, in turn, talks to OpenAI Vector Store APIs.
  - This is **not** OpenAI's own product, but it demonstrates a standard pattern for using OpenAI as a tool node within Claude's orchestration.

Other elements you requested (browser agents, computer-using agents, Codex CLI specifics, tool integration protocols beyond MCP, etc.) remain **UNKNOWN** in this evidence slice.

***

### E. Media stack

From the sources scanned, there is **no direct, first-party evidence** about current image/video/audio product SKUs, watermarks, or credit systems. Only two indirect pieces appear:

- Enterprise healthcare guides mention **HIPAA-compliant infrastructure** and "OpenAI for Healthcare" offerings, which strongly implies but does not enumerate specific media APIs.
- No direct mentions of DALL·E, Sora, or named media models appear in the checked sources.  

Thus: media stack details are **UNKNOWN** in this pass.

***

### F. Policy/governance surface (partial)

- **Apps and connectors data isolation & prompt-injection mitigations**  
  - "OpenAI applies ongoing testing, monitoring, and layered mitigation techniques to reduce prompt-injection risk… conversations that use apps have locked-down network access… all data remains encrypted in transit and at rest."
  - Lives: Apps platform, in Enterprise/Edu/Business.
  - Status: GA controls.  

- **Compliance surfaces for app usage**  
  - App conversations are included in the Compliance API and Compliance Logs, allowing audit and governance.
  - Lives: Enterprise governance APIs and logging surface.

- **Healthcare / HIPAA context (secondary)**  
  - Healthcare-focused guides describe OpenAI as offering BAAs, data residency, audit logs, customer-managed keys, SAML SSO, and SCIM as part of an enterprise-grade security posture.
  - These are **secondary** and must be cross-checked against first-party enterprise docs; for now, treat details as **Medium confidence** and tier mapping as **UNKNOWN**.

***

## 2) Tax code matrices (abbreviated, evidence-based slice)

Given the limited surfaces scanned, full matrices by Free/Plus/Pro/Business/Enterprise/API are not possible yet. Below is a **sample matrix** focusing on what is directly tier-gated in the evidence.

### 2.2 Agentic / apps tools (sample matrix)

**Rows**: specific features with evidence; **Columns**: Plus / Teams (Business proxy) / Enterprise / API.

| Feature                                      | Plus                     | Teams/Business           | Enterprise/Edu                        | API            |
|----------------------------------------------|--------------------------|--------------------------|----------------------------------------|----------------|
| Work with Apps (read coding apps, macOS)     | Y – early beta; Plus. | Y – early beta; Teams. | UNKNOWN (not mentioned).        | N (UI feature) |
| Custom apps using MCP in workspace           | UNKNOWN                  | UNKNOWN                  | Y – via developer mode & apps.  | N (client)     |
| Apps RBAC (assign apps to custom roles)      | N (consumer)             | UNKNOWN                  | Y – Enterprise/Edu only.        | N              |
| Compliance API coverage for app conversations| N                        | UNKNOWN                  | Y – Enterprise via Compliance API. | N          |

Notes:  
- Pro vs Plus is not distinguished in checked sources; **Pro** is therefore **UNKNOWN** across rows.  
- API = OpenAI public API; Apps & RBAC are client/org features, not API primitives.

***

## 3) Limits & quotas (official vs observed)

The scanned sources do **not** give concrete numeric message caps, video credits, deep research limits, etc. Therefore, for Plus/Pro limit tables, **all numeric values are UNKNOWN** in this pass. Where behavior is described qualitatively, that is noted.

Sample partial "limits ledger" rows (non-numeric):

| Surface                | Tier            | Claim                                                                 | Official/Observed | Evidence                                |
|------------------------|-----------------|-----------------------------------------------------------------------|-------------------|-----------------------------------------|
| Apps access by role    | Enterprise/Edu  | Apps are assignable to roles; admins can restrict which roles can use which apps. | Official          | Admin Controls article.          |
| Apps network access    | Enterprise/Edu  | "Conversations that use apps have locked-down network access…" | Official          | Admin Controls article.          |
| Voice on macOS app     | All macOS users | Voice experience removed after 2026‑01‑15 on macOS app only. | Official       | ChatGPT release notes + news. |

All message caps, context windows, project caps, etc. = **UNKNOWN** from the sources scanned here.

***

## 4) Deprecation / rename / roadmap signals (partial)

### 4.1 Deprecation table (sample)

| Surface          | Change                           | Date effective        | Replacement / Migration path                        | Evidence                        |
|------------------|----------------------------------|-----------------------|-----------------------------------------------------|---------------------------------|
| Voice on macOS   | Voice experience retiring        | 2026‑01‑15            | Use voice in web, iOS, Android, Windows apps instead. | ChatGPT release notes; news. |

No other deprecations (e.g., named models, plugins) appear in the checked sources.

### 4.2 Rename/merge radar

No explicit first-party rename mapping (e.g., "Custom GPTs → Apps") appears in the sources scanned. Treat rename map as **UNKNOWN** here.

### 4.3 Likely-to-change watchlist (from evidence seen)

Items that show recent, evolving behavior:

- Apps & connectors RBAC configuration and Compliance Logs integration (new article, 2026‑01‑05).
- Voice experiences across platforms (macOS voice sunset, consolidation in others).
- Apps SDK + MCP semantics and widget bundles, which are still documented in example repos and may evolve quickly.
- MCP servers for OpenAI APIs built by community (e.g., vector-store, docs server) that may track OpenAI API evolution.

These should be re-checked at least **monthly**.

***

## 5) Codex & "developer-agent" deep dive (integration slice)

Your routing reality: **Claude/Claude Code as orchestrator, OpenAI as MCP-served tool node.**

From current evidence, the relevant architectural pieces are:

- MCP as the wire protocol between Claude Codex and OpenAI-backed tools.  
  - Example: the OpenAI vector-store MCP server wraps OpenAI Vector Store API calls and exposes them via MCP to clients like Claude.
  - Apps SDK examples highlight how MCP responses carry both structured JSON and `_meta.openai/outputTemplate` metadata for UI hydration in OpenAI clients; the same patterns are usable when Claude is the LLM client.

- Codex ↔ OpenAI docs MCP server  
  - The practitioner post shows Codex connecting to an **OpenAI-maintained docs MCP server** to query OpenAI developer documentation.
  - This illustrates a pattern for "developer-agent" use: Codex as reasoning engine + MCP tool server as read-only documentation or vector store.  

Given that there is no first-party, detailed spec for OpenAI's own "developer agent" analogs in the scanned sources, a **Claude Code vs OpenAI developer agent** comparison is largely **UNKNOWN** here.

Nevertheless, in a Claude-centric constellation:

- **Interaction modes**  
  - Codex supports interactive (REPL-like) development flows and can call MCP tools in parallel; OpenAI's role is to serve tools (vector stores, docs servers, Apps SDK-based connectors).

- **Tool integration**  
  - MCP servers encapsulate OpenAI APIs, making it easier to share them across Claude and other MCP-speaking clients without per-orchestrator reimplementation.

Further specifics (permissions model, context management, parallelization strategies within OpenAI's own "agents") cannot be reliably stated from current evidence.

***

## 6) Browser / computer agents

The scanned sources **do not** surface OpenAI-branded browser agents or computer-use agents as distinct named products. Only incidental references exist:

- macOS "Work with Apps" feature allows reading from coding apps; this is a local integration, not a browser automation agent.
- Apps that connect to data sources via connectors and MCP may access external systems, but their autonomy and browsing behavior is constrained and network-locked per OpenAI's security overview.

Thus, all of the following are **UNKNOWN** in this pass: "ChatGPT agent mode", any dedicated browser agent products, API for computer control, and their autonomy/error-recovery.

***

## 7) Unique capabilities vs Claude (subscription justification slice, MCP-centric)

Since a full enumeration of OpenAI products is missing here, this section focuses on **MCP-level additive value** to a Claude-centric system.

### 7.1 "No Claude equivalent" (in the MCP/tool sense)

From the evidence:

- **OpenAI vector-store APIs as a managed retrieval backend**  
  - Accessible via community MCP server (`openai-vector-assistant-mcp`) that wraps OpenAI's vector store APIs in a standardized way.
  - Claude does not provide *OpenAI's* managed vector store; using this MCP server adds a differentiated retrieval backend that can be shared across orchestrators.  

- **OpenAI developer docs MCP server**  
  - Official MCP server exposing OpenAI's developer docs, which Codex can connect to.
  - For workflows where Codex must stay in sync with OpenAI API evolution, this is a unique, first-party documentation source.  

### 7.2 Overlap but useful for verification

- **Compliance and logging for app conversations in Enterprise**  
  - Having OpenAI's Compliance API and Compliance Logs for app conversations provides a second, independent audit trail when Claude is used primarily for logic and OpenAI for app/workspace-side usage.
  - This can be valuable for cross-verifying safety, access, and data flows in regulated sectors (e.g., healthcare, where OpenAI's HIPAA posture is documented).

***

## 8) Integration architecture for a Claude-centric constellation (MCP pattern)

Given the strong evidence that MCP is the standard tool protocol on the OpenAI side and is supported in the Claude ecosystem, a **canonical pattern** emerges:

- **Tool layer**:  
  - Implement OpenAI-facing MCP servers that:  
    - Wrap OpenAI APIs (vector stores, future media APIs, etc.).
    - Optionally use Apps SDK patterns for output templates and richer UI metadata, which Claude can ignore or partially use.

- **Routing decision tree (high-level)**:  
  - Tasks needing:  
    - **OpenAI-managed retrieval or OpenAI-specific docs** → route to MCP tools pointing at OpenAI APIs/docs.
    - **Enterprise governance with Compliance Logs** → prefer OpenAI apps/workspaces as the client surface.
    - General code reasoning, multi-tool orchestration, or broader non-OpenAI tools → route to Claude/Claude Code as primary.  

- **UI handoffs**:  
  - For org users: launch OpenAI "apps" (including custom MCP apps) inside Enterprise/Edu workspace where RBAC and compliance apply.
  - For developers: open Codex sessions connected to shared MCP tool servers, including OpenAI vector store MCP server and docs MCP server.

- **Operational concerns**:  
  - Logging: centralize MCP server logs plus OpenAI Compliance Logs and Claude logs for full observability.
  - Privacy: treat MCP servers as data-processors; ensure encryption in transit and at rest (OpenAI already enforces this for its side).

Many deeper details (e.g., specific reliability SLOs, retry semantics, token accounting) remain **UNKNOWN** here.

***

## 9) Cost / value model (status: UNKNOWN in this pass)

The current scan did not cover OpenAI's pricing pages or model/token tables, so:

- Subscription tiers (Free / Plus / Pro / Business / Enterprise) and their pricing are **UNKNOWN** here.  
- API pricing (tokens, video/image/audio, etc.) is also **UNKNOWN**.  

To build the full break-even analysis you requested, a second pass must explicitly target:

- ChatGPT plans & pricing pages.  
- API pricing tables and per-model specs.  

***

## 10) Appendices (abbreviated)

### 10A) Evidence ledger (for non-trivial claims in this pass)

| ID | Claim (one sentence) | Source class | Source title + publisher | Pub/updated date | Supporting excerpt (≤2 sentences) | Confidence |
|----|----------------------|--------------|--------------------------|------------------|-----------------------------------|------------|
| E1 | ChatGPT macOS app supports canvases, tasks, and projects, with project creation still on web. | First-party | ChatGPT MacOS app release notes – OpenAI Help Center | 2025‑01‑15 section | "Now, you can create and edit canvases on macOS using GPT 4o… Added support for Tasks. Added support for working in Projects. (For now, you'll still have to create them first on web.)" | High |
| E2 | ChatGPT macOS app includes a "Work with Apps" feature that reads from coding apps in early beta for Plus and Teams. | First-party | ChatGPT MacOS app release notes – OpenAI Help Center | 2024‑11‑14 section | "ChatGPT can now read content from your coding apps… This early beta is available to Plus and Teams users." | High |
| E3 | The macOS ChatGPT desktop app has a companion window with global Option+Space shortcut. | First-party | ChatGPT MacOS app release notes | 2024‑08‑06 | "The macOS desktop app now gives you side-by-side access to ChatGPT with the new companion window… Use the Option + Space shortcut to start a new chat…" | High |
| E4 | Voice experience in the macOS ChatGPT app is being retired effective January 15, 2026. | First-party | ChatGPT — Release Notes – OpenAI Help Center | 2025‑12‑11 | "We're retiring the Voice experience in the ChatGPT macOS app on January 15, 2026." | High |
| E5 | After retirement on macOS, Voice remains available on chatgpt.com, iOS, Android, and Windows app. | Press citing first-party support | "ChatGPT Mac app users will lose this key feature…" – Business Today | 2025‑12‑22 | "…it will be dropping its Voice feature for Mac users after January 15, 2026… However, the feature will be available on chatgpt.com, iOS, Android, and the Windows app." | Medium |
| E6 | ChatGPT Windows desktop app is installable via winget. | First-party | Windows App – Release Notes – OpenAI Help Center | 2025‑01‑30 update | "Install with winget. winget is now a supported way to install ChatGPT." | High |
| E7 | Enterprise and Edu workspaces have RBAC to assign apps to custom roles. | First-party | Admin Controls, Security, and Compliance in apps – OpenAI Help Center | 2026‑01‑05 | "Enterprise and Edu workspaces can assign apps to one or more custom roles… admins can control which roles have access." | High |
| E8 | Admins can allow roles to create/test custom apps using MCP in developer mode. | First-party | Admin Controls… – OpenAI Help Center | 2026‑01‑05 | "Admins can also allow roles to access developer mode, which allows the creation and testing of custom apps using MCP." | High |
| E9 | Conversations using apps have locked-down network access, with data encrypted in transit and at rest. | First-party | Admin Controls… – OpenAI Help Center | 2026‑01‑05 | "Conversations that use apps have locked-down network access… all data remains encrypted in transit and at rest." | High |
| E10 | App conversations are available via Compliance API and logged in the OpenAI Compliance Logs platform. | First-party | Admin Controls… – OpenAI Help Center | 2026‑01‑05 | "User conversations, including conversations using any app, are already available in the Compliance API… all app calls are logged as a part of the OpenAI Compliance Logs platform." | High |
| E11 | Business, Enterprise, and Edu can use domain-wide delegation (DWD) for Google Drive connectors. | First-party | Admin Controls… – OpenAI Help Center | 2026‑01‑05 | "Owners for Business, Enterprise, and Edu workspaces are able to utilize domain-wide delegation (DWD)." | High |
| E12 | The Model Context Protocol (MCP) is an open specification for connecting LLM clients to tools, data, and UIs. | First-party (GitHub) | openai/openai-apps-sdk-examples – GitHub | 2025‑10‑05 | "The Model Context Protocol (MCP) is an open specification for connecting large language model clients to external tools, data, and user interfaces." | High |
| E13 | Within the Apps SDK, MCP standardizes wire format, auth, and metadata and keeps server, model, and UI in sync. | First-party (GitHub) | openai/openai-apps-sdk-examples – GitHub | 2025‑10‑05 | "Within the Apps SDK, MCP keeps the server, model, and UI in sync. By standardizing the wire format, authentication, and metadata…" | High |
| E14 | The Apps SDK repo ships demo MCP servers (Pizzaz, Solar system) whose tool responses include JSON and `_meta.openai/outputTemplate`. | First-party (GitHub) | openai/openai-apps-sdk-examples – GitHub | 2025‑10‑05 | "The repository ships several demo MCP servers… Every tool response includes plain text content, structured JSON, and `_meta.openai/outputTemplate` metadata…" | High |
| E15 | `openai-vector-assistant-mcp` is a production-ready MCP server providing OpenAI Vector Store API access via multiple deployment options. | Practitioner (GitHub) | jezweb/openai-vector-assistant-mcp – GitHub | 2025‑07‑28 | "A production-ready Model Context Protocol (MCP) server that provides comprehensive OpenAI Vector Store API access through multiple deployment options." | High |
| E16 | The vector MCP server is implemented as a Cloudflare Worker with an MCP handler and OpenAI service wrapper. | Practitioner (GitHub) | jezweb/openai-vector-assistant-mcp – GitHub | 2025‑07‑28 | "Worker – Handles HTTP requests… MCP Handler – Implements MCP protocol… OpenAI Service – Wraps OpenAI Vector Store API calls." | High |
| E17 | Codex can integrate with OpenAI's developer documentation via OpenAI's official MCP server from CLI or IDE extension. | Practitioner/community | "Connect Codex to OpenAI Developer Docs via MCP" – OpenAI Community | 2026‑01‑09 | "You can now easily integrate Codex with OpenAI's developer documentation through OpenAI's official MCP server, directly from your CLI or IDE extension." | Medium |
| E18 | OpenAI for Healthcare deployments emphasize data residency, audit logs, customer-managed keys, SAML SSO, and SCIM. | Practitioner/secondary | "OpenAI for Healthcare: Complete 2026 Guide to HIPAA-Compliant AI" – ALM Corp | 2026‑01‑09 | "Enterprise Security Features: Data residency options… Comprehensive audit logs… Customer-managed encryption keys… SAML SSO and SCIM…" | Medium |
| E19 | OpenAI for Healthcare clinical documentation guides describe BAAs and HIPAA safeguards (administrative, physical, technical). | Practitioner/secondary | "OpenAI for Healthcare: Complete 2026 Clinical Documentation Guide" – SoapNoteAI | 2026‑01‑07 | "OpenAI for Healthcare includes comprehensive HIPAA compliance… Business Associate Agreements (BAAs)… Access controls and encryption… Audit controls and logging…" | Medium |

(Additional entries would be added as more surfaces are scanned.)

***

### 10B) Source map (grouped)

- **First-party, docs/help**: ChatGPT Release Notes; macOS app release notes; Windows app release notes; Admin Controls, Security, and Compliance in apps.
- **First-party, GitHub**: openai/openai-apps-sdk-examples.
- **Practitioner/community**: OpenAI vector MCP server repo; Codex–OpenAI docs MCP community thread.
- **Press**: Business Today article on macOS voice removal.
- **Sector guides**: ALM Corp healthcare guide; SoapNoteAI healthcare documentation guide.

***

### 10C) Known unknowns + how to resolve

Key "unknowns" relative to your full spec:

- Full list of ChatGPT consumer features (deep research, projects, canvas, custom GPTs, store, browsing).  
- Tier matrices (Free/Plus/Pro/Business/Enterprise/API), including numeric limits.  
- Full API model catalog with context windows, pricing, modalities, and tool availability.  
- Media stack specifics (image/video/audio, watermarks, credit systems).  
- Detailed org governance: full SSO/SCIM options, retention, audit log schema, data residency SKUs.  
- Any OpenAI-branded browser/computer-use agents and their APIs.  
- Deprecation and rename history for models and products.

**Resolution plan** (for each):  
- Target: OpenAI pricing pages, developer docs index, changelogs, and Help Center plan articles.  
- Cross-check with GitHub SDKs and first-party announcements ("Introducing…" posts).  
- For limits, supplement with large-sample practitioner reports but clearly label as "observed".  

***

### 10D) Re-run playbook (monthly/quarterly)

To extend this into the full "tax code" you want:

1. **Monthly**  
   - Scrape and diff: ChatGPT Release Notes, app release notes (macOS, Windows, iOS, Android), and Admin Controls/Enterprise docs.
   - Diff `openai/openai-apps-sdk-examples` and any official OpenAI MCP/tooling repos for new capabilities.

2. **Quarterly**  
   - Rebuild pricing & model matrices from first-party pricing and docs.  
   - Refresh org/governance scans (compliance, data residency, SSO/SCIM).  
   - Re-scan practitioner MCP servers and Codex integration guides for new patterns.

3. **Change detection**  
   - Track last-updated timestamps and commit hashes.  
   - Maintain a rename/deprecation ledger keyed to first-party deprecation notices and changelog entries.  

This skeleton is designed so you can now plug in additional evidence (pricing, model specs, more Help Center docs) and grow it into the full 10-part report you described, without silently inferring anything that is not supported.

(https://help.openai.com/en/articles/9703738-chatgpt-macos-app-release-notes)
(https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
(https://help.openai.com/en/articles/10003026-windows-app-release-notes)
(https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business)
(https://github.com/openai/openai-apps-sdk-examples)
(https://github.com/jezweb/openai-vector-assistant-mcp)
(https://almcorp.com/blog/openai-for-healthcare-complete-guide-2026/)
(https://community.openai.com/t/connect-codex-to-openai-developer-docs-via-mcp/1371352)
[9](https://www.soapnoteai.com/soap-note-guides-and-example/openai-for-healthcare-2026/)
(https://www.businesstoday.in/technology/news/story/chatgpt-mac-app-users-will-lose-this-key-feature-after-january-15-all-details-507805-2025-12-23)