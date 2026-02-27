# RESULT — TASK-20260205-outfitment_sync_and_smoketest_v2_ssh (Ajna)

Status: **STOPPED in Phase 3 (SSH auth failure)** per STOP CONDITION.
Date: 2026-02-05 (America/Los_Angeles)
Host: ajna-M1-Mac-mini (user `home`)

## PHASE 0 — Pull latest repo

`git pull --rebase` initially failed due to unstaged changes in the repo working tree.
I stashed local changes to proceed:

```bash
git stash push -u -m "ajna: WIP before outfitment_sync_and_smoketest_v2_ssh"
```

Then:

```bash
git pull --rebase
# output: Already up to date.
```

## PHASE 1 — Establish Psyche SSH reachability (discover host)

### Host resolution
Commands (per task):
- `dscacheutil -q host -a name <hostname>`

Results:
- `Lisas-MacBook-Air.local` resolves to `192.168.4.176`
- `lisas-macbook-air.local` also resolves to `192.168.4.176`

Note: ICMP ping returned 100% packet loss, but ARP shows `192.168.4.176` present on LAN (en1).

## PHASE 2 — Pin host key safely

Candidate host used for pinning: `Lisas-MacBook-Air.local`

### Key scan
```bash
ssh-keyscan -T 5 -t rsa,ecdsa,ed25519 Lisas-MacBook-Air.local | tee /tmp/psyche.hostkeys
```

### Fingerprints (audit)
```bash
ssh-keygen -lf /tmp/psyche.hostkeys
```
Output:
- RSA (3072): `SHA256:cyKOMAR/LtfUtO9tJFrpCOCLanCGjdv/nHslgTt0uIs`
- ECDSA (256): `SHA256:0zfHkgu/uughGWufVf/RD9XFeU56aHkDskMgnhtsNW4`
- ED25519 (256): `SHA256:ayE+iSDoL59kkIqGnc5ss5uC/4xI/HiCBc/Ug9/RRmM`

### known_hosts update
Idempotent add:
```bash
ssh-keygen -R Lisas-MacBook-Air.local || true
ssh-keygen -R lisas-macbook-air.local || true
cat /tmp/psyche.hostkeys >> ~/.ssh/known_hosts
```

## PHASE 3 — Create stable SSH alias + test

### ~/.ssh/config
Created/updated `Host psyche`:

```ssh-config
Host psyche
  HostName Lisas-MacBook-Air.local
  User system
  IdentitiesOnly yes
  StrictHostKeyChecking yes
  ServerAliveInterval 20
  ServerAliveCountMax 2
```

Important fix: there was an existing multi-pattern alias line:

```ssh-config
Host macbook-air "MacBook Air" psyche
```

That caused `psyche` to inherit the wrong `HostName` (`lisas-macbook-air-1`). I removed the `psyche` token from that Host patterns line so `Host psyche` resolves correctly.

### ssh test (STOP CONDITION HIT)
Command:
```bash
ssh -o BatchMode=yes -o ConnectTimeout=10 psyche "echo OK_PSY && hostname"
```
Exact stderr:
```text
system@lisas-macbook-air.local: Permission denied (publickey,password,keyboard-interactive).
```

## STOPPED

Per instructions, I did **not** proceed to:
- syncing `~/.openclaw/workspace/skills`
- running doctor fixes
- gateway / smoke agent test

## Next step to unblock

This is an SSH authentication/authorization issue. To proceed, we need one of:
- the correct private key installed on Ajna (and corresponding authorized_keys on Psyche), OR
- an updated `~/.ssh/config` for `psyche` specifying the correct `IdentityFile`, OR
- confirm Psyche allows `system` login from Ajna.

I did **not** attempt password guessing or bypass host-key checking.
