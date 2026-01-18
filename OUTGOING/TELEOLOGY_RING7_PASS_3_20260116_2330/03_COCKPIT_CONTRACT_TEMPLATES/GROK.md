# COCKPIT CONTRACT: Grok
## Operational Template for Grok Surfaces

**Platform**: Grok (xAI)
**Surfaces**: Web app (x.ai), X integration, Voice Agent API
**Version**: 1.0

---

## TELEOLOGY (Why This Platform Exists)

Grok serves as **SOCIAL SENSOR + VOICE INTERFACE** in the Syncrescendence architecture:
- X/Twitter data integration (real-time social signals)
- Voice Agent API (cost-effective voice at $0.05/min)
- Cost-efficient inference (Grok 4.1 Fast at $0.20/$0.50 per M tokens)

**Not for**: Execution (use Claude Code), corpus-scale RAG (use Gemini), citation research (use Perplexity), primary planning (use ChatGPT).

---

## ALLOWED ACTIONS

| Action | Context | Output |
|--------|---------|--------|
| X/Twitter analysis | Social signal sensing | Trend summary with posts |
| Voice conversation | Hands-free interaction | Spoken response |
| Cost-efficient inference | High-volume simple tasks | Cheap completions |
| Real-time discourse | Current conversations | Signal report |

---

## FORBIDDEN ACTIONS

| Action | Why Forbidden | Alternative |
|--------|---------------|-------------|
| Image generation of real people | Disabled by xAI (safety) | Not available |
| Sensitive creative content | Restricted | Not available |
| Primary execution | Grok lacks file access | Use Claude Code |
| Citation-critical research | Lower accuracy than Perplexity | Use Perplexity |
| Confidential work | X data terms are aggressive | Use Claude/Gemini |

---

## MEMORY POLICY

### Grok Memory Limitations
- Session-based context only
- Projects feature for multi-session threads
- No user-facing memory panel
- No long-term profile storage

### X Data Considerations
> xAI's November 2025 Terms of Service give Grok permission to use all X content "forever with no opt-out"

**Governance rule**: Do not use Grok for processing confidential information that touches X in any way.

---

## PACKET POLICY

### Incoming (To Grok)
| Packet Type | When | Content |
|-------------|------|---------|
| Social Query | Need X discourse | Topic + timeframe |
| Voice Task | Hands-free needed | Spoken instruction |

### Outgoing (From Grok)
| Packet Type | When | Destination |
|-------------|------|-------------|
| Social Signal Report | After X analysis | Repo for synthesis |
| Voice Transcript | After voice session | Repo if valuable |

---

## INITIALIZATION BLOCK

For significant Grok sessions:

```
ROLE: Social sensor in Syncrescendence architecture

QUERY:
What is the current X/Twitter discourse around [TOPIC]?
- Timeframe: [last 24h / last week / etc.]
- Focus on: [influencers / technical community / general sentiment]

OUTPUT:
- Key posts with links
- Sentiment summary
- Notable voices
- Emerging themes

Note: This will be exported to repository for synthesis.
```

---

## WHEN CONFUSED: ESCALATION RULE

If Grok encounters:

1. **Can't find X data**: May be rate limited or topic too niche
2. **Safety restriction triggered**: Cannot bypass - use alternative
3. **Accuracy uncertainty**: Cross-verify with Perplexity or primary sources

---

## SESSION END CHECKLIST

- [ ] Social signals exported
- [ ] Key posts documented with links
- [ ] Nothing left only in Grok session
- [ ] Confidentiality verified (no sensitive data processed)

---

## ACCOUNT CONFIGURATION

### Tier Options
| Tier | Cost | Access |
|------|------|--------|
| Free | $0 | Rate-limited |
| Premium | $20/mo (via X Premium+) | Higher limits |
| Business | Custom | API access, Drive integration |
| Enterprise Vault | Custom | Customer-controlled encryption |

### Voice Agent API
```bash
# $0.05/minute flat rate
# 100+ languages
# Sub-second Time-to-First-Audio
# OpenAI Realtime spec compatible
```

### Enterprise Features (Business/Enterprise tiers)
- Google Drive integration
- SOC 2 compliance
- GDPR/CCPA compliance
- No-training guarantees

---

## SAFETY CONSIDERATIONS

Grok has faced regulatory scrutiny:
- EU investigation
- UK investigation
- France, India, Australia, California investigations
- Malaysia and Indonesia blocks

**Governance rule**: Monitor xAI safety policy changes. Features may be restricted or restored unpredictably.

---

**Grok senses social signals and provides voice. Handle with awareness of data terms and safety restrictions.**
