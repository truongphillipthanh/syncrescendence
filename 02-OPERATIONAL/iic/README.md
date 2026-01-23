# Information Integration Constellation (IIC) Configs

**Version**: 1.0.0
**Updated**: 2026-01-23

---

## Purpose

IIC configurations define how content flows through the six virtue pathways (α, χ, ε, μ, τ).

---

## Configs

| Config | Virtue | Symbol | Focus |
|--------|--------|--------|-------|
| IIC-Acumen-config.md | Acumen | α | Feed curation, content triage |
| IIC-Coherence-config.md | Coherence | χ | Integration, consistency |
| IIC-Efficacy-config.md | Efficacy | ε | Execution, productivity |
| IIC-Mastery-config.md | Mastery | μ | Skill development, expertise |
| IIC-Transcendence-config.md | Transcendence | τ | Wisdom, synthesis |

---

## Shared Protocols

- **IIC-shared-protocols.md** — Common patterns across all IICs

---

## Usage (SN Notation)

```
PROC IICProcessing(content) -> integrated:
    sutra: "Feed >> Integrate >> Execute >> Deepen >> Synthesize"
    spec:
        steps:
            1. content >> triage(IIC-Acumen) >> {keep, discard}
            2. keep >> integrate(IIC-Coherence) >> consistent
            3. consistent >> execute(IIC-Efficacy) >> actionable
            4. actionable >> deepen(IIC-Mastery) >> expertise
            5. expertise >> synthesize(IIC-Transcendence) >> wisdom
        produces: integrated
end
```

---

## Relationship to Chains

IIC virtues map to developmental chains:

| Virtue | Primary Chain | Secondary |
|--------|---------------|-----------|
| α (Acumen) | ℹ Information | I Intelligence |
| χ (Coherence) | ∴ Insight | I Intelligence |
| ε (Efficacy) | E Expertise | K Knowledge |
| μ (Mastery) | E Expertise | W Wisdom |
| τ (Transcendence) | W Wisdom | All chains |

---

**Status**: IIC configuration directory (reorganized 2026-01-23).
