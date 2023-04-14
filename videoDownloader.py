from pathlib import Path
from pytube import YouTube
from downloader import Downloader

class VideoDownloader(Downloader):
    def __init__(self, link, save_path, res):
        super().__init__(link, save_path)
        self.res = res

    def download(self):
        youtube_object = self.get_youtube_object()
        if self.res == "1":
            stream = youtube_object.streams.get_highest_resolution()
        elif self.res == "2":
            stream = youtube_object.streams.get_lowest_resolution()
        elif self.res == "3":
            stream = self.get_stream_with_resolution(youtube_object, "360p")
        elif self.res == "4":
            stream = self.get_stream_with_resolution(youtube_object, "720p")
        else:
            print("Invalid resolution option")
            return

        try:
            self.download_stream(stream)
        except:
            print("An error has occurred")
        finally:
            print("Video download is completed successfully")

    def get_stream_with_resolution(self, youtube_object, resolution):
        available_streams = youtube_object.streams.filter(progressive=True, file_extension='mp4')
        for stream in available_streams:
            if stream.resolution == resolution:
                return stream
        return None
