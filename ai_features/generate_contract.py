import openai

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

# Optional if required by OpenRouter:
openai.api_type = "openrouter"

def generate_contract(contract_data):
    prompt = f"Generate an employment contract using this information:\n{contract_data}"
    response = openai.Completion.create(
        engine="gpt 3.5 Turbo",
        prompt=prompt,
        max_tokens=400
    )
    return response.choices[0].text.strip()
