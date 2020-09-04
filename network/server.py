import socket
import threading
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),os.pardir)))
from config.constants import HEADER,PORT,FORMAT,DISCONNECT_MESSAGE,clear

import command_parser as cp
import command_handler as ch
import audio_stream_player as asp
import finished_listener as fl

LOCALIP = '192.168.1.128'
ADDR = (LOCALIP,PORT)

clear()

# Short : https://www.youtube.com/watch?v=Z9LlEIDJL08
# Long  : https://www.youtube.com/watch?v=ahiM5XgtvMg
# https://www.youtube.com/watch?v=h41KFaq4UXc

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

player = asp.audio_stream_player()
comm_handler = ch.command_handler(player)

observer = threading.Thread(name = 'daemon_listener', target = fl.start_listen, args = (player,comm_handler,))
observer.setDaemon(1)
observer.start()


def handle_client(conn,addr):
    print("New Connection " ,addr, "connected.")
    connected = True
    try:
        while connected:
            msg = conn.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            comm_handler.accept_command(msg)
            comm_handler.show_queue()
            print(addr,", queued : ", msg)
            print("Currently playing : ", player.playing_title)
    except ConnectionResetError:
        print("Connection error", addr ,", client disconnected")
    conn.close()

def listen_client():
    server.listen()
    print("Server is listening on ",LOCALIP)
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn,addr))
        thread.setDaemon(1)
        thread.start()
        print("Active connections :", threading.activeCount() - 2)

print("STARTING SERVER")
listen_client()

