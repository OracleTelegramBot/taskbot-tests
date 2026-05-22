import subprocess
import sys
from integrations.jira_client import create_bug_ticket

result = subprocess.run(
    ["pytest", "tests/", "-v", "--tb=short", "--junit-xml=report.xml"],
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)

if result.returncode != 0:
    create_bug_ticket(
        test_name="pytest suite",
        error_message=result.stdout[-500:],
        service_name="taskbot"
    )

sys.exit(result.returncode)