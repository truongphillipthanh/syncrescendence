---
url: https://x.com/victormustar/status/2021964315994046897
author: Victor M (@victormustar)
captured_date: 2026-02-12
---

# Your MacBook Is a Local AI Agent

(Description: Black and white ink sketch illustration featuring a MacBook laptop centered in a swirling, organic landscape of branches and flowing lines. The image uses a high-contrast artistic style with intricate line work suggesting a natural, almost mystical computer environment.)

Your MacBook can run a fully local, offline AI agent that writes code, manages files, orchestrate complex tools by running shell commands. No API keys. No subscriptions. No data leaving your machine.

Apple Silicon's unified memory is the reason this works: the CPU and GPU share the same RAM, so your MacBook's full memory is available for inference. The model we'll use, GLM-4.7-Flash, has 30 billion parameters but only activates 3 billion per token (Mixture-of-Experts), giving it the knowledge of a large model at the speed of a small one. 59.2% on SWE-bench Verified, tool calling support, MIT licensed. 

You need 2 things to get started: a **server** to run the model and a **client** to turn it into an agent.

## Step 1: Launch your local AI server

### Install llama.cpp
```bash
brew install llama.cpp
```

### Launch llama.cpp server:
```bash
llama-server \\
  -hf unsloth/GLM-4.7-Flash-GGUF:UD-Q4_K_XL \\
  --jinja \\
  --temp 0.7 --top-p 1.0 --min-p 0.01 \\
  --repeat-penalty 1.0 --fit on \\
  --port 8080
```

This downloads the Unsloth GGUF (~18GB), auto-fits layers between GPU and CPU (--fit on), and starts an OpenAI-compatible API at http://localhost:8080. The sampling parameters (--temp 0.7 --top-p 1.0) are the Z.ai team's recommendation for tool-calling use cases. --jinja enables the chat template. --repeat-penalty 1.0 disables repeat penalty (important for this model).

### Which quantization fits your Mac?

- **8 GB**: Use a 7B model instead
- **16 GB**: UD-Q3_K_XL (tight fit, limited context)
- **24 GB**: UD-Q4_K_XL (sweet spot)
- **36 GB+**: UD-Q6_K (higher quality)

## Step 2: Connect Pi as your agent

Pi is a minimal terminal coding agent by Mario Zechner. Four tools: read, write, edit, bash. ~1,000 token system prompt.
```bash
npm install -g @mariozechner/pi-coding-agent
```

### Create ~/.pi/agent/models.json:
```json
{
  "providers": {
    "llama-cpp": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "none",
      "models": [{ "id": "GLM-4.7-Flash" }]
    }
  }
}
```

### Run it:
```bash
pi
```

Press `Ctrl+L`, select your local model, and start talking. Done. (warning Pi run)

## Extending with Skills

GLM-4.7-Flash reasons well but can't know every tool and API at this size. **Skills** fill that gap: markdown files that give the model domain-specific knowledge on demand. Unlike MCP servers (which dump thousands of tokens into context), only the skill name and description sit in context. Full instructions load when needed.

You can also ask Pi to build skills for itself. Need browser automation? Tell Pi to build it.

You can try Pi pre-built skills to get started quickly:
```bash
git clone https://github.com/badlogic/pi-skills ~/.pi/agent/skills/pi-skills
```

This gives you Gmail, Google Calendar, Google Drive, web search, browser automation, transcription, YouTube transcripts, and VS Code integration. Same SKILL.md format works with Claude Code, Codex CLI, Amp, and Droid.

## Other models

- **Qwen3-Coder-Next**: 80B MoE (3B active), 256K context. Needs ~46GB at Q4. For 64GB MacBooks.
- **Qwen2.5-Coder-7B**: Dense model, fits on 8-16GB Macs. Good fallback:
```bash
llama-server -hf bartowski/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M --fit on --jinja --port 8080
```

## Note on MLX

Apple's MLX framework is optimized backend for Apple Silicon (didn't try because llama.cpp was working great with the shared config). Worth exploring for maximum performance:
```bash
pip install mlx-lm
mlx_lm.server --model mlx-community/GLM-4.7-Flash-4bit --port 8080
```

Same Pi setup, just a different backend.