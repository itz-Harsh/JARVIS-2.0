# JARVIS 2.0 🤖✨

A local voice assistant written in Python. JARVIS 2.0 provides speech input/output, system controls, web searches, Wikipedia summaries, translations, and optional AI replies using the Google Generative AI SDK.

## 📁 What this repository contains

- `src/` — Python source modules (voice I/O, core actions, smart helpers, AI integration).
- `assets/lang.json` — language mappings used by translation features.
- `requirements.txt` — Python dependencies.

## ✨ Features (for future updates)

- 🎙️ Voice Input/Output – Talk to Jarvis naturally
- ⛅ Weather Updates – Live weather from OpenWeather API
- 🌍 Language Translation – Auto-responds in your language
- 🔊 System Controls – Manage volume, brightness, WiFi, Bluetooth
- 🔐 PC Sign-In Automation – Auto-type your PIN at login
- 🗣️ Text-to-Speech (TTS) – Supports multiple voices
- ⚡ Modular Commands – Easy to extend with new features

_Inspired by Iron Man's virtual assistant — JARVIS._

## 🛠️ Tech Stack

- 🐍 Python 3.13
- 🎤 SpeechRecognition (voice input)
- 🔊 pyttsx3 / alternatives (text-to-speech)
- 🌐 OpenWeather API (weather)
- 🌍 LibreTranslate API (translation)
- 💻 PyAutoGUI (PC automation)
- ⚡ Custom Commands Framework

## ✅ Requirements

- Windows (tested)
- Python 3.8+ (recommended 3.13 for parity with compiled files)
- Microphone and speaker access for voice features

## ⚙️ Install (PowerShell)

```powershell
# create and activate a virtual environment
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## 🔐 Environment

Create a `.env` file at the project root with any required secrets. Example:

```
ai-api-key=YOUR_GOOGLE_GENERATIVE_API_KEY
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_KEY
```

`src/Brain.py` reads `ai-api-key` from the environment for AI queries. Other modules may expect additional keys (for example, weather).

## 🛠️ Notes & Troubleshooting

- Microphone permissions: ensure your OS allows Python to access the microphone.
- `pyttsx3` voice index varies by system. If `voices[2]` raises an IndexError, print `voices` and pick an available index.
- `pyautogui` may require additional OS dependencies on Windows — check the package docs if installs fail.

## 📂 Assets

- `assets/lang.json` is required by the translation feature. Keep it in the `assets/` folder.

## ➕ Next steps you might want

- Add driver code to `src/main.py` to wire voice commands to the functions in `src/`.
- Add unit tests for core functions.
- Add a `.env.example` and `CONTRIBUTING.md` for contributors.

If you'd like, I can add a `.env.example`, create a minimal runnable `src/main.py` demo, or add a small test file — tell me which and I will implement it.

