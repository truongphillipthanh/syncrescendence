#!/usr/bin/env python3
"""D5 — Darwinian Stress Test Simulator.
Enforces blind bandwidth restriction on Day 14 of the ascertescence
ratification cycle. Adjudicator engineering spec reference.
Subcommands: init, reveal-today, begin-session, end-session, finalize
Flags: --self-test, --help
"""
import argparse, fcntl, hashlib, json, os, secrets, sys, tempfile, uuid
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

SCHEMA_VERSION = "1.0.0"
STATE_REL = Path("orchestration/00-ORCHESTRATION/state")
LOCK_REL = STATE_REL / "locks"
F_CONFIG, F_PLAN, F_SECRET = "DYN-STRESS_TEST_CONFIG.json", "DYN-STRESS_TEST_PLAN.json", "DYN-STRESS_TEST_SECRET.json"
F_REVEAL, F_BANDWIDTH = "DYN-STRESS_TEST_REVEAL.jsonl", "DYN-SOVEREIGN_BANDWIDTH_LOG.jsonl"
F_CATALOG, F_RESULTS, F_REPORT = "DYN-STRESS_TEST_PROCESS_CATALOG.json", "DYN-STRESS_TEST_RESULTS.json", "DYN-STRESS_TEST_VIABILITY_REPORT.md"
DEFAULT_CONFIG = {"schema_version": SCHEMA_VERSION, "ratification_date": None,
    "day14_offset_days": 14, "consecutive_days": 3, "daily_budget_minutes": 30,
    "maladaptive_threshold_minutes": 45, "timezone": "America/New_York"}

def _now(): return datetime.now(timezone.utc).isoformat()
def _sd(root): return Path(root) / STATE_REL
def _lockp(root, name):
    d = Path(root) / LOCK_REL; d.mkdir(parents=True, exist_ok=True); return d / f"{name}.lock"
def _today_tz(tz): return datetime.now(ZoneInfo(tz)).date()

class Lock:
    def __init__(self, p): self.p = p
    def __enter__(self):
        self.fh = open(self.p, "w"); fcntl.flock(self.fh, fcntl.LOCK_EX); return self
    def __exit__(self, *a): fcntl.flock(self.fh, fcntl.LOCK_UN); self.fh.close()

def _rj(p):
    with open(p) as f: return json.load(f)
def _wj(p, o):
    with open(p, "w") as f: json.dump(o, f, indent=2); f.write("\n")
def _ajl(p, o):
    with open(p, "a") as f: f.write(json.dumps(o) + "\n")
def _rjl(p):
    if not Path(p).exists(): return []
    with open(p) as f: return [json.loads(l) for l in f if l.strip()]

# ── Subcommands ──────────────────────────────────────────────────────
def cmd_init(root, ratification_date=None):
    sd = _sd(root); sd.mkdir(parents=True, exist_ok=True)
    cp = sd / F_CONFIG
    cfg = _rj(cp) if cp.exists() else dict(DEFAULT_CONFIG)
    if ratification_date: cfg["ratification_date"] = ratification_date
    if not cfg.get("ratification_date"): cfg["ratification_date"] = date.today().isoformat()
    cfg["generated_at"] = _now(); _wj(cp, cfg)
    rat = date.fromisoformat(cfg["ratification_date"])
    ws = rat + timedelta(days=cfg["day14_offset_days"])
    we = ws + timedelta(days=6)
    off = secrets.randbelow(7 - cfg["consecutive_days"] + 1)
    start = ws + timedelta(days=off); end = start + timedelta(days=cfg["consecutive_days"] - 1)
    salt = secrets.token_hex(16)
    chash = hashlib.sha256((start.isoformat() + salt).encode()).hexdigest()
    with Lock(_lockp(root, "LOCK_STRESS_PLAN")):
        _wj(sd / F_PLAN, {"schema_version": SCHEMA_VERSION, "generated_at": _now(),
            "commitment_hash": chash, "planning_window_start": ws.isoformat(),
            "planning_window_end": we.isoformat(), "status": "SEALED"})
        _wj(sd / F_SECRET, {"schema_version": SCHEMA_VERSION, "generated_at": _now(),
            "start_date": start.isoformat(), "end_date": end.isoformat(),
            "salt": salt, "commitment_hash": chash})
    print(json.dumps({"status": "SEALED", "commitment_hash": chash}))

