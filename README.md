# AI Voice Bot  

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square\&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🚀 Project Overview

**AI Voice Bot** is an end-to-end voice assistant built using Streamlit. The bot records user speech, converts it into text using a speech-to-text model (Whisper or provider API), processes the text via an LLM or rule-based logic, and then responds back using text-to-speech. This provides a natural, conversational voice-based interface.

This README provides a full, production-style documentation similar to the reference RAG chatbot README you provided.

---

## ✨ Features

*  **Microphone Recording** (browser-based)
*  **Upload Audio Files** (WAV/MP3)
*  **Speech-to-Text** using Whisper or provider API
*  **LLM/Text Processing** using configurable logic (OpenAI/Gemini/local)
*  **Text-to-Speech Reply** (pyttsx3 / gTTS / provider TTS)
*  **Conversation History** within Streamlit
*  **Transcript View** for STT output
*  **Simple UI & Real-Time Interaction**

---

## 🛠️ Technologies Used

> Update this based on your actual imports in `app.py` and `requirements.txt`.

* **Python 3.11+**
* **Streamlit** — Web UI
* **Whisper / openai-whisper** — Speech-to-text
* **pyttsx3 / gTTS** — Text-to-speech
* **pydub** — Audio handling
* **numpy, pandas** — Utility & display
* **yaml** — Optional config
* **openai / google-generativeai** — Optional LLM backend
* **streamlit-webrtc / sounddevice** — Audio streaming (optional)

---

## 📁 Project Structure

```
AI_Voice_Bot/
├─ app.py                # Main Streamlit application
├─ requirements.txt      # Python dependencies
├─ LICENSE               # MIT License
├─ README.md             # This documentation
             
```

---

##  How It Works (Architecture Overview)

### 1️ **Audio Capture**

* User speaks through the microphone.
* The app stores audio temporarily.

###  **Speech-to-Text**

* Whisper or another STT provider transcribes the audio.
* The transcription is shown to the user and passed forward.

###  **Text Processing / LLM**

* The transcript is processed:

  * By a rule-based function, **or**
  * Sent to an LLM (OpenAI, Gemini, etc.) for response generation.

###  **Text-to-Speech Output**

* The response text is synthesized via TTS.
* Audio is played back directly in the Streamlit UI.

###  **Display & State Management**

* Streamlit Session State maintains:

  * Chat history
  * User transcripts
  * Generated audio responses

---

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dhrumil1128/AI_Voice_Bot.git
cd AI_Voice_Bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure your `requirements.txt` includes all libraries used in your `app.py`.

### 4. Set Environment Variables

Update based on what your code uses:

```bash
export OPENAI_API_KEY="your_api_key"
export GOOGLE_API_KEY="your_google_key"
```

Or create a `.env` or YAML file if your app reads it.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the browser at:
👉 `http://localhost:8501`

---

## ☁️ Deployment (Render / Streamlit Cloud)

### 1. Push Code to GitHub

Ensure:

* No API keys are pushed
* `requirements.txt` contains complete dependency list

### 2. Render Start Command

```
streamlit run app.py --server.port $PORT --server.enableCORS false
```

### 3. Add Environment Variables in Render Dashboard

* `OPENAI_API_KEY`
* `GOOGLE_API_KEY`
* any others your app requires

---

## 🔧 Configuration

Key configuration parameters you may expose inside `app.py`:

| Setting            | Description                                     |
| ------------------ | ----------------------------------------------- |
| `TRANSCRIBE_MODEL` | Whisper model selection (`base`, `small`, etc.) |
| `TTS_ENGINE`       | `gTTS`, `pyttsx3`, cloud TTS, etc.              |
| `LLM_MODEL`        | `gpt-4o`, `gemini-1.5-flash`, etc.              |
| `SAMPLE_RATE`      | Audio sample rate                               |
| `MAX_UPLOAD_MB`    | Limit audio file size                           |

---

## 🧪 Troubleshooting

* **Mic not working?**
  Enable browser microphone permission.

* **Whisper slow?**
  Use a smaller model or install GPU-enabled PyTorch.

* **TTS not speaking?**
  Ensure audio backend libraries are properly installed.

* **Streamlit reload loops?**
  Check Session State variables.

---

## 🤝 Contributing

Pull requests are welcome! You can contribute:

* New TTS/STT integrations
* Better UI/UX
* Multilingual support
* Noise reduction or audio enhancement

---

## 📄 License

Licensed under the **MIT License**. See the `LICENSE` file.

---

## 🔚 Final Notes

Replace any placeholders in this README with **your exact project details**, including:

* dependency versions
* environment variable names
* deployment URL

This README is fully structured for production-quality documentation and directly matches the style of the example you provided.
