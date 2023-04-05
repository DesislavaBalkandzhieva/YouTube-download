
from pathlib import Path
from pytube import YouTube

class AudioDownloader:
    def __init__(self, link, save_path):
        self.link = link
        self.save_path = save_path

    def download(self):
        youtube_object = YouTube(self.link)
        stream = youtube_object.streams.get_audio_only()
        try:
            if self.save_path == "":
                self.save_path = Path.cwd()
            stream.download(self.save_path) 
        except:
            print("An error has occurred")
        print("Audio download is completed successfully")