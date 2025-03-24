import os

def add_file(file_path, content=""):
    """Create a new file with the given content."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"File '{file_path}' created successfully."

def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"File '{file_path}' deleted."
    return "File not found."