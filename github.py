import requests

# Replace these with your GitHub username and personal access token
GITHUB_USERNAME = "srujan259"
TOKEN = "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"

def make_repo_private(repo_name):
    """Function to make a given repository private."""
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"private": True}

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Successfully made {repo_name} private.")
    else:
        print(f"Failed to make {repo_name} private: {response.status_code} - {response.text}")

def get_all_repos():
    """Function to retrieve all repositories for the authenticated user."""
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    params = {"visibility": "all", "affiliation": "owner"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        repos = [repo['name'] for repo in response.json()]
        print("Your repositories:")
        for repo in repos:
            print(f"- {repo}")
        return repos
    else:
        print(f"Failed to fetch repositories: {response.status_code} - {response.text}")
        return []
if __name__ == "__main__":
    repos = get_all_repos()
    if repos:
        for repo in repos:
            make_repo_private(repo)
    else:
        print("No repositories found or failed to fetch repositories.")
