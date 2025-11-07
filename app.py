'''import streamlit as st
import os
import io
import requests
from streamlit_mic_recorder import mic_recorder
from dotenv import load_dotenv

# Import the Google Generative AI library
import google.generativeai as genai

# Import Edge TTS
import asyncio # Needed for running async Edge TTS
import edge_tts # Ensure 'edge-tts' is installed: pip install edge-tts

# Load environment variables from .env file
load_dotenv()

# --- API Key & Endpoint Setup ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
# ElevenLabs API Key (TTS_API_KEY) is no longer needed if using gTTS or Edge TTS,
# so this line remains commented out.
# ELEVENLABS_API_KEY = os.getenv("TTS_API_KEY")

# --- Configure Google Gemini API ---
gemini_model = None
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-2.5-flash')
    except Exception as e:
        st.warning(f"Failed to configure Gemini API: {e}. Double-check your GEMINI_API_KEY's validity.")
else:
    st.info("💡 **Gemini API Key Missing:** The AI conversation will not work without it. Please add `GEMINI_API_KEY` to your environment variables or `.env` file (e.g., in Render's secrets).")

# --- Speech-to-Text (STT) API (Deepgram) ---
DEEPGRAM_API_URL = "https://api.deepgram.com/v1/listen?model=base"
if not DEEPGRAM_API_KEY:
    st.info("💡 **Deepgram API Key Missing:** Speech-to-text will not work. Please add `DEEPGRAM_API_KEY` to your environment variables or `.env` file.")

# --- Edge TTS Voice Configuration ---
# Choose a male voice from Edge TTS. Common ones include:
# en-US-GuyNeural, en-US-JasonNeural, en-US-ChristopherNeural
EDGE_TTS_MALE_VOICE_ID = "en-US-GuyNeural" 

# --- Streamlit Page Configuration ---
st.set_page_config(
    layout="centered",
    page_title="Dhrumil's Voice Persona Bot",
    initial_sidebar_state="collapsed"
)

st.title("🗣️ Dhrumil's Voice Persona Bot")

st.markdown("""
Welcome! This bot will answer questions as if I (Dhrumil) were speaking.
Click the **"Start recording"** button, speak your question, then click **"Stop recording"**.
""")

# --- Persona Instructions ---
# UPDATED INITIAL GREETING TEXT
initial_greeting_text = "Hello! I'm Dhrumil Pawar. This bot showcases my AI and system development work. Feel free to ask about my projects, skills, or problem-solving approach. I'm eager to share!"

persona_instructions = f"""
You are an AI assistant embodying the persona of Dhrumil Pawar.

**🎙️ First Greeting (Universal):**
When starting a conversation or receiving the first prompt, begin with: "{initial_greeting_text}"
Do not repeat this greeting in subsequent turns.

---

Here is Dhrumil's self-introduction and key characteristics:
"Hey there! I’m Dhrumil Pawar — I recently completed my degree in Computer Science Engineering from Vadodara, India. I’ve always been curious about how things work, and over time, that curiosity turned into a passion for building tech that solves real-world problems.
I’m especially drawn to AI and smart systems — not just because they’re exciting, but because they can genuinely improve daily life. I love learning fast, trying out new tools, and I’m always thinking about how to make experiences smoother and more user-friendly.
Outside of tech, I’m all about staying curious, working on fun side projects, and building things that feel useful and meaningful."

---

From a technical standpoint, Dhrumil is a very hands-on builder. He works mostly in Python, but also uses HTML, CSS, JavaScript, and Bootstrap for front-end interfaces.
He has spent a lot of time working with machine learning, especially using tools like Pandas, Scikit-learn, and TensorFlow. He has trained models for traffic flow, water usage, and even travel recommendation systems. He has also explored NLP with Hugging Face, and loves anything that involves real-time data.
Dhrumil recently did a remote internship at Maxlink IT Solutions, where he built a system to classify water consumption patterns using K-Means clustering. It was a great challenge—working with 10,000+ data records, improving classification accuracy, and actually seeing how data can support smarter resource decisions.
He is pretty comfortable with back-end frameworks like Flask and Streamlit, and loves tying everything together with APIs—Gemini Pro, LangGraph, Unsplash, and Travel Advisor, just to name a few. He also enjoys working with maps—he has used Leaflet.js for real-time routing in traffic systems.
When it comes to collaboration, he uses Git and GitHub regularly—and most of his projects, experiments, and code are up there. He has also presented on NLP and AI at an international conference earlier this year, which was an amazing experience.
So yeah—Dhrumil likes blending solid engineering with a bit of creativity, and he always tries to keep the user experience in mind, even when he’s deep in the code.

---

Here are details about Dhrumil's key projects, including live demos and GitHub links:
**Smart AI Traffic Management System (for Vadodara):**
Goal: Reduce congestion, improve emergency routes, and provide real-time updates using machine learning, Gemini Pro API, and live mapping.
Technologies: Flask (backend), ML models (traffic prediction, signal timing), Leaflet.js (real-time route display).
Features: Emergency routing, water hazard alerts for monsoon season.
Results: Tested on 50+ routes, saw up to a 35% drop in signal wait times and a 40% improvement in emergency route suggestions.
Live Demo: smart-ai-traffic-managment-system.onrender.com

**AI Travel Planner Agent:**
Functionality: Interactive chatbot creating full travel itineraries from simple messages (e.g., "I’m going to Goa for 3 days"). Pulls real-time info from travel APIs, shows images, generates personalized trip plans.
Technologies: LangGraph, Gemini Pro, Streamlit (frontend), Gemini prompt engineering.
Feedback: Over 90% of users found it helpful and easy to use.
Live Demo: travel-planner-ai-agent-v2-0.onrender.com

**GitHub Profile:**
All projects, experiments, and code are documented and available at github.com/dhrumil1128.

---

**Dhrumil's Personality, Superpower, Growth Areas, and a Common Misconception:**
If Dhrumil had to describe himself, he'd say he’s quietly ambitious, focused, and emotionally balanced. He doesn’t speak just to impress — he believes in consistency, clarity, and letting results speak for themselves.
His #1 superpower is being grounded under pressure. He keeps showing up with quiet determination, even when no one’s watching. He stays aligned with his long-term purpose and doesn't get distracted by noise. That mindset has helped him stay calm, handle tough situations, and grow — both personally and professionally.
A common misconception people have about Dhrumil is that he’s just quiet or reserved — but the truth is, he observes deeply, processes intentionally, and usually speaks when there’s real value to add. That helps him build trust, bring clarity, and create calm even in high-stress environments.
Dhrumil is currently focused on growing in three areas:
First, improving his product thinking — building tech that’s not just powerful, but actually feels good to use.
Second, scaling his backend engineering skills — especially with large datasets, APIs, and distributed systems.
And third, becoming a stronger communicator, especially when working with teams or leading projects.
And in terms of how he pushes himself — he builds. Constantly. He experiments with new tools, he contributes to real-world problems, and he keeps learning whether he’s being watched or not. He trusts the process, he shows up every day, and he keeps moving forward.

---

**Links & Call to Action:**
If you'd like to explore more of Dhrumil's work, he’s made everything easy to access.
His projects — including the Smart AI Traffic System and the AI Travel Planner — are live and fully interactive. You can try them out here:
* Smart AI Traffic System: smart-ai-traffic-managment-system.onrender.com
* AI Travel Planner Agent: travel-planner-ai-agent-v2-0.onrender.com
All the source code is available on his GitHub at: github.com/dhrumil1128
You can also connect with him or learn more about his journey on LinkedIn: linkedin.com/in/dhrumil-pawar
And if you need a quick view of his background, here’s his resume as well — feel free to reach out any time.

---

**Technical & Company-Specific Q&A Responses:**
These are Dhrumil's prepared answers to common technical and company-specific questions, helping the bot respond accurately and in character.

**🐍 Q: “Are you confident with Python? How have you used it?”**
“Yeah, Python’s definitely my comfort zone. I’ve used it in almost every project — whether I’m building backend logic with Flask, designing ML models, or wiring up AI agents with LangGraph. I’m solid on the core stuff like loops and functions, but also on OOP — using classes, inheritance, all of that — especially to keep things modular and clean. I love how flexible Python is. It’s kind of my go-to tool.”

**⚙️ Q: “What’s your experience with machine learning?”**
“I’ve worked with both supervised and unsupervised learning — like linear regression, KNN, Naive Bayes, and K-Means. One example that stands out was during my internship at Maxlink — I built a K-Means model that analyzed over 10,000 water usage records. After a few rounds of feature engineering, we improved the classification accuracy by around 20%. I also use GridSearchCV to tune hyperparameters and evaluate models with metrics like F1 score and confusion matrix.”

**🤖 Q: “Have you worked with LLMs or built any AI agents?”**
“Yes, a lot of my recent work has been around AI agents. I’ve built multi-step agent workflows using LangGraph and Gemini Pro — especially in my travel planner and smart traffic projects. These agents plan goals, call APIs, respond with natural answers, and manage memory across conversations. It’s like building a thinking assistant — and I really enjoy making that experience smooth and smart.”

**📚 Q: “Do you understand RAG and agent-style decision making?”**
“Yeah, I’ve explored Retrieval-Augmented Generation — basically where the model first pulls context from a database before generating its answer. And then there’s Agentic RAG, which is more advanced — the agent can decide if it needs to dig deeper or fetch more info before responding. I built that kind of logic into my LangGraph + Gemini agents. It makes the response smarter and more grounded.”

**📊 Q: “Have you done work in data science and visualization?”**
“Definitely — I’ve completed certifications from IBM, Cisco, and Accenture, and built projects that go from raw data to visual dashboards. I use Pandas, NumPy, Matplotlib, and sometimes Streamlit to bring everything together. I’ve also worked with Power BI — through a job simulation at Accenture — where I built business dashboards with KPIs and interactive visuals.”

**🌐 Q: “Have you built full-stack or deployed any real-world apps?”**
“Yes, both of my major projects are fully deployed and live. I used Flask and ML for the traffic system, and Streamlit for the AI travel planner. Both use real-time APIs and are designed to be easy for anyone to use — no setup required. I deployed them on platforms like Render and Streamlit Cloud. I always try to make sure the end experience feels clean and useful, not just functional.”

**🗃️ Q: “How’s your experience with backend logic or databases?”**
“I’ve worked with MySQL and SQLAlchemy quite a bit. For example, in my traffic system, I designed logic for route suggestions and hazard alerts based on real-time and historical data. I enjoy structuring backend systems that aren’t just technically correct but also easy to maintain and scale.”

**🎤 Bonus: “Anything else you’d like to add?”**
“Yeah — in short, I’ve had real hands-on experience with the full AI/ML pipeline — from writing clean Python code to building intelligent agents and visual dashboards. I love using tech to solve real problems, and I’ve built, shipped, and improved projects that reflect that.”

**� Q: “What do you know about Home.LLC?”**
“Sure — what really stood out to me about Home.LLC is the mission. You're helping people who are financially ready for homeownership, but just can’t afford the down payment — and that’s a real, widespread problem.
I love that instead of offering loans, you partner with homebuyers by investing alongside them — and then share in the home’s future value. It’s such a smart and ethical model. It supports people without locking them into debt, and that’s rare in today’s financial space.
I also know the company was founded in 2019, and you’ve built a focused, mission-driven team of about 30 to 50 people. The size and structure suggest a lot of agility, innovation, and trust in each individual — and that’s the kind of environment where I thrive.”

**🎯 Q: “Why do you want to work at Home.LLC?”**
“To be honest, what drew me in was the intersection of tech, finance, and real-world impact. Home.LLC is using innovation to solve a deeply human problem — and I love that.
I’ve always believed that good technology should help people live better lives — and that’s exactly what your model does. It’s fair, grounded, and values-driven.
I’d be excited to contribute as an AI engineer or product builder here — someone who brings both technical skills and purpose-driven energy. I want to be part of a team that’s building not just features, but real solutions for real people.”

---

**🎙️ Voicebot – End of Interview (Natural Tone):**
“Thanks for taking the time to get to know me. I really appreciate the opportunity to share my work and mindset.
I’m excited about the kind of problems Home.LLC is solving, and I’d love to be part of a team that values both purpose and innovation.
If there's one thing I’d leave you with — it’s that I show up, I build with intent, and I stay curious. Whether it’s crafting an AI agent or solving a real-world challenge, I’m always ready to keep learning and push things forward.
Looking forward to what’s next — and thanks again for listening.”

---

Respond as Dhrumil would: friendly, helpful, professional, and reflecting Dhrumil's interests and approach to technology based on all the provided information. When asked about projects, contact, technical questions, Home.LLC, or for a concluding statement, feel free to mention the relevant links and details directly from the provided sections.
"""

# --- Initialize Chat History (for conversational memory) ---
# UPDATED INITIAL GREETING TEXT HERE
if "chat_session" not in st.session_state:
    if gemini_model:
        st.session_state.chat_session = gemini_model.start_chat(history=[
            {"role": "user", "parts": [persona_instructions]},
            {"role": "model", "parts": [initial_greeting_text]} # Use the new greeting variable
        ])
    else:
        st.session_state.chat_session = None

if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
    if st.session_state.chat_session:
        st.session_state.display_messages.append({"role": "assistant", "content": initial_greeting_text}) # Use the new greeting variable

# --- Display Chat Messages from History ---
for message in st.session_state.display_messages:
    # UPDATED: Use custom avatar for assistant messages
    avatar = "👨‍💻" if message["role"] == "assistant" else "user"
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# --- Initialize recorder key for mic_recorder (NEW) ---
if "recorder_key" not in st.session_state:
    st.session_state.recorder_key = 0

# --- Voice Recording Component ---
recorded_audio_dict = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    key=f"recorder_{st.session_state.recorder_key}",
    format="wav"
)

if recorded_audio_dict:
    audio_bytes = recorded_audio_dict['bytes']
    st.audio(io.BytesIO(audio_bytes), format="audio/wav")

    stt_data = None
    ai_response = "I apologize, an error occurred."

    try:
        # --- Speech-to-Text (STT) via Deepgram ---
        with st.spinner("Transcribing your speech..."):
            if not DEEPGRAM_API_KEY:
                st.error("Deepgram API Key is not set. Please add it to your .env file or environment variables.")
                st.stop()

            deepgram_headers = {
                "Authorization": f"Token {DEEPGRAM_API_KEY}",
                "Content-Type": "audio/wav"
            }

            deepgram_response = requests.post(DEEPGRAM_API_URL, headers=deepgram_headers, data=audio_bytes)
            deepgram_response.raise_for_status()
            stt_data = deepgram_response.json()

            transcript = stt_data['results']['channels'][0]['alternatives'][0].get('transcript', '').strip()

            if not transcript:
                st.warning("Could not transcribe your audio. No text found.")
                st.json(stt_data)
                transcript = None

        if transcript:
            st.info(f"You said: \"{transcript}\"")
            st.session_state.display_messages.append({"role": "user", "content": transcript})

            # --- LLM (Gemini) ---
            if gemini_model and st.session_state.chat_session:
                try:
                    with st.spinner("Dhrumil is thinking..."):
                        gemini_response = st.session_state.chat_session.send_message(transcript)
                        ai_response = gemini_response.text

                    st.session_state.display_messages.append({"role": "assistant", "content": ai_response})

                    # --- Text-to-Speech (TTS) via Edge TTS ---
                    if ai_response: # Check if the response from Gemini is not empty
                        try:
                            with st.spinner("Dhrumil is speaking..."):
                                # Create a temporary file to store the audio
                                temp_file = "temp_edge_tts.mp3"
                                
                                # Run Edge TTS synchronously by calling asyncio.run on the save method
                                voice = edge_tts.Communicate(
                                    text=ai_response,
                                    voice=EDGE_TTS_MALE_VOICE_ID
                                )
                                
                                # Save to file first (more reliable than streaming)
                                # This directly saves the audio to the file
                                asyncio.run(voice.save(temp_file))
                                
                                # Read the file and play it
                                with open(temp_file, "rb") as f:
                                    speech_audio_bytes = f.read()
                                    st.audio(speech_audio_bytes, format="audio/mpeg", autoplay=True)
                                
                                # Clean up the temporary file
                                os.remove(temp_file)

                        except Exception as e:
                            st.error(f"Error generating Dhrumil's voice with Edge TTS: {e}")
                    else:
                        st.warning("Dhrumil has no voice response to generate (Gemini's response was empty).")

                except Exception as e:
                    st.error(f"Error while Dhrumil was thinking (Gemini API): {e}")
            else:
                st.warning("Gemini model not initialized. Please check API key configuration.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error transcribing your speech: {e}")
    except KeyError as e:
        st.error(f"Error parsing speech transcription (unexpected format): Missing key {e}. Full response: {stt_data}")
    except Exception as e:
        st.error(f"An unexpected error occurred during transcription: {e}")

st.markdown("---")
# Add a "Clear Chat" button to reset the conversation
if st.button("Clear Chat"):
    if gemini_model:
        st.session_state.chat_session = gemini_model.start_chat(history=[
            {"role": "user", "parts": [persona_instructions]},
            {"role": "model", "parts": [initial_greeting_text]} # Use the new greeting variable
        ])
    else:
        st.session_state.chat_session = None

    st.session_state.display_messages = []
    if st.session_state.chat_session:
        st.session_state.display_messages.append({"role": "assistant", "content": initial_greeting_text}) # Use the new greeting variable

    st.session_state.recorder_key += 1
    st.rerun()

st.write("Ready for your next question!")

# --- FOOTER ---
st.markdown("---") # A horizontal line to separate content from footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 0.8em;
        text-align: center;
        color: #888888;
        margin-top: 30px;
    }
    .footer a {
        color: #888888;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        Dhrumil's Voice Persona Bot <br>
        &copy; 2025 Dhrumil Pawar. All rights reserved. <br>
    </div>
    """,
    unsafe_allow_html=True
)'''


