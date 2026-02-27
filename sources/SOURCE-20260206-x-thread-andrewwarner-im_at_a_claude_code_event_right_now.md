---
url: https://x.com/AndrewWarner/status/2019837230060044628
author: "@AndrewWarner"
captured_date: 2026-02-06
id: SOURCE-20260206-027
original_filename: "20260206-x_thread-im_at_a_claude_code_event_right_now-@andrewwarner.md"
status: triaged
platform: x
format: thread
creator: andrewwarner
signal_tier: tactical
topics: [ai-agents, developer-tools, tutorial]
teleology: reference
notebooklm_category: ai-agents
aliases: ["Andrew Warner - OpenClaw Troubleshooting Guide"]
synopsis: "Shares a comprehensive OpenClaw troubleshooting guide from a Claude Code meetup, covering 14 sections: triage, bot recovery, gateway issues, token/auth problems, config crash loops, channel issues, model/provider failures, session/memory problems, launchd/systemd service management, performance issues, nuclear reset options, debug toolkit, and common mistakes."
key_insights: ["The most common OpenClaw complaint at meetups is the agent shutting down unexpectedly — systematic triage order matters", "The guide covers launchd and systemd service management for persistent agent deployment on macOS and Linux", "Nuclear options (full reset) are documented as last resort with clear escalation path from triage to debug toolkit"]
---
# Andrew Warner's OpenClaw Troubleshooting Thread

I'm at a Claude Code event right now. Everyone's complaint: Openclaw keeps shutting down. @calebhodges gave us all a markdown file that solves the common issues. Want it? Comment "openclaw" and I'll DM it to you.

(Description: Image showing a markdown file titled "The Ultimate OpenClaw Troubleshooting Guide")

## The Ultimate OpenClaw Troubleshooting Guide

**For the Claude Code Meetup community — and anyone running OpenClaw.**

> Download this file, feed it to your agent, and never debug blind again.

---

## Table of Contents

1. [First 60 Seconds — The Triage](#first-60-seconds)
2. [Your Bot Went Down (Pod Bot Recovery)](#pod-bot-recovery)
3. [Gateway Won't Start](#gateway-wont-start)
4. [Token & Auth Issues](#token-auth-issues)
5. [Config Crash Loops](#config-crash-loops)
6. [Channel-Specific Issues](#channel-issues)
7. [Model & Provider Failures](#model-failures)
8. [Session & Memory Issues](#session-memory)
9. [Service Management (launchd/systemd)](#service-management)
10. [Performance & Resource Issues](#performance)
11. [Nuclear Options (Reset Everything)](#nuclear-options)
12. [The Debug Toolkit](#debug-toolkit)
13. [Common Mistakes to Avoid](#common-mistakes)
14. [Getting Help](#getting-help)

---

## 1. First 60 Seconds — The Triage {#first-60-seconds}

When something breaks, run these **in order**. Don't skip ahead.
```bash
# Step 1: Is it even running?
openclaw status
```