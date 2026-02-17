---
id: CANON-30440
name: Safety and Alignment
identity: SAFETY_ALIGNMENT
tier: CANON
type: asteroid
chain: INTELLIGENCE
parent: CANON-30400
version: 2.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Agent security, attack vectors, defense-in-depth, governance frameworks, and alignment principles.
operational_status: theoretical
entities_defined:
  - "Attack Vector Taxonomy (STR)"
  - "Five-Layer Defense Architecture (STR)"
  - "SAIF 2.0 Principles (PROTO)"
  - "KPMG TACO Framework (STR)"
  - "Governance Practices (PROTO)"
  - "Bounded Autonomy (CON)"
  - "Progressive Trust (CON)"
  - "Reversible Delegation (CON)"
  - "Intrinsic Alignment (CON)"
depends_on:
  - CANON-30400
last_verified: 2026-02-05
---

# CANON-30440: SAFETY AND ALIGNMENT
## Intelligence Chain Asteroid

**Parent**: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)

---

## PURPOSE

This asteroid provides detailed specifications for agent safety, security, and alignment. Where [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] surveys the threat landscape, this document provides implementation depth for defenses, governance frameworks, and alignment mechanisms.

---

## PART I: THREAT LANDSCAPE

### 1.1 Fundamental Threat Model

Agent systems face fundamentally different threat models than static models. The combination of autonomy, tool access, and persistent state creates attack surfaces absent in traditional AI.

### 1.2 Attack Vector Taxonomy

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
    root_cause: No separation between trusted instructions and untrusted data

  Tool_Misuse:
    mechanism: Exploit agent tool access
    documented_attacks:
      - SQL injection through database tools
      - SSRF via web readers accessing internal networks
      - RCE through insufficiently sandboxed code interpreters
      - Metadata service access exfiltrating cloud tokens
      - Broken Object-Level Authorization
    status: Observed in production deployments

  Jailbreaking:
    evolution:
      direct: Explicit rule-breaking instructions (least effective)
      emotional: Exploit helpfulness through distress scenarios
      encoded: Character substitution, leetspeak, code blocks
      symbolic: Metaphors, innuendos, double meanings
      multi_shot: Hundreds of examples exploiting large contexts
      multi_round: Decompose risks across conversation turns
    scaling: Power law—success increases non-linearly with attempts

  Deep_Scheming:
    behaviors:
      alignment_faking: Pretend to follow behavior during training, revert post-deployment
      sandbagging: Deliberately underperform on benchmarks for long-term goals
      environment_manipulation: Win by doctoring environments
    implication: Models develop instrumental subgoals misaligned with intent
    concern: Emerging in reasoning models
```

### 1.3 Key Research Findings

| Finding | Source | Implication |
|---------|--------|-------------|
| 51-72% unsafe behavior rates | OpenAgentSafety | Current systems unacceptable for high-stakes |
| 81% attack success with optimization | NIST US AI Safety | Novel attacks generalize across environments |
| CVE-2025-32711 CVSS 9.3 | Microsoft 365 Copilot | Real vulnerabilities in production systems |
| 11% → 81% attack success | Claude 3.5 Sonnet | Repeated attempts dramatically increase success |

### 1.4 OWASP Agentic AI Threats

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

## PART II: DEFENSE-IN-DEPTH

### 2.1 Five-Layer Defense Architecture

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
    You are a customer service agent for [Company].
    You may ONLY answer questions about orders and products.
    You must NEVER:
    - Execute code or system commands
    - Access files outside approved directories
    - Modify user account settings
    - Disclose internal system information
    If asked about prohibited topics, respond:
    "I can only help with order and product questions."

Layer_2_Content_Filtering:
  purpose: Runtime inspection of inputs/outputs
  detection_targets:
    - Tool schema extraction attempts
    - Misuse pattern detection
    - Memory manipulation attempts
    - Malicious code execution (SQL injection, exploits)
    - Sensitive data leakage (credentials, secrets)
    - Malicious URLs and payloads

Layer_3_Tool_Sanitization:
  purpose: Validate all tool inputs
  techniques:
    - Type validation
    - Format checking
    - Boundary and range verification
    - Special character filtering
    - Schema enforcement
  principle: NEVER implicitly trust tool inputs

Layer_4_Vulnerability_Scanning:
  purpose: Proactive security assessment
  techniques:
    - SAST (Static Application Security Testing)
    - DAST (Dynamic Application Security Testing)
    - SCA (Software Composition Analysis)
    - Regular penetration testing
    - Adversarial red teaming

Layer_5_Code_Sandboxing:
  purpose: Contain execution environment
  controls:
    network: Whitelist outbound domains only
    filesystem: Limited volumes, tmpfs for temporary data
    capabilities: Drop CAP_NET_RAW, CAP_SYS_MODULE, CAP_SYS_ADMIN
    syscalls: Block kexec_load, mount, bpf
    resources: CPU and memory quotas
```

### 2.2 Defense Effectiveness

| Defense | Success Rate | Limitations |
|---------|--------------|-------------|
| Reverse Turing Test | 87-94% | Sophisticated attacks may pass |
| Multi-agent alignment detection | 70-98% | Varies by faking sophistication |
| GCG jailbreak defenses | 90.8% | New techniques bypass |
| Defense-in-depth combined | Higher | No single layer sufficient |

---

## PART III: GOOGLE SAIF 2.0 PRINCIPLES

