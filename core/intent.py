from config.env import GROQ_API_KEY
import requests

def map_intent_to_command(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = """You're an intent mapper for a terminal assistant. Based on user input, respond ONLY with one of these internal commands:

/clearhistory
/history
/exit
/none

If user input doesn't match any, respond with /none. Do NOT explain. Only output the command."""

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.0
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    return result['choices'][0]['message']['content'].strip()
