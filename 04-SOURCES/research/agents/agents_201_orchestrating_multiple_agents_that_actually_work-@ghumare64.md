After building your first single agent, the next challenge isn't making it smarter, it's making multiple agents work together without burning through your token budget or creating coordination chaos.
This guide covers what happens when you need more than one agent: orchestration patterns, communication strategies, and production lessons from real deployments.
Why Multiple Agents?
Single agents hit limits fast. Context windows fill up, decision-making gets muddy, and debugging becomes impossible. Multi-agent systems solve this by distributing work across specialized agents, similar to how you'd structure a team.
The benefits are real:
Specialization: Each agent masters one domain instead of being mediocre at everything
Parallel processing: Multiple agents can work simultaneously on independent subtasks
Maintainability: When something breaks, you know exactly which agent to fix
Scalability: Add new capabilities by adding new agents, not rewriting everything
The tradeoff: coordination overhead. Agents need to communicate, share state, and avoid stepping on each other. Get this wrong and you've just built a more expensive failure mode.
The Three Orchestration Patterns
There are three proven patterns for coordinating multiple agents. Pick based on your coordination needs, not what sounds coolest.
Supervisor Pattern (Centralized Control)
A supervisor agent coordinates all work. It receives the task, breaks it into subtasks, routes to worker agents, validates outputs, and synthesizes the final response.
When to use it:
Tasks with clear decomposition into subtasks
You need auditability and reasoning transparency
Quality control matters more than speed
Handling 3-8 worker agents max
Example architecture:
markdown

User Request
    ↓
[Supervisor Agent]
    ↓
Decompose → Route → Monitor → Validate → Synthesize
    ↓         ↓         ↓
[Worker 1] [Worker 2] [Worker 3]
Real implementation: The AI Hedge Fund example uses this pattern. Four specialized analysts (Fundamental, Portfolio, Risk, Technical) run in parallel while a supervisor coordinates:
typescript

// Supervisor coordinates parallel analysis
const analyses = await Promise.all([
  fundamentalAgent.analyze(ticker),
  portfolioAgent.analyze(ticker),
  riskAgent.analyze(ticker),
  technicalAgent.analyze(ticker)
]);

// Supervisor synthesizes results
const report = await supervisorAgent.synthesize(analyses);
The problem: Supervisors become bottlenecks. Every decision flows through one agent, which means serial processing for coordination steps even when work happens in parallel. Token costs scale with coordination layers.
Swarm Pattern (Peer-to-Peer)
No central controller. Agents communicate directly, exchange information, and self-organize around the task. Think ant colonies, not org charts.
When to use it:
Tasks benefit from multiple perspectives
No clear decomposition into serial steps
Real-time responsiveness matters
Agents need to react to each other's work
Example architecture:
markdown

[Agent A] ←→ [Agent B]
    ↕  ↘     ↙  ↕
[Agent C] ←→ [Agent D]
Each agent can talk to any other agent. Information flows through the network until consensus emerges or the task is completed.
Real implementation: The SmartTravel Multi-Agent example demonstrates peer coordination. Six agents (Destination Explorer, Flight Search, Hotel Search, Dining, Itinerary, Budget) share information through a common state:
typescript

// Each agent reads and writes to shared state
await destinationAgent.explore(state);
await flightAgent.search(state);  // Uses destination from previous agent
await hotelAgent.search(state);   // Uses destination and dates

// Agents update shared state
class TravelState {
  destination: string;
  flightOptions: Flight[];
  hotelOptions: Hotel[];
  // ... shared across all agents
}
The problem: Emergent behavior is hard to predict. Without a coordinator, agents might duplicate work, create infinite loops, or converge on suboptimal solutions. Debugging is brutal, you're tracing information flow through a mesh, not a tree.
Hierarchical Pattern (Multi-Level Control)
Supervisor pattern, but recursive. Top-level agent manages mid-level agents, which manage worker agents. Three or more layers.
When to use it:
Tasks are too complex for flat supervision
Different domains require different management strategies
You're coordinating 10+ agents
You need both strategic and tactical control
Example architecture:
markdown

[Top-Level Supervisor]
              ↓
    ┌─────────┴─────────┐
    ↓                   ↓
[Mid-Level A]      [Mid-Level B]
    ↓                   ↓
[Workers 1-3]      [Workers 4-6]
Each mid-level agent is itself a supervisor for its domain. The top level coordinates strategy, mid levels handle tactics.
Real implementation: The NVIDIA Docs Generator example uses hierarchical decomposition:
typescript

// Top-level: Documentation orchestrator
const topLevel = {
  analyze: async (repo) => {
    // Delegates to analysis team
    const analysis = await analysisTeam.execute(repo);
    
    // Delegates to documentation team
    const docs = await docsTeam.execute(analysis);
    
    // Delegates to validation team
    return await validationTeam.execute(docs);
  }
};

