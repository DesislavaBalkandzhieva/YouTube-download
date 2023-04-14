import unittest
from audioDownloader import AudioDownloader
import os

class TestAudioDownloader(unittest.TestCase):
    def test_download(self):
        downloader = AudioDownloader('https://www.youtube.com/watch?v=7wtfhZwyrcc', '.')

        downloader.download()
        
        expected_output_path = './Rick Astley - Never Gonna Give You Up (Video).mp3'
        self.assertTrue(os.path.exists(expected_output_path))
        self.assertEqual(os.path.splitext(expected_output_path)[1], '.mp3')

if __name__ == '__main__':
    unittest.main()
