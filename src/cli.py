import openai
import os
import argparse
import chardet  # Detects file encoding

# Load API key (Ensure you set OPENAI_API_KEY in your environment variables)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def detect_encoding(file_path):
    """Detects the encoding of a file to avoid decoding errors."""
    with open(file_path, "rb") as f:
        raw_data = f.read()
        return chardet.detect(raw_data)["encoding"]


def get_language_prompt(file_path):
    """Determines AI's behavior based on file extension."""
    ext = os.path.splitext(file_path)[1]
    language_prompts = {
        ".py": "You are an AI that edits Python code. Use PEP8 conventions.",
        ".js": "You are an AI that edits JavaScript code. Use modern ES6+ syntax.",
        ".ts": "You are an AI that edits TypeScript code. Ensure type safety.",
        ".cpp": "You are an AI that edits C++ code. Use best practices for efficiency.",
        ".c": "You are an AI that edits C code. Follow standard conventions.",
        ".java": "You are an AI that edits Java code. Use OOP principles and best practices.",
        ".html": "You are an AI that edits HTML code. Keep it semantic and accessible.",
        ".css": "You are an AI that edits CSS code. Optimize for performance and readability.",
        ".json": "You are an AI that edits JSON files. Ensure valid formatting and structure.",
        ".md": "You are an AI that edits Markdown files. Keep formatting clean and concise.",
    }
    return language_prompts.get(ext, "You are an AI that edits code files.")


def modify_file(file_path, instructions):
    """Modifies a file based on user instructions using ChatGPT API."""
    try:
        encoding = detect_encoding(file_path)
        with open(file_path, "r", encoding=encoding) as f:
            content = f.read()

        language_prompt = get_language_prompt(file_path)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"{language_prompt} Return ONLY the modified code."},
                {"role": "user", "content": f"Modify this file based on these instructions:\n\n### Code:\n{content}\n\n### Instructions:\n{instructions}"},
            ],
        )

        modified_content = response["choices"][0]["message"]["content"]

        with open(file_path, "w", encoding=encoding) as f:
            f.write(modified_content)

        print(f"✅ Successfully modified {file_path}!")

    except Exception as e:
        print(f"❌ Error modifying {file_path}: {e}")


def add_file(file_path, description):
    """Creates a new file with AI-generated content based on description."""
    try:
        language_prompt = get_language_prompt(file_path)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"{language_prompt} Return ONLY the file content."},
                {"role": "user", "content": f"Create a new file with the following description:\n{description}"},
            ],
        )

        file_content = response["choices"][0]["message"]["content"]

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        print(f"✅ File created: {file_path}")

    except Exception as e:
        print(f"❌ Error creating {file_path}: {e}")


def delete_file(file_path):
    """Deletes a specified file."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"✅ Deleted {file_path}")
        else:
            print(f"❌ File {file_path} does not exist.")
    except Exception as e:
        print(f"❌ Error deleting {file_path}: {e}")


def refactor_repo(directory):
    """Refactors an entire repo by optimizing variable names and removing redundancy."""
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith((".py", ".js", ".cpp", ".java", ".ts")):
                    file_path = os.path.join(root, file)
                    modify_file(
                        file_path, "Refactor this code: improve variable names, remove redundancy, and optimize performance."
                    )

        print(f"✅ Repo refactored: {directory}")

    except Exception as e:
        print(f"❌ Error refactoring {directory}: {e}")


def generate_docs(directory):
    """Generates missing docstrings, comments, and README."""
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith((".py", ".js", ".cpp", ".java", ".ts")):
                    file_path = os.path.join(root, file)
                    modify_file(file_path, "Add missing docstrings and improve comments.")

        readme_path = os.path.join(directory, "README.md")
        add_file(readme_path, "Generate a README for this project.")

        print(f"✅ Documentation updated in {directory}")

    except Exception as e:
        print(f"❌ Error generating docs: {e}")


def lint_code(directory):
    """Auto-fixes coding style issues (PEP8 for Python, ESLint for JS, etc.)."""
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith((".py", ".js", ".ts", ".cpp", ".java")):
                    file_path = os.path.join(root, file)
                    modify_file(file_path, "Fix coding style issues, remove unused imports, and clean up code.")

        print(f"✅ Code linted in {directory}")

    except Exception as e:
        print(f"❌ Error linting {directory}: {e}")


def summarize_file(file_path):
    """Summarizes the content of a file."""
    try:
        encoding = detect_encoding(file_path)

        with open(file_path, "r", encoding=encoding) as f:
            content = f.read()

        language_prompt = get_language_prompt(file_path)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"{language_prompt} You summarize code files."},
                {"role": "user", "content": f"Summarize this file in a few sentences:\n\n### Code:\n{content}"},
            ],
        )

        summary = response["choices"][0]["message"]["content"]
        print(f"\n📜 Summary of {file_path}:\n{summary}\n")

    except Exception as e:
        print(f"❌ Error summarizing {file_path}: {e}")


def find_relevant_files(directory, feature_request):
    """Finds files related to the given feature request."""
    relevant_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                encoding = detect_encoding(file_path)
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    if feature_request.lower() in content.lower():  # Simple keyword match
                        relevant_files.append(file_path)
            except Exception:
                continue  # Skip non-readable files

    return relevant_files


def modify_project(directory, feature_request):
    """Modifies the project by finding and updating relevant files."""
    relevant_files = find_relevant_files(directory, feature_request)

    if not relevant_files:
        print(f"❌ No relevant files found for '{feature_request}'. Try refining your request.")
        return

    for file_path in relevant_files:
        modify_file(file_path, f"Modify this file to implement: {feature_request}")

    print(f"✅ Successfully updated project for '{feature_request}'.")


# CLI Setup
parser = argparse.ArgumentParser(description="AI-Powered Repo Modifier")
parser.add_argument("command", choices=["modify", "add", "delete", "refactor", "docs", "lint", "summarize", "update"],
                    help="Action to perform")
parser.add_argument("file_path", help="Path to file or directory")
parser.add_argument("instructions", nargs="?", help="Instructions for modification (only for 'modify', 'add', or 'update')",
                    default="")

args = parser.parse_args()

if args.command == "modify":
    modify_file(args.file_path, args.instructions)
elif args.command == "add":
    add_file(args.file_path, args.instructions)
elif args.command == "delete":
    delete_file(args.file_path)
elif args.command == "refactor":
    refactor_repo(args.file_path)
elif args.command == "docs":
    generate_docs(args.file_path)
elif args.command == "lint":
    lint_code(args.file_path)
elif args.command == "summarize":
    summarize_file(args.file_path)
elif args.command == "update":
    modify_project(args.file_path, args.instructions)