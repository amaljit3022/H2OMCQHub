# 🚰 H2OMCQHub

**H2OMCQHub** is a free, open-source platform to practice MCQs on **Water Supply**, **Sanitation**, and **Rural Infrastructure**. Developed under *The Krittika Project*, it empowers learners, engineers, and students through:

- 📘 Verified quiz content based on official manuals and advisories  
- ⚡ Instant feedback with explanations  
- 🎓 Auto-generated certificates  
- 📱 Offline Android app and responsive web interface

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![GitHub Pages](https://img.shields.io/badge/hosted%20on-GitHub%20Pages-blue)

---

## 🎯 **Features**

- ✅ **25,000+ questions** (target) based on CPHEEO, Jal Shakti, and SBM guidelines  
- 📚 **Manual-wise and topic-wise quizzes**  
- ⭐ **Bookmark and star tracking system**  
- 💡 **Explanations for each question**  
- 🧾 **PDF certificate after quiz completion**  
- 📱 **Android App using Jetpack Compose**  
- 🌐 **Static web interface (GitHub Pages compatible)**  

---

## 🛠️ **Tech Stack**

| Layer     | Technology                |
|-----------|---------------------------|
| Frontend  | HTML, JavaScript *(vanilla or React optional)* |
| Mobile    | Kotlin + Jetpack Compose  |
| Data      | JSON (auto-generated)     |
| Tools     | Python (Excel to JSON GUI converter)  

---

## 🚀 **Getting Started**

```bash
git clone https://github.com/amaljit3022/H2OMCQHub.git
cd H2OMCQHub
```

### 🔑 Key Components:
- `/web/` → Web quiz interface (static)
- `/android/` → Android app (Jetpack Compose)
- `/tools/` → Excel-to-JSON converter (GUI & .exe)
- `/data/` → Stores quiz and manual data (`quiz_data.json`, `manuals.json`)

---

## 📂 **Folder Structure**

```
H2OMCQHub/
├── web/
│   ├── index.html
│   ├── quiz.html
│   ├── manuals.html
│   ├── about.html
│   ├── data/
│   │   ├── quiz_data.json
│   │   └── manuals.json
│   └── assets/
├── android/
├── tools/
│   ├── quiz_converter_gui.py
│   ├── dist/
│   │   └── KrittikaQuizGen.exe
├── README.md
└── LICENSE
```

---

## 🧪 **How to Use the Excel-to-JSON Tool**

### 1. Prepare your Excel file with these headers:

| id | manualCode | section | question | optionA | optionB | optionC | optionD | correctAnswer | explanation |
|----|------------|---------|----------|---------|---------|---------|---------|----------------|-------------|

### 2. Run:
- `quiz_converter_gui.py` (Python script)
- Or `KrittikaQuizGen.exe` (portable GUI)

### 3. Output:
- `/data/quiz_data.json`
- `/data/manuals.json`
- `upload_log.txt` + auto backups

---

## 🌐 **Hosting the Web App**

You can host the `/web/` folder using:
- [GitHub Pages](https://pages.github.com)
- Or any static hosting (Netlify, Firebase, Vercel, etc.)

> **GitHub Pages Setup:**  
> Go to **Repo → Settings → Pages** → Source: `main` + `/web` folder  
> Visit: `https://<your-username>.github.io/H2OMCQHub`

---

## 📫 **Contact & Support**

- 📧 Email: [thekrittikaproject@gmail.com](mailto:thekrittikaproject@gmail.com)
- 💬 WhatsApp: [+91 91012 06226](https://wa.me/919101206226)

---

## ⚖️ **License**

- 💻 Code: [MIT License](LICENSE)
- 📚 Question Data: Creative Commons Attribution-NonCommercial (CC BY-NC)

---

## 🧭 **The Krittika Project**

> Guided by her star, driven by purpose. 🌠  
> Explore: [**The Krittika Project**](https://sites.google.com/view/thekrittikaproject)

✍️ **Amaljit Bharali** — writing with purpose, building with vision  
☄️ **Krittika Guides Me | The Rover Builds | 2025**
