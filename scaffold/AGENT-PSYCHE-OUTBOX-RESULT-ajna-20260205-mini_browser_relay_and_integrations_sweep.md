# RESULT — TASK-20260205-mini_browser_relay_and_integrations_sweep (Ajna / Mac mini)

## 1) Browser Relay extension (OpenClaw)
### Outcome
- `openclaw browser extension install` initially failed with:
  - `Error: Bundled Chrome extension is missing.`
- Root cause: OpenClaw CLI expects bundled extension at:
  - `.../lib/node_modules/assets/chrome-extension` (sibling to the `openclaw` module)
  - but on Ajna the extension exists at:
    - `/Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/assets/chrome-extension`

### Fix applied
Created the expected assets path and symlinked it to the packaged extension:
- created: `/Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/assets/`
- symlink:
  - `/Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/assets/chrome-extension` → `/Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/assets/chrome-extension`

After this:
- `openclaw browser extension install` → **success**
- `openclaw browser extension path` → `~/.openclaw/browser/chrome-extension`

## 2) Manual Chrome steps required (BLOCKER)
I cannot complete the Chrome UI steps from CLI alone.
Phillip must do this on the mini:
1. Open Chrome → `chrome://extensions`
2. Enable **Developer mode**
3. **Load unpacked** → select:
   - `~/.openclaw/browser/chrome-extension`
4. Pin **OpenClaw Browser Relay**
5. For each target SaaS tab (ClickUp, Linear, GitHub, Slack admin, Discord): click the extension icon so the badge shows **ON**.

## 3) SaaS native integrations sweep (BLOCKED on relay attachment)
Until Browser Relay is enabled on the relevant logged-in tabs (or credentials are provided for an isolated browser), I cannot reliably verify or tighten:
- Linear ↔ GitHub
- Linear ↔ Slack
- GitHub Apps (Linear/Notion scopes)
- ClickUp App Center connectors
- Make connectors
- Connected accounts for Airtable/Notion/Dropbox/Box/Google/Microsoft

## 4) Recommended minimal automation set (once access is confirmed)
- GitHub → Slack: PR opened/merged, CI failure, release published.
- Linear → Slack: issue created/assigned/status change.
- Linear ↔ GitHub: auto-link PRs/branches/commits to issues; enforce branch naming.
- ClickUp ↔ GitHub: link PRs to tasks (if ClickUp remains in use).

## 5) CC / receipts
- This result is saved to `-OUTBOX/ajna/RESULTS/...` as requested.
- Task CC has been set to **psyche** so the watcher can pipe the receipt.

## Blockers
- Requires manual Chrome extension load + per-tab relay activation (badge ON).
- Possible additional blockers later: missing admin rights on Slack/Linear/GitHub org settings, plan limitations.
