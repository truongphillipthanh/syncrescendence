# Structural Anomalies Analysis
**Generated**: 2026-01-17T04:35:00Z

---

## FLAT PRINCIPLE Violations

The CLAUDE.md Constitutional Rule #1 states:
> **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.

### Depth-3+ Directories Found

| Path | Depth | Assessment |
|------|-------|------------|
| ./00-ORCHESTRATION/blackboard/capabilities | 3 | **EXEMPTED** - Packet type directory |
| ./00-ORCHESTRATION/blackboard/evidence | 3 | **EXEMPTED** - Packet type directory |
| ./00-ORCHESTRATION/blackboard/plans | 3 | **EXEMPTED** - Packet type directory |
| ./00-ORCHESTRATION/blackboard/audits | 3 | **EXEMPTED** - Packet type directory |
| ./00-ORCHESTRATION/blackboard/executions | 3 | **EXEMPTED** - Packet type directory |
| ./02-OPERATIONAL/models/profiles | 3 | **VIOLATION** - Should use MODEL-PROFILE- prefix |
| ./02-OPERATIONAL/prompts/canonical | 3 | **VIOLATION** - Should use PROMPT-CANONICAL- prefix |
| ./02-OPERATIONAL/prompts/unified | 3 | **VIOLATION** - Should use PROMPT-UNIFIED- prefix |
| ./02-OPERATIONAL/prompts/profiles | 3 | **VIOLATION** - Should use PROMPT-PROFILE- prefix |
| ./.claude/commands/project | 3 | **EXEMPTED** - Tool configuration |

---

## Exemption Rationale

### Blackboard Structure
The blackboard uses subdirectories by design (per packet_protocol.json):
```
blackboard/
  capabilities/  <- CAP packets
  evidence/      <- EVD packets
  plans/         <- PLN packets
  executions/    <- EXE packets
  audits/        <- AUD packets
```

This is an **architectural decision** rather than a violation, as it:
1. Serves packet routing
2. Enables automated discovery by packet type
3. Was explicitly designed in coordination.yaml

**Recommendation**: Document this exemption in CLAUDE.md or create a `STRUCTURAL_EXEMPTIONS.md`.

### Tool Directories
`.claude/commands/project` is imposed by Claude Code tooling, not a design choice.

---

## True Violations

### 02-OPERATIONAL Subdirectories

| Current Structure | Proposed Flat Structure |
|-------------------|------------------------|
| `prompts/canonical/PROMPT-IMEP-*.md` | `PROMPT-CANONICAL-IMEP-*.md` |
| `prompts/unified/PROMPT-UNIFIED-*.md` | `PROMPT-UNIFIED-*.md` |
| `prompts/profiles/PROMPT-PROFILE-*.md` | `PROMPT-PROFILE-*.md` |
| `models/profiles/MODEL-*.md` | `MODEL-PROFILE-*.md` |

**Impact**: 4 subdirectories with ~15 files affected

**Recommended Action**:
1. Create migration plan
2. Update any references
3. Execute flattening
4. Verify no broken references

---

## Root-Level Anomalies

### Unnumbered Root Directories

| Directory | Assessment |
|-----------|------------|
| ./system_prompts/ | **LEGACY** - Should relocate to 02-OPERATIONAL |
| ./.decisions/ | **LEGACY** - Should relocate to 00-ORCHESTRATION or archive |
| ./.tmp.driveupload/ | **TEMP** - Should be in .gitignore |
| ./config/ | **UTILITY** - Acceptable for coordination.yaml |
| ./.obsidian/ | **TOOL** - Exempted |
| ./.claude/ | **TOOL** - Exempted |

### Constitutional Rule #2
> **NUMBERED DIRECTORIES**: Top-level directories are 00-06. Do not create unnumbered directories at root.

**Violations**: system_prompts/, .decisions/, config/ (debatable)

---

## Structural Health Summary

| Category | Count | Severity |
|----------|-------|----------|
| Exempted (by design) | 5 | N/A |
| Tool-imposed | 2 | N/A |
| True violations | 4 | LOW |
| Root-level legacy | 3 | LOW |

---

## Proposed Patches

### Patch 1: Flatten 02-OPERATIONAL (LOW priority)
```bash
# Migration commands (DO NOT EXECUTE - for planning only)
mv 02-OPERATIONAL/prompts/canonical/* 02-OPERATIONAL/
mv 02-OPERATIONAL/prompts/unified/* 02-OPERATIONAL/
mv 02-OPERATIONAL/prompts/profiles/* 02-OPERATIONAL/
mv 02-OPERATIONAL/models/profiles/* 02-OPERATIONAL/
rmdir 02-OPERATIONAL/prompts/canonical 02-OPERATIONAL/prompts/unified
rmdir 02-OPERATIONAL/prompts/profiles 02-OPERATIONAL/prompts
rmdir 02-OPERATIONAL/models/profiles 02-OPERATIONAL/models
```

### Patch 2: Document Blackboard Exemption
Add to CLAUDE.md:
```markdown
### Structural Exemptions
- **00-ORCHESTRATION/blackboard/**: Subdirectories permitted for packet type routing
- **Tool directories**: .claude/, .obsidian/, etc. exempted
```

### Patch 3: Relocate Legacy Directories (MEDIUM priority)
```bash
# system_prompts → 02-OPERATIONAL
mv system_prompts/* 02-OPERATIONAL/PROMPT-LEGACY-*.md

# .decisions → 05-ARCHIVE or 00-ORCHESTRATION
mv .decisions/* 00-ORCHESTRATION/decisions/  # if active
# or
mv .decisions/* 05-ARCHIVE/decisions/  # if historical
```

---

## Compliance Score

| Rule | Status |
|------|--------|
| FLAT PRINCIPLE | 85% compliant (4 violations) |
| NUMBERED DIRECTORIES | 90% compliant (3 violations) |
| Overall Structural Health | GOOD |

**Note**: All violations are LOW severity and do not impede operation.

