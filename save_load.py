import json
import os

SAVE_FILE = "save_data.json"

def load_game_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as f:
            return json.load(f)
    return None

def save_game_progress(progress_data):
    with open(SAVE_FILE, 'w') as f:
        json.dump(progress_data, f)
