from config.constants import COMM_LIST
from googleapiclient.discovery import build
from config.constants import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, API_KEY,clear

import command_parser as cp
class command_handler:
    def __init__(self, asp):
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey= API_KEY)
        self.youtube_search = self.youtube.search()
        self.parser = cp.command_parser()
        self.player = asp

    def skip(self):
        clear()
        self.player.stop()
    
    def show_queue(self):
        if(bool(self.player.get_queue())):
            clear()
            for e,i in reversed(list(enumerate(self.player.get_queue()))):
                print(e + 1, i[0])
        else:
            print("Queue is empty")

    def play(self, arg):
        if not self.parser.is_url(arg):
            self.player.queue_audio(self.search(arg))
        else:
            self.player.queue_audio(arg)

    # Only sterile inputs goes here
    def accept_command(self, command):
        syntax, arg = self.parser.separate(command)
        if(syntax == "p" or syntax == "play"):
            self.play(arg)
        elif(syntax == "skip"):
            self.skip()
        elif(syntax == "q" or syntax == "queue"):
            self.show_queue()
        else:
            print("Invalid command")
    
    def search(self, query):
        # Search using the provided query, returns the video ID
        search_result = self.youtube_search.list(
            q = query,
            part = 'id',
            maxResults = 1,
            type = 'video'
        ).execute()
        return search_result['items'][0]['id']['videoId']


