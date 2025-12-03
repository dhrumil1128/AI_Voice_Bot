# 🎤 AI Voice Assistant Bot (Gemini Powered)

## 🚀 Project Overview

This project implements an interactive AI Voice Assistant that allows users to communicate with the latest Large Language Models (LLMs) using natural voice commands. It is designed to capture spoken input, process it using the powerful Google Gemini API, and provide informative, real-time responses.

The application leverages a Speech-to-Text (STT) engine to convert voice input into text and then sends this query to the Gemini model for generation, creating a hands-free, conversational interface.

## ✨ Features

* **Voice Command Interface:** Allows users to interact with the AI purely through spoken words.
* **Google Gemini Integration:** Utilizes `gemini-1.5-flash` for high-quality, fast, and relevant text generation.
* **Real-time Speech Recognition:** Converts live audio streams into text input for the LLM.
* **Conversational Memory:** Maintains a continuous chat history, allowing the AI to recall previous turns and maintain context.
* **Intuitive UI:** Built with Streamlit for a simple, engaging, and modern web interface.
* **Easy Configuration:** Uses a secure method to load the Google API key via environment variables.

## 🛠️ Technologies Used

* **Python 3.10+** – The core programming language.
* **Streamlit** – For building the web interface.
* **Google GenAI SDK (`google-genai`)** – For connecting to the Gemini API.
* **SpeechRecognition** – For handling microphone input and speech recognition.
* **PyAudio** – Required for capturing live audio.

## ⚙️ Architecture & How It Works

1. **Voice Input:** The user clicks a button or triggers a voice activation command.
2. **Speech-to-Text (STT):** SpeechRecognition captures audio and converts it to text.
3. **LLM Processing:** The text is sent to the Gemini model via the Google GenAI SDK.
4. **Response Generation:** Gemini produces a relevant, contextual text response.
5. **Display:** The response shows in the Streamlit chat interface.

## 💻 Local Setup & Installation

Follow these steps to get the AI Voice Bot running locally.

### 1. Clone the Repository

```bash
git clone https://github.com/dhrumil1128/AI_Voice_Bot.git
cd AI_Voice_Bot
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
# .\\venv\\Scripts\\activate
# On macOS/Linux:
# source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: You may need to install system-level dependencies for PyAudio depending on your OS.

### 4. Set Up Your Google Gemini API Key

> ⚠️ **Security Warning:** *Do NOT commit your API key to GitHub.*

Set your API key as an environment variable named **`GEMINI_API_KEY`**.

**Linux/macOS:**

```bash
export GEMINI_API_KEY="YOUR_ACTUAL_GOOGLE_GEMINI_API_KEY"
```

**Windows (CMD):**

```bash
set GEMINI_API_KEY="YOUR_ACTUAL_GOOGLE_GEMINI_API_KEY"
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

This will open the AI Voice Assistant at: **[http://localhost:8501](http://localhost:8501)**

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the **MIT License**. See the LICENSE file for more details.
