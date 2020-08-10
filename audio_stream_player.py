import pafy
import vlc
pf = 0
def __init__(pafy):
    pf = pafy

def get_audio(link):
    audio = pafy.new(link).getbestaudio()
    return audio.url

def play_audio(url):
    vlc_obj = vlc.Instance()



get_audio("https://www.youtube.com/watch?v=h41KFaq4UXc")
