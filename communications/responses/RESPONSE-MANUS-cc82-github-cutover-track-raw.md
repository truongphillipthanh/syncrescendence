# GITHUB-CUTOVER-TRACK

**Project:** Syncrescendence Account Centralization — CC82
**Scope:** GitHub organization ownership, repository ownership, billing, and control plane validation
**Prepared:** 2026-03-05

---

## Overview

This document provides the detailed cutover procedure for the GitHub surface. The migration covers three distinct ownership surfaces: the GitHub **organization** (roles, billing, settings), individual **repositories** that may be owned by the personal account rather than the organization, and the **GitHub Actions / CI/CD** control plane (secrets, tokens, and environment variables tied to the legacy account).

GitHub's ownership model is well-documented and fully reversible. The process is UI-driven for the final ownership handoff, with supporting steps that can be scripted via the GitHub REST API.

---

## 1. Pre-Migration Checklist

Before executing any ownership mutation, confirm all of the following:

The `syncrescendence@gmail.com` account must have an active GitHub account. Confirm the username associated with this email at [github.com/settings/emails](https://github.com/settings/emails). The account must already be an active member of the Syncrescendence GitHub organization (not merely invited). Two-factor authentication (2FA) must be enabled on the `syncrescendence@gmail.com` GitHub account, as GitHub requires 2FA for organization owners. [^1]

Confirm that the current owner (`truongphillipthanh@icloud.com`) can log in and access **Organization Settings**. Run an audit of all repositories to identify which are owned by the organization versus the personal account. Export the current billing information for reference.

---

## 2. Organization Owner Role Transfer

**Preconditions**

`syncrescendence@gmail.com` must be a member of the organization. 2FA must be enabled on the new owner's account.

**Owner Mutation Step**

Step 1: Log in to GitHub as `truongphillipthanh@icloud.com`. Navigate to the organization page and select **Settings → Members**.

Step 2: Locate `syncrescendence@gmail.com` in the member list. Click the role dropdown next to the account and select **Owner**. [^1]

Step 3: Log in as `syncrescendence@gmail.com` and navigate to **Organization Settings** to confirm Owner access.

Step 4: As `syncrescendence@gmail.com`, navigate to **Settings → Billing & plans**. Update the billing email to `syncrescendence@gmail.com` and update the payment method. [^1]

> **Critical:** GitHub explicitly warns that removing yourself from the organization does **not** update billing information. The new owner must update billing separately before the old owner removes themselves.

Step 5: Log back in as `truongphillipthanh@icloud.com`. Navigate to **Organization Settings → Members** and select **Leave organization** to remove the legacy account.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com`. Confirm the account is the sole Owner in the Members list. Navigate to **Settings → Billing** and confirm the billing email and payment method are correct. Attempt to create a test team and invite a member to validate full Owner permissions. Confirm that no other accounts hold the Owner role unless intentionally retained.

**Rollback Step**

If the transfer produces an unacceptable state, the new owner (`syncrescendence@gmail.com`) can re-invite `truongphillipthanh@icloud.com` to the organization and assign the Owner role. The original owner can then update billing back to the original payment method. The new owner can then leave the organization.

---

## 3. Repository Ownership Transfer

If any repositories are owned by the personal account `truongphillipthanh@icloud.com` rather than the Syncrescendence organization, each must be transferred individually.

**Preconditions**

Run the following GitHub API query to enumerate all repositories owned by `truongphillipthanh@icloud.com` that are not already in the organization:

```
GET https://api.github.com/users/truongphillipthanh/repos?type=owner&per_page=100
```

For each repository, confirm whether it should be transferred to the organization or to the `syncrescendence@gmail.com` personal account.

**Owner Mutation Step**

For each repository to be transferred:

1. Navigate to the repository on GitHub.com.
2. Select **Settings → General → Danger Zone → Transfer**.
3. Type the repository name to confirm, then specify the destination (the Syncrescendence organization or `syncrescendence@gmail.com`). [^1]
4. Confirm the transfer. The repository will be moved immediately.

> **Note:** Transferring a repository to an organization requires the transferring account to be a member of the destination organization. All collaborators, branch protections, webhooks, and GitHub Actions workflows are preserved. Deploy keys and OAuth tokens may need to be reauthorized.

**Post-Verification Step**

Confirm the repository appears in the destination organization's repository list. Verify all collaborators, branch protections, and webhooks are intact. Run the CI/CD pipeline to confirm GitHub Actions workflows execute correctly.

**Rollback Step**

The repository can be transferred back to the original account using the same Danger Zone transfer flow.

---

## 4. GitHub Actions and CI/CD Control Plane

After ownership transfer, all GitHub Actions secrets, environment variables, and tokens that reference `truongphillipthanh@icloud.com` must be audited and updated.

**Audit Step**

Navigate to **Organization Settings → Secrets and variables → Actions** and enumerate all organization-level secrets. For each repository, navigate to **Repository Settings → Secrets and variables → Actions** and enumerate repository-level secrets. Identify any secrets that contain tokens or credentials tied to the legacy account.

**Mutation Step**

For each secret tied to the legacy account: generate a new token or credential under the `syncrescendence@gmail.com` account, update the secret value in GitHub, and verify that the associated workflow runs successfully.

For any Personal Access Tokens (PATs) used in workflows: revoke the PAT associated with `truongphillipthanh@icloud.com` and generate a new PAT under `syncrescendence@gmail.com`. Update all consumers of the old PAT.

**Post-Verification Step**

Trigger all affected GitHub Actions workflows and confirm they complete successfully. Review the Actions run logs for any authentication errors.

---

## 5. Billing and Subscription Validation

After the ownership transfer, the following billing validations must be completed:

The billing email must be updated to `syncrescendence@gmail.com` in **Organization Settings → Billing & plans → Billing contact**. The payment method (credit card or PayPal) must be updated to a payment method controlled by `syncrescendence@gmail.com`. Confirm the current plan (Free, Team, or Enterprise) is correct and that the seat count reflects the current membership. Confirm that any GitHub Marketplace app subscriptions are correctly associated with the new billing account.

---

## References

[^1]: [Transferring organization ownership — GitHub Docs](https://docs.github.com/en/organizations/managing-organization-settings/transferring-organization-ownership)
[^2]: [Roles in an organization — GitHub Docs](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
[^3]: [Managing your payment and billing information — GitHub Docs](https://docs.github.com/billing/managing-your-billing/managing-your-payment-and-billing-information)
[^4]: [Changing your primary email address — GitHub Docs](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/changing-your-primary-email-address)
