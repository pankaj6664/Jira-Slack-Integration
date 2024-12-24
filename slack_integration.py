import requests
import json

class SlackIntegration:
    def __init__(self, slack_bot_token):
        
        """
        Initialize the SlackIntegration class with the provided Slack bot token.
        
        :param slack_bot_token: The token used to authenticate with the Slack API.
        """
        self.slack_bot_token = slack_bot_token

    def get_slack_user_id(self, email):
        
        """
        Fetch Slack user ID using their email.
        
        :param email: The email address of the Slack user.
        :return: The Slack user ID if found, otherwise None.
        """
        url = "https://slack.com/api/users.lookupByEmail"
        headers = {"Authorization": f"Bearer {self.slack_bot_token}"}
        response = requests.get(url, headers=headers, params={"email": email})
        
        if response.status_code == 200:
            data = response.json()
            # Check if the response indicates success
            if data.get("ok"):
                # Extract and return the user ID from the response
                return data.get("user", {}).get("id")
            else:
                print(f"Error fetching Slack user ID: {data.get('error')}")
        else:
            print(f"Failed to fetch Slack user ID: {response.status_code}, {response.text}")
        return None

    def send_slack_dm(self, user_id, ticket_key, summary, description, jira_link):
        
        """
        Send a direct message to a Slack user.
        
        :param user_id: The Slack user ID to send the message to.
        :param ticket_key: The key of the Jira ticket.
        :param summary: The summary of the Jira ticket.
        :param description: The description of the Jira ticket.
        :param jira_link: The link to the Jira ticket.
        """
        url = "https://slack.com/api/chat.postMessage"
        headers = {
            "Authorization": f"Bearer {self.slack_bot_token}",
            "Content-Type": "application/json"
        }
        message = {
            "channel": user_id,
            "text": (
                f"Hi,<@{user_id}> you have been assigned a new Jira ticket!\n\n"
                f"*Ticket Key:* {ticket_key}\n"
                f"*Summary:* {summary}\n"
                f"*Description:* {description}\n"
                f"<{jira_link}|View the Jira Issue>"
            )
        }
        response = requests.post(url, headers=headers, data=json.dumps(message))
        
        if response.status_code == 200:
            data = response.json()
            # Check if the response indicates success
            if data.get("ok"):
                print(f"Slack DM sent to user {user_id} for ticket {ticket_key}")
            else:
                print(f"Error sending Slack DM: {data.get('error')}")
        else:
            print(f"Failed to send Slack DM: {response.status_code}, {response.text}")