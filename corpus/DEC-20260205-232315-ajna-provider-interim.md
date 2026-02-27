Decision ID: DEC-20260205-232315-ajna-provider-interim
Choice: Interim Ajna revival strategy: move Ajna’s primary LLM provider away from Anthropic Max to **OpenAI (openai-codex OAuth)** via OpenClaw, while keeping OpenClaw as the orchestrator substrate. Do not attempt to use “ChatGPT Plus” as an automation provider (Plus is a web subscription, not a stable orchestration API surface).
Why (lens 1-2): Meet the Moment (Anthropic plan instability), Systems Thinking (keep orchestrator stable; swap model brain)
Falsifier: If openai-codex OAuth becomes unavailable or too rate-limited for Ajna’s workload, we must pivot to a provider with stable API access (OpenAI API key, Gemini API, or Moonshot/Kimi API) and update routing accordingly.
Reversibility type: costly-reversible
Touched surfaces: OpenClaw config on Mac mini (~/.openclaw/openclaw.json); routing docs (COCKPIT.md/CANON-31150); watchers invoking `openclaw agent`
Evidence pointers: COCKPIT.md (Ajna role = LOCAL ORCH); openclaw.json auth.profiles (openai-codex:default = oauth)

DecisionAtom: DEC-20260205-232315-ajna-provider-interim
IntentionLink: —
Fingerprint: 1db3a82
