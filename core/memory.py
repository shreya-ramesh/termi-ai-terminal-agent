import json
from datetime import datetime

HISTORY_FILE = "db/history.json"

def save_history(prompt, command):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "command": command
    }

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def view_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def clear_history():
    with open(HISTORY_FILE, "w") as f:
        f.write("[]")

