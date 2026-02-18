import ollama

def generate_response(prompt: str):
    try:
        response = ollama.chat(
            model="gemma:2b",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]

    except Exception as e:
        return "AI engine not running. Please start Ollama."