# YouTube OAuth2 Setup (One-Time)

## 1. Create Credentials

Visit: https://console.cloud.google.com/apis/credentials?project=741156467927

1. Click **+ CREATE CREDENTIALS** > **OAuth client ID**
2. Application type: **Desktop app**
3. Name: `syncrescendence-ingest`
4. Click **Create**
5. Click **DOWNLOAD JSON** on the confirmation dialog

## 2. Save the File

Move the downloaded file to:

```
~/.syncrescendence/client_secret.json
```

```bash
mv ~/Downloads/client_secret_*.json ~/.syncrescendence/client_secret.json
```

## 3. Authenticate

```bash
source ~/.syncrescendence/venv/bin/activate && python3 /Users/system/Desktop/syncrescendence/00-ORCHESTRATION/scripts/youtube_oauth_setup.py
```

A browser window will open. Approve access. Token saves to `~/.syncrescendence/youtube_token.json`.
