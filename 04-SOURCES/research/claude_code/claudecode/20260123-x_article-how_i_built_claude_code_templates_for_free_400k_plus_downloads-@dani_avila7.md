---
url: https://x.com/dani_avila7/status/2014855040368783779
author: Daniel San (@dani_avila7)
captured_date: 2026-01-24
---

# How I Built Claude Code Templates for Free (400K+ Downloads)

Maintaining open source projects that scale is far from cheap. You need to get creative and leverage whatever free-tier services you can find.

One of my first thoughts was: the service should be built on top of something every developer already has. npm + GitHub came to mind immediately. So I built a CLI that runs easily with npx, and the entire backend sits on GitHub using their public API, which has rate limits per IP.

This way, I host absolutely nothing. The client runs npx, and each GitHub API call runs on their own account.

![Claude Code Templates - Free Architecture diagram showing CLI npm package (80K installs) connecting via Direct API calls per user IP to GitHub MY BACKEND (400K downloads), with aitmpl.com Vercel fetching components and connecting via Logs to Supabase and Analytics to Neon.](Description: A flowchart diagram illustrating the system architecture with four main components: CLI (blue box) labeled "npm package 80K installs", GitHub (purple box) labeled "MY BACKEND 400K downloads", aitmpl.com Vercel (green box), Supabase (pink rounded box), and Neon (orange rounded box). Arrows show data flow: Direct API calls per user IP from CLI to GitHub, Fetch components from aitmpl.com to GitHub, Logs from aitmpl.com to Supabase, and Analytics from aitmpl.com to Neon.)

## The Stack

- **Frontend:** Vercel (free) - Originally started on GitHub Pages, but moved to Vercel when traffic spiked
- **Component Storage:** GitHub repo - All Skills, Agents, Hooks stored as JSON/Markdown
- **Databases:** Supabase (free) for logs + Neon (free) for analytics
- **CLI:** npm package - Runs locally on developer machines

## The Secret: GitHub as backend

Here's where it gets interesting. Most package managers need servers to handle distribution. I skipped that entirely.

![Diagram showing multiple users (User 1, 2, 3, N) each running "npx claude-code-templates --skill='skill_name'" connecting via GitHub API Rate limit per User IP to a central GitHub Repo containing "Components as JSON/MD".](Description: A parallel architecture diagram displaying multiple user instances (blue boxes on the left) each labeled "User 1, 2, 3, N" with "npx claude-code-templates --skill='skill_name'" commands. All users connect via arrows labeled "GitHub API Rate limit: User IP" to a central purple box labeled "GitHub Repo Components as JSON/MD".)

When you run `npx claude-code-templates --skill="skill_name"`, the CLI makes a direct API call to GitHub from your machine. GitHub's public API has generous rate limits per IP address (5,000 requests/hour for authenticated, 60/hour for non-authenticated).

Since each user runs the CLI from their own IP, each one gets their own rate limit bucket. I'm not the bottleneck, GitHub is, and GitHub can handle way more traffic than I ever could on a free tier backend.

This architecture means:

- **Zero server costs** - No backend to maintain or pay for
- **Infinite scalability** - Each user is their own tenant
- **No rate limiting on my end** - GitHub handles all the traffic
- **Global CDN for free** - GitHub's infrastructure serves the files
- **No deployment complexity** - Just push to the repo

## Community-Driven Components

The beauty of having everything on GitHub is that developers can contribute directly. They can add new Skills, SubAgents, or Hooks through pull requests.

![GitHub workflow diagram showing: Developer → Fork & PR → GitHub Repo → Review & Merge → Main Branch → Auto Deploy → Vercel → aitmpl.com](Description: A horizontal flowchart showing the contribution workflow with green boxes for "Developer" and "Fork & PR", a purple box for "GitHub Repo", an orange box for "Review & Merge", another branch leading to a teal/green box for "Vercel", and a blue box labeled "aitmpl.com" at the end. Arrows connect each step showing the automated pipeline.)

Once a PR is merged:

1. **Vercel auto-deploys** - The website updates immediately showing the new component
2. **GitHub serves it** - The component becomes available for CLI downloads instantly
3. **No manual intervention** - Everything is automated through GitHub Actions

This means the community can grow the template library without any manual publishing steps from me. Fork, add your component, submit a PR, and once merged, it's live for everyone.

## How It Scales

The website ([aitmpl.com](https://aitmpl.com)) is just a browsing interface hosted on Vercel's free tier. It shows what's available but doesn't serve the actual components. When users install via CLI, they pull directly from GitHub.

I use two lightweight databases:

- **Supabase** for logging installs and tracking which components are popular
- **Neon** for analytics and usage patterns

Both are on free tiers and handle the load just fine because they're only storing metadata, not serving the actual components.

## The numbers

After being featured in Anthropic's official Claude Code documentation, the project took off:

- **80K+ npm installs** of the CLI
- **400K+ component downloads** from GitHub
- **18K+ GitHub stars**
- **$0 in infrastructure costs**

## Why this works

The key insight is building on top of infrastructure developers already use and trust. Everyone has npm and GitHub access. By leveraging their free tiers and public APIs, I built a distribution system that can handle massive scale without spending a dime.

The repo is fully open source, check it out: [https://github.com/davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

---

**Posted:** 4:17 PM · Jan 23, 2026  
**Engagement:** 4 replies, 14 reposts, 146 likes, 215 bookmarks, 21.5K views