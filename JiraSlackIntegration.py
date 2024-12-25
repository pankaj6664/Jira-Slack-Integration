from jira_integration import JiraIntegration
from slack_integration import SlackIntegration
import time
import os

class JiraSlackIntegration:
    def __init__(self, jira_url, jira_username, jira_api_token, project_keys, slack_bot_token):
        """
        Initialize the JiraSlackIntegration class with the provided Jira and Slack credentials.
        
        :param jira_url: The base URL of the Jira instance.
        :param jira_username: The username to authenticate with Jira.
        :param jira_api_token: The API token to authenticate with Jira.
        :param project_key: The key of the Jira project.
        :param slack_bot_token: The token used to authenticate with the Slack API.
        """
        self.jira_integration = JiraIntegration(jira_url, jira_username, jira_api_token, project_keys)
        self.slack_integration = SlackIntegration(slack_bot_token)
        self.notified_tickets = {}

    def process_tickets(self):
        """Process Jira tickets and notify Slack users."""
        polling_interval = os.getenv("POLLING_INTERVAL")
        issues = self.jira_integration.fetch_assigned_tickets()
        # print(issues)

        for issue in issues:
            ticket_key = issue['key']
            fields = issue.get('fields', {})
            assignee = fields.get('assignee', None)
            summary = fields.get('summary', 'No summary provided')
            description = fields.get('description', 'No description provided')
            updated = fields.get('updated', '')
            jira_link = f"{self.jira_integration.jira_url}/browse/{ticket_key}"
            # print(jira_link)
            # print(assignee)
            if assignee:
                email = assignee.get('emailAddress', None)
                # print(email)
                if email:
                    user_id = self.slack_integration.get_slack_user_id(email)
                    print(user_id)
                    if user_id:
                        # Check if the ticket has been notified already
                        if ticket_key not in self.notified_tickets or self.notified_tickets[ticket_key] != updated:
                            self.slack_integration.send_slack_dm(user_id, ticket_key, summary, description, jira_link)
                            self.notified_tickets[ticket_key] = updated
                        else:
                            print(f"Ticket {ticket_key} has already been notified and is unchanged.")
                    else:
                        print(f"No Slack user ID found for email: {email}")
                else:
                    print(f"No email found for assignee of ticket {ticket_key}")
            else:
                print(f"Ticket {ticket_key} has no assignee.")
        time.sleep(int(polling_interval))