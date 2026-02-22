---
id: SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills
platform: x
format: article
creator: dani_avila7
title: separation of responsibilities mcp vs skills
status: triaged
original_filename: "20260122-x_article-separation_of_responsibilities_mcp_vs_skills-@dani_avila7.md"
url: https://x.com/dani_avila7/status/2014409635370041517
author: "Daniel San (@dani_avila7)"
captured_date: 2026-02-04
signal_tier: strategic
topics: ""
teleology: contextualize
notebooklm_category: claude-code
aliases: ""
synopsis: ""
key_insights: ""
---
# Separation of Responsibilities: MCP vs Skills

## First understanding agentic flow

Here's something that clicked for me recently while building MCP servers: **they're not just another REST API wrapper**. I know, I know, when you first look at MCP, it's tempting to think "oh cool, so I can expose my existing API endpoints to an LLM." But that's missing the point entirely.

_The real challenge is thinking in terms of **agentic flow**._

You need to design your MCP server imagining how an LLM will actually navigate through your tools. Picture this: the LLM is like a developer exploring your codebase for the first time, it needs to discover what's available, understand when to use each tool, and figure out how to chain them together to accomplish complex tasks.

Let me show you what I mean by comparing traditional REST APIs with MCP servers.

## REST API vs MCP Server

In a traditional REST setup, your application layer sits between the user and your API. The app makes specific API calls, gets data back, and renders it. It's deterministic, you code exactly what happens.

(Description: A diagram showing API REST Flow with three components in sequence: User → Application Business Layer → REST API Server, with bidirectional arrows showing request/response flow.)

Now look at MCP. The user asks something vague like "what changed in the weather?" The LLM has to:

1. Parse that ambiguous request
2. Discover which tools are available in your MCP server
3. Decide which tools to call and in what order
4. Chain multiple tool calls together
5. Synthesize everything into a coherent answer

This is **agentic navigation**. The LLM is actively exploring and making decisions, not just following a predetermined script.

(Description: A diagram showing MCP Flow with five components: User: Query ↔ MCP Server ↔ Tools ↔ REST API, demonstrating multi-directional communication between the LLM agent and various system components.)

## Skills: The missing piece

So here's where it gets interesting. I was building MCP servers for a while, and I kept running into this problem: my docstrings were becoming massive walls of text. I was trying to cram everything into them, when to use the tool, how it relates to other tools, common workflows, edge cases, you name it.

Then Skills came along, and honestly, it was like someone finally understood the pain.

Skills sit between the user and your MCP server, acting as a guide for the LLM. Think of it this way:

(Description: A flow diagram showing the relationship between Skills and MCP. The diagram shows: User Request → Skill File → LLM Agent → MCP Server → Tools, with branches to REST API, Databases, and External Services.)

- **MCP = Your toolbox** (hammer, screwdriver, wrench)
- **Skill = The instruction manual** (when to use which tool, how to build things)

Before Skills, the chat was full of noise, conversation history, typos, random commands (input + output), /compact, context switching. Your MCP had to deal with all of that. Now? Skills filter and guide that input, helping the LLM make better decisions about which tools to use and when.

## The Docstring problem

When an MCP server starts, it reads tool docstrings to build tool metadata. This metadata can then be provided by the client or host as part of the LLM's tool context, which the model uses to decide when and how to invoke tools.

Simple enough. But here's the thing, before Skills existed, we were doing this:

(Description: A flow diagram showing metadata progression: MCP Server Starts → Tools with Docstring → Tool Metadata → Client or Host API → LLM Context Window)
```python
@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city.

    Args:
        city: City name

    Returns:
        Current weather data

    Usage:
    - Use this when user asks about current conditions
    - Always call this BEFORE get_forecast for context
    - If user asks about multiple cities, call this for each

    Related Tools:
    - get_forecast: Use for future weather
    - compare_weather: Use for city comparisons

    Common Patterns:
    1. Single city: Just call this tool
    2. Comparison: Call for each city, then compare_weather
    3. Planning: Call this first, then get_forecast

    Example Input:
    "Paris"

    Example Output:
    "Temperature: 18°C, Conditions: Partly cloudy..."

    Notes:
    - Returns Celsius by default
    - Includes humidity and wind speed
    - Data refreshes every 30 minutes
    """
    # Implementation here
```

