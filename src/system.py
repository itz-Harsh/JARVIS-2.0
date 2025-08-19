import datetime
import calendar
import os , time , pyautogui
from voice_io import speak , voice
from Basic import wish



# control the pc brightness

# def brightness_control():
    

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


 
    
signoff()
