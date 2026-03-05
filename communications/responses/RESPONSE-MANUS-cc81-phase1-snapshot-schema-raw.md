# Phase 1: Normalized Snapshot Schema

This document defines the normalized data schema for storing pre-cutover evidence artifacts. The goal is to create a consistent, cross-platform data model for users, groups, roles, and resources to simplify analysis and verification.

All snapshot artifacts should be stored as JSON files, with each file containing an array of objects conforming to the schemas defined below.

## Core Concepts

- **User:** An individual identity with access to a platform.
- **Group:** A collection of users, often used to manage permissions.
- **Role:** A set of permissions that can be assigned to users or groups.
- **Resource:** A platform-specific object to which access is controlled (e.g., a GitHub repository, a Google Drive folder, a Jira project).

## 1. User Schema

File naming convention: `<platform>-users.json`

| Field | Type | Description | Example |
|---|---|---|---|
| `id` | String | The unique identifier for the user on the platform. | `"109443942483258953483"` |
| `username` | String | The user's primary username or login name. | `"alex.smith"` |
| `email` | String | The user's primary email address. | `"alex.smith@example.com"` |
| `display_name` | String | The user's full name or display name. | `"Alex Smith"` |
| `status` | String | The current status of the user account (e.g., `ACTIVE`, `SUSPENDED`, `DEPROVISIONED`). | `"ACTIVE"` |
| `mfa_enabled` | Boolean | Indicates whether multi-factor authentication is enabled for the user. | `true` |
| `last_login_at` | String | The timestamp of the user's last login (ISO 8601 format). | `"2026-03-01T12:00:00Z"` |
| `created_at` | String | The timestamp when the user account was created (ISO 8601 format). | `"2024-01-15T10:30:00Z"` |

## 2. Group Schema

File naming convention: `<platform>-groups.json`

| Field | Type | Description | Example |
|---|---|---|---|
| `id` | String | The unique identifier for the group on the platform. | `"04d214gce6234d2"` |
| `name` | String | The name of the group. | `"engineering-team"` |
| `description` | String | A brief description of the group's purpose. | `"All members of the engineering department"` |
| `member_count` | Integer | The total number of members in the group. | `42` |
| `members` | Array[String] | An array of user IDs who are members of the group. | `["109...", "102..."]` |

## 3. Role Schema

File naming convention: `<platform>-roles.json`

| Field | Type | Description | Example |
|---|---|---|---|
| `id` | String | The unique identifier for the role on the platform. | `"project-admin"` |
| `name` | String | The name of the role. | `"Project Administrator"` |
| `description` | String | A description of the permissions granted by the role. | `"Can manage project settings and members"` |
| `permissions` | Array[String] | A list of specific permission strings associated with the role. | `["repo:write", "repo:admin"]` |

## 4. Resource Access Schema

File naming convention: `<platform>-resource-access.json`

This schema captures the relationship between users/groups and the resources they can access.

| Field | Type | Description | Example |
|---|---|---|---|
| `resource_id` | String | The unique identifier for the resource. | `"PROJ-123"` |
| `resource_type` | String | The type of the resource (e.g., `github_repository`, `google_drive_file`, `jira_project`). | `"jira_project"` |
| `principal_id` | String | The ID of the user or group being granted access. | `"04d214gce6234d2"` |
| `principal_type` | String | The type of the principal (`USER` or `GROUP`). | `"GROUP"` |
| `role` | String | The role or permission level granted to the principal for this resource. | `"Administrator"` |
