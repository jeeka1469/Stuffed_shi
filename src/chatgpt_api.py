import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your API key in environment variables

def chatgpt_request(prompt):
    """Sends a request to OpenAI's API and returns the response."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are an AI code assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def summarize_code(file_path):
    """Reads a code file and summarizes its content using GPT-4."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        prompt = f"Summarize this code file in 3 sentences:\n\n{code}"
        summary = chatgpt_request(prompt)
        return summary

    except Exception as e:
        return f"Error reading {file_path}: {e}"