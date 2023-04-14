from downloader import Downloader
from pathlib import Path
from pytube import YouTube

class AudioDownloader(Downloader):
    def download(self):
        youtube_object = self.get_youtube_object()
        stream = youtube_object.streams.get_audio_only()
        audio_file = stream.download(output_path=self.save_path)
        audio_path = Path(audio_file)
        output_path = audio_path.with_suffix('.mp3')
        audio_path.rename(output_path)
        print("Audio download is completed successfully")
