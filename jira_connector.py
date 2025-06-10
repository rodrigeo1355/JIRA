import os
import requests
from typing import Dict, Any, List

class JiraConnector:
    """Simple connector for Jira REST API."""
    def __init__(self, base_url: str, username: str, api_token: str) -> None:
        self.base_url = base_url.rstrip('/')
        self.auth = (username, api_token)
        self.session = requests.Session()
        self.session.auth = self.auth
        self.session.headers.update({'Accept': 'application/json'})

    def search_issues(self, jql: str, max_results: int = 50) -> List[Dict[str, Any]]:
        """Search issues using JQL."""
        url = f"{self.base_url}/rest/api/2/search"
        params = {'jql': jql, 'maxResults': max_results}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('issues', [])

if __name__ == "__main__":
    base_url = os.environ.get('JIRA_BASE_URL')
    username = os.environ.get('JIRA_USERNAME')
    api_token = os.environ.get('JIRA_API_TOKEN')
    jql = os.environ.get('JIRA_JQL', 'project=TEST')
    if not all([base_url, username, api_token]):
        raise SystemExit("Please set JIRA_BASE_URL, JIRA_USERNAME, and JIRA_API_TOKEN environment variables")

    connector = JiraConnector(base_url, username, api_token)
    issues = connector.search_issues(jql)
    for issue in issues:
        key = issue.get('key')
        summary = issue.get('fields', {}).get('summary')
        print(f"{key}: {summary}")
