#!/usr/bin/env python3
"""CC35 D1 DAG tension monitor."""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import math
import os
import re
import sys
import tempfile
import time
from pathlib import Path

SCHEMA = "1.0.0"
UNRESOLVED = {"OPEN", "PARTIAL", "BLOCKED"}
R = {
    "dag": "engine/02-ENGINE/certescence/DYN-DAG_STATE.json",
    "dag_md": "engine/02-ENGINE/certescence/PROTOCOL-ASCERTESCENCE.md",
    "lattice": "orchestration/00-ORCHESTRATION/state/DYN-LATTICE_HEALTH.json",
    "thr": "orchestration/00-ORCHESTRATION/state/DYN-ASCERTESCENCE_THRESHOLDS.yaml",
    "ambient": "orchestration/00-ORCHESTRATION/state/DYN-COWORK_AMBIENT_OPS.jsonl",
    "hist": "orchestration/00-ORCHESTRATION/state/DYN-DAG_TENSION_HISTORY.jsonl",
    "audit": "orchestration/00-ORCHESTRATION/state/DYN-EPISTEMIC_ENERGY_AUDIT.jsonl",
    "signal": "orchestration/00-ORCHESTRATION/state/DYN-DAG_SIGNAL.json",
    "locks": "orchestration/00-ORCHESTRATION/state/locks",
}
SAFE_THR = {
    "fire_threshold_base": 30.0,
    "cooldown_hours": 12,
    "status_weights": {"OPEN": 1.0, "PARTIAL": 0.6, "BLOCKED": 1.2},
    "max_allowed_new_nodes_ambient": 0,
    "ambient_charge_per_node": 5.0,
    "ambient_charge_cap": 30.0,
}
SAFE_LATTICE = {"global_coherence": 0.70, "global_drift": 0.0, "fragmentation_index": 0.0}


def znow(ts=None):
    ts = ts or dt.datetime.now(dt.timezone.utc)
    return ts.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def iso(s):
    if not s:
        return None
    s = s.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        d = dt.datetime.fromisoformat(s)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def p75(vals):
    if not vals:
        return 1.0
    vals = sorted(vals)
    if len(vals) == 1:
        return vals[0]
    i = 0.75 * (len(vals) - 1)
    a, b = math.floor(i), math.ceil(i)
    return vals[a] if a == b else vals[a] + (vals[b] - vals[a]) * (i - a)


def clamp(lo, hi, x):
    return max(lo, min(hi, x))


def scalar(raw):
    raw = raw.strip()
    if not raw:
        return ""
    if raw[:1] in {"'", '"'} and raw[-1:] == raw[:1]:
        return raw[1:-1]
    if re.fullmatch(r"[-+]?\d+", raw):
        return int(raw)
    if re.fullmatch(r"[-+]?\d+(\.\d+)?", raw):
        return float(raw)
    return raw


def parse_yaml(path):
    out, parent = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].rstrip()
        if not line.strip() or ":" not in line:
            continue
        if re.match(r"^\S[^:]*:\s*$", line):
            parent = line.split(":", 1)[0].strip()
            out[parent] = {}
            continue
        if line.startswith("  ") and parent and isinstance(out.get(parent), dict):
            k, v = line.strip().split(":", 1)
            out[parent][k.strip()] = scalar(v)
        else:
            k, v = line.split(":", 1)
            out[k.strip()] = scalar(v)
            parent = None
    return out


def append_jsonl(path, row):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(row, ensure_ascii=True) + "\n"
    for _ in range(2):
        try:
            with path.open("a", encoding="utf-8") as handle:
                handle.write(payload)
            return
        except OSError:
            time.sleep(0.05)


