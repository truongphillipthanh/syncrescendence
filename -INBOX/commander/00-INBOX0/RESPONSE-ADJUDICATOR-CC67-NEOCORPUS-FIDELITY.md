# Neocorpus Fidelity Verification — CC65 OpenClaw Entries

Verification target: commit `26af2d07`  
Verification method: all 10 neocorpus entries and all 31 cited corpus files were read directly from `git show 26af2d07:<path>` to avoid drift from the current checkout.

---

## 1. `openclaw-memory-architecture.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-memory-architecture.md` | 5/5 | FLAGGED — unsupported config schemas and unsupported setup/coordination machinery were added | FLAGGED — the actual `items.json` / `summary.md` knowledge-graph implementation and the S3 restore path were lost | FLAGGED |

### Fabrication evidence

- Invented `memoryFlush` schema and mechanics.
  - Entry: `memoryFlush` is presented as:
    > `"threshold": 0.8, "targets": ["MEMORY.md", "daily_log"]`
  - Source `corpus/openclaw/10964.md` actually gives:
    > `"compaction": { "memoryFlush": { "enabled": true, "softThresholdTokens": 40000, "prompt": "...", "systemPrompt": "..." } }`
  - The entry preserves the idea but fabricates the config shape, keys, and threshold mechanism.

- Invented `contextPruning` schema.
  - Entry:
    > `"contextPruning": { "enabled": true, "ttlDays": 30, "archiveTarget": "daily_log" }`
  - Source `corpus/openclaw/10964.md`:
    > `"contextPruning": { "mode": "cache-ttl", "ttl": "6h", "keepLastAssistants": 3 }`
  - `ttlDays` and `archiveTarget` are not in the cited source set.

- Unsupported setup-generation claim.
  - Entry:
    > `The source of truth from which other configs are generated (via make configs or equivalent). Never edit generated files directly`
  - Source `corpus/openclaw/00179.md` says:
    > `Create these files in the workspace root`
  - No source mentions generated configs, `make configs`, or generated-file discipline.

- Unsupported multi-agent coordination specifics.
  - Entry adds:
    > `Pattern 1: Designated writer`  
    > `Pattern 2: Inbox/outbox handoff`  
    > `Pattern 3: Event log merge`
  - None of `00051`, `00057`, `10904`, `10964`, or `00179` specify these named coordination patterns.

### Content loss evidence

- The source implementation uses entity folders with `summary.md` and `items.json`; the entry rewrites that into a different one-fact-per-file model.
  - Source `corpus/openclaw/00057.md`:
    > `/life/areas/people/sarah/summary.md`  
    > `/life/areas/people/sarah/items.json`
  - Source `corpus/openclaw/00057.md` also specifies:
    > `Save facts immediately to items.json`  
    > `Weekly: rewrite summary.md from active facts`
  - Entry instead says:
    > `Atomic fact files: One fact per file`
  - That is both a fabrication and a loss of the source’s concrete implementation.

- The reboot-survival path from `10904` is omitted.
  - Source `corpus/openclaw/10904.md`:
    > `For surviving reboots we sync memory/ to S3 every 5 min. On restart, files restore → vector index rebuilds automatically.`
  - The entry does not carry forward this backup-and-rebuild mechanism.

---

## 2. `openclaw-honcho-memory-integration.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-honcho-memory-integration.md` | 2/2 | FLAGGED — the entry adds unsourced Syncrescendence/QMD/Mem0 positioning and claims beyond the corpus | FLAGGED — it drops the automatic migration claim, which is a core product behavior in both sources | FLAGGED |

### Fabrication evidence

- Unsourced CRUSH / Syncrescendence machinery.
  - Entry:
    > `CRUSH does the same across the corpus. Both are lossless in intent, lossy in practice.`
  - Neither `corpus/openclaw/00122.md` nor `corpus/openclaw/08837.md` mentions CRUSH.

