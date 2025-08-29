import wikipedia
import requests
import pyautogui , pyperclip , keyControl
import time 
from voice_io import speak , voice
import json , os
from langdetect import detect
from Basic import open_app
from dotenv import load_dotenv
from Brain import ai_query
import pywhatkit as whatsapp

load_dotenv()

global json_data;
json_data = {}

with open('assets/lang.json', 'r') as file:
    json_data = json.load(file)




def wikipedia_summary(query):
    query = query.replace('wikipedia', '')
    speak(f'Searching {query} on Wikipedia ....')
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f'The query "{query}" is ambiguous. Please be more specific.')
    except wikipedia.exceptions.PageError:
        speak(f'No page found for "{query}". Please try a different query.')
    except Exception as e:
        speak('An error occurred while searching Wikipedia.')


def translate(query):
    parts = query.rsplit(' in ', 1)
    text = parts[0].strip()
    langto = parts[1].strip().lower()
    
    src = detect(text)
    
    trg = json_data.get(langto)
    print(f'Translating "{text}" to {langto}\n {trg}..')

    url = f"https://lingva.ml/api/v1/{src}/{trg}/{text}"
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Translation API error: {res.status_code}")
    speak(f'Translating {text} in {langto} ')
    respone = res.json().get("translation", "No translation found.")
    # print(respone)
    return respone

def write_to_file( command ):
    # speak('Opening Notepad for writing.')
    writing= True
    try:
        open_app('notepad')
        time.sleep(1)
        keyControl.newfile()
        if 'write what i say' in command:
            speak('Please say what you want to write')
            while writing:
                text = voice()
                if 'stop writing' in text.lower():
                    speak('Stopping writing')
                    writing = False
                else:
                    pyautogui.typewrite(text)
                    pyautogui.press('enter')
        else:
            res = ai_query(command)
            lang = detect(res)
            if lang != 'en':
                pyperclip.copy(res)
                pyautogui.hotkey("ctrl", "v")
            else:
                pyautogui.typewrite(res) 
            speak('Writing completed, Sir')
            return 

                  
            
    except Exception as e:
        speak('Could not open Notepad. Please try again.')
        print(f'Error opening Notepad: {e}')
        writing = False        




        
        
def weather(query):
    city = query.split('weather in', 1)[1].strip()
    apikey = os.getenv('weather-api')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    respone = requests.get(f"{base_url}appid={apikey}&q={city}&units=metric")
    res  = respone.json()
    if res["cod"] != "404":
        result = {
            "In" : res["name"],
            "temperature is" : f'{int(res["main"]["temp"])} Degrees Celsius',
            "and it probably" : res["weather"][0]["description"],
        }
        for key , value in result.items():
            speak(f'{key} {value}')
    else:
        speak(f'''Sorry I Couldn't found City''')




VCF_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "Contacts.vcf")
VCF_PATH = os.path.abspath(VCF_PATH)

VCF_FILE = os.path.join("assets", "Contacts.vcf")
def load_contacts():
    contacts = {}
    current_name = None
    current_numbers = []

    if not os.path.exists(VCF_FILE):
        print("❌ Contacts file not found.")
        return {}

    with open(VCF_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()

            if line.startswith("FN:"):  # Full name
                current_name = line[3:]
                current_numbers = []

            elif line.startswith("TEL"):  # TEL;CELL , TEL;WORK , etc.
                number = line.split(":")[-1]
                current_numbers.append(number)

            elif line.startswith("END:VCARD"):
                if current_name:
                    contacts[current_name] = current_numbers
                current_name = None
                current_numbers = []

    return contacts

def find_contact(name, contacts):
    """Search contact by name (case-insensitive)."""
    for contact_name, numbers in contacts.items():
        if name.lower() in contact_name.lower():
            # if only one number → return it
            if len(numbers) == 1:
                return numbers[0]
            # if multiple numbers → prefer the last (PREF is usually last in vcf)
            return numbers[-1]
    return None




contacts = load_contacts()
def send_message(message):
    msg = message.replace('send message to', '').strip()
    name = msg.split(' ',1)[0].strip()
    msg = msg.split(' ',1)[1].strip()
    if name in contacts:
        number = find_contact(name, contacts)
        whatsapp.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        print(f"Message sent to {name.title()} ({number})")
    else:
        print("Contact not found!")
        