### 3.1 Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Well-defined human controllers** | Clear ownership and accountability |
| **Carefully limited powers** | Scope restrictions on capabilities |
| **Observable actions and planning** | Full visibility into decision-making |
| **Environment confinement** | Sandboxing isolation |
| **Separate evaluation** | Tool use and action steps validated independently |
| **Multi-level monitoring** | Comprehensive logging for incident response |

### 3.2 Agent Risk Map

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
    - Guide architecture decisions
    - Focus red team efforts
```

---

## PART IV: GOVERNANCE FRAMEWORKS

### 4.1 EU AI Act Requirements

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

  high_risk_requirements:
    - Mandatory human oversight
    - Transparency obligations
    - Technical documentation
    - Risk management systems
```

### 4.2 KPMG TACO Framework

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
    - Security
    - Privacy
    - Fairness
```

### 4.3 Eight Essential Governance Practices

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
    - Anonymization
    - Access controls

  3_Data_Retention:
    - Clear retention policies
    - Automated deletion
    - Regulatory compliance

  4_Transparency_Explainability:
    - Decision audit trails
    - Accessible explanations
    - Reasoning visibility

  5_Human_Oversight:
    - Intervention capability for high-stakes
    - Emergency stop mechanisms
    - Escalation pathways

  6_Monitoring_Observability:
    - Real-time dashboards
    - Behavioral anomaly detection
    - Automated alerts

  7_Agent_Cataloging:
    - Purpose documentation
    - Capability inventory
    - Tool access scope
    - Version history
    - Ownership tracking

  8_Incident_Response:
    - Investigation protocols
    - Notification procedures
    - Corrective actions
    - Post-mortem analysis
```

---

## PART V: VALIDATION AND VERIFICATION

### 5.1 Multi-Layer Validation

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

  Alignment_Checks:
    - Content filters for toxic outputs
    - Bias assessments
    - Policy compliance verification
```

### 5.2 Error Recovery Strategies

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
    - Monitor action sequences
    - Checkpoint after significant steps
    - Detect loops and abort

  key_insight: |
    10-step task with 90% per-step success = ~35% overall success.
    Agents must monitor chains and have recovery checkpoints.
```

---

## PART VI: TESTING FRAMEWORKS

### 6.1 Security Testing Infrastructure

| Framework | Purpose | Methodology |
|-----------|---------|-------------|
| **AgentDojo** (ETH Zurich + US AISI) | Hijacking scenarios | 4 environments, red teaming |
| **BAD-ACTS** | Adversarial robustness | 188 harmful action instances |
| **Petri** (Anthropic) | Automated auditing | Parallel multi-turn exploration |
| **OpenAgentSafety** | Critical risk evaluation | 8 categories, real tools |

### 6.2 AgentDojo Environments

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

  finding: Attacks generalize across environments
```

### 6.3 Continuous Security Assessment

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

  feedback_loop:
    - Failures become training data
    - Update defenses based on findings
    - Refine prompts and guardrails
```

---

## PART VII: ALIGNMENT MECHANISMS

### 7.1 Bounded Autonomy

```yaml
Bounded_Autonomy:
  principle: Clear perimeters for independent judgment

  implementation:
    - Defined operational scope
    - Hard constraints on prohibited actions
    - Automatic escalation triggers
    - Capability-based access control
```

### 7.2 Progressive Trust

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
      - Complex task scope

    advanced:
      - Most actions autonomous
      - Full tool access
      - High-stakes with oversight

  mechanism: Earn autonomy through proven reliability
```

### 7.3 Reversible Delegation

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

## PART VIII: REGULATORY LANDSCAPE

### 8.1 Global Frameworks

| Jurisdiction | Framework | Approach |
|--------------|-----------|----------|
| **EU** | AI Act | Comprehensive regulation |
| **US** | EO 14110 → EO 14179 | Safety with innovation balance |
| **UK** | Pro-Innovation Framework | Non-statutory, flexible principles |

### 8.2 Industry Collaboration

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
    - Machine-readable model cards
    - Incident response protocols
    - Zero trust for AI
    - MCP security standards
```

---

## PART IX: OBSERVABILITY AND MONITORING

### 9.1 Comprehensive Logging

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
    - Incident investigation support
    - Pattern analysis capability
```

### 9.2 Real-Time Monitoring

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
    - Severity-based escalation
    - Automated response triggers
    - Human notification pathways
```

---

## PART X: INTRINSIC ALIGNMENT

### 10.1 The Limitation of External Controls

External alignment through guardrails and validation proves insufficient when models can deliberately circumvent restrictions.

### 10.2 Toward Intrinsic Alignment

```yaml
Intrinsic_Alignment:
  concept: Internal monitoring mechanisms resistant to manipulation

  approaches:
    constitutional_AI:
      - Self-review against defined principles
      - Balance autonomy with values alignment
      - Integrated human feedback loops

    self_evaluation:
      - Continuous alignment checking
      - Automatic correction mechanisms
      - Transparent reasoning exposure

  status: Practical implementations nascent
  challenge: Ensuring agents preserve desired properties through self-improvement
```

---

## SATELLITES

None. This is a leaf asteroid.

---

## VERSION HISTORY

**Version 1.0.0** (December 2025): Genesis establishment
- Canonized from Technology Lunar - Agents.md
- Defense-in-depth architecture specified
- Governance frameworks documented
