# Implementation Plan: Bidirectional SSH Configuration

**Version:** 1.0.0
**Context:** Constellation communication between MBA (Ajna) and Mac mini (Constellation Hub).
**Status:** PROPOSED

## 1. Objectives
- Enable passwordless SSH from MBA (system@MacBook-Air) to Mac mini (home@M1-Mac-mini).
- Verify existing passwordless SSH from Mac mini to MBA.
- Harden SSH configuration for LAN security.

## 2. Execution Steps

### Step 1: Generate Key on MBA (if not exists)
On **MacBook Air**:
```bash
ssh-keygen -t ed25519 -C "ajna@mba-to-mini" -f ~/.ssh/id_ed25519_ajna
```

### Step 2: Transfer Public Key to Mac mini
On **MacBook Air**:
```bash
ssh-copy-id -i ~/.ssh/id_ed25519_ajna.pub home@<MAC_MINI_IP>
```

### Step 3: Configure `~/.ssh/config` on MBA
Add to `~/.ssh/config` on **MacBook Air**:
```text
Host mini
    HostName <MAC_MINI_IP>
    User home
    IdentityFile ~/.ssh/id_ed25519_ajna
    IdentitiesOnly yes
```

### Step 4: Verify Bidirectional Connectivity
From **MBA**: `ssh mini "hostname"` (Should return `M1-Mac-mini`)
From **Mac mini**: `ssh ajna "hostname"` (Should return `MacBook-Air`)

## 3. Security Hardening (Both Nodes)

1. **Permissions:**
   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/id_ed25519*
   ```

2. **Disable Password Auth (Optional but Recommended for LAN):**
   In `/etc/ssh/sshd_config`:
   ```text
   PasswordAuthentication no
   ChallengeResponseAuthentication no
   ```
   *Note: Ensure key auth works before doing this.*

## 4. Verification Check
| Source | Target | Method | Expected Result |
|--------|--------|--------|-----------------|
| MBA | Mac mini | `ssh mini` | Immediate shell access |
| Mac mini | MBA | `ssh ajna` | Immediate shell access |
| External | Either | `nmap` | Port 22 open, Stealth Mode bypassable for ICMP (if configured) |

## 5. Metadata
- **Identity Files:**
  - MBA: `id_ed25519_ajna`
  - Mac mini: `id_ed25519_psyche_to_ajna` (Existing)
