# Phase 0: Security and Readiness Gate Checklist

This checklist must be successfully completed before proceeding to Phase 1. All checks are mandatory and must have a 'Pass' status.

| Category | Check ID | Description | Executor | Pass Criteria | Status |
|---|---|---|---|---|---|
| **Project Governance** | GOV-01 | Final cutover plan approved by all stakeholders (CC81 Steering Committee). | human | Signed approval document is stored in the project's central repository. | Fail |
| | GOV-02 | Communication plan for cutover activities has been distributed to all affected users and teams. | human | Confirmation of receipt from all team leads. | Fail |
| | GOV-03 | A detailed rollback plan for Phase 1 has been documented and reviewed by the technical team. | human | Rollback plan is versioned and stored in the project repository. | Fail |
| | GOV-04 | Go/No-Go decision meeting scheduled prior to Phase 1 start. | human | Calendar invite sent to all required attendees. | Fail |
| **Technical Readiness** | TECH-01 | All required API tokens and service account credentials for snapshotting have been provisioned. | manus | All credentials are stored securely in the designated secrets management system. | Fail |
| | TECH-02 | Connectivity to all 14 platform APIs from the execution environment (`manus`) has been successfully tested. | manus | A successful `GET` request (e.g., list users, list projects) has been made to each platform's API. | Fail |
| | TECH-03 | The `PLATFORM-SNAPSHOT-COMMAND-RECIPES` have been tested in a non-production environment for each platform. | commander | All snapshot commands execute without error and produce the expected output format. | Fail |
| | TECH-04 | The target storage for snapshot evidence (e.g., S3 bucket, GCS bucket) is provisioned and accessible. | psyche | A test file can be successfully written to and read from the evidence store. | Fail |
| **Security Posture** | SEC-01 | The principle of least privilege is applied to all API tokens and service accounts used for snapshotting (read-only access only). | psyche | A security review has confirmed that no write, delete, or modify permissions are granted. | Fail |
| | SEC-02 | Audit logging is enabled on all platforms for the accounts that will be used for snapshotting. | human | Audit logs show successful read-only API calls made during testing. | Fail |
| | SEC-03 | The execution environment (`manus`, `commander`) has been scanned for vulnerabilities. | psyche | No critical or high-severity vulnerabilities are present in the execution environment. | Fail |
| **Team Readiness** | TEAM-01 | All team members involved in the cutover have reviewed the runbook and confirmed their roles and responsibilities. | human | A sign-off sheet or confirmation email from each team member is collected. | Fail |
| | TEAM-02 | An on-call rotation for the cutover period has been established and communicated. | human | The on-call schedule is published in the team's shared calendar. | Fail |
| | TEAM-03 | Primary and secondary communication channels (e.g., dedicated Slack/Discord channel, video conference link) for the cutover team are established and tested. | human | A test message has been successfully sent and received by all team members in the designated channels. | Fail |