See the problem? That's a 35-line docstring for a simple weather function, just as an example. You obviously wouldn't need this level of detail for something that simple. But for more complex tools and multi-step workflows, this is exactly the kind of guidance you often end up needing. And if all of that gets loaded into the LLM's context every time the MCP server starts, token usage adds up fast.

We were mixing two completely different concerns:

1. **Technical definition** (what does this function do?)
2. **Usage intelligence** (when/how/why should I use it?)

## Finally: Separation of Responsibilities

This is where Skills save the day. We can finally split these concerns properly:

### What MCP should handle

Your MCP tools should be lean and focused on the technical contract:
```python
@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city.

    Args:
        city: City name

    Returns:
        Current weather data
    """
    # Implementation
```

That's it. Clean, simple, 8 lines. The LLM knows what the function does, what it takes, and what it returns.

### What Skills Should Handle

All that usage intelligence? That goes in your Skill file where it belongs. The Skill guides the LLM on the bigger picture, workflows, patterns, when to use which tool, how tools relate to each other. We'll see a full example in a bit.

**SKILL.md File:**
```markdown
---
name: weather-analysis
description: Analyze and compare weather patterns across cities
---

# Weather Analysis Skill

## When to Use These Tools

### get_current_weather

Use when:
- User asks "what's the weather in [city]?"
- Need current conditions for a single location
- Starting point for any weather query

**Do NOT use when:**
- User wants forecast (use `get_forecast`)
- User wants comparison (use `compare_weather`)

### get_forecast

Use when:
- User asks about future weather
- Planning trip or outdoor activities
- Need multi-day weather outlook

**Always specify days parameter based on context:**
- "tomorrow" → days=1
- "this week" → days=7
- "weekend" → days=2 (starting from Friday)

### compare_weather

Use when:
- User mentions multiple cities
- Questions like "which city is warmer?"
- Travel decisions between locations

## Common Workflows

### Workflow 1: Basic Weather Query

User: "What's the weather in Paris?"
→ Call get_current_weather("Paris")
→ Present results

### Workflow 2: Travel Planning

User: "I'm deciding between Barcelona and Rome for next week"
→ Call get_forecast("Barcelona", days=7)
→ Call get_forecast("Rome", days=7)
→ Call compare_weather("Barcelona", "Rome")
→ Synthesize recommendation

### Workflow 3: Multi-City Comparison

User: "Compare weather in London, Berlin, and Paris"
→ Call get_current_weather for each city
→ Call compare_weather for each pair
→ Present comparative analysis

## Best Practices

**ALWAYS DO:**
- Validate city names - If user provides abbreviation, expand it
- Consider time zones - Mention local time in responses
- Provide context - Don't just show numbers, explain what they mean
- Be proactive - If weather is extreme, mention it upfront

**NEVER DO:**
- Call tools redundantly - Use compare_weather instead of multiple get_current_weather
- Assume units - Clarify Celsius vs Fahrenheit based on location
- Ignore forecast when appropriate - For future-oriented questions, use forecast

## Troubleshooting

**City not found:**
→ Try alternative spellings or nearby major city
→ Ask user to clarify location

**Forecast unavailable:**
→ Fall back to current weather
→ Explain limitation to user

## Related Tools

- `get_current_weather` → Foundation for all queries
- `get_forecast` → Extension for time-based planning
- `compare_weather` → Synthesis tool for decisions
```

Notice: Rich context, workflows, when/how/why to use, business logic.

## Why this matters

MCP servers are navigation frameworks for LLM agents. Skills are the user manuals that guide this navigation.

(Description: A system flow diagram illustrating the interaction between components: User Query → Skill → LLM Reasoning → MCP Server → Tools, with a separate arrow from User Query directly to Final Answer, and bidirectional communication shown throughout the chain.)

Here's what you get with proper separation:

- **Token efficiency**: Smaller docstrings = less context window bloat
- **Maintainability**: Change workflows without touching MCP code
- **Reusability**: One MCP, many different Skills for different use cases
- **Clarity**: Technical definitions stay technical, business logic stays separate
- **Progressive disclosure**: Claude only loads Skill metadata at startup, reading full instructions only when needed.

By separating technical definitions (MCP) from usage intelligence (Skills), we create a scalable, maintainable, and efficient system for LLM tool use.