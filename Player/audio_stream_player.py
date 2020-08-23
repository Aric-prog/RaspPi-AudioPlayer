import pafy
import os
import time

os.add_dll_directory('C:\Program Files\VideoLAN\VLC')
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
        return audio_url ,audio_title

    def play_audio(self,url):
        try:
            audio_url ,audio_title = self.get_audio_info(url)
            self.playing_title = audio_title
            self.player.set_media(self.instance.media_new(audio_url))
            self.player.play()  
        except ValueError:
            print("Not a valid link")

    def queue_audio(self,url):
        if(not self.player.is_playing()):
            self.play_audio(url)
        else:
            # Add to list
            self.url_queue.append(url)

    def is_playing(self):
        return self.player.is_playing()

    def get_next_url(self):
        return self.url_queue.pop()

    def get_queue(self):
        return self.url_queue
    
    def stop(self):
        self.playing_title = ""
        self.player.stop()
    # Create a thread everytime a new song is played
    # Exit condition :
    # - Song is done
    # - Song is skipped



