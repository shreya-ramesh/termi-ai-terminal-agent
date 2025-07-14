import json
import os

SETTINGS_FILE = "settings.json"

default_settings = {
    "autorun": False
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def toggle_autorun(state: bool):
    settings = load_settings()
    settings["autorun"] = state
    save_settings(settings)
