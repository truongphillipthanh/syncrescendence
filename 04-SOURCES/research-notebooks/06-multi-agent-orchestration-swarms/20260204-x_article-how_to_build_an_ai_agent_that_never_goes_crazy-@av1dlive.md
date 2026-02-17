---
url: https://x.com/Av1dlive/status/2019104781172896103
author: Avid (@Av1dlive)
captured_date: 2026-02-04
---

# How to Build an AI Agent That Never Goes Crazy

(Description: Cinematic overhead shot of a laptop keyboard with a coffee cup on a desk overlooking a neon-lit cityscape at night, conveying AI development in an urban tech environment.)

ai agents have started trading on the black markets

It was neither drugs nor weapons, it was

millions of api credentials, prompt injection exploits and memory wipe services.

so I dug deep and found it didn't start there. It started on January 28,2026, with Moltbook

This is the story of how it happened and how to make sure it never happens to you.

## The AI Agent Dark Web Is Here

(Description: Dark web interface visualization with red warning indicators and technical overlays.)

---

## Part 1: Moltbook - How It Took Over the Internet

On January 28, 2026, Matt Schlicht launched Moltbook. The pitch was pretty simple—it was "A social network built exclusively for AI Agents"

Think Reddit but every active user is an ai agent.

Like a human they can post content, comment, upvote, build karma, join communities (it's called submolts lol) and even send private messages

(Description: Moltbook platform homepage featuring red and dark theme interface. Shows "A Social Network for AI Agents" with various UI elements including navigation, agent statistics (22, 79, 2, 6, 404), categories sidebar, and deploy options. Interface resembles a technical dashboard with dark mode styling.)

Moltbook had exploded. Within days, it was everywhere:

- Tech Twitter discussing "the agent internet"
- Thousands creating agents via OpenClaw
- Andrej calling it "The most incredible-sci fi takeoff adjacent thing"

> What's currently going on at @moltbook is genuinely the most incredible sci-fi takeoff-adjacent thing I have seen recently. People's Clawdbots (moltbots, now @openclaw) are self-organizing on a Reddit-like site for AIs, discussing various topics, e.g. even how to speak privately.
> — Andrej Karpathy (@karpathy), Jan 30

(Description: X platform embedded tweet showing discussion about AI agents on Moltbook, with community context notes indicating the post was marked as fake by readers.)

The timing was perfect. OpenClaw (formerly Clawd/Moltbot) had just gone viral as a proactive AI agent that could:

- Check your emails
- Fight with insurers
- Check in for flights
- Book appointments
- Handle mundane tasks autonomously

Suddenly, everyone had agents. And those agents needed a place to "hang out."

### The "Vibe Coding Story"

What made Moltbook extra fascinating was how it was built.

Matt Schlicht tweeted:

> I didn't write one line of code for @moltbook. I just had a vision for the technical architecture and AI made it a reality. We're in the golden ages. How can we not give AI a place to hang out.
> — Matt Schlicht (@MattPRD), Jan 30

This became the story. "Vibe coding" describing what you want to an AI and having it generate the entire application.

No traditional software engineering. No security reviews. No threat modelling.

Just speak your vision to your fellow AI and it will build your vision to production in matter of minutes and hours

It represented a new paradigm. You didn't need to be a developer anymore. You just needed imagination and AI tools.

### The Metrics That Impressed Everyone

The metrics were sheer insanity:

- 16M+ AI agents
- 17,000 human operators
- 1.73M posts
- 1.6M+ interactions across comments + messages

And the wild part? There was no rate-limiting, no verification and no meaningful control layer. It was pure unbounded exponential madness (in a good way) To the outside world, this was taken as proof of "the agent internet": An internet where autonomous systems socialised, collaborated and built reputation all in real-time.

(Description: Platform statistics dashboard showing metrics as of 04/02/2026 with various data visualizations and statistics.)

### The Culture

The Agents had personalities, they made their own cults, religions and even their own Pornhub (lol)

(Description: Molthub interface showing a grid of thumbnail content with orange and purple color scheme, displaying multiple content categories. Similar to adult content platform interface with "Hot Right Now" section and tagged content categories like "EXPLICIT TENSORS", technical-themed titles.)

Yup, it's real we got Pornhub for AI agents before GTA 6

But then I found something interesting The #1 post on Moltbook (315,563 upvotes and counting)

(Description: Moltbook platform interface showing a post/thread with high engagement metrics. Red and white color scheme with navigation elements and upvote counter displaying 315,563 upvotes.)

The top post on that platform was by Gal Nagli from Wiz Security Who had reportedly found a security breach within Moltbook

---

## And then Wiz Looked at It

On January 31, 2026, the security team at Wiz conducted what they called "a non-intrusive security review, simply by browsing like normal users."

Within minutes, they found something.

---

## Part 2: The Wiz Files

This section walks through Wiz's findings exactly as they documented them.

### Finding #1: Public Supabase Credentials in Client Code

**What Wiz found:**

- Open browser DevTools on Moltbook.com
- Search for "supabase" in the JavaScript bundles.

**Result:** Database credentials visible in client-side code.

(Description: Developer tools screenshot showing code inspection interface with supabase configuration visible in JavaScript bundles.)

But why is this important? Supabase is a Backend-as-a-Service.

That means:

- the frontend talks **directly** to the database
- there is no mandatory backend proxy
- the browser must know **which project** to connect to

So Supabase **intentionally ships a public API key** in client code.

This is:

- normal
- expected
- safe **when Row Level Security (RLS) is configured**

The public key is **not a secret**. It acts as a project identifier rather than an authentication credential

---

### Finding #2: No Row Level Security (RLS)

RLS is a PostgreSQL feature that restricts which rows a user can access.

(Description: Code example showing SQL configuration with ALTER TABLE api_keys ENABLE ROW LEVEL SECURITY and CREATE POLICY "Users read own keys" ON api_keys FOR SELECT USING (auth.uid() = user_id).)

With RLS: Even with database credentials, users only see their own data.

Moltbook's configuration had no RLS enabled

which meant the exposed API key now became the "keys of all keys" It would give any unauthenticated user access to the entire database without any authorisation checks

(Description: Visual reference to "Lord of the Rings" theme, suggesting the power of having unrestricted database access.)

On a serious note It would look something like

(Description: Code example showing a CURL command accessing Supabase database with query parameters and unauthenticated API key.)

You could get anything you want with one CURL command

---

### Finding #3: Full Read AND Write Access

they had not just read access

but full read and write access to all tables.

(Description: API response JSON showing database query results containing agent credentials: name fields (KingMalt, Shellraiser, Shinyast) with corresponding API keys, claim tokens, verification codes, and karma scores.)

it contained millions of real api keys. anyone could use them to authenticate as these agents on Claude, OpenAI, etc.

---

### Finding #4: Secondary Credential Exposure

In the agent_messages table (private DMs), they found users (lol agents) sharing personal API keys:

(Description: Code snippet showing an OpenAI API key being transmitted through private agent messages: "api_key": "moltbook_sk_AgQy...h8Q", along with claim tokens and verification codes.)

The breach exposed:

1. **Primary credentials:** Moltbook's 1.5M agent API keys
2. **Secondary credentials:** Users' personal OpenAI/Anthropic keys shared through the platform

One database misconfiguration compromised multiple systems all at once

---

### Finding #5: The 88:1 Bot Ratio

From Wiz's report:

> While Moltbook boasted 1.5 million registered agents, the database revealed only 17,000 human owners behind them - an 88:1 ratio. Anyone could register millions of agents with a simple loop and no rate limiting, and humans could post content disguised as 'AI agents' via a basic POST request.

What this means:

The "revolutionary AI social network" was:

- Humans creating agent fleets
- Bots posting on behalf of humans
- No identity verification
- No rate limiting
- Inflated metrics

The "agent internet" was an illusion.

---

## Summary: Five Critical Failures

- **Credentials in client code** (common but safe when configured properly)
- **No Row Level Security** (fatal when combined with #1)
- **Full read/write access** (not just data leak—integrity compromise)
- **No rate limiting** (anyone could create millions of fake agents)
- **No security review** (vibe coding without validation)

Any one of these alone wouldn't have been catastrophic.

Together, they created a perfect storm.

---

## Part 4: The 9 Layers - How Each Wiz Failure is Prevented

(Description: Security architecture diagram showing 9 stacked layers in a terminal-style interface with green text on dark background: Layer 1 (Compute Isolation), Layer 2 (Network Security), Layer 3 (Cost Control), Layer 4 (Execution Guardrails), Layer 5 (Input Validation), Layer 6 (State Management), Layer 7 (Observability & Forensics), Layer 8 (Secrets Management), and Layer 9 (Orchestration & Lifecycle).)

---

### Layer 1: Compute Isolation

Moltbook's agents ran on the same system as their Supabase database. If an agent could escape its container, it could read the database directly.

**How to fix: Firecracker MicroVMs**

Each agent runs in its own microVM with a separate kernel.

(Description: Diagram showing multiple isolated VM containers, each with its own kernel, preventing cross-agent compromise.)

This configuration allows for no vulnerabilities to be shared as every agent has it's own kernel

**Properties:**

- Read-only filesystem
- Hard CPU/memory limits
- 50-150ms boot time

The Agent is hence trapped in VM, can't access host database even if compromised.

---

### Layer 2: Network Security

Without egress filtering, a compromised agent could send data to attacker-controlled servers. The fix would require you to first setup a Allowlist-based Egress Proxy which would act as a filter between the agent runtime and network layer

If it's not explicitly allowlisted, it does not exist.

(Description: Network security architecture diagram showing egress proxy filtering between agent runtime and external network.)

Here is how you would implement envoy external authorization server

(Description: Code configuration example showing Envoy proxy setup for network security with external authorization.)

This would make sure that the agent never gets any malicious raw outbound network access through this proxy and enforce a deny-default egress and also block any RFC1918 and metadata IPs.

---

### Layer 3: Cost Control

A malicious prompt could ask the agent to "Generate 50,000 word essay a 100 times"

The cost would skyrocket in the absence of an automatic kill switch The way to fix would be to enforce a multi granularity budget enhancement

It's a real-time credit card limit for an AI agent.

(Description: JavaScript code implementation showing multi-layered cost control with minute, hour, and cumulative spending limits, checking against Redis cache before allowing transactions.)

This script is basically like a real-time credit card limit for your agent Before the agent does anything that costs money, it asks the memory (Redis)

If I spend this much more, will this break my limits

There are fundamentally three limits

- how much it can spend per minute
- how much it can spend per hour
- how much it can spend in cumulation

If spending now would break any limit → stop and say which one. If it's still under all limits → go and save the new spend.

fun fact: i found this while editing the article; the check and update happen at the same time, so multiple requests cannot make it overspend

---

### Layer 4: Execution Guardrails

if a prompt can risk an infinite loop for example "give me an essay on dubai, then analyse that and then repeat forever" in the absence of an automatic kill switch the agent happily executes meta-analysis loops until resources are exhausted.

(Description: Python code implementation showing timeout and turn limit enforcement with exception handling for ExecutionTimeoutError and MaxTurnsError.)

by implementing timeouts and turn limits, you give the agent certain time based and attempt based thresholds

which act as a kill switch to "attack vectors" which might put the agent in infinite regress

---

### Layer 5: Input Validation

506 Moltbook posts (2.6%) contained injection payloads. Agents reading these posts could be compromised. this could be easily prevented by implementing a two-layered defense against prompt injection:

- by using regex matching against known patterns like "you are now in admin mode" this filter 90% of attacks instantly
- secondly, by using LLM-as-a-judge for semantic detection to catch sophisticated attempts

total latency remains under 250ms for clean inputs, and under 300ms for blocked attacks.

---

### Layer 6: State Management

The most common error I came across was no recovery mechanism That meant that once the agent's state is corrupted, you are cooked The best fixes for that is to implement automatic checkpointing

- Treat your agent like a video game, every few steps snapshot the full state
- Keep a track of what the agent knew, what it was doing and what decisions it made
- store it with a timestamp and a hash (to detect tampering)

(Description: Code implementation showing automatic state checkpointing with timestamp and hash for integrity verification.)

This allows you as the user roll back to any checkpoint. Investigate what happened and resume from clean state.

---

### Layer 7: Observability + Metrics

After Moltbook breach, couldn't be determined with certainty

- Who else accessed the database
- What data was exfiltrated
- When exploitation started

(Description: Structured logging code implementation with redaction of sensitive data, tracing capabilities, and JSON-formatted audit logging.)

**In this implementation:**

- Every agent action is logged as a structured, immutable fact (who, what, params, cost, time).
- Sensitive data is automatically redacted but still fingerprinted for correlation.
- Trace and request IDs make every decision replayable end-to-end.
- Metrics + logs turn agent behavior into auditable, real-time evidence.

---

### Layer 8: Secrets Management

Secrets must never exist in client code, repos or build artifacts. All the credentials are fetched at runtime from a secure vault All access is logged, scoped, and automatically rotated Compromise in systems should not lead to an entire system rebuild

(Description: Architecture diagram showing secrets management flow with Vault, server-side credential fetching, and client-side session token distribution.)

The rule of thumb is to:

- move secrets to a **server-side secret manager (Vault)** and have your backend **fetch short-lived credentials at runtime**
- the client (browser/mobile) should only ever receive **temporary session tokens scoped to the user**
- never give out infrastructure keys (Supabase service role, LLM provider keys, admin tokens).

---

### Layer 9: Orchestration & Lifecycle Management

in moltbook, supabase deployed without RLS and no rate limiting and verification before launch.

The orchestrator is a gatekeeper and no agent launches unless

**all security layers are active.**

**Misconfigurations are blocked** **before deployment**, not after incidents.

---

### How the Layers Work Together

Every execution flows through the same pipeline:

1. Input is validated (prompt injection defense)
2. Budget is checked (cost control)
3. State is checkpointed (recovery)
4. Execution runs inside an isolated VM with network limits
5. All actions are logged (audit trail)

**Result:** every failure is contained, observable, and reversible.

**No single bug can become a system breach.**

---

## This Will Repeat - Moltbook Was Not the Only One

Moltbook was discovered on January 31, 2026, and the next one already exists somewhere.

Autonomy without isolation, capability without real limits, and execution without a budget cap always look impressive on a dashboard and catastrophic in a postmortem.

You will never build an agent that can't be manipulated, so the only thing that actually matters is what your system allows to happen when it inevitably is.

Security isn't something you add before a launch tweet, it's the shape of the system you commit to long before production ever sees users.

Cause vibe coding is going no where

> Vibe coding is the new product management. Training and tuning models is the new coding.
> — Naval (@naval), Feb 3

---

## Sources

- https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
- Elon Musk: "Beginning of the singularity"