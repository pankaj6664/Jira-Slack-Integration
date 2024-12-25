import os
from dotenv import load_dotenv
from jira_slack_integration import JiraSlackIntegration

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    # Fetch credentials from environment variables
    jira_url = os.getenv("JIRA_URL")
    jira_username = os.getenv("JIRA_USERNAME")
    jira_api_token = os.getenv("JIRA_API_TOKEN")
    project_keys = os.getenv("PROJECT_KEYS").split(",")  # Multiple projects
    slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
    # print(slack_bot_token)

    if not all([jira_url, jira_username, jira_api_token, project_keys, slack_bot_token]):
        raise EnvironmentError("Missing one or more required environment variables.")

    # Initialize the integration
    integration = JiraSlackIntegration(jira_url, jira_username, jira_api_token, project_keys, slack_bot_token)

    # Start processing tickets
    integration.process_tickets()
