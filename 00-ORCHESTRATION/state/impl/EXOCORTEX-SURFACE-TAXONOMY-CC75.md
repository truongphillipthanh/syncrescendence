# Exocortex Surface Taxonomy — CC75

**Date**: 2026-03-02  
**Purpose**: define a policy-compliant internal taxonomy for current and near-term exocortex surfaces after the first Oracle/Perplexity packet round

---

## Scope

This taxonomy is intentionally narrower than the Oracle response.

It only uses:

- current repo boundary contract
- current capture modes
- implemented runtime truth
- externally verified surface distinctions that survived assessment

It does **not** assume that future IIC routing, Oracle-central control, or new capture modes already exist.

---

## Status Vocabulary

- `implemented` = already has a real bridge or runtime path in the repo
- `packetized` = dispatch/landing packet path exists, but surface is not otherwise integrated
- `planned` = surface is recognized and bounded, but wrapper/bridge work has not yet been built

---

## Surface Taxonomy

| Surface Slug | Service / Class | Status | Category | Access Model | Current Owning Harness | Notes |
|---|---|---:|---|---|---|---|
| `oracle_web_surface` | Grok / Oracle web | `packetized` | strategic hypersensing | web | Commander relay | outbound packet + response bridge now exist |
| `perplexity_web_surface` | Perplexity web | `packetized` | external verification | web | Commander relay | outbound packet + response bridge now exist |
| `manus_workflow_surface` | Manus API / runs | `implemented` | autonomous backend execution | API | Manus | checkpoint bridge already exists |
| `github_issue_pr_surface` | GitHub issues / PRs / CI | `implemented` | coordination + verification | API/web | Commander local | issue bridge already exists |
| `cloudflare_dns_domain_surface` | Cloudflare / tunnel / DNS | `implemented` | domain + edge infrastructure | CLI/API | Commander local | bridge already exists |
| `slack_discord_runtime_surface` | Slack + Discord runtime state | `implemented` | channel runtime state | runtime | OpenClaw + Commander local | provider/runtime bridge exists; end-to-end dispatch still downstream-blocked |
| `obsidian_repo_surface` | repo-backed Obsidian notes | `implemented` | local exocortex writing surface | local CLI | Commander local | repo-backed bridge exists; `.obsidian/` remains non-authoritative |
| `google_model_surface` | Gemini API / AI Studio / Vertex model calls | `planned` | model execution | API | Commander local or future wrappers | must be separated from GCP infra and NotebookLM |
| `gcloud_resource_surface` | GCP projects / services / infra | `implemented` | cloud infrastructure | CLI/API | Commander local | readiness/status path exists; richer wrappers still planned |
| `notebooklm_surface` | NotebookLM personal / enterprise | `planned` | source-bounded synthesis | web | Commander relay initially | treat personal as browser-only until official API reality changes |
| `youtube_feed_surface` | YouTube Data API | `planned` | feed/media ingestion | API | Commander local or future wrapper | likely Feedcraft backbone |
| `xai_model_surface` | xAI API | `planned` | model execution | API | Commander local or future wrapper | must remain distinct from Grok web Oracle |
| `claude_cowork_surface` | Claude Cowork | `planned` | collaborative external execution | web/API | Commander relay initially | should follow same packet/landing contract |
| `feedcraft_surface` | Feedcraft subsystem | `planned` | feed conditioning + publication logic | hybrid | future dedicated wrapper | higher-order subsystem over multiple exocortex surfaces |
| `iic_line_surface` | IIC governance layer | `planned` | identity/governance overlay | internal | future stage | not a raw tool surface; governs surface ownership and flow later |

---

## Allowed Durable Capture Modes

These remain limited to current repo-approved modes only:

- `none`
- `pointer`
- `summary_markdown`
- `typed_record`
- `summary_and_typed_record`

No additional capture modes are ratified.

---

## Ownership Rule

For now, ownership should remain pragmatic and reality-based:

- `Commander local` when the surface is already accessible deterministically from this machine
- `Commander relay` when the surface is web-native and still depends on human/web relay
- `Manus` when the surface is better handled as bounded autonomous backend execution
- `future dedicated wrapper` only when no current wrapper exists yet

This is intentionally less ambitious than the Oracle ownership matrix.

---

## Immediate Next Extensions

The next wrappers should likely be:

1. `notebooklm_surface`
2. `youtube_feed_surface`
3. `xai_model_surface`
4. `claude_cowork_surface`

Only after those begin to exist should Feedcraft and IIC move from conceptual overlays into tooling artifacts.
