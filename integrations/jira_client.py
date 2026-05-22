import os
from jira import JIRA

def create_bug_ticket(test_name, error_message, service_name):
    token = os.environ.get("JIRA_API_TOKEN")
    if not token:
        print("JIRA_API_TOKEN no configurado, saltando creación de ticket")
        return

    jira = JIRA(
        server="https://taskbot.atlassian.net",
        basic_auth=("email@tec.mx", token)
    )

    jira.create_issue(
        project="TASKBOT",
        summary=f"[AUTO] Fallo en {test_name} — {service_name}",
        description=f"Error: {error_message}",
        issuetype={"name": "Bug"},
        labels=["auto-generated", "devops", service_name]
    )
    print(f"Ticket creado en Jira para {test_name}")