import downloader
from pathlib import Path
from pytube import YouTube

class AudioDownloader(Downloader):
    def download(self):
    youtube_object = self.get_youtube_object()
    stream = youtube_object.streams.get_audio_only()
    self.download_stream(stream)



