# Phase 1: Platform Snapshot Command Recipes

This document provides non-destructive, read-only command examples to collect baseline state from each platform. These commands should be executed by the `commander` persona.

**Authentication:** All `curl` commands assume that a valid API token is passed in the `Authorization` header. Replace `<TOKEN>` with the actual token for each platform.

---

## 1. GitHub

Uses the official GitHub CLI (`gh`) and `curl` for REST API calls.

| Artifact | Command |
|---|---|
| **Organization Members** | `gh api orgs/<ORG>/members --paginate -q ".[].login" > github-users.json` |
| **Teams** | `gh api orgs/<ORG>/teams --paginate > github-groups.json` |
| **Team Members** | `gh api orgs/<ORG>/teams/<TEAM_SLUG>/members --paginate > github-team-members.json` |
| **Repositories** | `gh repo list <ORG> --json id,name,visibility > github-repos.json` |
| **Repository Collaborators** | `gh api repos/<ORG>/<REPO>/collaborators --paginate > github-repo-collaborators.json` |
| **Audit Log** | `curl -H "Authorization: bearer <TOKEN>" "https://api.github.com/orgs/<ORG>/audit-log" > github-audit-log.json` |

---

## 2. Cloudflare

Uses `curl` with the Cloudflare API.

| Artifact | Command |
|---|---|
| **Account Members** | `curl -X GET "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/members" -H "Authorization: Bearer <TOKEN>" > cloudflare-users.json` |
| **Zones** | `curl -X GET "https://api.cloudflare.com/client/v4/zones" -H "Authorization: Bearer <TOKEN>" > cloudflare-zones.json` |
| **Audit Logs** | `curl -X GET "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/audit_logs" -H "Authorization: Bearer <TOKEN>" > cloudflare-audit-logs.json` |

---

## 3. Google Workspace

Uses the Admin SDK Reports API.

| Artifact | Command |
|---|---|
| **Users** | `curl "https://admin.googleapis.com/admin/reports/v1/users?userKey=all&customerId=<CUSTOMER_ID>" --oauth2-bearer <TOKEN> > google-workspace-users.json` |
| **Groups** | `curl "https://admin.googleapis.com/admin/reports/v1/groups?domain=<DOMAIN>" --oauth2-bearer <TOKEN> > google-workspace-groups.json` |
| **Logins** | `curl "https://admin.googleapis.com/admin/reports/v1/activities/all/all?eventName=login" --oauth2-bearer <TOKEN> > google-workspace-logins.json` |

---

## 4. GCP (Google Cloud Platform)

Uses the `gcloud` CLI.

| Artifact | Command |
|---|---|
| **IAM Policy** | `gcloud projects get-iam-policy <PROJECT_ID> --format=json > gcp-iam-policy.json` |
| **Asset Inventory** | `gcloud asset export --content-type resource --project=<PROJECT_ID> --output-path=gs://<BUCKET>/gcp-asset-inventory.json` |
| **Audit Logs** | `gcloud logging read "logName:logs/cloudaudit.googleapis.com" --project=<PROJECT_ID> --format=json > gcp-audit-logs.json` |

---

## 5. Slack

Uses the Slack Web API.

| Artifact | Command |
|---|---|
| **Users** | `curl -H "Authorization: Bearer <TOKEN>" "https://slack.com/api/users.list" > slack-users.json` |
| **User Groups** | `curl -H "Authorization: Bearer <TOKEN>" "https://slack.com/api/usergroups.list" > slack-groups.json` |
| **Audit Logs** | `curl -H "Authorization: Bearer <TOKEN>" "https://slack.com/api/team.accessLogs" > slack-audit-logs.json` |

---

## 6. Discord

Uses the Discord API.

