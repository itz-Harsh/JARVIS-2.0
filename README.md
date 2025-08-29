# JARVIS 2.0 🤖✨

Welcome to JARVIS 2.0 — a local, modular voice assistant for Windows built with Python. This project provides speech input/output, system control helpers, web/search utilities, translation, screenshots, messaging helpers, and an optional AI conversational backend.

## 📁 Project structure

- `src/` — core Python modules (voice_io, Basic, smart, system, multimedia, Brain)
- `assets/` — language mappings, contacts, screenshots
- `requirements.txt` — Python dependencies
- `commands.txt` — supported voice commands reference

## ✨ Key features

- 🎙️ Voice Input/Output — Speak naturally to JARVIS using your microphone
- 🌐 Web searches & Wikipedia — quick information retrieval
- ⛅ Weather — live weather via OpenWeather API
- 🌍 Translation — translate and auto-type translated text
- 🔊 System controls — volume, brightness, shutdown, restart, lock
- 📸 Screenshots — take and open saved screenshots
- � Messaging helpers — send WhatsApp messages (via pywhatkit) and load contacts from `assets/Contacts.vcf`
- 🧠 AI integration — optional Google Generative AI (Gemini) for conversational replies and code generation
- ⚡ Modular commands — add new features by editing `src/` modules

_Inspired by Iron Man's virtual assistant — JARVIS._

## 🛠️ Tech stack

- Python 3.8+ (project includes some .pyc built for 3.13)
- google-generativeai (optional, for AI replies)
- speech_recognition, pyttsx3 (voice I/O)
- pyautogui (automation & screenshots)
- requests, wikipedia, langdetect, pywhatkit
- python-dotenv (load `.env` keys)

## ✅ Requirements (short)

- Windows (features use Windows-specific commands)
- Microphone & speakers
- Python 3.8+
- Install dependencies from `requirements.txt`

## 🗂️ File Structure

Visual project tree (embedded):

```
# File Tree: JARVIS 2.0
├── 📁 .git/ 🚫 (auto-hidden)
├── 📁 .venv/ 🚫 (auto-hidden)
├── 📁 assets/
│   ├── 📁 screenshots/ 🚫 ((empty at Start))
│   ├── 📁 savefile/ 🚫 ((empty at Start))
│   └── 📄 lang.json
│   └── 📄 Contacts.vcf 🚫 (auto-hidden)
├── 📁 src/
├── ├── 📁 memory/
│        └── 📄 chat_memory.json 🚫 (empty at Start)
│   ├── 📁 __pycache__/ 🚫 (auto-hidden)
│   ├── 🐍 Basic.py
│   ├── 🐍 Brain.py
│   ├── 🐍 main.py
│   ├── 🐍 multimedia.py
│   ├── 🐍 smart.py
│   ├── 🐍 system.py
│   └── 🐍 voice_io.py
├── 🔒 .env 🚫 (auto-hidden)
├── 🚫 .gitignore
├── 📖 README.md
├── 📄 commands.txt
└── 📄 requirements.txt
```

You can also view the same content in the sibling file [`FileTree.txt`](./FileTree.txt).

## ⚙️ Install (PowerShell)

```powershell
# from project root
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Notes:
- If `PyAudio` fails to install on Windows, use a prebuilt wheel or consider `sounddevice` as an alternative.
- `pyttsx3` voice indices differ per system — inspect available voices and choose a valid index.

## 🔐 Environment variables

Create a `.env` file in the project root. Example:

```
ai-api-key=YOUR_GOOGLE_GENERATIVE_API_KEY
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_KEY
```

- `ai-api-key` (optional) — used by `src/Brain.py` for Gemini-based replies
- `weather-api` / `OPENWEATHER_API_KEY` — used by `src/smart.py` for weather lookups

## ▶️ How to run

The assistant entrypoint is `src/main.py`.

Run from project root (PowerShell):

```powershell
python -m src.main
```

Or run interactively in a REPL to test functions:

```powershell
python
>>> from src.voice_io import speak
>>> speak('Hello from JARVIS')
```

## 📚 Supported commands

See `commands.txt` for the full list of supported voice commands and examples. The file is kept updated as features are added.

## ⚙️ Implementation notes

- `src/voice_io.py` uses `speech_recognition` to listen and `pyttsx3` for TTS.
- `src/Basic.py` implements app launching, web search, and screenshots.
- `src/smart.py` handles Wikipedia, translation, notepad writing, weather, and messaging helpers.
- `src/system.py` exposes system-level actions (volume/brightness/shutdown/restart/lock/usage).
- `src/Brain.py` wires to Google Generative AI and persists chat history in `src/memory/chat_memory.json`.

## 🛠️ Troubleshooting & tips

- Microphone timeout/recognition: increase timeout in `src/voice_io.py` if your mic is slow.
- pyttsx3 voices: if `voices[2]` fails, list `engine.getProperty('voices')` and choose a valid index.
- Permissions: grant microphone access to Python and your terminal.
- PyAutoGUI: may require Pillow and OS-level support — ensure dependencies in `requirements.txt` are installed.

## 🧪 Testing suggestions

- Add a small test script under `tests/` that mocks `voice()` and verifies handlers in `src/main.py` call the right functions.

## ➕ Contributing

1. Fork the repo
2. Create a topic branch
3. Add tests for new behavior
4. Open a PR with a clear description

If you'd like, I can add a `.env.example`, a small `tests/` harness, or a minimal `src/main.py` demo with a dry-run mode. Tell me which and I'll implement it.

---
Small note: this README is kept intentionally developer-focused. If you want a shorter "Getting Started" or a visual quickstart with screenshots and emoji badges, tell me which style you prefer and I will update it.

Made with ❤️ by Harsh 