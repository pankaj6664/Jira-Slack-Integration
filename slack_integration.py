import requests
import json

class SlackIntegration:
    def __init__(self, slack_bot_token):
        self.slack_bot_token = slack_bot_token

    def get_slack_user_id(self, email):
        """Fetch Slack user ID using their email."""
        url = "https://slack.com/api/users.lookupByEmail"
        headers = {"Authorization": f"Bearer {self.slack_bot_token}"}
        response = requests.get(url, headers=headers, params={"email": email})
        
        if response.status_code == 200:
            data = response.json()
            # print(data['user']['name'])
        
            if data.get("ok"):
                user_email = data.get("profile", {}).get("email")
                print(f"mail is {user_email}")
                return data.get("user", {}).get("id")
            else:
                print(f"Error fetching Slack user ID: {data.get('error')}")
        else:
            print(f"Failed to fetch Slack user ID: {response.status_code}, {response.text}")
        return None
    
    

    def send_slack_dm(self, user_id, ticket_key, summary, description, jira_link):
        """Send a direct message to a Slack user."""
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
            if data.get("ok"):
                print(f"Slack DM sent to user {user_id} for ticket {ticket_key}")
            else:
                print(f"Error sending Slack DM: {data.get('error')}")
        else:
            print(f"Failed to send Slack DM: {response.status_code}, {response.text}")
