import openai

def refactor_repo(file_path):
    """Refactor the code: optimize functions, rename variables."""
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    prompt = f"""
    Refactor this code for better readability and efficiency.
    - Rename unclear variable names to meaningful names.
    - Optimize functions.
    - Remove redundancies.

    Code:
    {code}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    refactored_code = response["choices"][0]["message"]["content"]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(refactored_code)

    return "Code refactored successfully!"