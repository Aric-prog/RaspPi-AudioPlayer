import socket
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),os.pardir)))
from config.constants import HEADER, PORT, FORMAT, DISCONNECT_MESSAGE, COMM_LIST
import command_parser as cp

SERVER = '192.168.1.169'
# This should be replaced by a static ip from raspberry
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

parser = cp.command_parser()

def send(msg):
    client.send(msg.encode(FORMAT))

connected = True
while connected:
    try:
        output = input("Input text :")
        if output == DISCONNECT_MESSAGE:
            connected = False
        elif(parser()):
            send(output)
    except ConnectionResetError:
        print("Connection was reset, terminating program.")
        connected = False

print("Program terminated. Thank you for connecting.")
