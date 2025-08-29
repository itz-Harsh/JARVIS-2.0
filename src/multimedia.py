import  os , pyautogui , datetime , time
from voice_io import speak
from Basic import open_app


def play( src ):
    speak(f'Yes Sir, Playing {src} on spotify')
    src = src.split('play' , 1)[1].strip()
    open_app('spotify')
    time.sleep(5)
    pyautogui.hotkey('ctrl' , 'k')
    time.sleep(1)
    pyautogui.write(src)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')



def show_savefile():
    speak('Yes Sir, this are the savefiles')
    path = os.path.dirname(os.path.abspath(__file__)).replace('src', 'assets\\savefile')
    os.startfile(path)



def show_screenshot():
    speak('Yes Sir, this are the screenshots')
    dir = os.path.dirname(os.path.abspath(__file__)).replace('src', 'assets\\screenshots')
    os.startfile(dir)    
    
    


def music_control(command):
    if 'play' or 'stop' in command or 'pause' in command:
        pyautogui.press('playpause')
    else:
        speak('Please say play or stop or pause')
        

def screenshot():
    img = pyautogui.screenshot()
    try:
        name = datetime.datetime.now().strftime("%Y-%m-%d %I-%M %p")
        img.save(f"assets/screenshots/{name}.png")
        speak('Screenshot taken')
    
    except Exception as e:
        speak('Could not take screenshot. Please try again.')
        print(f'Error taking screenshot: {e}')

