# Jira-Slack Integration

This project integrates Jira and Slack to notify Slack users about assigned Jira tickets. It fetches assigned tickets from Jira and sends direct messages to the corresponding Slack users.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Install the required Python packages:
    ```sh
    pip install requests
    ```

## Configuration

1. Update the [main.py](http://_vscodecontentref_/0) file with your Jira and Slack credentials:
    ```python
    jira_url = "https://your-jira-instance.atlassian.net/"
    jira_username = "your-jira-username"
    jira_api_token = "your-jira-api-token"
    project_key = "your-project-key"
    slack_bot_token = "your-slack-bot-token"
    ```

2. Alternatively, you can use environment variables to store your credentials. Uncomment the relevant lines in [main.py](http://_vscodecontentref_/1) and set the environment variables:
    ```python
    # Uncomment the following lines to load credentials from environment variables
    # jira_url = os.getenv("JIRA_URL")
    # jira_username = os.getenv("JIRA_USERNAME")
    # jira_api_token = os.getenv("JIRA_API_TOKEN")
    # project_key = os.getenv("PROJECT_KEY")
    # slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
    ```

## Usage

1. Run the [main.py](http://_vscodecontentref_/2) file to start the integration process:
    ```sh
    python main.py
    ```

2. The script will continuously fetch assigned tickets from Jira and notify the corresponding Slack users every 60 seconds.

## Project Structure

- [main.py](http://_vscodecontentref_/3): Entry point of the application. Initializes and starts the integration process.
- [jira_integration.py](http://_vscodecontentref_/4): Contains the [JiraIntegration](http://_vscodecontentref_/5) class to interact with the Jira API.
- [slack_integration.py](http://_vscodecontentref_/6): Contains the [SlackIntegration](http://_vscodecontentref_/7) class to interact with the Slack API.
- [jira_slack_integration.py](http://_vscodecontentref_/8): Contains the [JiraSlackIntegration](http://_vscodecontentref_/9) class to process Jira tickets and notify Slack users.

## Example Notification
-  