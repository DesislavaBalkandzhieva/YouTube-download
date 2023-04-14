import unittest
from playlistDownloader import PlaylistDownloader

class TestPlaylistDownloader(unittest.TestCase):
    def test_download(self):
        downloader = PlaylistDownloader('https://www.youtube.com/playlist?list=PLfQpXSmyWfaOsgahe-OimmmGYm_9WfDf2', '.')
        downloader.download()

if __name__ == '__main__':
    unittest.main()