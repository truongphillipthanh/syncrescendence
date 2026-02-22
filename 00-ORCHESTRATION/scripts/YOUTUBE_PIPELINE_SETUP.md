# YouTube Ingest Pipeline — Setup Guide

## Overview

Stateless YouTube ingest pipeline: Liked Videos become SOURCE-*.md files in `04-SOURCES/`, then get removed from the playlist. Inbox zero for YouTube saves.

## 1. Install Python Dependencies

```bash
pip install google-auth-oauthlib google-api-python-client youtube-transcript-api
```

## 2. Create Google Cloud Project (if needed)

1. Go to https://console.cloud.google.com/
2. Create a new project (or use existing)
3. Navigate to **APIs & Services > Library**
4. Search for **YouTube Data API v3** and **Enable** it

## 3. Create OAuth2 Credentials

1. Go to **APIs & Services > Credentials**
2. Click **Create Credentials > OAuth client ID**
3. If prompted, configure the OAuth consent screen first:
   - User Type: **External** (or Internal if using Workspace)
   - App name: `Syncrescendence YouTube Ingest`
   - Add your email as a test user
4. Application type: **Desktop app**
5. Name: `syncrescendence-youtube`
6. Click **Create**
7. Click **Download JSON**
8. Save the downloaded file as:

```bash
mv ~/Downloads/client_secret_*.json ~/.syncrescendence/client_secret.json
```

## 4. Run OAuth Setup

```bash
python 00-ORCHESTRATION/scripts/youtube_oauth_setup.py
```

A browser window opens. Log in with the Google account that owns the YouTube channel. Approve the requested permissions (read + manage playlists). The token is saved to `~/.syncrescendence/youtube_token.json`.

## 5. Build the URL Index (first run)

```bash
python 00-ORCHESTRATION/scripts/build_url_index.py
```

This scans existing SOURCE-*.md files and creates `04-SOURCES/_meta/URL_INDEX.txt` — the dedup gate that prevents re-ingesting videos already in the corpus.

## 6. Run the Ingest

### Dry run (see what would be ingested):
```bash
python 00-ORCHESTRATION/scripts/youtube_ingest.py --dry-run
```

### Ingest Liked Videos (default):
```bash
python 00-ORCHESTRATION/scripts/youtube_ingest.py
```

### Ingest and clear from Liked after success:
```bash
python 00-ORCHESTRATION/scripts/youtube_ingest.py --clear-after-ingest
```

### Ingest from a specific playlist:
```bash
python 00-ORCHESTRATION/scripts/youtube_ingest.py --playlist PLxxxxxxxxxxxxxxxx
```

### Ingest from multiple playlists:
```bash
python 00-ORCHESTRATION/scripts/youtube_ingest.py --playlist LL --additional-playlists PLaaa PLbbb
```

## 7. Optional: Periodic Polling via launchd

Install the provided plist for automatic 6-hour polling:

```bash
cp 00-ORCHESTRATION/scripts/com.syncrescendence.youtube-ingest.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.syncrescendence.youtube-ingest.plist
```

Check status:
```bash
launchctl list | grep youtube-ingest
```

View logs:
```bash
tail -f ~/.syncrescendence/logs/youtube_ingest.log
```

To unload:
```bash
launchctl unload ~/Library/LaunchAgents/com.syncrescendence.youtube-ingest.plist
```

## File Locations

| File | Path |
|------|------|
| Client secret | `~/.syncrescendence/client_secret.json` |
| OAuth token | `~/.syncrescendence/youtube_token.json` |
| URL dedup index | `04-SOURCES/_meta/URL_INDEX.txt` |
| Ingest log | `~/.syncrescendence/logs/youtube_ingest.log` |
| launchd plist | `~/Library/LaunchAgents/com.syncrescendence.youtube-ingest.plist` |

## Notes

- **Watch Later (WL)** is deprecated in the YouTube API. Use Liked Videos (LL) or create a named playlist as your ingest queue.
- The pipeline is idempotent — safe to run repeatedly. The URL index prevents duplicate SOURCE files.
- Transcripts use `youtube-transcript-api` (no API quota cost). If unavailable, the video description is used as the body.
- All credentials live in `~/.syncrescendence/` (gitignored). Nothing is hardcoded.
