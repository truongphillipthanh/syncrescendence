#!/usr/bin/env python3
"""
Model & Platform Intelligence Database
Pilot implementation of CANON-30300 TechStackDB schema (subset).

Creates a SQLite database populated from MODEL-INDEX.md data,
enabling queries like:
  - "What model for strategic synthesis?"
  - "Cheapest long-context model?"
  - "Which platforms support video input?"
  - "Monthly cost breakdown by account"

Usage:
    python3 model_db.py init          # Create/recreate database
    python3 model_db.py query <sql>   # Run arbitrary SQL
    python3 model_db.py search <term> # Search models by capability
    python3 model_db.py cost          # Show cost analysis
    python3 model_db.py routing       # Show task routing matrix
    python3 model_db.py info <model>  # Show model details
    python3 model_db.py capabilities  # Show capability matrix
    python3 model_db.py shell         # Interactive SQL shell
"""
from config import *

import sqlite3
import sys
import os
import json
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
DB_PATH = SCRIPT_DIR.parent / "state" / "model_intelligence.db"

# ============================================================
# SCHEMA
# ============================================================

SCHEMA = """
-- Platforms (AI providers)
CREATE TABLE IF NOT EXISTS platforms (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    tier TEXT,
    account TEXT,
    monthly_cost REAL DEFAULT 0,
    status TEXT DEFAULT 'NOMINAL',
    avatar TEXT,
    role TEXT,
    url TEXT
);

-- Models (AI models)
CREATE TABLE IF NOT EXISTS models (
    id TEXT PRIMARY KEY,
    platform_id TEXT NOT NULL REFERENCES platforms(id),
    name TEXT NOT NULL,
    api_string TEXT,
    context_window INTEGER,
    effective_context INTEGER,
    input_price_per_m REAL,
    output_price_per_m REAL,
    status TEXT DEFAULT 'active',
    release_date TEXT,
    notes TEXT
);

-- Capabilities (per-model feature flags)
CREATE TABLE IF NOT EXISTS capabilities (
    model_id TEXT NOT NULL REFERENCES models(id),
    capability TEXT NOT NULL,
    value TEXT NOT NULL,
    notes TEXT,
    PRIMARY KEY (model_id, capability)
);

-- Task routing (task type → model assignment)
CREATE TABLE IF NOT EXISTS task_routing (
    task_type TEXT PRIMARY KEY,
    primary_model TEXT NOT NULL REFERENCES models(id),
    fallback_model TEXT REFERENCES models(id),
    rationale TEXT
);

-- IIC chain routing (chain → model assignment)
CREATE TABLE IF NOT EXISTS iic_routing (
    chain TEXT PRIMARY KEY,
    model_id TEXT NOT NULL REFERENCES models(id),
    rationale TEXT
);

-- Constellation economics (account-level view)
CREATE TABLE IF NOT EXISTS economics (
    account TEXT NOT NULL,
    platform_id TEXT NOT NULL REFERENCES platforms(id),
    tier TEXT,
    monthly_cost REAL,
    avatars TEXT,
    PRIMARY KEY (account, platform_id)
);

-- Metadata
CREATE TABLE IF NOT EXISTS db_metadata (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""

# ============================================================
# DATA (from MODEL-INDEX.md + REF-STACK_TELEOLOGY.md)
# ============================================================

PLATFORMS = [
    ("anthropic", "Anthropic", "Max 5x", "A1", 100, "NOMINAL", "Commander", "EXECUTOR-LEAD", "https://claude.ai"),
    ("anthropic_a2", "Anthropic", "Pro", "A2", 20, "NOMINAL", "Vizier/Adjudicator", "INTERPRETER/PARALLEL-EXEC", "https://claude.ai"),
    ("openai", "OpenAI", "Plus", "A1", 20, "NOMINAL", "Vanguard", "COMPILER", "https://chatgpt.com"),
    ("google", "Google", "AI Pro", "A2", 20, "NOMINAL", "Cartographer/Diviner", "SENSOR/DIGESTOR", "https://gemini.google.com"),
    ("xai", "xAI", "Premium+", "A1", 0, "NOMINAL", "Oracle", "RECON", "https://grok.x.ai"),
    ("deepseek", "DeepSeek", "API", None, 0, "WATCH", None, None, "https://deepseek.com"),
    ("alibaba", "Alibaba", "API", None, 0, "NOMINAL", None, None, "https://qwen.ai"),
    ("moonshot", "Moonshot", "API", None, 0, "NOMINAL", None, None, "https://kimi.ai"),
]

MODELS = [
    # Anthropic
    ("claude-opus", "anthropic", "Claude 4.5 Opus", "claude-opus-4-5-20251101", 200000, 200000, 5.0, 25.0, "active", "2025-11-01", "Deep synthesis, extended thinking"),
    ("claude-sonnet", "anthropic", "Claude 4.5 Sonnet", "claude-sonnet-4-5-20251101", 200000, 200000, 3.0, 15.0, "active", "2025-11-01", "Fast, balanced, excellent coding"),
    ("claude-haiku", "anthropic", "Claude 4.5 Haiku", "claude-haiku-4-5-20251101", 200000, 200000, 1.0, 5.0, "active", "2025-11-01", "Speed, efficiency, sub-tasks"),
    # OpenAI
    ("gpt-5.2", "openai", "GPT-5.2", "gpt-5-turbo", 128000, 128000, 5.0, 15.0, "active", "2025-09-15", "Versatile, broad knowledge"),
    ("gpt-4.1", "openai", "GPT-4.1", "gpt-4-turbo", 1000000, 500000, 2.0, 8.0, "active", "2025-06-01", "Long context, SWE-bench leader"),
    ("o3", "openai", "o3", "o3", 128000, 128000, None, None, "active", "2025-08-01", "Deep reasoning, chain-of-thought"),
    ("o3-pro", "openai", "o3-pro", "o3-pro", 128000, 128000, None, None, "active", "2025-10-01", "Extended reasoning, proofs"),
    # Google
    ("gemini-3-pro", "google", "Gemini 3 Pro", "gemini-3-pro", 1000000, 1000000, 2.0, 12.0, "active", "2025-10-01", "Multimodal, research synthesis"),
    ("gemini-3-flash", "google", "Gemini 3 Flash", "gemini-3-flash", 1000000, 1000000, None, None, "active", "2025-10-01", "Speed, efficiency"),
    ("gemini-3-deep", "google", "Gemini 3 Deep Think", "gemini-3-deep-think", 1000000, 1000000, None, None, "active", "2025-10-01", "Advanced reasoning"),
    # xAI
    ("grok-4", "xai", "Grok 4", "grok-4", 256000, 256000, None, None, "active", "2025-12-01", "Real-time X/Twitter, cultural fluency"),
    ("grok-4-fast", "xai", "Grok 4 Fast", "grok-4-fast", 256000, 256000, None, None, "active", "2025-12-01", "Speed, efficiency"),
    # Chinese labs
    ("deepseek-v3.2", "deepseek", "DeepSeek-V3.2", "deepseek-v3.2", 128000, 128000, 0.03, 0.15, "active", "2025-11-15", "Cost-efficient batch processing"),
    ("qwen3-max", "alibaba", "Qwen3-Max", "qwen3-max", 1000000, 1000000, None, None, "active", "2025-09-01", "Multilingual, long context"),
    ("kimi-k2", "moonshot", "Kimi K2", "kimi-k2", 256000, 256000, None, None, "active", "2025-10-01", "Sequential tool calling"),
]

CAPABILITIES = [
    # Claude family
    ("claude-opus", "extended_thinking", "yes", None),
    ("claude-opus", "tool_use", "native", "MCP support"),
    ("claude-opus", "image_input", "yes", None),
    ("claude-opus", "video_input", "no", None),
    ("claude-opus", "image_generation", "no", None),
    ("claude-opus", "agentic", "yes", None),
    ("claude-sonnet", "extended_thinking", "yes", None),
    ("claude-sonnet", "tool_use", "native", "MCP support"),
    ("claude-sonnet", "image_input", "yes", None),
    ("claude-sonnet", "video_input", "no", None),
    ("claude-sonnet", "image_generation", "no", None),
    ("claude-sonnet", "agentic", "yes", None),
    ("claude-haiku", "tool_use", "native", "MCP support"),
    ("claude-haiku", "image_input", "yes", None),
    ("claude-haiku", "agentic", "yes", None),
    # GPT family
    ("gpt-5.2", "tool_use", "native", "Via plugin"),
    ("gpt-5.2", "image_input", "yes", None),
    ("gpt-5.2", "video_input", "yes", None),
    ("gpt-5.2", "image_generation", "yes", "DALL-E integration"),
    ("gpt-5.2", "agentic", "yes", None),
    ("gpt-5.2", "memory", "yes", "Conversation continuity"),
    ("gpt-4.1", "tool_use", "native", None),
    ("gpt-4.1", "image_input", "yes", None),
    ("o3", "deep_reasoning", "yes", "Chain-of-thought"),
    ("o3-pro", "deep_reasoning", "yes", "Extended, mathematical proofs"),
    # Gemini family
    ("gemini-3-pro", "tool_use", "native", "MCP support"),
    ("gemini-3-pro", "image_input", "yes", None),
    ("gemini-3-pro", "video_input", "yes", "Native multimodal"),
    ("gemini-3-pro", "image_generation", "yes", "Imagen/Veo"),
    ("gemini-3-pro", "deep_research", "yes", None),
    ("gemini-3-pro", "agentic", "yes", None),
    ("gemini-3-flash", "tool_use", "native", None),
    ("gemini-3-flash", "image_input", "yes", None),
    ("gemini-3-deep", "deep_reasoning", "yes", "Advanced"),
    # Grok
    ("grok-4", "tool_use", "native", "Via API"),
    ("grok-4", "image_input", "yes", None),
    ("grok-4", "image_generation", "yes", "Aurora"),
    ("grok-4", "realtime_data", "yes", "X/Twitter firehose"),
    ("grok-4", "agentic", "yes", "Multi-agent native"),
    # Chinese labs
    ("deepseek-v3.2", "tool_use", "native", None),
    ("deepseek-v3.2", "agentic", "yes", None),
    ("kimi-k2", "tool_use", "native", "Sequential tool calling"),
]

TASK_ROUTING = [
    ("strategic_synthesis", "claude-opus", "gpt-5.2", "Deep architectural thinking"),
    ("daily_operations", "claude-sonnet", "gemini-3-flash", "Balance of speed/quality"),
    ("code_generation", "claude-sonnet", "gpt-4.1", "SWE-bench performance"),
    ("long_document_analysis", "gemini-3-pro", "gpt-4.1", "1M context"),
    ("realtime_discourse", "grok-4", "gpt-5.2", "X/Twitter integration"),
    ("mathematical_reasoning", "o3-pro", "gemini-3-deep", "Formal verification"),
    ("batch_processing", "deepseek-v3.2", "claude-haiku", "Cost optimization"),
    ("research_synthesis", "gemini-3-pro", "claude-opus", "Comprehensive coverage"),
]

IIC_ROUTING = [
    ("acumen", "grok-4", "Real-time awareness"),
    ("coherence", "claude-opus", "Deep integration"),
    ("efficacy", "claude-sonnet", "Code + speed"),
    ("mastery", "gpt-5.2", "Explanation clarity"),
    ("transcendence", "claude-opus", "Philosophical depth"),
]

ECONOMICS = [
    ("A1", "anthropic", "Max 5x", 100, "Commander"),
    ("A1", "openai", "Plus", 20, "Vanguard"),
    ("A2", "anthropic_a2", "Pro", 20, "Vizier, Adjudicator"),
    ("A2", "google", "AI Pro", 20, "Cartographer, Diviner"),
]


def init_db():
    """Create and populate the database."""
    # Remove existing DB for clean init
    if DB_PATH.exists():
        DB_PATH.unlink()

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create schema
    cur.executescript(SCHEMA)

    # Insert platforms
    cur.executemany(
        "INSERT INTO platforms VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        PLATFORMS
    )

    # Insert models
    cur.executemany(
        "INSERT INTO models VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        MODELS
    )

    # Insert capabilities
    cur.executemany(
        "INSERT INTO capabilities VALUES (?, ?, ?, ?)",
        CAPABILITIES
    )

    # Insert task routing
    cur.executemany(
        "INSERT INTO task_routing VALUES (?, ?, ?, ?)",
        TASK_ROUTING
    )

    # Insert IIC routing
    cur.executemany(
        "INSERT INTO iic_routing VALUES (?, ?, ?)",
        IIC_ROUTING
    )

    # Insert economics
    cur.executemany(
        "INSERT INTO economics VALUES (?, ?, ?, ?, ?)",
        ECONOMICS
    )

    # Metadata
    cur.execute("INSERT INTO db_metadata VALUES ('created', ?)", (datetime.now().astimezone().isoformat(),))
    cur.execute("INSERT INTO db_metadata VALUES ('schema_version', '1.0.0')")
    cur.execute("INSERT INTO db_metadata VALUES ('source', 'MODEL-INDEX.md + REF-STACK_TELEOLOGY.md')")
    cur.execute("INSERT INTO db_metadata VALUES ('canon_ref', 'CANON-30300')")

    conn.commit()

    # Report
    counts = {}
    for table in ["platforms", "models", "capabilities", "task_routing", "iic_routing", "economics"]:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        counts[table] = cur.fetchone()[0]

    conn.close()

    print(f"Database created: {DB_PATH}")
    print(f"  Platforms:    {counts['platforms']}")
    print(f"  Models:       {counts['models']}")
    print(f"  Capabilities: {counts['capabilities']}")
    print(f"  Task routes:  {counts['task_routing']}")
    print(f"  IIC routes:   {counts['iic_routing']}")
    print(f"  Economics:    {counts['economics']}")


def run_query(sql):
    """Execute arbitrary SQL and display results."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    try:
        cur.execute(sql)
        rows = cur.fetchall()

        if not rows:
            print("(no results)")
            return

        # Print header
        cols = rows[0].keys()
        widths = {c: max(len(c), max(len(str(r[c] or "")) for r in rows)) for c in cols}
        header = " | ".join(c.ljust(widths[c]) for c in cols)
        print(header)
        print("-+-".join("-" * widths[c] for c in cols))

        for row in rows:
            print(" | ".join(str(row[c] or "").ljust(widths[c]) for c in cols))

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        conn.close()


