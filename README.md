# 🎙️ AI Voice Bot (Google Gemini Powered)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square\&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-black?style=flat-square\&logo=flask)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-1.5_Flash-orange?style=flat-square\&logo=google)
![Speech Recognition](https://img.shields.io/badge/Speech_Recognition-Enabled-brightgreen?style=flat-square)
![TTS](https://img.shields.io/badge/Text_to_Speech-Enabled-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🚀 Project Overview

**AI Voice Persona Agent Bot** is an interactive, voice-driven AI agent built using **Flask** and powered by **Google Gemini**. Unlike a standard chatbot, this bot is designed to behave as a *persona-aware AI agent*—capable of responding to personal, reflective, or interview-style questions in a natural, human-like conversational tone.

The goal of the project is to create a universally accessible **voice-first AI agent** that can:

* Listen to a user’s voice input
* Understand and interpret the question (STT → Gemini)
* Generate a thoughtful, curated persona-based answer
* Speak the response back in natural audio (TTS)

This is ideal for hiring tests, personality assessments, product demos, and interactive AI experiences.

---

## ✨ Features

**AI Voice Bot** is an interactive voice-based chatbot built using **Flask** and powered by **Google Gemini (1.5 Flash)**. Users can speak directly into the browser, and the bot will:

1. Convert voice → text using `SpeechRecognition`
2. Generate natural conversational responses using **Gemini LLM**
3. Convert text → voice using Text-to-Speech (TTS)

This project is designed for **non-technical users**, recruiters, and hiring teams to easily test an AI voice assistant directly from a simple, clean web interface.

The bot is specifically optimized to answer prompts like:

* "What should we know about your life story in a few sentences?"
* "What’s your #1 superpower?"
* "What are the top 3 areas you’d like to grow in?"
* "What misconception do your coworkers have about you?"
* "How do you push your boundaries and limits?"

---

## ✨ Features

✔️ **Browser-based voice recording** (no installation required)
✔️ **Speech-to-Text (STT)** transcription using Python's `speech_recognition`
✔️ **Gemini LLM responses** using `google-generativeai`
✔️ **Text-to-Speech audio playback** generated on the server
✔️ **Simple Flask backend**
✔️ **Lightweight, mobile-friendly UI**
✔️ **Ready for deployment on Render / Railway / Heroku**
✔️ **No API key required for end users** (only stored on backend)

---

## 🛠️ Technologies Used

### **Backend**

* **Python 3.10+**
* **Flask** – lightweight backend server
* **SpeechRecognition** – STT
* **Pydub** – audio processing
* **Google Generative AI (Gemini API)** – LLM responses
* **gTTS / pyttsx3 / any TTS engine** – Text-to-Speech

### **Frontend**

* **Streamlit** – used as the main UI framework (not plain HTML/JS)
* Built‑in audio recorder component
* Clean, user‑friendly interface for non‑technical users

### **Additional Tools****

* `dotenv` for environment variable handling
* `requests` for API communication

---

## ⚙️ Architecture & How It Works

### **1️⃣ User Speaks**\

The browser records the user’s voice using **MediaRecorder API**.

### **2️⃣ Audio → Backend**\

Audio blob is sent to Flask backend via `/process_audio` endpoint.

### **3️⃣ Speech-to-Text (STT)**\

Python's `SpeechRecognition` converts audio → text.

### **4️⃣ LLM Response Generation**\

The transcribed text is sent to **Gemini (1.5 Flash)** via:

```python
from google.generativeai import GenerativeModel
model = GenerativeModel("gemini-1.5-flash")
```

### **5️⃣ Text-to-Speech (TTS)**\

Bot’s response is converted to audio (mp3/wav).

### **6️⃣ Audio → Browser**\

Frontend plays the final response.

---

## 🖥️ Demo

This project is ready for deployment to **Render / Railway / Heroku**.

📌 **Live Demo URL (replace after deployment):**
👉 [https://your-voicebot-demo-url.com](https://your-voicebot-demo-url.com)

---

## 💻 Local Setup & Installation

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dhrumil1128/AI_Voice_Bot.git
cd AI_Voice_Bot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your Gemini API Key

Create a `.env` file in the root folder:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

**Never upload `.env` to GitHub**.

### 5️⃣ Run Flask App

```bash
python app.py
```

Open in browser:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ☁️ Deployment (Render Recommended)

### 1️⃣ Push your code to GitHub

Make sure the structure looks like:

```
📁 AI_Voice_Bot
 ├── app.py
 ├── templates/
 ├── static/
 ├── requirements.txt
 ├── .env (NOT committed)
 ├── README.md
```

### 2️⃣ Add a `Procfile` (important)

```
web: python app.py
```

### 3️⃣ On Render:

* Create → Web Service
* Connect repo
* Add environment variable:

```
GOOGLE_API_KEY = your_api_key_here
```

* Deploy

### 4️⃣ Share your public URL 🎉

---

## 🧪 Sample Questions to Test the Bot

Use these when testing your voice bot:

* "Tell me your life story in a few sentences."
* "What’s your biggest strength?"
* "What misconceptions do people have about you?"
* "How do you push your limits?"

The bot will answer in the **same tone and style as ChatGPT**.

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve UI, TTS, or model prompting, feel free to contribute.

---

## 📄 License

This project is licensed under the **MIT License**.

---