- Unsourced comparative stack table.
  - Entry:
    > `QMD local | File-based, no inference, full autonomy`  
    > `Mem0 | Vector retrieval, no reasoning step`
  - The cited Honcho sources discuss Honcho only. QMD, Mem0, and native-context comparisons do not appear in either source.

- Unsourced superlative claim.
  - Entry:
    > `Honcho is the most cognitively ambitious option currently available as an OpenClaw plugin.`
  - The cited sources do not compare Honcho against the full plugin ecosystem.

### Content loss evidence

- The auto-migration behavior is omitted.
  - Source `corpus/openclaw/00122.md`:
    > `Already have context in your OpenClaw's memory files? The installer automatically migrates everything into Honcho. No extra steps.`
  - Source `corpus/openclaw/08837.md` repeats the same point:
    > `The installer automatically migrates everything into Honcho. No extra steps.`
  - The neocorpus entry never carries this forward, despite it being one of the most concrete integration details in the source set.

---

## 3. `openclaw-soul-and-identity-design.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-soul-and-identity-design.md` | 2/2 | FLAGGED — one major architectural claim is overstated as a research finding when the source presents it as a personal rebuild outcome | FLAGGED — the explicit self-improvement-loop takeaway is omitted | FLAGGED |

### Fabrication evidence

- The 17→4 architecture is overstated as a research finding.
  - Entry:
    > `tolibear_'s research found that large multi-agent systems with many top-level identities underperform systems organized as a small core with a specialist library.`
  - Source `corpus/openclaw/10971.md` frames this as the author’s own operational conclusion:
    > `That was the realization that forced the rebuild.`  
    > `The path to autonomy isn't more agents. It's fewer, sharper agents who spawn what they need.`  
    > `I consolidated everything down to four core roles:`
  - The source does not present that specific specialist-library architecture as a formal research finding.

### Content loss evidence

- The source’s explicit self-improvement-loop takeaway is missing.
  - Source `corpus/openclaw/10971.md`:
    > `7. An agent without a self-improvement loop is frozen on day one. The soul is a living document. Build a feedback mechanism or your agents will never grow.`
  - The entry covers calibration, anti-patterns, and consolidation, but it never preserves this named takeaway as a first-class principle.

---

## 4. `openclaw-phone-voice-integration.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-phone-voice-integration.md` | 2/2 | CLEAN | CLEAN | FAITHFUL |

The entry preserves the inbound setup, outbound skill flow, `x-openclaw-session-key` continuity mechanism, and cron-driven autonomous calling without introducing unsupported config or pricing details.

---

## 5. `openclaw-multi-agent-fleet-operations.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-multi-agent-fleet-operations.md` | 2/2 | CLEAN | CLEAN | FAITHFUL |

The entry faithfully carries forward the 3-agent and 6-agent patterns, the SOUL/MEMORY/filesystem coordination model, cron ordering, heartbeat self-healing, Telegram operations, and the staged rollout advice.

---

## 6. `openclaw-agent-management-dashboards.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-agent-management-dashboards.md` | 2/2 | FLAGGED — it attributes VidClaw’s localhost/SSH access model to Mission Control without source support | CLEAN | FLAGGED |

### Fabrication evidence

- The entry generalizes VidClaw’s security model to both systems.
  - Entry:
    > `Both Mission Control and VidClaw converge on the same access model: localhost-only, SSH tunnel for remote`
  - Source `corpus/openclaw/10900.md` supports this for VidClaw:
    > `VidClaw binds exclusively to localhost. It never touches the internet. Remote access is via SSH tunnel`
  - Source `corpus/openclaw/00167.md` does not support the same claim for Mission Control. What it actually says is:
    > `Jarvis created Mission Control, a SaaS that's built for one person: Bhanu.`
  - No cited Mission Control source mentions localhost-only binding or SSH tunneling.

---

## 7. `openclaw-communication-channels.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-communication-channels.md` | 3/3 | CLEAN | CLEAN | FAITHFUL |

