import openai
import os

def modify_file(file_path, instructions):
    """Modify the file based on AI-generated edits."""
    
    if not os.path.exists(file_path):
        return "Error: File not found."

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        prompt = f"""
        Modify the following code based on these instructions: {instructions}
        Respond with only the modified code. No explanations, comments, or extra notes.

        Code:
        {content}
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        modified_code = response["choices"][0]["message"]["content"].strip()

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_code)

        return True

    except Exception as e:
        return f"Error: {str(e)}"