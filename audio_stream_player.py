import pafy
import os
import time
from config.constants import ROOT_DIR

os.add_dll_directory(os.path.join(ROOT_DIR, "config"))
import vlc

class audio_stream_player:
    def __init__(self):
        self.playing_title = ""
        self.url_queue = []
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
    
    def get_audio_info(self,url):
        audio = pafy.new(url)
        audio_url = audio.getbestaudio().url
        audio_title = audio.title
        return audio_title, audio_url

    def play_audio(self,url):
        try:
            audio_title ,audio_url = self.get_audio_info(url)
            self.playing_title = audio_title
            self.player.set_media(self.instance.media_new(audio_url))
            self.player.play()
        except ValueError:
            print("Not a valid link")

    def play_next(self):
        next_info = self.url_queue.pop(0)
        self.playing_title = next_info[0]
        audio_url = next_info[1]
        self.player.set_media(self.instance.media_new(audio_url))
        self.player.play()

    def queue_audio(self,url):
        title,url = self.get_audio_info(url)
        temp = [title,url]
        self.url_queue.append(temp)

    def is_playing(self):
        return self.player.is_playing()

    def get_next_url(self):
        return self.url_queue.pop(0)[1]

    def get_queue(self):
        return self.url_queue
    
    def stop(self):
        self.playing_title = ""
        self.player.stop()
    # Create a thread everytime a new song is played
    # Exit condition :
    # - Song is done
    # - Song is skipped



