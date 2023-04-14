from pathlib import Path
from pytube import Playlist
from downloader import Downloader

class PlaylistDownloader(Downloader):
    def download(self):
        youtube_object = self.get_playlist_object()
        print ('The number of videos in the playlist are:')
        print(len(youtube_object.video_urls))

        try:
            for video in youtube_object.videos:
                audio_stream = video.streams.filter(only_audio=True).first()
                self.download_stream(audio_stream, file_extension='mp3')
        except IOError:
            print("An error has occurred")
        finally:
            print("Download is completed successfully")