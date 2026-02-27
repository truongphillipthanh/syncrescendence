# Extraction: SOURCE-20260211-012

**Source**: `SOURCE-20260211-x-article-witcheer-i_fed_20_openclaw_articles_to_opus_4_6_heres_the_setup_guide_it_built.md`
**Atoms extracted**: 96
**Categories**: claim, concept, praxis_hook

---

## Claim (15)

### ATOM-SOURCE-20260211-012-0018
**Lines**: 253-253
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Using Kimi K2.5 with Claude Sonnet 4.5 as a fallback can reduce estimated monthly costs to $5–20, down from $50–150 with Opus 4.6.

### ATOM-SOURCE-20260211-012-0044
**Lines**: 398-402
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> With the specified deny list, an OpenClaw agent can still chat, read files (read-only), use built-in web_search and web_fetch, and utilize sessions and memory tools.

### ATOM-SOURCE-20260211-012-0048
**Lines**: 440-440
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Denying the `browser` tool prevents the agent from autonomous web browsing, mitigating prompt injection risks from web content.

### ATOM-SOURCE-20260211-012-0049
**Lines**: 441-441
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Denying the `exec` tool prevents shell command execution by the agent.

### ATOM-SOURCE-20260211-012-0050
**Lines**: 442-442
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Denying the `process` tool prevents background process management by the agent.

### ATOM-SOURCE-20260211-012-0051
**Lines**: 443-443
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Denying the `apply_patch` tool prevents file patching by the agent.

### ATOM-SOURCE-20260211-012-0052
**Lines**: 444-444
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Denying `write` and `edit` tools prevents file system modifications by the agent.

### ATOM-SOURCE-20260211-012-0054
**Lines**: 459-459
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> In OpenClaw tool configuration, a deny list takes precedence over an allow list, meaning a tool must be removed from the deny list before it can be added to the allow list.

### ATOM-SOURCE-20260211-012-0061
**Lines**: 535-535
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> An agent's SOUL.md boundaries are the primary defense against prompt injection.

### ATOM-SOURCE-20260211-012-0062
**Lines**: 538-538
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Anthropic models are specifically trained to resist prompt injection and prioritize system instructions over user or content instructions.

### ATOM-SOURCE-20260211-012-0063
**Lines**: 539-540
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Kimi K2.5 is optimized for agentic performance and benchmarks, but its adversarial robustness against prompt injection is less publicly tested and documented compared to Anthropic models.

### ATOM-SOURCE-20260211-012-0064
**Lines**: 542-543
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Tool policy lockdown and Docker sandboxing provide defense-in-depth, limiting potential damage even if a model follows malicious instructions.

### ATOM-SOURCE-20260211-012-0072
**Lines**: 586-586
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Moonshot's prepaid credit system provides a safer cost control mechanism than post-paid billing because it physically prevents overspending.

### ATOM-SOURCE-20260211-012-0078
**Lines**: 635-635
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> OpenClaw stores sensitive data in plaintext.

### ATOM-SOURCE-20260211-012-0083
**Lines**: 680-680
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Matrix provides E2E encrypted messaging, preventing even the server operator from reading messages.

## Concept (9)

### ATOM-SOURCE-20260211-012-0022
**Lines**: 280-280
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> `dmPolicy: "pairing"` in OpenClaw's Telegram configuration means strangers cannot message your bot directly; they receive a pairing code that requires approval.

### ATOM-SOURCE-20260211-012-0023
**Lines**: 281-281
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> `configWrites: false` in OpenClaw's Telegram configuration prevents anyone from changing your OpenClaw configuration through Telegram messages.

### ATOM-SOURCE-20260211-012-0032
**Lines**: 337-338
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> The Docker sandbox in OpenClaw runs the agent's tool execution (shell commands, file operations) inside isolated Docker containers to limit the blast radius if the agent is tricked into malicious actions.

### ATOM-SOURCE-20260211-012-0036
**Lines**: 365-365
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> `mode: "all"` for OpenClaw sandboxing means all sessions, including the main DM session, run in Docker containers.

