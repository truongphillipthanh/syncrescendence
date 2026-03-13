# Ajna Exocortex Access Program — CC93

- Generated: `2026-03-13T06:27:04Z`
- Office: `ajna`
- Designated browser: `vivaldi` via OpenClaw profile `vivaldi`
- Mission: Give Ajna broad exocortex reach while keeping repo truth, least-privilege credentials, and staged onboarding discipline intact.

## Design Law

- Ajna is the browser-first exocortex operator, not the constitutional authority.
- Repo artifacts remain ratified truth; exocortex surfaces are execution, sensing, and relay surfaces.
- Access expansion must be staged by wave, not improvised tab sprawl.
- Parent-auth children must never be treated as independent identity roots.

## Counts

- `strategy_counts`: `{'browser_only': 1, 'browser_then_api': 32, 'browser_then_api_cli': 4, 'parent_auth_then_surface': 2}`
- `surface_count`: `39`
- `wave_counts`: `{'wave0_live_runtime': 2, 'wave1_priority_hubs': 12, 'wave2_secondary_systems': 15, 'wave3_long_tail': 10}`

## Waves

### wave0_live_runtime

- already-live operator bus and runtime comms surfaces
- `discord_surface`: `Discord` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `slack_surface`: `Slack` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`

### wave1_priority_hubs

- identity roots, work hubs, intelligence hubs, and operational P1 rails
- `airtable_surface`: `Airtable` | strategy=`browser_then_api` | role=`secondary_to_cli_or_automation` | priority=`P1`
- `chatgpt_openai_surface`: `ChatGPT/OpenAI` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `claude_anthropic_surface`: `Claude/Anthropic` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `cloudflare_surface`: `Cloudflare` | strategy=`browser_then_api_cli` | role=`secondary_to_cli_or_automation` | priority=`P1`
- `coda_surface`: `Coda` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `github_surface`: `GitHub` | strategy=`browser_then_api_cli` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `linear_surface`: `Linear` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `make_surface`: `Make` | strategy=`browser_then_api` | role=`secondary_to_cli_or_automation` | priority=`P1`
- `manus_surface`: `Manus` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `notion_surface`: `Notion` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `perplexity_surface`: `Perplexity` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`
- `youtube_surface`: `YouTube` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P1`

### wave2_secondary_systems

- secondary but still operationally meaningful surfaces
- `basecamp_surface`: `Basecamp` | strategy=`browser_only` | role=`primary_browser_operator` | priority=`P2`
- `canva_surface`: `Canva` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `clickup_surface`: `ClickUp` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `confluence_surface`: `Confluence` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `figma_surface`: `Figma` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `grok_surface`: `Grok` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `huggingface_surface`: `Hugging Face` | strategy=`browser_then_api_cli` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `incident_surface`: `Incident` | strategy=`parent_auth_then_surface` | role=`primary_auth_and_browser_operator` | priority=`P2` parent=`slack_surface`
- `jira_surface`: `Jira` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `openrouter_surface`: `OpenRouter` | strategy=`browser_then_api` | role=`secondary_to_cli_or_automation` | priority=`P2`
- `supabase_surface`: `Supabase` | strategy=`parent_auth_then_surface` | role=`secondary_to_cli_or_automation` | priority=`P2` parent=`github_surface`
- `ticktick_surface`: `TickTick` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `todoist_surface`: `Todoist` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `x_surface`: `X` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P2`
- `zapier_surface`: `Zapier` | strategy=`browser_then_api` | role=`secondary_to_cli_or_automation` | priority=`P2`

### wave3_long_tail

- lower-priority or highly manual surfaces that should not block the control plane
- `atlassian_projects_surface`: `Projects (Atlassian)` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `dropbox_surface`: `Dropbox` | strategy=`browser_then_api` | role=`secondary_to_cli_or_automation` | priority=`P3`
- `loveable_surface`: `Loveable` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `miro_surface`: `Miro` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `oracle_cloud_surface`: `Oracle Cloud` | strategy=`browser_then_api_cli` | role=`secondary_to_cli_or_automation` | priority=`P3`
- `reddit_surface`: `Reddit` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `replit_surface`: `Replit` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `tiktok_surface`: `TikTok` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `trello_surface`: `Trello` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P3`
- `twitch_surface`: `Twitch` | strategy=`browser_then_api` | role=`primary_auth_and_browser_operator` | priority=`P4`

## Operational Reading

- `browser_only` and `browser_then_api` surfaces are Ajna-primary.
- `browser_then_api_cli` surfaces are shared: Ajna handles login/browser auth, terminal harnesses consume stable CLI/API afterwards.
- `secondary_to_cli_or_automation` surfaces should still be visible to Ajna, but they should not distort role boundaries or make Ajna the new backend.

