#!/usr/bin/env python3
"""Salience-gated, fail-open model router for the Syncrescendence constellation.

Routes tasks to the best model based on task type, complexity, agent assignment,
and rate-limit awareness. Falls back gracefully if primary choice is unavailable.

Usage:
    python3 model_router.py "design a caching layer" --agent commander
    python3 model_router.py "survey all config files" --agent cartographer --complexity simple
    python3 model_router.py "speculate on market trends" --complexity complex

DC-147 | 220-320 LOC | stdlib only | fail-open
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from typing import Optional

# ── Model Registry (ground truth: CLAUDE.md / AGENTS.md v6.0.0) ─────────────

MODELS = {
    "opus-4.6":          {"lab": "Anthropic", "tier": "frontier", "pool": "claude-max-1"},
    "sonnet-4.5":        {"lab": "Anthropic", "tier": "mid",      "pool": "claude-max-1"},
    "haiku-4.5":         {"lab": "Anthropic", "tier": "light",    "pool": "claude-max-1"},
    "gpt-5.3-codex":     {"lab": "OpenAI",   "tier": "frontier", "pool": "chatgpt-plus-shared"},
    "gpt-5.2":           {"lab": "OpenAI",   "tier": "frontier", "pool": "chatgpt-plus-shared"},
    "gemini-pro-3.1":    {"lab": "Google",    "tier": "mid",      "pool": "google-ai-pro"},
    "gemini-flash-3.0":  {"lab": "Google",    "tier": "light",    "pool": "google-ai-pro"},
    "grok-4":            {"lab": "xAI",       "tier": "frontier", "pool": "xai-api"},
    "kimi-k2.5":         {"lab": "NVIDIA",    "tier": "frontier", "pool": "nvidia-kimi"},
}

# ── Agent → Model Mapping (CLAUDE.md Enterprise Role Mapping) ───────────────

AGENT_MODELS = {
    "commander":    "opus-4.6",
    "adjudicator":  "gpt-5.3-codex",
    "cartographer":  "gemini-pro-3.1",
    "psyche":       "gpt-5.3-codex",
    "ajna":         "kimi-k2.5",
}

AGENT_ROLES = {
    "commander":    "COO — synthesis, execution, staging, compilation",
    "adjudicator":  "CQO — deep hyper-technical design/engineering",
    "cartographer": "CIO — structural surveys, cross-domain mapping",
    "psyche":       "CTO — system cohesion, automation, policy",
    "ajna":         "CSO — strategic direction, orchestration",
}

# Shared pool pairs (rate-limit awareness)
SHARED_POOLS = {
    "chatgpt-plus-shared": ["psyche", "adjudicator"],
}

# ── Task Type Classification ────────────────────────────────────────────────

TASK_SIGNALS = {
    "research":    {"keywords": ["research", "investigate", "explore", "survey", "find", "search", "audit"],
                    "models": ["grok-4", "gemini-pro-3.1", "opus-4.6"]},
    "speculation": {"keywords": ["speculate", "predict", "forecast", "imagine", "hypothesize", "what if"],
                    "models": ["grok-4", "kimi-k2.5", "opus-4.6"]},
    "synthesis":   {"keywords": ["synthesize", "compile", "merge", "unify", "combine", "integrate", "consolidate"],
                    "models": ["opus-4.6", "grok-4", "gemini-pro-3.1"]},
    "code":        {"keywords": ["implement", "code", "build", "script", "function", "refactor", "debug", "fix"],
                    "models": ["opus-4.6", "gpt-5.3-codex", "sonnet-4.5"]},
    "engineering": {"keywords": ["architect", "design", "engineer", "schema", "pipeline", "system", "infra"],
                    "models": ["gpt-5.3-codex", "opus-4.6", "grok-4"]},
    "structural":  {"keywords": ["survey", "map", "catalog", "index", "inventory", "scan", "list"],
                    "models": ["gemini-pro-3.1", "opus-4.6", "grok-4"]},
    "strategic":   {"keywords": ["strategy", "vision", "roadmap", "plan", "direction", "prioritize"],
                    "models": ["kimi-k2.5", "grok-4", "opus-4.6"]},
    "quality":     {"keywords": ["review", "validate", "verify", "test", "check", "lint", "enforce"],
                    "models": ["gpt-5.3-codex", "opus-4.6", "sonnet-4.5"]},
}

# ── Complexity → Tier Mapping ───────────────────────────────────────────────

COMPLEXITY_TIERS = {
    "simple":  "light",
    "medium":  "mid",
    "complex": "frontier",
}

TIER_PREFERENCES = {
    "light":    ["haiku-4.5", "gemini-flash-3.0", "sonnet-4.5"],
    "mid":      ["sonnet-4.5", "gemini-pro-3.1", "opus-4.6"],
    "frontier": ["opus-4.6", "grok-4", "gpt-5.3-codex", "kimi-k2.5"],
}


def classify_task(description: str) -> tuple[str, float]:
    """Score task description against signal keywords. Returns (type, confidence)."""
    desc_lower = description.lower()
    scores: dict[str, int] = {}
    for task_type, spec in TASK_SIGNALS.items():
        score = sum(1 for kw in spec["keywords"] if re.search(rf'\b{kw}\b', desc_lower))
        if score > 0:
            scores[task_type] = score

    if not scores:
        return "general", 0.0

    best = max(scores, key=scores.get)  # type: ignore[arg-type]
    total_keywords = len(TASK_SIGNALS[best]["keywords"])
    confidence = min(scores[best] / max(total_keywords, 1), 1.0)
    return best, round(confidence, 2)


def check_pool_pressure(model: str, active_agent: Optional[str]) -> bool:
    """Return True if model's pool has contention risk for this agent."""
    pool = MODELS.get(model, {}).get("pool", "")
    if pool in SHARED_POOLS and active_agent in SHARED_POOLS[pool]:
        return True
    return False


