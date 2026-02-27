# Claude Teacher Framework

Add this paragraph to the **CLAUDE.md** file to turn Claude Code into Claude Teacher. Every project is a lesson to become more technical.

## Core Instruction

> For every project, write a detailed FOR[yourname].md file that explains the whole project in plain language.

Explain the technical architecture, the structure of the codebase and how the various parts are connected, the technologies used, why we made these technical decisions, and lessons I can learn from it (this should include the bugs we ran into and how we fixed them, potential pitfalls and how to avoid them in the future, new technologies used, how good engineers think and work, best practices, etc).

It should be very engaging to read; don't make it sound like boring technical documentation/textbook. Where appropriate, use analogies and anecdotes to make it more understandable and memorable.

## Example Structure

(Description: Code example showing project organization for a YouTube to Ebook Newsletter platform with three main sections:

**# FORZARA: YouTube to Ebook Newsletter**
**## The Big Picture: What We Built**

**## The Architecture: How the Pieces Fit Together**

Think of this project like a newspaper production line:
```
┌────────────────────────────────────────────────┐
│       YOUR YOUTUBE NEWSLETTER                  │
└────────────────────────────────────────────────┘

│ INTAKE      │ PROCESSING      │ OUTPUT         │
│ ────────────│─────────────────│────────────────│
│             │                 │                │
│ get_videos.py → get_transcripts.py → write_articles.py
│ (The Scout)   (The Stenographer)   (The Writer)
│             │                 │                │
│             v                 v                │
│        YouTube API      Transcript API    Claude AI
│                                                │
│                      │                        │
│                      v                        │
│                 send_email.py                 │
│              (The Publisher)                  │
│                      │                        │
│    ┌─────────────┬───┴────────┬─────────────┐ │
│    v             v            v             v │
│  EPUB Ebook    Email Newsletter               │
│                                                │
│ CONTROL CENTER                                │
│ ─────────────────────────────────────────── │
│ main.py        → Orchestrates the whole pipeline
│ video_tracker.py → Remembers what's already been sent
│ dashboard.py     → Pretty web interface (no Terminal needed!)
│ +.plist files    → Mac automation (runs while you sleep)

### The Cast of Characters (Files)

│ File │ Role │ Analogy │
│──────│──────│──────────│
│ get_videos.py │ Fetches latest videos from your channels │ The scout who...
```
)

---

*Metadata: 5:40 AM · Jan 24, 2026 | 909.8K Views | 113 Replies | 608 Reposts | 5,024 Likes | 9,433 Bookmarks*