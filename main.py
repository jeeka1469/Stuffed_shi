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

# 🔥 Set Page Config
st.set_page_config(page_title="No Idea What I'm Doing", layout="wide", initial_sidebar_state="expanded")

# 🎨 Custom Styling
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

# 🤡 App Title
st.title("Blip: The Ultimate Developer Roast Machine")

# 🔥 Sidebar UI
st.sidebar.markdown('<div class="sidebar-title">You Really Messed Up, Didn\'t You?</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-text">Pick your disaster:</div>', unsafe_allow_html=True)

options = {
    "Modify Your Broken Code": "Patch up your spaghetti mess.",
    "Add Another Useless File": "Because clutter is your thing.",
    "Delete Your Shame": "Erase a file like it never existed.",
    "Refactor Your 'Genius' Code": "Make it slightly less painful to read.",
    "Generate Docs Like a Pro": "Fake expertise with auto-generated documentation.",
    "Lint Your Abomination": "Fix your terrible formatting.",
    "Modify Multi-Language Code": "Because breaking one language wasn’t enough.",
    "Check Your Coding 'Style'": "See how far you are from decent coding.",
    "Analyze Your Dependency Addiction": "Spot the 500 libraries you don’t need.",
    "Commit Your Regrets": "Push your latest mess to GitHub.",
    "Create a PR and Pray": "Beg for approval on your nonsense.",
    "Check Git Chaos": "See how bad your repo situation is.",
    "Jump Between Nightmares": "Switch Git branches because why not?",
    "Start a Fresh Disaster": "Create a new branch for your sins.",
    "Delete a Branch and Forget": "Wipe away your git mistakes.",
    "Merge Your Misery": "Combine two branches and hope for the best.",
    "Undo Your Last Mistake": "Rewind and pretend nothing happened.",
    "View Your Past Failures": "See the cringe-worthy commits you've made.",
    "Sell Your Soul to GitHub": "Create a repo because why not?",
    "Clone and Claim": "Steal—uh, I mean, clone—a GitHub repo."
}

choice = st.sidebar.radio("", list(options.keys()), format_func=lambda x: f"{options[x]}")

# ⚠️ Repo Path Input
repo_path = st.sidebar.text_input("Enter your repo path:", value="C:/Users/srujan/Blip")

# 💥 Task Execution
st.markdown(f"### {choice}")

if choice == "Modify Your Broken Code":
    file_path = st.text_input("Enter the file path:")
    instructions = st.text_area("Enter modification instructions:")
    if st.button("Modify Code"):
        result = modify_file(file_path, instructions)
        st.success("Code modified successfully!") if result else st.error("Modification failed.")

elif choice == "Add Another Useless File":
    file_path = st.text_input("Enter the new file path:")
    content = st.text_area("Enter file content (optional):")
    if st.button("Add File"):
        result = add_file(file_path, content)
        st.success("File added successfully.") if result else st.error("File creation failed.")

elif choice == "Delete Your Shame":
    file_path = st.text_input("Enter the file path to delete:")
    if st.button("Delete File"):
        result = delete_file(file_path)
        st.warning("File deleted successfully!") if result else st.error("File not found.")

elif choice == "Refactor Your 'Genius' Code":
    file_path = st.text_input("Enter the file path to refactor:")
    if st.button("Refactor Code"):
        result = refactor_repo(file_path)
        st.success("Code refactored successfully!") if result else st.error("Refactoring failed.")

elif choice == "Generate Docs Like a Pro":
    file_path = st.text_input("Enter the file path:")
    if st.button("Generate Docs"):
        result = generate_docs(file_path)
        st.success("Docs generated successfully!") if result else st.error("Failed to generate docs.")

elif choice == "Commit Your Regrets":
    commit_message = st.text_input("Enter commit message:", value="🚀 Another questionable commit via Blip")
    if st.button("Commit Changes"):
        result = commit_changes(repo_path, commit_message)
        st.success(result) if result else st.error("Commit failed.")

