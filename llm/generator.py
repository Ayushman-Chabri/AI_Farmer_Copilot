from .ollama_client import generate_response
from .prompt_templates import build_prompt
from .response_formatter import format_response

def ask_ai(user_query: str):

    # build structured prompt
    prompt = build_prompt(user_query)

    # get raw AI response
    raw_response = generate_response(prompt)

    # format response
    final = format_response(raw_response)

    return final