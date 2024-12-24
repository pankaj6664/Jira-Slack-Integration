from jira_slack_integration import JiraSlackIntegration
# import os
# from dotenv import load_dotenv
# load_dotenv()
if __name__ == "__main__":
    # Jira and Slack credentials
    jira_url = "https://pankaj-pawar1.atlassian.net/"
    jira_username = "pankajpawar5259@gmail.com"
    jira_api_token = "ATATT3xFfGF09Mt4NIdAbPHqy7PWGkcUwO3hI-f_APzYEoh5XmC-TflLI95G7u5TEGD6P_MJfteRaFNSXqmlJvh-FZiJPC2EUry04TaRq28OPoatNqaQvPO5PbMsNCKnz4yf_ntN7njVtfaZcJFx5EWOoVBPTAxwUWT7MmJnid5FnrkhhAPsbWo=F96D2417"
    project_key = "PAN1"
    slack_bot_token = "xoxp-8215098509508-8198055880263-8209572566086-7816255ae16090dcbf8c50400b83c507"
    
    # jira_url = os.getenv("JIRA_URL")
    # jira_username = os.getenv("JIRA_USERNAME")
    # jira_api_token = os.getenv("JIRA_API_TOKEN")
    # project_key = os.getenv("PROJECT_KEY")
    # slack_bot_token = os.getenv("SLACK_BOT_TOKEN")

    # Initialize the integration
    integration = JiraSlackIntegration(jira_url, jira_username, jira_api_token, project_key, slack_bot_token)

    # Start processing tickets
    integration.process_tickets()
    
    
    # if not all([jira_url, jira_username, jira_api_token, project_key, slack_bot_token]):
    #     raise EnvironmentError("Missing one or more required environment variables.")

    # # Initialize the integration
    # integration = JiraSlackIntegration(jira_url, jira_username, jira_api_token, project_key, slack_bot_token)

    # # Start processing tickets
    # integration.process_tickets()
