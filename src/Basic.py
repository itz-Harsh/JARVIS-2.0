import datetime
import os
import json
import time
import pyautogui
import subprocess
import webbrowser
from voice_io import speak, voice


# in 12 hours


website = {
    'instagram': 'https://www.instagram.com',
    'facebook': 'https://www.facebook.com',
    'twitter': 'https://www.x.com',
    'linkedin': 'https://www.linkedin.com',
    'whatsapp': 'https://web.whatsapp.com',
    'amazon' : 'https://www.amazon.in',
    'flipkart': 'https://www.flipkart.com',
    'youtube' : 'https://www.youtube.com'
}



def open_website(query):
    for key, value in website.items():
        if key in query:
            speak(f'Opening {key}...')
            webbrowser.open(value)
            
            
def wish():
    hour = datetime.datetime.now().hour
    # wish me if its my birthday
    if datetime.datetime.now().month == 12 and datetime.datetime.now().day == 13:
        speak("Ohhhh Its Your Birthday Sir \nHappy Birthday Sir \nHave a Great Day")
    if hour < 12:
        speak("Good Morning Sir! \nHope you are having a great day")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir! \nHope you are having a great day")
    else:
        speak("Good Evening Sir! \nHope you are doing well")

def search(query):
    query = query.split('search' , 1)[0].strip()
    print(query)
    
    if 'youtube' in query:
        query = query.replace('on youtube', '')
        speak(f'Searching {query} on YouTube .....')
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
    else:
        if 'on google' in query:
            query = query.replace('on google', "").strip()
        speak(f'Searching {query} on Google ....')
        webbrowser.open(f'https://www.google.com/search?q='+query)
        


def open_app(app_name):
    if app_name in website:
        open_website(app_name)
    else:
        try:
            os.startfile(app_name)
            speak(f'Opening {app_name}')
        except Exception as e:
            pyautogui.hotkey('win', 's')
            time.sleep(0.8)
            pyautogui.typewrite(app_name)
            time.sleep(0.5)
            pyautogui.press('enter')
            speak(f'Opening {app_name}')






def close_app(app_name):
    ps_script = '''
        Get-Process | Select-Object Id, ProcessName, Description | Sort-Object ProcessName | ConvertTo-Json
    '''
    
    result = subprocess.check_output(
        ["powershell", "-Command", ps_script],
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    processes = json.loads(result)
    
    task_list = []
    
    for p in processes:
        task_list.append({
            "pid": p.get("Id"),
            "name": p.get("ProcessName"),
            "description": p.get("Description")
        })
    
    os.system(f'taskkill /im {app_name}.exe /f')
        
    try:
        for proc in task_list:
            if isinstance(proc["description"], str) and app_name in proc["description"].lower():
                os.system(f'taskkill /F /im {proc["name"]}.exe' or 'taskkill /F /pid {proc["pid"]}')
                # print(f"PID: {proc['pid']}, Name: {proc['name']}, Description: {proc['description'].lower()}")
                speak(f'Closing {app_name}')
                break
    except Exception as e:
        speak(f'The app is already closed')
        print(f"Error closing {app_name}: {e}")
        


