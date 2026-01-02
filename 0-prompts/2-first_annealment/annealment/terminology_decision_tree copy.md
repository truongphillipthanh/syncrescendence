# TERMINOLOGY DECISION TREE
## Five-Question Flowchart for Rapid Dimension Determination

**Purpose**: When encountering ambiguous terminology ("Level," "Tier," "Stage," "Phase"), determine correct dimension in <30 seconds  
**Authority**: Master Schema v1.0  
**Usage**: Refer to this during Document 1-6 updates when uncertain

---

## QUICK REFERENCE: THE FIVE DIMENSIONS

| Dimension | Format | Range | Use Case |
|-----------|--------|-------|----------|
| **Scale** | Scale: [1-4]-[Name] | 1-Micro to 4-Meta | Practitioner cosmological sophistication (optional advancement) |
| **Level** | Level: [1-4]-[Name] [Chain] | 1-Initial to 4-Mastery | Chain development progression (Technology, Sensing, Coherence, Efficacy, Embodiment, Transcendence) |
| **Degree** | Degree: [1-5]-[Name] | 1-Recognition to 5-Transmission | Lunar mastery progression (Coherence & Transcendence chains only) |
| **Stage** | Stage: [1-5]-[Name] | 1-Forum to 5-Portico | Content production platform maturity (organizational prerequisite) |
| **Phase** | Phase: [Name] Phase | Foundation → Infrastructure | Business timeline / organizational progression |

---

## DECISION TREE: 5 SEQUENTIAL QUESTIONS

### QUESTION 1: What's the context?

```
Is this about ORGANIZATIONAL/BUSINESS progression?
(deployment phases, business timeline, organizational readiness)

YES → Go to QUESTION 2 (Time-based determination)
NO  → Go to QUESTION 3 (Practitioner-based determination)
```

**Examples - YES (Business Context)**:
- "We're entering the Validation Phase"
- "By Scaling, we'll have infrastructure"
- "During Foundation, we built core"

**Examples - NO (Individual Context)**:
- "I'm at an intermediate level in sensing"
- "I've reached mastery in my practice"
- "I'm exploring this new domain"

---

### QUESTION 2: Is this business timeline? (Time-Sequential)

```
Is this about SEQUENTIAL ORGANIZATIONAL PROGRESSION?
(Foundation → Validation → Scaling → Institute → Infrastructure)

YES → Use PHASE: [Name] Phase
      Examples: "Phase: Foundation Phase"
                "Phase: Scaling Phase"

NO  → Is this platform maturity?
      (Forum → Podium → Amphitheatre → Atrium → Portico)
      
      YES → Use STAGE: [N]-[Name]
            Examples: "Stage: 1-Forum"
                      "Stage: 3-Amphitheatre"
      
      NO  → ESCALATE: Context unclear, ask user or flag [VERIFY]
```

---

### QUESTION 3: What's the practitioner dimension?

```
Is this about PRACTITIONER SOPHISTICATION or CAPABILITY?

Ask: "Is this about..."

A) Optional personal advancement level?
   (can stay at lower level, no hierarchy)
   
   YES → Use SCALE: [1-4]-[Name]
         Examples: "Scale: 1-Micro" (focused specialist)
                   "Scale: 3-Macro" (integrated generalist)
   
   NO → Go to QUESTION 4

B) Required competence in specific chain?
   (must achieve Level 1 before Level 2, chain-specific)
   
   YES → Use LEVEL: [1-4]-[Name] [Chain]
         Examples: "Level: 2-Intermediate in Technology"
                   "Level: 4-Mastery in Coherence"
   
   NO → Go to QUESTION 4
```

---

### QUESTION 4: Is this Lunar system specific?

```
Is this about COHERENCE or TRANSCENDENCE LUNAR PROGRESSION?
(1-Recognition, 2-Exploration, 3-Commitment, 4-Integration, 5-Transmission)

Checklist:
- [ ] Document mentions "Coherence" AND "Lunar"?
- [ ] Document mentions "Transcendence" AND "Lunar"?
- [ ] Reference is to 5-level progression (not 4)?

YES (Any of above) → Use DEGREE: [1-5]-[Name]
                     Examples: "Degree: 1-Recognition"
                               "Degree: 3-Commitment"
                               "Degree: 5-Transmission"

NO → Proceed to QUESTION 5
```

**Context Clues for YES**:
- "Coherence lunar..." or "Transcendence lunar..."
- "Five degrees of..."
- References to Recognition, Exploration, Commitment, Integration, Transmission
- "Epistemological" or "wisdom progression"

**Context Clues for NO**:
- "Technology chain" or "Sensing chain" or "Efficacy chain" or "Embodiment chain"
- Four-level progression (Initial, Intermediate, Advanced, Mastery)
- "Operational" or "practical" development

---

### QUESTION 5: Chain progression or ambiguous?

```
Can you identify which chain this refers to?
(Technology, Sensing, Coherence, Efficacy, Embodiment, Transcendence)

YES → Use LEVEL: [1-4]-[Name] [Chain]
      Examples: "Level: 1-Initial in Embodiment"
                "Level: 3-Advanced in Technology"

NO → Check document section/title for context clues:
     - Operations doc? → Probably STAGE:
     - Strategy doc? → Could be LEVEL: or PHASE:
     - Chain-specific doc? → Definitely LEVEL: [chain]
     - Assessment doc? → Could be SCALE: or DEGREE:

If STILL UNCLEAR → Mark [VERIFY] and ask user
```

---

## DECISION TREE FLOWCHART (ASCII)

