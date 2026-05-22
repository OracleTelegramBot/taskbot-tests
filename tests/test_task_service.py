import requests, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

BASE = config["base_url"]

def test_task_service_reachable():
    r = requests.get(f"{BASE}/api/tasks/sprint/1")
    assert r.status_code in [200, 401, 403, 500]
