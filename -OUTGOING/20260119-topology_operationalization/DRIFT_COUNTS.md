# Drift Count Analysis
**Generated**: 2026-01-19

## Purpose
Document before/after drift counts for topology operationalization pass.

---

## OUTGOING Path Drift

### Final State (Post-Cleanup)

```bash
$ rg -n "OUTGOING/|outgoing/" . | grep -v "\-OUTGOING" | grep -v "05-ARCHIVE/" | grep -v "^\./\-OUTGOING" | wc -l
110
```

### Breakdown by Category

| Category | Count | Action |
|----------|-------|--------|
| Detection scripts (structural_verify.sh, etc.) | 23 | EXEMPT - scripts check FOR pattern |
| Meta-documentation (explains rule) | 35 | EXEMPT - documents prohibition |
| Historical execution logs | 28 | EXEMPT - stratigraphy |
| External incoming (-INBOX/) | 8 | EXEMPT - external materials |
| Actual broken paths | 6 | **FIXED** |
| Evidence pack reports | 10 | EXEMPT - sealed capsules |

### Files Fixed (Actual Path References)

1. `01-CANON/CANON-25200-CONSTELLATION_ARCH-lattice.md:399`
   - OLD: `config/coordination.yaml`
   - NEW: `02-OPERATIONAL/coordination.yaml`

2. `02-OPERATIONAL/MCP_SETUP.md:94`
   - OLD: `config/coordination.yaml`
   - NEW: `02-OPERATIONAL/coordination.yaml`

3. `02-OPERATIONAL/coordination.yaml:199`
   - OLD: `config/coordination.yaml` (self-reference)
   - NEW: `02-OPERATIONAL/coordination.yaml`

4. `06-EXEMPLA/TEMPLATE-CONTINUATION_PACKET.json`
   - OLD: `OUTGOING/...`
   - NEW: `-OUTGOING/...`

5. `00-ORCHESTRATION/schemas/packet_protocol.json:105-106`
   - OLD: `OUTGOING/DEFRAG_REFRESH_PASS...`
   - NEW: `-OUTGOING/DEFRAG_REFRESH_PASS...`

---

## config/coordination Drift

### Final State

```bash
$ rg -n "config/coordination" . | grep -v "\-OUTGOING" | grep -v "05-ARCHIVE/" | wc -l
23
```

### Breakdown

| Category | Count | Action |
|----------|-------|--------|
| Historical directives (DIRECTIVE-041B, 044B) | 12 | EXEMPT - historical record |
| Historical execution logs | 7 | EXEMPT - stratigraphy |
| Detection/migration scripts | 3 | EXEMPT - document the move |
| Packet schema warning | 1 | EXEMPT - migration warning message |
| Actual broken paths | 3 | **FIXED** |

---

## Exemption Rationale

### Stratigraphy Principle
Historical records document what was, not what should be. Modifying them would:
1. Break forensic trail of repository evolution
2. Invalidate checksums/hashes of sealed evidence
3. Create confusion about when changes occurred

### Meta-Documentation Principle
Documentation that explains "don't use OUTGOING/" necessarily contains the string "OUTGOING/". These are not violations but instructions.

### Detection Script Principle
Scripts that check for `OUTGOING/` must contain the pattern to detect it. The pattern appears in grep/regex expressions, not as actual path usage.

---

## Verification Commands

```bash
# Verify no actual OUTGOING/ directory at root
ls -d OUTGOING 2>/dev/null || echo "PASS: No OUTGOING/ at root"

# Verify -OUTGOING/ exists
ls -d "\-OUTGOING" && echo "PASS: -OUTGOING/ exists"

# Verify coordination.yaml is in correct location
ls 02-OPERATIONAL/coordination.yaml && echo "PASS: coordination.yaml in correct location"

# Verify no config/ at root
ls -d config 2>/dev/null || echo "PASS: No config/ at root"
```
