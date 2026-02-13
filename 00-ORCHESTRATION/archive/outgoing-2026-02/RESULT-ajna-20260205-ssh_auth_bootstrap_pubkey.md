# RESULT — TASK-20260205-ssh_auth_bootstrap_pubkey (Ajna)

Date: 2026-02-05 (America/Los_Angeles)
Host: ajna-M1-Mac-mini (user `home`)
Target: Psyche laptop (user `system`)

## 1) Existing SSH keys on Ajna

`~/.ssh` contents (high-level):
- `id_ed25519` (+ `.pub`)
- `id_ed25519_ajna_to_psyche` (+ `.pub`)
- `config`, `known_hosts`, etc.

### Candidate key chosen: dedicated Ajna→Psyche key

File:
- `~/.ssh/id_ed25519_ajna_to_psyche`

Fingerprint:
```
256 SHA256:XJeE+B/803pJG/rwsfSUm3eHxI9oSrePBVDwYbtCc64 ajna->psyche (ED25519)
```

Public key line (install this into Psyche `system` user’s `~/.ssh/authorized_keys` if needed):

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPfROrVgD6wKd7WhFMeDc1dsKGjziDrk5g0k+df0lm1S ajna->psyche
```

## 2) ~/.ssh/config stanza for `psyche`

Intended stanza (now applied on Ajna):

```ssh-config
Host psyche
  HostName Lisas-MacBook-Air.local
  User system
  IdentityFile ~/.ssh/id_ed25519_ajna_to_psyche
  IdentitiesOnly yes
  StrictHostKeyChecking yes
  ServerAliveInterval 20
  ServerAliveCountMax 2
```

## 3) Connectivity test

Command:
```bash
ssh -o BatchMode=yes -o ConnectTimeout=10 psyche "echo OK_PSY && hostname"
```

Output:
```text
OK_PSY
Lisas-MacBook-Air.local
```

## Notes / safety
- No private key material printed or copied.
- Only fingerprints and public keys are included above.
