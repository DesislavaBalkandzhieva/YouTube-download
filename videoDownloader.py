from pathlib import Path
from pytube import YouTube

class VideoDownloader:
    def __init__(self, link, save_path, res):
        self.link = link
        self.save_path = save_path
        self.res=res

    def download(self):
        youtube_object = YouTube(self.link)
        if self.res=="1":
            stream = youtube_object.streams.get_highest_resolution()
        if self.res=="2":
            stream = youtube_object.streams.get_lowest_resolution()
        if self.res=="3":
            stream=youtube_object.filter(res="360p")
        if self.res=="4":
            stream=youtube_object.filter(res="720p")
        try:
            if self.save_path == "":
                self.save_path = Path.cwd()
            stream.download(self.save_path) 
        except:
            print("An error has occurred")
        print("Video download is completed successfully")

