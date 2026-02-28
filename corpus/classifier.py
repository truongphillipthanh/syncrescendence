import os
import re
import json

TOPICS = {
    "claude-code": ["claude code", "claude-code", "claudecode"],
    "openclaw": ["openclaw", "clawdbot", "claw-dbot"],
    "codex": ["openai codex", "codex"],
    "gemini": ["gemini pro", "gemini 1.5", "google gemini", "gemini api", "gemini flash"],
    "chatgpt": ["chatgpt", "gpt-4", "gpt-3.5", "gpt-4o", "openai chat"],
    "cursor": ["cursor ide", "cursor editor", "cursor ai"],
    "other-ai-tool": ["copilot", "tabnine", "bolt.new", "v0", "lovable", "midjourney", "sora"],
    
    "ai-agents": ["multi-agent", "agent architecture", "agent framework", "autonomous agent", "agentic", "crewai", "autogen", "langchain", "langgraph"],
    "ai-coding": ["ai-assisted coding", "vibe coding", "ai dev workflow", "code generation"],
    "prompt-engineering": ["prompt engineering", "system prompt", "few-shot", "chain of thought", "cot", "prompt design"],
    "ai-memory": ["rag", "vector store", "embeddings", "agent memory", "pinecone", "chromadb", "weaviate"],
    "ai-safety": ["ai safety", "alignment", "guardrail", "red teaming", "ai risk", "jailbreak"],
    "ai-models": ["model comparison", "benchmark", "scaling law", "parameters", "weights", "llama 3", "claude 3", "gpt-4"],
    "ai-business": ["ai startup", "ai economics", "ai market", "sam altman", "openai valuation", "anthropic funding"],
    "mcp": ["model context protocol", "mcp server", "mcp client", "tool use", "function calling"],
    "ai-video": ["video generation", "sora", "runway", "pika", "vfx", "luma"],
    "ai-image": ["image generation", "midjourney", "stable diffusion", "dall-e"],
    
    "geopolitics-us-china": ["us-china", "china relations", "taiwan", "semiconductor ban", "xi jinping"],
    "geopolitics-iran": ["iran", "middle east", "israel", "gaza", "palestine", "hamas", "hezbollah"],
    "geopolitics-russia": ["russia", "ukraine", "putin", "kyiv", "moscow", "nato"],
    "geopolitics-grand-strategy": ["grand strategy", "world order", "military theory", "hegemony", "geopolitics"],
    "geopolitics-other": ["europe", "india", "africa", "geopolitical"],
    "economics-macro": ["macroeconomics", "inflation", "interest rate", "fed", "federal reserve", "gdp", "monetary policy"],
    "economics-investing": ["investing", "stock market", "s&p 500", "portfolio", "trading", "equities", "bonds"],
    "economics-startups": ["startup", "venture capital", "vc", "entrepreneurship", "seed funding", "series a"],
    
    "physics-cosmology": ["universe", "dark energy", "quantum mechanics", "astrophysics", "relativity", "black hole", "cosmology"],
    "biology-evolution": ["evolution", "genetics", "organism", "natural selection", "dna"],
    "biology-neuroscience": ["brain", "neuroscience", "neuron", "cortex", "synapse"],
    
    "philosophy-consciousness": ["consciousness", "metaphysics", "vedanta", "phenomenology", "qualia", "panpsychism", "advaita"],
    "philosophy-epistemology": ["epistemology", "truth", "reasoning", "knowledge theory", "ontology", "empiricism"],
    "history": ["history", "roman empire", "world war", "historical", "ancient"],
    "self-improvement": ["focus", "discipline", "learning", "habit", "productivity", "atomic habits", "deep work", "motivation"],
    "content-creation": ["content strategy", "personal branding", "creator economy", "youtube channel", "newsletter", "audience"],
    "design": ["ui/ux", "visual design", "design system", "figma", "typography", "user interface"],
    "infrastructure": ["ssh", "networking", "server", "devops", "launchd", "kubernetes", "docker", "aws", "cloud", "nginx", "apache"],
    "software-engineering": ["programming", "architecture", "systems design", "api design", "database schema", "refactoring", "rust", "go", "python", "typescript", "java", "npm"],
    
    "sn-handoff": ["handoff", "session handoff", "cc file"],
    "sn-task": ["task dispatch", "dispatch file", "assignment"],
    "sn-confirm": ["confirmation receipt", "receipt"],
    "sn-result": ["result file", "execution result", "execlog"],
    "sn-prompt": ["triangulation", "prompt file"],
    "sn-certescence": ["clarescence", "ascertescence", "certescence"],
    "sn-config": ["yaml", "config", "coordination file", "settings"],
    "sn-script": ["bash script", "python script", "operational script"],
    "sn-watchdog": ["watchdog", "health monitoring", "heartbeat"],
    "sn-canon": ["canon document", "ontology", "principles", "canon"],
    "sn-rosetta": ["terminology reconciliation", "rosetta"],
    "sn-system-prompt": ["system prompt for constellation", "constellation agent"],
    "sn-architecture": ["syncrescendence architecture", "architecture doc"],
    "sn-pipeline": ["ingestion pipeline", "processing pipeline"],
    "sn-other": ["syncrescendence", "sn-"]
}

