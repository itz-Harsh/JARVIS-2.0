import wikipedia
import requests
import pyautogui
import time
from voice_io import speak , voice
import json
from langdetect import detect
from Basic import open_app



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

def write_to_file():
    writing= True
    try:
        # write to notepad
        speak('Opening Notepad to write ')
        open_app('notepad')
        time.sleep(1)
        speak('Please say what you want to write')
        while writing:
            text = voice()
            if 'stop writing' in text.lower():
                speak('Stopping writing')
                writing = False
            else:
                pyautogui.typewrite(text)
                pyautogui.press('enter')
                
            
    except Exception as e:
        speak('Could not open Notepad. Please try again.')
        print(f'Error opening Notepad: {e}')
        writing = False        
        
        
