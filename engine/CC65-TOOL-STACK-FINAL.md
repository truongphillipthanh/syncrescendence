# CC65 — Tool Stack Final Allocation

**Date**: 2026-03-01
**Status**: FINAL — supersedes CC63-TOOL-STACK-STRATEGY.md
**Authority**: Commander synthesis of 3 Oracle dispatches + Sovereign directives

---

## The Decision

The tool stack question is answered. Three Oracle dispatches (full strategy review, subscription triage, OpenClaw architecture) plus Sovereign corrections converge on a single architecture.

---

## I. Constellation Architecture — The Pedigree

```
Sovereign
    ↓ (vague strategic intent)
Ajna [CSO — Strategos]
    Claude Sonnet via OpenClaw (Max setup-token, MBA)
    Hyper-concise fortress dispatches — compress on send, expand on receive
    Haiku for routine/structured dispatches (same OpenClaw, model flag swap)
    ↓
    ├── Commander [COO — Viceroy]
    │   Claude Opus via Claude Code (native, MBA, same Max sub)
    │   Receives structured tasks, expands from repo context, executes
    │
    ├── Psyche [CTO — Synaptarch]
    │   GPT-5.3-codex via OpenClaw Gateway (Mac mini)
    │   Receives structured calibration tasks from Ajna
    │
    ├── Adjudicator [CQO — Executor]
    │   Codex CLI (native, Mac mini)
    │   Receives verification/engineering tasks
    │
    ├── Cartographer [CIO — Exegete]
    │   Gemini Pro 3.1 via Gemini CLI (native, Mac mini)
    │   Receives survey/mapping tasks
    │
    ├── Kimi daemon [repo maintenance + CRUSH batches]
    │   Kimi K2.5 via OpenCode (Mac mini, NVIDIA NIM free)
    │   Always-on. Receives batch tasks from Ajna or Commander.
    │
    └── Oracle [sensing]
        SuperGrok (Sovereign-relayed, not programmatic yet)
        xAI data sharing enrollment unlocks programmatic dispatch
```

**Dispatch direction**: Ajna dispatches FROM OpenClaw downward. This is the pedigree — strategist commands operators. The C-suite labels are cognitive function type signatures, not org chart cosplay. The hierarchy exists because CRUSH will reveal what it needs, and the strategist layer (Ajna) routes work to the specialist that fits.

**The fortress protocol**: Ajna's outbound dispatches are hyper-concise — task ID, agent target, objective, constraints, success criteria. No prose. No context the receiver can derive from repo. Expansion happens on receipt. This minimizes Ajna's token footprint through OpenClaw (3-5 rate limit hits per dispatch cycle) and keeps Max viable for both Ajna and Commander.

**If Max rate limits collide**: Onboard Account 3 (Claude Pro, $20/mo) for dedicated Ajna capacity. This is contingent, not committed. Test first.

---

## II. Subscription Stack — 30-Day Sprint (March 2026)

### Secured ($210/mo — committed, burning)

| Service | $/mo | Function | Status |
|---------|------|----------|--------|
| Claude Max | $100 | Commander (Claude Code) + Ajna (OpenClaw Sonnet/Haiku) | ACTIVE — Ajna pending OpenClaw revival |
| Manus Pro | $40 | Autonomous backend engineer | DEPLOY THIS WEEK on VPS pipeline |
| SuperGrok | $30 | Oracle sensing | ACTIVE |
| ChatGPT Plus | $20 | Psyche + Adjudicator (when mini revives) | DORMANT — mini anesthetized |
| Gemini Pro | student/$0 | Cartographer (Gemini CLI) + NotebookLM + Antigravity + GCP credits | ACTIVE (partially) |

### New This Sprint

| Action | $/mo | Rationale |
|--------|------|-----------|
| xAI data sharing enrollment | +$0 (earns $150 credits) | Oracle programmatic dispatch unlock. Biggest single leverage. |
| Hetzner VPS (CX22) | +$5 | Miniflux + n8n + sovereign infrastructure |
| syncrescendence.com | +$1.50 | Ontology front door |
| OpenCode (install) | $0 | Kimi daemon harness on mini |
| Gemini CLI (install) | $0 | Cartographer's local instrument |

### Cut

| Service | $/mo saved | Rationale |
|---------|-----------|-----------|
| Perplexity Pro | -$20 | Redundant — Gemini CLI + NotebookLM + Oracle cover same ground. Factory test fail. |
| Setapp | -$0 | Already cancelled (CC65 confirmed) |

### Contingent (test before committing)

| Decision | $/mo | Trigger |
|----------|------|---------|
| Claude Pro Account 3 | +$20 | ONLY if Max rate limit test fails (Ajna OpenClaw + Commander Claude Code concurrent) |

### Deferred (not this sprint)

| Service | $/mo | Revisit When |
|---------|------|-------------|
| Cursor Pro | $20 | If Antigravity + Continue.dev insufficient for HighCommand SwiftUI |
| Windsurf | $15 | Wave 4+, if Antigravity quotas constrain |
| ElevenLabs | $11-22 | After Fish Speech test on mini. Factory test: build voice locally first. |

