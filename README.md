# 👨‍🌾 Agro-Sahayak: GenAI Chatbot for Farmers

Agro-Sahayak is an **intelligent Generative AI chatbot** built using **Flask** and **Gemini API** (Google Generative AI) that helps Indian farmers by answering agricultural queries in both **Hindi and English**.

It aims to bridge the knowledge gap in farming by providing expert advice on crop selection, soil health, pest control, weather awareness, and government schemes — all in the farmer’s preferred language.

---

## 🚀 Features

- ✅ **Bilingual** support (English & Hindi)
- ✅ **Context-aware** responses using Gemini AI
- ✅ Covers key topics: soil, pests, fertilizer, crop planning, and more
- ✅ **User-friendly web UI** built with Flask
- ✅ Ready for integration with AgroTech projects

---

## 📸 User Interface

### 💬 Chat Interface:

> Type in English or Hindi and get an intelligent response tailored to your input.

![Image 1](User%20Interface/Image%201.png)  
![Image 2](User%20Interface/Image%202.png)

---

## 🛠️ Tech Stack

- 🐍 **Python (Flask)**
- 🤖 **Google Generative AI (Gemini)**
- 🌐 **HTML/CSS** frontend (mobile responsive)
- 🔑 API integration via `google-generativeai` package

---

## 🧑‍💻 Installation Guide

```bash
# ✅ Step-by-Step Setup for Agro-Sahayak Chatbot

# 1️⃣ Clone the repository
git clone https://github.com/CodesbyHim/Agro-Sahayak-Chatbot-Project.git
cd Agro-Sahayak-Chatbot-Project

# 2️⃣ Create and activate virtual environment
python -m venv .chatvenv
# Activate on Windows
.chatvenv\Scripts\activate
# Activate on macOS/Linux
# source .chatvenv/bin/activate

# 3️⃣ Install required dependencies
pip install -r requirements.txt

# 4️⃣ Set your Gemini API key
# Edit the file 'config.py' and paste your API key like this:
# GEMINI_API_KEY = "your_actual_api_key_here"

# 5️⃣ Run the Flask app
python app.py

# Visit http://localhost:5000 in your browser 🚀
