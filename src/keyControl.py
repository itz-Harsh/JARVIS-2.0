import pyautogui
from voice_io import speak , voice
import time


def selectall():
    pyautogui.hotkey('ctrl', 'a')
    return 'all files are selected'

def copy():
    pyautogui.hotkey('ctrl', 'c')
    return 'copied to clipboard'

def paste():
    pyautogui.hotkey('ctrl', 'v')
    return 'done pasting'

def cut():
    pyautogui.hotkey('ctrl', 'x')
    return 'cut to clipboard'

def undo():
    pyautogui.hotkey('ctrl', 'z')
    return 'undone'

def redo():
    pyautogui.hotkey('ctrl', 'y')
    return 'redone'

def save():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.press('enter')
    return 'file saved'

def newfile():
    pyautogui.hotkey('ctrl', 'n')
    return 'new file created'

def delete():
    pyautogui.press('delete')
    return 'deleted'

def find():
    pyautogui.hotkey('ctrl', 'f')
    return 'find window opened'


def switchwindow():
    pyautogui.hotkey('alt', 'tab')
    return 'switched window'    

def saveas():
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(3)
    speak('Please provide the file name')
    name = voice()
    pyautogui.typewrite(name)
    time.sleep(2)
    pyautogui.press('enter')
    return 'save as window opened'

