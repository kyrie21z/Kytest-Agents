"""Live board server: run discovery, the path guard and the event cursor."""
import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

import board


@pytest.fixture
def server(tmp_path):
    run = tmp_path / "a" / "run"
    (run / "workspace").mkdir(parents=True)
    (run / "state.json").write_text(json.dumps({"status": "running", "next": "testgen", "source": "SECRET SOURCE",
                                                "plan": {"items": [{"id": "P1"}], "ambiguities": []}}))
    (run / "workspace" / "state.json").write_text("{}")  # never listed: inside a workspace
    (run / "log.jsonl").write_text('{"t": 1, "event": "start", "next": "planner"}\n'
                                   '{"t": 2, "event": "node_start", "node": "planner"}\n{"t": 3, "ev')
    handler = type("H", (board.Board,), {"runs_root": tmp_path})
    srv = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()


def get(url):
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())


def test_runs_are_discovered_but_workspaces_are_not(server):
    assert [r["id"] for r in get(server + "/api/runs")["runs"]] == ["a/run"]


def test_events_resume_from_cursor_and_skip_a_half_written_line(server):
    first = get(server + "/api/run?id=a/run&cursor=0")
    assert [e["event"] for e in first["events"]] == ["start", "node_start"] and first["cursor"] == 2
    assert get(server + "/api/run?id=a/run&cursor=2")["events"] == []
    assert "source" not in first["state"] and first["state"]["plan"]["items"] == [{"id": "P1"}]


@pytest.mark.parametrize("bad", ["../a/run", "/etc", "a/run/../../x", ""])
def test_unknown_or_traversing_ids_are_refused(server, bad):
    with pytest.raises(urllib.error.HTTPError) as err:
        get(server + "/api/run?id=" + bad)
    assert err.value.code == 404


def test_only_known_mock_scenarios_can_be_started(server):
    req = urllib.request.Request(server + "/api/mock?scenario=rm", method="POST")
    with pytest.raises(urllib.error.HTTPError) as err:
        urllib.request.urlopen(req)
    assert err.value.code == 400
