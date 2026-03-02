# YouTube Watch Later: Programmatic Access Capability Map

**Date**: 2026-02-22
**Context**: The YouTube Data API deprecated Watch Later (WL) playlist access on 2016-09-12. The `contentDetails.relatedPlaylists.watchLater` property returns `WL` for all channels, but `playlistItems.list` against it returns empty results. This document maps every viable alternative for building a stateless "inbox zero" ingest pipeline.

---

## Background

The existing pipeline (`orchestration/scripts/youtube_ingest.py`) handles Liked Videos (`LL`) and named playlists via the YouTube Data API v3 with OAuth2. Watch Later requires a different strategy because YouTube deliberately walled it off from API access to prevent third-party manipulation of a user-facing queue.

---

## Approach 1: yt-dlp with Browser Cookies

**How it works**: yt-dlp supports the `:ytwatchlater` extractor. It authenticates by importing cookies from your browser session, then scrapes the Watch Later page server-side (not via API) to extract video URLs and metadata.

**Commands**:
```bash
# Auto-extract cookies from browser (easiest)
yt-dlp --cookies-from-browser chrome --flat-playlist -j :ytwatchlater

# Or export cookies manually (more stable, doesn't rotate)
# 1. Open private/incognito window
# 2. Log into YouTube
# 3. Navigate to youtube.com/robots.txt (same tab)
# 4. Export cookies via "Get cookies.txt" extension
# 5. Close incognito (never reopen — prevents cookie rotation)
yt-dlp --cookies cookies.txt --flat-playlist -j :ytwatchlater
```

The `--flat-playlist -j` flags output one JSON object per video (id, title, url, duration, etc.) without downloading any media.

**Setup complexity**: LOW. Install yt-dlp (`brew install yt-dlp`), export cookies once.

**Auto-clear support**: NO native support. yt-dlp cannot remove videos from Watch Later. Would require a separate Playwright/Selenium step or manual clearing.

**Automation (launchd/cron)**: PARTIAL. The `--cookies` file method works headlessly. The `--cookies-from-browser` method requires the browser's cookie store to be accessible (may fail under launchd if browser is not running or keychain is locked). Cookie rotation is the main risk: YouTube invalidates cookies if the same session is active in a browser tab. The incognito export method mitigates this.

**Limitations and risks**:
- Cookie expiry: YouTube session cookies expire; re-export needed periodically (weeks to months)
- Cookie rotation: If the browser session that generated the cookies is still active, YouTube rotates them and yt-dlp auth fails
- OAuth no longer works with yt-dlp (YouTube blocked it)
- No write access (cannot remove videos after ingest)
- YouTube may rate-limit or block automated access patterns

---

## Approach 2: Google Takeout Export

**How it works**: Google Takeout (takeout.google.com) exports your YouTube data including playlists. The Watch Later playlist exports as a CSV file containing video IDs, timestamps, and basic metadata.

**Export path**: `Takeout/YouTube and YouTube Music/playlists/Watch later-videos.csv`

**Setup complexity**: LOW (manual), HIGH (automated). The export is a manual web process: visit Takeout, select YouTube, download archive. There is no API for triggering Takeout exports programmatically.

**Auto-clear support**: NO. Takeout is read-only; it cannot modify playlists.

**Automation (launchd/cron)**: NO. Takeout requires manual initiation via web UI. Google does offer scheduled exports (every 2 months), but the delivery is via email/Drive link, not a programmatic endpoint.

**Limitations and risks**:
- Manual trigger only (or at best, bi-monthly scheduled)
- Export contains only video IDs, not full metadata or transcripts
- Latency: export generation takes minutes to hours
- No removal capability
- Useful as a one-time bulk recovery tool, not a pipeline component

---

## Approach 3: Browser Extensions

**How it works**: Several Chrome extensions can export Watch Later playlist contents:

- **yt-watchlater-exporter**: Exports to JSON (title + URL)
- **YouTube Advanced Playlist Export**: Exports to JSON/CSV/TXT with detailed metadata
- **Exportron**: One-click playlist export

These work by running JavaScript against the authenticated YouTube page DOM, extracting video data as the user scrolls.

**Setup complexity**: LOW. Install extension, navigate to Watch Later, click export.

**Auto-clear support**: NO (most extensions are read-only). Some console scripts exist that can remove videos, but they are fragile DOM-dependent hacks.

**Automation (launchd/cron)**: NO. Extensions require an active browser window and human interaction. Cannot be headlessly automated.

**Limitations and risks**:
- Manual operation required each time
- Extensions may break when YouTube updates its DOM structure
- Trust concern: extensions have access to your YouTube session
- No removal capability in most cases
- Useful as a manual fallback, not a pipeline component

---

## Approach 4: Named Playlist Workaround (API-Compatible)

