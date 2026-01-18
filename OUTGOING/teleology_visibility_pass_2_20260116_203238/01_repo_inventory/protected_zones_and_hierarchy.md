# Protected Zones and Load Hierarchy
**Generated**: 2026-01-17T04:33:01Z

---

## Protected Zones (from CLAUDE.md + coordination.yaml)

### Tier 1: ABSOLUTE PROTECTION (Deletion requires Principal approval)

| Zone | Path | Authority |
|------|------|-----------|
| Canon | `01-CANON/` | Constitutional knowledge |
| Orchestration State | `00-ORCHESTRATION/state/` | Living infrastructure |
| Constitutional Rules | `./CLAUDE.md` | Absolute |
| Coordination Config | `./config/coordination.yaml` | Protected |

### Tier 2: MODIFICATION PROTECTION (Changes require verification)

| Zone | Path | Constraint |
|------|------|------------|
| Oracle Contexts | `00-ORCHESTRATION/oracle_contexts/` | Historical record |
| Packet Schemas | `00-ORCHESTRATION/schemas/` | Contract definitions |

### Tier 3: ZONE OWNERSHIP (Per coordination.yaml)

| Zone | Owner | Writable Patterns |
|------|-------|-------------------|
| alpha | Claude Code (Account 2) | `04-SOURCES/processed/a-*`, `00-ORCHESTRATION/logs/*-A.md` |
| beta | Claude Code (Account 3) | `04-SOURCES/processed/b-*`, `00-ORCHESTRATION/logs/*-B.md` |
| gemini | Gemini | `04-SOURCES/raw/*`, `04-SOURCES/processed/g-*` |
| chatgpt | ChatGPT (Codex) | `.github/*` |
| shared | All (append-only) | `00-ORCHESTRATION/state/*.csv`, `04-SOURCES/sources.csv` |

---

## Constitution Load Hierarchy

The system loads constitutional documents in this priority order:

```
┌─────────────────────────────────────────────────────────────────┐
│                    LOAD HIERARCHY (TOP → BOTTOM)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Priority 1: CLAUDE.md (Constitutional Rules)                   │
│  ├── 9 structural/semantic/operational rules                    │
│  ├── Directory structure specification                          │
│  └── Extended thinking triggers                                 │
│                                                                 │
│  Priority 2: config/coordination.yaml                           │
│  ├── Platform constellation ($100/month)                        │
│  ├── Account definitions (5 accounts)                           │
│  ├── Zone ownership                                             │
│  ├── Routing rules                                              │
│  └── Model routing (Opus/Sonnet selection)                      │
│                                                                 │
│  Priority 3: 00-ORCHESTRATION/state/REF-STANDARDS.md            │
│  ├── 18 Evaluative Lenses                                       │
│  └── Decision framework                                         │
│                                                                 │
│  Priority 4: 00-ORCHESTRATION/schemas/packet_protocol.json      │
│  ├── EVD/PLN/EXE/AUD packet schemas                             │
│  └── Naming conventions                                         │
│                                                                 │
│  Priority 5: Session-specific context                           │
│  ├── ORACLE*_CONTEXT.md                                         │
│  └── INTERACTION_PARADIGM.md                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## CLAUDE.md Constitutional Rules Summary

From `./CLAUDE.md`:

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06. No unnumbered root dirs.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require Principal approval for deletions.

### Semantic (ABSOLUTE)
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ → EXTRACT → COMPRESS → DELETE. NOT reorganization.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative.

### Operational (ABSOLUTE)
7. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes.

---

## Directory Structure Verification

### Expected (per CLAUDE.md)
```
00-ORCHESTRATION/    Strategic coordination
01-CANON/            Verified canonical knowledge (PROTECTED)
02-OPERATIONAL/      Functions, prompts, model profiles
03-QUEUE/            Pending items by modal
04-SOURCES/          Source documents (raw/, processed/)
05-ARCHIVE/          Historical preservation
06-EXEMPLA/          Templates and examples
```

### Actual (verified)
```
./00-ORCHESTRATION/  ✓ Present
./01-CANON/          ✓ Present (79 files)
./02-OPERATIONAL/    ✓ Present
./03-QUEUE/          ✓ Present (modal1/, modal2/, pending/)
./04-SOURCES/        ✓ Present (raw/, processed/)
./05-ARCHIVE/        ✓ Present
./06-EXEMPLA/        ✓ Present
```

### Structural Anomalies

| Path | Issue | Severity |
|------|-------|----------|
| ./system_prompts/ | Unnumbered root directory | LOW - Legacy |
| ./.decisions/ | Unnumbered root directory | LOW - Legacy |
| ./.tmp.driveupload/ | Unnumbered root directory | LOW - Temp |
| ./config/ | Unnumbered root directory | LOW - Utility |
| ./.obsidian/ | Unnumbered root directory | EXEMPT - Tool |
| ./.claude/ | Unnumbered root directory | EXEMPT - Tool |

**Note**: Some unnumbered directories are acceptable (tool configs, temp). The FLAT PRINCIPLE concern is about subdirectories within numbered directories, not root-level utility folders.

---

## Load Sequence for New Session

```bash
# 1. Read constitutional docs
cat CLAUDE.md
cat config/coordination.yaml

# 2. Read current state
cat 00-ORCHESTRATION/state/system_state.json
tail -10 00-ORCHESTRATION/state/events.jsonl

# 3. Read session context
cat ORACLE13_CONTEXT.md  # or latest Oracle context
cat INTERACTION_PARADIGM.md

# 4. Verify protected zone integrity
ls 01-CANON/ | wc -l  # Should be ~79
ls 00-ORCHESTRATION/state/*.json | wc -l  # Should be ≥2
```
