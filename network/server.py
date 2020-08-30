import socket
import threading
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),os.pardir)))
from config.constants import HEADER,PORT,FORMAT,DISCONNECT_MESSAGE,clear

import audio_stream_player as asp
import finished_listener as fl

LOCALIP = socket.gethostbyname(socket.gethostname())
ADDR = (LOCALIP,PORT)

clear()

# Short : https://www.youtube.com/watch?v=Z9LlEIDJL08
# Long  : https://www.youtube.com/watch?v=ahiM5XgtvMg
# https://www.youtube.com/watch?v=h41KFaq4UXc

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

player = asp.audio_stream_player()
listener = threading.Thread(name = 'daemon_listener', target = fl.start_listen, args = (player,))
listener.setDaemon(1)
listener.start()

def player_command(url):
    if(url == "skip"):
        player.stop()
        clear()
    elif(url == "terminate"):
        running = False
    elif(url == DISCONNECT_MESSAGE):
        pass
    else:
        player.queue_audio(url)
        clear()

def handle_client(conn,addr):
    print("New Connection " ,addr, "connected.")
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        player_command(msg)
        print(addr,", queued : ", msg)
        print("Currently playing : ", player.playing_title)
    conn.close()

def listen_client():
    server.listen()
    print(f"Server is listening on {LOCALIP}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn,addr))
        thread.setDaemon(1)
        thread.start()
        print("Active connections :", threading.activeCount() - 2)

print("STARTING SERVER")
listen_client()

