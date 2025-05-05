import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import shutil
import os
from datetime import datetime

# Dynamic base path: same as where script or .exe runs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
QUIZ_JSON = os.path.join(DATA_DIR, "quiz_data.json")
MANUALS_JSON = os.path.join(DATA_DIR, "manuals.json")
LOG_FILE = os.path.join(BASE_DIR, "upload_log.txt")

# Create /data if missing
os.makedirs(DATA_DIR, exist_ok=True)

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def backup(file_path):
    if os.path.exists(file_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_path = file_path.replace(".json", f"_backup_{timestamp}.json")
        shutil.copy(file_path, new_path)
        return new_path
    return None

def convert_excel(filepath):
    try:
        df = pd.read_excel(filepath)

        # Backup
        b1 = backup(QUIZ_JSON)
        b2 = backup(MANUALS_JSON)
        if b1: log(f"Backed up quiz_data.json → {b1}")
        if b2: log(f"Backed up manuals.json → {b2}")

        # Convert quiz_data.json
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

        # Convert manuals.json
        manuals = {}
        for q in quiz_list:
            code = q["manualCode"]
            if code not in manuals:
                manuals[code] = {
                    "code": code,
                    "title": f"Quiz on {code}",
                    "org": "TBD",
                    "year": "TBD",
                    "category": "General"
                }
        with open(MANUALS_JSON, "w", encoding="utf-8") as f:
            json.dump(list(manuals.values()), f, indent=2, ensure_ascii=False)
        log(f"✅ Created manuals.json with {len(manuals)} entries.")

        messagebox.showinfo("Success", "✅ Quiz & Manuals JSON created successfully!")
    except Exception as e:
        log(f"❌ Error: {e}")
        messagebox.showerror("Error", str(e))

def browse_file():
    path = filedialog.askopenfilename(
        filetypes=[("Excel Files", "*.xlsx *.xls")],
        title="Select your MCQ Excel file"
    )
    if path:
        convert_excel(path)

# GUI
root = tk.Tk()
root.title("🧠 Quiz JSON Generator - The Krittika Project")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="📘 Select your MCQ Excel file to convert", font=("Arial", 11)).pack(pady=20)
tk.Button(root, text="📂 Browse Excel File", command=browse_file, width=25, height=2).pack()
tk.Label(root, text="© The Krittika Project | ☄️ Krittika Guides Me | 2025", font=("Arial", 9), fg="gray").pack(side="bottom", pady=10)

root.mainloop()
