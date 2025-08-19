# 🕶️ Jarvis 2.0 – Your AI Desktop Assistant 🤖✨  

Jarvis 2.0 is a **voice-controlled AI assistant** built with Python 🐍.  
It can perform **system tasks, translations, weather reports, and much more** – just like Tony Stark’s J.A.R.V.I.S 😎.  

---

## ✨ Features  
- 🎙️ **Voice Input/Output** – Talk to Jarvis naturally  
- ⛅ **Weather Updates** – Live weather from OpenWeather API  
- 🌍 **Language Translation** – Auto-responds in your language  
- 🔊 **System Controls** – Manage **volume, brightness, WiFi, Bluetooth**  
- 🔐 **PC Sign-In Automation** – Auto-type your PIN at login  
- 🗣️ **Text-to-Speech (TTS)** – Supports multiple voices  
- ⚡ **Modular Commands** – Easy to extend with new features  

---

## 🛠️ Tech Stack  
- 🐍 Python 3.13  
- 🎤 SpeechRecognition (voice input)  
- 🔊 pyttsx3 / alternatives (text-to-speech)  
- 🌐 OpenWeather API (weather)  
- 🌍 LibreTranslate API (translation)  
- 💻 PyAutoGUI (PC automation)  
- ⚡ Custom Commands Framework  

---

## 🚀 Installation  

```bash
# Clone this repo
git clone https://github.com/your-username/jarvis-2.0.git
cd jarvis-2.0

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
