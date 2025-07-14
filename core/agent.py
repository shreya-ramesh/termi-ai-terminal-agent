import requests
from config.env import GROQ_API_KEY

def generate_command(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",  
        "messages": [
            {"role": "system", "content": "You are Termi,a helpful terminal assistant. Respond with only the best shell command for the user's prompt. No explanation."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        

        if "choices" in result:
            return result['choices'][0]['message']['content'].strip()
        else:
            print("❌ Groq API returned no choices!")
            return "echo 'Error: Groq returned an invalid response.'"

    except Exception as e:
        print("❌ Exception occurred while calling Groq API:", str(e))
        return "echo 'Error: Could not connect to Groq API.'"