| Artifact | Command |
|---|---|
| **Guild Members** | `curl -H "Authorization: Bot <TOKEN>" "https://discord.com/api/v10/guilds/<GUILD_ID>/members?limit=1000" > discord-members.json` |
| **Guild Roles** | `curl -H "Authorization: Bot <TOKEN>" "https://discord.com/api/v10/guilds/<GUILD_ID>/roles" > discord-roles.json` |
| **Audit Log** | `curl -H "Authorization: Bot <TOKEN>" "https://discord.com/api/v10/guilds/<GUILD_ID>/audit-logs" > discord-audit-log.json` |

---

## 7. Notion

Uses the Notion API.

| Artifact | Command |
|---|---|
| **Users** | `curl -X GET "https://api.notion.com/v1/users" -H "Authorization: Bearer <TOKEN>" -H "Notion-Version: 2022-06-28" > notion-users.json` |
| **Search (All Pages/DBs)** | `curl -X POST "https://api.notion.com/v1/search" -H "Authorization: Bearer <TOKEN>" -H "Notion-Version: 2022-06-28" > notion-search.json` |

---

## 8. Coda

Uses the Coda API.

| Artifact | Command |
|---|---|
| **Docs** | `curl -H "Authorization: Bearer <TOKEN>" "https://coda.io/apis/v1/docs" > coda-docs.json` |
| **Doc Sharing Metadata** | `curl -H "Authorization: Bearer <TOKEN>" "https://coda.io/apis/v1/docs/<DOC_ID>/acl/metadata" > coda-doc-sharing.json` |

---

## 9. Jira

Uses the Jira Cloud platform REST API.

| Artifact | Command |
|---|---|
| **Users** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/rest/api/3/users/search" > jira-users.json` |
| **Projects** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/rest/api/3/project" > jira-projects.json` |
| **Project Roles** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/rest/api/3/project/<PROJECT_KEY>/role" > jira-project-roles.json` |
| **Audit Records** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/rest/api/3/auditing/record" > jira-audit-records.json` |

---

## 10. Confluence

Uses the Confluence Cloud REST API.

| Artifact | Command |
|---|---|
| **Spaces** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/wiki/rest/api/space" > confluence-spaces.json` |
| **Groups** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/wiki/rest/api/group" > confluence-groups.json` |
| **Audit Records** | `curl -u <EMAIL>:<TOKEN> -X GET "https://<YOUR_DOMAIN>.atlassian.net/wiki/rest/api/audit" > confluence-audit-records.json` |

---

## 11. Linear

Uses the Linear GraphQL API.

| Artifact | Command |
|---|---|
| **Users & Teams** | `curl -X POST -H "Authorization: <TOKEN>" -H "Content-Type: application/json" --data '{"query": "query { users { nodes { id name email } } teams { nodes { id name } } }"}' https://api.linear.app/graphql > linear-users-teams.json` |

---

## 12. ClickUp

Uses the ClickUp API.

| Artifact | Command |
|---|---|
| **Teams (Workspaces)** | `curl -H "Authorization: <TOKEN>" "https://api.clickup.com/api/v2/team" > clickup-teams.json` |
| **Team Members** | `curl -H "Authorization: <TOKEN>" "https://api.clickup.com/api/v2/team/<TEAM_ID>/user" > clickup-team-members.json` |

---

## 13. Basecamp

Uses the Basecamp 4 API.

| Artifact | Command |
|---|---|
| **People** | `curl -H "Authorization: Bearer <TOKEN>" "https://3.basecampapi.com/<ACCOUNT_ID>/people.json" > basecamp-people.json` |
| **Projects** | `curl -H "Authorization: Bearer <TOKEN>" "https://3.basecampapi.com/<ACCOUNT_ID>/projects.json" > basecamp-projects.json` |

---

## 14. Airtable

Uses the Airtable API.

| Artifact | Command |
|---|---|
| **Bases** | `curl -H "Authorization: Bearer <TOKEN>" "https://api.airtable.com/v0/meta/bases" > airtable-bases.json` |
| **Base Collaborators** | `curl -H "Authorization: Bearer <TOKEN>" "https://api.airtable.com/v0/meta/bases/<BASE_ID>/collaborators" > airtable-base-collaborators.json` |
