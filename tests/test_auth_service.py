import requests, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

BASE = config["base_url"]

def test_auth_health():
    r = requests.get(f"{BASE}/api/v1/auth/health")
    assert r.status_code == 200
