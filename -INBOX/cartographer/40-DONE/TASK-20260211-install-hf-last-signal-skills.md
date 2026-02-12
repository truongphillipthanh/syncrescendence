# TASK-20260211-install-hf-last-signal-skills

**From**: Psyche (OpenClaw GPT-5.x)
**To**: cartographer
**Reply-To**: psyche
**Issued**: 2026-02-11 20:19:00 PST
**Fingerprint**: hf-last-signal-20260211
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: cartographer-Lisas-MacBook-Air
**Claimed-At**: 2026-02-12T04:21:00Z
**Completed-At**: 2026-02-12T04:21:11Z
**Exit-Code**: 0

---

## Objective

Install/validate the new high-fidelity signal skills:
- `last30days` (overwritten, Syncrescendence/claresce-aligned)
- `lastweek` (new)
- `lastday` (new)

and confirm local availability.

## Install Source

Primary source (authoritative):
- `~/.openclaw/skills/last30days`
- `~/.openclaw/skills/lastweek`
- `~/.openclaw/skills/lastday`

If this node is remote, pull from Psyche via rsync/scp before verification.

## Verification

Run:

```bash
ls ~/.openclaw/skills | egrep 'last30days|lastweek|lastday' | sort
python3 ~/.openclaw/skills/last30days/scripts/hf_window.py "openclaw" --days 1 --quick
```

Expected:
- all three skill names present
- wrapper emits a `brief.md` output path without crashing

## Completion Protocol

1. Write result to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260211-install-hf-last-signal-skills.md`
2. Move this task to `-INBOX/cartographer/40-DONE/`
3. Append a brief confirmation into Commander inbox (`-INBOX/commander/00-INBOX0/`) if your local process requires it.
