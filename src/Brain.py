import google.generativeai as genai
import os, json
from dotenv import load_dotenv
from voice_io import speak

load_dotenv()
api_key = os.getenv('ai-api-key')

genai.configure(api_key=api_key)

model_name = "gemini-1.5-flash"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "memory")
os.makedirs(ASSETS_DIR, exist_ok=True)

HISTORY_FILE = os.path.join(ASSETS_DIR, "chat_memory.json")

# Load history if exists
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = []

# Model setup
model = genai.GenerativeModel(
    model_name=model_name,
    system_instruction=(
        "You are a helpful virtual assistant like a real human. "
        "Your Name is JARVIS. You can answer questions, provide information, "
        "and assist with various tasks. Please respond in a friendly and short length. "
        "You will respond in the same as the user query language. "
        "You can remember our previous conversation."
        "When writing code, do not include any explanations, only provide the code block. Only the pure script"
        "telling to send any message to anyone, you do not do anything, just retrun the message only as it is. No need to explain whom the message is sended. like don't say 'message sent to xyz' or 'message to xyz'."
    ),
)

chat = model.start_chat(history=history)

def ai_query(query):
    global chat, history
    response = chat.send_message(query)

    history = []
    for h in chat.history:
        history.append({
            "role": h.role,
            "parts": [p.text for p in h.parts if hasattr(p, "text")]
        })

    # Save to file
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

    res = response.text
    if 'message to' in res.lower():
        res = res.split(':',1)[1].strip()
            
    print(res)
    return res



def reset_memory():
    global chat, history
    history = []
    chat = model.start_chat(history=[])
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    print("🧹 Memory cleared!")
    speak("Memory Cleared, Sir")