def search_models(term):
    """Search models by capability or name."""
    sql = f"""
    SELECT m.name, m.api_string, m.context_window, m.effective_context,
           p.name as provider, p.status,
           m.input_price_per_m as input_price, m.output_price_per_m as output_price
    FROM models m
    JOIN platforms p ON m.platform_id = p.id
    WHERE m.name LIKE '%{term}%'
       OR m.notes LIKE '%{term}%'
       OR m.id IN (
           SELECT model_id FROM capabilities
           WHERE capability LIKE '%{term}%' OR value LIKE '%{term}%'
       )
    ORDER BY p.name, m.name
    """
    print(f"Models matching '{term}':\n")
    run_query(sql)


def show_cost():
    """Show cost analysis."""
    print("CONSTELLATION ECONOMICS\n")
    run_query("""
    SELECT e.account, p.name as platform, e.tier, e.monthly_cost, e.avatars
    FROM economics e
    JOIN platforms p ON e.platform_id = p.id
    ORDER BY e.account
    """)

    print(f"\n{'='*50}")
    run_query("SELECT SUM(monthly_cost) as total_monthly FROM economics")

    print("\n\nCOST PER OUTPUT TOKEN (cheapest first)\n")
    run_query("""
    SELECT m.name, p.name as provider,
           m.input_price_per_m as '$/M_input',
           m.output_price_per_m as '$/M_output',
           m.context_window
    FROM models m
    JOIN platforms p ON m.platform_id = p.id
    WHERE m.output_price_per_m IS NOT NULL
    ORDER BY m.output_price_per_m ASC
    """)