elif choice == "Create a PR and Pray":
    pr_title = st.text_input("Enter PR title:", value="AI-Generated Fixes")
    pr_description = st.text_area("Enter PR description:", value="This PR includes AI-optimized code and fixes.")
    if st.button("Create Pull Request"):
        result = create_pull_request(repo_path, pr_title, pr_description)
        st.success(result) if result else st.error("Failed to create PR.")

elif choice == "Check Git Chaos":
    if st.button("Check Git Status"):
        result = check_git_status(repo_path)
        st.text(result)

elif choice == "Jump Between Nightmares":
    branch_name = st.text_input("Enter branch name to switch to:")
    if st.button("Switch Branch"):
        result = switch_branch(repo_path, branch_name)
        st.success(result) if result else st.error("Failed to switch branches.")

elif choice == "Sell Your Soul to GitHub":
    repo_name = st.text_input("Enter GitHub repo name:")
    description = st.text_area("Enter repo description:")
    if st.button("Create GitHub Repo"):
        result = create_github_repo(repo_name, description)
        st.success(result) if result else st.error("Repo creation failed.")
        
elif choice == "Clone and Claim":
    repo_url = st.text_input("Enter GitHub repo URL:")
    clone_path = st.text_input("Enter clone destination path:")
    if st.button("Clone Repository"):
        result = clone_repository(repo_url, clone_path)
        st.success(result) if result else st.error("Failed to clone repo.")

elif choice == "Start a Fresh Disaster":
    branch_name = st.text_input("Enter new branch name:")
    if st.button("Create Branch"):
        result = create_branch(repo_path, branch_name)
        st.success(result) if result else st.error("Failed to create branch.")
        
elif choice == "Delete a Branch and Forget":
    branch_name = st.text_input("Enter branch name to delete:")
    if st.button("Delete Branch"):
        result = delete_branch(repo_path, branch_name)
        st.success(result) if result else st.error("Failed to delete branch.")

elif choice == "Merge Your Misery":
    base_branch = st.text_input("Enter base branch name:")
    compare_branch = st.text_input("Enter branch to merge:")
    if st.button("Merge Branches"):
        result = merge_branches(repo_path, base_branch, compare_branch)
        st.success(result) if result else st.error("Failed to merge branches.")

elif choice == "Undo Your Last Mistake":
    if st.button("Undo Last Commit"):
        result = undo_last_commit(repo_path)
        st.success(result) if result else st.error("Failed to undo last commit.")

elif choice == "View Your Past Failures":
    st.text("Here are your past commits:")
    result = get_recent_commits(repo_path)
    st.text(result if result else "No commits found.")

elif choice == "Modify Multi-Language Code":
    file_path = st.text_input("Enter the file path:")
    instructions = st.text_area("Enter modification instructions:")
    if st.button("Modify Code"):
        result = modify_code_multilang(file_path, instructions)
        st.success("Code modified successfully!") if result else st.error("Modification failed.")

elif choice == "Check Your Coding 'Style'":
    code_style = detect_code_style(repo_path)
    st.text(f"Detected Code Style: {code_style}" if code_style else "Failed to detect code style.")

elif choice == "Analyze Your Dependency Addiction":
    result = analyze_dependencies(repo_path)
    st.text(result if result else "No dependencies found.")
    
elif choice == "Lint Your Abomination":
    if st.button("Lint Code"):
        result = lint_code(repo_path)
        st.success("Code linted successfully!") if result else st.error("Linting failed.")
        
elif choice == "Add Another Useless File":
    file_path = st.text_input("Enter the new file path:")
    content = st.text_area("Enter file content (optional):")
    if st.button("Add File"):
        result = add_file(file_path, content)
        st.success("File added successfully.") if result else st.error("File creation failed.")

elif choice == "Delete Your Shame":
    file_path = st.text_input("Enter the file path to delete:")
    if st.button("Delete File"):
        result = delete_file(file_path)
        st.warning("File deleted successfully!") if result else st.error("File not found.")

elif choice == "Refactor Your 'Genius' Code":
    st.text("Refactor option selected, but no action defined.")

st.sidebar.markdown("---")
st.sidebar.markdown("this shit is made by me aka Srujannnn")
