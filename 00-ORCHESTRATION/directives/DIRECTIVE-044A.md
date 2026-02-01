# DIRECTIVE-044A: INTENTION COMPASS UPDATE + TECH TREE VERIFICATION
## Stream A — Claude 2 (Sonnet 4.5)

**Issued**: 2026-01-11
**Stream**: A (Sonnet 4.5 recommended — tactical, clear instructions)
**Priority**: MODERATE
**Estimated Duration**: 30-45 minutes
**Parallel**: DIRECTIVE-044B executing simultaneously on Claude 3
**Companion**: ORACLE12_PEDIGREE.md (read first)

---

## PREAMBLE

You are Claude 2, executing Stream A of Blitzkrieg 44. This is a **minor** blitzkrieg focused on housekeeping captured during Oracle 12 strategic session.

**Your mandate**: Update the Intention Compass with new intentions and verify tech tree concepts are canonized.

---

## PHASE 1: UPDATE ARCH-INTENTION_COMPASS.md (~15 minutes)

### 1.1 Read Current State
```bash
cat 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
```

### 1.2 Add New Intentions from Oracle 12

**Add to URGENT section**:
```markdown
### URGENT
- [ ] Temporal intelligence refresh pipeline — Automation candidate for model/platform features that expire. Cadenced update system for ARCH- archived research.
```

**Add to SPRINT section**:
```markdown
### SPRINT
- [ ] Canonize Model Manual/Prompting conceptual space — Verify coverage in CANON-31100-ACUMEN, CANON-31120-TONE_LIBRARY, translate.xml
- [ ] Canonize Platform Features/Ecosystem Leverage — Cross-ref CANON-31142-PLATFORM_GRAMMAR, AI_ECOSYSTEM_SURVEY.md
- [ ] Canonize Model Qualities/Capabilities/Benchmarks — Cross-ref MODEL_INDEX.md, CANON-30000-INTELLIGENCE
- [ ] Blitzkrieg model specification protocol — Formalize in CLAUDE.md or coordination.yaml
```

**Add to BACKLOG section**:
```markdown
### BACKLOG
- [ ] Deep Research: Claude Code + Anthropic Ecosystem (prompt prepared)
- [ ] Deep Research: OpenAI Codex + ecosystem (requires community sampling)
- [ ] Deep Research: Google Jules + Gemini CLI (requires community sampling)
- [ ] Plan Mode as Oracle replacement — Evaluate CLI Plan vs web app strategic synthesis
- [ ] Permission fatigue mitigation — --dangerously-skip-permissions vs allowlisting
```

**Add to PATTERNS section**:
```markdown
### PATTERNS
- [x] Temporal vs evergreen distinction — RESOLVED: Archive temporal intelligence with expiration warning; CANON = evergreen only
```

### 1.3 Verify Update
```bash
wc -l 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
```

---

## PHASE 2: TECH TREE CANONIZATION VERIFICATION (~20 minutes)

The Sovereign's old tech tree had three conceptual domains needing canonization verification:
1. **Model Manual and Prompting**
2. **Model Qualities, Capabilities and Benchmarks**
3. **Platform Features and Ecosystem Leverage**

### 2.1 Audit Coverage

Run these searches and document findings:

```bash
# Model Manual / Prompting
grep -l -i "prompting\|prompt engineering\|system prompt" 01-CANON/*.md

# Model Qualities / Capabilities / Benchmarks
grep -l -i "benchmark\|capability\|model quality\|frontier model" 01-CANON/*.md

# Platform Features / Ecosystem
grep -l -i "platform\|ecosystem\|mcp\|integration" 01-CANON/*.md
```

### 2.2 Create Verification Report

Create `00-ORCHESTRATION/state/ARCH-TECH_TREE_AUDIT.md`:

```markdown
# TECH TREE CANONIZATION AUDIT
## Oracle 12 Verification

**Date**: 2026-01-11
**Purpose**: Verify Sovereign's tech tree concepts have CANON coverage

---

## Domain 1: Model Manual and Prompting

### Coverage Found:
- [list CANON files with prompting content]

### Gap Analysis:
- [identify any gaps]

### Recommendation:
- [SUFFICIENT / NEEDS_WORK / REQUIRES_NEW_CANON]

---

## Domain 2: Model Qualities, Capabilities, Benchmarks

### Coverage Found:
- [list CANON files]

### Gap Analysis:
- [identify gaps]

### Recommendation:
- [SUFFICIENT / NEEDS_WORK / REQUIRES_NEW_CANON]

---

## Domain 3: Platform Features and Ecosystem Leverage

### Coverage Found:
- [list CANON files]

### Gap Analysis:
- [identify gaps]

### Recommendation:
- [SUFFICIENT / NEEDS_WORK / REQUIRES_NEW_CANON]

---

*Audit completed 2026-01-11 | DIRECTIVE-044A*
```

---

## PHASE 3: LEDGER UPDATE (~5 minutes)

### 3.1 Add Tasks to tasks.csv

```csv
TASK-088,PROJ-012,Update ARCH-INTENTION_COMPASS with Oracle 12 intentions,task,done,P2,Claude_Code,null,0.5,null,2026-01-11,2026-01-11,Blitzkrieg 44
TASK-089,PROJ-012,Audit tech tree canonization coverage,task,done,P2,Claude_Code,TASK-088,0.5,null,2026-01-11,2026-01-11,Blitzkrieg 44
```

---

## VERIFICATION CHECKLIST

- [ ] ARCH-INTENTION_COMPASS.md updated with 11 new intentions
- [ ] ARCH-TECH_TREE_AUDIT.md created with coverage analysis
- [ ] tasks.csv updated with TASK-088-089
- [ ] No subdirectories created (FLAT PRINCIPLE)

---

## EXECUTION LOG TEMPLATE

Create `EXECUTION_LOG-2026-01-11-044A.md` upon completion with:
1. Phases executed
2. Files modified/created
3. Verification outputs
4. Duration

---

*DIRECTIVE-044A issued 2026-01-11 | Oracle 12 | Blitzkrieg 44*