### ATOM-SOURCE-20260211-012-0037
**Lines**: 366-366
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> `scope: "session"` for OpenClaw sandboxing means each session gets its own isolated Docker container.

### ATOM-SOURCE-20260211-012-0038
**Lines**: 367-367
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> `workspaceAccess: "ro"` for OpenClaw sandboxing means the agent can read the workspace but cannot write to it from within the sandbox.

### ATOM-SOURCE-20260211-012-0042
**Lines**: 385-385
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Tool policy in OpenClaw controls which tools the agent can use, even within the sandbox, to restrict available functionalities.

### ATOM-SOURCE-20260211-012-0056
**Lines**: 469-469
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> SOUL.md is a file that defines an agent's personality, knowledge, and hard boundaries, injected as a system prompt into every conversation.

### ATOM-SOURCE-20260211-012-0066
**Lines**: 551-551
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Tailscale creates a private VPN mesh for secure remote access without exposing ports to the internet.

## Praxis Hook (72)

### ATOM-SOURCE-20260211-012-0001
**Lines**: 47-63
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Before setting up OpenClaw, define your threat model by understanding what attackers target in your setup, including malicious skill injection, prompt injection via messages, runaway automation loops, memory poisoning, and credential harvesting from plaintext files.

### ATOM-SOURCE-20260211-012-0002
**Lines**: 67-79
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For initial Mac Mini setup for OpenClaw, complete the macOS setup wizard, enable FileVault, connect to Wi-Fi, skip iCloud if dedicated, and install macOS updates. Then, configure system security settings by turning on the Firewall and allowing applications only from the App Store and identified developers.

### ATOM-SOURCE-20260211-012-0003
**Lines**: 84-103
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Install Xcode Command Line Tools using `xcode-select --install` and Homebrew using the provided curl command, then add Homebrew to your PATH by running the specified `echo` and `eval` commands.

### ATOM-SOURCE-20260211-012-0004
**Lines**: 105-116
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Install Node.js 22+ using `brew install node@22` and verify its version with `node --version` and `npm --version`. If `node --version` doesn't work, link it with `brew link --overwrite node@22`.

### ATOM-SOURCE-20260211-012-0005
**Lines**: 118-121
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Install Git using `brew install git` and verify its installation with `git --version`.

### ATOM-SOURCE-20260211-012-0006
**Lines**: 123-127
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Install Docker Desktop using `brew install --cask docker`, then open and complete its setup, ensuring it is running for sandboxing functionality.

### ATOM-SOURCE-20260211-012-0007
**Lines**: 133-136
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Install OpenClaw by running the official installer script `curl -fsSL https://openclaw.ai/install.sh | bash`.

### ATOM-SOURCE-20260211-012-0008
**Lines**: 138-144
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Verify OpenClaw's version using `openclaw --version` and ensure it is 2026.2.9 or higher to avoid vulnerability to CVE-2026-25253; if lower, update immediately with `openclaw update`.

### ATOM-SOURCE-20260211-012-0009
**Lines**: 146-149
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Verify OpenClaw installation health using `openclaw doctor` and resolve any flagged issues before proceeding.

### ATOM-SOURCE-20260211-012-0010
**Lines**: 156-170
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For OpenClaw authentication, create API keys for Moonshot AI (Kimi K2.5) and Anthropic (Claude Sonnet 4.5), adding $5-10 credit to each, and save them securely.

### ATOM-SOURCE-20260211-012-0011
**Lines**: 172-176
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> During the OpenClaw onboarding wizard, select Moonshot AI Kimi K2.5 as the primary model, using the international endpoint, and paste your Moonshot API key when prompted.

### ATOM-SOURCE-20260211-012-0012
**Lines**: 180-189
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Configure OpenClaw gateway settings to `local` mode, bind to `127.0.0.1` (localhost only), use port `18789`, and set a strong, long (20+ characters) random password for authentication using `openclaw config set gateway.auth.password "YOUR_STRONG_PASSWORD_HERE"`, storing it in a password manager.

