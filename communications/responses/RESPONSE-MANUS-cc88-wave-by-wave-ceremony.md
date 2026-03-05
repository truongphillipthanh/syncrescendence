# WAVE-BY-WAVE-CEREMONY

This document details the phased migration sequence, designed to minimize risk, prevent lockout, and ensure a clear rollback path at each stage. Each wave must be completed and verified before the next begins.

---

### Wave 0: Preparation & Audit

*   **Goal:** Establish a baseline and prepare for migration without making any state changes.
*   **Actions:**
    1.  **Account Verification:** Human operator logs into all four key accounts (`syncrescendence@gmail.com`, `truongphillipthanh@icloud.com`, `icloud.truongphillipthanh@gmail.com`, `truongphillipthanh@gmail.com`) to confirm access and MFA functionality.
    2.  **New Owner Prep:** Ensure `syncrescendence@gmail.com` has a strong, unique password and MFA enabled on Google.
    3.  **Break-Glass Test:** Confirm `truongphillipthanh@icloud.com` can access critical systems (e.g., log into GitHub).
    4.  **Billing Audit:** Human operator verifies that the GitHub organization's paid plan is correctly billed to `icloud.truongphillipthanh@gmail.com`.
    5.  **Manus Audit:** Manus runs a read-only audit of GitHub org/repo settings, Vercel/Doppler configs (if applicable) using a temporary token from the current owner.
*   **Gate:** All accounts are accessible, and the audit is complete. A full backup of critical configuration data is available.
*   **Anti-Lockout Check:** No changes are made in this wave. The check is to confirm that the designated break-glass account (`truongphillipthanh@icloud.com`) has verified access.

---

### Wave 1: Additive Changes & Identity Propagation

*   **Goal:** Introduce the new primary identity (`syncrescendence@gmail.com`) across all platforms without removing existing owners.
*   **Actions (Human Auth Window):**
    1.  **GitHub:** Invite `syncrescendence@gmail.com` as an *Owner* of the GitHub organization.
    2.  **Deployment/Secret Platforms:** Invite `syncrescendence@gmail.com` as an *Owner/Admin* to Vercel, Doppler, etc.
    3.  **Accept Invites:** Operator logs into `syncrescendence@gmail.com` and accepts all invitations.
*   **Gate:** `syncrescendence@gmail.com` is listed as an Owner/Admin on all relevant platforms alongside the legacy owner.
*   **Anti-Lockout Check:** The legacy owner (`truongphillipthanh@icloud.com`) must log in and confirm they still have full administrative privileges on all platforms.

---

### Wave 2: Ownership Transfers (The Human Window)

*   **Goal:** Atomically transfer the single point of truth (ownership) to the new primary identity.
*   **Actions (Human Auth Window):**
    1.  **GitHub Org Ownership:** From the `truongphillipthanh@icloud.com` account, transfer GitHub organization ownership to `syncrescendence@gmail.com`. This is a critical, irreversible (without cooperation) step.
    2.  **Google Cloud/Workspace:** Manually update ownership of any critical OAuth clients or service accounts to `syncrescendence@gmail.com`.
*   **Gate:** `syncrescendence@gmail.com` is the primary, designated *Owner* of the GitHub organization and any critical Google Cloud resources.
*   **Anti-Lockout Check:** `syncrescendence@gmail.com` must log in and perform an administrative action (e.g., change a repo setting) to confirm its new owner status. The legacy owner should now see a demoted role.

---

### Wave 3: Demotion & Repo Identity Cutover

*   **Goal:** Demote the legacy owner account and cut over the developer identity in the local repository.
*   **Actions:**
    1.  **Human Auth:** Demote `truongphillipthanh@icloud.com` from *Owner* to *Member* in the GitHub organization.
    2.  **Human Auth:** Operator generates a new GPG/SSH signing key associated with `syncrescendence@gmail.com`.
    3.  **Manus Run Batch:** Manus executes a script to update the local `git config` to use `syncrescendence@gmail.com` and the new signing key.
    4.  **Manus Run Batch:** Manus triggers a test commit/push to a test repository to verify the new commit signing.
*   **Gate:** The legacy owner account is a Member, not an Owner. New commits are successfully signed by and attributed to `syncrescendence@gmail.com`.
*   **Anti-Lockout Check:** The break-glass account (`truongphillipthanh@icloud.com`) should still be able to clone/pull from repos, but not perform administrative actions.

---

### Wave 4: Final Cleanup & Validation

*   **Goal:** Remove legacy accounts where they are no longer needed and perform a final system-wide validation.
*   **Actions:**
    1.  **Human Auth:** Remove `truongphillipthanh@icloud.com` from the GitHub organization entirely. It will remain the break-glass account but does not need to be a member.
    2.  **Human Auth:** Remove `truongphillipthanh@gmail.com` (personal secondary) from all platforms if it exists.
    3.  **Manus Run Batch:** Manus performs a final, comprehensive audit of all platforms to confirm the topology matches the target state.
*   **Gate:** All platforms report `syncrescendence@gmail.com` as the sole owner, with `icloud.truongphillipthanh@gmail.com` as the billing anchor. Legacy accounts are removed.
*   **Anti-Lockout Check:** Final check that `syncrescendence@gmail.com` has full control and that the break-glass account is secure and offline.
