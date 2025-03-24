import os
import openai

def modify_code_multilang(file_path, instructions):
    """Modify code for any programming language based on AI-generated edits."""

    if not os.path.exists(file_path):
        return "Error: File not found."

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    prompt = f"""
    Modify the given code according to the instructions:
    {instructions}
    
    Respond with only the modified code. No explanations, comments, or extra notes.

    Code:
    {content}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        modified_code = response["choices"][0]["message"]["content"]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_code)
        
        return "Code modified successfully!"
    
    except Exception as e:
        return f"Error: {str(e)}"