// Mid-level: Analysis team supervises specific analyzers
const analysisTeam = {
  codeAnalyzer: new Agent(),
  archDiagrammer: new Agent(),
  testGenerator: new Agent()
};
The problem: Token costs explode. Each layer adds coordination overhead. A three-layer hierarchy with 5 agents per layer can easily burn 50K+ tokens on coordination alone. Only justified when flat patterns genuinely can't handle the complexity.
Agent Communication Strategies
Orchestration patterns tell you the structure. Communication strategies tell you how information actually moves between agents.
Shared State (Most Common)
All agents read from and write to a common state object. Changes are visible to everyone.
Implementation:
typescript

interface SharedState {
  task: string;
  results: Map<string, any>;
  currentStep: string;
}

// Agent A writes
state.results.set('analysis', analysisResult);

// Agent B reads
const analysis = state.results.get('analysis');
Advantages:
Simple to implement
Easy to debug (just inspect state)
No message passing complexity
Disadvantages:
Race conditions if agents write simultaneously
No isolation between agent contexts
State grows unbounded without pruning
When to use it: Start here. Most agent systems should use shared state until they hit specific problems it can't solve.
Message Passing (Event-Driven)
Agents send messages to each other. No direct state sharing.
Implementation:
typescript

// Agent A publishes event
eventBus.publish('analysis.complete', {
  ticker: 'AAPL',
  analysis: result
});

// Agent B subscribes to event
eventBus.subscribe('analysis.complete', async (event) => {
  await portfolioAgent.process(event.analysis);
});
Advantages:
Loose coupling between agents
Natural for async work
Easy to add new agents without changing existing ones
Disadvantages:
Harder to debug (trace message flow)
Potential for message loops
Need infrastructure (event bus, queues)
When to use it: When agents are truly independent and shouldn't know about each other. Or when you need async processing across services.
Handoff Mechanism (Explicit Control Transfer)
One agent explicitly passes control to another agent, often with context.
Implementation:
typescript

class Agent {
  async handoff(targetAgent: Agent, context: Context) {
    // Prepare handoff context
    const handoffContext = {
      previousAgent: this.name,
      taskContext: context,
      timestamp: Date.now()
    };
    
    // Transfer control
    return await targetAgent.execute(handoffContext);
  }
}
Advantages:
Clear control flow
Easy to audit who did what
Context preservation across agents
Disadvantages:
Tight coupling between agents
Serial processing by default
Handoff overhead on every transition
When to use it: When tasks must happen in specific order and context must flow through the chain.
Memory Architecture for Multi-Agent Systems
Single agents use context windows and external memory. Multi-agent systems have an additional problem: agents need to coordinate state without duplicating it or creating conflicts.
Session-Based Memory
Each agent interaction is a session. Sessions have isolated state that gets merged back into shared memory on completion.
Pattern:
typescript

class MemoryManager {
  async createSession(agentId: string): Session {
    return {
      id: generateId(),
      agentId,
      localState: {},
      sharedSnapshot: this.getSnapshot()
    };
  }
  
  async commitSession(session: Session) {
    // Merge local changes back to shared state
    this.merge(session.localState);
  }
}
Use case: Parallel agents that need to read shared context but make isolated changes. Common in supervisor patterns where workers operate independently.
Window Memory (Conversation Context)
Keep a sliding window of recent exchanges across all agents. Oldest entries get compressed or dropped.
Pattern:
typescript

class WindowMemory {
  private window: Message[] = [];
  private maxSize = 50;
  
  add(message: Message) {
    this.window.push(message);
    
    if (this.window.length > this.maxSize) {
      // Compress oldest third
      this.compressOldest();
    }
  }
  
  compressOldest() {
    const toCompress = this.window.slice(0, this.maxSize / 3);
    const summary = await this.summarize(toCompress);
    this.window = [summary, ...this.window.slice(this.maxSize / 3)];
  }
}
Use case: Long-running agent conversations where context matters but you can't keep everything. The RAG applications in motia-examples use this pattern.
Episodic Memory (Cross-Agent Learning)
Store interaction history between specific agents. Enables agents to learn from past coordination.
Pattern:
typescript

interface Episode {
  agentA: string;
  agentB: string;
  interaction: Interaction;
  outcome: 'success' | 'failure';
  learnings: string[];
}

