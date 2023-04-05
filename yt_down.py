from pathlib import Path
from pytube import YouTube

class VideoDownloader:
    def __init__(self, link, save_path):
        self.link = link
        self.save_path = save_path

    def download(self):
        youtube_object = YouTube(self.link)
        stream = youtube_object.streams.get_highest_resolution()
        try:
            if self.save_path == "":
                self.save_path = Path.cwd()
            stream.download(self.save_path) 
        except:
            print("An error has occurred")
        print("Video download is completed successfully")

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

operation = input('1. Video \n2. Audio\n')
link = input("Enter the YouTube video URL: ")
print("Enter the destination (leave blank for current directory)")
save_path = input(">> ")
if operation == "1":
    downloader = VideoDownloader(link, save_path)
elif operation == "2":
    downloader = AudioDownloader(link, save_path)
else:
    print("Invalid input")
    exit(1)

downloader.download()
