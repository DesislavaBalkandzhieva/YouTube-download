from abc import ABC, abstractmethod
from pytube import YouTube
from pytube import Playlist
from pathlib import Path


class Downloader(ABC):
    def __init__(self, link, save_path):
        self.link = link
        self.save_path = save_path

    @abstractmethod
    def download(self):
        pass

    def get_youtube_object(self):
        return YouTube(self.link)

    def get_playlist_object(self):
        return Playlist(self.link)

    def download_stream(self, stream):
        try:
            if self.save_path == "":
                self.save_path = Path.cwd()
            stream.download(self.save_path) 
        except IOError:
            print("An error has occurred")
        finally:
            print("Download is completed successfully")