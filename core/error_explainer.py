import requests
from config.env import GROQ_API_KEY

def explain_error(error_text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = """You are a Linux error explainer. 
Given a stderr or shell error message, explain what it means and how to fix it, clearly and simply."""

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Explain this error: {error_text}"}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    return result['choices'][0]['message']['content'].strip()
