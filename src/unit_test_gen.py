import openai

def generate_unit_test(function_code):
    """AI generates a unit test for the given function."""
    prompt = f"Write a Python unittest for the following function:\n\n{function_code}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    function_example = """def add_numbers(a, b): return a + b"""
    unit_test = generate_unit_test(function_example)
    print("Generated Unit Test:\n", unit_test)