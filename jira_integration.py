import requests

class JiraIntegration:
    def __init__(self, jira_url, jira_username, jira_api_token, project_keys):
        self.jira_url = jira_url
        self.jira_username = jira_username
        self.jira_api_token = jira_api_token
        self.project_keys = project_keys

    def fetch_assigned_tickets(self):
        """
        Fetch assigned tickets from multiple Jira projects.
        
        :return: A list of assigned Jira tickets.
        """
        headers = {"Content-Type": "application/json"}
        auth = (self.jira_username, self.jira_api_token)

        all_issues = []
        for project_key in self.project_keys:
            jql_query = f"project={project_key} AND assignee IS NOT EMPTY"
            jira_issue_url = f"{self.jira_url}/rest/api/2/search?jql={jql_query}"
            # print(jira_issue_url)

            response = requests.get(jira_issue_url, auth=auth, headers=headers)
            # print(response.json())
            if response.status_code == 200:
                issues = response.json().get('issues', [])
                # print(issues)
                all_issues.extend(issues)
                # print(all_issues)
            else:
                print(f"Failed to fetch Jira tickets for {project_key}: {response.status_code}, {response.text}")
        
        return all_issues
