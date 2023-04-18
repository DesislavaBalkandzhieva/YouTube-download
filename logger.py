import logging
from pytube import YouTube

logging.basicConfig(filename='downloader.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Logger:
    def __init__(self, link, save_path):
        self.link = link
        self.save_path = save_path
        
    def get_youtube_object(self):
        logging.debug('Getting YouTube object for link: {}'.format(self.link))
        return YouTube(self.link)

    def download_stream(self, stream, file_extension='mp4'):
        logging.debug('Downloading stream with resolution: {}'.format(stream.resolution))
        file_name = '{}.{}'.format(stream.default_filename[:-4], file_extension)
        output_path = os.path.join(self.save_path, file_name)
        stream.download(output_path)
        logging.info('Downloaded stream to path: {}'.format(output_path))