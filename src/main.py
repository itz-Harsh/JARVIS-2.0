# Entrence of project
from voice_io import speak , voice
import Basic as b , system as s , smart as sm , multimedia as multi
 


if __name__ == '__main__':
    b.wish()
    while True:
        query = voice().lower()
        
        # logic building for tasks
        
        if 'wikipedia' in query:
            sm.wikipedia_summary(query)
            
        elif 'open' in query:
            app_name = query.replace('open ', '')
            b.open_app(app_name)
            
        elif 'search' in query:
            sm.search(query)
            
        elif 'translate' in query:
            try:
                translation = sm.translate(query)
                speak(translation)
            except Exception as e:
                print(e)
                speak('Sorry, I am unable to translate at the moment.')
                
        elif 'write a note' in query or 'write to file' in query:
            sm.write_to_file()
            
        elif 'screenshot' in query or 'take screenshot' in query:
            multi.screenshot()
            
        elif 'show screenshots' in query or 'show screenshot' in query:
            multi.show_screenshot()
            
        elif 'play music' in query or 'play song' in query:
            multi.music_control('play')
            
        elif 'stop music' in query or 'stop song' in query or 'pause music' in query or 'pause song' in query:
            multi.music_control('pause')
            
        elif 'volume' in query:
            s.volume_control(query)
            
        elif 'brightness' in query:
            s.brightness_control(query)
            
        elif 'time' in query or 'date' in query:
            datetime = s.date_time()
            speak(f'The current date and time is {datetime}')
            
        elif 'shutdown the system' in query or 'shut down the system' in query:
            s.shutdown()
            
        elif 'restart the system' in query or 'reboot the system' in query:
            s.restart()
            
        elif 'sign out' in query or 'log off' in query:
            s.signoff()
            
        elif 'cpu usage' in query or 'system usage' in query or 'how much memory is used' in query:
            cpu , memory = s.system_usage()
            speak(f'The CPU is at {cpu} percent and Memory is at {memory} percent')
        
        elif 'exit' in query or 'quit' in query or 'goodbye' in query or 'stop listening' in query:
            speak('Okay Sir, I am going offline now. Goodbye!')