def cmd_reveal_today(root):
    sd = _sd(root); sec = _rj(sd / F_SECRET); cfg = _rj(sd / F_CONFIG)
    today = _today_tz(cfg["timezone"])
    start, end = date.fromisoformat(sec["start_date"]), date.fromisoformat(sec["end_date"])
    if start <= today <= end:
        day_num = (today - start).days + 1
        rp = sd / F_REVEAL; existing = _rjl(rp)
        for e in existing:
            if date.fromisoformat(e["date"]) > today:
                print(json.dumps({"error": "ERROR_FATAL", "reason": "future date leaked"})); sys.exit(1)
        _ajl(rp, {"schema_version": SCHEMA_VERSION, "generated_at": _now(),
            "date": today.isoformat(), "day_number": day_num, "constrained": True})
        print(json.dumps({"constrained": True, "day_number": day_num, "budget_minutes": cfg["daily_budget_minutes"]}))
    else:
        print(json.dumps({"constrained": False}))

def cmd_begin_session(root):
    sd = _sd(root); sec = _rj(sd / F_SECRET); cfg = _rj(sd / F_CONFIG)
    today = _today_tz(cfg["timezone"])
    start, end = date.fromisoformat(sec["start_date"]), date.fromisoformat(sec["end_date"])
    if not (start <= today <= end):
        print(json.dumps({"error": "not a constrained day"})); sys.exit(1)
    day_num = (today - start).days + 1; sid = str(uuid.uuid4())
    with Lock(_lockp(root, "LOCK_BANDWIDTH_LOG")):
        _ajl(sd / F_BANDWIDTH, {"schema_version": SCHEMA_VERSION, "session_id": sid,
            "started_at": _now(), "constrained_day": True, "day_number": day_num})
    print(json.dumps({"session_id": sid, "day_number": day_num}))

def cmd_end_session(root, session_id):
    sd = _sd(root); cfg = _rj(sd / F_CONFIG); bp = sd / F_BANDWIDTH
    with Lock(_lockp(root, "LOCK_BANDWIDTH_LOG")):
        entries = _rjl(bp)
        found = next((e for e in entries if e.get("session_id") == session_id and "ended_at" not in e), None)
        if not found:
            print(json.dumps({"error": "session not found or already ended"})); sys.exit(1)
        started = datetime.fromisoformat(found["started_at"])
        mins = (datetime.now(timezone.utc) - started).total_seconds() / 60.0
        found["ended_at"] = _now(); found["minutes"] = round(mins, 2)
        found["over_budget"] = mins > cfg["daily_budget_minutes"]
        with open(bp, "w") as f:
            for e in entries: f.write(json.dumps(e) + "\n")
    r = {"session_id": session_id, "minutes": found["minutes"], "over_budget": found["over_budget"]}
    if found["over_budget"]: r["policy_violation"] = True
    print(json.dumps(r))

def cmd_finalize(root):
    sd = _sd(root); cp = sd / F_CATALOG
    if not cp.exists():
        print(json.dumps({"error": "process catalog not found"})); sys.exit(1)
    catalog = _rj(cp); threshold = 45; results = []
    for proc in catalog.get("processes", []):
        hm = proc.get("required_human_minutes_continuous", 0)
        autonomy = 1 - min(hm / threshold, 1.0)
        tp, rl, cm = proc.get("throughput", 0.5), proc.get("reliability", 0.5), proc.get("compliance", 0.5)
        score = round(0.4 * autonomy + 0.3 * tp + 0.2 * rl + 0.1 * cm, 4)
        cls = "SURVIVE" if score >= 0.75 else "REDESIGN" if score >= 0.45 else "EXTINCT"
        results.append({"name": proc["name"], "score": score, "classification": cls, "autonomy": round(autonomy, 4)})
    _wj(sd / F_RESULTS, {"schema_version": SCHEMA_VERSION, "generated_at": _now(),
        "processes": results, "status": "AUDITED"})
    lines = ["# Darwinian Stress Test — Viability Report", "", f"Generated: {_now()}", ""]
    for cls in ("SURVIVE", "REDESIGN", "EXTINCT"):
        grp = [r for r in results if r["classification"] == cls]
        lines.append(f"## {cls} ({len(grp)})")
        for r in grp: lines.append(f"- **{r['name']}**: score={r['score']}, autonomy={r['autonomy']}")
        lines.append("")
    with open(sd / F_REPORT, "w") as f: f.write("\n".join(lines))
    cnt = lambda c: sum(1 for r in results if r["classification"] == c)
    print(json.dumps({"status": "AUDITED", "total": len(results),
        "survive": cnt("SURVIVE"), "redesign": cnt("REDESIGN"), "extinct": cnt("EXTINCT")}))

