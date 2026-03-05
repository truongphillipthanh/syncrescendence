# COMPLETION-DEFINITION

This document provides the clear and unambiguous criteria for considering the migration of each platform, and the overall migration, complete. Completion is defined by the target account topology being fully realized and verified.

### Per-Platform Completion Criteria

| Platform | Completion Criteria | Primary Evidence |
|---|---|---|
| **GitHub (Organization)** | `syncrescendence@gmail.com` is the sole owner of the organization. The legacy owner and secondary accounts are removed. | Screenshot of the GitHub organization's "People" page showing `syncrescendence@gmail.com` as the only owner. |
| **GitHub (Billing)** | The organization's subscription is active and billing is managed by `icloud.truongphillipthanh@gmail.com`. | Screenshot of the GitHub organization's "Billing and plans" page. |
| **GitHub (Repo Identity)** | All new commits to the organization's repositories are authored by `syncrescendence@gmail.com` and are signed with a corresponding GPG/SSH key. | `git log` output showing a commit with `Author: Syncrescendence <syncrescendence@gmail.com>` and a valid signature. |
| **Google Workspace / Gmail** | All critical OAuth clients, API credentials, and service accounts are owned by `syncrescendence@gmail.com`. | Screenshots from the Google Cloud Console API & Services dashboard showing the new ownership. |
| **Deployment Platforms** | `syncrescendence@gmail.com` is the sole owner/admin of any Vercel, Netlify, or other deployment platform accounts. | Screenshot of the team management page on each respective platform. |
| **Secret Management** | `syncrescendence@gmail.com` is the sole owner/admin of any Doppler, Vault, or other secret management platform accounts. | Screenshot of the team/access control page on each respective platform. |

### Global Migration Completion

The entire migration is considered **complete** when all of the following conditions are met:

1.  **All per-platform completion criteria listed above have been met and verified.**
2.  The `MANUS-RUN-BATCH` for the final validation audit (Post-Wave 4) has been executed, and the resulting audit files confirm the target topology.
3.  The legacy owner account (`truongphillipthanh@icloud.com`) has been successfully removed from the GitHub organization and other platforms, and its status as a secure, offline break-glass account is confirmed.
4.  A final, successful login and administrative action have been performed by `syncrescendence@gmail.com` on all critical platforms to ensure full control.
