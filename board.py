"""Kytest-Agents live board: the workflow's architecture, lit up as nodes run.

    python board.py                         watch runs/ (latest run selected)
    python board.py --runs results/bench/test1 --port 8770

Then open http://127.0.0.1:8770. The board only reads what the engine already
writes (state.json, log.jsonl); start a run in another terminal, e.g.
`python kytest.py --mock bug`, or use the board's "Run mock" button, and the
nodes light up as their events arrive. Standard library only; binds to
127.0.0.1 and serves no file outside the page and the discovered run
directories.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "mas" / "board" / "index.html"
MOCK_SCENARIOS = ("pass", "revise", "bug", "stubborn", "flaky")
MAX_RUNS = 200


def find_runs(root: Path) -> list:
    """Run directories under root, newest first: any directory holding state.json."""
    runs = []
    for state in root.rglob("state.json"):
        if "workspace" in state.parts:
            continue
        try:
            data = json.loads(state.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        runs.append({"id": state.parent.relative_to(root).as_posix(), "status": data.get("status"),
                     "mtime": state.stat().st_mtime})
    runs.sort(key=lambda r: r["mtime"], reverse=True)
    return runs[:MAX_RUNS]


def summarize(state: dict) -> dict:
    """The parts of state.json the board shows; drops source code and long text."""
    plan = state.get("plan") or {}
    return {
        "status": state.get("status"), "next": state.get("next"), "round": state.get("round"),
        "config": state.get("config"), "history": state.get("history"), "target": state.get("target"),
        "plan": {"summary": plan.get("summary"), "items": plan.get("items", []),
                 "ambiguities": plan.get("ambiguities", [])} if plan else None,
        "testgen": [{k: t.get(k) for k in ("round", "status", "accepted", "attempts", "turns")}
                    | {"failed": [f["name"] for f in t.get("failed", [])]} for t in state.get("testgen", [])],
        "verification": state.get("verification", []),
        "reviews": state.get("reviews", []),
        "suspected_bugs": [{k: b.get(k) for k in ("name", "plan_ids", "reason", "round")}
                           for b in state.get("suspected_bugs", [])],
        "degraded": state.get("degraded", []),
        "errors": [{k: e.get(k) for k in ("node", "attempt", "round", "error")} for e in state.get("errors", [])],
        "usage": state.get("usage", {}),
    }


def read_events(run_dir: Path, cursor: int) -> tuple:
    try:
        lines = (run_dir / "log.jsonl").read_text(encoding="utf-8").splitlines()
    except OSError:
        return [], 0
    events = []
    for line in lines[cursor:]:
        try:
            event = json.loads(line)
        except ValueError:
            break  # a line still being written: pick it up next poll
        if isinstance(event.get("content"), str):
            event["content"] = event["content"][:240]
        events.append(event)
    return events, cursor + len(events)


class Board(BaseHTTPRequestHandler):
    runs_root: Path

    def log_message(self, fmt, *args):  # keep the terminal quiet
        pass

    def _send(self, code: int, body: bytes, kind: str):
        self.send_response(code)
        self.send_header("Content-Type", kind)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, data, code=200):
        self._send(code, json.dumps(data, ensure_ascii=False, default=str).encode("utf-8"),
                   "application/json; charset=utf-8")

    def _run_dir(self, run_id: str):
        # Only ids that discovery itself produced: no path from the request is trusted.
        known = {r["id"] for r in find_runs(self.runs_root)}
        return self.runs_root / run_id if run_id in known else None

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)
        if url.path == "/":
            return self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        if url.path == "/api/runs":
            return self._json({"root": str(self.runs_root), "runs": find_runs(self.runs_root),
                               "scenarios": MOCK_SCENARIOS})
        if url.path == "/api/run":
            run_dir = self._run_dir(query.get("id", [""])[0])
            if run_dir is None:
                return self._json({"error": "unknown run"}, 404)
            try:
                cursor = max(0, int(query.get("cursor", ["0"])[0]))
            except ValueError:
                cursor = 0
            events, cursor = read_events(run_dir, cursor)
            try:
                state = summarize(json.loads((run_dir / "state.json").read_text(encoding="utf-8")))
            except (OSError, ValueError):
                state = None
            return self._json({"state": state, "events": events, "cursor": cursor})
        self._json({"error": "not found"}, 404)

    def do_POST(self):
        url = urlparse(self.path)
        scenario = parse_qs(url.query).get("scenario", [""])[0]
        if url.path != "/api/mock" or scenario not in MOCK_SCENARIOS:
            return self._json({"error": "unknown scenario"}, 400)
        subprocess.Popen([sys.executable, str(ROOT / "kytest.py"), "--mock", scenario,
                          "--runs", str(self.runs_root)], cwd=ROOT,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self._json({"started": scenario})


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=ROOT / "runs", help="directory to search for runs")
    ap.add_argument("--port", type=int, default=8770)
    a = ap.parse_args(argv)
    root = a.runs.resolve()
    root.mkdir(parents=True, exist_ok=True)
    handler = type("BoundBoard", (Board,), {"runs_root": root})
    server = ThreadingHTTPServer(("127.0.0.1", a.port), handler)
    print(f"Kytest-Agents board on http://127.0.0.1:{server.server_address[1]}  (runs: {root})", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
