#!/usr/bin/env python3
"""Webhook receiver and task dispatcher for Syncrescendence constellation."""
from config import *

import subprocess
from datetime import datetime, timezone
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

VAULT = Path("/Users/home/Desktop/syncrescendence")
INBOX = VAULT / "-INBOX"
LEDGER = VAULT / "orchestration/state/DYN-GLOBAL_LEDGER.md"
AGENTS = ["commander", "adjudicator", "cartographer", "psyche", "ajna"]

app = FastAPI(title="Syncrescendence Webhook Receiver")


class DispatchRequest(BaseModel):
    agent: str
    topic: str
    description: str
    from_agent: str = "webhook"


class WebhookEvent(BaseModel):
    event: str
    data: dict = {}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


@app.get("/status")
def status():
    counts = {}
    for agent in AGENTS:
        inbox_dir = INBOX / agent / "00-INBOX0"
        if inbox_dir.exists():
            tasks = [f.name for f in inbox_dir.glob("TASK-*.md")]
            counts[agent] = {"pending": len(tasks), "files": tasks}
        else:
            counts[agent] = {"pending": 0, "files": []}
    git_status = "unknown"
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(VAULT), capture_output=True, text=True, timeout=5,
        )
        lines = [l for l in result.stdout.strip().split("\n") if l]
        git_status = f"{len(lines)} modified" if lines else "clean"
    except Exception as e:
        git_status = f"error: {e}"
    return {"inbox_counts": counts, "git_status": git_status, "timestamp": now_iso()}


@app.post("/dispatch")
def dispatch(req: DispatchRequest):
    if req.agent not in AGENTS:
        raise HTTPException(400, f"Unknown agent: {req.agent}. Valid: {AGENTS}")
    inbox_dir = INBOX / req.agent / "00-INBOX0"
    inbox_dir.mkdir(parents=True, exist_ok=True)
    stamp = now_stamp()
    filename = f"TASK-{stamp}-{req.topic.replace(' ', '_')[:30]}.md"
    filepath = inbox_dir / filename
    content = f"""# TASK: {req.topic}
**From**: {req.from_agent}
**To**: {req.agent}
**Reply-To**: {req.from_agent}
**CC**: {req.from_agent}
**Status**: PENDING
**Priority**: P2
**Issued**: {now_iso()}

## Objective
{req.description}
"""
    filepath.write_text(content, encoding="utf-8")
    # Append to ledger
    entry = f"| {now_iso()} | DISPATCH | {req.from_agent} -> {req.agent} | {req.topic} |\n"
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(entry)
    return {"dispatched": True, "file": str(filepath), "timestamp": now_iso()}


@app.post("/webhook")
def webhook(event: WebhookEvent):
    entry = f"| {now_iso()} | WEBHOOK:{event.event} | external | {str(event.data)[:120]} |\n"
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(entry)
    return {"received": True, "event": event.event, "timestamp": now_iso()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888, log_level="info")
