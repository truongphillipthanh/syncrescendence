---
id: SOURCE-20260129-x-thread-adocomplete-parakeet_tdt_from_nvidia_is_damn
platform: x
format: thread
creator: adocomplete
title: parakeet tdt from nvidia is damn
status: triaged
original_filename: "20260129-x_thread-parakeet_tdt_from_nvidia_is_damn-@adocomplete.md"
url: https://x.com/adocomplete/status/2016926628044292237
author: "@adocomplete"
captured_date: 2026-01-29
signal_tier: tactical
topics:
  - developer-tools
  - automation
teleology: extract
notebooklm_category: coding-tools
aliases:
  - "adocomplete - Parakeet TDT local voice transcription"
synopsis: "Brief thread about deploying NVIDIA's parakeet-tdt-0.6b-v3 speech-to-text model on a homelab server (Ryzen 9 9745HX) and building a local macOS voice transcription app with Claude Code. Near-instant transcription quality comparable to Whispr Flow but free and self-hosted."
key_insights:
  - "NVIDIA's parakeet-tdt-0.6b-v3 provides near-instant local voice transcription with correct formatting (capitalization, punctuation) on consumer hardware."
  - "The model can replace paid services like Whispr Flow ($12/month) with equivalent quality on self-hosted infrastructure."
  - "Claude Code was used to build the macOS transcription app, demonstrating practical vibe-coding for desktop utility apps."
---
# Parakeet TDT Thread

parakeet-tdt-0.6b-v3 from nVidia is damn good.

I deployed it on a homelab server (Ryzen 9 9745HX), built a local voice transcription MacOS app (with Claude Code), and the transcription is near instant.

This tweet may or may not have been written by that app. ;)

(Description: Embedded video showing a MacOS app deployment checklist interface. The window displays "Mac OS app deployment checklist" at the top. The main content contains:

**Submit for Notarization section:**
- scrun notarytool submit YourApp.zip -apple-id X -password Z --wait

**Staple the ticket:**
- scrun stapler staple YourApp.app

**Verify stapling:**
- scrun stapler validate YourApp.app

**Upload & Submit section:**
- Upload via Xcode Organizer or `scrun altool`
- Wait for App Store processing (usually 15-30 min)
- Submit for review once processing completes

**Post-Submission section:**
- Monitor for review feedback in App Store Connect
- Have a rollback plan if critical issues surface
- Prepare announcement / release columns

At the bottom: "Anything specific giving you trouble, or is this for OpenLifeLog or another project?"

On the right side: A "Local Whisper" panel showing "Recording... 0:08" with text "Hey Claude, it is a good day to ship. Can you give me a checklist for deploying a Mac OS app, please?" and audio waveform visualization below.

At the bottom of the dialog: "Claude is AI and can make mistakes. Please double-check responses"

Backdrop shows a scenic mountain landscape with forest.
)

---

## Reply 1

Going to make the repo open source. There's really not much magic to it.

---

## Reply 2

Nice. I used Whispr Flow prior to this and I'd say it's just as good and saves you $12/mo.

---

## Reply 3

I used this repo for the deployment (https://github.com/groxaxo/parakeet-tdt-0.6b-v3-fastapi-openai/blob/main/DOCKER.md). Haven't checked if it's doing anything specific in regards to formatting, but for me it is formatting text correctly: capitalizing, adding punctuation, etc.