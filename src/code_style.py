import re

def detect_code_style(file_path):
    """Analyze code style (indentation, naming conventions)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    indent_style = "tabs" if "\t" in content else "spaces"
    snake_case = bool(re.search(r"_[a-z]", content))
    camelCase = bool(re.search(r"[a-z][A-Z]", content))

    return {
        "indentation": indent_style,
        "naming_convention": "snake_case" if snake_case else "camelCase" if camelCase else "unknown"
    }