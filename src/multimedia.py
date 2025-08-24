import os , pyautogui
from voice_io import speak


def show_screenshot():
    speak('Yes Sir, this are the screenshots that are taken till now')
    dir = os.path.dirname(os.path.abspath(__file__)).replace('src', 'assets\\screenshots')
    os.startfile(dir)    
    

def music_control(command):
    if 'play' or 'stop' in command or 'pause' in command:
        pyautogui.press('playpause')
    else:
        speak('Please say play or stop or pause')
        

# music_control('play')
music_control('pause')