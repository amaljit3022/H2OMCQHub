import json
import os

# Paths
SCRIPT_DIR = os.path.dirname(__file__)
QUIZ_FILE = os.path.join(SCRIPT_DIR, "data", "quiz_data.json")
MANUALS_FILE = os.path.join(SCRIPT_DIR, "data", "manuals.json")

# Load quiz data
with open(QUIZ_FILE, "r", encoding="utf-8") as f:
    quiz_data = json.load(f)

# Build unique manualCode entries
manual_set = {}
for q in quiz_data:
    code = q["manualCode"]
    if code not in manual_set:
        manual_set[code] = {
            "code": code,
            "title": f"Quiz on {code}",     # Placeholder title
            "org": "TBD",                   # You can manually fill later
            "year": "TBD",
            "category": "General"
        }

# Write manuals.json
manuals_list = list(manual_set.values())
with open(MANUALS_FILE, "w", encoding="utf-8") as f:
    json.dump(manuals_list, f, indent=2, ensure_ascii=False)

print(f"✅ Generated {len(manuals_list)} manuals to {MANUALS_FILE}")