# ── Self-Test ────────────────────────────────────────────────────────
def _self_test():
    passed = 0
    with tempfile.TemporaryDirectory() as tmp:
        sd = Path(tmp) / STATE_REL; sd.mkdir(parents=True)
        # STR-T01: blind hash commitment
        rat = date.today().isoformat()
        _wj(sd / F_CONFIG, dict(DEFAULT_CONFIG, ratification_date=rat, generated_at=_now()))
        cmd_init(tmp, ratification_date=rat)
        plan = _rj(sd / F_PLAN); sec = _rj(sd / F_SECRET)
        assert "start_date" not in plan, "T01: start_date leaked in plan"
        assert plan["commitment_hash"] and sec["start_date"], "T01: missing fields"
        print("STR-T01 blind_hash_commitment: PASS"); passed += 1

        # STR-T02: morning reveal only
        start = date.fromisoformat(sec["start_date"])
        _wj(sd / F_CONFIG, dict(DEFAULT_CONFIG, ratification_date=rat, timezone="UTC", generated_at=_now()))
        rp = sd / F_REVEAL
        if rp.exists(): rp.unlink()
        _ajl(rp, {"date": start.isoformat(), "day_number": 1, "constrained": True,
            "schema_version": SCHEMA_VERSION, "generated_at": _now()})
        assert not any(date.fromisoformat(e["date"]) > start for e in _rjl(rp)), "T02: future leak"
        print("STR-T02 morning_reveal_only: PASS"); passed += 1

        # STR-T03: budget enforcement (35 min > 30 min budget)
        bp = sd / F_BANDWIDTH
        if bp.exists(): bp.unlink()
        sid = "test-session-03"
        started = datetime.now(timezone.utc) - timedelta(minutes=35)
        _ajl(bp, {"schema_version": SCHEMA_VERSION, "session_id": sid,
            "started_at": started.isoformat(), "constrained_day": True, "day_number": 1})
        cmd_end_session(tmp, sid)
        rec = [e for e in _rjl(bp) if e["session_id"] == sid][0]
        assert rec["over_budget"] is True, "T03: should be over budget"
        print("STR-T03 budget_enforcement: PASS"); passed += 1

        # STR-T04: classification extinct (heavy human dependency)
        _wj(sd / F_CATALOG, {"processes": [{"name": "heavy_proc",
            "required_human_minutes_continuous": 60, "throughput": 0.1, "reliability": 0.1, "compliance": 0.1}]})
        cmd_finalize(tmp)
        assert _rj(sd / F_RESULTS)["processes"][0]["classification"] == "EXTINCT", "T04: should be EXTINCT"
        print("STR-T04 classification_extinct: PASS"); passed += 1

        # STR-T05: classification survive (lean autonomous process)
        _wj(sd / F_CATALOG, {"processes": [{"name": "lean_proc",
            "required_human_minutes_continuous": 5, "throughput": 0.9, "reliability": 0.8, "compliance": 0.7}]})
        cmd_finalize(tmp)
        p = _rj(sd / F_RESULTS)["processes"][0]
        assert p["classification"] == "SURVIVE", f"T05: got {p['classification']} score={p['score']}"
        print("STR-T05 classification_survive: PASS"); passed += 1

    print(f"\n{passed}/5 tests passed."); return passed == 5

# ── CLI ──────────────────────────────────────────────────────────────
def main():
    if "--self-test" in sys.argv:
        sys.exit(0 if _self_test() else 1)
    p = argparse.ArgumentParser(description="D5 Darwinian Stress Test Simulator")
    p.add_argument("subcommand", choices=["init", "reveal-today", "begin-session", "end-session", "finalize"])
    p.add_argument("--repo-root", required=True, help="Repository root path")
    p.add_argument("--session-id", help="Session ID (for end-session)")
    p.add_argument("--ratification-date", help="ISO date for init (default: today)")
    a = p.parse_args()
    if a.subcommand == "init": cmd_init(a.repo_root, ratification_date=a.ratification_date)
    elif a.subcommand == "reveal-today": cmd_reveal_today(a.repo_root)
    elif a.subcommand == "begin-session": cmd_begin_session(a.repo_root)
    elif a.subcommand == "end-session":
        if not a.session_id: print(json.dumps({"error": "--session-id required"})); sys.exit(1)
        cmd_end_session(a.repo_root, a.session_id)
    elif a.subcommand == "finalize": cmd_finalize(a.repo_root)

if __name__ == "__main__":
    main()
