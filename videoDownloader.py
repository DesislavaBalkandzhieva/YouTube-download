from pathlib import Path
from pytube import YouTube
import downloader
import logging
import logger

logger = logging.getLogger(__name__)

class VideoDownloader(downloader.Downloader):
    def __init__(self, link, save_path, res):
        super().__init__(link, save_path)
        self.res = res

    def download(self):
        youtube_object = self.get_youtube_object()
        switcher = {
            "1": youtube_object.streams.get_highest_resolution,
            "2": youtube_object.streams.get_lowest_resolution,
            "3": lambda: self.get_stream_with_resolution(youtube_object, "360p"),
            "4": lambda: self.get_stream_with_resolution(youtube_object, "720p")
        }
        stream = switcher.get(self.res, lambda: None)()
        if stream is None:
            logger.error("Invalid resolution option")
            return

        try:
            self.download_stream(stream)
        except:
            logger.error("An error has occurred")
        finally:
            logger.info("Video download is completed successfully")

    def get_stream_with_resolution(self, youtube_object, resolution):
        available_streams = youtube_object.streams.filter(progressive=True, file_extension='mp4')
        for stream in available_streams:
            if stream.resolution == resolution:
                return stream
        return None
    
    def download_stream(self, stream, file_extension='mp4'):
        logger.debug('Downloading stream with resolution: {}'.format(stream.resolution))
        file_name = '{}.{}'.format(stream.default_filename[:-4], file_extension)
        output_path = Path(self.save_path) / file_name
        stream.download(output_path)
        logger.info('Downloaded stream to path: {}'.format(output_path))
