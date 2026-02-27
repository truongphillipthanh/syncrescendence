# agent-browser 0.8.3 Performance Update Thread

## Post 1: Main Announcement
**Date:** Jan 26, 2026 · 11:10 PM  
**Views:** 81K | **Replies:** 53 | **Reposts:** 54 | **Likes:** 1.1K | **Bookmarks:** 872

agent-browser 0.8.3 is *even faster*

npm install -g agent-browser

(Description: Monospace benchmark chart showing performance comparison between versions 0.8.2 and 0.8.3, displaying startup times of approximately 42ms vs. 7ms respectively, with the heading "agent-browser: 6x faster")

---

## Post 2: Repository Link
**Date:** Jan 26, 2026  
**Views:** 6.3K | **Replies:** 4 | **Reposts:** 3 | **Likes:** 68 | **Bookmarks:** 77

GitHub - vercel-labs/agent-browser: Browser automation CLI for AI agents

---

## Post 3: Focus Areas Response
**Date:** Jan 27, 2026  
**Views:** 1.9K | **Replies:** 1 | **Likes:** 2 | **Bookmarks:** (not shown)

Right now, most of the focus is on performance and stability (with many Windows fixes as well), but we did make some consumption improvements and will keep driving it down

---

## Post 4: Implementation Language
**Date:** Jan 27, 2026  
**Views:** 1.2K | **Replies:** 0 | **Likes:** 4 | **Bookmarks:** (not shown)

Rust

---

## Post 5: Performance Breakdown
**Date:** Jan 27, 2026  
**Views:** 3.4K | **Replies:** 2 | **Likes:** 27 | **Bookmarks:** 2

Average completion time for each command (snapshot, scroll, click, etc.)

Startup time has been drastically reduced, so the majority of the remaining time is now spent on the actual work

---

## Post 6: Technical Implementation Details
**Date:** Jan 27, 2026  
**Views:** 1.5K | **Replies:** 3 | **Likes:** 11 | **Bookmarks:** 2

It was actually pretty simple. I took out the script that picked the binary based on platform and architecture from every command and moved it to postinstall so it only runs once. Now everything just uses the Rust binary. The only reason I thought to look in the first place was that the script was blocking Windows use.

---