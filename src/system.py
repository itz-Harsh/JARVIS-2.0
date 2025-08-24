import datetime
import calendar
import os , time , psutil , pyautogui
from voice_io import speak , voice
from Basic import wish



# control the pc brightness

def volume_control(command):
    if 'volume up' in command:
        pyautogui.press('volumeup')
        speak('Volume Up')
    elif 'volume down' in command:
        pyautogui.press('volumedown')
        speak('Volume Down')
    elif 'mute' in command:
        pyautogui.press('volumemute')
        speak('Unmuted')
    else:
        speak('Please say volume up or volume down or mute')


def brightness_control(command):
    if 'brightness up' in command:
        pyautogui.press('brightnessup')
        speak('Brightness Up')
    elif 'brightness down' in command:
        pyautogui.press('brightnessdown')
        speak('Brightness Down')
    else:
        speak('Please say brightness up or brightness down')


def date_time():
    now = datetime.datetime.now()
    
    res = now.strftime("%Y-%m-%d %I:%M %p")
    day = calendar.day_name[now.weekday()]
    print(f'The current date and time is {res}\n and the day is {day}')
    return res

def shutdown():
    speak("Shutting down the system")
    time.sleep(1)
    os.system("shutdown /s /t 1")

def restart():
    speak("Restarting the system")
    time.sleep(1)
    os.system("shutdown /r /t 1")

def signoff():
    speak("See You Sir") 
    os.system("rundll32.exe user32.dll,LockWorkStation")



def system_usage( query ):
    if 'cpu' in query.lower():
        cpu = psutil.cpu_percent()
        return f'Sir, CPU is at {int(cpu)} percent'
    elif 'memory' in query or 'ram' in query.lower():
        ram = psutil.virtual_memory().percent
        return f'Sir, RAM is at {int(ram)} percent'

