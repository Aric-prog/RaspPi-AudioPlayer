import time
import os
from config.constants import clear

def start_listen(asp):
    # Function will check every second if the song ended or not, if finished, play next
    while True:
        time.sleep(1)
        if(not asp.is_playing()):
            if(asp.get_queue()):
                clear()
                asp.play_audio(asp.get_next_url())
                print("Currently playing : ", asp.playing_title)