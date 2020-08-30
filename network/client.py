import socket
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),os.pardir)))
from config.constants import HEADER,PORT,FORMAT,DISCONNECT_MESSAGE

SERVER = '192.168.1.169'
# This should be replaced by a static ip from raspberry
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    client.send(msg.encode(FORMAT))

connected = True
while connected:
    try:
        output = input("Input text :")
        send(output)
        if output == DISCONNECT_MESSAGE:
            connected = False
    except ConnectionResetError:
        print("Connection was reset, terminating program.")
        connected = False

print("Program terminated. Thank you for connecting.")
