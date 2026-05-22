import requests, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

BASE = config["base_url"]

def test_telegram_service_reachable():
    r = requests.get(f"{BASE}/api/webhook/telegram")
    assert r.status_code in [200, 400, 401, 403, 405]