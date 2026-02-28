import os

dirs = [
    "ai-biotech", "ai-capability-futures", "ai-memory-retrieval", "ai-models",
    "ai-safety", "ai-video-vfx", "claude-code", "design-taste",
    "geopolitics-grand-strategy", "health-psychology", "infrastructure",
    "leadership-management", "meaning-civilization", "multi-agent-systems",
    "openclaw", "philosophy-esoterica", "product-business", "productivity-pkm",
    "prompt-engineering", "startup-vc", "vibe-coding", "writing-creation"
]

base_dir = "/Users/system/syncrescendence/corpus/"
out_file = "/Users/system/syncrescendence/corpus/samples.txt"

with open(out_file, "w") as f_out:
    for d in dirs:
        dir_path = os.path.join(base_dir, d)
        if not os.path.exists(dir_path):
            continue
        files = sorted([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])
        if not files:
            continue
        n = len(files)
        indices = []
        if n <= 4:
            indices = list(range(n))
        else:
            indices = [0, n//3, 2*n//3, n-1]
        
        f_out.write(f"=== FOLDER: {d} ===\n")
        for i in indices:
            filepath = os.path.join(dir_path, files[i])
            f_out.write(f"--- FILE: {d}/{files[i]} ---\n")
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read(1500)
                    f_out.write(content + "\n...[TRUNCATED]...\n")
            except Exception as e:
                f_out.write(f"Error reading file: {e}\n")
        f_out.write("\n\n")
