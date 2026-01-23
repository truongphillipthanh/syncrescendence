# Structural Stabilization Procedure
## Defrag and Constitutional Compliance Runbook

**Version**: 1.0.0
**Created**: 2026-01-18
**Authority**: STRUCTURAL_STABILIZATION_PASS
**Status**: Constitutional Reference

---

## Purpose

This document defines the canonical procedure for maintaining structural integrity of the Syncrescendence repository. It covers:

1. Constitutional rules for repository structure
2. Defrag execution procedure (preflight, apply, verify, rollback)
3. Casing invariant enforcement (`OUTGOING/` vs `outgoing/`)
4. Continuation packet creation and storage

---

## Constitutional Summary

Full rules in [CLAUDE.md](../../CLAUDE.md). Key structural rules:

| Rule | Summary |
|------|---------|
| **#1 FLAT PRINCIPLE** | Zones are flat; use prefixes (ARCH-, DYN-, REF-) not subdirectories |
| **#2 NUMBERED DIRECTORIES** | Root is zones 00-06 + sanctioned exceptions only |
| **#4 EXCHANGE DIR INVARIANT** | `-OUTGOING/` and `-INBOX/` are canonical. Legacy `OUTGOING/` and `outgoing/` are prohibited |
| **#11 PORTABLE SCRIPTS** | Use `git rev-parse --show-toplevel`, no hardcoded paths |

### Root Exceptions (Sanctioned)

| Item | Type | Purpose |
|------|------|---------|
| `CLAUDE.md` | File | Constitutional rules |
| `COCKPIT.md` | File | Navigation contract |
| `Makefile` | File | Build commands |
| `-OUTGOING/` | Directory | Export staging, reinit capsules |
| `-INBOX/` | Directory | Incoming artifacts from external platforms |

**Everything else at root is a violation.** Legacy `OUTGOING/` and lowercase `outgoing/` are PROHIBITED.

---

## Defrag Procedure

### When to Run Defrag

Run defrag when:
- Files accumulate at repository root
- Directories outside 00-06 appear (except `OUTGOING/`)
- `structural_verify.sh` reports errors
- After major refactoring work

### Pre-Flight Checklist

Before running defrag:

```bash
# 1. Check current state
cd $(git rev-parse --show-toplevel)
./00-ORCHESTRATION/scripts/structural_verify.sh

# 2. Verify no lowercase outgoing/
ls -1 | grep -i outgoing  # Should show OUTGOING only

# 3. Create backup
git stash push -u -m "pre-defrag-$(date +%Y%m%d_%H%M%S)"

# 4. Review what will change
git status
ls *.md 2>/dev/null | grep -v CLAUDE | grep -v COCKPIT
```

### Apply Procedure

```bash
# 1. Create approval file
echo "I_APPROVE_DEFRAG_APPLY" > APPLY_DEFRAG_APPROVAL.txt

# 2. Run hardened defrag script
./00-ORCHESTRATION/scripts/defrag_apply_hardened.sh

# 3. Verify success
./00-ORCHESTRATION/scripts/structural_verify.sh

# 4. Review changes
git status
git diff --cached

# 5. Commit
git add -A
git commit -m "chore(defrag): structural stabilization pass"

# 6. Clean up
rm APPLY_DEFRAG_APPROVAL.txt
```

### Verify Procedure

After any defrag or structural change:

```bash
./00-ORCHESTRATION/scripts/structural_verify.sh
```

Expected output: All checks should pass or show only warnings.

### Rollback Procedure

If defrag fails or causes issues:

```bash
# Option 1: Restore from stash
git stash list
git stash pop

# Option 2: Reset to pre-defrag commit
git log --oneline -5
git reset --hard <commit-before-defrag>

# Option 3: Selective undo via git checkout
git checkout HEAD~1 -- <specific-file>
```

---

## Exchange Directory Invariant Enforcement

### The Rule

`-OUTGOING/` and `-INBOX/` (dash-prefixed) are the only valid exchange directories. Legacy `OUTGOING/` and lowercase `outgoing/` are constitutional violations.

### Detection

```bash
# Check for legacy forms (should return nothing)
ls -1 | grep -E "^(OUTGOING|outgoing)$"

# Verify canonical forms exist
ls -1 | grep "^-OUTGOING$"
ls -1 | grep "^-INBOX$"

# Check for legacy references in live docs
grep -rn "OUTGOING/" --include="*.md" --include="*.sh" | grep -v "\-OUTGOING/"
```

### Prevention

The hardened defrag script checks for legacy forms and fails fast if found:

