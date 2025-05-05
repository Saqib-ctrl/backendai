import os
import openai

# Configure OpenRouter
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def generate_contract(contract_data):
    try:
        messages = [
            {
                "role": "user",
                "content": f"Generate a professional employment contract using the following details:\n{contract_data}"
            }
        ]

        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",  # or any model OpenRouter supports
            messages=messages,
            max_tokens=800
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error: {str(e)}"
