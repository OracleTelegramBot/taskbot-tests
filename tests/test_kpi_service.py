import requests, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

BASE = config["base_url"]

def test_kpi_health():
    r = requests.get(f"{BASE}/api/kpis/sprints/activoss")
    assert r.status_code in [200, 401, 403]