**How it works**: Instead of using YouTube's native Watch Later, create a named playlist (e.g., "Ingest Queue"). Use the YouTube mobile/desktop "Save to playlist" flow (which allows selecting any playlist) instead of the Watch Later button. The named playlist is fully accessible via the YouTube Data API v3.

**Setup**:
1. Create playlist via YouTube UI or API
2. Change save habit: "Save to playlist > Ingest Queue" instead of "Watch Later"
3. Pipeline reads playlist via `playlistItems.list` (already implemented)
4. Pipeline removes videos via `playlistItems.delete` after ingest (already implemented)

**Setup complexity**: VERY LOW technically. The only cost is a behavioral change: 2 taps instead of 1 to save a video (select playlist instead of Watch Later).

**Auto-clear support**: YES. The YouTube Data API supports `playlistItems.delete`, and the existing pipeline already implements this via `--clear-after-ingest`.

**Automation (launchd/cron)**: YES, fully. OAuth2 token refresh is handled by the existing pipeline. Runs headlessly with no browser dependency.

**Limitations and risks**:
- Requires changing the save habit (2 taps instead of 1)
- Watch Later button muscle memory must be retrained
- Videos saved before migration remain in Watch Later (need one-time bulk transfer)
- API quota: 10,000 units/day default (each list call = 1 unit, each delete = 50 units; ~190 delete operations/day at quota)

---

## Approach 5: YouTube Data API Direct Access

**How it works**: It does not. The API returns empty results for Watch Later since September 2016.

**Details**: `playlistItems.list(playlistId="WL")` returns `{"items": []}`. `channels.list(part="contentDetails")` returns `watchLater: "WL"` for all channels, but this ID is non-functional.

**Setup complexity**: N/A

**Auto-clear support**: N/A

**Automation**: N/A

**Limitations**: Completely non-functional. This is a dead end.

---

## Approach 6: Selenium/Playwright Browser Automation

**How it works**: Use Playwright (recommended over Selenium for modern JS-heavy sites) to:
1. Launch a browser with saved auth state (cookies/localStorage)
2. Navigate to `youtube.com/playlist?list=WL`
3. Scroll to load all items (YouTube uses infinite scroll)
4. Extract video URLs, titles, and metadata from the DOM
5. Optionally click the "Remove from Watch Later" menu item for each video

**Implementation sketch** (Playwright + Python):
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="/path/to/chrome-profile",
        headless=False,  # headless may trigger bot detection
    )
    page = browser.pages[0]
    page.goto("https://www.youtube.com/playlist?list=WL")
    page.wait_for_selector("ytd-playlist-video-renderer")

    # Scroll to load all items
    last_count = 0
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)
        items = page.query_selector_all("ytd-playlist-video-renderer")
        if len(items) == last_count:
            break
        last_count = len(items)

    # Extract video data
    for item in items:
        link = item.query_selector("a#video-title")
        title = link.get_attribute("title")
        href = link.get_attribute("href")  # /watch?v=VIDEO_ID
        print(f"{title}: https://youtube.com{href}")

    # Optional: remove each video via 3-dot menu
    # (fragile — DOM selectors change frequently)
```

**Setup complexity**: MEDIUM-HIGH. Requires Playwright installation, a persistent browser profile with YouTube auth, and ongoing maintenance as YouTube updates its DOM.

**Auto-clear support**: YES, but fragile. Removing videos requires clicking through YouTube's UI menu (3-dot > "Remove from Watch Later"), which depends on DOM selectors that YouTube changes without notice.

**Automation (launchd/cron)**: PARTIAL. Headless mode may trigger YouTube's bot detection. Using `headless=False` requires a display (or virtual framebuffer like Xvfb on Linux, which is N/A on macOS without extra setup). A persistent Chrome profile avoids re-authentication but may still face CAPTCHAs.

**Limitations and risks**:
- DOM selectors break when YouTube updates its frontend (frequent)
- Bot detection: YouTube may serve CAPTCHAs or block automated browsers
- Headless mode unreliable for authenticated YouTube
- macOS launchd context has no display server (headless required, but headless is detected)
- Maintenance burden: expect breakage every few months
- Slow: must render full browser, scroll, wait for JS hydration

---

## Comparison Matrix

| Criterion | yt-dlp + cookies | Google Takeout | Browser Ext | Named Playlist | API Direct | Playwright |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Reads Watch Later | YES | YES | YES | N/A (bypass) | NO | YES |
| Auto-clear after ingest | NO | NO | NO | YES | NO | YES (fragile) |
| Fully automatable | PARTIAL | NO | NO | YES | NO | PARTIAL |
| Setup complexity | Low | Low | Low | Very Low | N/A | Medium-High |
| Maintenance burden | Low | None | Low | None | N/A | High |
| Headless/launchd safe | YES* | NO | NO | YES | N/A | NO |
| 1-tap save UX | YES | YES | YES | NO (2 taps) | N/A | YES |
| API quota risk | None | None | None | Moderate | N/A | None |
| Breakage risk | Cookie expiry | Manual only | DOM changes | Stable (API) | Dead | DOM changes |

\* With exported cookie file method only; `--cookies-from-browser` may fail headlessly.

---

## RECOMMENDED APPROACH: Hybrid — Named Playlist + yt-dlp Bootstrap

### Architecture

```
                    +------------------+
  Save action:      |  YouTube Mobile  |
  "Save to playlist |  / Desktop       |
   > Ingest Queue"  +--------+---------+
                             |
                    Named Playlist (API-accessible)
                             |
               +-------------+-------------+
               |                           |
        youtube_ingest.py            (auto-clear)
        --playlist PLxxxxx           --clear-after-ingest
        --clear-after-ingest
               |
        sources/SOURCE-*.md
