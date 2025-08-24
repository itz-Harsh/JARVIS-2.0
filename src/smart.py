import wikipedia
import requests
import pyautogui , pyperclip
import time
from voice_io import speak , voice
import json , os
from langdetect import detect
from Basic import open_app
from dotenv import load_dotenv
from Brain import ai_query

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
    print(respone)
    return respone

def write_to_file( command ):
    writing= True
    try:
        # new page in notepad
        open_app('notepad')
        speak('Opening Notepad')
        time.sleep(1)
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

                  
            
    except Exception as e:
        speak('Could not open Notepad. Please try again.')
        print(f'Error opening Notepad: {e}')
        writing = False        
        
        
def weather(query):
    city = query.replace('weather of', '').strip()
    
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


while True:
    cmd =voice()
    if 'write' in cmd: 
        write_to_file(cmd)
        