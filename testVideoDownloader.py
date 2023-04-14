import unittest
from videoDownloader import VideoDownloader

class TestVideoDownloader(unittest.TestCase):
    
    def test_download_highest_resolution(self):
        downloader = VideoDownloader("https://www.youtube.com/watch?v=ozv4q2ov3Mk", ".", "1")
        downloader.download()
    
    def test_download_lowest_resolution(self):
        downloader = VideoDownloader("https://www.youtube.com/watch?v=ozv4q2ov3Mk", ".", "2")
        downloader.download()
    
    def test_download_360p_resolution(self):
        downloader = VideoDownloader("https://www.youtube.com/watch?v=ozv4q2ov3Mk", ".", "3")
        downloader.download()
    
    def test_download_720p_resolution(self):
        downloader = VideoDownloader("https://www.youtube.com/watch?v=ozv4q2ov3Mk", ".", "4")
        downloader.download()

if __name__ == '__main__':
    unittest.main()