```

### Why Named Playlist Wins

1. **Full API support**: Read, write, delete — all via OAuth2, all headless, all automatable via launchd/cron.
2. **Already implemented**: The existing `youtube_ingest.py` pipeline handles named playlists with `--playlist PLxxxxx --clear-after-ingest`. Zero new code needed for the steady-state flow.
3. **Inbox zero native**: `--clear-after-ingest` removes each video after successful transcription. The playlist empties itself.
4. **No cookie management**: OAuth2 refresh tokens last indefinitely (until revoked). No browser dependency.
5. **No DOM fragility**: API is versioned and stable. No breakage from YouTube frontend changes.
6. **The UX cost is minimal**: On mobile, "Save to playlist" then selecting "Ingest Queue" is 2 taps instead of 1. On desktop, it is identical (the playlist picker appears either way). This is the only tradeoff.

### yt-dlp for One-Time Bootstrap

Use yt-dlp to drain the existing Watch Later backlog into the named playlist or directly into SOURCE files:

```bash
# Export current Watch Later as JSON (video IDs + titles)
yt-dlp --cookies cookies.txt --flat-playlist -j :ytwatchlater > wl_dump.json

# Extract video IDs
jq -r '.id' wl_dump.json > wl_video_ids.txt

# Option A: Add each to the named playlist via API, then let pipeline ingest
# Option B: Feed IDs directly to youtube_ingest.py (add --video-ids flag)
```

After the bootstrap drain, Watch Later becomes vestigial. All future saves go to the named "Ingest Queue" playlist.

### Implementation Checklist

1. **Create playlist**: `youtube_ingest.py --create-playlist "Ingest Queue"` (or create via YouTube UI)
2. **Export cookies**: One-time incognito cookie export for yt-dlp bootstrap
3. **Bootstrap drain**: Run yt-dlp to dump Watch Later, feed video IDs to pipeline
4. **Retrain muscle memory**: Change save habit to "Save to playlist > Ingest Queue"
5. **Schedule pipeline**: launchd plist running `youtube_ingest.py --playlist PLxxxxx --clear-after-ingest` on a cron (e.g., every 6 hours)
6. **Optional**: Add `--watch-later-bootstrap` flag to pipeline that wraps the yt-dlp cookie flow for one-time use

### Future Enhancement: iOS Shortcut

To recover the 1-tap UX, create an iOS Shortcut that:
1. Accepts a YouTube URL from the Share Sheet
2. Calls a webhook or writes to a file/API that adds the video to the named playlist

This restores the single-tap save experience while routing through the API-accessible pipeline.

---

## Sources

- [yt-dlp FAQ and cookie documentation](https://github.com/yt-dlp/yt-dlp/wiki/FAQ)
- [yt-dlp Watch Later issue #9029](https://github.com/yt-dlp/yt-dlp/issues/9029)
- [YouTube Data API Revision History (WL deprecation)](https://developers.google.com/youtube/v3/revision_history)
- [yt-watchlater-exporter Chrome extension](https://github.com/afnan-nex/yt-watchlater-exporter)
- [yt-playlist-export Python tool](https://github.com/daydiff/yt-playlist-export)
- [YouTube Advanced Playlist Export](https://chromewebstore.google.com/detail/youtube-advanced-playlist/njipopjohbjffopcfebochjnjbejhfpc)
- [Console script to remove Watch Later videos](https://gist.github.com/astamicu/eb351ce10451f1a51b71a1287d36880f)
- [Console script to extract Watch Later URLs](https://gist.github.com/huaminghuangtw/6d691b0314738be2b37f5317082558c3)
- [Google Takeout playlist export format](https://www.ticktechtold.com/export-youtube-playlists/)
- [Playwright vs Selenium comparison 2025](https://www.browserless.io/blog/playwright-vs-selenium-2025-browser-automation-comparison)