### Net Budget Impact

| | $/mo |
|---|---|
| Secured (existing) | $210 |
| New committed | +$6.50 |
| Cut | -$20 |
| **Total committed** | **$196.50** |
| Contingent (Account 3) | +$20 |
| xAI credits earned | +$150 |
| **Total with credits** | **$346.50 leverage on $196.50 spend** |

---

## III. Infrastructure Map

### MacBook Air (Sovereign-proximate, interactive)
- Commander: Claude Code (native)
- Ajna: OpenClaw with Claude Sonnet/Haiku (Max setup-token)
- Keyboard Maestro: macro orchestration
- OpenClaw Gateway: runs here initially, may move to mini later

### Mac mini (always-on, persistent)
- Psyche: GPT-5.3-codex via OpenClaw (ChatGPT Plus)
- Adjudicator: Codex CLI (native)
- Cartographer: Gemini CLI (native)
- Kimi daemon: OpenCode + Kimi K2.5 (NVIDIA NIM free)
- Fish Speech: voice AI experiment (Week 3-4)
- tmux constellation: revived session for all persistent processes

### Cloud (sovereign infrastructure)
- Hetzner VPS: Miniflux + n8n (feedcraft pipeline)
- GCP: Cloud Run + Vertex AI embeddings (ontology, when ready)
- Cloudflare: DNS/proxy for syncrescendence.com

---

## IV. The Fortress Dispatch Protocol (Draft — Ajna's Output Format)

Ajna's dispatches compress maximally. Receiving agents expand from repo context.

```
DISPATCH CC65-001
TO: Commander
OBJECTIVE: Scaffold ontology API layer on Hetzner VPS
CONSTRAINTS: Postgres + pg_vector + GraphQL (MVP path per Oracle S1). No Neo4j yet.
SUCCESS: /api/health returns 200 from syncrescendence.com
CONTEXT: Read CANON-ONTOLOGY-GATE_v2.md for schema contract
```

Sonnet produces these natively. Haiku can produce them for routine tasks IF the dispatch template is pre-structured. The fortress for Haiku = rigid template with fill-in-the-blank fields. The fortress for Sonnet = minimal — just the output format spec.

---

## V. 30-Day Execution Sequence

### Week 1 (THIS WEEK — deadline: today for decisions, Friday for artifacts)
- [x] Setapp cancelled
- [x] Oracle strategy review ingested (3 dispatches)
- [x] Tool stack decisions locked (this document)
- [ ] xAI data sharing enrollment
- [ ] Register syncrescendence.com (Cloudflare)
- [ ] Revive OpenClaw on MBA (Max setup-token)
- [ ] Test: Ajna (OpenClaw Sonnet) + Commander (Claude Code) concurrent on Max
- [ ] Deploy Manus on VPS provisioning (Hetzner CX22 + Miniflux + n8n)
- [ ] Install Gemini CLI (`npm install -g @google/gemini-cli`)
- [ ] Cancel Perplexity Pro
- [ ] Claim GCP $10/mo credits

### Week 2
- [ ] Revive Mac mini (tmux constellation session)
- [ ] Install OpenCode on mini, configure Kimi K2.5 daemon
- [ ] Wire Miniflux + n8n pipeline (Manus continues)
- [ ] First Ajna → Commander fortress dispatch (real task)
- [ ] Account 3 decision based on Max rate limit test results

### Week 3
- [ ] Kimi daemon live on mini (repo maintenance)
- [ ] CRUSH nucleosynthesis — let workload reveal agent needs
- [ ] Fish Speech experiment on mini
- [ ] Ajna/Psyche task profile elucidation (from actual dispatches)

### Week 4
- [ ] HighCommand Phase 13 evaluation (Antigravity vs Continue.dev)
- [ ] Monthly retool checkpoint — audit every subscription against factory test
- [ ] Fortress protocol refinement (Sonnet → Haiku buttress if pattern proves)
- [ ] ElevenLabs decision based on Fish Speech results

---

## VI. Open Questions (CRUSH Resolves)

These are NOT decisions to make now. They emerge from doing the work.

1. **Ajna's task profile**: What does strategic dispatch actually look like in practice? How many dispatches per day? What's the token profile? (Answered by Week 2-3 real usage)
2. **Psyche's task profile**: What is "deep technical calibration" concretely? Does GPT-5.3's neediness kill it or does structured dispatch from Ajna tame it? (Answered by mini revival)
3. **Constellation size**: Do we need all 6 core agents or do some merge/split? (Answered by CRUSH revealing the actual workload)
4. **OpenClaw scope**: Which agents route through Gateway vs stay native? (Answered by dispatch pattern observation)
5. **Voice AI**: Fish Speech sufficient or ElevenLabs needed? (Answered by Week 3-4 experiment)

---

## VII. What This Document Is

This is the FINAL tool stack allocation for March 2026. It supersedes:
- CC62-TOOL-STACK-STRATEGY.md
- CC63-TOOL-STACK-STRATEGY.md
- All Oracle recommendations where Commander/Sovereign overrode them

The next strategy document is the **April retool** at month end. Until then: execute, observe, let CRUSH inform.