def guess_topic(text, filename):
    text_lower = text.lower()
    
    if filename.endswith(".orchestrator_last_run"): return "sn-script"
    if filename.endswith(".watchdog_state"): return "sn-watchdog"
    if "EXECLOG" in filename: return "sn-result"
    if filename.endswith(".sh") or filename.endswith(".py"):
        if "syncrescendence" in text_lower or "sn_" in text_lower:
            return "sn-script"
    if filename.endswith(".yaml") or filename.endswith(".json") or filename.endswith(".plist"):
        if "syncrescendence" in text_lower or "sn_" in text_lower:
            return "sn-config"
    if "demoted" in text_lower and "syncrescendence" in text_lower:
        return "sn-other"

    scores = {topic: 0 for topic in TOPICS}
    for topic, keywords in TOPICS.items():
        for kw in keywords:
            scores[topic] += text_lower.count(kw)
    
    best_topic = max(scores, key=scores.get)
    if scores[best_topic] == 0:
        if filename.endswith(".sh") or filename.endswith(".py") or filename.endswith(".j2"):
            return "software-engineering"
        if filename.endswith(".yaml") or filename.endswith(".json") or filename.endswith(".plist") or filename.endswith(".xml"):
            return "infrastructure"
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            return "ai-image"
        if "import " in text_lower or "def " in text_lower or "const " in text_lower:
            return "software-engineering"
        return "ai-general"
    
    return best_topic

def summarize(text):
    lines = text.strip().splitlines()
    for line in lines:
        line = line.strip()
        if len(line) > 20 and not line.startswith('{') and not line.startswith('<'):
            summary = re.sub(r'\s+', ' ', line)
            return summary[:100] + ('...' if len(summary) > 100 else '')
    return "No textual content extracted"

def main():
    directory = "/Users/system/syncrescendence/corpus/"
    out_file = os.path.join(directory, "CLUSTER-MAP-CARTOGRAPHER.tsv")
    
    files = os.listdir(directory)
    target_files = []
    for f in files:
        m = re.match(r'^0*(\d+)(?:\.|$)', f)
        if m:
            num = int(m.group(1))
            if 1 <= num <= 4000:
                target_files.append(f)
                
    target_files.sort(key=lambda x: int(re.match(r'^0*(\d+)', x).group(1)))
    
    with open(out_file, 'w', encoding='utf-8') as out:
        for filename in target_files:
            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath):
                continue
                
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(5000)
            except Exception:
                content = ""
            
            if filename.endswith(".jsonl") or filename.endswith(".json"):
                try:
                    lines = content.splitlines()
                    first_obj = json.loads(lines[0])
                    if "content" in first_obj:
                        content = first_obj["content"]
                    elif "text" in first_obj:
                        content = first_obj["text"]
                    else:
                        content = str(first_obj)
                except Exception:
                    pass
            
            if "# Extraction:" in content:
                parts = content.split("# Extraction:")
                if len(parts) > 1:
                    content = parts[1]
                    
            topic = guess_topic(content, filename)
            
            scores = {t: 0 for t in TOPICS}
            text_lower = content.lower()
            for t, keywords in TOPICS.items():
                if t != topic:
                    for kw in keywords:
                        scores[t] += text_lower.count(kw)
            
            best_sec = max(scores, key=scores.get)
            sec_topic = best_sec if scores[best_sec] > 0 else ""
                
            summ = summarize(content).replace('\t', ' ')
            
            out.write(f"{filename}\t{topic}\t{sec_topic}\t{summ}\n")

if __name__ == "__main__":
    main()
