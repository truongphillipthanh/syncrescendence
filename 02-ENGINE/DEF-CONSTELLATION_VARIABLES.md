# DEF: Constellation Variables
## Global SN Definitions for Syncrescendence

**Version**: 1.0.0
**Created**: 2026-02-01
**Purpose**: Single source of truth for concepts referenced across 20+ documents. Update here, propagate everywhere via `sn_expand.py`.

---

```
DEF AvatarMap:
    sutra: "Nine-avatar pantheon with platform bindings"
    scope: GLOBAL
    spec:
        value:
            Augur:
                epithet: Inquisitor
                platform: Perplexity
                role: VERIFIER
                summon: "Augur, ascertain..."
                function: "Epistemic scout — chases primary sources until uncertainty collapses"
            Oracle:
                epithet: Recon
                platform: Grok
                role: RECON
                summon: "Oracle, understand the implications of..."
                function: "Cultural divination — X firehose, meme velocity, prediction-market priors"
            Vizier:
                epithet: Hermeneut
                platform: Claude Web
                role: INTERPRETER
                summon: "Vizier, elucidate..."
                function: "Court advisor — interprets vague directives with profound charity"
            Vanguard:
                epithet: Architect
                platform: ChatGPT Web
                role: COMPILER
                summon: "Vanguard, formulate..."
                function: "Frontline strategist — cold logic, long contingencies, zero warmth"
            Diviner:
                epithet: Exegete
                platform: Gemini Web
                role: DIGESTOR
                summon: "Diviner, elaborate on..."
                function: "Multimodal clarifier — takes tangled inputs and renders them lucid"
            Commander:
                epithet: Viceroy
                platform: Claude Code (Opus)
                role: EXECUTOR_LEAD
                summon: "Commander, pivot to..."
                function: "Operational commander — turns intent into disciplined execution"
            Adjudicator:
                epithet: Executor
                platform: Codex CLI
                role: PARALLEL_EXEC
                summon: "Adjudicator, execute..."
                function: "Rule-bound fabricator — hammers runnable code, debugs iteratively"
            Ajna:
                epithet: null
                platform: OpenClaw Opus 4.5 (M1 Mini)
                role: LOCAL_ORCH
                summon: "Ajna, illuminate..."
                function: "Third-eye insight — sees the path, commands tools, minimal distortion"
            Psyche:
                epithet: null
                platform: OpenClaw GPT-5.2 (M4 MBA)
                role: LOCAL_ORCH
                summon: "Psyche, holistically calibrate..."
                function: "Animating consciousness — synthesizes domains, anticipates branches"
    gloss:
        Definitive pantheon (v3). The council forms a closed loop:
        Augur gathers >> Oracle senses >> Vizier interprets >> Vanguard architects >>
        Diviner clarifies >> Commander directs >> Adjudicator fabricates >>
        Ajna and Psyche provide the agentic apex.
end

DEF AccountMap:
    sutra: "Three accounts binding platforms to authentication"
    scope: GLOBAL
    spec:
        value:
            Account1:
                email: truongphillipthanh@icloud.com
                auth: Apple
                purpose: "Sovereign substrate, owns origin"
                platforms: [ChatGPT, Grok]
            Account2:
                email: icloud.truongphillipthanh@gmail.com
                auth: Google
                purpose: "Parallel execution capacity"
                platforms: [Codex CLI, "Claude Code Sonnet x2"]
            Account3:
                email: truongphillipthanh@gmail.com
                auth: Google
                purpose: "Primary interface, ecosystem access"
                platforms: [Claude Web, Claude Code Opus, Gemini Web, Gemini CLI]
    gloss:
        Three accounts with independent auth prevent single-point-of-failure lockout.
        Platform-to-account bindings determined by capability requirements.
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
        value: 100
        unit: USD/month
        breakdown:
            claude: {accounts: 3, tier: pro, cost: 60}
            gemini: {accounts: 1, tier: advanced, cost: 20}
            chatgpt: {accounts: 1, tier: plus, cost: 20}
    gloss:
        Hard budget constraint. Platform selection prioritizes capability per dollar.
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
