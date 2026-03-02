## Verification: Google, YouTube & xAI API Surfaces

The claim is **verified**: these are genuinely distinct API surfaces with different auth shapes, access models, and credential scopes — they should not be treated as one undifferentiated toolset.

***

## Surface-by-Surface Breakdown

### Gemini API / Google AI Studio

This is a **developer-first API surface** at `https://generativelanguage.googleapis.com/v1beta/`, distinct from Vertex AI. Authentication uses a flat API key passed as the `x-goog-api-key` HTTP header or `GEMINI_API_KEY` / `GOOGLE_API_KEY` environment variable. Keys are provisioned directly through Google AI Studio (ai.google.dev) with no GCP project required — making this the lowest-friction Google AI surface. REST, Python, Go, and JavaScript SDKs are all officially supported. [ai.google](https://ai.google.dev/gemini-api/docs)

### Vertex AI (Gemini on Vertex)

Vertex AI is a **GCP-native surface** and is architecturally separate from the Gemini Developer API, even when accessing the same underlying models. Auth requires either a **Google Cloud API key** or **Application Default Credentials (ADC)** via `gcloud auth application-default login`. For production workloads, a GCP service account with a JSON key file is standard, with the `GOOGLE_APPLICATION_CREDENTIALS` env var pointing to that file. A GCP project ID and region are mandatory parameters. Vertex AI Studio (within GCP console) is a browser UI companion, not an API surface. [googleapis.github](https://googleapis.github.io/python-genai/)

### NotebookLM (Personal vs. Enterprise)

**Personal NotebookLM** (notebooklm.google.com) is **browser-only** — there is no official public API. Unofficial community implementations exist via browser automation or intercepted JSON calls, but these are unsupported. **NotebookLM Enterprise** is a distinct GCP-provisioned product with IAM-based access control; it uses predefined roles (`Cloud NotebookLM Admin`, `Cloud NotebookLM User`) and supports Google Workspace/Cloud Identity or third-party IdP via Workforce Identity Federation. Enterprise access is managed via GCP Console, not the personal UI. [docs.cloud.google](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview)

### GCP Resources (General)

GCP is not a single API surface but a **project-scoped infrastructure layer** that underlies Vertex AI, NotebookLM Enterprise, and other services. Auth universally flows through IAM: ADC for local dev, service account JSON keys for programmatic access, and optionally Workload Identity Federation for non-Google identity providers. Each service within GCP has its own required IAM roles and may require the relevant API to be enabled per project. [docs.cloud.google](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm)

### YouTube Data API v3

This surface is **entirely separate from Google's AI products** — it lives at `https://www.googleapis.com/youtube/v3` and is governed by the Google Developer Console. Auth is **dual-mode**: a plain API key suffices for public read operations (videos, playlists, search), but **OAuth 2.0 is mandatory** for any write operations (uploads, playlist edits) or retrieval of authenticated user private data. This means credential shape differs significantly depending on capture intent: read-only capture needs only a key, but write/private access requires an OAuth flow with user consent. [developers.google](https://developers.google.com/youtube/v3/docs)

### xAI API

The xAI API (Grok) lives at `https://api.x.ai/v1` and is **OpenAI SDK-compatible** — migration from OpenAI requires only changing the base URL and API key. Auth uses a standard HTTP Bearer token: `Authorization: Bearer YOUR_API_KEY`. Keys are team-scoped and provisioned via `console.x.ai`, which requires an X (Twitter) account for login. The management API supports fine-grained key/team/ACL controls. There is no Google dependency or GCP project involvement. [docs.x](https://docs.x.ai/developers/quickstart)

***

## Auth Shape Reference

| Surface | Access Model | Auth Credential | Key Source |
|---|---|---|---|
| Gemini API / AI Studio | Full API | `x-goog-api-key` header | ai.google.dev console |
| Vertex AI | Full API (GCP-native) | ADC / service account JSON / GCP API key | GCP project IAM |
| NotebookLM (personal) | **Browser-only** | Google account session | No API |
| NotebookLM Enterprise | Browser UI + IAM | Cloud Identity / 3rd-party IdP + IAM roles | GCP project setup |
| GCP (general resources) | API (per-service) | Service account / ADC / Workload Identity | GCP IAM |
| YouTube Data API v3 | Full API | API key (reads) or OAuth 2.0 (writes/private) | Google Developer Console |
| xAI API | Full API | Bearer token (team-scoped API key) | console.x.ai |

***

## Caveats and Confidence Limits

- **NotebookLM personal API absence** is confirmed by official Google developer forum staff as of late 2024; this status should be re-verified before any tooling decision that depends on programmatic access to the personal product. [discuss.ai.google](https://discuss.ai.google.dev/t/notebooklm-api/55950)
- The xAI console onboarding note about requiring X Premium  appears in a third-party source, not the official xAI docs — treat as **inference, not verified fact**. [apideck](https://www.apideck.com/blog/how-to-get-your-grok-xai-api-key)
- Vertex AI and Gemini API share underlying models but have **different billing, quota, and feature availability** — this is strongly implied by the SDK's conditional environment variable logic  but full feature-parity details would require direct comparison of Vertex and AI Studio feature matrices. [googleapis.github](https://googleapis.github.io/python-genai/)
- All source dates are February–March 2026, making this current as of the verification date. [ai.google](https://ai.google.dev/api)