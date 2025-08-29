# Entrence of project
from voice_io import speak, voice
from Basic import wish, search, open_app, close_app
from keyControl import (
    selectall,
    copy,
    paste,
    cut,
    undo,
    redo,
    save,
    newfile,
    delete,
    find,
    switchwindow,
    saveas,
)
from Brain import reset_memory, ai_query
from system import (
    volume_control,
    brightness_control,
    date_time,
    shutdown,
    restart,
    signoff,
    system_usage,
)
from multimedia import play, show_savefile, show_screenshot, music_control, screenshot
from smart import wikipedia_summary, translate, write_to_file, send_message, weather


def handle_key_control(query: str):
    """Handle short keyboard/control commands and return an optional spoken response."""
    if 'select all' in query or 'select everything' in query:
        return selectall()
    if 'copy' == query or query.startswith('copy '):
        return copy()
    if 'paste' == query or query.startswith('paste '):
        return paste()
    if 'cut' == query or query.startswith('cut '):
        return cut()
    if 'undo' in query:
        return undo()
    if 'redo' in query:
        return redo()
    if 'save as' in query:
        # try to pull filename from the phrase, otherwise ask
        if ' as ' in query:
            return saveas(query=query)
        else:
            fname = voice()
            return saveas(query=fname)
    if 'save' in query and 'save as' not in query:
        return save()
    if 'new file' in query or 'new document' in query:
        return newfile()
    if 'delete' in query or 'remove' in query:
        return delete()
    if 'find' in query and 'search' not in query:
        return find()
    if 'switch window' in query or 'switch application' in query:
        return switchwindow()
    return None


def main_loop():
    wish()
    running = True

    speak('Jarvis is online. Say help to hear available commands.')

    while running:
        try:
            query = voice()
            if not query:
                continue

            # query from voice() is already lowercased in voice_io; keep local var
            q = query

            # quick global commands
            if 'reset memory' in q or 'clear memory' in q:
                reset_memory()
                continue

            if 'help' == q or 'what can you do' in q:
                speak('I can open and close apps, search the web, control system volume and brightness, take screenshots, play music, send messages, and more. Say commands like open notepad, take screenshot, or send message to John.')
                continue

            # Basic commands
            if q.startswith('open '):
                app_name = q.replace('open ', '', 1).strip()
                open_app(app_name)
                continue

            if q.startswith('close '):
                app_name = q.replace('close ', '', 1).strip()
                close_app(app_name)
                continue

            if 'wish me' in q:
                wish()
                continue

            # Key control commands
            kc_resp = handle_key_control(q)
            if kc_resp is not None:
                try:
                    speak(kc_resp)
                except Exception:
                    # fallback: print
                    print(kc_resp)
                continue

            # Smart module commands
            if 'wikipedia' in q:
                wikipedia_summary(q)
                continue

            if 'weather in' in q:
                weather(q)
                continue

            if q.startswith('translate'):
                try:
                    text = q.replace('translate', '', 1).strip()
                    translation = translate(text)
                    speak(translation)
                except Exception as e:
                    print('Translate error:', e)
                    speak('Sorry, I am unable to translate at the moment.')
                continue

            if q.startswith('write') or 'write a code' in q:
                write_to_file(q)
                continue

            if q.startswith('send message') or q.startswith('send whatsapp message') or q.startswith('send message to'):
                send_message(q)
                continue

            # Multimedia
            if 'take screenshot' in q:
                screenshot()
                continue

            if 'show screenshot' in q or 'show screenshots' in q:
                show_screenshot()
                continue

            if q.startswith('play'):
                # normalize phrase and play
                play(q)
                continue

            if any(x in q for x in ['stop music', 'stop song', 'pause music', 'pause song']):
                music_control('pause')
                continue

            if 'show savefile' in q or 'show saved file' in q:
                show_savefile()
                continue

            # System
            if 'volume' in q:
                volume_control(q)
                continue

            if 'brightness' in q:
                brightness_control(q)
                continue

            if 'time' in q or 'date' in q:
                dtime = date_time()
                speak(f'The current date and time is {dtime}')
                continue

            if 'shutdown the system' in q or 'shut down the system' in q:
                shutdown()
                continue

            if 'restart the system' in q or 'reboot the system' in q:
                restart()
                continue

            if 'sign out' in q or 'log off' in q:
                signoff()
                continue

            if any(x in q for x in ['cpu usage', 'system usage', 'how much memory is used', 'ram']):
                usage = system_usage(q)
                speak(usage)
                continue

            # Exit
            if q in ('exit', 'quit', 'goodbye', 'stop listening'):
                speak('Okay Sir, I am going offline now. Goodbye!')
                running = False
                continue

            # Fallback to AI
            res = ai_query(q)
            try:
                if res:
                    speak(res)
            except Exception:
                print('AI response:', res)

        except Exception as e:
            # catch and log but keep the assistant running
            print('Main loop error:', e)
            speak('I encountered an error but I am still running.')


if __name__ == '__main__':
    main_loop()