# Phase 1: Evidence Receipt Template

This JSON template should be used to create a receipt for each snapshot artifact collected. The receipt serves as a manifest file, ensuring the integrity and providing metadata for each piece of evidence.

A separate receipt file, named `<artifact_filename>.receipt.json`, should be created for each corresponding evidence file.

```json
{
  "schema_version": "1.0",
  "receipt_id": "",
  "timestamp_utc": "",
  "platform": "",
  "artifact_name": "",
  "artifact_type": "",
  "executor": "",
  "command_executed": "",
  "checksums": {
    "sha256": ""
  },
  "record_count": 0,
  "notes": ""
}
```

## Template Fields

| Field | Type | Description |
|---|---|---|
| `schema_version` | String | The version of this receipt schema. |
| `receipt_id` | String | A unique identifier (UUID) for this receipt. |
| `timestamp_utc` | String | The ISO 8601 timestamp (in UTC) when the snapshot was captured. |
| `platform` | String | The name of the platform from which the evidence was collected (e.g., `github`, `cloudflare`). |
| `artifact_name` | String | The filename of the snapshot artifact (e.g., `github-users.json`). |
| `artifact_type` | String | The type of data contained in the artifact, referencing the `PHASE1-SNAPSHOT-SCHEMA` (e.g., `user`, `group`). |
| `executor` | String | The entity that executed the snapshot command (e.g., `commander`, `manus`). |
| `command_executed` | String | The exact command that was run to generate the artifact. |
| `checksums` | Object | An object containing cryptographic hashes of the artifact file. At a minimum, SHA256 is required. |
| `record_count` | Integer | The number of individual records (e.g., users, groups) contained within the artifact. |
| `notes` | String | Any relevant notes or observations about the snapshot process or the resulting artifact. |
