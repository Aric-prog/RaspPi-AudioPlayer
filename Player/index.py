import pafy
import audio_stream_player as asp
import threading
import finished_listener as fl
import os

# Short :
# https://www.youtube.com/watch?v=Z9LlEIDJL08
# https://www.youtube.com/watch?v=ahiM5XgtvMg
# https://www.youtube.com/watch?v=h41KFaq4UXc
# Main cli thread, will keep running until program is terminated

player = asp.audio_stream_player()
listener = threading.Thread(name = 'daemon_listener', target = fl.start_listen, args = (player,))
listener.setDaemon(1)
listener.start()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

os.environ["VLC_VERBOSE"] = str("-1")
while(True):
    print("Playing : ", player.playing_title)
    url = input("Command : ")
    if(url == "skip"):
        player.stop()
        clear()
    elif(url == "terminate"):
        break
    else:
        player.queue_audio(url)
        clear()
