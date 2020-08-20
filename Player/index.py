import pafy
import audio_stream_player as asp

# Main cli thread, will keep running until program is terminated
player = asp.audio_stream_player()
while(True):
    url = input("Enter link : ")
    player.queue_audio(url)
