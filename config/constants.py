import os
from pathlib import Path

PORT = 5050
HEADER = 1024
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '-DISCONNECT'
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
COMM_LIST = ["-p","-play", "-skip","-q","-queue", DISCONNECT_MESSAGE]

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
