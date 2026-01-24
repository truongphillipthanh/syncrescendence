---
id: [[CANON-30440-SAFETY_ALIGNMENT-asteroid-INTELLIGENCE]]
name: Safety and Alignment
identity: SAFETY_ALIGNMENT
tier: CANON
type: asteroid
chain: INTELLIGENCE
parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
version: 2.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Agent security, attack vectors, defense-in-depth, governance frameworks, and alignment principles.
---

# CANON-30440-SAFETY_ALIGNMENT-asteroid-INTELLIGENCE (SN Format)

**Note**: This is a Semantic Notation compressed version.
**Original**: 1,780 words, 14,791 characters

---

TERM IntelligenceChainAsteroid:
    sutra: "Parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)  ---"
    gloss:
        **Parent**: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)

---
end


TERM PURPOSE:
    sutra: "This asteroid provides detailed specifications for agent safety, security, and alignment"
    gloss:
        This asteroid provides detailed specifications for agent safety, security, and alignment. Where [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] surveys the threat landscape, this document provides implementation depth for defenses, governance frameworks, and alignment mechanisms.

---
end


TERM 11FundamentalThreatModel:
    sutra: "Agent systems face fundamentally different threat models than static models"
    gloss:
        Agent systems face fundamentally different threat models than static models. The combination of autonomy, tool access, and persistent state creates attack surfaces absent in traditional AI.
end


TERM 12AttackVectorTaxonomy:
    sutra: "``yaml Attack_Vectors:   Agent_Hijacking:     mechanism: Indirect prompt injection via ingested d..."
    gloss:
        ```yaml
Attack_Vectors:
  Agent_Hijacking:
    mechanism: Indirect prompt injection via ingested data
    success_rate: 81% with optimization
    vectors:
      - Malicious content in emails
      - Poisoned documents
      - Compromised web pages
      - Injected database records
    root_cause: No...
end


TERM 13KeyResearchFindings:
    sutra: "| Finding | Source | Implication | |---------|--------|-------------| | 51-72% unsafe behavior ra..."
    gloss:
        | Finding | Source | Implication |
|---------|--------|-------------|
| 51-72% unsafe behavior rates | OpenAgentSafety | Current systems unacceptable for high-stakes |
| 81% attack success with optimization | NIST US AI Safety | Novel attacks generalize across environments |
| CVE-2025-32711 CVSS 9....
end


TERM 14OWASPAgenticAIThreats:
    sutra: "``yaml OWASP_Taxonomy:   - Prompt injection   - Tool misuse   - Intent breaking and goal manipula..."
    gloss:
        ```yaml
OWASP_Taxonomy:
  - Prompt injection
  - Tool misuse
  - Intent breaking and goal manipulation
  - Identity spoofing
  - Unexpected RCE
  - Agent communication poisoning
  - Resource overload
```

---
end


NORM 21FiveLayerDefenseArchitecture:
    sutra: "``yaml Layer_1_Prompt_Hardening:   purpose: First line of defense   techniques:     - Strict beha..."
    gloss:
        ```yaml
Layer_1_Prompt_Hardening:
  purpose: First line of defense
  techniques:
    - Strict behavioral constraints
    - Explicit prohibitions
    - Narrow responsibility definitions
    - Out-of-scope rejection instructions
    - Clear role boundaries

  example: |
    You are a customer service...
end


TERM 22DefenseEffectiveness:
    sutra: "| Defense | Success Rate | Limitations | |---------|--------------|-------------| | Reverse Turin..."
    gloss:
        | Defense | Success Rate | Limitations |
|---------|--------------|-------------|
| Reverse Turing Test | 87-94% | Sophisticated attacks may pass |
| Multi-agent alignment detection | 70-98% | Varies by faking sophistication |
| GCG jailbreak defenses | 90.8% | New techniques bypass |
| Defense-in-d...
end


TERM 31CorePrinciples:
    sutra: "| Principle | Implementation | |-----------|----------------| | Well-defined human controllers | ..."
    gloss:
        | Principle | Implementation |
|-----------|----------------|
| **Well-defined human controllers** | Clear ownership and accountability |
| **Carefully limited powers** | Scope restrictions on capabilities |
| **Observable actions and planning** | Full visibility into decision-making |
| **Environme...
end


