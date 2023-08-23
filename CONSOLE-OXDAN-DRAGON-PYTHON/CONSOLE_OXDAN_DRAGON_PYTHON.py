import imports.own.start_start
import git
import requests
import shutil
import time
from winotify import Notification, audio

def get_latest_commit_hash(username, repo, branch):
    url = f"https://api.github.com/repos/{username}/{repo}/branches/{branch}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["commit"]["sha"]
    return None

def get_current_commit_hash(repo_path):
    repo = git.Repo(repo_path)
    return repo.head.commit.hexsha

def update_program(username, repo, branch, local_dir):
    try:
        remote_commit_hash = get_latest_commit_hash(username, repo, branch)
        local_commit_hash = get_current_commit_hash(local_dir)

        if remote_commit_hash and local_commit_hash and remote_commit_hash != local_commit_hash:
            #print("A new version is available.")
            message = Notification(app_id="OXDAN-DRAGON-PYTHON",
                                   title="New Update",
                                   msg="New update available. after login use('update', to update program to last version).",
                                   duration="short")
            
            message.show()
            #shutil.rmtree(local_dir)  # Remove the existing directory
            #git.Repo.clone_from(f"https://github.com/{username}/{repo}.git", local_dir)
            
            #print("Program updated successfully.")
        #else:
            #print("You have the latest version.")

    except Exception as e:
        print("Error:", e)
        
github_username = "Mester-Oxdan"
repository_name = "Oxdan-Dragon-Python"
target_branch = "main"  # Update this with the branch you want to update from
local_directory = "../CONSOLE-OXDAN-DRAGON-PYTHON"  # Update this with your local program directory
    
update_program(github_username, repository_name, target_branch, local_directory)


imports.own.start_start.start_start()
