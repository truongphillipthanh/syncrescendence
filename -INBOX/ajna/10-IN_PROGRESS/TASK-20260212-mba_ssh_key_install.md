# TASK-20260212-mba_ssh_key_install

**From**: Commander (Claude Code Opus)
**To**: Ajna (OpenClaw Opus 4.5)
**Reply-To**: commander
**Issued**: 2026-02-12 17:03:01
**Fingerprint**: f291879
**Kind**: TASK
**Priority**: P1
**Status**: IN_PROGRESS
**Kanban**: IN_PROGRESS
**Claimed-By**: ajna-M1-Mac-mini
**Claimed-At**: 2026-02-13T01:03:02Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/ajna/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Install Mac mini SSH public key into MBA authorized_keys for cross-machine access.

Required action:
1. Ensure ~/.ssh/ directory exists: mkdir -p ~/.ssh && chmod 700 ~/.ssh
2. Add this public key to ~/.ssh/authorized_keys:
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDU68F335rySyExhQCe2398MQ4Yp3xndgSq2MXbSpK42 truongphillithanh@icloud.com
3. chmod 600 ~/.ssh/authorized_keys
4. Verify Remote Login is enabled: System Settings > General > Sharing > Remote Login = ON
5. Smoke test: confirm sshd is listening on port 22

Acceptance criteria:
- authorized_keys contains the key
- sshd running and accepting connections
- Report: hostname, whoami, sshd status

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/ajna/RESULTS/RESULT-ajna-20260212-mba_ssh_key_install.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: mba_ssh_key_install complete" && git push`
