# DEF: Constellation Variables
## Global SN Definitions for Syncrescendence

**Version**: 2.0.0
**Created**: 2026-02-01
**Purpose**: Single source of truth for concepts referenced across 20+ documents. Update here, propagate everywhere via `sn_expand.py`.

---

```
DEF AvatarMap:
    sutra: "Ten-avatar pantheon with platform bindings (Gemini bifurcated)"
    scope: GLOBAL
    spec:
        value:
            Augur:
                epithet: Inquisitor
                platform: Perplexity
                role: VERIFIER
                account: null
                summon: "Augur, ascertain..."
                function: "Epistemic scout — chases primary sources until uncertainty collapses"
            Oracle:
                epithet: Recon
                platform: Grok
                role: RECON
                account: 1
                summon: "Oracle, understand the implications of..."
                function: "Cultural divination — X firehose, meme velocity, prediction-market priors"
            Vizier:
                epithet: Hermeneut
                platform: Claude Web
                role: INTERPRETER
                account: 2
                summon: "Vizier, elucidate..."
                function: "Court advisor — interprets vague directives with profound charity"
            Vanguard:
                epithet: Architect
                platform: ChatGPT Web
                role: COMPILER
                account: 1
                summon: "Vanguard, formulate..."
                function: "Frontline strategist — cold logic, long contingencies, zero warmth"
            Diviner:
                epithet: Illuminator
                platform: Gemini Web
                role: DIGESTOR
                account: 2
                summon: "Diviner, elaborate on..."
                function: "Multimodal clarifier — sheds light on tangled inputs, renders them lucid"
            Cartographer:
                epithet: Exegete
                platform: Gemini CLI
                role: SENSOR
                account: 2
                summon: "Cartographer, survey..."
                function: "Corpus cartographer — maps the territory with scholarly precision, 1M+ context"
            Commander:
                epithet: Viceroy
                platform: Claude Code (Opus)
                role: EXECUTOR_LEAD
                account: 1
                summon: "Commander, pivot to..."
                function: "Operational commander — turns intent into disciplined execution"
            Adjudicator:
                epithet: Executor
                platform: Codex CLI
                role: PARALLEL_EXEC
                account: 2
                summon: "Adjudicator, execute..."
                function: "Rule-bound fabricator — hammers runnable code, debugs iteratively"
            Ajna:
                epithet: null
                platform: OpenClaw Opus 4.5 (M1 Mini)
                role: LOCAL_ORCH
                account: null
                summon: "Ajna, illuminate..."
                function: "Third-eye insight — sees the path, commands tools, minimal distortion"
            Psyche:
                epithet: null
                platform: OpenClaw GPT-5.2 (M4 MBA)
                role: LOCAL_ORCH
                account: null
                summon: "Psyche, holistically calibrate..."
                function: "Animating consciousness — synthesizes domains, anticipates branches"
    gloss:
        Definitive pantheon (v3, bifurcated). The council forms a closed loop:
        Augur gathers >> Oracle senses >> Vizier interprets >> Vanguard architects >>
        Diviner illuminates >> Cartographer maps >> Commander directs >>
        Adjudicator fabricates >> Ajna and Psyche provide the agentic apex.
end

DEF AccountMap:
    sutra: "Three accounts with tiered subscriptions binding platforms to authentication"
    scope: GLOBAL
    spec:
        value:
            Account1:
                email: truongphillipthanh@icloud.com
                auth: Apple
                purpose: "Sovereign substrate, primary execution"
                tiers: [Claude Max, ChatGPT Plus]
                monthly: 120
                platforms: [Claude Code Opus, ChatGPT Web, Grok]
                avatars: [Commander, Vanguard, Oracle]
            Account2:
                email: icloud.truongphillipthanh@gmail.com
                auth: Google
                purpose: "Parallel execution + corpus sensing"
                tiers: [Claude Pro, Google AI Pro]
                monthly: 40
                platforms: [Claude Web, Codex CLI, "Claude Code Sonnet x2", Gemini Web, Gemini CLI]
                avatars: [Vizier, Adjudicator, Diviner, Cartographer]
            Account3:
                email: truongphillipthanh@gmail.com
                auth: Google
                purpose: "Free tier access"
                tiers: [Unpaid]
                monthly: 0
                platforms: []
                avatars: []
    gloss:
        Three accounts with independent auth prevent single-point-of-failure lockout.
        Account 1 (Claude Max) provides 5x usage for primary execution via Commander.
        Account 2 pools Claude Pro + Google AI Pro for parallel + sensing capacity.
        Account 3 reserved for future expansion or free-tier experimentation.
end

DEF ChainNames:
    sutra: "Six developmental chains in canonical order"
    scope: GLOBAL
    spec:
        value:
            - {name: Intelligence, symbol: I, virtue: null, element: Technology, canon: 30000}
            - {name: Information, symbol: ℹ, virtue: "α (Acumen)", element: Air, canon: 31000}
            - {name: Insight, symbol: ∴, virtue: "χ (Coherence)", element: Water, canon: 32000}
            - {name: Expertise, symbol: E, virtue: "ε (Efficacy)", element: Fire, canon: 33000}
            - {name: Knowledge, symbol: K, virtue: "μ (Mastery)", element: Earth, canon: 34000}
            - {name: Wisdom, symbol: W, virtue: "τ (Transcendence)", element: Quintessence, canon: 35000}
    gloss:
        Foundational taxonomy referenced in ~40 CANON documents.
        Intelligence is dual-nature: substrate AND developmental trajectory.
        Wisdom develops LAST (emerges from other chains).
end

DEF PalaceLayers:
    sutra: "Seven-layer cognitive palace operating simultaneously"
    scope: GLOBAL
    spec:
        value:
            - {layer: 0, name: Reality, domain: Ontological Bedrock}
            - {layer: 1, name: Imaginality, domain: Teleological Attraction}
            - {layer: 2, name: Potentiality, domain: Resource Substrate}
            - {layer: 3, name: Temporality, domain: Rhythmic Harmonics}
            - {layer: 4, name: Practicality, domain: Operational Methods}
            - {layer: 5, name: Actuality, domain: Present Nexus}
            - {layer: 6, name: Consequentiality, domain: Wisdom Accumulation}
            - {layer: 7, name: "Strategic Harmony", domain: Meta-Orchestration}
    gloss:
        Not sequential stages but concurrent dimensions operating simultaneously.
        Layer 5 (Actuality) is the convergence point — only actuality provides evidence.
end

DEF SevenPulses:
    sutra: "Daily 2-minute state vector assessment"
    scope: GLOBAL
    spec:
        value:
            - {pulse: 1, name: Foundation, measures: "values grounding"}
            - {pulse: 2, name: Energy, measures: "capacity level"}
            - {pulse: 3, name: Direction, measures: "path clarity"}
            - {pulse: 4, name: Connection, measures: "relationship health"}
            - {pulse: 5, name: Progress, measures: "advancement sense"}
            - {pulse: 6, name: Integration, measures: "coherence quality"}
            - {pulse: 7, name: Transcendence, measures: "purpose engagement"}
    gloss:
        Minimal viable measurement protocol.
        Referenced in CANON-10000 (Core), CANON-00010 (Operations), CANON-20000 (Palace).
end

DEF EnergyStates:
    sutra: "Four energy levels governing protocol adaptation"
    scope: GLOBAL
    spec:
        value:
            - {state: Peak, action: "Full capacity protocols"}
            - {state: Baseline, action: "Standard protocols"}
            - {state: Depletion, action: "Maintenance only"}
            - {state: Crisis, action: "Suspend development, preserve stability"}
    gloss:
        Energy-aware practice prevents burnout and respects neurodivergent reality.
        All operational protocols adapt to current energy state.
end

DEF ModalSequence:
    sutra: "Technology-gated strategic progression across decades"
    scope: GLOBAL
    spec:
        value:
            - {modal: 1, name: Abstraction, period: "2024-2027", focus: "Text-based intelligence"}
            - {modal: 2, name: Simulation, period: "2027-2030", focus: "Visual/geometric intelligence"}
            - {modal: 3, name: Embodiment, period: "2031-2036", focus: "Physical construction, robotics"}
            - {modal: 4, name: Transcendence, period: "2037+", focus: "Distributed intelligence, Field Nodes"}
    gloss:
        Cannot skip modals — each enables the next.
        Currently in Modal 1 (Abstraction). Respect technology maturity windows.
end

DEF PlatformBudget:
    sutra: "Monthly constellation cost ceiling"
    scope: GLOBAL
    spec:
        value: 160
        unit: USD/month
        breakdown:
            claude_max: {account: 1, tier: max, cost: 100}
            chatgpt_plus: {account: 1, tier: plus, cost: 20}
            claude_pro: {account: 2, tier: pro, cost: 20}
            google_ai_pro: {account: 2, tier: pro, cost: 20}
    gloss:
        Budget increased from $100 to $160 with Claude Max tier adoption.
        Claude Max (5x capacity) justifies premium for primary execution pipeline.
        Sustainability target: self-funding by 2026-06.
end

DEF DirectoryStructure:
    sutra: "Five numbered dirs + three sanctioned exceptions"
    scope: GLOBAL
    spec:
        value:
            numbered:
                - {id: "00", name: ORCHESTRATION, purpose: "Strategic coordination"}
                - {id: "01", name: CANON, purpose: "Verified canonical knowledge (PROTECTED)"}
                - {id: "02", name: ENGINE, purpose: "Functions, prompts, avatars, model profiles"}
                - {id: "04", name: SOURCES, purpose: "Source documents"}
                - {id: "05", name: SIGMA, purpose: "Operational knowledge corpus"}
            sanctioned:
                - {name: "-INBOX", purpose: "Incoming from external platforms"}
                - {name: "-OUTGOING", purpose: "Export staging, cross-platform handoffs"}
                - {name: "-SOVEREIGN", purpose: "Sovereign-only workspace"}
    gloss:
        Gap at 03 is intentional (03-QUEUE absorbed into 02-ENGINE).
        FLAT PRINCIPLE: no subdirectories except sanctioned locations.
end
```

---

## Usage

Reference any DEF value in other SN blocks:
```
PROC Example:
    spec:
        avatar: ${AvatarMap.Commander.platform}  # resolves to "Claude Code (Opus)"
        chains: ${ChainNames}                     # resolves to full list
end
```

Update workflow:
1. Edit the DEF value in this file
2. Run `sn_expand.py` to resolve references in all SN-encoded documents
3. Commit the changes

---

## Cross-References

- Block template spec: `00-ORCHESTRATION/scripts/SN_BLOCK_TEMPLATES.md`
- Symbol glossary: `00-ORCHESTRATION/scripts/sn_symbols.yaml`
- CANON lean-out recommendations: `00-ORCHESTRATION/state/REF-CANON_LEAN_OUT_RECOMMENDATIONS.md`
