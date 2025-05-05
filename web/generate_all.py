import pandas as pd
import json
import os
import shutil
from datetime import datetime

# Base folder
SCRIPT_DIR = os.path.dirname(__file__)
INPUT_EXCEL = os.path.join(SCRIPT_DIR, "mcq_upload.xlsx")
QUIZ_JSON = os.path.join(SCRIPT_DIR, "data", "quiz_data.json")
MANUALS_JSON = os.path.join(SCRIPT_DIR, "data", "manuals.json")
LOG_FILE = os.path.join(SCRIPT_DIR, "upload_log.txt")

def backup_file(file_path):
    if os.path.exists(file_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.replace(".json", f"_backup_{timestamp}.json")
        shutil.copy(file_path, backup_path)
        return backup_path
    return None

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

log("=== Running generate_all.py ===")

# Step 1: Backup old files
quiz_backup = backup_file(QUIZ_JSON)
manuals_backup = backup_file(MANUALS_JSON)

if quiz_backup:
    log(f"🔄 quiz_data.json backed up to {quiz_backup}")
if manuals_backup:
    log(f"🔄 manuals.json backed up to {manuals_backup}")

# Step 2: Convert Excel to quiz_data.json
try:
    df = pd.read_excel(INPUT_EXCEL)
    quiz_list = []

    for _, row in df.iterrows():
        quiz = {
            "id": int(row["id"]),
            "manualCode": str(row["manualCode"]).strip(),
            "section": str(row["section"]).strip(),
            "question": str(row["question"]).strip(),
            "options": [
                str(row["optionA"]).strip(),
                str(row["optionB"]).strip(),
                str(row["optionC"]).strip(),
                str(row["optionD"]).strip()
            ],
            "correctAnswerIndex": int(row["correctAnswer"]) - 1,
            "marks": {"positive": 1, "negative": -0.25},
            "explanation": str(row["explanation"]).strip()
        }
        quiz_list.append(quiz)

    with open(QUIZ_JSON, "w", encoding="utf-8") as f:
        json.dump(quiz_list, f, indent=2, ensure_ascii=False)

    log(f"✅ Created quiz_data.json with {len(quiz_list)} questions.")
    print(f"✅ quiz_data.json generated")
except Exception as e:
    log(f"❌ Error generating quiz_data.json: {e}")
    print("❌ Error in Step 1:", e)

# Step 3: Generate manuals.json
try:
    manual_set = {}
    for q in quiz_list:
        code = q["manualCode"]
        if code not in manual_set:
            manual_set[code] = {
                "code": code,
                "title": f"Quiz on {code}",
                "org": "TBD",
                "year": "TBD",
                "category": "General"
            }

    manuals_list = list(manual_set.values())
    with open(MANUALS_JSON, "w", encoding="utf-8") as f:
        json.dump(manuals_list, f, indent=2, ensure_ascii=False)

    log(f"✅ Created manuals.json with {len(manuals_list)} entries.")
    print(f"✅ manuals.json generated")
except Exception as e:
    log(f"❌ Error generating manuals.json: {e}")
    print("❌ Error in Step 2:", e)

log("=== Script complete ===\n")
print("✅ All tasks completed. Check upload_log.txt for details.")
# This script generates quiz_data.json and manuals.json from an Excel file.