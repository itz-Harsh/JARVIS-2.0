# Entrence of project
from voice_io import speak , voice
import Basic as b , system as s , smart as sm , multimedia as multi , Brain as ai , keyControl
 


if __name__ == '__main__':
    b.wish()
    running= True 
    while running:
        
        try:
            query = voice()
            
            if 'open' in query:
                app_name = query.replace('open ', '')
                b.open_app(app_name)

            elif 'close' in query:
                app_name = query.replace('close ', '')
                b.close_app(app_name)
            
            elif 'wish me' in query:
                b.wish()
    
    #  KeyControl.py calls
            elif 'select all' in query or 'select everything' in query:
                speak(keyControl.selectall())
                
            elif 'copy' in query:
                speak(keyControl.copy())
                
            elif 'paste' in query:
                speak(keyControl.paste())
                
            elif 'cut' in query:
                speak(keyControl.cut())
                
            elif 'undo' in query:
                speak(keyControl.undo())
                
            elif 'redo' in query:
                speak(keyControl.redo())
            
            elif 'save as' in query:
                speak(keyControl.saveas())
                       
            elif 'save' in query:
                speak(keyControl.save())
                
            elif 'new file' in query or 'new document' in query:
                speak(keyControl.newfile())            
    
            elif 'delete' in query or 'remove' in query:
                speak(keyControl.delete())
            
            elif 'find' in query or 'search' in query:
                speak(keyControl.find())
                
            elif 'switch window' in query or 'switch application' in query:
                speak(keyControl.switchwindow())
            
           
    

    
    
    
    
    
    
         
    #    smart.py calls
            if 'wikipedia' in query:
                sm.wikipedia_summary(query)
            
            elif 'weather' in query:
                sm.weather(query)
                
            elif 'translate' in query:
                try:
                    query = query.replace('translate' , '')
                    translation = sm.translate(query)
                    speak(translation)
                except Exception as e:
                    print(e)
                    speak('Sorry, I am unable to translate at the moment.')
                    
                    
            elif 'write' in query or 'write a code' in query:
                sm.write_to_file(query)

            elif 'send message' in query or 'send whatsapp message' in query:
                sm.send_whatsapp_message(query)

    #    Multimedia.py calls
        
            elif 'take screenshot' in query:
                multi.screenshot()
                
            elif 'show screenshot' in query:
                multi.show_screenshot()
                
            elif 'play music' in query or 'play song' in query:
                multi.music_control('play')
                
            elif 'stop music' in query or 'stop song' in query or 'pause music' in query or 'pause song' in query:
                multi.music_control('pause')
            
        
    #   System.py calls      
        
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
                usage = s.system_usage(query)
                speak(usage)



    #    Close Program

            elif 'exit' in query or 'quit' in query or 'goodbye' in query or 'stop listening' in query:
                speak('Okay Sir, I am going offline now. Goodbye!')
                running= False
            
    #    Ai StandBy
            elif 'reset memory' in query or 'clear memory' in query:
                ai.reset_memory()
            
            
            else:
                res =ai.ai_query(query)
                speak(res)
        except Exception as e:
            pass