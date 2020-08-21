import time
import audio_stream_player

def start_listen(asp):
    try:
        while True:
            time.sleep(1)
            asp.is_playing()
    except:
        print("Thread ended unexpectedly")


    