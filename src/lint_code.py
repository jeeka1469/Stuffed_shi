import subprocess

def lint_code(file_path):
    """Auto-fix linting issues using Black (for Python)."""
    try:
        subprocess.run(["black", file_path], check=True)
        return f"Linting and formatting applied to {file_path}."
    except Exception as e:
        return str(e)