# REF-OPERATIONAL_TOPOLOGY
## Executable Coordination Contract
**Version**: 1.0.0
**Created**: 2026-01-19
**Authority**: C2 (Tactical Topology Agent)

---

## 1. Zone Ownership Matrix

| Zone | Primary Writer | Secondary | Notes |
|------|----------------|-----------|-------|
| `00-ORCHESTRATION/` | Principal, Claude Code | Oracle (directives) | Protected: state/, oracle_contexts/ |
| `01-CANON/` | Principal | Claude (with approval) | PROTECTED - deletions require approval |
| `02-OPERATIONAL/` | Claude Code | Principal | Contains coordination.yaml |
| `03-QUEUE/` | Claude Code | Principal | Modal-organized pending work |
| `04-SOURCES/` | Gemini (raw/), Alpha/Beta (processed/) | Principal | Zone-prefixed outputs |
| `05-ARCHIVE/` | Claude Code | Principal | Historical preservation |
| `06-EXEMPLA/` | Principal | Claude Code | Templates only |
| `-INBOX/` | External Platforms | Principal | ChatGPT drops, reinit capsules |
| `-OUTGOING/` | Claude Code | Principal | Export staging, blitzkrieg bundles |

### Zone Write Permissions (coordination.yaml extract)
```
alpha:  04-SOURCES/processed/a-*, 00-ORCHESTRATION/logs/*-A.md
beta:   04-SOURCES/processed/b-*, 00-ORCHESTRATION/logs/*-B.md
gemini: 04-SOURCES/raw/*, 04-SOURCES/processed/g-*
chatgpt: .github/*
shared: *.csv (append-only, row-level locking)
```

---

## 2. Flow Diagram

```
                    INTAKE FLOW
    ================================================
    External Platform    -INBOX/              Zone
    ------------------------------------------------
    ChatGPT      -----> blitzkrieg_drop/ --> 00-ORCHESTRATION/directives/
    Gemini       -----> (direct)         --> 04-SOURCES/raw/
    Reinit Caps  -----> YYYYMMDD-slug/   --> (rehydration reference)

                    EXPORT FLOW
    ================================================
    Zone                 -OUTGOING/          External
    ------------------------------------------------
    00-ORCHESTRATION --> YYYYMMDD-blitzkrieg/ --> Multi-agent dispatch
    Any Zone         --> YYYYMMDD-<slug>/     --> Reinit capsule
    Survey Results   --> YYYYMMDD-corpus_survey/ --> Analysis bundles

                    KAIZEN FEEDBACK
    ================================================
    Operational learnings --> 00-ORCHESTRATION/state/
                              - DYN-* (dynamic state)
                              - REF-* (reference docs)
                              - ARCH-* (architectural decisions)
```

---

## 3. Coordination Contract

### Canonical Paths
| Artifact | Canonical Path |
|----------|----------------|
| Coordination Config | `02-OPERATIONAL/coordination.yaml` |
| Blitzkrieg Protocol | `00-ORCHESTRATION/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md` |
| System State | `00-ORCHESTRATION/state/system_state.json` |
| Structural Verifier | `00-ORCHESTRATION/scripts/structural_verify.sh` |
| Constitution | `CLAUDE.md` (root) |
| Navigation | `COCKPIT.md` (root) |

### Output Conventions
| Output Type | Path Pattern |
|-------------|--------------|
| Blitzkrieg bundles | `-OUTGOING/${DATE}-blitzkrieg/` |
| Reinit capsules | `-OUTGOING/YYYYMMDD-<slug>/` |
| Execution logs | `00-ORCHESTRATION/execution_logs/EXECUTION_LOG-YYYY-MM-DD-NNN.md` |
| Survey exports | `-OUTGOING/YYYYMMDD-corpus_survey/` |

### Communication Patterns
```
Oracle --> Code:  00-ORCHESTRATION/directives/DIRECTIVE-NNN.md
Code --> Oracle:  00-ORCHESTRATION/execution_logs/EXECUTION_LOG-*.md
Inter-instance:   Git branches (no direct communication)
```

---

## 4. Prohibited Patterns

| Pattern | Violation | Correct Form |
|---------|-----------|--------------|
| `OUTGOING/` at root | Legacy form | `-OUTGOING/` |
| `outgoing/` at root | Lowercase legacy | `-OUTGOING/` |
| `config/` at root | Deprecated location | `02-OPERATIONAL/` |
| Subdirectories in zones | Flat principle violation | Use naming prefixes |
| Orphan files at root | Structure violation | Only CLAUDE.md, COCKPIT.md, Makefile |

### Constitutional Rules (CLAUDE.md extract)
1. **FLAT PRINCIPLE**: Use prefixes (ARCH-, DYN-, REF-, SCAFF-), not subdirectories
2. **NUMBERED DIRECTORIES**: Only 00-06 plus `-INBOX/`, `-OUTGOING/`
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/, 01-CANON/ require approval for deletions

---

## 5. Verification Commands

### Primary Verification
```bash
./00-ORCHESTRATION/scripts/structural_verify.sh
```

### Quick Checks
```bash
# Check for forbidden root directories
ls -1 | grep -E "^(OUTGOING|outgoing|config)$"

# Check for legacy OUTGOING/ references in live docs
rg "OUTGOING/" --glob "*.md" | grep -v "\-OUTGOING/"

# Verify coordination.yaml location
test -f 02-OPERATIONAL/coordination.yaml && echo "OK" || echo "MISSING"

# Count orphan files at root
ls -1 *.md 2>/dev/null | grep -v -E "^(CLAUDE|COCKPIT)\.md$" | wc -l
```

### Report Location
Verification writes to: `00-ORCHESTRATION/state/DYN-STRUCTURAL_VERIFY_REPORT.md`

---

## Cross-References

- Detailed topology survey: `-OUTGOING/20260119-corpus_survey/TOPOLOGY_MAP.md`
- Zone ownership details: `02-OPERATIONAL/coordination.yaml`
- Processing pattern: `00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md`
- 18 evaluative lenses: `00-ORCHESTRATION/state/REF-STANDARDS.md`

---

*This document is an operational contract. Modifications require coordination.yaml alignment.*
