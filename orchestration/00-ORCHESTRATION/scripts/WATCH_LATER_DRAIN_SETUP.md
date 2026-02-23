# Watch Later Drain — Setup Guide

## What This Does

`drain_watch_later.py` extracts every video from your YouTube Watch Later playlist using yt-dlp (browser cookie auth), fetches metadata via the YouTube Data API, fetches transcripts via youtube-transcript-api, generates SOURCE-*.md files, and deduplicates against URL_INDEX.txt.

## Prerequisites

### 1. yt-dlp

Already installed in the Syncrescendence venv:

```bash
~/.syncrescendence/venv/bin/yt-dlp --version
```

If missing:

```bash
~/.syncrescendence/venv/bin/pip install yt-dlp
```

### 2. youtube-transcript-api (v1.x)

```bash
~/.syncrescendence/venv/bin/pip install youtube-transcript-api
```

### 3. requests

```bash
~/.syncrescendence/venv/bin/pip install requests
```

### 4. YouTube Data API Key

Hardcoded in the script. Override with `--api-key` if needed. The key is used only for video metadata (snippet, contentDetails). If the API key is exhausted or invalid, the script falls back to yt-dlp metadata (less structured but functional).

## Critical: Browser Must Be Closed

yt-dlp reads cookies directly from the browser's SQLite database. Chrome (and most browsers) hold an exclusive lock on this file while running. **You must quit Chrome before running the script.** If the script hangs at "Extracting Watch Later", this is why.

### Alternative: Export Cookies to a File

If you cannot close Chrome, export cookies once and reuse:

```bash
# Export (requires Chrome closed for this one-time step):
~/.syncrescendence/venv/bin/yt-dlp --cookies-from-browser chrome \
  --cookies ~/wl_cookies.txt \
  "https://www.youtube.com/playlist?list=WL" --flat-playlist --print id 2>/dev/null

# Then drain using the exported file (Chrome can be open):
python drain_watch_later.py --cookies-file ~/wl_cookies.txt
```

Note: Cookies expire. Re-export periodically.

## Usage

```bash
# Activate venv (or use full path)
source ~/.syncrescendence/venv/bin/activate

# Dry run — see what would be ingested
python orchestration/scripts/drain_watch_later.py --dry-run

# Full drain
python orchestration/scripts/drain_watch_later.py

# Use Firefox instead of Chrome
python orchestration/scripts/drain_watch_later.py --cookies-from-browser firefox

# Use exported cookies file
python orchestration/scripts/drain_watch_later.py --cookies-file ~/wl_cookies.txt

# Verbose logging
python orchestration/scripts/drain_watch_later.py -v
```

## Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--dry-run` | off | List videos without writing files |
| `--cookies-from-browser` | `chrome` | Browser for cookie extraction |
| `--cookies-file` | none | Netscape cookies file (bypasses browser lock) |
| `--api-key` | built-in | YouTube Data API v3 key |
| `--remove-after` | off | Log warning (removal not supported, see below) |
| `--sources-dir` | `sources/` | Override output directory |
| `-v` / `--verbose` | off | Debug logging |

## Known Limitations

### Watch Later Removal Not Supported

The `--remove-after` flag is accepted but only logs a warning. Neither yt-dlp nor the YouTube Data API support removing videos from the Watch Later playlist:

- **YouTube Data API**: Deprecated Watch Later (WL) playlist access entirely in 2016. `playlistItems.delete()` returns 403 for WL.
- **yt-dlp**: Read-only extraction tool. No playlist mutation capability.
- **Workaround**: After a successful drain, manually clear Watch Later in the browser, or use a browser extension.

### Cookie Extraction Requires Browser Closed

See "Critical: Browser Must Be Closed" above. This is a fundamental limitation of how yt-dlp reads browser cookie databases.

### macOS Keychain Prompt

On macOS, yt-dlp may trigger a Keychain access prompt when reading Chrome cookies (Chrome encrypts cookies with a Keychain-stored key). Click "Allow" or "Always Allow" when prompted.

### API Quota

The YouTube Data API has a default quota of 10,000 units/day. Each `videos.list` call costs 1 unit. A Watch Later with 500 videos uses 500 units. If quota is exhausted, the script falls back to yt-dlp-provided metadata (less structured but functional for SOURCE file generation).

## Output

- SOURCE files: `sources/SOURCE-{YYYYMMDD}-youtube-{format}-{creator}-{title}.md`
- Dedup index: `sources/_meta/URL_INDEX.txt` (one URL per line, appended)
- Frontmatter schema: identical to `youtube_ingest.py` output

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Script hangs at extraction | Browser is open | Quit browser, re-run |
| `ERROR: Sign in to confirm` | Cookies invalid/expired | Re-export cookies |
| Empty Watch Later | Already drained or wrong account | Check account in browser |
| API 403 errors | API key invalid or quota exceeded | Script auto-falls back to yt-dlp metadata |
| Keychain popup | macOS cookie decryption | Click "Allow" |
