import os
from chatgpt_api import chatgpt_request

def edit_file(file_path, instruction):
    """Modifies a file based on a natural language instruction."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        prompt = f"Modify the following file based on this instruction: '{instruction}'\n\n{content}"
        new_content = chatgpt_request(prompt)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"✅ Updated {file_path}")

    except Exception as e:
        print(f"❌ Error modifying {file_path}: {e}")

def add_file(file_path, content=""):
    """Creates a new file with optional content."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created {file_path}")
    except Exception as e:
        print(f"❌ Error creating file: {e}")

def delete_file(file_path):
    """Deletes a file."""
    try:
        os.remove(file_path)
        print(f"🗑️ Deleted {file_path}")
    except Exception as e:
        print(f"❌ Error deleting {file_path}: {e}")
