import requests

def create_github_repo():
    # Set up your personal access token and the base URL for the GitHub API
    personal_access_token = "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"
    api_base_url = "https://api.github.com"

    # Create a dictionary to store the data for your new repository
    data = {
        "name": "my-new-repo",
        "description": "This is my new repository",
        "private": False
    }

    # Send a POST request to the API endpoint to create a new repository
    response = requests.post(f"{api_base_url}/user/repos", json=data, headers={
        "Authorization": f"Bearer {personal_access_token}"
    })

    # Check the status code of the response
    if response.status_code == 201:
        print("Successfully created repository")
        # Extract the repository information from the response JSON
        repo_data = response.json()
        owner = repo_data["owner"]["login"]
        repo_name = repo_data["name"]

        # Set the file path and content for the file you want to add to the repository
        file_path = "bot1.py"
        file_content = "This is the content of the file"

        # Create a dictionary for creating a new file in the repository
        file_data = {
            "message": "Initial commit",
            "content": file_content
        }

        # Send a PUT request to create the file in the repository
        response = requests.put(f"{api_base_url}/repos/{owner}/{repo_name}/contents/{file_path}", json=file_data, headers={
            "Authorization": f"Bearer {personal_access_token}"
        })

        if response.status_code == 201:
            print(f"Successfully added {file_path} to the repository")
        else:
            print(f"Failed to add {file_path} to the repository")
    else:
        print("Failed to create repository")

if __name__ == "__main__":
    create_github_repo()

