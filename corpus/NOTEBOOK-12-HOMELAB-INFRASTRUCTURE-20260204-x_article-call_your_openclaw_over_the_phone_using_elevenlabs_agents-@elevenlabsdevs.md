# Call Your OpenClaw over the phone using ElevenLabs Agents

*if you copy this article to your coding agent, it can perform many steps from it for you*

What if you could simply call your OpenClaw bot and ask how your coding agent is doing? Or ask it to remember something while you're driving? Or perhaps get a digest of recent moltbook bangers?

While OpenClaw supports text-to-speech and speech-to-text out of the box, it takes effort to make it truly conversational.

ElevenLabs Agents platform orchestrates all things voice, leaving your OpenClaw to be the brains.

## The Architecture

(Description: A system architecture diagram with five connected components. On the left: "Twilio Phone" diamond shape. Connected via arrows to "ElevenLabs Agents (orchestration)" rectangular box in the center. The center box connects bidirectionally to "OpenClaw" with label "/chat/completions". From OpenClaw, arrows point right to three diamond shapes: "Tools", "Memory", and "Skills". Arrows are labeled showing the flow of voice orchestration and chat completions protocol.)

ElevenLabs Agents handle turn taking, speech synthesis and recognition, phone integration, and other voice related things. OpenClaw handles tools, memory and skills. Systems interact using standard OpenAI `/chat/completions` protocol.

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

This exposes /v1/chat/completions on your gateway port. That's the universal endpoint ElevenLabs will use to interact with your OpenClaw.

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

(Description: Screenshot of ElevenLabs agent configuration interface showing the Agent settings panel with various options including language selection, prompt settings, and LLM configuration dropdown menu pointing to "Custom LLM" option.)

3. Set the URL to your ngrok endpoint: `https://your-unique-url.ngrok.io/v1/chat/completions`
4. Add your OpenClaw gateway token as the authentication header

(Description: Screenshot showing the LLM settings panel with fields for Server URL and API Key configuration, with red arrows highlighting where to input the ngrok endpoint and authentication token.)

Alternatively, instead of manually following the steps above, your coding agent can make these requests:

### Step 1: Create the secret
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

### Step 2: Create the agent
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
            "api_key": {
              "secret_id": "RETURNED_SECRET_ID"
            }
          }
        }
      }
    }
  }'
```

Replace:
- `YOUR_ELEVENLABS_API_KEY` – your ElevenLabs API key
- `YOUR_OPENCLAW_GATEWAY_TOKEN` – from ~/.openclaw/openclaw.json under gateway.auth.token
- `YOUR_NGROK_URL` – your ngrok subdomain
- `RETURNED_SECRET_ID` – the secret_id from step 1

ElevenLabs will now route all conversation turns through your Claw. It sends the full message history on each turn, so your assistant has complete context.

At this stage, you can already talk to your OpenClaw bot using your ElevenLabs agent!

## Attaching a Phone Number

This is where it gets interesting.

1. In Twilio, purchase a phone number
2. In the ElevenLabs agent settings, go to the Phone section

(Description: Screenshot of ElevenLabs dashboard showing the "Phone Numbers" section with interface elements for managing Twilio integration, displaying phone number management and configuration options with red arrows indicating the location of phone number attachment settings.)

3. Enter your Twilio credentials (Account SID and Auth Token)
4. Connect your Twilio number to the agent

That's it. Your Claw now answers the phone! 🦞

---

*Captured: February 3, 2026 at 1:28 PM*
*Views: 417.7K | Replies: 59 | Reposts: 206 | Likes: 1.6K | Bookmarks: 2.7K*