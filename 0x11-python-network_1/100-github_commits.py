import requests
import sys

def list_commits(repo_name, owner_name):
    """
    Retrieves the 10 most recent commits for the given repository and owner, and prints them in the requested format.
    
    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The name of the repository owner.
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    headers = {"Accept": "application/vnd.github+json"}
    
    # Fetch the first page of commits
    response = requests.get(url, headers=headers)
    commits = response.json()
    
    # Print the 10 most recent commits
    for i, commit in enumerate(commits[:10]):
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
