# How to Build an Open Source AI Assistant That Never Sleeps. (2.0)
![OpenClaw Agent Interface](https://x.com/YJstacked/status/2022371168469254168/media/2022370801362833410)
(Description: Futuristic holographic interface showing a red glowing spherical AI agent at the center labeled "OpenClaw" with radiating light paths. Surrounding the agent are multiple smartphones, laptops, and displays arranged in a circle showing data dashboards, world maps with network overlays, and analytics panels. The environment features neon blue and red lighting with transparent glass panels and sci-fi architecture.)
Most people are still opening a browser tab, typing a prompt, copying the answer somewhere, and closing the tab. That loop has a ceiling.
OpenClaw removes the ceiling entirely. Before that, if you want us to set this up for you or automate different business operations head here - https://tally.so/r/mZbV0a
## WHAT OPENCLAW ACTUALLY IS
OpenClaw is an open source framework (MIT licensed) that turns your own hardware into a persistent AI agent you fully control. It bridges your messaging apps directly to AI models and gives the agent the ability to take actions, not just respond to text.
You message your agent through WhatsApp, Telegram, Discord, iMessage, or Mattermost. The agent persists memory across sessions, can execute code, browse the web, manage files, and run automated workflows without you supervising each step.
It runs continuously in the background. It persists memory across sessions. It acts.
**One thing before you go further:** if you give it runtime and filesystem tools, it can do real damage. Pairing, sandboxing, and allowlists are not optional. More on this below.
Built on Node.js v22 or higher. A WebSocket gateway manages communication between your messaging channels, agents, and tools. A skills system works like plugins for adding capabilities. Works with Claude, GPT, local models via Ollama, DeepSeek, Qwen, Gemini, and others via connectors and providers.
**Platform support:** macOS with native menu bar integration. Linux via systemd daemon. Windows via WSL2. VPS deployment from around $5 a month for always-on operation. Docker for containerized isolation.
Start at [openclaw.ai](https://openclaw.ai). Documentation at [docs.openclaw.ai](https://docs.openclaw.ai). Main repo at [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw).
## WHY THIS IS DIFFERENT
Most AI tools require you to show up. You open them, ask something, get a result, leave.
OpenClaw inverts that relationship.
### The practical difference:
**Without OpenClaw:** Ask Claude to write an email. Copy it to Gmail. Ask Claude to schedule a reminder. Manually add it to your calendar. Four context switches. Four places something gets dropped.
**With OpenClaw:** You say handle this. The agent writes the email, sends it, creates the calendar event, sets the reminder, and updates your task list. One instruction.
That is not an incremental improvement. It is a different way of working with AI entirely.
## THREE THINGS PEOPLE ARE ACTUALLY RUNNING
### Morning intelligence brief
Calendar, inbox, and news feeds checked automatically every morning. Priorities ranked, conflicts flagged, meeting context pulled from previous conversations. Complete brief sent to your phone before you wake up. This requires setting up integrations and relevant skills. It takes time to build. People who have it running do not go back.
### Competitor and price monitoring
Agent checks target pages on a schedule, detects changes, and sends an alert. No manual checking. No missed updates. Set it once.
### Development assistant
Agent reads your repo, generates solutions to errors you paste in, applies patches to files, and runs tests. The conversation becomes the development environment. No more switching between your IDE and a chat window.
## HOW TO SET IT UP
**Time investment:** 1 to 2 hours for a working basic setup. Another 2 to 3 hours to customize.
**Cost:** Free on your own hardware. From around $5 a month for a VPS. Plus API costs, which matter more than people expect. Heavy users report $50 to $200 a month with active agent loops running tools. Set spending alerts on your API dashboard from day one.
### The core installation path:
**Install OpenClaw:**
```
npm install -g openclaw@latest
```
**Run onboarding:**
```
openclaw onboard --install-daemon
```
This walks you through gateway configuration, API key entry for your provider of choice, runtime selection (stay on Node.js), daemon setup for your OS, and initial channel connection.
Config is stored under `~/.openclaw/`. The workspace directory where your agent's memory and skills live is configurable during setup.
Connect Telegram first. It is the simplest channel to get working and the best place to test before adding others.
### For manual config, edit `~/.openclaw/openclaw.json`:
```json
{
  "auth": {
    "profiles": {
      "claude": {
        "apiKey": "sk-ant-your-key-here"
      }
    }
  },
  "agents": {
    "defaults": {
      "model": "claude-sonnet-4-5-20250929"
    }
  }
}
```
Use the built-in status and doctor commands to validate the gateway and channels after setup. The gateway runs on port 18789 by default and you can access the dashboard at `http://127.0.0.1:18789/` in your browser.
### Connecting channels:
**Telegram:** Create a bot via BotFather. Copy the token. Paste when prompted. Set DM policy to pairing.
**WhatsApp:** QR code appears in terminal. Scan from your phone under Settings, Linked Devices.
**Discord:** Create a Discord application. Generate a bot token. Set group policy to allowlist to control which servers the agent joins.
**iMessage (macOS only):** Requires accessibility and automation permissions in System Preferences.
### Channel config:
```json
{
  "channels": {
    "telegram": {
      "dmPolicy": "pairing",
      "groupPolicy": "disabled",
      "streamMode": "partial"
    },
    "whatsapp": {
      "dmPolicy": "pairing",
      "groupPolicy": "allowlist"
    }
  }
}
```
### Customizing your workspace:
**IDENTITY.md** defines the persona. **USER.md** gives the agent context about you, your schedule, your projects, your preferences. **MEMORY.md** is the persistent knowledge index that grows over time. The skills directory holds installed capabilities.
### Installing skills:
Skills extend what the agent can actually do. They are available through the OpenClaw skills repository at [github.com/openclaw/skills](https://github.com/openclaw/skills) and community maintained lists.
To install from within your agent conversation:
```
Install skill: brave-search
```
**Review the code before confirming. Do not skip this regardless of the source.**
**Core skills worth installing early:** Brave Search for web queries. Browser Control for headless automation, form filling, and data extraction. GitHub for repo management. Whisper for voice transcription. Code Execution for sandboxed code running. Calendar for Google Calendar. Email for Gmail.
You can also instruct the agent to write a custom skill for a specific need. It generates the code. You review it. You install it. Always read what it wrote.
### VPS deployment for 24/7 operation:
SSH into a Hetzner or DigitalOcean instance. Install Node.js. Clone the repo or install via npm. Run openclaw onboard. Set up Tailscale for secure access without exposing ports:
```
openclaw gateway --bind tailnet --token <tailscale-token>
```
### Docker:
```
docker pull openclaw/openclaw:latest
docker run -d --name openclaw \\
  -v ~/clawd:/workspace \\
  -e CLAUDE_API_KEY=your-key \\
  openclaw/openclaw
```
### Linux persistence after logout:
```
sudo loginctl enable-linger $USER
```
## SECURITY
**This is not the section to skim.**
**Pairing system:** When someone first messages your agent they receive a pairing code. You manually approve it before they can interact. Never disable this.
**Allowlist groups:** Do not let the agent join arbitrary group chats. Use allowlist mode.
**Keep sandboxing enabled:** Default behavior provides isolation. Disabling it for convenience is how serious incidents happen. Only change this if you understand exactly what you are exposing.
**Review every skill before installing:** Skills run arbitrary code. This includes skills the agent writes. Most documented security incidents in the OpenClaw community trace back to unreviewed skills or sandboxing being turned off.
**Use allowlists, sandboxing, and strict tool policies to resist prompt injection:** Malicious content in web pages or documents the agent reads can attempt to hijack behavior. Keep your tool permissions as narrow as possible for each task.
**Secure your API keys:** Environment variables or secure config files. Never in a git repository.
**Back up your workspace directory regularly:** It contains your agent's memory and configuration.
**Monitor API spend obsessively:** Agentic loops with tool use chain into many more API calls than you expect. What looks like a simple task can become hundreds of calls. Set alerts. Check them daily until you know your patterns.
## YOUR FIRST WEEK
**Day one:** Install and connect Telegram only.
**Day two:** Customize IDENTITY.md and USER.md. Have conversations. Build memory context.
**Day three:** Install Brave Search. Test research workflows.
**Day four:** Set up morning briefs. Add calendar integration if you want it.
**Day five:** Add GitHub skill if you are a developer. Test coding workflows.
**Day six:** Deploy to VPS if you want it running when your machine is off.
**Day seven:** Review what is working. Add one custom skill for something specific to your workflow.
Start minimal. Use it daily. Expand deliberately. The people who try to connect everything on day one consistently abandon it.
## THE ACTUAL MATH
If you reclaim 30 minutes a day through automation that is 182 hours a year. Over four full work weeks recovered.
The difference between OpenClaw and every other AI tool is not capability. It is persistence. The agent is always running, always remembering, always ready to act without you rebuilding context from scratch.
The setup costs you three to four focused hours upfront. Most people will not make that investment.
The ones who do will be operating differently within a week.
Start at [openclaw.ai](https://openclaw.ai). Work with us - https://tally.so/r/mZbV0a
---
**Engagement:** 5 replies, 18 reposts, 145 likes, 267 bookmarks, 29.9K views  
**Posted:** 10:03 AM · Feb 13, 2026