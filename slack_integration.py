import requests

class SlackIntegration:
    def __init__(self, slack_bot_token):
        self.slack_bot_token = slack_bot_token
        # print(self.slack_bot_token)


    def get_slack_user_id(self, email):
        """
        Fetch Slack user ID using their email.
        
        :param email: The email address of the Slack user.
        :return: The Slack user ID if found, otherwise None.
        """
        url = "https://slack.com/api/users.lookupByEmail"
        headers = {
            "Authorization": f"Bearer {self.slack_bot_token}",
            "Content-Type": "application/json"
        }

        params = {"email": email}
       
        # print(email) --
        response = requests.get(url, headers=headers, params=params)
        # print(response.json())
        # print(response.headers)
        # print(f"Response Status Code: {response.status_code}")
        # print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            # print(data)
            if data.get('ok'):
                return data['user']['id']
            else:
                print(f"Error fetching Slack user ID: {data.get('error')}")
        else:
            print(f"Failed to fetch Slack user ID: {response.status_code}, {response.text}")
        return None

    def send_slack_dm(self, user_id, ticket_key, summary, description, jira_link):
        """Send a direct message to Slack user with ticket details."""
        url = f"https://slack.com/api/chat.postMessage"
        headers = {"Authorization": f"Bearer {self.slack_bot_token}"}
        message = f"Hey,<@{user_id}> you have been assign a new ticket !!\n Jira Ticket: {ticket_key}\nSummary: {summary}\nDescription: {description}\n{jira_link}"
        # print(message)
        data = {
            "channel": user_id,
            "text": message
        }
        # print(data)
        response = requests.post(url, headers=headers, data=data)
        if(response.status_code==200):
            data = response.json()
            if(data.get('ok')):
                print(f"Slack DM sent to user {user_id} for ticket {ticket_key}")
            else:
                print(f"Error sending Slack DM: {data.get('error')}")
        else:
            print(f"Failed to send message: {response.status_code}, {response.text}")
