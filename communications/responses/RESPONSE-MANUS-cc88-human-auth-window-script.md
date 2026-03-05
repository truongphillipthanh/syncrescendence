# HUMAN-AUTH-WINDOW-SCRIPT

This script provides the exact, step-by-step instructions for the human operator to execute during the required manual intervention windows. Follow these steps precisely. Each action corresponds to a wave in the `WAVE-BY-WAVE-CEREMONY`.

**Operator:** You will need a password manager and your MFA device.

---

### Wave 0: Preparation & Audit

**Objective:** Verify access to all accounts and confirm current settings before making changes.

1.  **Verify `syncrescendence@gmail.com`:**
    *   Open a new incognito browser window.
    *   Navigate to `https://gmail.com`.
    *   Log in with the `syncrescendence@gmail.com` credentials.
    *   Confirm you can access the inbox.
    *   Navigate to Google Account security settings and confirm MFA is active.

2.  **Verify `truongphillipthanh@icloud.com` (Legacy Break-Glass):**
    *   Open a new incognito browser window.
    *   Navigate to `https://www.icloud.com/`.
    *   Log in with the `truongphillipthanh@icloud.com` credentials.
    *   Confirm you can access the account.
    *   In a separate tab, navigate to `https://github.com/login` and log in using this account to confirm it has access.

3.  **Verify `icloud.truongphillipthanh@gmail.com` (Billing Anchor):**
    *   Open a new incognito browser window.
    *   Navigate to `https://gmail.com`.
    *   Log in with the `icloud.truongphillipthanh@gmail.com` credentials.
    *   Confirm you can access the inbox.

4.  **Verify `truongphillipthanh@gmail.com` (Optional Secondary):**
    *   Log in and confirm access as above.

5.  **Audit GitHub Billing:**
    *   While logged into GitHub as `truongphillipthanh@icloud.com`, go to your organization's settings.
    *   Click on "Billing and plans".
    *   Verify that the subscription is active and that the billing email is `icloud.truongphillipthanh@gmail.com`.

---

### Wave 1: Additive Changes & Identity Propagation

**Objective:** Add the new owner account to all platforms.

1.  **Invite New GitHub Owner:**
    *   While logged into GitHub as `truongphillipthanh@icloud.com`, go to your organization's "People" settings.
    *   Click "Invite member".
    *   Enter `syncrescendence@gmail.com` and select the **Owner** role.
    *   Send the invitation.

2.  **Invite Owner on Other Platforms (Vercel, Doppler, etc.):**
    *   Log into each respective platform as the current owner.
    *   Navigate to the team/member settings.
    *   Invite `syncrescendence@gmail.com` with the **Owner** or **Admin** role.

3.  **Accept All Invitations:**
    *   Log into the `syncrescendence@gmail.com` Gmail account.
    *   Find the invitation emails from GitHub and all other platforms.
    *   Click the link in each email to accept the invitation.
    *   Verify on each platform that `syncrescendence@gmail.com` is now listed as an Owner.

---

### Wave 2: Ownership Transfers

**Objective:** Make the new account the official owner.

1.  **Transfer GitHub Organization Ownership:**
    *   Log into GitHub as `truongphillipthanh@icloud.com`.
    *   Go to the organization's settings.
    *   Click the "Transfer ownership" button.
    *   Follow the prompts to transfer the organization to `syncrescendence@gmail.com`.
    *   You will need to type the organization name and confirm with your password/MFA.
    *   **This is the most critical step. Proceed with caution.**

2.  **Confirm New Ownership:**
    *   Log out of GitHub.
    *   Log back in as `syncrescendence@gmail.com`.
    *   Go to the organization settings and confirm you are the sole owner.

---

### Wave 3: Demotion & Repo Identity Cutover

**Objective:** Demote the legacy account and switch to the new commit identity.

1.  **Demote Legacy GitHub Owner:**
    *   While logged in as `syncrescendence@gmail.com`, go to the organization's "People" settings.
    *   Find the `truongphillipthanh@icloud.com` member.
    *   Change their role from **Owner** to **Member**.

2.  **Generate New Signing Key:**
    *   On your local development machine, generate a new GPG or SSH key.
    *   Associate this new key with the `syncrescendence@gmail.com` email address.
    *   Add the new public key to your `syncrescendence@gmail.com` GitHub account.

---

### Wave 4: Final Cleanup

**Objective:** Remove legacy accounts from the organization.

1.  **Remove Legacy Member:**
    *   While logged in as `syncrescendence@gmail.com`, go to the organization's "People" settings.
    *   Find the `truongphillipthanh@icloud.com` member.
    *   Remove them from the organization.

2.  **Remove Optional Secondary Account:**
    *   If `truongphillipthanh@gmail.com` is a member of the organization or other platforms, remove it now.
