import openai

def optimize_code(code_snippet):
    """AI-based optimization of inefficient code."""
    prompt = f"Optimize the following Python code for better performance:\n\n{code_snippet}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    sample_code = "for i in range(len(arr)):\n    print(arr[i])  # Inefficient loop"
    optimized_code = optimize_code(sample_code)
    print("Optimized Code:\n", optimized_code)