```
START: Ambiguous terminology found
  |
  ├─ QUESTION 1: Business or individual context?
  |  |
  |  ├─ BUSINESS → QUESTION 2: Timeline or platform?
  |  |  |
  |  |  ├─ TIMELINE → Phase: [Name] Phase ✓
  |  |  |
  |  |  └─ PLATFORM → Stage: [N]-[Name] ✓
  |  |
  |  └─ INDIVIDUAL → QUESTION 3: What aspect?
  |     |
  |     ├─ SOPHISTICATION (optional) → Scale: [1-4]-[Name] ✓
  |     |
  |     ├─ CHAIN COMPETENCE (required) → QUESTION 4: Lunar?
  |     |  |
  |     |  ├─ YES → Degree: [1-5]-[Name] ✓
  |     |  |
  |     |  └─ NO → QUESTION 5: Which chain?
  |     |     |
  |     |     ├─ IDENTIFIED → Level: [1-4]-[Name] [Chain] ✓
  |     |     |
  |     |     └─ UNCLEAR → [VERIFY] flag for review
```

---

## ANTI-PATTERNS: WHAT NOT TO DO

### Anti-Pattern 1: Mixing Dimensions
```
❌ BAD: "Must reach Scale 3 before Level 2"
✓ GOOD: "Level: 1-Initial required before Level: 2-Intermediate in Technology"

REASON: Scale and Level are orthogonal (independent)—no ordering between them
```

### Anti-Pattern 2: Missing Chain Context
```
❌ BAD: "Practitioners at Level 2"
✓ GOOD: "Practitioners at Level: 2-Intermediate in Technology Chain"

REASON: Level is always chain-specific; context is required
```

### Anti-Pattern 3: Wrong Dimension for Timeline
```
❌ BAD: "We're at Phase 3 development"
✓ GOOD: "We're in Phase: Scaling Phase of business deployment"

REASON: Phase refers to business timeline only (Foundation/Validation/Scaling)
```

### Anti-Pattern 4: Degree Outside Lunar
```
❌ BAD: "Technology practitioners at Degree 2"
✓ GOOD: "Technology practitioners at Level: 2-Intermediate in Technology"

REASON: Degree only applies to Coherence/Transcendence Lunar systems
```

### Anti-Pattern 5: Missing Stage Names
```
❌ BAD: "Stage 2 content platform"
✓ GOOD: "Stage: 2-Podium content platform"

REASON: Stage must include theatrical name (Forum/Podium/Amphitheatre/Atrium/Portico)
```

---

## QUICK-REFERENCE DISAMBIGUATION TABLE

| Ambiguous Term | Context A | Answer A | Context B | Answer B | Context C | Answer C |
|---|---|---|---|---|---|---|
| **Level** | Chain progression (Tech, Sensing...) | Level: [1-4]-[Chain] | Lunar (Coherence/Transcendence) | Degree: [1-5] | Timeline | DON'T USE—wrong term |
| **Tier** | Platform maturity | Stage: [1-5]-[Name] | Practitioner sophistication | Scale: [1-4]-[Name] | Generic/unclear | USE DECISION TREE |
| **Stage** | Platform deployment | Stage: [1-5]-[Name] | Chain development | Level: [1-4]-[Chain] | Generic | USE DECISION TREE |
| **Phase** | Business timeline | Phase: [Name] Phase | Practitioner development | Level: or Degree: | Avoid using generically | ONLY for business timeline |
| **Degree** | Lunar progression (Coherence/Transcendence) | Degree: [1-5]-[Name] | Chain development | Level: [1-4]-[Chain] | Any other | DON'T USE |

---

## VALIDATION QUICK-CHECKS

**Before finalizing any replacement, verify**:

1. **Primary Label Present**: All references include primary label + name
   - ✓ "Scale: 1-Micro" not just "1"
   - ✓ "Level: 2-Intermediate in Technology" not just "2"
   - ✓ "Stage: 3-Amphitheatre" not just "3"

2. **Chain Context When Needed**: All Level: references specify chain
   - ✓ "Level: 3-Advanced in Coherence Chain"
   - ✗ "Level: 3-Advanced" (missing chain)

3. **Theatrical Names for Stage**: All Stage: include theatrical name
   - ✓ "Stage: 1-Forum" (yes, has name)
   - ✗ "Stage: 1" (missing theatrical name)

4. **No Dimension Mixing**: Single statement uses only one dimension per reference
   - ✓ "Practitioners at Scale: 2-Meso work in Level: 1-Initial Technology"
   - ✗ "Practitioners at Scale 2 Level must be Stage 1" (mixing without labels)

5. **Orthogonality Respected**: No statement suggests dimensional hierarchy
   - ✓ "Scale and Level are independent"
   - ✗ "Reach Scale 3 before Level 2" (violates orthogonality)

---

## ESCALATION PATH

**If decision tree doesn't resolve**:

1. **Mark with [VERIFY]** in the document
2. **Note context** in comments (where it appears, what it could mean)
3. **Continue with best guess** based on most likely interpretation
4. **Flag for gate validation** review

**Example**:
```
[VERIFY] "practitioners at tier 2" — Could be:
  - Scale: 2-Meso (sophistication)?
  - Level: 2-Intermediate (chain context missing)?
  - Stage: 2-Podium (platform)?
  Best guess: Scale: 2-Meso based on surrounding context
```

---

**Use this tree every time you encounter "Tier," "Level," "Stage," "Phase," or "Degree" ambiguity.**  
**Target: <30 seconds per decision**  
**Result: Zero dimensional confusion in finished corpus**