// Agent looks up past interactions before coordinating
const pastEpisodes = await memory.query({
  agents: ['supervisor', 'riskAnalyst'],
  outcome: 'success'
});
Use case: Agents that frequently collaborate and can improve based on what worked before.
Production Considerations
Lab demos scale differently than production. Here's what actually matters when you run multiple agents under load.
Token Economics
Multi-agent systems burn tokens fast. Four agents coordinating on a task can easily 10x your costs versus a single agent.
Cost breakdown for typical supervisor system:
Supervisor decomposition: 1K tokens
4 worker agents: 3K tokens each (12K total)
Supervisor synthesis: 2K tokens
Total: 15K tokens per task
Compare to single agent: 4K tokens for same task. You're paying for coordination.
Optimization strategies:
Cache supervisor instructions: Don't regenerate task decomposition every time
Compress worker outputs: Workers don't need to return prose, structured data works
Parallel execution: 4 agents running sequentially costs same as parallel but takes 4x longer
Lazy agent activation: Only invoke agents when their output is needed
Latency Management
Multiple agents means multiple LLM calls. Each call adds 2-5 seconds. Serial processing destroys user experience.
The math:
1 agent: 3 seconds
4 agents (serial): 12 seconds
4 agents (parallel): 3-4 seconds
Always parallelize independent work. The AI Hedge Fund example saves 9 seconds by running four analysts in parallel instead of serial.
Error Propagation
In single-agent systems, failures are local. In multi-agent systems, one agent's failure can cascade.
Failure modes:
Poison pills: One agent returns garbage that breaks downstream agents
Deadlocks: Agents wait for each other in circular dependencies
Resource exhaustion: Parallel agents all try to use the same rate-limited API
Cascading failures: Supervisor fails, orphaning all workers
Defense strategies:
Timeouts at every layer: Agents must complete within bounded time
Circuit breakers: After N failures, stop calling problematic agents
Graceful degradation: System should work with subset of agents
Isolate state: Worker failures shouldn't corrupt shared state
Monitoring & Observability
You can't debug what you can't see. Multi-agent systems need observability from day one.
Essential metrics:
Per-agent success rate: Which agents are failing?
Coordination overhead: How much time spent coordinating vs working?
Token consumption by agent: Where are costs coming from?
Agent interaction patterns: Which agents talk to which?
Example instrumentation:
typescript

class ObservableAgent {
  async execute(task: Task): Result {
    const span = tracer.startSpan('agent.execute', {
      agentId: this.id,
      taskType: task.type
    });
    
    try {
      const result = await this.process(task);
      span.setStatus({ code: SpanStatusCode.OK });
      return result;
    } catch (error) {
      span.setStatus({ 
        code: SpanStatusCode.ERROR,
        message: error.message 
      });
      throw error;
    } finally {
      span.end();
    }
  }
}
Real Implementation Examples
The motia-examples repo contains production-ready multi-agent implementations:
ChessArena AI (Competitive Multi-Agent)
Multiple LLMs compete in chess matches, evaluated by Stockfish. Demonstrates:
Parallel agent execution
Real-time streaming of agent decisions
Quality-based ranking (move evaluation, not just wins)
Source
Finance Agent (Supervisor Pattern)
Combines multiple data sources with AI analysis. Shows:
Supervisor coordinating data collection and analysis
Parallel processing of financial data
Synthesis of multiple perspectives
Source
SmartTravel Multi-Agent (Swarm Pattern)
Six specialized agents collaborating on travel planning:
Peer-to-peer communication via shared state
Dynamic task routing based on agent availability
Consensus building across agent recommendations
Source
Common Anti-Patterns
Things that seem smart but break in production:
Over-coordination: Don't make agents coordinate when they don't need to. If agents work on independent tasks, let them run independently.
Kitchen sink agents: Don't make one agent do everything. The whole point of multiple agents is specialization.
Synchronous everything: Don't block waiting for agents unless you must. Most coordination can be async.
Ignoring costs: Don't deploy multi-agent systems without tracking token usage. You'll get a surprise bill.
No fallbacks: Don't assume all agents will work. Build degraded modes.
When to Use Which Pattern
Use Supervisor when:
You need auditability
Tasks decompose clearly
3-8 specialized agents
Quality > speed
Use Swarm when:
Multiple perspectives needed
No clear task decomposition
Real-time responsiveness critical
Agents can self-organize
Use Hierarchical when:
Managing 10+ agents
Multiple layers of abstraction needed
Both strategic and tactical control required
Token costs are acceptable
Use single agent when:
Task is simple enough
One domain of expertise sufficient
Minimizing costs matters
You're not sure yet
Getting Started
Pick the simplest pattern that could work. Most teams should start with supervisor pattern:
Build one capable agent
Identify where it struggles (usually specialization or parallel work)
Extract that into a second agent
Add supervisor to coordinate
Iterate
Don't build a complex multi-agent system from day one. Build one agent, see where it breaks, add another agent. Repeat.
What's Next
You now understand how to orchestrate multiple agents. The next level is understanding production deployment: how do you run these systems at scale, handle failures gracefully, and keep costs under control?
For now, take these patterns and build something. Pick a task your single agent struggles with, break it into specialized agents, choose an orchestration pattern, and ship it.
The code is at motia-examples and awesome-ai-apps. Fork them, break them, make them your own.
TL;DR
Use multiple agents when: Specialization, parallel work, or single agent hits limits
Three patterns: Supervisor (centralized), Swarm (peer-to-peer), Hierarchical (multi-level)
Communication: Shared state (start here), message passing (async work), handoffs (explicit control)
Memory: Session-based for parallel work, window for long conversations, episodic for learning
Production: Watch token costs, parallelize everything, expect failures, instrument everything
Start simple: One agent → identify bottleneck → add second agent → add supervisor → iterate
Build one system that uses two agents reliably before building ten.