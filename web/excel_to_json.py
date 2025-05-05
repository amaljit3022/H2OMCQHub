import pandas as pd
import json

# Input Excel file (you can change this)
EXCEL_FILE = "web/mcq_upload.xlsx"
OUTPUT_FILE = "web/data/quiz_data.json"

# Load Excel
df = pd.read_excel(EXCEL_FILE)

# Convert to JSON structure
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
        "correctAnswerIndex": int(row["correctAnswer"]) - 1,  # Excel uses 1-based
        "marks": { "positive": 1, "negative": -0.25 },
        "explanation": str(row["explanation"]).strip()
    }
    quiz_list.append(quiz)

# Save to JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(quiz_list, f, indent=2, ensure_ascii=False)

print(f"✅ Converted {len(quiz_list)} questions to {OUTPUT_FILE}")
