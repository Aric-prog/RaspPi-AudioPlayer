import time
import os
from config.constants import clear

def start_listen(asp,ch):
    # Function will check every second if the song ended or not, if finished, play next
    # Not good but fuck it
    
    while True:
        time.sleep(1)
        if(not asp.is_playing()):
            if(bool(asp.get_queue())):
                clear()
                asp.play_next()
                ch.show_queue()
                print("Currently playing : ", asp.playing_title)