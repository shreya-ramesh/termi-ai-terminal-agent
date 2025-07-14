# core/explainer.py

import requests
from config.env import GROQ_API_KEY

def explain_command(user_prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = """
You are a command-line explainer assistant.
If the user asks to explain a Linux command, return a short, clear explanation.
Do not output actual commands, only explanations.
Do not add extra markdown or formatting.
Be concise and beginner-friendly.
"""

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    try:
        return result['choices'][0]['message']['content'].strip()
    except KeyError:
        return "[ERROR] Could not get explanation."