def build_fallback_chain(primary: str, task_models: list[str],
                         tier_models: list[str]) -> list[str]:
    """Build ordered fallback chain, deduplicating while preserving priority."""
    seen = {primary}
    chain = []
    for m in task_models + tier_models + list(MODELS.keys()):
        if m not in seen and m in MODELS:
            seen.add(m)
            chain.append(m)
        if len(chain) >= 3:
            break
    return chain


def route(description: str, agent: Optional[str] = None,
          complexity: Optional[str] = None) -> dict:
    """Core routing logic. Fail-open: always returns a recommendation."""

    rationale_parts = []
    task_type, confidence = classify_task(description)

    # 1. Agent-locked routing (strongest signal)
    if agent and agent in AGENT_MODELS:
        primary = AGENT_MODELS[agent]
        rationale_parts.append(f"Agent '{agent}' is assigned to {primary}")
    else:
        primary = None

    # 2. Task-type signal
    task_models = TASK_SIGNALS.get(task_type, {}).get("models", [])
    if task_type != "general":
        rationale_parts.append(
            f"Task classified as '{task_type}' (confidence={confidence})")
        if not primary and task_models:
            primary = task_models[0]

    # 3. Complexity gate — may override tier
    effective_complexity = complexity or ("complex" if not complexity else complexity)
    if not complexity:
        # Infer: long descriptions or engineering tasks → complex
        if len(description.split()) > 20 or task_type in ("engineering", "strategic"):
            effective_complexity = "complex"
        elif task_type in ("quality", "structural"):
            effective_complexity = "medium"
        else:
            effective_complexity = "medium"
        rationale_parts.append(f"Complexity inferred as '{effective_complexity}'")
    else:
        rationale_parts.append(f"Complexity specified as '{effective_complexity}'")

    target_tier = COMPLEXITY_TIERS.get(effective_complexity, "mid")
    tier_models = TIER_PREFERENCES.get(target_tier, [])

    # If no primary yet, pick from tier
    if not primary:
        primary = tier_models[0] if tier_models else "opus-4.6"
        rationale_parts.append(f"Defaulting to tier '{target_tier}' primary: {primary}")

    # 4. Pool pressure check
    if check_pool_pressure(primary, agent):
        rationale_parts.append(
            f"WARNING: {primary} shares rate-limit pool with co-agent; "
            f"consider staggering")

    # 5. Build fallback chain
    fallback_chain = build_fallback_chain(primary, task_models, tier_models)

    # 6. Fail-open guarantee
    if primary not in MODELS:
        rationale_parts.append(f"Unknown model '{primary}'; fail-open to opus-4.6")
        primary = "opus-4.6"

    result = {
        "recommended_model": primary,
        "agent": agent or "unassigned",
        "task_type": task_type,
        "task_confidence": confidence,
        "complexity": effective_complexity,
        "rationale": "; ".join(rationale_parts),
        "fallback_chain": fallback_chain,
        "pool_pressure": check_pool_pressure(primary, agent),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Syncrescendence model router — salience-gated, fail-open",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  %(prog)s 'design a caching layer' --agent commander\n"
               "  %(prog)s 'survey config files' --agent cartographer --complexity simple\n"
               "  %(prog)s 'speculate on AGI timelines' --complexity complex\n"
               "  %(prog)s 'fix the broken test' --agent adjudicator",
    )
    parser.add_argument("task", help="Task description to route")
    parser.add_argument("--agent", "-a", choices=list(AGENT_MODELS.keys()),
                        help="Agent hint (commander/adjudicator/cartographer/psyche/ajna)")
    parser.add_argument("--complexity", "-c", choices=["simple", "medium", "complex"],
                        help="Task complexity (default: auto-inferred)")
    parser.add_argument("--compact", action="store_true",
                        help="Print single-line JSON")

    args = parser.parse_args()
    result = route(args.task, agent=args.agent, complexity=args.complexity)

    indent = None if args.compact else 2
    print(json.dumps(result, indent=indent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