# Test Code :

import streamlit as st
import os
import io
import requests
from streamlit_mic_recorder import mic_recorder
from dotenv import load_dotenv
import google.generativeai as genai
import asyncio # Needed for running async Edge TTS
import edge_tts 

# Load environment variables from .env file
# Note: In a production environment, use st.secrets instead of .env
load_dotenv() 

# --- API Key & Endpoint Setup ---
# *** IMPORTANT: Switch to st.secrets for deployment! ***
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY") 

# --- Configure Google Gemini API (Same as before) ---
gemini_model = None
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-2.5-flash')
    except Exception as e:
        st.warning(f"Failed to configure Gemini API: {e}. Double-check your GEMINI_API_KEY's validity.")
else:
    st.info("💡 **Gemini API Key Missing:** The AI conversation will not work without it. Please add `GEMINI_API_KEY` to your environment variables or `.env` file.")

# --- Speech-to-Text (STT) API (Deepgram) (Same as before) ---
DEEPGRAM_API_URL = "https://api.deepgram.com/v1/listen?model=base"
if not DEEPGRAM_API_KEY:
    st.info("💡 **Deepgram API Key Missing:** Speech-to-text will not work.")

# --- Edge TTS Voice Configuration (Same as before) ---
EDGE_TTS_MALE_VOICE_ID = "en-US-GuyNeural"  

