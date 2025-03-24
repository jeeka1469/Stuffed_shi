import openai

def generate_docs(file_path):
    """Generate docstrings and README."""
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    prompt = f"Generate proper docstrings and a README for the following code:\n{code}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    docs = response["choices"][0]["message"]["content"]

    with open(file_path.replace(".py", "_docs.md"), 'w', encoding='utf-8') as f:
        f.write(docs)

    return "Documentation generated!"