The entry stays inside the source set: Slack for operator/business workflows, Discord for per-agent/per-project channel structure and thread-based context, and iMessage/imsg v0.5.0 with typing indicators, reactions, and events.

---

## 8. `openclaw-security-hardening.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-security-hardening.md` | 5/5 | CLEAN | CLEAN | FAITHFUL |

The entry faithfully combines the five source threads: top-10 vulnerability list, UTM isolation, 1Password and email protocols, Tailscale + Matrix hardening, Cloudflare Tunnel + Access + SSH hardening, prompt-injection defenses, and the SHIELD.md policy structure.

---

## 9. `openclaw-cost-optimization.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-cost-optimization.md` | 5/5 | CLEAN | CLEAN | FAITHFUL |

The entry preserves the script-first cost thesis, the tiered routing framework, the routing skill/OpenRouter/ClawRouter material, prompt caching, Ollama/local-model economics, the `$127` post-mortem, and the MiniMax M2.5 case study without introducing unsupported config fragments.

---

## 10. `openclaw-threat-model-attack-surface.md`

| Entry | Sources Read | Fabrication Check | Content Loss Check | Verdict |
|---|---:|---|---|---|
| `openclaw-threat-model-attack-surface.md` | 3/3 | CLEAN | CLEAN | FAITHFUL |

The entry faithfully preserves the reconnaissance model, the 10-vector taxonomy, the reverse-proxy bypass/root-access case study, the credential and perception-manipulation consequences, and the consumer-gap framing.

---

## Summary Table

| # | Entry | Sources | Fabrication | Loss | Verdict |
|---:|---|---:|---|---|---|
| 1 | `openclaw-memory-architecture.md` | 5/5 | 4 issues | 2 issues | FLAGGED |
| 2 | `openclaw-honcho-memory-integration.md` | 2/2 | 3 issues | 1 issue | FLAGGED |
| 3 | `openclaw-soul-and-identity-design.md` | 2/2 | 1 issue | 1 issue | FLAGGED |
| 4 | `openclaw-phone-voice-integration.md` | 2/2 | CLEAN | CLEAN | FAITHFUL |
| 5 | `openclaw-multi-agent-fleet-operations.md` | 2/2 | CLEAN | CLEAN | FAITHFUL |
| 6 | `openclaw-agent-management-dashboards.md` | 2/2 | 1 issue | CLEAN | FLAGGED |
| 7 | `openclaw-communication-channels.md` | 3/3 | CLEAN | CLEAN | FAITHFUL |
| 8 | `openclaw-security-hardening.md` | 5/5 | CLEAN | CLEAN | FAITHFUL |
| 9 | `openclaw-cost-optimization.md` | 5/5 | CLEAN | CLEAN | FAITHFUL |
| 10 | `openclaw-threat-model-attack-surface.md` | 3/3 | CLEAN | CLEAN | FAITHFUL |

---

## Overall Assessment

- Total entries verified: 10/10
- Faithful: 6
- Flagged: 4
- Overall fidelity score: 60%

### Specific remediation needed

1. Rewrite `openclaw-memory-architecture.md` against the actual source configs and structures.
   - Remove invented JSON schemas.
   - Restore the actual `items.json` / `summary.md` three-layer implementation.
   - Restore the `10904` S3 sync / rebuild detail.

2. Rewrite `openclaw-honcho-memory-integration.md` to stay inside the Honcho corpus.
   - Remove unsourced CRUSH/QMD/Mem0/native-context comparisons.
   - Restore the automatic migration behavior.

3. Patch `openclaw-soul-and-identity-design.md`.
   - Reword the 17→4 claim as an operational conclusion from the source, not a formal research finding.
   - Add the explicit self-improvement-loop principle from the source takeaway section.

4. Patch `openclaw-agent-management-dashboards.md`.
   - Remove or source the claim that Mission Control used the same localhost-only / SSH-tunnel access model as VidClaw.

