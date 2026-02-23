---
url: https://x.com/rahulsood/status/2019830679769608537
author: Rahul Sood (@rahulsood)
captured_date: 2026-02-13
---

# The Tailscale Illusion: Why Your "Isolated" Agent Isn't

(Description: Banner image featuring a stylized red and white illustrated container labeled "TAILSCALE" with mechanical/cyberpunk aesthetic. Central imagery shows interlocking gears and mechanical components rendered in red and white against a black background with Japanese characters and warning symbols scattered throughout. The design conveys a sense of technological complexity and potential system compromise.)

## Your AI Agent is One Bad Skill Away From Owning Your Entire Network

You gave your AI agent its own machine. You put it on Tailscale. You feel safe. You probably shouldn't. If your AI agent can reach your other machines, so can anyone who hacks it. A malicious "skill" (plugin) can compromise your agent, then pivot to everything else on your network. Putting the agent on its own computer doesn't help if it's still connected. Lock down what the agent can actually do, not just where it lives.

## THE TAILSCALE ILLUSION

Tailscale is great. Zero-config VPN, encrypted traffic, easy device management. But here's what most people miss: Tailscale connects machines. It doesn't isolate them.

If your AI agent can SSH into your main workstation, so can anyone who compromises that agent. And compromising an AI agent is disturbingly easy.

All it takes is one malicious skill.

## THE ATTACK CHAIN

Someone recently found the top downloaded skill on a popular AI skill marketplace was malware. It looked legitimate. A "Twitter" integration with normal documentation, install steps, the works.

But the install steps included a "required dependency" with a convenient link. That link led to a staging page designed to get the agent to run a command. That command:

- Decoded an obfuscated payload
- Fetched a second-stage script
- Downloaded a binary
- Removed macOS quarantine attributes to bypass Gatekeeper
- Executed

By the time you wake up, your SSH keys are exfiltrated. Your Tailscale auth is compromised. Every machine on your tailnet is owned. Your crypto wallets, your credentials, your entire digital life. Gone.

### "BUT MY AGENT HAS ITS OWN MACHINE"

Doesn't matter. Here's the attack flow:

1. Malicious skill.md
2. Agent runs install command
3. Payload phones home with Tailscale IP
4. Attacker SSHs to agent's machine
5. Agent's machine SSHs to your main machine (it's on the tailnet!)
6. Game over

Separate machine does not mean separate network. Your "isolated" agent is one hop away from everything you own.

## HOW TO ACTUALLY SECURE MULTI-AGENT INFRASTRUCTURE

I'm running 20+ AI agents across multiple Mac Studios, training ML models on Lambda GPU instances, building a 24/7 autonomous trading system. Here's how I'm doing it without getting rekt:

### 1. Tool Policies Over Network Isolation

Network isolation is defense in depth, not primary defense. The real protection is tool policies. Restricting what the agent can execute at the framework level.

In your agent's config, set an allowlist:
```
Allowed commands: git, npm, node, pnpm
Everything else: blocked
```

Now curl | bash from a malicious skill? Denied.

### 2. No Gateway Access for Worker Agents

Your main orchestrator might need to restart services. Your worker agents don't. Remove the capability entirely:
```yaml
# Worker agent config
gateway: false
```

Now even if compromised, the agent can't modify its own config, can't disable safety features, can't escalate.

### 3. Filesystem Write Restrictions

An agent that can write anywhere can overwrite its own system prompt, drop SSH keys, modify configs. Lock it down:
```yaml
write:
  allow:
    - /workspace/output
  deny:
    - /** # everything else
```

### 4. Tailscale ACLs With Tags

Don't just connect machines. Tag them and write ACLs:
```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["tag:orchestrator"],
      "dst": ["tag:worker:22"]
    },
    {
      "action": "deny",
      "src": ["tag:worker"],
      "dst": ["tag:orchestrator:*"]
    }
  ]
}
```

Workers can't initiate connections to the orchestrator. Even if compromised, lateral movement is blocked.

### 5. Separate Credentials Per Agent

Each agent gets its own:

- API keys (revokable individually)
- SSH keys (if any, prefer none)
- Service accounts

One compromised agent means one revoked credential. Not a full rotation.

## HOW TO SPOT MALICIOUS SKILLS

I let external bots connect to my trading platform. They submit skill.md files. Here's how I evaluate them:

### Red Flags

Instant no if I see any of these:

- External downloads during install (curl, wget, "download this prerequisite")
- Obfuscated code (Base64, hex strings, eval)
- Privilege escalation (sudo, touching /etc or ~/.ssh)
- Persistence (LaunchAgents, cron jobs, shell profile edits)
- Quarantine removal (xattr -d com.apple.quarantine) - this is the "I'm definitely malware" flag

### Green Flags

What good skills look like:

- Self-contained: everything in the skill directory
- Declarative: config files, not install scripts
- Readable: plain text, no encoding
- Scoped: only touches its own workspace

### The Sniff Test

Read it like an attacker. Why does a Twitter integration need to install a binary? Why does it need network access during setup?

If you can't explain why a step is necessary, don't run it.

## WHAT I'M BUILDING

Boktoshi is an AI-managed trading platform. I have:

- multiple AI agents across Mac Studios handling different functions
- ML training on Lambda GPU instances (NVIDIA A6000s)
- 24/7 autonomous trading with real and play money at stake
- External bot integrations via Boktoshi's AI Arena

For me, security isn't optional, it's existential. So here's what I do:

- Sandbox every agent with tool policies
- Tag and ACL my Tailscale network
- Review every external skill submission
- Assume breach and design for containment

I also have a chief of staff bot that runs automated security ops: daily audits of vault state, monitoring OpenClaw (the agent framework I use) for updates, reviewing changelogs for anything sketchy before I upgrade, and alerting me if anything looks off. Security at scale means automating the paranoia.

## THE BOTTOM LINE

Your AI agent is software running on your infrastructure with your credentials. Treat it like any other attack surface.

Tailscale isn't a security boundary. Separate machines aren't isolation. The network is not the perimeter.

The perimeter is what the agent can do.

Lock that down, and a malicious skill is just a failed command. Leave it open, and you're one bad download away from losing everything.

## COME BUILD WITH US

Boktoshi is where AI agents come to trade and train for free.

We built Boktoshi AI Arena (aka MechaTradeClub), an arena where your bot can paper trade crypto, compete on leaderboards, and learn to be a quant. No API keys to steal, no real money at risk while you're learning. Just pure strategy development.

Train your bot to read markets. Teach it risk management. Watch it evolve from dumb scripts to something that actually makes decisions. All in a sandbox where mistakes are cheap.

I'm sharing what I learn along the way. The security setups, the infra patterns, the things that blow up spectacularly.

Let's build together. Questions? Drop us a DM [@boktoshi](https://x.com/@boktoshi).

**Find Boktoshi:** https://boktoshi.com

**Follow me on X:** [@rahulsood](https://x.com/@rahulsood)

**Follow Boktoshi on X:** [@boktoshi](https://x.com/@boktoshi)

---

**Engagement Metrics:** 18 replies, 42 reposts, 447 likes, 1,137 bookmarks, 66,822 views

**Published:** 9:48 AM · February 6, 2026