def show_routing():
    """Show task routing matrix."""
    print("TASK ROUTING MATRIX\n")
    run_query("""
    SELECT t.task_type,
           pm.name as primary_model,
           fm.name as fallback_model,
           t.rationale
    FROM task_routing t
    JOIN models pm ON t.primary_model = pm.id
    LEFT JOIN models fm ON t.fallback_model = fm.id
    ORDER BY t.task_type
    """)

    print("\n\nIIC CHAIN ROUTING\n")
    run_query("""
    SELECT i.chain, m.name as model, i.rationale
    FROM iic_routing i
    JOIN models m ON i.model_id = m.id
    ORDER BY i.chain
    """)


def show_info(model_name):
    """Show detailed info for a model."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("""
    SELECT m.*, p.name as provider, p.tier, p.status as platform_status
    FROM models m
    JOIN platforms p ON m.platform_id = p.id
    WHERE m.name LIKE ? OR m.id LIKE ?
    """, (f"%{model_name}%", f"%{model_name}%"))

    rows = cur.fetchall()
    if not rows:
        print(f"No model found matching '{model_name}'")
        conn.close()
        return

    for row in rows:
        print(f"Model: {row['name']}")
        print(f"  Provider:    {row['provider']} ({row['tier']})")
        print(f"  API String:  {row['api_string']}")
        print(f"  Context:     {row['context_window']:,} tokens (effective: {row['effective_context']:,})")
        if row['input_price_per_m']:
            print(f"  Pricing:     ${row['input_price_per_m']}/M input, ${row['output_price_per_m']}/M output")
        print(f"  Status:      {row['status']}")
        print(f"  Released:    {row['release_date']}")
        print(f"  Notes:       {row['notes']}")

        cur.execute("SELECT capability, value, notes FROM capabilities WHERE model_id = ?", (row['id'],))
        caps = cur.fetchall()
        if caps:
            print(f"  Capabilities:")
            for cap in caps:
                note = f" ({cap['notes']})" if cap['notes'] else ""
                print(f"    - {cap['capability']}: {cap['value']}{note}")

        cur.execute("SELECT task_type, rationale FROM task_routing WHERE primary_model = ?", (row['id'],))
        tasks = cur.fetchall()
        if tasks:
            print(f"  Primary for:")
            for task in tasks:
                print(f"    - {task['task_type']}: {task['rationale']}")

        cur.execute("SELECT chain, rationale FROM iic_routing WHERE model_id = ?", (row['id'],))
        chains = cur.fetchall()
        if chains:
            print(f"  IIC chains:")
            for chain in chains:
                print(f"    - {chain['chain']}: {chain['rationale']}")

        print()

    conn.close()


def show_capabilities():
    """Show capability comparison matrix."""
    print("CAPABILITY MATRIX\n")

    # Get all unique capabilities
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT capability FROM capabilities ORDER BY capability")
    all_caps = [r[0] for r in cur.fetchall()]

    # Get all active models
    cur.execute("SELECT id, name FROM models WHERE status = 'active' ORDER BY name")
    all_models = cur.fetchall()

    # Build matrix
    header = f"{'Capability':<25}"
    for _, name in all_models:
        short = name[:12]
        header += f" | {short:<12}"
    print(header)
    print("-" * len(header))

    for cap in all_caps:
        row = f"{cap:<25}"
        for model_id, _ in all_models:
            cur.execute("SELECT value FROM capabilities WHERE model_id = ? AND capability = ?", (model_id, cap))
            result = cur.fetchone()
            val = result[0] if result else "-"
            row += f" | {val:<12}"
        print(row)

    conn.close()


def interactive_shell():
    """Interactive SQL shell."""
    print("Model Intelligence Database — Interactive Shell")
    print(f"Database: {DB_PATH}")
    print("Type SQL queries, or 'help' for commands, 'quit' to exit.\n")

    while True:
        try:
            sql = input("sql> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if not sql:
            continue
        if sql.lower() in ("quit", "exit", "q"):
            break
        if sql.lower() == "help":
            print("Commands:")
            print("  .tables     - List all tables")
            print("  .schema T   - Show schema for table T")
            print("  Any SQL     - Execute query")
            print("  quit        - Exit")
            continue
        if sql == ".tables":
            run_query("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
            continue
        if sql.startswith(".schema"):
            parts = sql.split()
            if len(parts) > 1:
                run_query(f"SELECT sql FROM sqlite_master WHERE name='{parts[1]}'")
            else:
                run_query("SELECT sql FROM sqlite_master WHERE type='table'")
            continue

        run_query(sql)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "init":
        init_db()
    elif cmd == "query" and len(sys.argv) > 2:
        run_query(" ".join(sys.argv[2:]))
    elif cmd == "search" and len(sys.argv) > 2:
        search_models(sys.argv[2])
    elif cmd == "cost":
        show_cost()
    elif cmd == "routing":
        show_routing()
    elif cmd == "info" and len(sys.argv) > 2:
        show_info(" ".join(sys.argv[2:]))
    elif cmd == "capabilities":
        show_capabilities()
    elif cmd == "shell":
        interactive_shell()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
