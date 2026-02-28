# Call Your OpenClaw over the phone using ElevenLabs Agents

*if you copy this article to your coding agent, it can perform many steps from it for you*

What if you could simply call your OpenClaw bot and ask how your coding agent is doing? Or ask it to remember something while you're driving? Or perhaps get a digest of recent moltbook bangers?

While OpenClaw supports text-to-speech and speech-to-text out of the box, it takes effort to make it truly conversational.

ElevenLabs Agents platform orchestrates all things voice, leaving your OpenClaw to be the brains.

## The Architecture

(Description: Diagram showing system architecture with five connected components: Twilio Phone connects to ElevenLabs Agents (Orchestration) via /chat/completions protocol, which connects to OpenClaw, which branches to three components: Tools, Memory, and Skills.)

ElevenLabs Agents handle turn taking, speech synthesis and recognition, phone integration, and other voice related things.

OpenClaw handles tools, memory and skills.

Systems interact using standard OpenAI `/chat/completions` protocol.

## Prerequisites

- ElevenLabs account
- OpenClaw installed and running
- ngrok installed
- A Twilio account (if you want phone numbers)

## Setting Up OpenClaw

In your openclaw.json, enable the chat completions endpoint:
```json
{
  "gateway": {
    "http": {
      "endpoints": {
        "chatCompletions": {
          "enabled": true
        }
      }
    }
  }
}
```

This exposes `/v1/chat/completions` on your gateway port. That's the universal endpoint ElevenLabs will use to interact with your OpenClaw.

## Exposing Your Claw with ngrok

Start your tunnel:
```bash
ngrok http 18789
```

(Replace 18789 with whatever port your gateway runs on.)

ngrok gives you a public URL like `https://your-unique-url.ngrok.io`. Keep this terminal open — you'll need that URL for the next step.

## Configuring ElevenLabs

In the ElevenLabs Agent:

1. Create a new ElevenLabs Agent
2. Under LLM settings, select **Custom LLM**

(Description: Screenshot of ElevenLabs Agent configuration interface showing the LLM settings panel with "Custom LLM" option highlighted by a red arrow.)

3. Set the URL to your ngrok endpoint: `https://your-unique-url.ngrok.io/v1/chat/completions`
4. Add your OpenClaw gateway token as the authentication header

(Description: Screenshot of ElevenLabs Agent configuration interface showing the Custom LLM settings panel with authentication header configuration and red arrows highlighting the URL field and API key field.)

Alternatively, instead of manually following the steps above, your coding agent can make these requests:

**Step 1: Create the secret**
```bash
curl -X POST https://api.elevenlabs.io/v1/convai/secrets \\
  -H "xi-api-key: YOUR_ELEVENLABS_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "type": "new",
    "name": "openclaw_gateway_token",
    "value": "YOUR_OPENCLAW_GATEWAY_TOKEN"
  }'
```

This returns a response with secret_id:
```json
{"type":"stored","secret_id":"abc123...","name":"openclaw_gateway_token"}
```

**Step 2: Create the agent**
```bash
curl -X POST https://api.elevenlabs.io/v1/convai/agents/create \\
  -H "xi-api-key: YOUR_ELEVENLABS_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "conversation_config": {
      "agent": {
        "language": "en",
        "prompt": {
          "llm": "custom-llm",
          "prompt": "You are a helpful assistant.",
          "custom_llm": {
            "url": "https://YOUR_NGROK_URL.ngrok-free.app/v1/chat/completions",
            "api_key": {"secret_id": "RETURNED_SECRET_ID"}
          }
        }
      }
    }
  }'
```

Replace:
- `YOUR_ELEVENLABS_API_KEY` – your ElevenLabs API key
- `YOUR_OPENCLAW_GATEWAY_TOKEN` – from `~/.openclaw/openclaw.json` under `gateway.auth.token`
- `YOUR_NGROK_URL` – your ngrok subdomain
- `RETURNED_SECRET_ID` – the secret_id from step 1

ElevenLabs will now route all conversation turns through your Claw. It sends the full message history on each turn, so your assistant has complete context.

At this stage, you can already talk to your OpenClaw bot using your ElevenLabs agent!

## Attaching a Phone Number

This is where it gets interesting.

1. In Twilio, purchase a phone number
2. In the ElevenLabs agent settings, go to the Phone section

(Description: Screenshot of ElevenLabs Phone Numbers configuration interface showing the "Manage credentials" button with a red arrow pointing to it, and a "No phone numbers" message indicating no numbers are currently set up.)

3. Enter your Twilio credentials (Account SID and Auth Token)
4. Connect your Twilio number to the agent

(Description: Screenshot of ElevenLabs Phone Numbers configuration interface showing the Phone section with red arrows pointing to the Twilio Account SID field and the "From Twilio" / "From SIP Trunk" options for adding credentials.)

That's it. Your Claw now answers the phone! 🦞

---

**Engagement metrics:** 66 replies, 240 reposts, 1.8K likes, 3.1K bookmarks, 536.4K views

**Published:** 1:28 PM · Feb 3, 2026