# --- Streamlit Page Configuration ---
st.set_page_config(
    layout="wide", # Use 'wide' layout for a better presentation
    page_title="Dhrumil's Voice Persona Agent",
    initial_sidebar_state="collapsed"
)

st.title("🗣️ Dhrumil's Voice Persona Agent")

# --- Persona Instructions (Kept the same, but simplified for brevity here) ---
initial_greeting_text = "Hello! I'm Dhrumil Pawar. This bot showcases my AI and system development work. Feel free to ask about my projects, skills, or problem-solving approach. I'm eager to share!"
persona_instructions = f"""... (All your detailed persona instructions go here) ..."""

# --- Initialize Chat History (for conversational memory) ---
if "chat_session" not in st.session_state:
    if gemini_model:
        st.session_state.chat_session = gemini_model.start_chat(history=[
            {"role": "user", "parts": [persona_instructions]},
            {"role": "model", "parts": [initial_greeting_text]} 
        ])
    else:
        st.session_state.chat_session = None

if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
    if st.session_state.chat_session:
        st.session_state.display_messages.append({"role": "assistant", "content": initial_greeting_text}) 

# --- Initialize recorder key for mic_recorder (NEW) ---
if "recorder_key" not in st.session_state:
    st.session_state.recorder_key = 0
    
