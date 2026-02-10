# Setapp Audit Report
## SYN-56 — Application Stack Rationalization

**Date**: 2026-02-10
**Status**: COMPLETE
**Linear**: SYN-56
**Method**: Automated inventory (brew cask + /Applications/ + Setapp/) cross-referenced with DYN-FUNCTIONS.csv

---

## Executive Summary

- **51 Setapp apps** installed in `/Applications/Setapp/`
- **67 brew cask apps** installed
- **~195 entries** in `/Applications/`
- **53 apps** previously cataloged in DYN-FUNCTIONS.csv
- **Setapp subscription**: $9.99/mo — **KEEP** (8-9 active keeper apps, break-even at ~3 apps)

---

## Setapp Keeper Apps (9)

| App | Category | Use Case | Replacement Cost |
|-----|----------|----------|-----------------|
| BetterTouchTool | input | Trackpad gestures, window snapping, shortcuts | $22 one-time |
| Default Folder X | productivity | Enhanced file dialogs, recent folders | $40 one-time |
| Expressions | developer_tool | Regex testing and visualization | Free alternatives exist |
| ForkLift | developer_tool | Dual-pane file manager, SFTP | $30 one-time |
| Hookmark | productivity | Bidirectional file/app linking | $35/yr |
| Nitro PDF Pro | productivity | PDF editing, annotation, OCR | $180 one-time |
| PixelSnap | design | Pixel-perfect measurement tool | $40 one-time |
| Presentify | productivity | Screen annotation for presentations | $15 one-time |
| Soulver | productivity | Natural language calculator, variables | $35 one-time |

**Total replacement cost if buying individually**: ~$400+ one-time + $35/yr
**Setapp annual cost**: $120/yr — worth keeping.

---

## Setapp Cancellation Candidates (42)

Apps not actively used or redundant with existing stack:

| App | Reason for Cancellation |
|-----|------------------------|
| AirBuddy | Bluetooth management — rarely used |
| Archiver | File compression — `tar`/`zip` CLI sufficient |
| Bartender | Menu bar management — Ice (free) replaces |
| Bike | Outliner — Obsidian handles this |
| BoltAI | AI assistant — Claude Code is primary |
| CodeRunner | Code execution — terminal/nvim preferred |
| Craft | Note-taking — Obsidian is primary |
| DeskMinder | Desktop reminders — unused |
| Euclid | Math tool — Soulver preferred |
| Glyphs Mini | Font editor — not needed |
| Goldie App | Golden ratio — PixelSnap covers layout |
| GoodTask | Task manager — Linear/ClickUp/Things3 cover this |
| Hype | HTML animation — not used |
| Icon (folder) | Icon management — unused |
| IconJar | Icon organization — unused |
| Merlin Project Express | Project management — TeamGantt planned |
| Mission Control Plus | Window management — Raycast covers |
| Mockuuups Studio | Mockup generator — Figma covers |
| Moonlock | Security scanner — system level covered |
| Muse | Spatial canvas — Milanote preferred |
| Numi | Calculator — Soulver preferred |
| Paper | Note sketching — unused |
| Paste | Clipboard manager — Maccy (free) preferred |
| PDF Pals | PDF AI — unused |
| PDF Search | PDF search — DEVONthink covers |
| PDF Squeezer | PDF compression — Nitro handles |
| Plus | Calculator — Soulver preferred |
| PocketCAS | Math CAS — overkill |
| PopChar | Character picker — San Fransymbols free |
| Prizmo Remix | OCR — Nitro PDF handles |
| QuitAll | Quit utility — Swift Quit (free) covers |
| Receipts | Receipt scanning — not used |
| Rocket Typist | Text expansion — Raycast snippets cover |
| Slidepad | Floating browser — unused |
| Squash | Image compression — ImageOptim (free) covers |
| start.app | App launcher — Raycast covers |
| Tab Finder | Safari tab search — Chrome-based workflow |
| TaskPaper | Task management — redundant with Linear/ClickUp |
| TextSoap | Text cleaning — CLI tools preferred |
| Timing | Time tracking — not actively tracking |
| Typeface | Font manager — not needed |
| Whisk | HTML/CSS editor — nvim/Cursor covers |
| Workspaces | Project launcher — sesh/tmux covers |

---

## Redundancy Map

| Category | Apps Installed | Primary | Action |
|----------|---------------|---------|--------|
| Clipboard | Maccy, Paste, PastePal, Raycast | **Maccy** | Remove Paste, PastePal |
| Calculator | Soulver, Numi, Plus, PocketCAS, Euclid | **Soulver** | Remove rest |
| PDF | Nitro PDF Pro, PDF Pals, PDF Search, PDF Squeezer | **Nitro PDF Pro** | Remove rest |
| Window Mgmt | Raycast, Magnet, Moom Classic, BetterTouchTool, AeroSpace (disabled) | **Raycast + BTT** | AeroSpace stays disabled |
| Browsers | Brave, Chrome, Chromium, Opera, Vivaldi, Orion, Safari | **Brave + Chrome** | Keep others for testing |
| Note-taking | Obsidian, Notion, Craft, RemNote, NotePlan, SideNotes | **Obsidian** | Notion secondary; rest remove |
| Task Mgmt | Linear, ClickUp, Things3, GoodTask, TaskPaper, Planny, MinimaList | **Linear + ClickUp + Things3** | Remove rest |

---

## Financial Analysis

| Service | Monthly Cost | Status |
|---------|-------------|--------|
| Setapp | $9.99 | **KEEP** — 9 keeper apps justify cost |
| Claude Max | $100.00 | KEEP — primary executor |
| ChatGPT Plus | $20.00 | KEEP — Psyche agent + Codex CLI |
| Google AI Pro | $20.00 | KEEP — Cartographer agent |
| NVIDIA NIM | Free tier | KEEP — Ajna agent (evaluation) |

**Total monthly AI+tool cost**: ~$150/mo

---

## Action Items

1. [x] Catalog all apps in DYN-FUNCTIONS.csv
2. [ ] SOVEREIGN: Review Setapp keeper list — confirm or override
3. [ ] SOVEREIGN: Schedule app cleanup session (uninstall cancellation candidates)
4. [ ] Add keeper apps to ontology substrate (apps table)
5. [ ] Update DYN-API_PRICING.csv with Setapp line item

---

*Generated by Commander (COO) as part of SYN-56 tool onboarding audit.*