TERM 32AgentRiskMap:
    sutra: "``yaml SAIF_Risk_Map:   purpose: Full-stack threat visualization    dimensions:     - Attack surf..."
    gloss:
        ```yaml
SAIF_Risk_Map:
  purpose: Full-stack threat visualization

  dimensions:
    - Attack surface by layer
    - Capability exposure
    - Data access scope
    - User impact potential
    - Recovery difficulty

  application:
    - Prioritize defensive investment
    - Guide architecture decisi...
end


TERM 41EUAIActRequirements:
    sutra: "``yaml EU_AI_Act:   pillars:     - Risk assessment     - Transparency tools     - Technical deplo..."
    gloss:
        ```yaml
EU_AI_Act:
  pillars:
    - Risk assessment
    - Transparency tools
    - Technical deployment controls
    - Human oversight design

  obligations:
    GPAISR_providers: 10 measures
    Agent_providers: Specific requirements
    Deployers: Ongoing compliance

  high_risk_requirements:...
end


TERM 42KPMGTACOFramework:
    sutra: "``yaml TACO_Framework:   agent_categories:     Taskers: Single-task automation     Automators: Wo..."
    gloss:
        ```yaml
TACO_Framework:
  agent_categories:
    Taskers: Single-task automation
    Automators: Workflow automation
    Collaborators: Human-AI partnership
    Orchestrators: Multi-agent coordination

  trusted_AI_principles:
    - Reliability
    - Accountability
    - Transparency
    - Security...
end


TERM 43EightEssentialGovernancePractices:
    sutra: "``yaml Governance_Practices:   1_Permissions_Boundaries:     - Specify accessible data     - Defi..."
    gloss:
        ```yaml
Governance_Practices:
  1_Permissions_Boundaries:
    - Specify accessible data
    - Define allowable actions
    - Establish escalation triggers
    - Machine-readable policies

  2_Privacy_by_Design:
    - Data minimization
    - Purpose limitation
    - Encryption
    - Anonymization...
end


TEST 51MultiLayerValidation:
    sutra: "``yaml Validation_Layers:   Verification_Agent:     - Review outcomes before execution     - Cros..."
    gloss:
        ```yaml
Validation_Layers:
  Verification_Agent:
    - Review outcomes before execution
    - Cross-check against policies
    - Flag anomalies

  Testing_Protocols:
    - Simulate decisions before execution
    - Sandbox high-stakes actions
    - Double-check with second agent

  Alignment_Checks:...
end


TERM 52ErrorRecoveryStrategies:
    sutra: "``yaml Error_Recovery:   tool_failure:     - Catch and retry with alternatives     - Request new ..."
    gloss:
        ```yaml
Error_Recovery:
  tool_failure:
    - Catch and retry with alternatives
    - Request new instructions if stuck
    - Graceful degradation

  plan_failure:
    - Escalate to human
    - Checkpoint and rollback
    - Alternative approach selection

  chain_failure:
    - Monitor action sequen...
end


TEST 61SecurityTestingInfrastructure:
    sutra: "| Framework | Purpose | Methodology | |-----------|---------|-------------| | AgentDojo (ETH Zuri..."
    gloss:
        | Framework | Purpose | Methodology |
|-----------|---------|-------------|
| **AgentDojo** (ETH Zurich + US AISI) | Hijacking scenarios | 4 environments, red teaming |
| **BAD-ACTS** | Adversarial robustness | 188 harmful action instances |
| **Petri** (Anthropic) | Automated auditing | Parallel mu...
end


TERM 62AgentDojoEnvironments:
    sutra: "``yaml AgentDojo:   environments:     - Workspace     - Travel     - Slack     - Banking    metho..."
    gloss:
        ```yaml
AgentDojo:
  environments:
    - Workspace
    - Travel
    - Slack
    - Banking

  methodology:
    - Combine benign user tasks with injection tasks
    - Red team to develop novel attacks
    - Measure attack success and defense effectiveness

  finding: Attacks generalize across environm...
end


TERM 63ContinuousSecurityAssessment:
    sutra: "``yaml Continuous_Assessment:   automated:     - Regular penetration testing     - Adversarial in..."
    gloss:
        ```yaml
Continuous_Assessment:
  automated:
    - Regular penetration testing
    - Adversarial input generation
    - Policy compliance verification

  metrics:
    - Attack success rate trending
    - Defense bypass frequency
    - Mean time to detect
    - Mean time to respond

  feedback_loop:...
end