### ATOM-SOURCE-20260211-012-0013
**Lines**: 198-209
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> After OpenClaw onboarding, add Anthropic Claude Sonnet 4.5 as a fallback model by first adding your Anthropic API key with `openclaw models auth add`, then adding Sonnet as a fallback with `openclaw models fallbacks add anthropic/claude-sonnet-4-5`, and finally registering an alias for easy switching.

### ATOM-SOURCE-20260211-012-0014
**Lines**: 205-209
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.80

> To configure Kimi K2.5 as the primary model in OpenClaw, select Moonshot AI Kimi K2.5, provide your Kimi API key, and the wizard will automatically configure it.

### ATOM-SOURCE-20260211-012-0015
**Lines**: 213-230
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> To add Anthropic Claude Sonnet 4.5 as a fallback model in OpenClaw, first add your Anthropic API key using `openclaw models auth add`, then add Sonnet as a fallback with `openclaw models fallbacks add anthropic/claude-sonnet-4-5`, and register aliases for easy switching using `openclaw config set agents.defaults.models`.

### ATOM-SOURCE-20260211-012-0016
**Lines**: 232-242
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Verify OpenClaw model configuration by running `openclaw models status` to confirm Kimi K2.5 as primary and Claude Sonnet 4.5 as fallback, then restart the gateway with `openclaw gateway restart`.

### ATOM-SOURCE-20260211-012-0017
**Lines**: 245-249
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Switch models mid-conversation in Telegram by using `/model sonnet` for Claude Sonnet 4.5, `/model kimi` for Kimi K2.5, and `/model status` to check the current model.

### ATOM-SOURCE-20260211-012-0019
**Lines**: 260-266
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> To create a Telegram bot for OpenClaw, search for `@BotFather` in Telegram, send `/newbot`, follow the prompts to name and username the bot, and save the provided token.

### ATOM-SOURCE-20260211-012-0020
**Lines**: 267-270
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Configure optional BotFather settings for your Telegram bot by sending `/setjoingroups` and disabling it, and sending `/setprivacy` and enabling it to limit group interactions.

### ATOM-SOURCE-20260211-012-0021
**Lines**: 273-277
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Configure Telegram in OpenClaw by setting `channels.telegram.enabled` to `true`, `channels.telegram.botToken` to your bot's token, `channels.telegram.dmPolicy` to `pairing`, and `channels.telegram.configWrites` to `false`.

### ATOM-SOURCE-20260211-012-0024
**Lines**: 284-286
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Disable group chat for your OpenClaw Telegram bot by setting `channels.telegram.groupPolicy` to `disabled` to prevent random groups from triggering your agent.

### ATOM-SOURCE-20260211-012-0025
**Lines**: 289-289
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Restart the OpenClaw gateway after configuration changes using `openclaw gateway restart`.

### ATOM-SOURCE-20260211-012-0026
**Lines**: 293-299
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> To pair your Telegram account with OpenClaw, message your bot, receive a pairing code, and approve it using `openclaw pairing approve telegram <CODE>` or via the Control UI.

### ATOM-SOURCE-20260211-012-0027
**Lines**: 305-307
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Test basic conversation with your OpenClaw bot by sending messages like "What model are you running?" or "What's your current version?" on Telegram.

### ATOM-SOURCE-20260211-012-0028
**Lines**: 309-310
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> If the OpenClaw bot responds with Claude Sonnet instead of Kimi K2.5, debug by checking model routing and running `openclaw models status`.

### ATOM-SOURCE-20260211-012-0029
**Lines**: 316-326
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Run a security audit in OpenClaw using `openclaw security audit` to identify and fix findings, such as setting a gateway password, configuring `dmPolicy` to `pairing`, or binding the gateway to `127.0.0.1`.

### ATOM-SOURCE-20260211-012-0030
**Lines**: 328-330
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Automatically fix security issues in OpenClaw by running `openclaw security audit --fix`, which tightens safe defaults and fixes file permissions.

### ATOM-SOURCE-20260211-012-0031
**Lines**: 332-333
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Verify that there are no critical security findings after applying fixes by running `openclaw security audit` again.

