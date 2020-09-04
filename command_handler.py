from audio_stream_player import audio_stream_player
class command_handler:
    def __init__(self, asp):
        self.player = asp

    def skip(self):
        self.player.stop()
    
    def queue(self, url):
        self.player.queue_audio(url)

    