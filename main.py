import time
import requests
from jira_integration import JiraIntegration
from slack_integration import SlackIntegration

class JiraSlackIntegration:
    def __init__(self, jira_url, jira_username, jira_api_token, project_key, slack_bot_token):
        self.jira_integration = JiraIntegration(jira_url, jira_username, jira_api_token, project_key)
        self.slack_integration = SlackIntegration(slack_bot_token)
        self.notified_tickets = {}

    def process_tickets(self):
        """Process Jira tickets and notify Slack users."""
        while True:
            issues = self.jira_integration.fetch_assigned_tickets()
            
            # print(issues)
            for issue in issues:
                
                ticket_key = issue['key']
                fields = issue.get('fields', {})
                assignee = fields.get('assignee', None)
                # displayName=fields.get('displayName',None)
                summary = fields.get('summary', 'No summary provided')
                description = fields.get('description', 'No description provided')
                updated = fields.get('updated', '')
                jira_link = f"{self.jira_integration.jira_url}/browse/{ticket_key}"

                if assignee:
                    email = assignee.get('emailAddress', None)
                    
                    # print(assignee)
                    # print(displayName)
                    if email:
                        user_id = self.slack_integration.get_slack_user_id(email)
                        # print(user_id)
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
            time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    jira_url = "https://pankaj-pawar1.atlassian.net/"
    jira_username = "pankajpawar5259@gmail.com"
    jira_api_token = "ATATT3xFfGF09Mt4NIdAbPHqy7PWGkcUwO3hI-f_APzYEoh5XmC-TflLI95G7u5TEGD6P_MJfteRaFNSXqmlJvh-FZiJPC2EUry04TaRq28OPoatNqaQvPO5PbMsNCKnz4yf_ntN7njVtfaZcJFx5EWOoVBPTAxwUWT7MmJnid5FnrkhhAPsbWo=F96D2417"
    project_key = "PAN1"
    slack_bot_token = "xoxp-8215098509508-8198055880263-8209572566086-7816255ae16090dcbf8c50400b83c507"

    integration = JiraSlackIntegration(jira_url, jira_username, jira_api_token, project_key, slack_bot_token)
    integration.process_tickets()
