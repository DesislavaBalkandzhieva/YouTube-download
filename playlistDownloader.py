from pathlib import Path
from pytube import Playlist
from downloader import Downloader
import logger
import logging

logger = logging.getLogger(__name__)
class PlaylistDownloader(Downloader):
    def download(self):
        youtube_object = self.get_playlist_object()
        logger.info ('The number of videos in the playlist are:')
        logger.info(len(youtube_object.video_urls))

        try:
            for video in youtube_object.videos:
                audio_stream = video.streams.get_highest_resolution()
                self.download_stream(audio_stream)
        except IOError:
            logger.error("An error has occurred")
        finally:
            logger.info("Download is completed successfully")