TERM 71BoundedAutonomy:
    sutra: "``yaml Bounded_Autonomy:   principle: Clear perimeters for independent judgment    implementation..."
    gloss:
        ```yaml
Bounded_Autonomy:
  principle: Clear perimeters for independent judgment

  implementation:
    - Defined operational scope
    - Hard constraints on prohibited actions
    - Automatic escalation triggers
    - Capability-based access control
```
end


TERM 72ProgressiveTrust:
    sutra: "``yaml Progressive_Trust:   principle: Capability expansion based on demonstrated reliability    ..."
    gloss:
        ```yaml
Progressive_Trust:
  principle: Capability expansion based on demonstrated reliability

  stages:
    initial:
      - All actions require review
      - Limited tool access
      - Simple task scope

    intermediate:
      - Low-risk actions autonomous
      - Expanded tool access
      -...
end


TERM 73ReversibleDelegation:
    sutra: "``yaml Reversible_Delegation:   principle: Human oversight can reclaim control at any level    im..."
    gloss:
        ```yaml
Reversible_Delegation:
  principle: Human oversight can reclaim control at any level

  implementation:
    - Emergency stop mechanisms
    - Override capabilities at all levels
    - Escalation pathways always available
    - No catastrophic failure from control reclamation
```

---
end


TERM 81GlobalFrameworks:
    sutra: "| Jurisdiction | Framework | Approach | |--------------|-----------|----------| | EU | AI Act | C..."
    gloss:
        | Jurisdiction | Framework | Approach |
|--------------|-----------|----------|
| **EU** | AI Act | Comprehensive regulation |
| **US** | EO 14110 → EO 14179 | Safety with innovation balance |
| **UK** | Pro-Innovation Framework | Non-statutory, flexible principles |
end


TERM 82IndustryCollaboration:
    sutra: "``yaml Coalition_for_Secure_AI:   purpose: Industry collaboration for normative best practices   ..."
    gloss:
        ```yaml
Coalition_for_Secure_AI:
  purpose: Industry collaboration for normative best practices

  focus_areas:
    - AI supply chain security
    - Defender preparation
    - Risk governance
    - Agentic AI security patterns

  outputs:
    - Model signing standards
    - Machine-readable model ca...
end


TERM 91ComprehensiveLogging:
    sutra: "``yaml Logging_Requirements:   actions:     - Every tool invocation     - All external API calls ..."
    gloss:
        ```yaml
Logging_Requirements:
  actions:
    - Every tool invocation
    - All external API calls
    - State modifications
    - Decision points

  metadata:
    - Timestamps
    - Context snapshots
    - Confidence scores
    - Reasoning traces

  retention:
    - Audit trail compliance
    - Inci...
end


TERM 92RealTimeMonitoring:
    sutra: "``yaml Monitoring_Infrastructure:   dashboards:     - System health     - Behavioral patterns    ..."
    gloss:
        ```yaml
Monitoring_Infrastructure:
  dashboards:
    - System health
    - Behavioral patterns
    - Security alerts
    - Performance metrics

  anomaly_detection:
    - Behavioral baseline deviation
    - Unusual tool access patterns
    - Unexpected output characteristics

  alerting:
    - Sever...
end


TERM 101TheLimitationofExternalControls:
    sutra: "External alignment through guardrails and validation proves insufficient when models can delibera..."
    gloss:
        External alignment through guardrails and validation proves insufficient when models can deliberately circumvent restrictions.
end


TERM 102TowardIntrinsicAlignment:
    sutra: "``yaml Intrinsic_Alignment:   concept: Internal monitoring mechanisms resistant to manipulation  ..."
    gloss:
        ```yaml
Intrinsic_Alignment:
  concept: Internal monitoring mechanisms resistant to manipulation

  approaches:
    constitutional_AI:
      - Self-review against defined principles
      - Balance autonomy with values alignment
      - Integrated human feedback loops

    self_evaluation:
      - C...
end


TERM SATELLITES:
    sutra: "None"
    gloss:
        None. This is a leaf asteroid.

---
end


TERM VERSIONHISTORY:
    sutra: "Version 1.0.0 (December 2025): Genesis establishment - Canonized from Technology Lunar - Agents.m..."
    gloss:
        **Version 1.0.0** (December 2025): Genesis establishment
- Canonized from Technology Lunar - Agents.md
- Defense-in-depth architecture specified
- Governance frameworks documented
end
