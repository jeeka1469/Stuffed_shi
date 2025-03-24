import os
import streamlit as st
from src.file_operations import add_file, delete_file
from src.modify_code import modify_file
from src.refactor_code import refactor_repo
from src.generate_docs import generate_docs
from src.lint_code import lint_code
from src.multi_language import modify_code_multilang
from src.code_style import detect_code_style
from src.dependency_analysis import analyze_dependencies
from src.git_automation import (
    commit_changes, create_pull_request, check_git_status, switch_branch,
    list_branches, create_branch, delete_branch, merge_branches,
    get_recent_commits, undo_last_commit, create_github_repo, clone_repository
)

# Set Page Config
st.set_page_config(page_title="No Idea What I'm Doing", layout="wide", initial_sidebar_state="expanded")

# Custom Styling
st.markdown("""
    <style>
        [data-testid="stSidebar"] { background-color: #121212 !important; color: white; padding: 20px; }
        .sidebar-title { font-size: 22px; font-weight: bold; color: #4A90E2; margin-bottom: 10px; }
        .sidebar-text { font-size: 16px; color: #bbbbbb; margin-bottom: 15px; padding-left: 5px; }
        .stButton>button { background-color: #2C2F33; color: white; border-radius: 8px; font-size: 16px; transition: 0.3s ease-in-out; }
        .stButton>button:hover { background-color: #40444B; transform: scale(1.05); }
        .stTextInput>div>div>input, .stTextArea>div>textarea { background-color: #222; color: white; border-radius: 6px; border: 1px solid #444; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("random shi")

# Sidebar UI
st.sidebar.markdown('<div class="sidebar-title">You Really Messed Up, Didn\'t You?</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-text">Pick your mistake:</div>', unsafe_allow_html=True)

options = {
    "You Should've Known Better": "Modify code like you have no clue what you're doing.",
    "Add Yet Another Pointless File": "Because the more files, the better, right?",
    "Delete This Nightmare": "Delete a file that you probably shouldn't have created in the first place.",
    "Refactor Your 'Masterpiece'": "Turn your coding failure into something slightly less embarrassing.",
    "Get AI to Pretend You Know What You're Doing": "Generate docs like you actually wrote meaningful code.",
    "Fix Your 'Beautiful' Formatting": "Lint your code after you destroyed it with random indents.",
    "Try Fixing This Multi-Language Mess": "Modify multi-language code because you can't even handle one.",
    "Pretend You Have Standards": "Check code style even though you're too lazy to follow one.",
    "Analyze Your Addiction to Dependencies": "Take a hard look at your project's bloated dependencies.",
    "Commit and Regret": "Push your latest spaghetti code to GitHub.",
    "Beg for a Merge": "Create a pull request and hope no one notices the mess.",
    "Check How Bad Things Are": "View your Git status and regret everything.",
    "Jump Between Disasters": "Switch Git branches, because why not?",
    "Create a Fresh Mess": "Start a new branch to ruin things separately.",
    "Destroy Your Evidence": "Delete a branch like it never happened.",
    "Merge the Mayhem": "Merge two branches and pray nothing explodes.",
    "Rewind Your Regrets": "Undo your last commit and pretend it never happened.",
    "Stalk Your Past Mistakes": "View your last few commits and cringe at your past self.",
    "Sell Your Soul to GitHub": "Create a new GitHub repo because why not?",
    "Steal Someone Else's Work": "Clone a GitHub repo and pretend it's yours."
}

choice = st.sidebar.radio("", list(options.keys()), format_func=lambda x: f"{options[x]}")

# Repo Path Input
repo_path = st.sidebar.text_input("Enter your repo path:", value="C:/Users/srujan/Blip")

# Task Execution
st.markdown(f"### {choice}")

if choice == "You Should've Known Better":
    file_path = st.text_input("Enter the file path:")
    instructions = st.text_area("Enter modification instructions:")
    if st.button("Modify Code"):
        result = modify_file(file_path, instructions)
        st.success("Code modified successfully!") if result else st.error("Modification failed.")

elif choice == "Add Yet Another Pointless File":
    file_path = st.text_input("Enter the new file path:")
    content = st.text_area("Enter file content (optional):")
    if st.button("Add File"):
        result = add_file(file_path, content)
        st.success("File added successfully.") if result else st.error("File creation failed.")

elif choice == "Delete This Nightmare":
    file_path = st.text_input("Enter the file path to delete:")
    if st.button("Delete File"):
        result = delete_file(file_path)
        st.warning("File deleted successfully!") if result else st.error("File not found.")

elif choice == "Refactor Your 'Masterpiece'":
    file_path = st.text_input("Enter the file path to refactor:")
    if st.button("Refactor Code"):
        result = refactor_repo(file_path)
        st.success("Code refactored successfully!") if result else st.error("Refactoring failed.")

elif choice == "Get AI to Pretend You Know What You're Doing":
    file_path = st.text_input("Enter the file path:")
    if st.button("Generate Docs"):
        result = generate_docs(file_path)
        st.success("Documentation generated successfully.") if result else st.error("Failed to generate docs.")

elif choice == "Commit and Regret":
    commit_message = st.text_input("Enter commit message:", value="🚀 Auto-commit via Blip")
    if st.button("Commit Changes"):
        result = commit_changes(repo_path, commit_message)
        st.success(result) if result else st.error("Commit failed.")

elif choice == "Beg for a Merge":
    pr_title = st.text_input("Enter PR title:", value="AI-Generated Fixes")
    pr_description = st.text_area("Enter PR description:", value="This PR includes AI-optimized code and fixes.")
    if st.button("Create Pull Request"):
        result = create_pull_request(repo_path, pr_title, pr_description)
        st.success(result) if result else st.error("Failed to create PR.")

elif choice == "Check How Bad Things Are":
    if st.button("Check Git Status"):
        result = check_git_status(repo_path)
        st.text(result)

elif choice == "Jump Between Disasters":
    branch_name = st.text_input("Enter branch name to switch to:")
    if st.button("Switch Branch"):
        result = switch_branch(repo_path, branch_name)
        st.success(result) if result else st.error("Failed to switch branches.")

elif choice == "Create a Fresh Mess":
    branch_name = st.text_input("Enter new branch name:")
    if st.button("Create Branch"):
        result = create_branch(repo_path, branch_name)
        st.success(result) if result else st.error("Branch creation failed.")

elif choice == "Destroy Your Evidence":
    branch_name = st.text_input("Enter branch name to delete:")
    if st.button("Delete Branch"):
        result = delete_branch(repo_path, branch_name)
        st.warning(result) if result else st.error("Branch deletion failed.")

elif choice == "Merge the Mayhem":
    source_branch = st.text_input("Enter source branch:")
    target_branch = st.text_input("Enter target branch:", value="main")
    if st.button("Merge Branches"):
        result = merge_branches(repo_path, source_branch, target_branch)
        st.success(result) if result else st.error("Merge failed.")

elif choice == "Sell Your Soul to GitHub":
    repo_name = st.text_input("Enter GitHub repo name:")
    description = st.text_area("Enter repo description:")
    if st.button("Create GitHub Repo"):
        result = create_github_repo(repo_name, description)
        st.success(result) if result else st.error("Repo creation failed.")

st.sidebar.markdown("---")
st.sidebar.markdown("This masterpiece was created by yours truly, Srujan. Don't blame me for your mistakes.")