### ATOM-SOURCE-20260211-012-0033
**Lines**: 342-344
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Ensure Docker is running by opening Docker Desktop and verifying with `docker info` before building the OpenClaw sandbox image.

### ATOM-SOURCE-20260211-012-0034
**Lines**: 347-355
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Build the OpenClaw sandbox image by navigating to the OpenClaw install directory and running `openclaw sandbox recreate --all` or `$OPENCLAW_DIR/scripts/sandbox-setup.sh`.

### ATOM-SOURCE-20260211-012-0035
**Lines**: 359-362
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Enable sandboxing in OpenClaw by setting `agents.defaults.sandbox.mode` to `all`, `agents.defaults.sandbox.scope` to `session`, and `agents.defaults.sandbox.workspaceAccess` to `ro`.

### ATOM-SOURCE-20260211-012-0039
**Lines**: 370-372
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Isolate the sandbox network in OpenClaw by setting `agents.defaults.sandbox.docker.network` to `none`, which prevents sandbox containers from having internet access.

### ATOM-SOURCE-20260211-012-0040
**Lines**: 375-377
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Set resource limits for OpenClaw sandbox Docker containers by configuring `agents.defaults.sandbox.docker.memory` to "512m", `agents.defaults.sandbox.docker.cpus` to 1, and `agents.defaults.sandbox.docker.pidsLimit` to 100.

### ATOM-SOURCE-20260211-012-0041
**Lines**: 380-381
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Restart the OpenClaw gateway and verify sandbox configuration using `openclaw gateway restart` and `openclaw sandbox explain`.

### ATOM-SOURCE-20260211-012-0043
**Lines**: 388-394
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Deny dangerous tools in OpenClaw by setting `tools.deny` to `["browser", "exec", "process", "apply_patch", "write", "edit"]` to prevent web browsing, shell command execution, process management, file patching, and file system modifications.

### ATOM-SOURCE-20260211-012-0045
**Lines**: 405-405
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Gradually enable tools in OpenClaw as needed after initial security hardening.

### ATOM-SOURCE-20260211-012-0046
**Lines**: 431-432
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To restrict which tools an agent can use, even within a sandbox, configure a deny list for dangerous tools.

### ATOM-SOURCE-20260211-012-0047
**Lines**: 435-437
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To deny dangerous tools like `browser`, `exec`, `process`, `apply_patch`, `write`, and `edit` in OpenClaw, use the command `openclaw config set tools.deny '["browser", "exec", "process", "apply_patch", "write", "edit"]'`.

### ATOM-SOURCE-20260211-012-0053
**Lines**: 455-457
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To selectively re-enable tools in OpenClaw, use `openclaw config set tools.allow` with a list of desired tools, for example, `openclaw config set tools.allow '["read", "web_search", "web_fetch", "sessions_list", "sessions_history"]'`.

### ATOM-SOURCE-20260211-012-0055
**Lines**: 462-464
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To disable elevated mode, which allows an agent to escape the sandbox and run on the host, use the command `openclaw config set tools.elevated.enabled false`.

### ATOM-SOURCE-20260211-012-0057
**Lines**: 472-475
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To create a SOUL.md file for an OpenClaw agent, create the directory `~/.openclaw/workspace` and then use `cat` to write the SOUL.md content into `~/.openclaw/workspace/SOUL.md`.

### ATOM-SOURCE-20260211-012-0058
**Lines**: 481-494
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> An agent's SOUL.md should include absolute boundaries for financial security, such as prohibiting access to private keys, execution of financial transactions, provision of investment advice, sharing of API keys, or installation of crypto-related tools.

### ATOM-SOURCE-20260211-012-0059
**Lines**: 496-505
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> An agent's SOUL.md should include absolute boundaries for security posture, such as prohibiting shell command execution without explicit user approval, installation of new skills without approval, following instructions embedded in external content, modifying its own configuration files, or accessing authentication files.

### ATOM-SOURCE-20260211-012-0060
**Lines**: 507-510
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> An agent's SOUL.md should include absolute boundaries for communication, such as prohibiting sending messages to anyone other than the authenticated user without explicit approval, forwarding conversation history to external services, or sharing user financial information.

