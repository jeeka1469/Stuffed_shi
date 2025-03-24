import os
import git
import subprocess
import requests
import json
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# GitHub API Token and Username (Use environment variables, because hardcoding is for amateurs)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

def check_git_status(repo_path):
    """Checks the Git status of the repository, because you probably forgot what you did."""
    try:
        repo = git.Repo(repo_path)
        status = repo.git.status()
        return f"📢 Git Status:\n{status}"
    except Exception as e:
        return f"❌ Error checking Git status: {e}. Maybe try using Git first?"

def list_branches(repo_path):
    """Lists all branches in the repository because you clearly forgot what you created."""
    try:
        repo = git.Repo(repo_path)
        return [branch.name for branch in repo.branches]
    except Exception as e:
        return f"❌ Error listing branches: {e}. Maybe check if your repo actually exists?"

def switch_branch(repo_path, branch_name):
    """Switches to the specified branch. Assuming you actually spelled it right."""
    try:
        repo = git.Repo(repo_path)
        repo.git.checkout(branch_name)
        return f"✅ Switched to branch: {branch_name}. Hope you know what you're doing!"
    except Exception as e:
        return f"❌ Error switching branch: {e}. Maybe try switching to a real branch?"

def create_branch(repo_path, new_branch_name):
    """Creates and switches to a new branch. Because one branch wasn’t chaotic enough."""
    try:
        repo = git.Repo(repo_path)
        if new_branch_name in list_branches(repo_path):
            return "❌ Branch already exists, genius!"
        repo.git.checkout("-b", new_branch_name)
        return f"✅ Created and switched to branch: {new_branch_name}. Good luck not messing it up!"
    except Exception as e:
        return f"❌ Error creating branch: {e}. Maybe don’t name it something stupid?"

def delete_branch(repo_path, branch_name):
    """Deletes a branch from the repository. Hope you didn’t need it."""
    try:
        repo = git.Repo(repo_path)
        if branch_name == "main":
            return "❌ You cannot delete the main branch, genius."
        repo.git.branch("-D", branch_name)
        return f"🗑️ Deleted branch: {branch_name}. Say goodbye!"
    except Exception as e:
        return f"❌ Error deleting branch: {e}. Maybe you weren’t meant to delete it?"

def merge_branches(repo_path, source_branch, target_branch="main"):
    """Merges a branch into the target branch. Let’s see if conflicts ruin your day."""
    try:
        repo = git.Repo(repo_path)
        repo.git.checkout(target_branch)
        repo.git.merge(source_branch)
        return f"✅ Merged `{source_branch}` into `{target_branch}`. Hopefully, nothing broke!"
    except Exception as e:
        return f"❌ Error merging branches: {e}. Maybe next time, test before merging?"

def get_recent_commits(repo_path, count=5):
    """Fetches recent commits because you obviously forgot what you did."""
    try:
        repo = git.Repo(repo_path)
        commits = list(repo.iter_commits("main", max_count=count))
        return [f"{commit.message} - {commit.author}" for commit in commits]
    except Exception as e:
        return f"❌ Error fetching commits: {e}. Maybe actually commit something first?"

def undo_last_commit(repo_path):
    """Undo the last commit because regret is a powerful emotion."""
    try:
        repo = git.Repo(repo_path)
        repo.git.reset("HEAD~1")
        return "❌ Last commit undone. Hope you know what you’re doing!"
    except Exception as e:
        return f"❌ Error undoing last commit: {e}. Maybe don’t panic next time?"

def commit_changes(repo_path, commit_message="🚀 Auto-commit via Blip"):
    """Commits changes because you're too lazy to type 'git commit' manually."""
    try:
        repo = git.Repo(repo_path)

        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)
            repo.index.commit(commit_message)
            return "✅ Changes committed! Hope it’s not full of bugs."
        else:
            return "⚠️ No changes detected. Maybe actually do some work?"
    except Exception as e:
        return f"❌ Error committing changes: {e}. Maybe try writing code first?"

def commit_and_push(repo_path, commit_message="🚀 Auto-commit via Blip"):
    """Commits and pushes changes because apparently, you don’t trust your own memory."""
    try:
        repo = git.Repo(repo_path)

        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)
            repo.index.commit(commit_message)
            repo.remote().push()
            return "✅ Changes committed and pushed. Let’s hope you didn’t break production!"
        else:
            return "⚠️ No changes detected. Maybe do something before committing?"
    except Exception as e:
        return f"❌ Error committing changes: {e}. Git is judging you right now."

def create_github_repo(repo_name, description, private=False):
    """Creates a new GitHub repository because clearly, one wasn’t enough."""
    if not GITHUB_TOKEN or not GITHUB_USERNAME:
        return "❌ GitHub credentials are missing. Set GITHUB_TOKEN & GITHUB_USERNAME, Einstein."

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "name": repo_name,
        "description": description,
        "private": private
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 201:
            return f"✅ Repository `{repo_name}` created successfully! 🚀 Now don’t abandon it."
        else:
            return f"❌ Failed to create repo: {response.json()}. Maybe you hit GitHub’s rate limit?"
    except Exception as e:
        return f"❌ Error creating GitHub repo: {e}. Maybe actually read the error message?"

def create_pull_request(repo_path, pr_title="AI-Generated Fixes", pr_description="This PR includes AI-optimized code and fixes."):
    """Creates an automated pull request because manual PRs are beneath you."""
    try:
        repo = git.Repo(repo_path)
        origin = repo.remote(name="origin")
        branch = repo.active_branch.name

        if subprocess.run(["gh", "--version"], capture_output=True, text=True).returncode != 0:
            return "❌ GitHub CLI (gh) is not installed. Install it from https://cli.github.com/ and try again."

        process = subprocess.run(
            ["gh", "pr", "create", "--title", pr_title, "--body", pr_description, "--base", "main", "--head", branch],
            capture_output=True, text=True
        )

        if process.returncode == 0:
            return f"✅ Pull request created successfully!\n{process.stdout.strip()}"
        else:
            return f"❌ Failed to create pull request: {process.stderr.strip()}. Maybe check your GitHub settings?"

    except Exception as e:
        return f"❌ Error creating pull request: {e}. Maybe Google it?"

def clone_repository(repo_url, clone_path):
    """Clones a GitHub repository because you love hoarding code."""
    try:
        if os.path.exists(clone_path):
            return "⚠️ Destination folder already exists. Maybe don’t overwrite your own work?"

        git.Repo.clone_from(repo_url, clone_path)
        return f"✅ Repository cloned successfully to {clone_path}. Time to make a mess!"
    except Exception as e:
        return f"❌ Error cloning repository: {e}. Maybe check the URL?"

if __name__ == "__main__":
    repo_path = "C:/Users/srujan/Blip"

    print(check_git_status(repo_path))
    print(commit_and_push(repo_path, "🔧 Auto-commit via Blip"))
    print(create_pull_request(repo_path, "Blip's AI-Generated Code Improvements", "This PR includes refactored and AI-enhanced code."))
