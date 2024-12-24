import requests

class JiraIntegration:
    def __init__(self, jira_url, jira_username, jira_api_token, project_key):
        self.jira_url = jira_url
        self.jira_username = jira_username
        self.jira_api_token = jira_api_token
        self.project_key = project_key

    def fetch_assigned_tickets(self):
        """Fetch assigned tickets from Jira."""
        auth = (self.jira_username, self.jira_api_token)
        headers = {"Content-Type": "application/json"}
        jql_query = f"project={self.project_key} AND assignee IS NOT EMPTY"
        jira_issue_url = f"{self.jira_url}/rest/api/2/search?jql={jql_query}"

        response = requests.get(jira_issue_url, auth=auth, headers=headers)
        if response.status_code == 200:
            return response.json().get('issues', [])
        else:
            print(f"Failed to fetch Jira tickets: {response.status_code}, {response.text}")
            return []