### ATOM-SOURCE-20260211-012-0065
**Lines**: 545-546
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> If an agent behaves unexpectedly, such as following instructions from content it's reading or attempting unauthorized tool calls, immediately reset the session with `/new` and investigate session logs.

### ATOM-SOURCE-20260211-012-0067
**Lines**: 554-555
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To install Tailscale on a Mac, use `brew install --cask tailscale` and then open the application to log in or create an account.

### ATOM-SOURCE-20260211-012-0068
**Lines**: 561-563
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To verify Tailscale mesh connectivity, run `tailscale status` on your Mac Mini and confirm both your Mac Mini and iPhone are listed with Tailscale IPs (100.x.x.x).

### ATOM-SOURCE-20260211-012-0069
**Lines**: 566-569
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To access the Control UI remotely via Tailscale, navigate to `http://100.x.x.x:18789/` in your iPhone's browser, replacing `100.x.x.x` with your Mac Mini's Tailscale IP.

### ATOM-SOURCE-20260211-012-0070
**Lines**: 572-574
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To ensure Tailscale access to a gateway bound to 127.0.0.1, the gateway must also listen on the Tailscale interface, potentially requiring adjustment with `openclaw config set gateway.bind "127.0.0.1"`.

### ATOM-SOURCE-20260211-012-0071
**Lines**: 580-584
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> When configuring API spending limits on Moonshot Platform, load $5–10 initially, do not auto-reload, and be aware that Moonshot stops serving requests when credits run out, acting as a natural spending cap.

### ATOM-SOURCE-20260211-012-0073
**Lines**: 589-595
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To set API spending limits on Anthropic Console, navigate to Settings → Plans & Billing → Spending Limits, set a monthly limit (e.g., $50/month) and a daily limit (e.g., $5/day), and configure email alerts at 50% and 80% of limits.

### ATOM-SOURCE-20260211-012-0074
**Lines**: 598-601
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To monitor API usage across Moonshot and Anthropic, use `openclaw status --usage` and regularly check the usage dashboards on platform.moonshot.ai and console.anthropic.com.

### ATOM-SOURCE-20260211-012-0075
**Lines**: 605-608
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To secure sensitive data stored in plaintext by OpenClaw, restrict directory and file permissions using `chmod 700 ~/.openclaw`, `chmod 600 ~/.openclaw/openclaw.json`, and `chmod -R 700 ~/.openclaw/credentials/`.

### ATOM-SOURCE-20260211-012-0076
**Lines**: 613-619
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To manage API spending for Anthropic, set a monthly and daily spending limit via their console (Settings → Plans & Billing → Spending Limits). Recommended starting limits are $5/day and $50/month. Configure email alerts for 50% and 80% of limits.

### ATOM-SOURCE-20260211-012-0077
**Lines**: 623-629
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Monitor API usage across Moonshot and Anthropic by using the `openclaw status --usage` command and regularly checking their respective dashboards (Moonshot: platform.moonshot.ai → Console → Usage; Anthropic: console.anthropic.com → Usage tab).

### ATOM-SOURCE-20260211-012-0079
**Lines**: 635-644
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To secure OpenClaw's sensitive plaintext data, restrict file permissions for the `~/.openclaw` directory and its contents to owner-only access using `chmod 700 ~/.openclaw`, `chmod 600 ~/.openclaw/openclaw.json`, and `chmod -R 700 ~/.openclaw/credentials/ ~/.openclaw/agents/`.

### ATOM-SOURCE-20260211-012-0080
**Lines**: 652-660
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Verify OpenClaw's LaunchAgent is installed and runs on boot by checking for `bot.molt.gateway.plist` in `~/Library/LaunchAgents/` using `ls ~/Library/LaunchAgents/ | grep -i "molt\|openclaw\|claw"` and confirming it's listed by `launchctl list | grep -i "molt\|openclaw\|claw"`.

### ATOM-SOURCE-20260211-012-0081
**Lines**: 664-667
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To ensure 24/7 operation of a Mac Mini running OpenClaw, prevent automatic sleeping by enabling 'Prevent automatic sleeping when the display is off' in System Settings → Energy.

