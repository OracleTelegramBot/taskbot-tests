import requests, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

BASE = config["base_url"]

def test_frontend_loads():
    r = requests.get(BASE)
    assert r.status_code == 200