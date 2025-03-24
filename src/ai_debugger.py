import openai

def ai_debug_code(code_snippet):
    """Uses OpenAI API to debug the given code snippet."""
    prompt = f"Debug the following Python code and provide a corrected version:\n\n{code_snippet}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    sample_code = "print('Hello'  # Missing closing parenthesis"
    fixed_code = ai_debug_code(sample_code)
    print("Fixed Code:\n", fixed_code)