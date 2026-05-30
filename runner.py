import subprocess
import sys
from integrations.jira_client import create_bug_ticket

result = subprocess.run(
    ["pytest", "tests/", "-v", "--tb=short", "--junit-xml=report.xml", "--html=report.html", "--self-contained-html"],
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)

if result.returncode != 0:
    create_bug_ticket(
        test_name="pytest suite",
        error_message=result.stdout[-500:],
        service_name="SCRUM"
    )

sys.exit(result.returncode)