def write_json(path, row):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(row, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def load_thresholds(path):
    cfg = json.loads(json.dumps(SAFE_THR))
    reasons = []
    try:
        if not path.exists():
            raise ValueError("missing")
        text = path.read_text(encoding="utf-8")
        d = json.loads(text) if text.lstrip().startswith(("{", "[")) else parse_yaml(path)
        fire = float(d.get("fire_threshold_base"))
        cool = int(d.get("cooldown_hours"))
        ws = d.get("status_weights", {})
        w = {k: float(ws[k]) for k in ("OPEN", "PARTIAL", "BLOCKED")}
        if fire <= 0 or cool < 0 or any(v <= 0 for v in w.values()):
            raise ValueError("invalid")
        cfg.update({"fire_threshold_base": fire, "cooldown_hours": cool, "status_weights": w})
        cfg["max_allowed_new_nodes_ambient"] = int(d.get("max_allowed_new_nodes_ambient", 0))
        cfg["ambient_charge_per_node"] = float(d.get("ambient_charge_per_node", 5.0))
        cfg["ambient_charge_cap"] = float(d.get("ambient_charge_cap", 30.0))
    except Exception:
        reasons.append("INVALID_THRESHOLD_CONFIG")
    return cfg, reasons


def load_lattice(path, now):
    d, reasons = dict(SAFE_LATTICE), []
    if not path.exists():
        return d, ["MISSING_LATTICE_HEALTH"]
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        for k in SAFE_LATTICE:
            if isinstance(raw.get(k), (int, float)):
                d[k] = float(raw[k])
        g = iso(str(raw.get("generated_at", "")))
        if g and (now - g) > dt.timedelta(hours=24):
            reasons.append("STALE_LATTICE_HEALTH")
    except Exception:
        reasons.append("MISSING_LATTICE_HEALTH")
    return d, reasons


def dag_from_md(path, now):
    tier, out = 0, {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        t = re.match(r"^####\s+Tier\s+(\d+)", line)
        if t:
            tier = int(t.group(1))
        n = re.search(r"\*\*(C-\d{3})\*\*", line)
        if n:
            out[n.group(1)] = {
                "node_id": n.group(1),
                "tier": tier,
                "status": "OPEN",
                "last_state_change_at": znow(now),
            }
    return [out[k] for k in sorted(out)]


def load_nodes(dag_json, dag_md, now):
    if dag_json.exists():
        try:
            nodes = json.loads(dag_json.read_text(encoding="utf-8")).get("nodes", [])
            if isinstance(nodes, list) and nodes:
                return nodes
        except Exception:
            pass
    if dag_md.exists():
        nodes = dag_from_md(dag_md, now)
        if nodes:
            return nodes
    raise RuntimeError("ERROR_FATAL_DAG_SOURCE_UNAVAILABLE")


def read_hist(path):
    last_fire = last_any = None
    if not path.exists():
        return None, None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = iso(str(rec.get("generated_at") or rec.get("timestamp") or ""))
        if ts and (not last_any or ts > last_any):
            last_any = ts
        if rec.get("signal") == "FIRE" and ts and (not last_fire or ts > last_fire):
            last_fire = ts
    return last_fire, last_any


def audit_ambient(path, since, max_allowed):
    checked = max_net = 0
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines() if path.exists() else []
    for line in lines:
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = iso(str(r.get("generated_at") or r.get("timestamp") or r.get("created_at") or ""))
        if since and ts and ts <= since:
            continue
        before = r.get("open_nodes_before", r.get("node_count_open_before"))
        after = r.get("open_nodes_after", r.get("node_count_open_after"))
        net = r.get("net_new_nodes")
        if net is None and isinstance(before, (int, float)) and isinstance(after, (int, float)):
            net = after - before
        if not isinstance(net, (int, float)):
            continue
        checked += 1
        max_net = max(max_net, int(net))
    return {
        "energy_audit_status": "REJECT" if max_net > max_allowed else "PASS",
        "ops_checked": checked,
        "max_net_new_nodes": max_net,
    }


def compute(nodes, weights, lattice, now):
    u = [n for n in nodes if str(n.get("status", "")).upper() in UNRESOLVED]
    inter = clamp(0.5, 2.0, 1.0 + lattice["fragmentation_index"] + max(0.0, lattice["global_drift"] - 0.05))
    if not u:
        return 0.0, 0, 1.0, 0.0, inter
    ages, wsum = [], 0.0
    for n in u:
        st = str(n.get("status", "OPEN")).upper()
        ts = iso(str(n.get("last_state_change_at") or n.get("created_at") or "")) or now
        ages.append(max(0.0, (now - ts).total_seconds() / 86400.0))
        wsum += float(weights.get(st, 1.0))
    age = max(1.0, p75(ages))
    return len(u) * age * wsum * inter, len(u), age, wsum, inter


def run_once(repo_root, p, mode, now, write_state=True):
    thr, reasons = load_thresholds(p["thr"])
    try:
        nodes = load_nodes(p["dag"], p["dag_md"], now)
    except RuntimeError as e:
        return 1, {
            "signal": "HOLD",
            "tension": 0.0,
            "threshold": float(thr["fire_threshold_base"]),
            "node_count_unresolved": 0,
            "reason_codes": [str(e)],
            "energy_audit_status": "PASS",
        }

    lattice, lr = load_lattice(p["lattice"], now)
    reasons += lr
    tension, count, age, wsum, inter = compute(nodes, thr["status_weights"], lattice, now)
    threshold = float(thr["fire_threshold_base"])
    last_fire, last_hist = read_hist(p["hist"])
    energy = audit_ambient(p["ambient"], last_hist, int(thr["max_allowed_new_nodes_ambient"]))

    # Ambient charge: violations increase tension instead of vetoing
    max_allowed = int(thr.get("max_allowed_new_nodes_ambient", 0))
    charge_per_node = float(thr["ambient_charge_per_node"])
    charge_cap = float(thr["ambient_charge_cap"])
    excess_nodes = max(0, energy.get("max_net_new_nodes", 0) - max_allowed)
    ambient_charge = min(charge_cap, excess_nodes * charge_per_node)
    effective_tension = tension + ambient_charge

    signal, state = "HOLD", "READY"
    if mode == "audit-only":
        reasons.append("AUDIT_ONLY_MODE")
    elif effective_tension >= threshold:
        cool = dt.timedelta(hours=int(thr["cooldown_hours"]))
        if last_fire and now < (last_fire + cool):
            reasons.append("COOLDOWN_ACTIVE")
            state = "COOLDOWN"
        else:
            signal, state = "FIRE", "FIRE"
            reasons.append("THRESHOLD_EXCEEDED")
    else:
        reasons.append("BELOW_THRESHOLD")
        state = "CHARGING" if ambient_charge > 0 else "READY"
    if energy["energy_audit_status"] == "REJECT":
        reasons.append("ENERGY_VIOLATION")

    payload = {
        "signal": signal,
        "tension": round(tension, 4),
        "effective_tension": round(effective_tension, 4),
        "ambient_charge": round(ambient_charge, 4),
        "threshold": threshold,
        "oscillator_state": state,
        "node_count_unresolved": count,
        "reason_codes": sorted(set(reasons)),
        "energy_audit_status": energy["energy_audit_status"],
    }

    if write_state:
        g = znow(now)
        append_jsonl(p["hist"], {
            "schema_version": SCHEMA,
            "generated_at": g,
            "state": state,
            "mode": mode,
            "age_days_p75": round(age, 4),
            "unresolved_status_weighted": round(wsum, 4),
            "lattice_interference_score": round(inter, 4),
            **payload,
        })
        append_jsonl(p["audit"], {
            "schema_version": SCHEMA,
            "generated_at": g,
            "state": "AUDIT_AMBIENT",
            **energy,
            "reason_codes": payload["reason_codes"],
        })
        write_json(p["signal"], {"schema_version": SCHEMA, "generated_at": g, "state": state, "mode": mode, **payload})
    return 0, payload


def lock(path, timeout=5.0):
    path.parent.mkdir(parents=True, exist_ok=True)
    h, stop = path.open("a+", encoding="utf-8"), time.monotonic() + timeout
    while True:
        try:
            fcntl.flock(h.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            h.seek(0)
            h.truncate()
            h.write(str(os.getpid()))
            h.flush()
            return h
        except BlockingIOError:
            if time.monotonic() >= stop:
                h.close()
                return None
            time.sleep(0.1)


def self_test(_repo_root):
    now = iso("2026-02-26T12:00:00Z")

    def nodes(statuses, age_days):
        return [
            {
                "node_id": f"C-{i:03d}",
                "tier": 0,
                "status": s,
                "last_state_change_at": znow(now - dt.timedelta(days=age_days)),
            }
            for i, s in enumerate(statuses, 1)
        ]

    def case(cid, n, threshold, ambient=None, hist=None, lattice_at="2026-02-26T00:00:00Z"):
        with tempfile.TemporaryDirectory(prefix=f"{cid.lower()}-") as td:
            root = Path(td)
            (root / "engine/02-ENGINE/certescence").mkdir(parents=True)
            (root / "orchestration/00-ORCHESTRATION/state").mkdir(parents=True)
            write_json(root / R["dag"], {"nodes": n})
            (root / R["thr"]).write_text(
                f"fire_threshold_base: {threshold}\n"
                "cooldown_hours: 12\n"
                "status_weights:\n  OPEN: 1.0\n  PARTIAL: 0.6\n  BLOCKED: 1.2\n"
                "max_allowed_new_nodes_ambient: 0\n"
                "ambient_charge_per_node: 5.0\n"
                "ambient_charge_cap: 30.0\n",
                encoding="utf-8",
            )
            write_json(root / R["lattice"], {
                "generated_at": lattice_at,
                "global_coherence": 0.7,
                "global_drift": 0.2,
                "fragmentation_index": 0.1,
            })
            for x in (ambient or []):
                append_jsonl(root / R["ambient"], x)
            for x in (hist or []):
                append_jsonl(root / R["hist"], x)
            p = {k: root / v for k, v in R.items() if k != "locks"}
            return run_once(root, p, "monitor", now, True)[1]

    tests = [
        ("DTM-T01", lambda r: r["signal"] == "FIRE", case("DTM-T01", nodes(["OPEN"] * 8, 4), 30.0)),
        ("DTM-T02", lambda r: r["signal"] == "HOLD", case("DTM-T02", nodes(["PARTIAL", "PARTIAL"], 1), 10.0)),
        (
            "DTM-T03",
            lambda r: r["signal"] == "FIRE" and r["energy_audit_status"] == "REJECT" and "ENERGY_VIOLATION" in r["reason_codes"] and r["ambient_charge"] > 0,
            case("DTM-T03", nodes(["OPEN"] * 8, 4), 30.0, ambient=[{"timestamp": "2026-02-26T11:00:00Z", "open_nodes_before": 4, "open_nodes_after": 5}]),
        ),
        (
            "DTM-T04",
            lambda r: r["signal"] == "HOLD" and "COOLDOWN_ACTIVE" in r["reason_codes"],
            case("DTM-T04", nodes(["OPEN"] * 8, 4), 30.0, hist=[{"generated_at": "2026-02-26T09:00:00Z", "signal": "FIRE"}]),
        ),
        (
            "DTM-T05",
            lambda r: "STALE_LATTICE_HEALTH" in r["reason_codes"],
            case("DTM-T05", nodes(["OPEN"] * 3, 2), 30.0, lattice_at="2026-02-25T00:00:00Z"),
        ),
    ]

    bad = []
    for name, ok, res in tests:
        if ok(res):
            print(f"[PASS] {name}")
        else:
            bad.append(name)
            print(f"[FAIL] {name}: {json.dumps(res, ensure_ascii=True)}")
    if bad:
        print(f"self-test failures: {', '.join(bad)}", file=sys.stderr)
        return 1
    print("self-test: all 5 passed")
    return 0


def path_arg(repo_root, value, default_rel):
    if not value:
        return repo_root / default_rel
    p = Path(value)
    return p if p.is_absolute() else (repo_root / p)


def main():
    ap = argparse.ArgumentParser(description="Compute DAG tension and emit FIRE/HOLD signal")
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--dag-state")
    ap.add_argument("--dag-fallback-md")
    ap.add_argument("--lattice-health")
    ap.add_argument("--threshold-config")
    ap.add_argument("--ambient-op-log")
    ap.add_argument("--mode", choices=["monitor", "audit-only"], default="monitor")
    ap.add_argument("--now")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    repo = Path(a.repo_root).resolve()
    if a.self_test:
        return self_test(repo)

    now = iso(a.now) if a.now else dt.datetime.now(dt.timezone.utc)
    if not now:
        print("ERROR: invalid --now", file=sys.stderr)
        return 2

    p = {
        "dag": path_arg(repo, a.dag_state, R["dag"]),
        "dag_md": path_arg(repo, a.dag_fallback_md, R["dag_md"]),
        "lattice": path_arg(repo, a.lattice_health, R["lattice"]),
        "thr": path_arg(repo, a.threshold_config, R["thr"]),
        "ambient": path_arg(repo, a.ambient_op_log, R["ambient"]),
        "hist": repo / R["hist"],
        "audit": repo / R["audit"],
        "signal": repo / R["signal"],
    }

    ldir = repo / R["locks"]
    l3 = lock(ldir / "LOCK_LATTICE_HEALTH.lock")
    l4 = lock(ldir / "LOCK_DAG_STATE.lock") if l3 else None
    if not (l3 and l4):
        if l3:
            fcntl.flock(l3.fileno(), fcntl.LOCK_UN)
            l3.close()
        print(json.dumps({
            "signal": "HOLD",
            "tension": 0.0,
            "threshold": SAFE_THR["fire_threshold_base"],
            "node_count_unresolved": 0,
            "reason_codes": ["CONCURRENT_MONITOR_RACE"],
            "energy_audit_status": "PASS",
        }, ensure_ascii=True))
        return 0

    try:
        code, payload = run_once(repo, p, a.mode, now, True)
    finally:
        fcntl.flock(l4.fileno(), fcntl.LOCK_UN)
        l4.close()
        fcntl.flock(l3.fileno(), fcntl.LOCK_UN)
        l3.close()

    print(json.dumps(payload, ensure_ascii=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