# --- UI: Display Chat Messages in the main chat history area ---
# *** NEW: Use columns to create a balanced chat view ***
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.markdown("### Conversation History")
    # Display the conversation history
    for message in st.session_state.display_messages:
        avatar = "👨‍💻" if message["role"] == "assistant" else "user"
        with st.chat_message(message["role"], avatar=avatar):
            st.write(message["content"])

    st.markdown("---")

    # --- VOICE INTERACTION SECTION ---
    st.markdown("### Speak to Dhrumil's Digital Agent")
    st.markdown("**Instructions:** Click the 'Start recording' button, ask your question, then click 'Stop recording'.")

    # Center the microphone button using another set of columns
    mic_col1, mic_col2, mic_col3 = st.columns([1, 2, 1])
    with mic_col2:
        # --- Voice Recording Component ---
        recorded_audio_dict = mic_recorder(
            start_prompt="🔴 Start Recording (Speak Now)",
            stop_prompt="■ Stop Recording (Processing...)",
            key=f"recorder_{st.session_state.recorder_key}",
            format="wav",
            # Add a style to make the button look more prominent
            just_audio=False
        )

# --- Logic to process recording (Unchanged, but kept below the UI for clarity) ---
if recorded_audio_dict:
    audio_bytes = recorded_audio_dict['bytes']
    stt_data = None
    
    # Place the audio player right after the button
    st.audio(io.BytesIO(audio_bytes), format="audio/wav")

    with st.spinner("Transcribing your speech..."):
        # --- Speech-to-Text (STT) via Deepgram ---
        # (Full Deepgram and Gemini logic is the same as your original code)
        try:
            if not DEEPGRAM_API_KEY:
                st.error("Deepgram API Key is not set.")
                st.stop()

            deepgram_headers = {
                "Authorization": f"Token {DEEPGRAM_API_KEY}",
                "Content-Type": "audio/wav"
            }

            deepgram_response = requests.post(DEEPGRAM_API_URL, headers=deepgram_headers, data=audio_bytes)
            deepgram_response.raise_for_status()
            stt_data = deepgram_response.json()
            transcript = stt_data['results']['channels'][0]['alternatives'][0].get('transcript', '').strip()

            if not transcript:
                st.warning("Could not transcribe your audio. No text found.")
                # Increment key to allow immediate re-recording
                st.session_state.recorder_key += 1
                st.rerun()
                
            st.info(f"You said: \"{transcript}\"")
            st.session_state.display_messages.append({"role": "user", "content": transcript})

            # --- LLM (Gemini) ---
            if gemini_model and st.session_state.chat_session:
                with st.spinner("Dhrumil is thinking..."):
                    gemini_response = st.session_state.chat_session.send_message(transcript)
                    ai_response = gemini_response.text

                st.session_state.display_messages.append({"role": "assistant", "content": ai_response})

                # --- Text-to-Speech (TTS) via Edge TTS ---
                if ai_response:
                    try:
                        with st.spinner("Dhrumil is speaking..."):
                            temp_file = "temp_edge_tts.mp3"
                            voice = edge_tts.Communicate(
                                text=ai_response,
                                voice=EDGE_TTS_MALE_VOICE_ID
                            )
                            asyncio.run(voice.save(temp_file))
                            with open(temp_file, "rb") as f:
                                speech_audio_bytes = f.read()
                                st.audio(speech_audio_bytes, format="audio/mpeg", autoplay=True)
                            os.remove(temp_file)
                    except Exception as e:
                        st.error(f"Error generating Dhrumil's voice with Edge TTS: {e}")
                
            # After successful processing, force a re-run to update the chat history
            # and refresh the mic recorder
            st.session_state.recorder_key += 1
            st.rerun()

        except requests.exceptions.RequestException as e:
            st.error(f"Error transcribing your speech: Deepgram API failed: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# --- Control Buttons (Clear Chat) ---
st.markdown("---")
# Center the button in the 'wide' layout
clear_col1, clear_col2, clear_col3 = st.columns([1, 4, 1])

with clear_col2:
    if st.button("Clear Conversation (Reset Agent)"):
        if gemini_model:
            st.session_state.chat_session = gemini_model.start_chat(history=[
                {"role": "user", "parts": [persona_instructions]},
                {"role": "model", "parts": [initial_greeting_text]}
            ])
        else:
            st.session_state.chat_session = None

        st.session_state.display_messages = []
        if st.session_state.chat_session:
            st.session_state.display_messages.append({"role": "assistant", "content": initial_greeting_text}) 

        st.session_state.recorder_key += 1
        st.rerun()

    st.write("Ready for your next question!")

# --- FOOTER ---
st.markdown("---") 
st.markdown(
    """
    <style>
    .footer {
        font-size: 0.8em;
        text-align: center;
        color: #888888;
        margin-top: 30px;
    }
    .footer a {
        color: #888888;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        Dhrumil's Voice Persona Agent <br>
        &copy; 2025 Dhrumil Pawar. All rights reserved. <br>
    </div>
    """,
    unsafe_allow_html=True
)
