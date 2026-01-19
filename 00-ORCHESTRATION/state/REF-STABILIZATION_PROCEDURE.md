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
| **#4 CASING INVARIANT** | `OUTGOING/` (uppercase) is canonical. `outgoing/` is prohibited |
| **#11 PORTABLE SCRIPTS** | Use `git rev-parse --show-toplevel`, no hardcoded paths |

### Root Exceptions (Sanctioned)

| Item | Type | Purpose |
|------|------|---------|
| `CLAUDE.md` | File | Constitutional rules |
| `COCKPIT.md` | File | Navigation contract |
| `Makefile` | File | Build commands |
| `OUTGOING/` | Directory | Export staging |

**Everything else at root is a violation.**

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

## Casing Invariant Enforcement

### The Rule

`OUTGOING/` (uppercase) is the only valid casing. `outgoing/` is a constitutional violation.

### Detection

```bash
# Check actual casing (works on case-insensitive filesystems)
ls -1 | grep -i "^outgoing$"

# Check for lowercase references in docs
grep -rn "outgoing/" --include="*.md" --include="*.sh" | grep -v "OUTGOING/"
```

### Prevention

The hardened defrag script checks for lowercase `outgoing/` and fails fast if found:

```bash
ACTUAL_OUTGOING=$(ls -1 "$REPO_ROOT" | grep -i "^outgoing$" || true)
if [ -n "$ACTUAL_OUTGOING" ] && [ "$ACTUAL_OUTGOING" != "OUTGOING" ]; then
    error "VIOLATION: lowercase '$ACTUAL_OUTGOING/' exists"
fi
```

### Remediation

If lowercase `outgoing/` exists:

```bash
# 1. Check actual casing
ls -1 | grep -i outgoing

# 2. Rename to correct casing
git mv outgoing OUTGOING

# 3. If both exist (shouldn't happen on case-insensitive FS), merge manually
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
- `OUTGOING/` for cross-platform handoffs (e.g., `OUTGOING/CHATGPT_REINIT_CONT_CAPSULE_YYYYMMDD_HHMM/`)
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
# 1. No lowercase outgoing/ at root
ls -1 | grep -i "^outgoing$" | grep -v OUTGOING && echo "FAIL" || echo "PASS"

# 2. COCKPIT paths valid
bash 00-ORCHESTRATION/scripts/structural_verify.sh | grep "COCKPIT Paths"

# 3. No orphan files at root
ls *.md 2>/dev/null | grep -v CLAUDE | grep -v COCKPIT | wc -l

# 4. No forbidden root directories
ls -d */ | grep -v "^0[0-6]-" | grep -v "^OUTGOING"

# 5. Continuation packet schema valid
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
| lowercase `outgoing/` | Rename to `OUTGOING/` |
| config/ references after defrag | Update to `02-OPERATIONAL/coordination.yaml` |
| Orphan files at root | Move to appropriate zone per CLAUDE.md |
| Broken COCKPIT paths | Update paths after any structural change |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-18 | Initial formalization of stabilization procedure |

---

*This document is a constitutional reference. Modifications require Principal approval.*