```bash
LEGACY_OUTGOING=$(ls -1 "$REPO_ROOT" | grep -E "^(OUTGOING|outgoing)$" || true)
if [ -n "$LEGACY_OUTGOING" ]; then
    error "VIOLATION: legacy '$LEGACY_OUTGOING/' exists. Use -OUTGOING/ instead"
fi
```

### Remediation

If legacy `OUTGOING/` exists:

```bash
# 1. Check for legacy forms
ls -1 | grep -E "^(OUTGOING|outgoing)$"

# 2. Migrate to canonical form
git mv OUTGOING -OUTGOING

# 3. Ensure -INBOX/ exists
mkdir -p -INBOX
```

---

## Continuation Packets

### Purpose

Continuation (CONT) packets enable session handoff between platforms or across context resets.

### Schema

See `00-ORCHESTRATION/schemas/packet_protocol.json` for the `continuation` packet type.

Required fields:
- `id`: CONT-YYYYMMDD-NNN
- `timestamp`: ISO 8601
- `source_platform`: originating platform
- `target_platform`: destination platform
- `session_context`: Oracle/Blitzkrieg state
- `pending_tasks`: list of action items
- `critical_state`: files to read, decisions pending, warnings

### Template

Use `06-EXEMPLA/TEMPLATE-CONTINUATION_PACKET.json` as starting point.

### Storage

Store continuation packets in:
- `-OUTGOING/` for cross-platform handoffs (e.g., `-OUTGOING/YYYYMMDD-deviser_reinit/`)
- `-INBOX/` for incoming artifacts from external platforms
- `00-ORCHESTRATION/blackboard/continuation/` for internal tracking

### Naming Convention

Format: `CONT-YYYYMMDD-NNN.json`

Example: `CONT-20260118-001.json`

### Migration from YAML-ish Format

Prior CONT capsules used markdown with YAML-like structure. Convert to JSON:

| Old Format | New JSON Field |
|------------|----------------|
| Oracle/Blitzkrieg header | `session_context` |
| Action items list | `pending_tasks` |
| File references | `attachments` |
| SHA256 checksums | `hash_manifest` |

---

## Acceptance Checklist

Run these commands to verify structural compliance:

```bash
# 1. No legacy OUTGOING/ or lowercase outgoing/ at root
ls -1 | grep -E "^(OUTGOING|outgoing)$" && echo "FAIL" || echo "PASS"

# 2. -OUTGOING/ and -INBOX/ exist
ls -1 | grep "^-OUTGOING$" && ls -1 | grep "^-INBOX$" && echo "PASS" || echo "FAIL"

# 3. COCKPIT paths valid
bash 00-ORCHESTRATION/scripts/structural_verify.sh | grep "COCKPIT Paths"

# 4. No orphan files at root
ls *.md 2>/dev/null | grep -v CLAUDE | grep -v COCKPIT | wc -l

# 5. No forbidden root directories
ls -d */ | grep -v "^0[0-6]-" | grep -v "^-OUTGOING" | grep -v "^-INBOX"

# 6. Continuation packet schema valid
grep -q '"continuation"' 00-ORCHESTRATION/schemas/packet_protocol.json && echo "PASS"
```

Or simply run:

```bash
./00-ORCHESTRATION/scripts/structural_verify.sh
```

---

## Quick Reference

### Scripts

| Script | Purpose |
|--------|---------|
| `00-ORCHESTRATION/scripts/structural_verify.sh` | Validate constitutional compliance |
| `00-ORCHESTRATION/scripts/defrag_apply_hardened.sh` | Execute defrag with safety checks |

### Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Constitutional rules (v2.2.0) |
| `COCKPIT.md` | Navigation contract |
| `00-ORCHESTRATION/schemas/packet_protocol.json` | Packet schema (v1.1.0) |
| `06-EXEMPLA/TEMPLATE-CONTINUATION_PACKET.json` | CONT packet template |

### Common Issues

| Issue | Solution |
|-------|----------|
| Legacy `OUTGOING/` or `outgoing/` | Migrate to `-OUTGOING/`: `git mv OUTGOING -OUTGOING` |
| Missing `-INBOX/` | Create: `mkdir -p -INBOX` |
| config/ references after defrag | Update to `02-ENGINE/coordination.yaml` |
| Orphan files at root | Move to appropriate zone per CLAUDE.md |
| Broken COCKPIT paths | Update paths after any structural change |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-18 | Initial formalization of stabilization procedure |
| 2.0.0 | 2026-01-18 | Migration to -OUTGOING/-INBOX canonical form |

---

*This document is a constitutional reference. Modifications require Principal approval.*
