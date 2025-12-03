🎤 AI Voice Assistant Bot (Gemini Powered)

🚀 Project Overview

This project implements an interactive AI Voice Assistant that allows users to communicate with the latest Large Language Models (LLMs) using natural voice commands. It is designed to capture spoken input, process it using the powerful Google Gemini API, and provide informative, real-time responses.

The application leverages a Speech-to-Text (STT) engine to convert voice input into text and then sends this query to the Gemini model for generation, creating a hands-free, conversational interface.

✨ Features

Voice Command Interface: Allows users to interact with the AI purely through spoken words.

Google Gemini Integration: Utilizes gemini-1.5-flash for high-quality, fast, and relevant text generation.

Real-time Speech Recognition: Converts live audio streams into text input for the LLM.

Conversational Memory: Maintains a continuous chat history, allowing the AI to recall previous turns and maintain context.

Intuitive UI: Built with Streamlit for a simple, engaging, and modern web interface.

Easy Configuration: Uses a secure method to load the Google API key via environment variables.

🛠️ Technologies Used

Python 3.10+: The core programming language.

Streamlit: For building the web application and user interface.

Google GenAI SDK (google-genai): The official library for connecting to the Gemini API.

SpeechRecognition: A robust Python library used for handling voice input and integrating with various speech recognition engines (e.g., Google Speech Recognition).

PyAudio: Necessary dependency for microphone input support.

⚙️ Architecture & How It Works

The voice assistant follows a straightforward yet powerful flow:

Voice Input: The user clicks a button or triggers a voice activation command to begin speaking.

Speech-to-Text (STT): The SpeechRecognition library captures the audio from the microphone and sends it to a recognition service (e.g., Google's) to convert the speech into a written query string.

LLM Processing: The text query is sent to the gemini-1.5-flash model via the google-genai SDK, along with the current conversation history.

Response Generation: Gemini processes the request and generates a concise, relevant text answer.

Display: The generated text response is displayed to the user in the Streamlit chat interface.

💻 Local Setup & Installation

Follow these steps to get the AI Voice Bot running on your local machine.

1. Clone the Repository

git clone [https://github.com/dhrumil1128/AI_Voice_Bot.git](https://github.com/dhrumil1128/AI_Voice_Bot.git)
cd AI_Voice_Bot


2. Create a Virtual Environment (Recommended)

python -m venv venv
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3. Install Dependencies

Install all required Python packages using the requirements.txt file.

pip install -r requirements.txt


(Note: Depending on your operating system, you may need to install system dependencies for PyAudio before running the pip install command.)

4. Set Up Your Google Gemini API Key

⚠️ SECURITY WARNING: DO NOT commit your API key directly to your GitHub repository.

You must set your API key as an environment variable named GEMINI_API_KEY.

Linux/macOS

export GEMINI_API_KEY="YOUR_ACTUAL_GOOGLE_GEMINI_API_KEY"


Windows (Command Prompt)

set GEMINI_API_KEY="YOUR_ACTUAL_GOOGLE_GEMINI_API_KEY"


(For persistence across sessions, consult your operating system's documentation on setting permanent environment variables.)

5. Run the Streamlit Application

Execute the following command from the root directory of the project:

streamlit run app.py


This will automatically open the AI Voice Assistant in your default web browser, usually at http://localhost:8501.

🤝 Contributing

We welcome contributions! If you have suggestions for new features, bug fixes, or improvements to the architecture, please feel free to open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
