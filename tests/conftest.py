import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from integrations.jira_client import create_bug_ticket


@pytest.fixture(scope="session")
def config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    d = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield d
    d.quit()


def pytest_runtest_logreport(report):
    if report.when == "call" and report.failed:
        service_name = (
            report.nodeid.split("/")[-1]
            .replace("test_", "")
            .replace(".py", "")
            .split("::")[0]
        )
        create_bug_ticket(
            test_name=report.nodeid,
            error_message=str(report.longrepr)[:500],
            service_name=service_name,
        )
