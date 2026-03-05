# MANUS-RUN-BATCH

This document contains the specific, non-interactive command batches that Manus is cleared to execute immediately after a corresponding Human Authentication Window is closed. These are designed to be idempotent and safe to run.

---

### Post-Wave 0: Audit Run

**Trigger:** After human operator confirms all accounts are accessible.

**Action:** This batch is for read-only auditing. It requires a temporary, read-only GitHub Personal Access Token (PAT) provided by the operator.

```bash
# Requires GITHUB_PAT environment variable to be set
# Example: export GITHUB_PAT="ghp_..."

# --- GitHub Organization Audit ---
gh api orgs/{your_org_name} > /home/ubuntu/syncrescendence/audit/wave0_org_details.json
gh api orgs/{your_org_name}/members --jq ".[].login" > /home/ubuntu/syncrescendence/audit/wave0_org_members.txt
gh api orgs/{your_org_name}/teams --jq ".[].slug" > /home/ubuntu/syncrescendence/audit/wave0_org_teams.txt

# --- GitHub Repository Audit ---
# (This would need to be scripted to loop through all repos)
gh repo list {your_org_name} --json name --jq ".[].name" | while read repo; do \
  echo "Auditing repo: $repo"; \
  gh api repos/{your_org_name}/$repo/actions/secrets > /home/ubuntu/syncrescendence/audit/wave0_repo_${repo}_secrets.json; \
done

# Note: Auditing Vercel/Doppler would require their respective CLIs and API keys.
# Example for Vercel:
# vercel team ls > /home/ubuntu/syncrescendence/audit/wave0_vercel_teams.txt
```

---

### Post-Wave 3: Git Identity Cutover

**Trigger:** After human operator has demoted the legacy owner and generated a new GPG/SSH signing key.

**Action:** This batch reconfigures the local Git identity and pushes a test commit to validate the new setup. The operator must provide the new GPG key ID.

```bash
# Requires GPG_KEY_ID environment variable to be set
# Example: export GPG_KEY_ID="ABC123XYZ"

# --- Configure Git for New Identity ---
git config --global user.name "Syncrescendence"
git config --global user.email "syncrescendence@gmail.com"
git config --global user.signingkey $GPG_KEY_ID
git config --global commit.gpgsign true

# --- Create and Push Test Commit ---
# (Assumes a test repository has been created and cloned)
cd /path/to/test-repo
echo "Test commit for new identity" >> README.md
git add README.md
git commit -m "chore: verify new commit identity and signing key"
git push origin main

# --- Verify Commit ---
git log -1 --show-signature
```

---

### Post-Wave 4: Final Validation Audit

**Trigger:** After human operator has removed all legacy accounts from the organization.

**Action:** This batch re-runs the audit from Wave 0 to produce a final state snapshot for comparison and verification.

```bash
# Requires GITHUB_PAT for the new owner account

# --- Final GitHub Organization Audit ---
gh api orgs/{your_org_name} > /home/ubuntu/syncrescendence/audit/wave4_final_org_details.json
gh api orgs/{your_org_name}/members --jq ".[].login" > /home/ubuntu/syncrescendence/audit/wave4_final_org_members.txt

# --- Verification ---
# Expected output of members command should be only 'syncrescendence'
# Diff the wave0 and wave4 audit files to confirm changes.
diff /home/ubuntu/syncrescendence/audit/wave0_org_members.txt /home/ubuntu/syncrescendence/audit/wave4_final_org_members.txt
```
