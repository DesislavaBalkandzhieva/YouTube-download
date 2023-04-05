from pathlib import Path
from pytube import Playlist

class PlaylistDownloader:
    def __init__(self, link, save_path):
        self.link = link
        self.save_path = save_path

    def download(self):
        youtube_object = Playlist(self.link)
        print(len(youtube_object.video_urls))

        try:
            for video in youtube_object.videos:
                audio_stream = video.streams.get_highest_resolution()
                audio_stream.download(output_path=self.save_path)
        except:
            print("An error has occurred")
        print("Download is completed successfully")