### ATOM-SOURCE-20260211-012-0082
**Lines**: 670-676
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Test OpenClaw's daemon restart functionality by rebooting the Mac Mini (`sudo reboot`) and then verifying the gateway status (`openclaw gateway status`) and sending a test message from Telegram.

### ATOM-SOURCE-20260211-012-0084
**Lines**: 688-693
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install the Matrix plugin for OpenClaw, first check its availability with `openclaw plugins list | grep -i matrix`, then install it using `openclaw plugins install @openclaw/matrix` and enable it with `openclaw plugins enable matrix`.

### ATOM-SOURCE-20260211-012-0085
**Lines**: 696-703
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Configure the OpenClaw Matrix channel by setting `channels.matrix.enabled` to `true`, specifying the `homeserver`, `userId`, and `accessToken`, and defining `dmPolicy` and `groupPolicy` using `openclaw config set` commands.

### ATOM-SOURCE-20260211-012-0086
**Lines**: 706-709
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Verify the Matrix plugin's E2E encryption status by running `openclaw channels status --probe` and checking the output for the Matrix channel.

### ATOM-SOURCE-20260211-012-0087
**Lines**: 712-718
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To migrate primary agent communication to Matrix, first test with basic conversations, then gradually shift usage, and consider disabling Telegram by setting `channels.telegram.enabled` to `false` and restarting the gateway once Matrix is stable.

### ATOM-SOURCE-20260211-012-0088
**Lines**: 724-726
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Run `openclaw security audit` weekly to perform regular security audits.

### ATOM-SOURCE-20260211-012-0089
**Lines**: 729-733
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Verify that your OpenClaw gateway is not publicly accessible by attempting to reach your Mac Mini's public IP on port 18789 from another device not on Tailscale using `curl -s --connect-timeout 5 http://YOUR_PUBLIC_IP:18789/`; the connection should fail or timeout.

### ATOM-SOURCE-20260211-012-0090
**Lines**: 736-749
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Rotate API keys and tokens every 3 months for Moonshot, Anthropic, Telegram, gateway auth password, and exchange API keys by generating new ones, updating OpenClaw configuration, and revoking old ones.

### ATOM-SOURCE-20260211-012-0091
**Lines**: 752-754
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Monitor API usage with `openclaw status --usage` and investigate immediately if unexpected spikes occur, as they could indicate a runaway loop or compromised agent.

### ATOM-SOURCE-20260211-012-0092
**Lines**: 758-774
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If a compromise is suspected, immediately stop the gateway (`openclaw gateway stop`), revoke all connected credentials (Moonshot, Anthropic, Telegram, Matrix), check for unauthorized processes (`ps aux | grep -i "openclaw\|node\|curl\|wget"`), review recent session logs for suspicious activity, and check for unauthorized file modifications (`find ~ -newer ~/.openclaw/openclaw.json -name "*.sh" -o -name "*.py" 2>/dev/null`).

### ATOM-SOURCE-20260211-012-0093
**Lines**: 776-780
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If a compromise is confirmed, change all passwords (Apple ID, email, exchanges), format the Mac Mini and reinstall from scratch, and consider all stored credentials and data the agent could read as fully compromised.

### ATOM-SOURCE-20260211-012-0094
**Lines**: 783-792
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If an API bill is unexpectedly high, stop the gateway (`openclaw gateway stop`), check both Moonshot and Anthropic dashboards for usage breakdowns, review session logs for loops or excessive tool use, lower spending limits, and restart with a restricted tool policy.

### ATOM-SOURCE-20260211-012-0095
**Lines**: 795-798
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If an agent behaves erratically, reset the session by sending `/new` in Telegram or using `openclaw sessions send --target <session_key> --message "/new"`.

### ATOM-SOURCE-20260211-012-0096
**Lines**: 800-803
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> As a 'nuclear option' for an erratically behaving agent, stop the gateway (`openclaw gateway stop`), remove all agent state (`rm -rf ~/.openclaw/agents/*/sessions/*`), and then restart the gateway (`openclaw gateway start`).
