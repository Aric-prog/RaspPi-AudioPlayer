import time
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def start_listen(asp):
    # Function will check every second if the song ended or not, if finished, play next
    while True:
        time.sleep(1)
        if(not asp.is_playing()):
            if(asp.get_queue()):
                clear()
                asp.play_audio(asp.get_next_url())
                print("Playing : ", asp.playing_title, end = "\nCommand : ")